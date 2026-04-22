#!/usr/bin/env python3
"""Repair and verify repo-local gsd-sdk runtime executability when possible."""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import stat
import subprocess
from typing import Any


SH_PATH = "/bin/sh"
SDK_NAME = "gsd-sdk"
RECOVERABLE_STATUSES = {"healthy", "repaired"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify the repo-local gsd-sdk runtime and repair the known executable-bit failure when possible."
    )
    parser.add_argument("--output")
    parser.add_argument("--pretty", action="store_true")
    parser.add_argument("--no-repair", action="store_true")
    return parser.parse_args()


def write_json(payload: dict[str, Any], output: pathlib.Path | None, pretty: bool = False) -> None:
    text = json.dumps(payload, indent=2 if pretty else None, sort_keys=pretty) + "\n"
    if output is None:
        print(text, end="")
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")


def run_shell(command: str, env: dict[str, str]) -> dict[str, Any]:
    completed = subprocess.run(
        [SH_PATH, "-c", command],
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def path_candidates(env: dict[str, str]) -> list[pathlib.Path]:
    candidates: list[pathlib.Path] = []
    seen: set[str] = set()
    for entry in env.get("PATH", "").split(os.pathsep):
        if not entry:
            continue
        candidate = pathlib.Path(entry).expanduser() / SDK_NAME
        key = str(candidate)
        if key in seen:
            continue
        seen.add(key)
        candidates.append(candidate)
    return candidates


def npm_prefix_probe(env: dict[str, str]) -> list[dict[str, Any]]:
    attempts: list[dict[str, Any]] = []
    for command in (["npm", "prefix", "-g"], ["npm", "config", "get", "prefix"]):
        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                env=env,
                check=False,
            )
            attempts.append(
                {
                    "command": command,
                    "returncode": completed.returncode,
                    "stdout": completed.stdout.strip(),
                    "stderr": completed.stderr.strip(),
                }
            )
            if completed.returncode == 0 and completed.stdout.strip():
                break
        except FileNotFoundError as exc:
            attempts.append(
                {
                    "command": command,
                    "returncode": None,
                    "stdout": "",
                    "stderr": str(exc),
                }
            )
    return attempts


def npm_prefix_candidates(env: dict[str, str]) -> tuple[list[pathlib.Path], list[dict[str, Any]]]:
    attempts = npm_prefix_probe(env)
    candidates: list[pathlib.Path] = []
    for attempt in attempts:
        if attempt["returncode"] != 0:
            continue
        prefix = attempt["stdout"]
        if not prefix:
            continue
        candidates.append(pathlib.Path(prefix).expanduser() / "bin" / SDK_NAME)
        break
    return candidates, attempts


def inspect_candidate(path: pathlib.Path, source: str) -> dict[str, Any]:
    record: dict[str, Any] = {
        "path": str(path),
        "source": source,
        "exists": path.exists(),
        "is_symlink": path.is_symlink(),
    }
    if not path.exists():
        return record

    record["path_executable"] = os.access(path, os.X_OK)
    target = pathlib.Path(os.path.realpath(path))
    record["realpath"] = str(target)
    record["target_exists"] = target.exists()
    if not target.exists():
        return record

    mode = target.stat().st_mode & 0o777
    record["target_mode"] = oct(mode)
    record["target_executable"] = os.access(target, os.X_OK)
    first_line = None
    try:
        lines = target.read_text(encoding="utf-8", errors="replace").splitlines()
        if lines:
            first_line = lines[0]
    except OSError:
        first_line = None
    record["first_line"] = first_line
    record["has_shebang"] = bool(first_line and first_line.startswith("#!"))
    return record


def discover_candidates(env: dict[str, str]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    path_records = [inspect_candidate(path, "path") for path in path_candidates(env)]
    prefix_paths, npm_attempts = npm_prefix_candidates(env)
    seen = {record["path"] for record in path_records}
    for path in prefix_paths:
        key = str(path)
        if key in seen:
            continue
        path_records.append(inspect_candidate(path, "npm-prefix"))
        seen.add(key)
    return path_records, npm_attempts


def repair_record(record: dict[str, Any]) -> dict[str, Any] | None:
    if not record.get("target_exists"):
        return None
    if record.get("target_executable"):
        return None
    if not record.get("has_shebang"):
        return None

    target = pathlib.Path(record["realpath"])
    before_mode = target.stat().st_mode
    after_mode = before_mode | stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
    if after_mode != before_mode:
        target.chmod(after_mode)

    return {
        "action": "chmod_target_executable",
        "path": record["path"],
        "realpath": record["realpath"],
        "before_mode": oct(before_mode & 0o777),
        "after_mode": oct(after_mode & 0o777),
    }


def build_report(env: dict[str, str] | None = None, *, allow_repair: bool = True) -> dict[str, Any]:
    runtime_env = dict(os.environ if env is None else env)
    initial_command_v = run_shell(f"command -v {SDK_NAME}", runtime_env)
    initial_exec = run_shell(f"{SDK_NAME} --version", runtime_env)
    candidates, npm_attempts = discover_candidates(runtime_env)
    existing_candidates = [record for record in candidates if record.get("exists")]
    repair_action = None

    if allow_repair and not (
        initial_command_v["returncode"] == 0 and initial_exec["returncode"] == 0
    ):
        for record in existing_candidates:
            repair_action = repair_record(record)
            if repair_action is not None:
                break

    final_command_v = run_shell(f"command -v {SDK_NAME}", runtime_env)
    final_exec = run_shell(f"{SDK_NAME} --version", runtime_env)

    if final_command_v["returncode"] == 0 and final_exec["returncode"] == 0:
        status = "repaired" if repair_action else "healthy"
    elif not existing_candidates:
        status = "unresolved_no_candidate"
    elif any(record["source"] == "npm-prefix" for record in existing_candidates):
        status = "unresolved_off_path_or_nonrepairable"
    else:
        status = "unresolved"

    return {
        "status": status,
        "repair_attempted": allow_repair,
        "repair_action": repair_action,
        "initial_command_v": initial_command_v,
        "initial_exec": initial_exec,
        "final_command_v": final_command_v,
        "final_exec": final_exec,
        "candidates": candidates,
        "npm_prefix_attempts": npm_attempts,
    }


def main() -> int:
    args = parse_args()
    report = build_report(allow_repair=not args.no_repair)
    output_path = pathlib.Path(args.output) if args.output else None
    write_json(report, output_path, pretty=args.pretty)
    return 0 if report["status"] in RECOVERABLE_STATUSES else 1


if __name__ == "__main__":
    raise SystemExit(main())
