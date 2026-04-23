#!/usr/bin/env python3
"""Compare updater boundary truth, carried-subset truth, and frozen runtime truth."""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
from collections import Counter
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from harness_modifier.contract import runtime_visibility as rv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build a three-surface manifest/install coherence report from updater "
            "manifest truth, carried-subset metadata, and a frozen runtime snapshot."
        )
    )
    parser.add_argument("repo_root", nargs="?", default=".")
    parser.add_argument("--snapshot", required=True, help="Path to a captured runtime snapshot JSON file.")
    parser.add_argument(
        "--runtime",
        choices=tuple(rv.VALID_RUNTIME_SCOPES),
        default="both",
        help="Runtime scope to compare against the snapshot. Default: both.",
    )
    parser.add_argument("--output", help="Optional path to write the JSON report.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any hard gate fails.",
    )
    return parser.parse_args()


def read_json(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


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


def gate(name: str, passed: bool, detail: str, severity: str = "fail") -> dict:
    return {
        "name": name,
        "passed": passed,
        "severity": severity,
        "detail": detail,
    }


def normalize_snapshot_runtime_report(snapshot_payload: dict[str, Any]) -> dict[str, Any]:
    runtime_report = snapshot_payload["runtime_visibility_report"]
    if "runtimes" in runtime_report:
        return runtime_report
    summary = runtime_report.get("summary", {})
    return {
        "runtime_scope": snapshot_payload.get("runtime_scope", "codex"),
        "parity_state": "single-runtime",
        "parity_details": {
            "parity_state": "single-runtime",
            "present_runtimes": ["codex"],
            "missing_runtimes": [],
            "read_side_runtimes": [],
            "conflicting_runtimes": [],
            "version_alignment": {"aligned": True, "values": {"codex": runtime_report.get("live_runtime_version")}},
            "manifest_alignment": {
                "aligned": True,
                "values": {"codex": runtime_report.get("live_runtime_manifest_version")},
            },
            "notes": ["legacy codex-only runtime visibility snapshot normalized for coherence checks"],
        },
        "runtimes": {"codex": runtime_report},
        "summary": summary,
        "subclassification_summary": runtime_report.get("subclassification_summary", {}),
    }


def scope_covers_request(captured_runtimes: set[str], requested_runtimes: set[str]) -> bool:
    return requested_runtimes.issubset(captured_runtimes)


def scoped_rel_path(runtime: str, rel_path: str, runtimes: list[str]) -> str:
    if len(runtimes) == 1:
        return rel_path
    return f"{runtime}:{rel_path}"


def aggregate_selected_runtime_report(
    snapshot_runtime_report: dict[str, Any],
    runtimes: list[str],
) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    summary = rv.empty_summary()
    subclassifications: Counter[str] = Counter()
    selected_runtime_reports: dict[str, dict[str, Any]] = {}
    for runtime in runtimes:
        runtime_report = snapshot_runtime_report["runtimes"].get(runtime)
        if runtime_report is None:
            continue
        runtime_report = {
            "present": True,
            "has_modifier_materialization_marker": True,
            "live_runtime_version": None,
            "live_runtime_manifest_version": None,
            "summary": rv.empty_summary(),
            "subclassification_summary": {},
            "entries": [],
            **runtime_report,
        }
        selected_runtime_reports[runtime] = runtime_report
        for key, value in runtime_report["summary"].items():
            summary[key] += value
        subclassifications.update(runtime_report.get("subclassification_summary", {}))
        for entry in runtime_report.get("entries", []):
            entries.append({"runtime": runtime, **entry})

    parity = rv.build_parity_assessment(selected_runtime_reports) if selected_runtime_reports else {
        "parity_state": "single-runtime",
        "present_runtimes": [],
        "missing_runtimes": runtimes,
        "read_side_runtimes": [],
        "conflicting_runtimes": [],
        "version_alignment": {"aligned": False, "values": {}},
        "manifest_alignment": {"aligned": False, "values": {}},
        "notes": ["requested runtime scope is absent from snapshot"],
    }
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
        "runtime_scope": "both" if len(runtimes) > 1 else runtimes[0],
        "parity_state": parity["parity_state"],
        "parity_details": parity,
        "runtimes": selected_runtime_reports,
        "summary": summary,
        "subclassification_summary": {key: count for key, count in sorted(subclassifications.items()) if count},
        "entries": entries,
    }


def evaluate_gates(
    snapshot_payload: dict,
    runtime_report: dict,
    repo_root: pathlib.Path,
    captured_runtimes: set[str] | None = None,
    requested_runtimes: set[str] | None = None,
) -> list[dict]:
    current_dirty = bool(git_output(repo_root, "status", "--short"))
    basis_commit = snapshot_payload.get("basis_commit")
    if captured_runtimes is None:
        captured_runtimes = {"codex"}
    if requested_runtimes is None:
        requested_runtimes = {"codex"}
    scope_covers = scope_covers_request(captured_runtimes, requested_runtimes)
    gates = [
        gate(
            "snapshot_scope_covers_request",
            scope_covers,
            (
                "snapshot covers the requested runtime scope"
                if scope_covers
                else f"snapshot only covers {sorted(captured_runtimes)} while report requested {sorted(requested_runtimes)}"
            ),
        ),
        gate(
            "snapshot_clean_boundary",
            not snapshot_payload.get("dirty_worktree", False),
            "snapshot was captured on a clean boundary"
            if not snapshot_payload.get("dirty_worktree", False)
            else "snapshot was captured on a dirty worktree",
        ),
        gate(
            "snapshot_basis_commit_present",
            bool(basis_commit),
            "snapshot basis commit recorded" if basis_commit else "snapshot basis commit missing",
        ),
        gate(
            "current_worktree_clean",
            not current_dirty,
            "current worktree is clean" if not current_dirty else "current worktree is dirty",
        ),
        gate(
            "selected_scope_unknown_drift_zero",
            runtime_report["summary"]["unknown_live_drift"] == 0,
            (
                "no unknown live drift inside selected runtime scope"
                if runtime_report["summary"]["unknown_live_drift"] == 0
                else f"{runtime_report['summary']['unknown_live_drift']} unknown live drift entries remain"
            ),
        ),
        gate(
            "selected_scope_obsolete_residue_zero",
            runtime_report["summary"]["obsolete_live_residue"] == 0,
            (
                "no currently evidenced obsolete live residue inside selected runtime scope"
                if runtime_report["summary"]["obsolete_live_residue"] == 0
                else f"{runtime_report['summary']['obsolete_live_residue']} obsolete residue entries remain"
            ),
        ),
    ]
    if requested_runtimes == set(rv.supported_runtime_names()):
        gates.append(
            gate(
                "selected_scope_dual_runtime_conflict_free",
                runtime_report["parity_state"] != "dual-runtime-conflict",
                (
                    "dual-runtime scope is conflict-free"
                    if runtime_report["parity_state"] != "dual-runtime-conflict"
                    else "dual-runtime scope still carries a composed conflict"
                ),
            )
        )
    return gates


def build_report(
    repo_root: pathlib.Path,
    snapshot_path: pathlib.Path,
    runtime_scope: str = "both",
) -> dict[str, Any]:
    snapshot_payload = read_json(snapshot_path)
    snapshot_runtime_report = normalize_snapshot_runtime_report(snapshot_payload)
    runtimes = rv.runtime_scope_runtimes(runtime_scope)
    runtime_report = aggregate_selected_runtime_report(snapshot_runtime_report, runtimes)
    captured_runtimes = set(snapshot_runtime_report["runtimes"])
    requested_runtimes = set(runtimes)

    family_summary = dict(sorted(Counter(entry["family"] for entry in runtime_report["entries"]).items()))
    overlap_summary: dict[str, Any] = {
        "runtime_scope": runtime_scope,
        "snapshot_runtime_scope": snapshot_runtime_report.get("runtime_scope", snapshot_payload.get("runtime_scope")),
        "selected_scope_total_entries": len(runtime_report["entries"]),
        "selected_scope_entries_in_manifest": 0,
        "selected_scope_entries_in_backup_meta": 0,
        "selected_scope_entries_install_mutation_targets": 0,
        "selected_scope_overlay_covered_entries": 0,
        "selected_scope_live_only_entries": 0,
        "manifest_total_files": 0,
        "backup_total_files": 0,
        "install_mutation_target_total_files": 0,
        "runtime_totals": {},
    }

    for runtime in runtimes:
        live_root = rv.runtime_root_path(repo_root, runtime)
        manifest_paths = rv.load_manifest_paths(live_root) if live_root.exists() else set()
        backup_paths = rv.load_backup_paths(live_root) if live_root.exists() else set()
        install_mutation_targets = rv.load_install_mutation_targets(repo_root, runtime=runtime)
        runtime_entries = [entry for entry in runtime_report["entries"] if entry["runtime"] == runtime]
        overlap_summary["runtime_totals"][runtime] = {
            "manifest_total_files": len(manifest_paths),
            "backup_total_files": len(backup_paths),
            "install_mutation_target_total_files": len(install_mutation_targets),
            "selected_scope_total_entries": len(runtime_entries),
            "selected_scope_entries_in_manifest": sum(1 for entry in runtime_entries if entry["in_manifest"]),
            "selected_scope_entries_in_backup_meta": sum(1 for entry in runtime_entries if entry["in_backup_meta"]),
            "selected_scope_entries_install_mutation_targets": sum(
                1 for entry in runtime_entries if entry["is_install_mutation_target"]
            ),
            "selected_scope_overlay_covered_entries": sum(1 for entry in runtime_entries if entry["overlay_exists"]),
            "selected_scope_live_only_entries": sum(
                1 for entry in runtime_entries if entry["live_exists"] and not entry["overlay_exists"]
            ),
        }
        overlap_summary["manifest_total_files"] += len(manifest_paths)
        overlap_summary["backup_total_files"] += len(backup_paths)
        overlap_summary["install_mutation_target_total_files"] += len(install_mutation_targets)
        overlap_summary["selected_scope_entries_in_manifest"] += overlap_summary["runtime_totals"][runtime][
            "selected_scope_entries_in_manifest"
        ]
        overlap_summary["selected_scope_entries_in_backup_meta"] += overlap_summary["runtime_totals"][runtime][
            "selected_scope_entries_in_backup_meta"
        ]
        overlap_summary["selected_scope_entries_install_mutation_targets"] += overlap_summary["runtime_totals"][
            runtime
        ]["selected_scope_entries_install_mutation_targets"]
        overlap_summary["selected_scope_overlay_covered_entries"] += overlap_summary["runtime_totals"][runtime][
            "selected_scope_overlay_covered_entries"
        ]
        overlap_summary["selected_scope_live_only_entries"] += overlap_summary["runtime_totals"][runtime][
            "selected_scope_live_only_entries"
        ]

    candidate_future_overlay_carry = sorted(
        scoped_rel_path(entry["runtime"], entry["rel_path"], runtimes)
        for entry in runtime_report["entries"]
        if entry["subclassification"] == rv.SUB_SELECTIVE_UNTRACKED
    )
    install_mutation_outside_overlay_subset = sorted(
        scoped_rel_path(entry["runtime"], entry["rel_path"], runtimes)
        for entry in runtime_report["entries"]
        if entry["subclassification"] == rv.SUB_SELECTIVE_INSTALL
    )
    backup_subset_inside_scope = sorted(
        scoped_rel_path(entry["runtime"], entry["rel_path"], runtimes)
        for entry in runtime_report["entries"]
        if entry["in_backup_meta"]
    )

    gates = evaluate_gates(
        snapshot_payload,
        runtime_report,
        repo_root,
        captured_runtimes,
        requested_runtimes,
    )
    hard_failures = [gate_info["name"] for gate_info in gates if not gate_info["passed"] and gate_info["severity"] == "fail"]

    findings = [
        {
            "name": "manifest_boundary_survives",
            "detail": (
                f"{overlap_summary['selected_scope_entries_in_manifest']} selected-scope entries are still manifest-backed, "
                "which confirms the updater/custom-file boundary remains active inside the coherence comparison."
            ),
        },
        {
            "name": "carried_subset_stays_narrow",
            "detail": (
                f"{overlap_summary['selected_scope_entries_in_backup_meta']} selected-scope entries are tracked in backup metadata, "
                "which confirms backup-meta remains a bounded carried-subset surface rather than a full runtime roster."
            ),
        },
        {
            "name": "install_mutation_boundary_is_explicit",
            "detail": (
                f"{len(install_mutation_outside_overlay_subset)} selected-scope entries are explained as install-mutation targets outside overlay carry."
            ),
        },
        {
            "name": "remaining_future_pressure_is_live_only_cohort",
            "detail": (
                f"{len(candidate_future_overlay_carry)} selected-scope entries remain untracked live-only surfaces outside the overlay subset; "
                "these are future carry/authority decisions, not current manifest-semantic contradictions."
            ),
        },
    ]

    return {
        "repo_root": str(repo_root),
        "snapshot_path": str(snapshot_path),
        "snapshot_label": snapshot_payload.get("label"),
        "snapshot_basis_commit": snapshot_payload.get("basis_commit"),
        "snapshot_dirty_worktree": snapshot_payload.get("dirty_worktree"),
        "requested_runtime_scope": runtime_scope,
        "captured_runtime_scope": snapshot_runtime_report.get("runtime_scope", snapshot_payload.get("runtime_scope")),
        "selected_runtimes": runtimes,
        "current_head": git_output(repo_root, "rev-parse", "HEAD"),
        "current_branch": git_output(repo_root, "rev-parse", "--abbrev-ref", "HEAD"),
        "current_dirty_worktree": bool(git_output(repo_root, "status", "--short")),
        "parity_state": runtime_report["parity_state"],
        "parity_details": runtime_report["parity_details"],
        "runtime_summary": runtime_report["summary"],
        "runtime_subclassification_summary": runtime_report["subclassification_summary"],
        "family_summary": family_summary,
        "overlap_summary": overlap_summary,
        "gates": gates,
        "hard_failures": hard_failures,
        "findings": findings,
        "candidate_future_overlay_carry": candidate_future_overlay_carry,
        "install_mutation_outside_overlay_subset": install_mutation_outside_overlay_subset,
        "backup_subset_inside_selected_scope": backup_subset_inside_scope,
    }


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path(args.repo_root).resolve()
    snapshot_path = pathlib.Path(args.snapshot)
    if not snapshot_path.is_absolute():
        snapshot_path = (repo_root / snapshot_path).resolve()

    report = build_report(repo_root, snapshot_path, runtime_scope=args.runtime)
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

    if args.strict and report["hard_failures"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
