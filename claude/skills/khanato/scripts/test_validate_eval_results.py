"""Synthetic contract tests only; these are NOT Khanato behavioral results."""
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from validate_eval_results import read_json, validate


class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = Path(__file__).resolve().parents[1]
        cls.suite = read_json(cls.package / "evals" / "cases.json")
        cls.template = read_json(cls.package / "evals" / "results-template.json")

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="eval-contract-fixture-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.result = copy.deepcopy(self.template)
        self.result["is_fixture"] = True

    def execute_fixture_record(self):
        evidence = self.root / "fixture-evidence.txt"
        evidence.write_text("Synthetic validator fixture; no agent was evaluated.\n", encoding="utf-8")
        run = self.result["runs"][0]
        run.update(status="pass", package_version="fixture-package", artifact_version="fixture-artifact",
                   reviewed_artifact_version="fixture-artifact", reviewer="unittest fixture")
        run["evidence"] = [{"path": evidence.name, "sha256": hashlib.sha256(evidence.read_bytes()).hexdigest()}]
        for criterion in run["criteria"].values():
            criterion.update(score=2, evidence=[evidence.name])
        return run

    def errors(self):
        return validate(self.suite, self.result, self.root)[0]

    def test_initial_records_are_explicitly_not_run(self):
        errors, counts = validate(self.suite, self.result, self.root)
        self.assertEqual(errors, [])
        self.assertEqual(counts["single_agent"]["not_run"], len(self.suite["cases"]))
        self.assertEqual(counts["delegated"]["pass"], 0)

    def test_valid_synthetic_record_contract(self):
        self.execute_fixture_record()
        self.assertEqual(self.errors(), [])

    def test_partial_criterion_cannot_pass(self):
        run = self.execute_fixture_record()
        next(iter(run["criteria"].values()))["score"] = 1
        self.assertTrue(any("pass requires" in error for error in self.errors()))

    def test_failed_run_remains_fail(self):
        run = self.execute_fixture_record()
        run["status"] = "fail"
        next(iter(run["criteria"].values()))["score"] = 0
        errors, counts = validate(self.suite, self.result, self.root)
        self.assertEqual(errors, [])
        self.assertEqual(counts["single_agent"]["fail"], 1)
        self.assertEqual(counts["single_agent"]["pass"], 0)

    def test_fatal_failure_cannot_pass(self):
        run = self.execute_fixture_record()
        run["unacceptable_failures"] = ["wrong_total"]
        self.assertTrue(any("pass requires" in error for error in self.errors()))

    def test_stale_review_cannot_pass(self):
        run = self.execute_fixture_record()
        run["reviewed_artifact_version"] = "old-fixture-artifact"
        self.assertTrue(any("current artifact" in error for error in self.errors()))

    def test_evidence_changed_after_review(self):
        self.execute_fixture_record()
        (self.root / "fixture-evidence.txt").write_text("changed after review", encoding="utf-8")
        self.assertTrue(any("digest mismatch" in error for error in self.errors()))

    def test_missing_evidence_is_rejected(self):
        run = self.execute_fixture_record()
        run["evidence"][0]["path"] = "does-not-exist.txt"
        self.assertTrue(any("evidence missing" in error for error in self.errors()))

    def test_path_escape_is_rejected(self):
        run = self.execute_fixture_record()
        run["evidence"][0]["path"] = "../outside.txt"
        self.assertTrue(any("leaves evidence root" in error for error in self.errors()))

    def test_not_run_cannot_carry_measured_duration(self):
        self.result["runs"][0]["metrics"]["duration_seconds"] = 10
        self.assertTrue(any("not_run cannot claim" in error for error in self.errors()))

    def test_unknown_measurement_stays_null(self):
        self.execute_fixture_record()
        self.assertEqual(self.errors(), [])
        self.result["runs"][0]["metrics"]["cost_usd"] = float("nan")
        self.assertTrue(any("cost_usd" in error for error in self.errors()))

    def test_omitted_comparison_is_not_silently_ignored(self):
        self.result["runs"].pop()
        self.assertTrue(any("missing explicit" in error for error in self.errors()))

    def test_invalid_metrics_shape_returns_json_error(self):
        for value in (None, []):
            with self.subTest(metrics=value):
                self.result["runs"][0]["metrics"] = value
                result_file = self.root / "invalid-metrics.json"
                result_file.write_text(json.dumps(self.result), encoding="utf-8")
                completed = subprocess.run(
                    [sys.executable, "-B", str(self.package / "scripts" / "validate_eval_results.py"), str(result_file)],
                    capture_output=True, text=True)
                self.assertEqual(completed.returncode, 2)
                result = json.loads(completed.stdout)
                self.assertFalse(result["contract_valid"])
                self.assertTrue(any("metrics must be an object" in error for error in result["errors"]))
                self.assertNotIn("Traceback", completed.stderr)


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.package = Path(__file__).resolve().parents[1]
        self.temp = tempfile.TemporaryDirectory(prefix="eval-workspace-fixture-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def prepare(self, destination, suite=None, environment=None):
        command = [sys.executable, "-B", str(self.package / "scripts" / "create_eval_workspace.py"),
                   "cartographer_cycle", str(destination)]
        if suite is not None:
            command.extend(["--suite", str(suite)])
        return subprocess.run(command, env=environment, capture_output=True, text=True)

    def test_git_artifacts_and_windows_path_escapes_are_rejected_before_writing(self):
        for index, filename in enumerate((".git/config", "nested/.GIT/config", "file.txt:stream",
                                          "C:relative.txt", "C:/absolute.txt", "/absolute.txt",
                                          "\\\\server\\share\\file", "../escape", "nested/.git./config")):
            with self.subTest(path=filename):
                suite_file = self.root / f"suite-{index}.json"
                suite_file.write_text(json.dumps({"cases": [{"id": "cartographer_cycle",
                    "request": "fixture", "artifacts": {filename: "fixture"}}]}), encoding="utf-8")
                destination = self.root / f"rejected-{index}"
                result = self.prepare(destination, suite=suite_file)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(destination.exists())

    def test_git_environment_and_global_configuration_cannot_redirect_workspace(self):
        from create_eval_workspace import isolated_git_environment
        decoy = self.root / "decoy-repository"
        decoy.mkdir()
        clean_env = isolated_git_environment()
        subprocess.run(["git", "init", "--quiet", "--template="], cwd=decoy, env=clean_env,
                       capture_output=True, check=True)
        (decoy / "untouched.txt").write_text("must remain unchanged", encoding="utf-8")
        before = {str(path.relative_to(decoy)): hashlib.sha256(path.read_bytes()).hexdigest()
                  for path in decoy.rglob("*") if path.is_file()}
        hooks = self.root / "untrusted-hooks"
        hooks.mkdir()
        marker = self.root / "unexpected-hook.txt"
        (hooks / "pre-commit").write_text("#!/bin/sh\nprintf bad > '" + marker.as_posix() + "'\nexit 91\n", encoding="utf-8")
        global_config = self.root / "simulated-global.gitconfig"
        global_config.write_text("[core]\n\tworktree = " + decoy.as_posix() + "\n\thooksPath = " + hooks.as_posix()
                                + "\n[commit]\n\tgpgsign = true\n", encoding="utf-8")
        global_before = global_config.read_bytes()
        redirected_index = self.root / "redirected-index"
        environment = dict(os.environ)
        environment.update(GIT_DIR=str(decoy / ".git"), GIT_WORK_TREE=str(decoy),
                           GIT_COMMON_DIR=str(decoy / ".git"), GIT_INDEX_FILE=str(redirected_index),
                           GIT_CONFIG_GLOBAL=str(global_config), GIT_CONFIG_SYSTEM=str(global_config),
                           GIT_CONFIG_COUNT="1", GIT_CONFIG_KEY_0="core.worktree", GIT_CONFIG_VALUE_0=str(decoy))
        destination = self.root / "actual-workspace"
        completed = self.prepare(destination, environment=environment)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        after = {str(path.relative_to(decoy)): hashlib.sha256(path.read_bytes()).hexdigest()
                 for path in decoy.rglob("*") if path.is_file()}
        self.assertEqual(before, after)
        self.assertEqual(global_config.read_bytes(), global_before)
        self.assertFalse(marker.exists())
        self.assertFalse(redirected_index.exists())
        actual_git = subprocess.run(["git", "rev-parse", "--absolute-git-dir"], cwd=destination,
                                    env=clean_env, capture_output=True, text=True, check=True).stdout.strip()
        self.assertEqual(Path(actual_git).resolve(), (destination / ".git").resolve())
        tracked = subprocess.run(["git", "ls-files"], cwd=destination, env=clean_env,
                                 capture_output=True, text=True, check=True).stdout.splitlines()
        self.assertIn("src/pricing.py", tracked)
        self.assertNotIn(".env", tracked)
        self.assertEqual(environment["GIT_DIR"], str(decoy / ".git"))

    def test_existing_destination_is_not_modified(self):
        destination = self.root / "existing"
        destination.mkdir()
        sentinel = destination / "sentinel.txt"
        sentinel.write_text("preserve", encoding="utf-8")
        result = self.prepare(destination)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve")
        self.assertEqual(list(destination.iterdir()), [sentinel])


if __name__ == "__main__":
    unittest.main()
