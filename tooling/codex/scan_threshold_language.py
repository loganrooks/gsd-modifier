#!/usr/bin/env python3
"""Scan docs/specs/prompts/reviews for threshold or deficit-oriented framing residue."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


DEFAULT_EXTENSIONS = {".md", ".txt"}

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    (
        "threshold_language",
        re.compile(
            r"\b(adequate|sufficient|good enough|well enough|passes review|pass/fail|ready/not ready|works well)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "deficit_oriented_pseudopositive",
        re.compile(
            r"\b(not lacking|no longer missing|no longer best described as|not the real problem|not merely deficient|not mainly|not primarily)\b",
            re.IGNORECASE,
        ),
    ),
]


def iter_files(root: pathlib.Path) -> list[pathlib.Path]:
    if root.is_file():
        return [root]
    paths: list[pathlib.Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in DEFAULT_EXTENSIONS or any(
            part.endswith(".md.txt") for part in [path.name]
        ):
            paths.append(path)
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan markdown/text artifacts for threshold or deficit-oriented framing."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    args = parser.parse_args()

    findings: list[tuple[str, int, str, str]] = []
    for raw in args.paths:
        root = pathlib.Path(raw)
        for path in iter_files(root):
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for line_no, line in enumerate(text.splitlines(), start=1):
                for category, pattern in PATTERNS:
                    if pattern.search(line):
                        findings.append((str(path), line_no, category, line.rstrip()))

    if not findings:
        print("No threshold-language residue found.")
        return 0

    current_path = None
    for path, line_no, category, line in findings:
        if path != current_path:
            if current_path is not None:
                print()
            print(path)
            current_path = path
        print(f"  {line_no}: [{category}] {line}")

    print()
    print(f"Findings: {len(findings)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
