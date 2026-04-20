#!/usr/bin/env python3
"""Capture a durable runtime-visibility snapshot with lightweight git metadata."""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
from datetime import datetime, timezone

if __package__ in {None, ""}:
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from tooling.codex import runtime_visibility


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Capture a selected-lane runtime-visibility snapshot so audit/intervention "
            "work can carry final-runtime truth with commit metadata."
        )
    )
    parser.add_argument("repo_root", nargs="?", default=".")
    parser.add_argument("--label", required=True, help="Short label for this snapshot.")
    parser.add_argument("--output", required=True, help="Output JSON path.")
    parser.add_argument(
        "--notes",
        help="Optional note describing why this snapshot was captured.",
    )
    return parser.parse_args()


def git_output(repo_root: pathlib.Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError:
        return None
    return result.stdout.strip()


def build_snapshot(repo_root: pathlib.Path, label: str, notes: str | None) -> dict:
    report = runtime_visibility.build_report(repo_root)
    basis_commit = git_output(repo_root, "rev-parse", "HEAD")
    branch = git_output(repo_root, "rev-parse", "--abbrev-ref", "HEAD")
    dirty = bool(git_output(repo_root, "status", "--short"))
    return {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "label": label,
        "basis_commit": basis_commit,
        "branch": branch,
        "dirty_worktree": dirty,
        "notes": notes,
        "runtime_visibility_report": report,
    }


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path(args.repo_root).resolve()
    output_path = pathlib.Path(args.output)
    if not output_path.is_absolute():
        output_path = (repo_root / output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = build_snapshot(repo_root, args.label, args.notes)
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
