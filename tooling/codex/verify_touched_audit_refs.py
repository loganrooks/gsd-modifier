#!/usr/bin/env python3

"""Verify markdown references for touched audit workspaces."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
AUDITS_ROOT = REPO_ROOT / ".planning" / "audits"
REFMAP = REPO_ROOT / "tooling" / "codex" / "audit_refmap.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run audit_refmap verify against touched audit workspaces, or all audit "
            "workspaces when requested."
        )
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Verify every immediate workspace under .planning/audits.",
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Use staged paths only instead of git status porcelain.",
    )
    parser.add_argument(
        "--output",
        help="Write the aggregate markdown report here.",
    )
    return parser.parse_args()


def repo_relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def list_all_audit_roots() -> list[Path]:
    if not AUDITS_ROOT.exists():
        return []
    return sorted(path for path in AUDITS_ROOT.iterdir() if path.is_dir())


def parse_changed_paths(staged: bool) -> list[Path]:
    if staged:
        command = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"]
        result = subprocess.run(
            command,
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return [REPO_ROOT / line for line in result.stdout.splitlines() if line.strip()]

    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    paths: list[Path] = []
    for raw in result.stdout.splitlines():
        if not raw:
            continue
        payload = raw[3:]
        if " -> " in payload:
            left, right = payload.split(" -> ", 1)
            paths.append(REPO_ROOT / left)
            paths.append(REPO_ROOT / right)
        else:
            paths.append(REPO_ROOT / payload)
    return paths


def touched_audit_roots(staged: bool) -> list[Path]:
    roots: dict[str, Path] = {}
    for path in parse_changed_paths(staged):
        try:
            relative = path.resolve().relative_to(REPO_ROOT)
        except ValueError:
            continue
        parts = relative.parts
        if len(parts) < 3 or parts[0] != ".planning" or parts[1] != "audits":
            continue
        root = REPO_ROOT / parts[0] / parts[1] / parts[2]
        roots[repo_relative(root)] = root
    return [roots[key] for key in sorted(roots)]


def verify_root(root: Path) -> tuple[int, str]:
    result = subprocess.run(
        [sys.executable, str(REFMAP), "verify", str(root)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.strip()


def main() -> int:
    args = parse_args()
    roots = list_all_audit_roots() if args.all else touched_audit_roots(args.staged)

    lines = [
        "# Touched Audit Ref Verification",
        "",
        f"- Mode: `{'all' if args.all else ('staged' if args.staged else 'status')}`",
        f"- Audit roots checked: `{len(roots)}`",
        "",
    ]

    if not roots:
        lines.append("- no audit roots to verify")
        output_text = "\n".join(lines) + "\n"
        if args.output:
            Path(args.output).write_text(output_text, encoding="utf-8")
        else:
            sys.stdout.write(output_text)
        return 0

    overall_exit = 0
    for root in roots:
        exit_code, report = verify_root(root)
        if exit_code != 0:
            overall_exit = exit_code
        lines.append(f"## {repo_relative(root)}")
        lines.append("")
        lines.append(f"- status: `{'ok' if exit_code == 0 else 'failed'}`")
        lines.append("")
        if report:
            lines.append(report)
            lines.append("")

    output_text = "\n".join(lines) + "\n"
    if args.output:
        Path(args.output).write_text(output_text, encoding="utf-8")
    else:
        sys.stdout.write(output_text)
    return overall_exit


if __name__ == "__main__":
    raise SystemExit(main())
