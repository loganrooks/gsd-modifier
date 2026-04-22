#!/usr/bin/env python3
"""Compare updater boundary truth, carried-subset truth, and frozen runtime truth."""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
from collections import Counter

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


def evaluate_gates(snapshot_payload: dict, runtime_report: dict, repo_root: pathlib.Path) -> list[dict]:
    current_dirty = bool(git_output(repo_root, "status", "--short"))
    basis_commit = snapshot_payload.get("basis_commit")
    gates = [
        gate(
            "snapshot_clean_boundary",
            not snapshot_payload.get("dirty_worktree", False),
            "snapshot was captured on a clean boundary" if not snapshot_payload.get("dirty_worktree", False) else "snapshot was captured on a dirty worktree",
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
    return gates


def build_report(repo_root: pathlib.Path, snapshot_path: pathlib.Path) -> dict:
    snapshot_payload = read_json(snapshot_path)
    runtime_report = snapshot_payload["runtime_visibility_report"]
    entries = runtime_report["entries"]
    live_root = repo_root / ".codex"

    manifest_paths = rv.load_manifest_paths(live_root)
    backup_paths = rv.load_backup_paths(live_root)
    install_mutation_targets = rv.load_install_mutation_targets(repo_root)

    family_summary = dict(sorted(Counter(entry["family"] for entry in entries).items()))
    overlap_summary = {
        "manifest_total_files": len(manifest_paths),
        "backup_total_files": len(backup_paths),
        "install_mutation_target_total_files": len(install_mutation_targets),
        "selected_runtime_scope_total_entries": len(entries),
        "selected_scope_entries_in_manifest": sum(1 for entry in entries if entry["in_manifest"]),
        "selected_scope_entries_in_backup_meta": sum(1 for entry in entries if entry["in_backup_meta"]),
        "selected_scope_entries_install_mutation_targets": sum(1 for entry in entries if entry["is_install_mutation_target"]),
        "selected_scope_overlay_covered_entries": sum(1 for entry in entries if entry["overlay_exists"]),
        "selected_scope_live_only_entries": sum(1 for entry in entries if entry["live_exists"] and not entry["overlay_exists"]),
    }

    candidate_future_overlay_carry = sorted(
        entry["rel_path"] for entry in entries if entry["subclassification"] == rv.SUB_SELECTIVE_UNTRACKED
    )
    install_mutation_outside_overlay_subset = sorted(
        entry["rel_path"] for entry in entries if entry["subclassification"] == rv.SUB_SELECTIVE_INSTALL
    )
    backup_subset_inside_scope = sorted(
        entry["rel_path"] for entry in entries if entry["in_backup_meta"]
    )

    gates = evaluate_gates(snapshot_payload, runtime_report, repo_root)
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
        "current_head": git_output(repo_root, "rev-parse", "HEAD"),
        "current_branch": git_output(repo_root, "rev-parse", "--abbrev-ref", "HEAD"),
        "current_dirty_worktree": bool(git_output(repo_root, "status", "--short")),
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

    report = build_report(repo_root, snapshot_path)
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
