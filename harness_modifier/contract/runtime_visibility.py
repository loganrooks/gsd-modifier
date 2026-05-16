#!/usr/bin/env python3
"""Summarize final repo-local GSD runtime truth without rewriting updater manifests."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
from collections import Counter
from dataclasses import dataclass
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from harness_modifier.compatibility import declaration as compatibility_declaration
from harness_modifier.contract import inject_operations
from harness_modifier.contract import portable_gsd_contract as pgc


DEFAULT_COMPACT_PROMPT_FILE = pgc.DEFAULT_COMPACT_PROMPT_FILE
LOCAL_COMPACT_PROMPT_SELECTOR = pgc.LOCAL_COMPACT_PROMPT_SELECTOR
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
SUB_INJECT_VERIFIED = "inject_operation_state_verified"
SUB_INJECT_UNVERIFIED = "inject_operation_state_unverified"
SUB_UNKNOWN_MISSING_LIVE = "overlay_covered_missing_from_live"
SUB_UNKNOWN_MISSING_BOTH = "missing_from_overlay_and_live"
SUB_UNKNOWN_UNRESOLVED = "unresolved_overlay_live_divergence"

SINGLE_RUNTIME_SCOPES = tuple(compatibility_declaration.supported_runtimes())
VALID_RUNTIME_SCOPES = SINGLE_RUNTIME_SCOPES + ("both",)


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
        "--runtime",
        choices=VALID_RUNTIME_SCOPES,
        default="both",
        help="Runtime scope to inspect. Default: both.",
    )
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


def read_json(path: pathlib.Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(read_text(path))


def supported_runtime_names() -> list[str]:
    return list(SINGLE_RUNTIME_SCOPES)


def runtime_scope_runtimes(runtime_scope: str) -> list[str]:
    if runtime_scope == "both":
        return supported_runtime_names()
    if runtime_scope not in SINGLE_RUNTIME_SCOPES:
        raise ValueError(f"unsupported runtime scope: {runtime_scope}")
    return [runtime_scope]


def runtime_root_rel_path(runtime: str) -> str:
    return compatibility_declaration.runtime_root(runtime)


def runtime_root_path(live_repo_root: pathlib.Path, runtime: str) -> pathlib.Path:
    return live_repo_root / runtime_root_rel_path(runtime)


def read_runtime_version(repo_root: pathlib.Path, runtime: str) -> str | None:
    path = repo_root / compatibility_declaration.version_source(runtime)
    if not path.exists():
        return None
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        return None
    return lines[0]


def read_runtime_manifest_version(repo_root: pathlib.Path, runtime: str) -> str | None:
    payload = read_json(repo_root / compatibility_declaration.manifest_version_source(runtime)) or {}
    value = payload.get("version")
    return value if isinstance(value, str) and value else None


def load_manifest_paths(runtime_root: pathlib.Path) -> set[str]:
    manifest_path = runtime_root / "gsd-file-manifest.json"
    if not manifest_path.exists():
        return set()
    manifest = json.loads(read_text(manifest_path))
    files = manifest.get("files", {})
    if isinstance(files, dict):
        return set(files.keys())
    if isinstance(files, list):
        return set(files)
    return set()


def load_backup_paths(runtime_root: pathlib.Path) -> set[str]:
    backup_meta_path = runtime_root / "gsd-local-patches" / "backup-meta.json"
    if not backup_meta_path.exists():
        return set()
    backup_meta = json.loads(read_text(backup_meta_path))
    files = backup_meta.get("files", [])
    if isinstance(files, list):
        return set(files)
    if isinstance(files, dict):
        return set(files.keys())
    return set()


def load_install_mutation_targets(repo_root: pathlib.Path, runtime: str = "codex") -> set[str]:
    return pgc.install_mutation_targets(runtime=runtime)


def compact_prompt_file(repo_root: pathlib.Path) -> str:
    return pgc.compact_prompt_file(repo_root)


def normalize_overlay_text(text: str, repo_root: pathlib.Path, compact_prompt: str) -> str:
    return pgc.render_overlay_text(text, repo_root, compact_prompt)


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


def entry_specs_for_family(
    modifier_repo_root: pathlib.Path,
    runtime: str,
    rel_glob: str,
) -> dict[str, dict[str, Any]]:
    return {
        rel_path: spec
        for rel_path, spec in pgc.load_overlay_manifest_specs(modifier_repo_root, runtime=runtime).items()
        if pathlib.PurePosixPath(rel_path).match(rel_glob)
    }


def inject_verification_payload(
    verify_result: inject_operations.VerifyResult,
) -> dict[str, Any]:
    return {
        "passed": verify_result.passed,
        "extraction_error": verify_result.extraction_error,
        "operation_verifications": [
            {
                "marker_key": verification.marker_key,
                "kind": verification.kind,
                "status": verification.status,
                "detail": verification.detail,
                "op_index": verification.op_index,
            }
            for verification in verify_result.operation_verifications
        ],
    }


def failed_inject_verification_summary(
    verify_result: inject_operations.VerifyResult,
) -> str:
    if verify_result.extraction_error is not None:
        return f"marker structural corruption: {verify_result.extraction_error}"
    failed = [
        f"#{verification.op_index} {verification.kind} {verification.marker_key}: {verification.status}"
        for verification in verify_result.operation_verifications
        if verification.status != inject_operations.VERIFY_STATUS_OK
    ]
    return "; ".join(failed) if failed else "no failed operations reported"


def empty_summary() -> dict[str, int]:
    return {
        "total_entries": 0,
        "intentional_materialized_carry": 0,
        "repo_local_config_carry": 0,
        "selective_overlay_boundary": 0,
        "obsolete_live_residue": 0,
        "unknown_live_drift": 0,
    }


def subclassification_summary(entries: list[dict[str, Any]]) -> dict[str, int]:
    return {
        key: count
        for key, count in sorted(Counter(entry["subclassification"] for entry in entries).items())
        if count
    }


def summarize_entries(entries: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "total_entries": len(entries),
        "intentional_materialized_carry": sum(1 for entry in entries if entry["classification"] == INTENTIONAL),
        "repo_local_config_carry": sum(1 for entry in entries if entry["classification"] == REPO_LOCAL),
        "selective_overlay_boundary": sum(1 for entry in entries if entry["classification"] == SELECTIVE),
        "obsolete_live_residue": sum(1 for entry in entries if entry["classification"] == OBSOLETE),
        "unknown_live_drift": sum(1 for entry in entries if entry["classification"] == UNKNOWN),
    }


def build_runtime_report_for_runtime_roots(
    modifier_repo_root: pathlib.Path,
    live_repo_root: pathlib.Path,
    runtime: str,
) -> dict[str, Any]:
    overlay_root = modifier_repo_root / "tooling" / "portable-gsd" / "overlay"
    live_root = runtime_root_path(live_repo_root, runtime)
    compact_prompt = compact_prompt_file(modifier_repo_root)
    present = live_root.exists()
    manifest_paths = load_manifest_paths(live_root) if present else set()
    backup_paths = load_backup_paths(live_root) if present else set()
    install_targets = load_install_mutation_targets(modifier_repo_root, runtime=runtime)
    entries: list[dict[str, Any]] = []

    if not overlay_root.exists():
        raise SystemExit(f"Overlay root not found: {overlay_root}")

    if present:
        for spec in SURFACE_SPECS:
            runtime_entry_specs = entry_specs_for_family(modifier_repo_root, runtime, spec.rel_glob)
            overlay_paths = set(runtime_entry_specs)
            live_paths = collect_rel_paths(live_root, spec.rel_glob)
            for rel_path in sorted(overlay_paths | live_paths):
                overlay_spec = runtime_entry_specs.get(rel_path)
                is_inject = overlay_spec is not None and overlay_spec.get("mode") == "inject"
                overlay_path = (
                    None
                    if is_inject
                    else pathlib.Path(overlay_spec["source_path"]) if overlay_spec else overlay_root / rel_path
                )
                live_path = live_root / rel_path
                overlay_exists = (
                    overlay_spec is not None
                    and (is_inject or (overlay_path is not None and overlay_path.exists()))
                )
                live_exists = live_path.exists()
                in_manifest = rel_path in manifest_paths
                in_backup_meta = rel_path in backup_paths
                is_install_mutation_target = rel_path in install_targets
                overlay_text = None
                live_text = None
                normalized_overlay = None
                raw_equal = False
                normalized_equal = False
                inject_verification = None

                if overlay_exists and not is_inject and overlay_path is not None:
                    overlay_text = read_text(overlay_path)
                    normalized_overlay = normalize_overlay_text(
                        overlay_text,
                        modifier_repo_root,
                        compact_prompt,
                    )
                if live_exists:
                    live_text = read_text(live_path)

                if overlay_text is not None and live_text is not None:
                    raw_equal = overlay_text == live_text
                if normalized_overlay is not None and live_text is not None:
                    normalized_equal = normalized_overlay == live_text

                if is_inject and live_text is not None:
                    operations = overlay_spec.get("operations", []) if overlay_spec else []
                    verify_result = inject_operations.verify_inject_state(
                        live_text,
                        operations if isinstance(operations, list) else [],
                    )
                    inject_verification = inject_verification_payload(verify_result)
                    if verify_result.passed:
                        classification = INTENTIONAL
                        subclassification = SUB_INJECT_VERIFIED
                        note = "mode: inject operation state verified against the live runtime target"
                    else:
                        classification = UNKNOWN
                        subclassification = SUB_INJECT_UNVERIFIED
                        note = (
                            "mode: inject live target failed operation-state verification: "
                            + failed_inject_verification_summary(verify_result)
                        )
                else:
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
                        "mode": overlay_spec.get("mode") if overlay_spec else None,
                        "overlay_exists": overlay_exists,
                        "live_exists": live_exists,
                        "overlay_path": str(overlay_path) if overlay_exists and overlay_path is not None else None,
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
                        "inject_verification": inject_verification,
                    }
                )

    live_version = read_runtime_version(live_repo_root, runtime)
    live_manifest_version = read_runtime_manifest_version(live_repo_root, runtime)
    observed_version = read_runtime_version(modifier_repo_root, runtime)
    observed_manifest_version = read_runtime_manifest_version(modifier_repo_root, runtime)

    return {
        "modifier_repo_root": str(modifier_repo_root),
        "live_repo_root": str(live_repo_root),
        "runtime": runtime,
        "profile_name": compatibility_declaration.runtime_profile(runtime)["profile_name"],
        "runtime_root": runtime_root_rel_path(runtime),
        "overlay_root": str(overlay_root),
        "live_root": str(live_root),
        "present": present,
        "has_modifier_materialization_marker": (live_root / "gsd-local-patches" / "backup-meta.json").exists(),
        "version_source": compatibility_declaration.version_source(runtime),
        "manifest_version_source": compatibility_declaration.manifest_version_source(runtime),
        "observed_runtime_version": observed_version,
        "live_runtime_version": live_version,
        "observed_runtime_manifest_version": observed_manifest_version,
        "live_runtime_manifest_version": live_manifest_version,
        "compact_prompt_file": compact_prompt,
        "normalized_overlay_sha_scope": "checkout-local",
        "summary": summarize_entries(entries),
        "subclassification_summary": subclassification_summary(entries),
        "entries": entries,
    }


def build_parity_assessment(runtime_reports: dict[str, dict[str, Any]]) -> dict[str, Any]:
    present_runtimes = [runtime for runtime, report in runtime_reports.items() if report["present"]]
    missing_runtimes = [runtime for runtime, report in runtime_reports.items() if not report["present"]]
    read_side_runtimes = [
        runtime
        for runtime, report in runtime_reports.items()
        if report["present"] and not report["has_modifier_materialization_marker"]
    ]
    conflicting_runtimes = [
        runtime
        for runtime, report in runtime_reports.items()
        if report["present"]
        and (
            report["summary"]["unknown_live_drift"] > 0
            or report["summary"]["obsolete_live_residue"] > 0
        )
    ]
    present_versions = {
        runtime: report["live_runtime_version"]
        for runtime, report in runtime_reports.items()
        if report["present"]
    }
    present_manifest_versions = {
        runtime: report["live_runtime_manifest_version"]
        for runtime, report in runtime_reports.items()
        if report["present"]
    }
    version_values = [value for value in present_versions.values() if value]
    manifest_values = [value for value in present_manifest_versions.values() if value]
    version_alignment = (
        len(present_versions) < 2
        or (len(version_values) == len(present_versions) and len(set(version_values)) == 1)
    )
    manifest_alignment = (
        len(present_manifest_versions) < 2
        or (len(manifest_values) == len(present_manifest_versions) and len(set(manifest_values)) == 1)
    )

    if len(present_runtimes) < 2:
        parity_state = "single-runtime"
    elif read_side_runtimes:
        parity_state = "dual-runtime-read-side"
    elif conflicting_runtimes or not version_alignment or not manifest_alignment:
        parity_state = "dual-runtime-conflict"
    else:
        parity_state = "dual-runtime-aligned"

    notes: list[str] = []
    if read_side_runtimes:
        notes.append(
            "dual-runtime repo is still read-side because one or more runtimes lack modifier-side materialization markers"
        )
    if conflicting_runtimes:
        notes.append(
            "dual-runtime repo has runtime-local unknown drift or obsolete residue in at least one present runtime"
        )
    if len(present_runtimes) >= 2 and not version_alignment:
        notes.append("present runtimes disagree on runtime version anchors")
    if len(present_runtimes) >= 2 and not manifest_alignment:
        notes.append("present runtimes disagree on manifest version anchors")

    return {
        "parity_state": parity_state,
        "present_runtimes": present_runtimes,
        "missing_runtimes": missing_runtimes,
        "read_side_runtimes": read_side_runtimes,
        "conflicting_runtimes": conflicting_runtimes,
        "version_alignment": {
            "aligned": version_alignment,
            "values": present_versions,
        },
        "manifest_alignment": {
            "aligned": manifest_alignment,
            "values": present_manifest_versions,
        },
        "notes": notes,
    }


def build_report_for_runtime_roots(
    modifier_repo_root: pathlib.Path,
    live_repo_root: pathlib.Path,
    runtime_scope: str = "both",
) -> dict[str, Any]:
    runtimes = runtime_scope_runtimes(runtime_scope)
    runtime_reports = {
        runtime: build_runtime_report_for_runtime_roots(modifier_repo_root, live_repo_root, runtime)
        for runtime in runtimes
    }
    summary = empty_summary()
    subclassifications: Counter[str] = Counter()
    for report in runtime_reports.values():
        for key, value in report["summary"].items():
            summary[key] += value
        subclassifications.update(report["subclassification_summary"])

    parity = build_parity_assessment(runtime_reports)
    summary.update(
        {
            "requested_runtime_count": len(runtimes),
            "present_runtime_count": len(parity["present_runtimes"]),
            "present_runtimes": parity["present_runtimes"],
            "missing_runtimes": parity["missing_runtimes"],
            "read_side_runtime_count": len(parity["read_side_runtimes"]),
            "dual_runtime_version_aligned": parity["version_alignment"]["aligned"],
            "dual_runtime_manifest_aligned": parity["manifest_alignment"]["aligned"],
        }
    )

    return {
        "modifier_repo_root": str(modifier_repo_root),
        "live_repo_root": str(live_repo_root),
        "runtime_scope": runtime_scope,
        "parity_state": parity["parity_state"],
        "parity_details": parity,
        "runtimes": runtime_reports,
        "normalized_overlay_sha_scope": "checkout-local",
        "summary": summary,
        "subclassification_summary": {key: count for key, count in sorted(subclassifications.items()) if count},
    }


def build_report(repo_root: pathlib.Path, runtime_scope: str = "both") -> dict[str, Any]:
    return build_report_for_runtime_roots(repo_root, repo_root, runtime_scope=runtime_scope)


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path(args.repo_root).resolve()
    report = build_report(repo_root, runtime_scope=args.runtime)
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
