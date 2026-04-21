#!/usr/bin/env python3
"""Shared portable-GSD overlay contract helpers."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
from typing import Any


DEFAULT_COMPACT_PROMPT_FILE = "tooling/compact-prompts/project.md"
LOCAL_COMPACT_PROMPT_SELECTOR = ".codex.local/compact-prompt.txt"
OVERLAY_REL_PATH = "tooling/portable-gsd/overlay"
OVERLAY_MANIFEST_REL_PATH = "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json"
VALID_MODES = {"add", "overwrite"}

QUALITY_REASONING = {
    "gsd-planner": "xhigh",
    "gsd-roadmapper": "xhigh",
    "gsd-phase-researcher": "xhigh",
    "gsd-project-researcher": "xhigh",
    "gsd-ui-researcher": "xhigh",
    "gsd-executor": "high",
    "gsd-debugger": "high",
    "gsd-doc-writer": "high",
    "gsd-research-synthesizer": "high",
    "gsd-codebase-mapper": "high",
    "gsd-verifier": "high",
    "gsd-plan-checker": "high",
    "gsd-integration-checker": "high",
    "gsd-nyquist-auditor": "high",
    "gsd-ui-checker": "high",
    "gsd-ui-auditor": "high",
    "gsd-doc-verifier": "high",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Portable GSD overlay contract helper.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate-manifest", help="Validate overlay add/overwrite contract.")
    validate.add_argument("repo_root", nargs="?", default=".")
    validate.add_argument("--output")
    validate.add_argument("--pretty", action="store_true")
    validate.add_argument("--strict", action="store_true")

    apply_overlay_parser = subparsers.add_parser("apply-overlay", help="Apply tracked overlay into .codex.")
    apply_overlay_parser.add_argument("repo_root", nargs="?", default=".")
    apply_overlay_parser.add_argument("--compact-prompt-file")

    capture_pristine = subparsers.add_parser(
        "capture-pristine-overwrites",
        help="Capture fresh-install pristine copies for overwrite-mode overlay entries.",
    )
    capture_pristine.add_argument("repo_root", nargs="?", default=".")
    capture_pristine.add_argument("--output")
    capture_pristine.add_argument("--pretty", action="store_true")
    capture_pristine.add_argument("--strict", action="store_true")

    reasoning = subparsers.add_parser("apply-reasoning-defaults", help="Apply repo-local reasoning defaults.")
    reasoning.add_argument("repo_root", nargs="?", default=".")

    verify = subparsers.add_parser("verify-materialized", help="Verify post-materialization overlay coherence.")
    verify.add_argument("repo_root", nargs="?", default=".")
    verify.add_argument("--compact-prompt-file")
    verify.add_argument("--output")
    verify.add_argument("--pretty", action="store_true")
    verify.add_argument("--strict", action="store_true")

    return parser.parse_args()


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def write_json(payload: dict[str, Any], output: pathlib.Path | None, pretty: bool = True) -> None:
    text = json.dumps(payload, indent=2 if pretty else None, sort_keys=pretty) + "\n"
    if output is None:
        print(text, end="")
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")


def compact_prompt_file(repo_root: pathlib.Path) -> str:
    selector = repo_root / LOCAL_COMPACT_PROMPT_SELECTOR
    if selector.exists():
        first_line = selector.read_text(encoding="utf-8").splitlines()
        if first_line and first_line[0].strip():
            return first_line[0].strip()
    return DEFAULT_COMPACT_PROMPT_FILE


def install_mutation_targets() -> set[str]:
    return {"config.toml"} | {f"agents/{name}.toml" for name in QUALITY_REASONING}


def render_overlay_text(text: str, repo_root: pathlib.Path, compact_prompt: str) -> str:
    return text.replace("__PROJECT_ROOT__", str(repo_root)).replace("__COMPACT_PROMPT_FILE__", compact_prompt)


def normalize_reasoning_defaults(rel_path: str, text: str) -> str:
    if rel_path == "config.toml" or (rel_path.startswith("agents/") and rel_path.endswith(".toml")):
        lines = [line for line in text.splitlines() if not line.startswith("model_reasoning_effort = ")]
        normalized = "\n".join(lines)
        if text.endswith("\n"):
            normalized += "\n"
        return normalized
    return text


def load_backup_meta_paths(codex_root: pathlib.Path) -> set[str]:
    backup_meta_path = codex_root / "gsd-local-patches" / "backup-meta.json"
    if not backup_meta_path.exists():
        return set()
    payload = json.loads(read_text(backup_meta_path))
    files = payload.get("files", [])
    if isinstance(files, dict):
        return set(files.keys())
    if isinstance(files, list):
        return set(files)
    return set()


def load_runtime_manifest_paths(codex_root: pathlib.Path) -> set[str]:
    manifest_path = codex_root / "gsd-file-manifest.json"
    if not manifest_path.exists():
        return set()
    payload = json.loads(read_text(manifest_path))
    files = payload.get("files", {})
    if isinstance(files, dict):
        return set(files.keys())
    if isinstance(files, list):
        return set(files)
    return set()


def list_overlay_paths(overlay_root: pathlib.Path) -> set[str]:
    return {
        str(path.relative_to(overlay_root)).replace("\\", "/")
        for path in overlay_root.rglob("*")
        if path.is_file() and path.name != "OVERLAY-MANIFEST.json"
    }


def load_overlay_manifest(repo_root: pathlib.Path) -> dict[str, str]:
    manifest_path = repo_root / OVERLAY_MANIFEST_REL_PATH
    payload = json.loads(read_text(manifest_path))
    entries = payload.get("entries", {})
    if not isinstance(entries, dict):
        raise ValueError("overlay manifest entries must be an object")
    return {str(key): str(value) for key, value in entries.items()}


def build_manifest_validation_report(repo_root: pathlib.Path) -> dict[str, Any]:
    overlay_root = repo_root / OVERLAY_REL_PATH
    manifest_path = repo_root / OVERLAY_MANIFEST_REL_PATH
    codex_root = repo_root / ".codex"

    hard_failures: list[str] = []
    if not overlay_root.exists():
        hard_failures.append(f"overlay root missing: {overlay_root}")
    if not manifest_path.exists():
        hard_failures.append(f"overlay manifest missing: {manifest_path}")

    overlay_paths = list_overlay_paths(overlay_root) if overlay_root.exists() else set()
    entries = load_overlay_manifest(repo_root) if manifest_path.exists() else {}
    backup_paths = load_backup_meta_paths(codex_root) if codex_root.exists() else set()

    manifest_paths = set(entries)
    invalid_modes = sorted(path for path, mode in entries.items() if mode not in VALID_MODES)
    missing_from_manifest = sorted(overlay_paths - manifest_paths)
    missing_from_overlay = sorted(manifest_paths - overlay_paths)
    overwrite_paths = {path for path, mode in entries.items() if mode == "overwrite"}
    add_paths = {path for path, mode in entries.items() if mode == "add"}
    overwrite_missing_in_backup = sorted(overwrite_paths - backup_paths)
    add_present_in_backup = sorted(add_paths & backup_paths)
    backup_overlay_not_overwrite = sorted((backup_paths & overlay_paths) - overwrite_paths)

    if invalid_modes:
        hard_failures.append(f"overlay manifest contains invalid modes for {len(invalid_modes)} paths")
    if missing_from_manifest:
        hard_failures.append(f"{len(missing_from_manifest)} overlay files are missing manifest entries")
    if missing_from_overlay:
        hard_failures.append(f"{len(missing_from_overlay)} manifest entries do not exist in overlay")
    if overwrite_missing_in_backup:
        hard_failures.append(
            f"{len(overwrite_missing_in_backup)} overwrite entries are not backed by backup-meta upstream carry"
        )
    if add_present_in_backup:
        hard_failures.append(f"{len(add_present_in_backup)} add entries are incorrectly present in backup-meta")
    if backup_overlay_not_overwrite:
        hard_failures.append(
            f"{len(backup_overlay_not_overwrite)} backup-meta overlay paths are not typed as overwrite entries"
        )

    return {
        "overlay_root": str(overlay_root),
        "manifest_path": str(manifest_path),
        "summary": {
            "overlay_file_count": len(overlay_paths),
            "manifest_entry_count": len(manifest_paths),
            "overwrite_count": len(overwrite_paths),
            "add_count": len(add_paths),
            "backup_meta_count": len(backup_paths),
        },
        "invalid_modes": invalid_modes,
        "missing_from_manifest": missing_from_manifest,
        "missing_from_overlay": missing_from_overlay,
        "overwrite_missing_in_backup": overwrite_missing_in_backup,
        "add_present_in_backup": add_present_in_backup,
        "backup_overlay_not_overwrite": backup_overlay_not_overwrite,
        "hard_failures": hard_failures,
    }


def capture_pristine_overwrites(repo_root: pathlib.Path) -> dict[str, Any]:
    codex_root = repo_root / ".codex"
    backup_root = codex_root / "gsd-local-patches"
    entries = load_overlay_manifest(repo_root)
    overwrite_paths = sorted(path for path, mode in entries.items() if mode == "overwrite")
    runtime_manifest_paths = load_runtime_manifest_paths(codex_root)
    copied: list[str] = []
    missing_live: list[str] = []
    missing_runtime_manifest: list[str] = []

    for rel_path in overwrite_paths:
        live_path = codex_root / rel_path
        if not live_path.exists():
            missing_live.append(rel_path)
            continue
        if runtime_manifest_paths and rel_path not in runtime_manifest_paths:
            missing_runtime_manifest.append(rel_path)
            continue
        target = backup_root / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(live_path.read_bytes())
        copied.append(rel_path)

    backup_root.mkdir(parents=True, exist_ok=True)
    backup_meta_path = backup_root / "backup-meta.json"
    backup_meta_path.write_text(
        json.dumps(
            {
                "source": "repo-local pristine overwrite capture",
                "files": copied,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    hard_failures: list[str] = []
    if missing_live:
        hard_failures.append(f"{len(missing_live)} overwrite entries are missing from fresh live .codex")
    if missing_runtime_manifest:
        hard_failures.append(f"{len(missing_runtime_manifest)} overwrite entries are absent from gsd-file-manifest")

    return {
        "repo_root": str(repo_root),
        "backup_meta_path": str(backup_meta_path),
        "summary": {
            "overwrite_count": len(overwrite_paths),
            "copied_count": len(copied),
            "missing_live_count": len(missing_live),
            "missing_runtime_manifest_count": len(missing_runtime_manifest),
        },
        "copied": copied,
        "missing_live": missing_live,
        "missing_runtime_manifest": missing_runtime_manifest,
        "hard_failures": hard_failures,
    }


def apply_overlay(repo_root: pathlib.Path, compact_prompt: str) -> list[str]:
    overlay_root = repo_root / OVERLAY_REL_PATH
    codex_root = repo_root / ".codex"
    entries = load_overlay_manifest(repo_root)
    written: list[str] = []
    for rel_path in sorted(entries):
        source = overlay_root / rel_path
        target = codex_root / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        text = render_overlay_text(read_text(source), repo_root, compact_prompt)
        target.write_text(text, encoding="utf-8")
        written.append(rel_path)
    return written


def apply_reasoning_defaults(repo_root: pathlib.Path) -> None:
    codex_root = repo_root / ".codex"
    config_path = codex_root / "config.toml"
    config_text = read_text(config_path)
    config_text = re.sub(
        r'^model_reasoning_effort = "[^"]+"$',
        'model_reasoning_effort = "xhigh"',
        config_text,
        count=1,
        flags=re.M,
    )
    config_path.write_text(config_text, encoding="utf-8")

    for agent_name, effort in QUALITY_REASONING.items():
        agent_path = codex_root / "agents" / f"{agent_name}.toml"
        text = read_text(agent_path)
        line = f'model_reasoning_effort = "{effort}"'
        if re.search(r'^model_reasoning_effort = "[^"]+"$', text, re.M):
            text = re.sub(r'^model_reasoning_effort = "[^"]+"$', line, text, count=1, flags=re.M)
        else:
            text = re.sub(r'^(description = ".*"\n)', r"\1" + line + "\n", text, count=1, flags=re.M)
        agent_path.write_text(text, encoding="utf-8")


def build_materialization_report(repo_root: pathlib.Path, compact_prompt: str) -> dict[str, Any]:
    validation = build_manifest_validation_report(repo_root)
    hard_failures = list(validation["hard_failures"])
    overlay_root = repo_root / OVERLAY_REL_PATH
    codex_root = repo_root / ".codex"
    backup_paths = load_backup_meta_paths(codex_root)
    entries = load_overlay_manifest(repo_root)

    missing_live_targets: list[str] = []
    backup_copy_missing: list[str] = []
    content_mismatch: list[str] = []

    for rel_path, mode in sorted(entries.items()):
        live_path = codex_root / rel_path
        if not live_path.exists():
            missing_live_targets.append(rel_path)
            continue
        overlay_text = render_overlay_text(read_text(overlay_root / rel_path), repo_root, compact_prompt)
        live_text = read_text(live_path)
        if normalize_reasoning_defaults(rel_path, overlay_text) != normalize_reasoning_defaults(rel_path, live_text):
            content_mismatch.append(rel_path)
        if mode == "overwrite":
            backup_copy = codex_root / "gsd-local-patches" / rel_path
            if not backup_copy.exists():
                backup_copy_missing.append(rel_path)

    if missing_live_targets:
        hard_failures.append(f"{len(missing_live_targets)} manifest entries are missing from live .codex")
    if backup_copy_missing:
        hard_failures.append(f"{len(backup_copy_missing)} overwrite entries are missing backup copies")
    if content_mismatch:
        hard_failures.append(f"{len(content_mismatch)} live targets do not match the materialized overlay contract")

    return {
        "repo_root": str(repo_root),
        "compact_prompt_file": compact_prompt,
        "install_mutation_targets": sorted(install_mutation_targets()),
        "summary": {
            **validation["summary"],
            "live_target_count": len(entries),
            "missing_live_target_count": len(missing_live_targets),
            "backup_copy_missing_count": len(backup_copy_missing),
            "content_mismatch_count": len(content_mismatch),
        },
        "missing_live_targets": missing_live_targets,
        "backup_copy_missing": backup_copy_missing,
        "content_mismatch": content_mismatch,
        "hard_failures": hard_failures,
    }


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path(args.repo_root).resolve()

    if args.command == "validate-manifest":
        report = build_manifest_validation_report(repo_root)
        write_json(report, pathlib.Path(args.output) if args.output else None, pretty=args.pretty or not args.output)
        return 1 if args.strict and report["hard_failures"] else 0

    if args.command == "apply-overlay":
        compact_prompt = args.compact_prompt_file or compact_prompt_file(repo_root)
        written = apply_overlay(repo_root, compact_prompt)
        for rel_path in written:
            print(f"  patched .codex/{rel_path}")
        return 0

    if args.command == "capture-pristine-overwrites":
        report = capture_pristine_overwrites(repo_root)
        write_json(report, pathlib.Path(args.output) if args.output else None, pretty=args.pretty or not args.output)
        return 1 if args.strict and report["hard_failures"] else 0

    if args.command == "apply-reasoning-defaults":
        apply_reasoning_defaults(repo_root)
        return 0

    if args.command == "verify-materialized":
        compact_prompt = args.compact_prompt_file or compact_prompt_file(repo_root)
        report = build_materialization_report(repo_root, compact_prompt)
        write_json(report, pathlib.Path(args.output) if args.output else None, pretty=args.pretty or not args.output)
        return 1 if args.strict and report["hard_failures"] else 0

    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
