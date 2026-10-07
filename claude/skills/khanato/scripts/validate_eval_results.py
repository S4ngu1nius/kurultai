#!/usr/bin/env python3
"""Validate evaluation records and evidence integrity; never grade agent behavior."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def validate(suite, results, evidence_root):
    errors = []
    summary = {mode: {state: 0 for state in ("pass", "fail", "not_run")}
               for mode in ("single_agent", "delegated")}
    cases = {case["id"]: case for case in suite["cases"]}
    root = Path(evidence_root).resolve()
    if results.get("suite_version") != suite["version"]:
        errors.append("suite_version does not match")
    if not isinstance(results.get("is_fixture"), bool):
        errors.append("is_fixture must be explicit")
    records = results.get("runs")
    if not isinstance(records, list):
        return ["runs must be a list"], summary
    seen = set()
    for index, run in enumerate(records):
        label = f"runs[{index}]"
        if not isinstance(run, dict):
            errors.append(f"{label}: expected object")
            continue
        case_id, mode = run.get("case_id"), run.get("mode")
        status = run.get("status")
        if case_id not in cases or mode not in summary or status not in ("pass", "fail", "not_run"):
            errors.append(f"{label}: unknown case, mode or status")
            continue
        key = (case_id, mode, run.get("run_id"))
        if not isinstance(run.get("run_id"), str) or not run["run_id"] or key in seen:
            errors.append(f"{label}: missing or duplicate run_id within case/mode")
        seen.add(key)
        summary[mode][status] += 1
        expected_criteria = {criterion["id"] for criterion in cases[case_id]["criteria"]}
        criteria = run.get("criteria", {})
        if not isinstance(criteria, dict) or set(criteria) != expected_criteria:
            errors.append(f"{label}: criteria do not match suite")
            continue
        metrics = run.get("metrics", {})
        if not isinstance(metrics, dict):
            errors.append(f"{label}: metrics must be an object")
            metrics = {}
        for name in ("duration_seconds", "cost_usd", "tokens"):
            value = metrics.get(name)
            if name not in metrics or (value is not None and (
                    isinstance(value, bool) or not isinstance(value, (float, int))
                    or not math.isfinite(value) or value < 0)):
                errors.append(f"{label}: {name} must be null or a finite nonnegative number")
        failures = run.get("unacceptable_failures")
        allowed_failures = {failure["id"] for failure in cases[case_id]["unacceptable_failures"]}
        if not isinstance(failures, list) or any(f not in allowed_failures for f in failures):
            errors.append(f"{label}: unknown unacceptable failure")
        evidence = run.get("evidence")
        if not isinstance(evidence, list):
            errors.append(f"{label}: evidence must be a list")
            continue
        evidence_paths = set()
        for item in evidence:
            if not isinstance(item, dict) or not isinstance(item.get("path"), str):
                errors.append(f"{label}: invalid evidence item")
                continue
            relative = Path(item["path"])
            target = (root / relative).resolve()
            if relative.is_absolute() or not target.is_relative_to(root) or target == root:
                errors.append(f"{label}: evidence path leaves evidence root")
                continue
            if item["path"] in evidence_paths:
                errors.append(f"{label}: duplicate evidence path")
            evidence_paths.add(item["path"])
            if not target.is_file():
                errors.append(f"{label}: evidence missing: {item['path']}")
            elif hashlib.sha256(target.read_bytes()).hexdigest() != item.get("sha256"):
                errors.append(f"{label}: evidence digest mismatch: {item['path']}")
        scores = []
        for criterion_id, assessment in criteria.items():
            if not isinstance(assessment, dict):
                errors.append(f"{label}: invalid assessment {criterion_id}")
                continue
            score = assessment.get("score")
            refs = assessment.get("evidence", [])
            if not isinstance(refs, list) or any(ref not in evidence_paths for ref in refs):
                errors.append(f"{label}: unknown evidence reference in {criterion_id}")
            if status == "not_run":
                if score is not None or refs:
                    errors.append(f"{label}: not_run cannot have scored criteria")
            else:
                if isinstance(score, bool) or not isinstance(score, int) or score not in (0, 1, 2):
                    errors.append(f"{label}: executed criteria require integer scores 0..2")
                else:
                    scores.append(score)
                if not refs:
                    errors.append(f"{label}: executed criterion lacks evidence: {criterion_id}")
        if status == "not_run":
            if evidence or failures or any(metrics.get(name) is not None for name in metrics):
                errors.append(f"{label}: not_run cannot claim execution evidence, failures or metrics")
            if any(run.get(name) is not None for name in (
                    "package_version", "artifact_version", "reviewed_artifact_version", "reviewer")):
                errors.append(f"{label}: not_run execution metadata must be null")
        else:
            for name in ("package_version", "artifact_version", "reviewed_artifact_version", "reviewer"):
                if not isinstance(run.get(name), str) or not run[name].strip():
                    errors.append(f"{label}: executed run requires {name}")
            if status == "pass":
                if failures or len(scores) != len(expected_criteria) or any(score != 2 for score in scores):
                    errors.append(f"{label}: pass requires all criteria satisfied and no unacceptable failure")
                if run.get("artifact_version") != run.get("reviewed_artifact_version"):
                    errors.append(f"{label}: review does not cover current artifact version")
            elif scores and all(score == 2 for score in scores) and not failures:
                errors.append(f"{label}: fail needs an unsatisfied criterion or unacceptable failure")
    covered = {(key[0], key[1]) for key in seen}
    for case_id in cases:
        for mode in summary:
            if (case_id, mode) not in covered:
                errors.append(f"missing explicit result or not_run: {case_id}/{mode}")
    return errors, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", type=Path)
    parser.add_argument("--suite", type=Path, default=Path(__file__).resolve().parents[1] / "evals" / "cases.json")
    parser.add_argument("--evidence-root", type=Path, help="Default: results directory")
    args = parser.parse_args()
    try:
        results = read_json(args.results)
        errors, summary = validate(read_json(args.suite), results, args.evidence_root or args.results.parent)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"contract_valid": False, "errors": [str(exc)]}, ensure_ascii=False))
        return 2
    print(json.dumps({
        "contract_valid": not errors,
        "is_fixture": results.get("is_fixture"),
        "counts": summary,
        "errors": errors,
        "meaning": "Contract and evidence integrity only; reported scores require an actual evaluator. Fixtures are not Khanato performance evidence."
    }, ensure_ascii=False, indent=2))
    return 2 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
