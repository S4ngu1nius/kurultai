#!/usr/bin/env python3
"""Materialize synthetic case artifacts in a new local workspace; run no agent."""
import argparse
import json
import os
from pathlib import Path, PureWindowsPath
import subprocess


def artifact_path(filename):
    """Accept portable relative files, excluding Git internals and Windows aliases."""
    if not isinstance(filename, str) or not filename or ":" in filename:
        raise ValueError("unsafe artifact path")
    relative = PureWindowsPath(filename)
    if relative.drive or relative.root or not relative.parts:
        raise ValueError("unsafe artifact path")
    for part in relative.parts:
        if (part in (".", "..") or part.casefold() == ".git"
                or part != part.rstrip(" .") or any(ord(char) < 32 for char in part)):
            raise ValueError("unsafe artifact path")
    return Path(*relative.parts)


def isolated_git_environment():
    """Configure only Git child processes; never modify the caller's environment."""
    environment = {key: value for key, value in os.environ.items()
                   if not key.upper().startswith("GIT_")}
    environment.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_SYSTEM=os.devnull,
                       GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_COUNT="0")
    return environment


def initialize_repository(destination):
    environment = isolated_git_environment()

    def git(*values):
        return subprocess.run(
            ["git", "-c", "user.name=Khanato Eval Fixture", "-c", "user.email=fixture@invalid.example",
             "-c", "commit.gpgsign=false", "-c", "core.hooksPath=.git/hooks",
             "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-c", "maintenance.auto=false", *values],
            cwd=destination, env=environment, check=True, capture_output=True, text=True)

    git("init", "--quiet", "--template=")
    git_dir = Path(git("rev-parse", "--absolute-git-dir").stdout.strip()).resolve()
    work_tree = Path(git("rev-parse", "--show-toplevel").stdout.strip()).resolve()
    if (git_dir != (destination / ".git").resolve() or not git_dir.is_relative_to(destination)
            or work_tree != destination):
        raise RuntimeError("Git resolved outside the new evaluation workspace; add/commit refused")
    git("add", "--", ".")
    git("commit", "--quiet", "-m", "Synthetic evaluation baseline")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_id")
    parser.add_argument("destination", type=Path)
    parser.add_argument("--suite", type=Path, default=Path(__file__).resolve().parents[1] / "evals" / "cases.json")
    args = parser.parse_args()
    suite = json.loads(args.suite.read_text(encoding="utf-8"))
    case = next((item for item in suite["cases"] if item["id"] == args.case_id), None)
    if case is None:
        parser.error("unknown case")
    destination = args.destination.resolve()
    if destination.exists():
        parser.error("destination must not exist; create a fresh workspace for every run")
    files = case["artifacts"]
    if not isinstance(files, dict):
        parser.error("artifacts must be an object")
    checked_files = []
    try:
        for filename, content in files.items():
            relative = artifact_path(filename)
            candidate = (destination / relative).resolve()
            if not candidate.is_relative_to(destination) or candidate == destination:
                raise ValueError("unsafe artifact path")
            if not isinstance(content, str):
                raise ValueError("artifact content must be text")
            checked_files.append((relative, content))
    except ValueError as exc:
        parser.error(str(exc))
    destination.mkdir(parents=True)
    for relative, content in checked_files:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8", newline="\n")
    if case.get("initialize_git"):
        initialize_repository(destination)
    print(json.dumps({"case_id": case["id"], "workspace": str(destination), "synthetic": True,
                      "request": case["request"], "status": "prepared_not_run"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
