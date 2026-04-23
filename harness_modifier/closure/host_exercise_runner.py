#!/usr/bin/env python3
"""Run one bounded observe-only host exercise against a disjoint host repo."""

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


def detect_runtime_targets(host_repo_root: pathlib.Path) -> list[str]:
    return [
        runtime
        for runtime in compatibility_declaration.supported_runtimes()
        if (host_repo_root / compatibility_declaration.runtime_root(runtime)).exists()
    ]


def runtime_scope_from_targets(runtime_targets: list[str]) -> str:
    if set(runtime_targets) == set(compatibility_declaration.supported_runtimes()):
        return "both"
    if len(runtime_targets) != 1:
        raise ValueError(f"unsupported runtime target set: {runtime_targets}")
    return runtime_targets[0]


def host_has_modifier_materialization_marker(host_repo_root: pathlib.Path, runtime: str) -> bool:
    return (
        host_repo_root
        / compatibility_declaration.runtime_root(runtime)
        / "gsd-local-patches"
        / "backup-meta.json"
    ).exists()


def host_has_regular_gsd(host_repo_root: pathlib.Path, runtime_targets: list[str]) -> bool:
    return all(
        (
            host_repo_root / compatibility_declaration.runtime_root(runtime) / "get-shit-done"
        ).exists()
        for runtime in runtime_targets
    )


def target_host_class(runtime_targets: list[str]) -> str:
    if runtime_targets == ["codex"]:
        return "codex-disjoint-gsd-installed-no-reflect"
    if runtime_targets == ["claude"]:
        return "claude-disjoint-gsd-installed-no-reflect"
    if set(runtime_targets) == set(compatibility_declaration.supported_runtimes()):
        return "dual-runtime-disjoint-gsd-installed-no-reflect"
    raise ValueError(f"unsupported host class for runtimes: {runtime_targets}")


def runtime_class(runtime_targets: list[str]) -> str:
    if runtime_targets == ["codex"]:
        return "codex-only"
    if runtime_targets == ["claude"]:
        return "claude-only"
    if set(runtime_targets) == set(compatibility_declaration.supported_runtimes()):
        return "dual-runtime"
    raise ValueError(f"unsupported runtime class for runtimes: {runtime_targets}")


def host_shape(runtime_targets: list[str]) -> str:
    if runtime_targets == ["codex"]:
        return "disjoint-codex-only"
    if runtime_targets == ["claude"]:
        return "disjoint-claude-only"
    if set(runtime_targets) == set(compatibility_declaration.supported_runtimes()):
        return "disjoint-dual-runtime"
    raise ValueError(f"unsupported host shape for runtimes: {runtime_targets}")


def evaluate_compatibility_window(
    modifier_repo_root: pathlib.Path,
    host_repo_root: pathlib.Path,
    runtime_targets: list[str],
) -> dict[str, Any]:
    runtime_results: dict[str, dict[str, Any]] = {}
    outside_runtimes: list[str] = []
    unknown_runtimes: list[str] = []
    for runtime in runtime_targets:
        observed_version = runtime_visibility.read_runtime_version(modifier_repo_root, runtime)
        host_version = runtime_visibility.read_runtime_version(host_repo_root, runtime)
        observed_manifest_version = runtime_visibility.read_runtime_manifest_version(modifier_repo_root, runtime)
        host_manifest_version = runtime_visibility.read_runtime_manifest_version(host_repo_root, runtime)

        if not all(isinstance(value, str) and value for value in (observed_version, host_version)):
            state = "unknown"
            reason = "runtime version missing"
            unknown_runtimes.append(runtime)
        elif not all(
            isinstance(value, str) and value
            for value in (observed_manifest_version, host_manifest_version)
        ):
            state = "unknown"
            reason = "runtime manifest version missing"
            unknown_runtimes.append(runtime)
        elif observed_version == host_version and observed_manifest_version == host_manifest_version:
            state = "inside-window"
            reason = "host runtime version and manifest version match the observed basis"
        else:
            state = "outside-window"
            reason = "host runtime version or manifest version differs from the observed basis"
            outside_runtimes.append(runtime)

        runtime_results[runtime] = {
            "runtime_root": compatibility_declaration.runtime_root(runtime),
            "state": state,
            "reason": reason,
            "observed_runtime_version": observed_version,
            "host_runtime_version": host_version,
            "observed_runtime_manifest_version": observed_manifest_version,
            "host_runtime_manifest_version": host_manifest_version,
        }

    if outside_runtimes:
        state = "outside-window"
        reason = "one or more selected runtimes differ from the observed basis"
    elif unknown_runtimes:
        state = "unknown"
        reason = "one or more selected runtimes are missing version or manifest anchors"
    else:
        state = "inside-window"
        reason = "all selected runtimes match the observed basis"

    return {
        "state": state,
        "reason": reason,
        "runtime_results": runtime_results,
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

        for rel in (
            ".codex/config.toml",
            ".claude/settings.json",
            "commands/gsd/reflect.md",
            "commands/gsd/signal.md",
        ):
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


def aggregate_materialization_reports(runtime_reports: dict[str, dict[str, Any]]) -> dict[str, Any]:
    hard_failures: list[str] = []
    summary = {
        "runtime_count": len(runtime_reports),
        "missing_live_target_count": 0,
        "backup_copy_missing_count": 0,
        "content_mismatch_count": 0,
        "runtime_specific_reference_hit_count": 0,
        "runtime_specific_reference_review_needed_count": 0,
    }
    failing_runtimes: list[str] = []
    for runtime, report in runtime_reports.items():
        summary["missing_live_target_count"] += report["summary"]["missing_live_target_count"]
        summary["backup_copy_missing_count"] += report["summary"]["backup_copy_missing_count"]
        summary["content_mismatch_count"] += report["summary"]["content_mismatch_count"]
        summary["runtime_specific_reference_hit_count"] += report["summary"]["runtime_specific_reference_hit_count"]
        summary["runtime_specific_reference_review_needed_count"] += report["summary"][
            "runtime_specific_reference_review_needed_count"
        ]
        if report["hard_failures"]:
            failing_runtimes.append(runtime)
        for failure in report["hard_failures"]:
            hard_failures.append(f"[{runtime}] {failure}")
    summary["hard_failure_count"] = len(hard_failures)
    summary["failing_runtime_count"] = len(failing_runtimes)
    return {
        "runtimes": runtime_reports,
        "summary": summary,
        "hard_failures": hard_failures,
        "failing_runtimes": failing_runtimes,
    }


def summarize_materialization_report(report: dict[str, Any]) -> str:
    lines = [
        "# Verify Materialized Summary",
        "",
        "## Summary",
    ]
    summary = report["summary"]
    for key in (
        "runtime_count",
        "missing_live_target_count",
        "backup_copy_missing_count",
        "content_mismatch_count",
        "runtime_specific_reference_hit_count",
        "runtime_specific_reference_review_needed_count",
        "hard_failure_count",
    ):
        lines.append(f"- {key}: `{summary[key]}`")

    lines.extend(["", "## Hard Failures"])
    if report["hard_failures"]:
        for failure in report["hard_failures"]:
            lines.append(f"- {failure}")
    else:
        lines.append("- none")

    for runtime, runtime_report in sorted(report["runtimes"].items()):
        lines.extend(
            [
                "",
                f"## Runtime `{runtime}`",
                f"- missing_live_target_count: `{runtime_report['summary']['missing_live_target_count']}`",
                f"- backup_copy_missing_count: `{runtime_report['summary']['backup_copy_missing_count']}`",
                f"- content_mismatch_count: `{runtime_report['summary']['content_mismatch_count']}`",
                "- requires_contextual_reread: "
                f"`{runtime_report['runtime_specific_reference_scan']['requires_contextual_reread']}`",
            ]
        )
    return "\n".join(lines) + "\n"


def summarize_skipped_materialization(missing_markers: list[str]) -> str:
    return "\n".join(
        [
            "# Verify Materialized Summary",
            "",
            "## Summary",
            "- status: `skipped`",
            "- reason: `one or more selected runtimes lack modifier-side pristine/materialization markers`",
            f"- missing_runtime_markers: `{', '.join(missing_markers)}`",
            "",
            "## Note",
            "- full verify-materialized was intentionally not run because the host does not yet carry the modifier-side pristine/materialization marker for every selected runtime",
            "",
        ]
    )


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
    if materialization_report["summary"]["runtime_specific_reference_review_needed_count"] > 0:
        return "warn"
    return "accept"


def compatibility_outcome(compatibility_window: dict[str, Any]) -> str:
    if compatibility_window["state"] == "outside-window":
        return "refuse"
    if compatibility_window["state"] == "inside-window":
        return "accept"
    return "warn"


def parity_outcome(parity_state: str) -> str:
    if parity_state == "dual-runtime-aligned":
        return "accept"
    if parity_state == "dual-runtime-read-side":
        return "shift-mode"
    if parity_state == "dual-runtime-conflict":
        return "refuse"
    return "accept"


def build_observation_payload(
    packet: dict[str, Any],
    packet_path: pathlib.Path,
    host_state: dict[str, Any],
    compatibility_window: dict[str, Any],
    reflect_artifacts: list[dict[str, str]],
    runtime_visibility_report: dict[str, Any],
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
            "check_outcome": compatibility_outcome(compatibility_window),
        },
        {
            "check": "runtime_visibility_snapshot",
            "check_outcome": "accept",
        },
    ]
    if len(packet["runtime_targets"]) > 1:
        expectation_rows.append(
            {
                "check": "dual_runtime_alignment",
                "check_outcome": parity_outcome(runtime_visibility_report["parity_state"]),
            }
        )
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
                "summary": "Host is inside the observed-basis version window but does not yet carry the modifier-side pristine/materialization marker for every selected runtime, so verify-materialized stayed deferred and the run remained read-side.",
            }
        )
    elif materialization_report is not None and materialization_report["summary"]["missing_live_target_count"] > 0:
        semantic_deviation.append(
            {
                "signal_subtype": "contract-mismatch",
                "summary": "Host live runtime does not yet match the modifier materialization contract; observe-only run should stay read-side.",
            }
        )
    elif len(packet["runtime_targets"]) > 1 and runtime_visibility_report["parity_state"] == "dual-runtime-conflict":
        semantic_deviation.append(
            {
                "signal_subtype": "parity-classifier-drift",
                "summary": "Dual-runtime host is present but not yet aligned across the composed runtime proof surfaces.",
            }
        )
    elif (
        materialization_report is not None
        and materialization_report["summary"]["runtime_specific_reference_review_needed_count"] > 0
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
            "summary": "Observe-only host exercise now carries packet, snapshot, and materialization-summary evidence in one durable record.",
        }
    ]

    host_runtime_versions = {
        runtime: row["host_runtime_version"]
        for runtime, row in compatibility_window["runtime_results"].items()
    }
    host_runtime_manifest_versions = {
        runtime: row["host_runtime_manifest_version"]
        for runtime, row in compatibility_window["runtime_results"].items()
    }

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
            {"key": "compatibility_window_reason", "value": compatibility_window["reason"] or "not_available"},
            {"key": "runtime_targets", "value": ",".join(packet["runtime_targets"])},
            {"key": "parity_state", "value": runtime_visibility_report["parity_state"]},
            {
                "key": "host_runtime_versions",
                "value": json.dumps(host_runtime_versions, sort_keys=True),
            },
            {
                "key": "host_runtime_manifest_versions",
                "value": json.dumps(host_runtime_manifest_versions, sort_keys=True),
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
    runtime_targets: list[str],
    compatibility_window: dict[str, Any],
    runtime_visibility_report: dict[str, Any],
) -> dict[str, Any]:
    host_state = host_git_state(host_repo_root)
    packet_policy = host_exercise_packet_writer.host_exercise_packet_policy()
    reflect_artifacts = detect_reflect_artifacts(host_repo_root, packet_policy)
    declaration = compatibility_declaration.load_declaration()
    held_annotations = declaration.get("runtime_held_annotations", [])
    held_annotation_runtime = held_annotations[0]["runtime"] if held_annotations else "not_available"
    all_materialized = all(
        host_has_modifier_materialization_marker(host_repo_root, runtime) for runtime in runtime_targets
    )
    payload = {
        "packet_id": exercise_id,
        "target_host_class": target_host_class(runtime_targets),
        "host_reference": host_reference,
        "host_repo_path": str(host_repo_root),
        "runtime_targets": runtime_targets,
        "runtime_results": {
            runtime: {
                "runtime_root": compatibility_declaration.runtime_root(runtime),
                "compatibility_window_state": result["state"],
            }
            for runtime, result in compatibility_window["runtime_results"].items()
        },
        "parity_state": runtime_visibility_report["parity_state"],
        "runtime_class": runtime_class(runtime_targets),
        "host_shape": host_shape(runtime_targets),
        "host_has_regular_gsd": host_has_regular_gsd(host_repo_root, runtime_targets),
        "host_has_reflect_artifacts": bool(reflect_artifacts),
        "host_has_reflect_artifacts_rationale": (
            "No Reflect-specific artifacts or tokens detected."
            if not reflect_artifacts
            else "Detected: " + ", ".join(item["entry"] for item in reflect_artifacts)
        ),
        "host_age_posture": host_age_posture,
        "declaration_capture": {
            "declaration_posture": declaration["compatibility_posture"],
            "observed_basis_runtime": declaration["runtime_basis"]["runtime"],
            "held_annotation_runtime": held_annotation_runtime,
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
    if not all_materialized:
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
    runtime_targets = detect_runtime_targets(host_repo_root)
    if not runtime_targets:
        raise ValueError("host repo does not carry any supported runtime roots")
    runtime_scope = runtime_scope_from_targets(runtime_targets)
    compatibility_window = evaluate_compatibility_window(
        modifier_repo_root,
        host_repo_root,
        runtime_targets,
    )
    runtime_visibility_report = runtime_visibility.build_report_for_runtime_roots(
        modifier_repo_root,
        host_repo_root,
        runtime_scope=runtime_scope,
    )
    packet_payload = build_packet_payload(
        modifier_repo_root,
        host_repo_root,
        output_dir,
        exercise_id,
        host_reference,
        host_age_posture,
        runtime_targets,
        compatibility_window,
        runtime_visibility_report,
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
        "runtime_scope": runtime_scope,
        "modifier_repo_root": str(modifier_repo_root),
        "host_repo_root": str(host_repo_root),
        "modifier_basis_commit": git_output(modifier_repo_root, "rev-parse", "HEAD"),
        "host_basis_commit": host_state["basis_commit"],
        "host_branch": host_state["branch"],
        "dirty_worktree": host_state["dirty_worktree"],
        "runtime_visibility_report": runtime_visibility_report,
    }
    runtime_snapshot_path.write_text(json.dumps(runtime_snapshot, indent=2) + "\n", encoding="utf-8")

    verify_summary_path = pathlib.Path(packet["output_targets"]["verify_materialized_summary"])
    missing_markers = [
        runtime for runtime in runtime_targets if not host_has_modifier_materialization_marker(host_repo_root, runtime)
    ]
    verify_materialized_skipped = bool(missing_markers)
    materialization_report: dict[str, Any] | None = None
    if verify_materialized_skipped:
        verify_summary_path.write_text(
            summarize_skipped_materialization(missing_markers),
            encoding="utf-8",
        )
    else:
        compact_prompt = pgc.compact_prompt_file(modifier_repo_root)
        runtime_materialization_reports = {
            runtime: pgc.build_materialization_report_for_roots(
                modifier_repo_root,
                host_repo_root,
                compact_prompt,
                runtime=runtime,
            )
            for runtime in runtime_targets
        }
        materialization_report = aggregate_materialization_reports(runtime_materialization_reports)
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
        runtime_visibility_report,
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
    print(json.dumps({key: str(path) for key, path in outputs.items()}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
