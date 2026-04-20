#!/usr/bin/env python3
"""Summarize final repo-local GSD runtime truth without rewriting updater manifests."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from dataclasses import dataclass


DEFAULT_COMPACT_PROMPT_FILE = "tooling/compact-prompts/project.md"
LOCAL_COMPACT_PROMPT_SELECTOR = ".codex.local/compact-prompt.txt"
INTENTIONAL = "intentional materialized carry"
REPO_LOCAL = "repo-local config carry"
SELECTIVE = "selective overlay boundary"
OBSOLETE = "obsolete live residue"
UNKNOWN = "unknown live drift"

SUB_RAW_EQUAL = "raw_equal"
SUB_TEMPLATE_MATERIALIZATION = "template_materialization_equal"
SUB_REPO_LOCAL_CONFIG_DEFAULTS = "repo_local_config_defaults"
SUB_REPO_LOCAL_REASONING_DEFAULTS = "repo_local_reasoning_defaults"
SUB_SELECTIVE_UPSTREAM = "upstream_shipped_outside_overlay_subset"
SUB_SELECTIVE_BACKUP = "backup_carried_outside_overlay_subset"
SUB_SELECTIVE_INSTALL = "install_mutation_outside_overlay_subset"
SUB_SELECTIVE_UNTRACKED = "untracked_live_only_outside_overlay_subset"
SUB_OBSOLETE_UNTRACKED = "untracked_live_only_residue"
SUB_UNKNOWN_MISSING_LIVE = "overlay_covered_missing_from_live"
SUB_UNKNOWN_MISSING_BOTH = "missing_from_overlay_and_live"
SUB_UNKNOWN_UNRESOLVED = "unresolved_overlay_live_divergence"


@dataclass(frozen=True)
class SurfaceSpec:
    family: str
    rel_glob: str


SURFACE_SPECS = [
    SurfaceSpec("config", "config.toml"),
    SurfaceSpec("agent_toml", "agents/*.toml"),
    SurfaceSpec("workflow", "get-shit-done/workflows/*"),
    SurfaceSpec("reference", "get-shit-done/references/*"),
    SurfaceSpec("bin_lib", "get-shit-done/bin/lib/*"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Report final repo-local GSD runtime truth for selected high-leverage "
            "families without overloading gsd-file-manifest.json semantics."
        )
    )
    parser.add_argument("repo_root", nargs="?", default=".")
    parser.add_argument(
        "--output",
        help="Optional path to write the JSON report.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output (default true when writing to stdout).",
    )
    return parser.parse_args()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def load_manifest_paths(codex_root: pathlib.Path) -> set[str]:
    manifest_path = codex_root / "gsd-file-manifest.json"
    if not manifest_path.exists():
        return set()
    manifest = json.loads(read_text(manifest_path))
    files = manifest.get("files", {})
    if isinstance(files, dict):
        return set(files.keys())
    if isinstance(files, list):
        return set(files)
    return set()


def load_backup_paths(codex_root: pathlib.Path) -> set[str]:
    backup_meta_path = codex_root / "gsd-local-patches" / "backup-meta.json"
    if not backup_meta_path.exists():
        return set()
    backup_meta = json.loads(read_text(backup_meta_path))
    files = backup_meta.get("files", [])
    if isinstance(files, list):
        return set(files)
    if isinstance(files, dict):
        return set(files.keys())
    return set()


def load_install_mutation_targets(repo_root: pathlib.Path) -> set[str]:
    targets = {"config.toml"}
    setup_script = repo_root / "scripts" / "setup-portable-gsd.sh"
    if not setup_script.exists():
        return targets
    script_text = read_text(setup_script)
    for match in re.finditer(r'"([^"]+)":\s*"[^"]+"', script_text):
        targets.add(f"agents/{match.group(1)}.toml")
    return targets


def compact_prompt_file(repo_root: pathlib.Path) -> str:
    selector = repo_root / LOCAL_COMPACT_PROMPT_SELECTOR
    if selector.exists():
        first_line = selector.read_text(encoding="utf-8").splitlines()
        if first_line and first_line[0].strip():
            return first_line[0].strip()
    return DEFAULT_COMPACT_PROMPT_FILE


def normalize_overlay_text(text: str, repo_root: pathlib.Path, compact_prompt: str) -> str:
    return (
        text.replace("__PROJECT_ROOT__", str(repo_root))
        .replace("__COMPACT_PROMPT_FILE__", compact_prompt)
    )


def classify(
    family: str,
    rel_path: str,
    overlay_exists: bool,
    live_exists: bool,
    in_manifest: bool,
    in_backup_meta: bool,
    is_install_mutation_target: bool,
    raw_equal: bool,
    normalized_equal: bool,
    overlay_text: str | None,
    live_text: str | None,
) -> tuple[str, str, str]:
    if not overlay_exists and live_exists:
        supports_obsolete_detection = family in {"workflow", "reference", "bin_lib"}
        if supports_obsolete_detection and not in_manifest and not in_backup_meta and not is_install_mutation_target:
            return (
                OBSOLETE,
                SUB_OBSOLETE_UNTRACKED,
                "live-only surface is outside overlay, manifest, carried-subset metadata, and install-script mutation targets",
            )
        if in_manifest:
            return (
                SELECTIVE,
                SUB_SELECTIVE_UPSTREAM,
                "upstream-shipped surface exists outside the tracked overlay subset for this family",
            )
        if in_backup_meta:
            return (
                SELECTIVE,
                SUB_SELECTIVE_BACKUP,
                "live-only surface is carried in backup metadata outside the tracked overlay subset for this family",
            )
        if is_install_mutation_target:
            return (
                SELECTIVE,
                SUB_SELECTIVE_INSTALL,
                "live-only surface is an install-script mutation target outside the tracked overlay subset for this family",
            )
        return (
            SELECTIVE,
            SUB_SELECTIVE_UNTRACKED,
            "live surface exists outside the tracked overlay subset for this family",
        )
    if overlay_exists and not live_exists:
        return (
            UNKNOWN,
            SUB_UNKNOWN_MISSING_LIVE,
            "overlay-covered surface is missing from live runtime",
        )
    if not overlay_exists and not live_exists:
        return (
            UNKNOWN,
            SUB_UNKNOWN_MISSING_BOTH,
            "surface missing from both overlay and live runtime",
        )
    if raw_equal:
        return (
            INTENTIONAL,
            SUB_RAW_EQUAL,
            "difference is explained by direct equality",
        )
    if normalized_equal:
        return (
            INTENTIONAL,
            SUB_TEMPLATE_MATERIALIZATION,
            "difference is explained by direct equality or template materialization",
        )
    if family == "config":
        return (
            REPO_LOCAL,
            SUB_REPO_LOCAL_CONFIG_DEFAULTS,
            "config surface carries repo-local defaults beyond the generic overlay template",
        )
    if family == "agent_toml" and overlay_text is not None and live_text is not None:
        overlay_wo_reasoning = "\n".join(
            line for line in overlay_text.splitlines() if not line.startswith("model_reasoning_effort = ")
        )
        live_wo_reasoning = "\n".join(
            line for line in live_text.splitlines() if not line.startswith("model_reasoning_effort = ")
        )
        if overlay_wo_reasoning == live_wo_reasoning:
            return (
                REPO_LOCAL,
                SUB_REPO_LOCAL_REASONING_DEFAULTS,
                "agent contract differs only in repo-local reasoning defaults",
            )
    return (
        UNKNOWN,
        SUB_UNKNOWN_UNRESOLVED,
        "overlay-covered surface still differs after materialization-aware comparison",
    )


def collect_rel_paths(root: pathlib.Path, rel_glob: str) -> set[str]:
    return {path.relative_to(root).as_posix() for path in root.glob(rel_glob) if path.is_file()}


def build_report(repo_root: pathlib.Path) -> dict:
    overlay_root = repo_root / "tooling" / "portable-gsd" / "overlay"
    live_root = repo_root / ".codex"
    compact_prompt = compact_prompt_file(repo_root)
    manifest_paths = load_manifest_paths(live_root)
    backup_paths = load_backup_paths(live_root)
    install_mutation_targets = load_install_mutation_targets(repo_root)
    entries = []

    if not overlay_root.exists():
        raise SystemExit(f"Overlay root not found: {overlay_root}")
    if not live_root.exists():
        raise SystemExit(f"Live runtime root not found: {live_root}")

    for spec in SURFACE_SPECS:
        overlay_paths = collect_rel_paths(overlay_root, spec.rel_glob)
        live_paths = collect_rel_paths(live_root, spec.rel_glob)
        for rel_path in sorted(overlay_paths | live_paths):
            overlay_path = overlay_root / rel_path
            live_path = live_root / rel_path
            overlay_exists = overlay_path.exists()
            live_exists = live_path.exists()
            in_manifest = rel_path in manifest_paths
            in_backup_meta = rel_path in backup_paths
            is_install_mutation_target = rel_path in install_mutation_targets
            overlay_text = None
            live_text = None
            normalized_overlay = None
            raw_equal = False
            normalized_equal = False

            if overlay_exists:
                overlay_text = read_text(overlay_path)
                normalized_overlay = normalize_overlay_text(overlay_text, repo_root, compact_prompt)
            if live_exists:
                live_text = read_text(live_path)

            if overlay_text is not None and live_text is not None:
                raw_equal = overlay_text == live_text
            if normalized_overlay is not None and live_text is not None:
                normalized_equal = normalized_overlay == live_text

            classification, subclassification, note = classify(
                family=spec.family,
                rel_path=rel_path,
                overlay_exists=overlay_exists,
                live_exists=live_exists,
                in_manifest=in_manifest,
                in_backup_meta=in_backup_meta,
                is_install_mutation_target=is_install_mutation_target,
                raw_equal=raw_equal,
                normalized_equal=normalized_equal,
                overlay_text=normalized_overlay if normalized_overlay is not None else overlay_text,
                live_text=live_text,
            )

            entries.append(
                {
                    "family": spec.family,
                    "rel_path": rel_path,
                    "overlay_exists": overlay_exists,
                    "live_exists": live_exists,
                    "overlay_path": str(overlay_path) if overlay_exists else None,
                    "live_path": str(live_path) if live_exists else None,
                    "in_manifest": in_manifest,
                    "in_backup_meta": in_backup_meta,
                    "is_install_mutation_target": is_install_mutation_target,
                    "overlay_sha256": sha256_text(overlay_text) if overlay_text is not None else None,
                    "normalized_overlay_sha256": sha256_text(normalized_overlay) if normalized_overlay is not None else None,
                    "live_sha256": sha256_text(live_text) if live_text is not None else None,
                    "raw_equal": raw_equal,
                    "normalized_equal": normalized_equal,
                    "classification": classification,
                    "subclassification": subclassification,
                    "note": note,
                }
            )

    summary = {
        "total_entries": len(entries),
        "intentional_materialized_carry": sum(1 for e in entries if e["classification"] == INTENTIONAL),
        "repo_local_config_carry": sum(1 for e in entries if e["classification"] == REPO_LOCAL),
        "selective_overlay_boundary": sum(1 for e in entries if e["classification"] == SELECTIVE),
        "obsolete_live_residue": sum(1 for e in entries if e["classification"] == OBSOLETE),
        "unknown_live_drift": sum(1 for e in entries if e["classification"] == UNKNOWN),
    }
    subclassification_summary = {
        key: count
        for key, count in sorted(
            (
                subclassification,
                sum(1 for e in entries if e["subclassification"] == subclassification),
            )
            for subclassification in {e["subclassification"] for e in entries}
        )
        if count
    }

    return {
        "repo_root": str(repo_root),
        "overlay_root": str(overlay_root),
        "live_root": str(live_root),
        "compact_prompt_file": compact_prompt,
        "normalized_overlay_sha_scope": "checkout-local",
        "summary": summary,
        "subclassification_summary": subclassification_summary,
        "entries": entries,
    }


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path(args.repo_root).resolve()
    report = build_report(repo_root)
    indent = 2 if args.pretty or not args.output else None
    payload = json.dumps(report, indent=indent, sort_keys=False)

    if args.output:
        output_path = pathlib.Path(args.output)
        if not output_path.is_absolute():
            output_path = (repo_root / output_path).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload + "\n", encoding="utf-8")
    else:
        sys.stdout.write(payload + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
