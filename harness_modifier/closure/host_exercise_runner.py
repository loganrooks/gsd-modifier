#!/usr/bin/env python3
"""Run one bounded observe-only host exercise against a disjoint Codex host."""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
from datetime import datetime, timezone
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from harness_modifier.closure import host_exercise_packet_writer
from harness_modifier.closure import observation_writer
from harness_modifier.compatibility import declaration as compatibility_declaration
from harness_modifier.contract import portable_gsd_contract as pgc
from harness_modifier.contract import runtime_visibility


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run one bounded observe-only host exercise without mutating the host repo."
    )
    parser.add_argument("host_repo", help="Path to the disjoint host repo.")
    parser.add_argument(
        "--modifier-repo-root",
        default=str(REPO_ROOT),
        help="Modifier repo root that owns the overlay/install contract.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory where packet, observation, snapshot, and summary artifacts are written.",
    )
    parser.add_argument(
        "--exercise-id",
        required=True,
        help="Stable exercise id used to name durable artifacts.",
    )
    parser.add_argument(
        "--host-reference",
        help="Short human-facing host reference. Defaults to the host repo directory name.",
    )
    parser.add_argument(
        "--host-age-posture",
        default="lightly-aged",
        choices=tuple(
            host_exercise_packet_writer.host_exercise_packet_policy()["host_age_posture_vocab"]
        ),
        help="Declared host age posture for this packet.",
    )
    parser.add_argument(
        "--narrative-summary",
        help="Optional terse interpretation to preserve inside the observation record.",
    )
    return parser.parse_args()


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: pathlib.Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def read_runtime_version(repo_root: pathlib.Path, rel_path: str) -> str | None:
    path = repo_root / rel_path
    if not path.exists():
        return None
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        return None
    return lines[0]


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


def host_git_state(host_repo_root: pathlib.Path) -> dict[str, Any]:
    return {
        "basis_commit": git_output(host_repo_root, "rev-parse", "HEAD"),
        "branch": git_output(host_repo_root, "rev-parse", "--abbrev-ref", "HEAD"),
        "dirty_worktree": bool(git_output(host_repo_root, "status", "--short")),
    }


def evaluate_compatibility_window(
    modifier_repo_root: pathlib.Path,
    host_repo_root: pathlib.Path,
) -> dict[str, str | None]:
    declaration = compatibility_declaration.load_declaration()
    basis_version = read_runtime_version(modifier_repo_root, declaration["runtime_basis"]["version_source"])
    host_version = read_runtime_version(host_repo_root, declaration["runtime_basis"]["version_source"])
    basis_manifest = read_json(modifier_repo_root / declaration["runtime_basis"]["manifest_version_source"]) or {}
    host_manifest = read_json(host_repo_root / declaration["runtime_basis"]["manifest_version_source"]) or {}
    basis_manifest_version = basis_manifest.get("version")
    host_manifest_version = host_manifest.get("version")

    if not all(isinstance(value, str) and value for value in (basis_version, host_version)):
        return {
            "state": "unknown",
            "reason": "runtime version missing",
            "observed_runtime_version": basis_version,
            "host_runtime_version": host_version,
            "observed_runtime_manifest_version": basis_manifest_version,
            "host_runtime_manifest_version": host_manifest_version,
        }

    if not all(
        isinstance(value, str) and value
        for value in (basis_manifest_version, host_manifest_version)
    ):
        return {
            "state": "unknown",
            "reason": "runtime manifest version missing",
            "observed_runtime_version": basis_version,
            "host_runtime_version": host_version,
            "observed_runtime_manifest_version": basis_manifest_version,
            "host_runtime_manifest_version": host_manifest_version,
        }

    if basis_version == host_version and basis_manifest_version == host_manifest_version:
        return {
            "state": "inside-window",
            "reason": "host runtime version and manifest version match the observed basis",
            "observed_runtime_version": basis_version,
            "host_runtime_version": host_version,
            "observed_runtime_manifest_version": basis_manifest_version,
            "host_runtime_manifest_version": host_manifest_version,
        }

    return {
        "state": "outside-window",
        "reason": "host runtime version or manifest version differs from the observed basis",
        "observed_runtime_version": basis_version,
        "host_runtime_version": host_version,
        "observed_runtime_manifest_version": basis_manifest_version,
        "host_runtime_manifest_version": host_manifest_version,
    }


def detect_reflect_artifacts(
    host_repo_root: pathlib.Path,
    packet_policy: dict[str, Any],
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for entry in packet_policy["reflect_artifact_abort_list"]:
        if "/" in entry or entry.endswith("/"):
            candidate = host_repo_root / entry
            if candidate.exists():
                findings.append(
                    {
                        "kind": "path",
                        "entry": entry,
                        "match": str(candidate),
                    }
                )
            continue

        for rel in (".codex/config.toml", ".claude/settings.json", "commands/gsd/reflect.md"):
            candidate = host_repo_root / rel
            if not candidate.exists() or not candidate.is_file():
                continue
            try:
                text = candidate.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if entry in text:
                findings.append(
                    {
                        "kind": "token",
                        "entry": entry,
                        "match": str(candidate.relative_to(host_repo_root)),
                    }
                )
    return findings


def summarize_materialization_report(report: dict[str, Any]) -> str:
    lines = [
        "# Verify Materialized Summary",
        "",
        "## Summary",
    ]
    summary = report["summary"]
    for key in (
        "live_target_count",
        "missing_live_target_count",
        "backup_copy_missing_count",
        "content_mismatch_count",
        "runtime_specific_reference_hit_count",
        "runtime_specific_reference_review_needed_count",
    ):
        lines.append(f"- {key}: `{summary[key]}`")

    lines.extend(["", "## Hard Failures"])
    if report["hard_failures"]:
        for failure in report["hard_failures"]:
            lines.append(f"- {failure}")
    else:
        lines.append("- none")

    lines.extend(["", "## Runtime Specific Reference Review Needed"])
    lines.append(
        f"- requires_contextual_reread: `{report['runtime_specific_reference_scan']['requires_contextual_reread']}`"
    )
    return "\n".join(lines) + "\n"


def summarize_skipped_materialization(reason: str) -> str:
    return "\n".join(
        [
            "# Verify Materialized Summary",
            "",
            "## Summary",
            "- status: `skipped`",
            f"- reason: `{reason}`",
            "",
            "## Note",
            "- full verify-materialized was intentionally not run because the host does not yet carry the modifier-side pristine/materialization marker",
            "",
        ]
    )


def host_has_modifier_materialization_marker(host_repo_root: pathlib.Path) -> bool:
    return (host_repo_root / ".codex" / "gsd-local-patches" / "backup-meta.json").exists()


def derive_disposition(
    reflect_artifacts: list[dict[str, str]],
    host_state: dict[str, Any],
    compatibility_window: dict[str, Any],
    materialization_report: dict[str, Any] | None,
    verify_materialized_skipped: bool,
) -> str:
    if reflect_artifacts:
        return "refuse"
    if host_state["dirty_worktree"] or not host_state["basis_commit"]:
        return "refuse"
    if compatibility_window["state"] == "outside-window":
        return "refuse"
    if verify_materialized_skipped:
        return "shift-mode"
    if materialization_report is None:
        return "warn"
    if materialization_report["summary"]["missing_live_target_count"] > 0:
        return "shift-mode"
    if materialization_report["hard_failures"]:
        return "warn"
    if materialization_report["runtime_specific_reference_scan"]["requires_contextual_reread"]:
        return "warn"
    return "accept"


def build_observation_payload(
    packet: dict[str, Any],
    packet_path: pathlib.Path,
    host_state: dict[str, Any],
    compatibility_window: dict[str, Any],
    reflect_artifacts: list[dict[str, str]],
    runtime_snapshot_path: pathlib.Path,
    verify_summary_path: pathlib.Path,
    materialization_report: dict[str, Any] | None,
    verify_materialized_skipped: bool,
    narrative_summary: str | None,
) -> dict[str, Any]:
    disposition = derive_disposition(
        reflect_artifacts,
        host_state,
        compatibility_window,
        materialization_report,
        verify_materialized_skipped,
    )

    expectation_rows: list[dict[str, Any]] = [
        {
            "check": "reflect_artifact_scan",
            "check_outcome": "refuse" if reflect_artifacts else "accept",
        },
        {
            "check": "host_clean_worktree",
            "check_outcome": "refuse" if host_state["dirty_worktree"] else "accept",
        },
        {
            "check": "host_known_basis_commit",
            "check_outcome": "accept" if host_state["basis_commit"] else "refuse",
        },
        {
            "check": "compatibility_window",
            "check_outcome": (
                "refuse"
                if compatibility_window["state"] == "outside-window"
                else "accept"
                if compatibility_window["state"] == "inside-window"
                else "warn"
            ),
        },
        {
            "check": "runtime_visibility_snapshot",
            "check_outcome": "accept",
        },
    ]
    if verify_materialized_skipped:
        expectation_rows.append(
            {
                "check": "verify_materialized",
                "skip_reason": "context_deferred",
            }
        )
    elif materialization_report is not None:
        expectation_rows.append(
            {
                "check": "verify_materialized",
                "check_outcome": (
                    "shift-mode"
                    if materialization_report["summary"]["missing_live_target_count"] > 0
                    else "warn"
                    if materialization_report["hard_failures"]
                    else "accept"
                ),
            }
        )

    semantic_deviation: list[dict[str, Any]] = []
    if reflect_artifacts:
        semantic_deviation.append(
            {
                "signal_subtype": "capability-gap",
                "summary": "Host carries Reflect-specific artifacts and is outside the first-host class.",
            }
        )
    elif compatibility_window["state"] == "outside-window":
        semantic_deviation.append(
            {
                "signal_subtype": "config-mismatch",
                "summary": "Host runtime version or manifest version lies outside the declared observed-basis compatibility window.",
            }
        )
    elif verify_materialized_skipped:
        semantic_deviation.append(
            {
                "signal_subtype": "contract-mismatch",
                "summary": "Host is inside the observed-basis version window but does not yet carry the modifier-side pristine/materialization marker, so verify-materialized stayed deferred and the run remained read-side.",
            }
        )
    elif materialization_report is not None and materialization_report["summary"]["missing_live_target_count"] > 0:
        semantic_deviation.append(
            {
                "signal_subtype": "contract-mismatch",
                "summary": "Host live runtime does not yet match the modifier materialization contract; observe-only run should stay read-side.",
            }
        )
    elif (
        materialization_report is not None
        and materialization_report["runtime_specific_reference_scan"]["requires_contextual_reread"]
    ):
        semantic_deviation.append(
            {
                "signal_subtype": "parity-classifier-drift",
                "summary": "Runtime-specific references need contextual reread before the host can be read as a cleaner parity sample.",
            }
        )

    positive_gain = [
        {
            "signal_subtype": "verification-surface-sharpened",
            "summary": "First disjoint host exercise now carries packet, snapshot, and materialization-summary evidence in one durable record.",
        }
    ]

    payload: dict[str, Any] = {
        "observation_id": f"{packet['packet_id']}-observation",
        "observed_at": utc_now_iso(),
        "basis_commit": packet["declaration_capture"]["basis_commit"],
        "exercise_id": packet["packet_id"],
        "target_host_class": packet["target_host_class"],
        "evidence_family": "derived",
        "disposition": disposition,
        "deployment_context": [
            {"key": "host_reference", "value": packet["host_reference"]},
            {"key": "host_repo_path", "value": packet["host_repo_path"]},
            {"key": "host_age_posture", "value": packet["host_age_posture"]},
            {"key": "host_branch", "value": host_state["branch"] or "not_available"},
            {"key": "host_basis_commit", "value": host_state["basis_commit"] or "not_available"},
            {"key": "declaration_posture", "value": packet["declaration_capture"]["declaration_posture"]},
            {
                "key": "observed_basis_runtime",
                "value": packet["declaration_capture"]["observed_basis_runtime"],
            },
            {
                "key": "held_annotation_runtime",
                "value": packet["declaration_capture"]["held_annotation_runtime"],
            },
            {
                "key": "compatibility_window_state",
                "value": packet["declaration_capture"]["compatibility_window_state"],
            },
            {
                "key": "compatibility_window_reason",
                "value": compatibility_window["reason"] or "not_available",
            },
            {
                "key": "host_runtime_version",
                "value": compatibility_window["host_runtime_version"] or "not_available",
            },
            {
                "key": "host_runtime_manifest_version",
                "value": compatibility_window["host_runtime_manifest_version"] or "not_available",
            },
            {"key": "reflect_artifact_count", "value": len(reflect_artifacts)},
            {"key": "runtime_visibility_snapshot_path", "value": str(runtime_snapshot_path)},
            {"key": "verify_materialized_summary_path", "value": str(verify_summary_path)},
        ],
        "expectation_vs_observation": expectation_rows,
        "semantic_deviation": semantic_deviation,
        "positive_gain": positive_gain,
        "measurement_provenance": {
            "detected_by": {
                "runtime": "codex",
                "helper": "harness_modifier.closure.host_exercise_runner",
            },
            "written_by": {
                "runtime": "codex",
                "helper": "harness_modifier.closure.host_exercise_runner",
            },
            "about_work": {
                "bundle_family": packet["bundle_family"],
                "packet_path": str(packet_path),
            },
        },
    }
    if narrative_summary:
        payload["narrative_summary"] = narrative_summary
    return payload


def build_packet_payload(
    modifier_repo_root: pathlib.Path,
    host_repo_root: pathlib.Path,
    output_dir: pathlib.Path,
    exercise_id: str,
    host_reference: str,
    host_age_posture: str,
    compatibility_window: dict[str, Any],
) -> dict[str, Any]:
    host_state = host_git_state(host_repo_root)
    packet_policy = host_exercise_packet_writer.host_exercise_packet_policy()
    reflect_artifacts = detect_reflect_artifacts(host_repo_root, packet_policy)
    payload = {
        "packet_id": exercise_id,
        "target_host_class": "codex-disjoint-gsd-installed-no-reflect",
        "host_reference": host_reference,
        "host_repo_path": str(host_repo_root),
        "runtime_class": "codex-only",
        "host_shape": "disjoint-codex-only",
        "host_has_regular_gsd": (host_repo_root / ".codex" / "get-shit-done").exists(),
        "host_has_reflect_artifacts": bool(reflect_artifacts),
        "host_has_reflect_artifacts_rationale": (
            "No Reflect-specific artifacts or tokens detected."
            if not reflect_artifacts
            else "Detected: " + ", ".join(item["entry"] for item in reflect_artifacts)
        ),
        "host_age_posture": host_age_posture,
        "declaration_capture": {
            "basis_commit": host_state["basis_commit"] or "unknown",
            "dirty_worktree": host_state["dirty_worktree"],
            "compatibility_window_state": compatibility_window["state"],
        },
        "output_targets": {
            "observation_record_path": str(output_dir / f"{exercise_id}-observation.json"),
            "runtime_visibility_snapshot_path": str(
                output_dir / f"{exercise_id}-runtime-visibility-snapshot.json"
            ),
            "verify_materialized_summary": str(
                output_dir / f"{exercise_id}-verify-materialized-summary.md"
            ),
        },
    }
    if not host_has_modifier_materialization_marker(host_repo_root):
        payload["preflight_reads"] = host_exercise_packet_writer.host_exercise_packet_policy()[
            "required_preflight_reads"
        ]
    return payload


def run_host_exercise(
    modifier_repo_root: pathlib.Path,
    host_repo_root: pathlib.Path,
    output_dir: pathlib.Path,
    exercise_id: str,
    host_reference: str,
    host_age_posture: str,
    narrative_summary: str | None = None,
) -> dict[str, pathlib.Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    compatibility_window = evaluate_compatibility_window(modifier_repo_root, host_repo_root)
    packet_payload = build_packet_payload(
        modifier_repo_root,
        host_repo_root,
        output_dir,
        exercise_id,
        host_reference,
        host_age_posture,
        compatibility_window,
    )
    packet_path = output_dir / f"{exercise_id}-packet.json"
    packet = host_exercise_packet_writer.write_host_exercise_packet(packet_path, packet_payload)

    host_state = host_git_state(host_repo_root)
    reflect_artifacts = detect_reflect_artifacts(
        host_repo_root,
        host_exercise_packet_writer.host_exercise_packet_policy(),
    )

    runtime_snapshot_path = pathlib.Path(packet["output_targets"]["runtime_visibility_snapshot_path"])
    runtime_snapshot = {
        "captured_at": utc_now_iso(),
        "label": exercise_id,
        "modifier_repo_root": str(modifier_repo_root),
        "host_repo_root": str(host_repo_root),
        "modifier_basis_commit": git_output(modifier_repo_root, "rev-parse", "HEAD"),
        "host_basis_commit": host_state["basis_commit"],
        "host_branch": host_state["branch"],
        "dirty_worktree": host_state["dirty_worktree"],
        "runtime_visibility_report": runtime_visibility.build_report_for_runtime_roots(
            modifier_repo_root,
            host_repo_root,
        ),
    }
    runtime_snapshot_path.write_text(json.dumps(runtime_snapshot, indent=2) + "\n", encoding="utf-8")

    verify_summary_path = pathlib.Path(packet["output_targets"]["verify_materialized_summary"])
    verify_materialized_skipped = not host_has_modifier_materialization_marker(host_repo_root)
    materialization_report: dict[str, Any] | None = None
    if verify_materialized_skipped:
        verify_summary_path.write_text(
            summarize_skipped_materialization(
                "host lacks modifier-side pristine/materialization marker (.codex/gsd-local-patches/backup-meta.json)"
            ),
            encoding="utf-8",
        )
    else:
        compact_prompt = pgc.compact_prompt_file(modifier_repo_root)
        materialization_report = pgc.build_materialization_report_for_roots(
            modifier_repo_root,
            host_repo_root,
            compact_prompt,
        )
        verify_summary_path.write_text(
            summarize_materialization_report(materialization_report),
            encoding="utf-8",
        )

    observation_payload = build_observation_payload(
        packet,
        packet_path,
        host_state,
        compatibility_window,
        reflect_artifacts,
        runtime_snapshot_path,
        verify_summary_path,
        materialization_report,
        verify_materialized_skipped,
        narrative_summary,
    )
    if observation_payload["basis_commit"] != packet["declaration_capture"]["basis_commit"]:
        raise ValueError("packet/observation basis_commit must agree")

    observation_path = pathlib.Path(packet["output_targets"]["observation_record_path"])
    observation_writer.write_observation_record(observation_path, observation_payload)
    return {
        "packet_path": packet_path,
        "runtime_visibility_snapshot_path": runtime_snapshot_path,
        "verify_materialized_summary_path": verify_summary_path,
        "observation_path": observation_path,
    }


def main() -> int:
    args = parse_args()
    modifier_repo_root = pathlib.Path(args.modifier_repo_root).resolve()
    host_repo_root = pathlib.Path(args.host_repo).resolve()
    output_dir = pathlib.Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = (modifier_repo_root / output_dir).resolve()
    host_reference = args.host_reference or host_repo_root.name

    outputs = run_host_exercise(
        modifier_repo_root=modifier_repo_root,
        host_repo_root=host_repo_root,
        output_dir=output_dir,
        exercise_id=args.exercise_id,
        host_reference=host_reference,
        host_age_posture=args.host_age_posture,
        narrative_summary=args.narrative_summary,
    )
    for key, value in outputs.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
