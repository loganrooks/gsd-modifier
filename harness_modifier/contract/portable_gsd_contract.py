#!/usr/bin/env python3
"""Shared portable-GSD overlay contract helpers."""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
from typing import Any

REPO_ROOT_FOR_IMPORTS = pathlib.Path(__file__).resolve().parents[2]
if str(REPO_ROOT_FOR_IMPORTS) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT_FOR_IMPORTS))

from harness_modifier.compatibility import declaration as compatibility_declaration
from harness_modifier.contract import inject_operations
from harness_modifier.contract.runtime_adapters import registry as runtime_adapter_registry


DEFAULT_COMPACT_PROMPT_FILE = "tooling/compact-prompts/project.md"
LOCAL_COMPACT_PROMPT_SELECTOR = ".codex.local/compact-prompt.txt"
OVERLAY_REL_PATH = "tooling/portable-gsd/overlay"
OVERLAY_MANIFEST_REL_PATH = "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json"
VALID_MODES = {"add", "overwrite", "inject"}
VALID_PARITY_TIERS = {"core_required", "core_adapted", "runtime_specific"}
SUPPORTED_SCHEMA_VERSIONS = {2, 3, 4}
RUNTIME_SPECIFIC_REFERENCE_PATTERN = re.compile(r"(?:~|\$HOME)\/\.claude\b")
RUNTIME_SPECIFIC_REFERENCE_SUFFIXES = {".md", ".toml"}
RUNTIME_SPECIFIC_REFERENCE_EXCLUDED = {"CHANGELOG.md"}
COMPATIBILITY_DECLARATION = compatibility_declaration.load_declaration()

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

SUPPORTED_RUNTIMES = tuple(runtime_adapter_registry.supported_runtimes())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Portable GSD overlay contract helper.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate-manifest", help="Validate overlay add/overwrite contract.")
    validate.add_argument("repo_root", nargs="?", default=".")
    add_runtime_args(validate, allow_all_supported=True)
    validate.add_argument("--output")
    validate.add_argument("--pretty", action="store_true")
    validate.add_argument("--strict", action="store_true")
    validate.add_argument(
        "--source-only",
        action="store_true",
        help="Validate tracked manifest and overlay source without requiring materialized runtime backup metadata.",
    )

    apply_overlay_parser = subparsers.add_parser("apply-overlay", help="Apply tracked overlay into .codex.")
    apply_overlay_parser.add_argument("repo_root", nargs="?", default=".")
    add_runtime_args(apply_overlay_parser)
    apply_overlay_parser.add_argument("--compact-prompt-file")

    capture_pristine = subparsers.add_parser(
        "capture-pristine-overwrites",
        help="Capture fresh-install pristine copies for overwrite-mode overlay entries.",
    )
    capture_pristine.add_argument("repo_root", nargs="?", default=".")
    add_runtime_args(capture_pristine)
    capture_pristine.add_argument("--output")
    capture_pristine.add_argument("--pretty", action="store_true")
    capture_pristine.add_argument("--strict", action="store_true")

    reasoning = subparsers.add_parser("apply-reasoning-defaults", help="Apply repo-local reasoning defaults.")
    reasoning.add_argument("repo_root", nargs="?", default=".")
    add_runtime_args(reasoning)

    verify = subparsers.add_parser("verify-materialized", help="Verify post-materialization overlay coherence.")
    verify.add_argument("repo_root", nargs="?", default=".")
    add_runtime_args(verify, allow_all_supported=True)
    verify.add_argument("--compact-prompt-file")
    verify.add_argument("--output")
    verify.add_argument("--pretty", action="store_true")
    verify.add_argument("--strict", action="store_true")

    return parser.parse_args()


def add_runtime_args(parser: argparse.ArgumentParser, allow_all_supported: bool = False) -> None:
    if allow_all_supported:
        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            "--runtime",
            choices=SUPPORTED_RUNTIMES,
            default="codex",
            help="Runtime to inspect or materialize. Default: codex.",
        )
        group.add_argument(
            "--all-supported",
            action="store_true",
            help="Run the helper across all supported runtimes.",
        )
        return
    parser.add_argument(
        "--runtime",
        choices=SUPPORTED_RUNTIMES,
        default="codex",
        help="Runtime to inspect or materialize. Default: codex.",
    )


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def write_json(payload: dict[str, Any], output: pathlib.Path | None, pretty: bool = True) -> None:
    text = json.dumps(payload, indent=2 if pretty else None, sort_keys=pretty) + "\n"
    if output is None:
        print(text, end="")
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")


def selected_runtimes(args: argparse.Namespace) -> list[str]:
    if getattr(args, "all_supported", False):
        return list(SUPPORTED_RUNTIMES)
    return [getattr(args, "runtime", "codex")]


def runtime_root_rel_path(runtime: str) -> str:
    return compatibility_declaration.runtime_root(runtime)


def runtime_root(repo_root: pathlib.Path, runtime: str) -> pathlib.Path:
    return repo_root / runtime_root_rel_path(runtime)


def runtime_version_source(runtime: str) -> str:
    return compatibility_declaration.version_source(runtime)


def runtime_manifest_source(runtime: str) -> str:
    return compatibility_declaration.manifest_version_source(runtime)


def compact_prompt_file(repo_root: pathlib.Path) -> str:
    selector = repo_root / LOCAL_COMPACT_PROMPT_SELECTOR
    if selector.exists():
        first_line = selector.read_text(encoding="utf-8").splitlines()
        if first_line and first_line[0].strip():
            return first_line[0].strip()
    return DEFAULT_COMPACT_PROMPT_FILE


def install_mutation_targets(runtime: str = "codex") -> set[str]:
    if runtime == "codex":
        return {"config.toml"} | {f"agents/{name}.toml" for name in QUALITY_REASONING}
    return set()


def render_overlay_text(text: str, repo_root: pathlib.Path, compact_prompt: str) -> str:
    return text.replace("__PROJECT_ROOT__", str(repo_root)).replace("__COMPACT_PROMPT_FILE__", compact_prompt)


def normalize_reasoning_defaults(rel_path: str, text: str, runtime: str = "codex") -> str:
    if runtime == "codex" and (
        rel_path == "config.toml" or (rel_path.startswith("agents/") and rel_path.endswith(".toml"))
    ):
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


def load_overlay_manifest(repo_root: pathlib.Path) -> dict[str, Any]:
    manifest_path = repo_root / OVERLAY_MANIFEST_REL_PATH
    payload = json.loads(read_text(manifest_path))
    entries = payload.get("entries", {})
    if not isinstance(entries, dict):
        raise ValueError("overlay manifest entries must be an object")
    return entries


def normalize_overlay_manifest_entry(
    repo_root: pathlib.Path, rel_path: str, entry: Any
) -> dict[str, str]:
    if isinstance(entry, str):
        source_rel_path = f"{OVERLAY_REL_PATH}/{rel_path}"
        return {
            "mode": entry,
            "target_path": rel_path,
            "source_rel_path": source_rel_path,
            "source_path": str((repo_root / source_rel_path).resolve()),
        }
    if isinstance(entry, dict):
        mode = entry.get("mode")
        target_rel_path = entry.get("target", rel_path)
        source_rel_path = entry.get("source", f"{OVERLAY_REL_PATH}/{rel_path}")
        if not isinstance(mode, str):
            raise ValueError(f"overlay manifest entry {rel_path} is missing string mode")
        if not isinstance(target_rel_path, str):
            raise ValueError(f"overlay manifest entry {rel_path} has a non-string target")
        if not isinstance(source_rel_path, str):
            raise ValueError(f"overlay manifest entry {rel_path} has a non-string source")
        return {
            "mode": mode,
            "target_path": target_rel_path,
            "source_rel_path": source_rel_path,
            "source_path": str((repo_root / source_rel_path).resolve()),
        }
    raise ValueError(f"overlay manifest entry {rel_path} must be a string or object")


def normalize_overlay_materializer_entry(
    repo_root: pathlib.Path,
    logical_id: str,
    capability_id: str,
    parity_tier: str,
    runtime: str,
    materializer: dict[str, Any],
) -> dict[str, Any]:
    mode = materializer.get("mode")
    target = materializer.get("target")
    source = materializer.get("source")
    if not isinstance(mode, str):
        raise ValueError(f"overlay manifest entry {logical_id} has non-string mode for {runtime}")
    if not isinstance(target, str) or not target:
        raise ValueError(f"overlay manifest entry {logical_id} has non-string target for {runtime}")
    if not isinstance(source, str) or not source:
        raise ValueError(f"overlay manifest entry {logical_id} has non-string source for {runtime}")
    return {
        "logical_id": logical_id,
        "capability_id": capability_id,
        "parity_tier": parity_tier,
        "runtime": runtime,
        "mode": mode,
        "target_path": target,
        "source_rel_path": source,
        "source_path": str((repo_root / source).resolve()),
    }


def normalize_overlay_inject_materializer_entry(
    repo_root: pathlib.Path,
    logical_id: str,
    capability_id: str,
    parity_tier: str,
    runtime: str,
    materializer: dict[str, Any],
) -> dict[str, Any]:
    target = materializer.get("target")
    operations = materializer.get("operations")
    if not isinstance(target, str) or not target:
        raise ValueError(f"overlay manifest entry {logical_id} has non-string target for {runtime}")
    if not isinstance(operations, list):
        raise ValueError(
            f"overlay manifest entry {logical_id} inject materializer must declare operations list for {runtime}"
        )
    return {
        "logical_id": logical_id,
        "capability_id": capability_id,
        "parity_tier": parity_tier,
        "runtime": runtime,
        "mode": "inject",
        "target_path": target,
        "source_rel_path": "",
        "source_path": "",
        "operations": operations,
    }


def load_overlay_manifest_specs(repo_root: pathlib.Path, runtime: str = "codex") -> dict[str, dict[str, Any]]:
    payload = load_overlay_manifest_payload(repo_root)
    schema_version = int(payload.get("schema_version", 2))
    entries = payload.get("entries", {})
    if not isinstance(entries, dict):
        raise ValueError("overlay manifest entries must be an object")
    if schema_version == 2:
        return {
            str(rel_path): {
                **normalize_overlay_manifest_entry(repo_root, str(rel_path), entry),
                "logical_id": str(rel_path),
                "capability_id": str(rel_path),
                "parity_tier": "runtime_specific",
                "runtime": "codex",
            }
            for rel_path, entry in entries.items()
            if runtime == "codex"
        }
    if schema_version not in SUPPORTED_SCHEMA_VERSIONS:
        raise ValueError(f"unsupported overlay manifest schema version: {schema_version}")

    flattened: dict[str, dict[str, Any]] = {}
    for logical_id, entry in entries.items():
        if not isinstance(entry, dict):
            raise ValueError(f"overlay manifest entry {logical_id} must be an object under schema {schema_version}")
        capability_id = entry.get("capability_id")
        parity_tier = entry.get("parity_tier")
        materializers = entry.get("materializers", {})
        if not isinstance(capability_id, str) or not capability_id:
            raise ValueError(f"overlay manifest entry {logical_id} is missing capability_id")
        if parity_tier not in VALID_PARITY_TIERS:
            raise ValueError(f"overlay manifest entry {logical_id} has invalid parity_tier")
        if not isinstance(materializers, dict):
            raise ValueError(f"overlay manifest entry {logical_id} materializers must be an object")
        if runtime not in materializers:
            continue
        materializer = materializers[runtime]
        if not isinstance(materializer, dict):
            raise ValueError(
                f"overlay manifest entry {logical_id} materializer for {runtime} must be an object"
            )
        mode = materializer.get("mode")
        if mode == "inject":
            if schema_version < 4:
                raise ValueError(
                    f"overlay manifest entry {logical_id} uses mode: inject which requires schema_version >= 4"
                )
            spec = normalize_overlay_inject_materializer_entry(
                repo_root,
                str(logical_id),
                capability_id,
                parity_tier,
                runtime,
                materializer,
            )
        else:
            spec = normalize_overlay_materializer_entry(
                repo_root,
                str(logical_id),
                capability_id,
                parity_tier,
                runtime,
                materializer,
            )
        target_path = spec["target_path"]
        if target_path in flattened:
            raise ValueError(f"duplicate overlay target for runtime {runtime}: {target_path}")
        flattened[target_path] = spec
    return flattened


def overlay_entry_source_path(repo_root: pathlib.Path, rel_path: str) -> pathlib.Path:
    entry = load_overlay_manifest_specs(repo_root)[rel_path]
    return pathlib.Path(entry["source_path"])


def load_overlay_manifest_payload(repo_root: pathlib.Path) -> dict[str, Any]:
    manifest_path = repo_root / OVERLAY_MANIFEST_REL_PATH
    return json.loads(read_text(manifest_path))


def iter_runtime_specific_reference_hits(codex_root: pathlib.Path) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for path in sorted(codex_root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix not in RUNTIME_SPECIFIC_REFERENCE_SUFFIXES:
            continue
        if path.name in RUNTIME_SPECIFIC_REFERENCE_EXCLUDED:
            continue
        rel_path = str(path.relative_to(codex_root)).replace("\\", "/")
        for line_number, line in enumerate(read_text(path).splitlines(), start=1):
            if not RUNTIME_SPECIFIC_REFERENCE_PATTERN.search(line):
                continue
            hits.append(
                {
                    "path": rel_path,
                    "line": line_number,
                    "text": line.strip(),
                }
            )
    return hits


def classify_runtime_specific_reference_hit(
    hit: dict[str, Any], overlay_entries: dict[str, str]
) -> dict[str, Any]:
    rel_path = str(hit["path"])
    line_text = str(hit["text"])
    overlay_mode = overlay_entries.get(rel_path)

    classification = "unreviewed_runtime_specific_reference_hit"
    family = "needs_contextual_reread"
    ownership = "untyped"
    expected_baseline = False
    requires_contextual_reread = True
    note = "net-new or unclassified runtime-specific reference hit; reread context before taking action"

    for rule in COMPATIBILITY_DECLARATION["parity_scan_baseline"]["rules"]:
        path_match_mode = rule.get("path_match_mode", "exact")
        if path_match_mode == "exact" and rel_path != rule["path"]:
            continue
        if path_match_mode == "prefix" and not rel_path.startswith(rule["path"]):
            continue

        text_match_mode = rule.get("text_match_mode", "exact")
        if text_match_mode == "exact" and line_text != rule["text"]:
            continue
        if text_match_mode == "contains" and rule["text"] not in line_text:
            continue

        classification = str(rule["classification"])
        family = str(rule["family"])
        if "ownership_if_overlay_mode_present" in rule:
            ownership = str(rule["ownership_if_overlay_mode_present"]) if overlay_mode else str(rule["ownership_otherwise"])
        else:
            ownership = str(rule["ownership"])
        expected_baseline = True
        requires_contextual_reread = False
        note = str(rule["note"])
        break

    return {
        **hit,
        "classification": classification,
        "family": family,
        "ownership": ownership,
        "overlay_mode": overlay_mode,
        "expected_baseline": expected_baseline,
        "requires_contextual_reread": requires_contextual_reread,
        "note": note,
    }


def build_runtime_specific_reference_report(
    live_root: pathlib.Path, overlay_entries: dict[str, str], runtime: str
) -> dict[str, Any]:
    if runtime != "codex":
        return {
            "pattern": RUNTIME_SPECIFIC_REFERENCE_PATTERN.pattern,
            "scope": f"runtime-specific reference scan not required for {runtime}",
            "compatibility_declaration_path": compatibility_declaration.DECLARATION_REL_PATH,
            "target_runtime": runtime,
            "baseline_rule_count": 0,
            "hits": [],
            "summary": {
                "total_hits": 0,
                "expected_baseline_count": 0,
                "contextual_count": 0,
                "review_needed_count": 0,
            },
            "requires_contextual_reread": False,
            "notes": [
                f"{runtime} does not currently use the Codex-specific runtime reference scan.",
            ],
        }
    raw_hits = iter_runtime_specific_reference_hits(live_root)
    hits = [classify_runtime_specific_reference_hit(hit, overlay_entries) for hit in raw_hits]
    expected_baseline_count = sum(1 for hit in hits if hit["expected_baseline"])
    contextual_count = sum(1 for hit in hits if hit["family"] != "needs_contextual_reread")
    review_needed_count = sum(1 for hit in hits if hit["requires_contextual_reread"])
    return {
        "pattern": RUNTIME_SPECIFIC_REFERENCE_PATTERN.pattern,
        "scope": COMPATIBILITY_DECLARATION["parity_scan_baseline"]["scope"],
        "compatibility_declaration_path": compatibility_declaration.DECLARATION_REL_PATH,
        "target_runtime": COMPATIBILITY_DECLARATION["parity_scan_baseline"]["target_runtime"],
        "baseline_rule_count": len(COMPATIBILITY_DECLARATION["parity_scan_baseline"]["rules"]),
        "hits": hits,
        "summary": {
            "total_hits": len(hits),
            "expected_baseline_count": expected_baseline_count,
            "contextual_count": contextual_count,
            "review_needed_count": review_needed_count,
        },
        "requires_contextual_reread": review_needed_count > 0,
        "notes": [
            "This report is a bounded parity-reference aid, not a final defect judge.",
            "Known baseline hits are classified explicitly; any unreviewed hit requires contextual reread before action.",
        ],
    }


def build_manifest_validation_report_for_roots(
    modifier_repo_root: pathlib.Path,
    live_repo_root: pathlib.Path,
    runtime: str = "codex",
    require_backup_meta: bool = True,
) -> dict[str, Any]:
    overlay_root = modifier_repo_root / OVERLAY_REL_PATH
    manifest_path = modifier_repo_root / OVERLAY_MANIFEST_REL_PATH
    live_runtime_root = runtime_root(live_repo_root, runtime)
    manifest_payload = load_overlay_manifest_payload(modifier_repo_root) if manifest_path.exists() else {}
    manifest_schema_version = int(manifest_payload.get("schema_version", 2)) if manifest_payload else None

    hard_failures: list[str] = []
    if not overlay_root.exists():
        hard_failures.append(f"overlay root missing: {overlay_root}")
    if not manifest_path.exists():
        hard_failures.append(f"overlay manifest missing: {manifest_path}")

    overlay_paths = list_overlay_paths(overlay_root) if overlay_root.exists() else set()
    entry_specs = load_overlay_manifest_specs(modifier_repo_root, runtime=runtime) if manifest_path.exists() else {}
    backup_paths = load_backup_meta_paths(live_runtime_root) if live_runtime_root.exists() else set()

    manifest_paths = {spec["target_path"] for spec in entry_specs.values()}
    declared_overlay_source_paths: set[str] = set()
    if manifest_payload:
        for supported_runtime in SUPPORTED_RUNTIMES:
            for spec in load_overlay_manifest_specs(
                modifier_repo_root,
                runtime=supported_runtime,
            ).values():
                source_rel_path = spec["source_rel_path"]
                if source_rel_path.startswith(f"{OVERLAY_REL_PATH}/"):
                    declared_overlay_source_paths.add(
                        source_rel_path.removeprefix(f"{OVERLAY_REL_PATH}/")
                    )
    default_overlay_paths = {
        spec["target_path"]
        for spec in entry_specs.values()
        if spec["source_rel_path"] == f"{OVERLAY_REL_PATH}/{spec['target_path']}"
    }
    invalid_modes = sorted(path for path, spec in entry_specs.items() if spec["mode"] not in VALID_MODES)
    missing_from_manifest = sorted(overlay_paths - declared_overlay_source_paths)
    missing_from_overlay = sorted(default_overlay_paths - overlay_paths)
    missing_source_files = sorted(
        rel_path
        for rel_path, spec in entry_specs.items()
        if spec["mode"] != "inject" and not pathlib.Path(spec["source_path"]).exists()
    )
    overwrite_paths = {spec["target_path"] for spec in entry_specs.values() if spec["mode"] == "overwrite"}
    add_paths = {spec["target_path"] for spec in entry_specs.values() if spec["mode"] == "add"}
    external_source_entries = sorted(
        {
            spec["target_path"]: spec["source_rel_path"]
            for spec in entry_specs.values()
            if spec["mode"] != "inject"
            and spec["source_rel_path"] != f"{OVERLAY_REL_PATH}/{spec['target_path']}"
        }.items()
    )
    overwrite_missing_in_backup = sorted(overwrite_paths - backup_paths) if require_backup_meta else []
    add_present_in_backup = sorted(add_paths & backup_paths) if require_backup_meta else []
    backup_overlay_not_overwrite = sorted((backup_paths & overlay_paths) - overwrite_paths) if require_backup_meta else []

    if manifest_schema_version in (3, 4):
        manifest_entries = manifest_payload.get("entries", {})
        for logical_id, entry in sorted(manifest_entries.items()):
            if not isinstance(entry, dict):
                hard_failures.append(f"schema {manifest_schema_version} entry {logical_id} must be an object")
                continue
            parity_tier = entry.get("parity_tier")
            materializers = entry.get("materializers")
            if parity_tier not in VALID_PARITY_TIERS:
                hard_failures.append(
                    f"schema {manifest_schema_version} entry {logical_id} has invalid parity_tier"
                )
            if not isinstance(materializers, dict):
                hard_failures.append(
                    f"schema {manifest_schema_version} entry {logical_id} must declare materializers"
                )
                continue
            if parity_tier in {"core_required", "core_adapted"}:
                missing_runtimes = sorted(set(SUPPORTED_RUNTIMES) - set(materializers))
                if missing_runtimes:
                    hard_failures.append(
                        f"schema {manifest_schema_version} entry {logical_id} is {parity_tier} "
                        f"but is missing materializers for {', '.join(missing_runtimes)}"
                    )

    if manifest_schema_version == 4:
        manifest_entries = manifest_payload.get("entries", {})
        marker_key_entry_locations: dict[str, dict[str, list[str]]] = {}
        for logical_id, entry in sorted(manifest_entries.items()):
            if not isinstance(entry, dict):
                continue
            materializers = entry.get("materializers")
            if not isinstance(materializers, dict):
                continue
            inject_runtimes = sorted(
                runtime_id
                for runtime_id, m in materializers.items()
                if isinstance(m, dict) and m.get("mode") == "inject"
            )
            if not inject_runtimes:
                continue
            parity_intent = entry.get("parity_intent")
            if parity_intent is None:
                hard_failures.append(
                    f"schema 4 entry {logical_id} has mode: inject materializer but is missing parity_intent"
                )
            else:
                hard_failures.extend(
                    inject_operations.validate_parity_intent(parity_intent, str(logical_id))
                )
            for runtime_id in inject_runtimes:
                materializer = materializers[runtime_id]
                mat_errors, marker_keys = inject_operations.validate_inject_materializer(
                    materializer, str(logical_id), str(runtime_id)
                )
                hard_failures.extend(mat_errors)
                seen_in_runtime: dict[str, int] = {}
                for op_index, mk in enumerate(marker_keys):
                    seen_in_runtime[mk] = seen_in_runtime.get(mk, 0) + 1
                    entries_for_key = marker_key_entry_locations.setdefault(mk, {})
                    entries_for_key.setdefault(str(logical_id), []).append(
                        f"{runtime_id}#{op_index}"
                    )
                for mk, count in seen_in_runtime.items():
                    if count > 1:
                        hard_failures.append(
                            f"schema 4 entry {logical_id} runtime {runtime_id}: "
                            f"marker_key {mk!r} appears {count} times in operations list; expected once"
                        )
        for mk in sorted(marker_key_entry_locations):
            entry_locations = marker_key_entry_locations[mk]
            if len(entry_locations) > 1:
                detail = ", ".join(
                    f"{entry_id} ({'/'.join(locs)})"
                    for entry_id, locs in sorted(entry_locations.items())
                )
                hard_failures.append(
                    f"schema 4 marker_key {mk!r} is used by multiple entries: {detail}"
                )

    if invalid_modes:
        hard_failures.append(f"overlay manifest contains invalid modes for {len(invalid_modes)} paths")
    if missing_from_manifest:
        hard_failures.append(f"{len(missing_from_manifest)} overlay files are missing manifest entries")
    if missing_from_overlay:
        hard_failures.append(f"{len(missing_from_overlay)} manifest entries do not exist in overlay")
    if missing_source_files:
        hard_failures.append(f"{len(missing_source_files)} manifest entries point at missing source files")
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
        "modifier_repo_root": str(modifier_repo_root),
        "live_repo_root": str(live_repo_root),
        "runtime": runtime,
        "live_runtime_root": str(live_runtime_root),
        "overlay_root": str(overlay_root),
        "manifest_path": str(manifest_path),
        "summary": {
            "manifest_schema_version": manifest_schema_version,
            "overlay_file_count": len(overlay_paths),
            "manifest_entry_count": len(manifest_paths),
            "overwrite_count": len(overwrite_paths),
            "add_count": len(add_paths),
            "backup_meta_count": len(backup_paths),
            "requires_backup_meta": require_backup_meta,
        },
        "invalid_modes": invalid_modes,
        "missing_from_manifest": missing_from_manifest,
        "missing_from_overlay": missing_from_overlay,
        "missing_source_files": missing_source_files,
        "external_source_entries": [
            {"path": rel_path, "source_rel_path": source_rel_path}
            for rel_path, source_rel_path in external_source_entries
        ],
        "overwrite_missing_in_backup": overwrite_missing_in_backup,
        "add_present_in_backup": add_present_in_backup,
        "backup_overlay_not_overwrite": backup_overlay_not_overwrite,
        "hard_failures": hard_failures,
    }


def build_manifest_validation_report(
    repo_root: pathlib.Path,
    runtime: str = "codex",
    require_backup_meta: bool = True,
) -> dict[str, Any]:
    return build_manifest_validation_report_for_roots(
        repo_root,
        repo_root,
        runtime=runtime,
        require_backup_meta=require_backup_meta,
    )


def capture_pristine_overwrites(repo_root: pathlib.Path, runtime: str = "codex") -> dict[str, Any]:
    live_root = runtime_root(repo_root, runtime)
    backup_root = live_root / "gsd-local-patches"
    entry_specs = load_overlay_manifest_specs(repo_root, runtime=runtime)
    overwrite_paths = sorted(spec["target_path"] for spec in entry_specs.values() if spec["mode"] == "overwrite")
    runtime_manifest_paths = load_runtime_manifest_paths(live_root)
    copied: list[str] = []
    missing_live: list[str] = []
    missing_runtime_manifest: list[str] = []

    for rel_path in overwrite_paths:
        live_path = live_root / rel_path
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
        "runtime": runtime,
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


def apply_overlay(repo_root: pathlib.Path, compact_prompt: str, runtime: str = "codex") -> list[str]:
    live_root = runtime_root(repo_root, runtime)
    entry_specs = load_overlay_manifest_specs(repo_root, runtime=runtime)
    written: list[str] = []
    for rel_path, spec in sorted(entry_specs.items()):
        target = live_root / spec["target_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        if spec["mode"] == "inject":
            # Inject mode enriches an upstream-installed file in place per ADR-001 §7.
            # The target MUST exist (the installer ran first); apply_inject_operations
            # produces the new content atomically — write only on success.
            if not target.exists():
                raise FileNotFoundError(
                    f"inject target {target} does not exist; mode: inject requires the "
                    f"upstream file to be installed before injection runs"
                )
            original_content = read_text(target)
            operations = spec.get("operations", [])

            def _resolver(source_rel_path: str) -> str:
                return render_overlay_text(
                    read_text(repo_root / source_rel_path), repo_root, compact_prompt
                )

            new_content, _records = inject_operations.apply_inject_operations(
                original_content, operations, _resolver
            )
            target.write_text(new_content, encoding="utf-8")
            written.append(spec["target_path"])
            continue
        source = pathlib.Path(spec["source_path"])
        text = render_overlay_text(read_text(source), repo_root, compact_prompt)
        target.write_text(text, encoding="utf-8")
        written.append(spec["target_path"])
    return written


def apply_reasoning_defaults(repo_root: pathlib.Path, runtime: str = "codex") -> None:
    if runtime != "codex":
        return
    live_root = runtime_root(repo_root, runtime)
    config_path = live_root / "config.toml"
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
        agent_path = live_root / "agents" / f"{agent_name}.toml"
        text = read_text(agent_path)
        line = f'model_reasoning_effort = "{effort}"'
        if re.search(r'^model_reasoning_effort = "[^"]+"$', text, re.M):
            text = re.sub(r'^model_reasoning_effort = "[^"]+"$', line, text, count=1, flags=re.M)
        else:
            text = re.sub(r'^(description = ".*"\n)', r"\1" + line + "\n", text, count=1, flags=re.M)
        agent_path.write_text(text, encoding="utf-8")


def build_materialization_report_for_roots(
    modifier_repo_root: pathlib.Path,
    live_repo_root: pathlib.Path,
    compact_prompt: str,
    runtime: str = "codex",
) -> dict[str, Any]:
    validation = build_manifest_validation_report_for_roots(
        modifier_repo_root,
        live_repo_root,
        runtime=runtime,
    )
    hard_failures = list(validation["hard_failures"])
    live_root = runtime_root(live_repo_root, runtime)
    backup_paths = load_backup_meta_paths(live_root)
    entry_specs = load_overlay_manifest_specs(modifier_repo_root, runtime=runtime)
    overlay_manifest_payload = load_overlay_manifest_payload(modifier_repo_root)
    overlay_modes = {spec["target_path"]: spec["mode"] for spec in entry_specs.values()}
    runtime_specific_reference_scan = build_runtime_specific_reference_report(live_root, overlay_modes, runtime)
    declared_overlay_schema_version = compatibility_declaration.overlay_schema_version()
    observed_overlay_schema_version = overlay_manifest_payload.get("schema_version")
    overlay_schema_version_matches_declaration = observed_overlay_schema_version == declared_overlay_schema_version or {
        observed_overlay_schema_version,
        declared_overlay_schema_version,
    } == {2, 3}

    if not overlay_schema_version_matches_declaration:
        hard_failures.append(
            "compatibility declaration overlay schema version does not match the live overlay manifest schema version"
        )

    missing_live_targets: list[str] = []
    backup_copy_missing: list[str] = []
    content_mismatch: list[str] = []
    inject_verifications: list[dict[str, Any]] = []
    inject_failures: list[str] = []

    for rel_path, spec in sorted(entry_specs.items()):
        mode = spec["mode"]
        target_rel_path = spec["target_path"]
        live_path = live_root / target_rel_path
        if not live_path.exists():
            missing_live_targets.append(target_rel_path)
            continue
        if mode == "inject":
            # Phase 2 Slice 4: verify_inject_state asserts each operation's
            # effects landed per ADR-001 §8 Option V1 (marker presence + position
            # check; non-marker regions are NOT asserted). Structural corruption
            # surfaces via extraction_error.
            materialized_content = read_text(live_path)
            verify_result = inject_operations.verify_inject_state(
                materialized_content, spec.get("operations", [])
            )
            per_op_records = [
                {
                    "marker_key": v.marker_key,
                    "kind": v.kind,
                    "status": v.status,
                    "detail": v.detail,
                    "op_index": v.op_index,
                }
                for v in verify_result.operation_verifications
            ]
            inject_verifications.append(
                {
                    "target_path": target_rel_path,
                    "passed": verify_result.passed,
                    "extraction_error": verify_result.extraction_error,
                    "operation_verifications": per_op_records,
                }
            )
            if not verify_result.passed:
                if verify_result.extraction_error is not None:
                    inject_failures.append(
                        f"{target_rel_path}: marker structural corruption "
                        f"({verify_result.extraction_error})"
                    )
                else:
                    failed_summaries = [
                        f"#{v.op_index} {v.kind} {v.marker_key}: {v.status}"
                        for v in verify_result.operation_verifications
                        if v.status != inject_operations.VERIFY_STATUS_OK
                    ]
                    inject_failures.append(
                        f"{target_rel_path}: " + "; ".join(failed_summaries)
                    )
            continue
        overlay_text = render_overlay_text(
            read_text(pathlib.Path(spec["source_path"])),
            modifier_repo_root,
            compact_prompt,
        )
        live_text = read_text(live_path)
        if normalize_reasoning_defaults(target_rel_path, overlay_text, runtime=runtime) != normalize_reasoning_defaults(
            target_rel_path,
            live_text,
            runtime=runtime,
        ):
            content_mismatch.append(target_rel_path)
        if mode == "overwrite":
            backup_copy = live_root / "gsd-local-patches" / target_rel_path
            if not backup_copy.exists():
                backup_copy_missing.append(target_rel_path)

    if missing_live_targets:
        hard_failures.append(
            f"{len(missing_live_targets)} manifest entries are missing from live {runtime_root_rel_path(runtime)}"
        )
    if backup_copy_missing:
        hard_failures.append(f"{len(backup_copy_missing)} overwrite entries are missing backup copies")
    if content_mismatch:
        hard_failures.append(f"{len(content_mismatch)} live targets do not match the materialized overlay contract")
    if inject_failures:
        hard_failures.append(
            f"{len(inject_failures)} inject entries failed verify_inject_state: "
            + "; ".join(inject_failures)
        )

    return {
        "modifier_repo_root": str(modifier_repo_root),
        "live_repo_root": str(live_repo_root),
        "runtime": runtime,
        "runtime_root": runtime_root_rel_path(runtime),
        "compact_prompt_file": compact_prompt,
        "install_mutation_targets": sorted(install_mutation_targets(runtime=runtime)),
        "compatibility_declaration": {
            "path": compatibility_declaration.DECLARATION_REL_PATH,
            "schema_version": COMPATIBILITY_DECLARATION["schema_version"],
            "compatibility_posture": COMPATIBILITY_DECLARATION["compatibility_posture"],
            "runtime_basis": COMPATIBILITY_DECLARATION["runtime_basis"],
            "runtime_held_annotations": COMPATIBILITY_DECLARATION["runtime_held_annotations"],
            "runtime_profiles": COMPATIBILITY_DECLARATION["runtime_profiles"],
            "support_claims": COMPATIBILITY_DECLARATION["support_claims"],
            "mixed_runtime_policy": COMPATIBILITY_DECLARATION["mixed_runtime_policy"],
            "capability_contract": COMPATIBILITY_DECLARATION["capability_contract"],
            "declared_overlay_schema_version": declared_overlay_schema_version,
            "observed_overlay_schema_version": observed_overlay_schema_version,
            "overlay_schema_version_matches_declaration": overlay_schema_version_matches_declaration,
            "upstream_compatibility_window": COMPATIBILITY_DECLARATION["upstream_compatibility_window"],
            "parity_scan_baseline": {
                "target_runtime": COMPATIBILITY_DECLARATION["parity_scan_baseline"]["target_runtime"],
                "rule_count": len(COMPATIBILITY_DECLARATION["parity_scan_baseline"]["rules"]),
            },
        },
        "summary": {
            **validation["summary"],
            "live_target_count": len(entry_specs),
            "missing_live_target_count": len(missing_live_targets),
            "backup_copy_missing_count": len(backup_copy_missing),
            "content_mismatch_count": len(content_mismatch),
            "inject_entry_count": len(inject_verifications),
            "inject_failure_count": len(inject_failures),
            "runtime_specific_reference_hit_count": runtime_specific_reference_scan["summary"]["total_hits"],
            "runtime_specific_reference_review_needed_count": runtime_specific_reference_scan["summary"][
                "review_needed_count"
            ],
            "compatibility_declaration_rule_count": len(COMPATIBILITY_DECLARATION["parity_scan_baseline"]["rules"]),
            "overlay_schema_version_matches_declaration": overlay_schema_version_matches_declaration,
        },
        "missing_live_targets": missing_live_targets,
        "backup_copy_missing": backup_copy_missing,
        "content_mismatch": content_mismatch,
        "inject_verifications": inject_verifications,
        "inject_failures": inject_failures,
        "runtime_specific_reference_scan": runtime_specific_reference_scan,
        "hard_failures": hard_failures,
    }


def build_materialization_report(
    repo_root: pathlib.Path, compact_prompt: str, runtime: str = "codex"
) -> dict[str, Any]:
    return build_materialization_report_for_roots(repo_root, repo_root, compact_prompt, runtime=runtime)


def aggregate_runtime_reports(reports: dict[str, dict[str, Any]]) -> dict[str, Any]:
    hard_failures: list[str] = []
    for runtime, report in reports.items():
        for failure in report.get("hard_failures", []):
            hard_failures.append(f"[{runtime}] {failure}")
    return {
        "runtimes": reports,
        "summary": {
            "runtime_count": len(reports),
            "hard_failure_count": len(hard_failures),
            "failing_runtimes": sorted(runtime for runtime, report in reports.items() if report.get("hard_failures")),
        },
        "hard_failures": hard_failures,
    }


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path(args.repo_root).resolve()

    if args.command == "validate-manifest":
        runtimes = selected_runtimes(args)
        if len(runtimes) == 1:
            report = build_manifest_validation_report(
                repo_root,
                runtime=runtimes[0],
                require_backup_meta=not args.source_only,
            )
        else:
            report = aggregate_runtime_reports(
                {
                    runtime: build_manifest_validation_report(
                        repo_root,
                        runtime=runtime,
                        require_backup_meta=not args.source_only,
                    )
                    for runtime in runtimes
                }
            )
        write_json(report, pathlib.Path(args.output) if args.output else None, pretty=args.pretty or not args.output)
        return 1 if args.strict and report["hard_failures"] else 0

    if args.command == "apply-overlay":
        compact_prompt = args.compact_prompt_file or compact_prompt_file(repo_root)
        runtime = args.runtime
        written = apply_overlay(repo_root, compact_prompt, runtime=runtime)
        for rel_path in written:
            print(f"  patched {runtime_root_rel_path(runtime)}/{rel_path}")
        return 0

    if args.command == "capture-pristine-overwrites":
        report = capture_pristine_overwrites(repo_root, runtime=args.runtime)
        write_json(report, pathlib.Path(args.output) if args.output else None, pretty=args.pretty or not args.output)
        return 1 if args.strict and report["hard_failures"] else 0

    if args.command == "apply-reasoning-defaults":
        apply_reasoning_defaults(repo_root, runtime=args.runtime)
        return 0

    if args.command == "verify-materialized":
        compact_prompt = args.compact_prompt_file or compact_prompt_file(repo_root)
        runtimes = selected_runtimes(args)
        if len(runtimes) == 1:
            report = build_materialization_report(repo_root, compact_prompt, runtime=runtimes[0])
        else:
            report = aggregate_runtime_reports(
                {
                    runtime: build_materialization_report(repo_root, compact_prompt, runtime=runtime)
                    for runtime in runtimes
                }
            )
        write_json(report, pathlib.Path(args.output) if args.output else None, pretty=args.pretty or not args.output)
        return 1 if args.strict and report["hard_failures"] else 0

    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
