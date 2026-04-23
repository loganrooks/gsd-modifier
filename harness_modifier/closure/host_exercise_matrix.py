#!/usr/bin/env python3
"""Build and run the synthetic host-exercise matrix."""

from __future__ import annotations

import argparse
import json
import pathlib
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from harness_modifier.closure import host_exercise_runner
from harness_modifier.compatibility import declaration as compatibility_declaration
from harness_modifier.contract import portable_gsd_contract as pgc


@dataclass(frozen=True)
class MatrixScenario:
    scenario_id: str
    profile: str
    fixture_kind: str
    host_reference: str
    host_age_posture: str
    expected_disposition: str
    expected_compatibility_window_state: str
    expected_parity_state: str
    expected_verify_materialized_skipped: bool
    expect_zero_verify_hard_failures: bool
    narrative_summary: str


CODEX_SCENARIOS = (
    MatrixScenario(
        scenario_id="pristine-read-side",
        profile="codex",
        fixture_kind="pristine-read-side",
        host_reference="fixture-pristine-read-side",
        host_age_posture="pristine",
        expected_disposition="shift-mode",
        expected_compatibility_window_state="inside-window",
        expected_parity_state="single-runtime",
        expected_verify_materialized_skipped=True,
        expect_zero_verify_hard_failures=False,
        narrative_summary=(
            "Synthetic pristine Codex host stays inside the observed basis window but does not carry "
            "modifier materialization markers, so the run remains read-side."
        ),
    ),
    MatrixScenario(
        scenario_id="materialized-aligned",
        profile="codex",
        fixture_kind="materialized-aligned",
        host_reference="fixture-materialized-aligned",
        host_age_posture="lightly-aged",
        expected_disposition="accept",
        expected_compatibility_window_state="inside-window",
        expected_parity_state="single-runtime",
        expected_verify_materialized_skipped=False,
        expect_zero_verify_hard_failures=True,
        narrative_summary=(
            "Synthetic aligned Codex host carries the rendered overlay subset and typed backup markers, "
            "so the bounded observe-only check accepts the current contract."
        ),
    ),
    MatrixScenario(
        scenario_id="version-drift",
        profile="codex",
        fixture_kind="version-drift",
        host_reference="fixture-version-drift",
        host_age_posture="drifted",
        expected_disposition="refuse",
        expected_compatibility_window_state="outside-window",
        expected_parity_state="single-runtime",
        expected_verify_materialized_skipped=True,
        expect_zero_verify_hard_failures=False,
        narrative_summary=(
            "Synthetic drift host falls outside the observed basis version window, so the run "
            "refuses without widening runtime claims."
        ),
    ),
)

DUAL_RUNTIME_SCENARIOS = (
    MatrixScenario(
        scenario_id="dual-runtime-read-side",
        profile="dual-runtime",
        fixture_kind="dual-runtime-read-side",
        host_reference="fixture-dual-runtime-read-side",
        host_age_posture="pristine",
        expected_disposition="shift-mode",
        expected_compatibility_window_state="inside-window",
        expected_parity_state="dual-runtime-read-side",
        expected_verify_materialized_skipped=True,
        expect_zero_verify_hard_failures=False,
        narrative_summary=(
            "Synthetic mixed-runtime host carries both regular runtimes inside the observed basis window, "
            "but neither runtime has modifier markers yet, so the run remains read-side."
        ),
    ),
    MatrixScenario(
        scenario_id="dual-runtime-aligned",
        profile="dual-runtime",
        fixture_kind="dual-runtime-aligned",
        host_reference="fixture-dual-runtime-aligned",
        host_age_posture="lightly-aged",
        expected_disposition="accept",
        expected_compatibility_window_state="inside-window",
        expected_parity_state="dual-runtime-aligned",
        expected_verify_materialized_skipped=False,
        expect_zero_verify_hard_failures=True,
        narrative_summary=(
            "Synthetic mixed-runtime host carries both runtime trees with aligned modifier materialization, "
            "so the bounded observe-only check accepts the composed core profile."
        ),
    ),
    MatrixScenario(
        scenario_id="dual-runtime-core-conflict",
        profile="dual-runtime",
        fixture_kind="dual-runtime-core-conflict",
        host_reference="fixture-dual-runtime-core-conflict",
        host_age_posture="drifted",
        expected_disposition="refuse",
        expected_compatibility_window_state="outside-window",
        expected_parity_state="dual-runtime-conflict",
        expected_verify_materialized_skipped=False,
        expect_zero_verify_hard_failures=True,
        narrative_summary=(
            "Synthetic mixed-runtime host carries both runtime trees, but one runtime drifts off the observed basis, "
            "so the run refuses the composed core claim."
        ),
    ),
)

SCENARIOS = CODEX_SCENARIOS + DUAL_RUNTIME_SCENARIOS


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build and run the synthetic host-exercise matrix for codex and dual-runtime profiles."
    )
    parser.add_argument(
        "repo_root",
        nargs="?",
        default=".",
        help="Modifier repo root that owns the observed-basis overlay contract.",
    )
    parser.add_argument(
        "--profile",
        choices=("codex", "dual-runtime", "all"),
        default="all",
        help="Select which synthetic host profile set to run. Default: all.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory where the synthetic hosts, artifacts, and matrix summary are written.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when any scenario issues are detected.",
    )
    return parser.parse_args(argv)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: pathlib.Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path: pathlib.Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: pathlib.Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def host_staging_root(modifier_repo_root: pathlib.Path) -> pathlib.Path:
    return modifier_repo_root.parent / f".{modifier_repo_root.name}-host-exercise-matrix"


def load_basis_versions(modifier_repo_root: pathlib.Path, runtime: str) -> tuple[str, str]:
    basis_version = host_exercise_runner.runtime_visibility.read_runtime_version(modifier_repo_root, runtime)
    manifest_version = host_exercise_runner.runtime_visibility.read_runtime_manifest_version(
        modifier_repo_root,
        runtime,
    )
    if not isinstance(basis_version, str) or not basis_version:
        raise ValueError(f"modifier basis version missing for runtime {runtime}")
    if not isinstance(manifest_version, str) or not manifest_version:
        raise ValueError(f"modifier manifest version missing for runtime {runtime}")
    return basis_version, manifest_version


def write_runtime_basis(host_repo_root: pathlib.Path, runtime: str, version: str, manifest_version: str) -> None:
    write_text(host_repo_root / compatibility_declaration.version_source(runtime), version + "\n")
    write_json(
        host_repo_root / compatibility_declaration.manifest_version_source(runtime),
        {"version": manifest_version},
    )


def init_git_repo(host_repo_root: pathlib.Path, commit_message: str) -> None:
    subprocess.run(
        ["git", "init"],
        cwd=host_repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        ["git", "add", "."],
        cwd=host_repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Codex Test",
            "-c",
            "user.email=codex@example.com",
            "commit",
            "-m",
            commit_message,
        ],
        cwd=host_repo_root,
        check=True,
        capture_output=True,
        text=True,
    )


def render_live_overlay_entries(
    modifier_repo_root: pathlib.Path,
    runtime: str,
) -> tuple[dict[str, str], list[str]]:
    entry_specs = pgc.load_overlay_manifest_specs(modifier_repo_root, runtime=runtime)
    compact_prompt = pgc.compact_prompt_file(modifier_repo_root)
    rendered_entries: dict[str, str] = {}
    overwrite_paths: list[str] = []
    for rel_path, spec in sorted(entry_specs.items()):
        source_path = pathlib.Path(spec["source_path"])
        rendered_entries[rel_path] = pgc.render_overlay_text(
            source_path.read_text(encoding="utf-8"),
            modifier_repo_root,
            compact_prompt,
        )
        if spec["mode"] == "overwrite":
            overwrite_paths.append(rel_path)
    return rendered_entries, overwrite_paths


def materialize_aligned_host(
    modifier_repo_root: pathlib.Path,
    host_repo_root: pathlib.Path,
    runtime: str,
) -> None:
    live_root = host_repo_root / compatibility_declaration.runtime_root(runtime)
    rendered_entries, overwrite_paths = render_live_overlay_entries(modifier_repo_root, runtime)

    for rel_path, rendered_text in rendered_entries.items():
        write_text(live_root / rel_path, rendered_text)

    backup_root = live_root / "gsd-local-patches"
    write_json(
        backup_root / "backup-meta.json",
        {
            "source": "synthetic host exercise matrix placeholder carry",
            "files": overwrite_paths,
        },
    )
    for rel_path in overwrite_paths:
        write_text(
            backup_root / rel_path,
            f"Synthetic pristine placeholder for {runtime}:{rel_path}\n",
        )


def create_host_fixture(
    modifier_repo_root: pathlib.Path,
    host_repo_root: pathlib.Path,
    scenario: MatrixScenario,
) -> None:
    write_text(
        host_repo_root / "README.md",
        f"# {scenario.scenario_id}\n\nSynthetic host fixture for the host exercise matrix.\n",
    )

    codex_version, codex_manifest_version = load_basis_versions(modifier_repo_root, "codex")
    claude_version, claude_manifest_version = load_basis_versions(modifier_repo_root, "claude")

    if scenario.fixture_kind == "pristine-read-side":
        write_runtime_basis(host_repo_root, "codex", codex_version, codex_manifest_version)
        return
    if scenario.fixture_kind == "materialized-aligned":
        materialize_aligned_host(modifier_repo_root, host_repo_root, "codex")
        write_runtime_basis(host_repo_root, "codex", codex_version, codex_manifest_version)
        return
    if scenario.fixture_kind == "version-drift":
        write_runtime_basis(host_repo_root, "codex", "0.0.0-drift", "0.0.0-drift")
        return
    if scenario.fixture_kind == "dual-runtime-read-side":
        write_runtime_basis(host_repo_root, "codex", codex_version, codex_manifest_version)
        write_runtime_basis(host_repo_root, "claude", claude_version, claude_manifest_version)
        return
    if scenario.fixture_kind == "dual-runtime-aligned":
        materialize_aligned_host(modifier_repo_root, host_repo_root, "codex")
        materialize_aligned_host(modifier_repo_root, host_repo_root, "claude")
        write_runtime_basis(host_repo_root, "codex", codex_version, codex_manifest_version)
        write_runtime_basis(host_repo_root, "claude", claude_version, claude_manifest_version)
        return
    if scenario.fixture_kind == "dual-runtime-core-conflict":
        materialize_aligned_host(modifier_repo_root, host_repo_root, "codex")
        materialize_aligned_host(modifier_repo_root, host_repo_root, "claude")
        write_runtime_basis(host_repo_root, "codex", codex_version, codex_manifest_version)
        write_runtime_basis(host_repo_root, "claude", "0.0.0-drift", "0.0.0-drift")
        return
    raise ValueError(f"unknown fixture_kind: {scenario.fixture_kind}")


def expected_artifact_paths(artifact_dir: pathlib.Path, scenario_id: str) -> dict[str, pathlib.Path]:
    return {
        "packet_path": artifact_dir / f"{scenario_id}-packet.json",
        "runtime_visibility_snapshot_path": artifact_dir
        / f"{scenario_id}-runtime-visibility-snapshot.json",
        "verify_materialized_summary_path": artifact_dir
        / f"{scenario_id}-verify-materialized-summary.md",
        "observation_path": artifact_dir / f"{scenario_id}-observation.json",
    }


def verify_hard_failure_count(
    modifier_repo_root: pathlib.Path,
    host_repo_root: pathlib.Path,
    runtimes: list[str],
) -> int:
    compact_prompt = pgc.compact_prompt_file(modifier_repo_root)
    return sum(
        len(
            pgc.build_materialization_report_for_roots(
                modifier_repo_root,
                host_repo_root,
                compact_prompt,
                runtime=runtime,
            )["hard_failures"]
        )
        for runtime in runtimes
    )


def scenario_summary(
    modifier_repo_root: pathlib.Path,
    scenario: MatrixScenario,
    host_repo_root: pathlib.Path,
    artifact_paths: dict[str, pathlib.Path],
) -> dict[str, Any]:
    issues: list[str] = []
    for key, path in artifact_paths.items():
        if not path.exists():
            issues.append(f"missing expected artifact {key}: {path}")

    packet = read_json(artifact_paths["packet_path"]) or {}
    observation = read_json(artifact_paths["observation_path"]) or {}
    snapshot = read_json(artifact_paths["runtime_visibility_snapshot_path"]) or {}
    disposition = observation.get("disposition", "not_available")
    if disposition != scenario.expected_disposition:
        issues.append(
            f"expected disposition {scenario.expected_disposition!r} but saw {disposition!r}"
        )

    deployment_context = {
        row["key"]: row["value"]
        for row in observation.get("deployment_context", [])
        if isinstance(row, dict) and "key" in row
    }
    compatibility_window_state = deployment_context.get("compatibility_window_state", "not_available")
    if compatibility_window_state != scenario.expected_compatibility_window_state:
        issues.append(
            f"expected compatibility window state {scenario.expected_compatibility_window_state!r} but saw {compatibility_window_state!r}"
        )

    parity_state = deployment_context.get("parity_state", "not_available")
    if parity_state != scenario.expected_parity_state:
        issues.append(
            f"expected parity state {scenario.expected_parity_state!r} but saw {parity_state!r}"
        )

    verify_rows = [
        row
        for row in observation.get("expectation_vs_observation", [])
        if isinstance(row, dict) and row.get("check") == "verify_materialized"
    ]
    verify_skipped = any(row.get("skip_reason") == "context_deferred" for row in verify_rows)
    if verify_skipped != scenario.expected_verify_materialized_skipped:
        issues.append(
            f"expected verify_materialized_skipped={scenario.expected_verify_materialized_skipped} but saw {verify_skipped}"
        )

    verify_hard_failures = 0
    runtime_targets = packet.get("runtime_targets", [])
    if not verify_skipped and runtime_targets:
        verify_hard_failures = verify_hard_failure_count(
            modifier_repo_root,
            host_repo_root,
            runtime_targets,
        )
    if scenario.expect_zero_verify_hard_failures and verify_hard_failures:
        issues.append(
            f"scenario produced {verify_hard_failures} verify-materialized hard failures"
        )

    snapshot_parity_state = (
        snapshot.get("runtime_visibility_report", {}).get("parity_state", "not_available")
    )
    if snapshot_parity_state != scenario.expected_parity_state:
        issues.append(
            f"expected snapshot parity state {scenario.expected_parity_state!r} but saw {snapshot_parity_state!r}"
        )

    return {
        "scenario_id": scenario.scenario_id,
        "profile": scenario.profile,
        "fixture_kind": scenario.fixture_kind,
        "host_reference": scenario.host_reference,
        "host_age_posture": scenario.host_age_posture,
        "host_repo_root": str(host_repo_root),
        "expected_disposition": scenario.expected_disposition,
        "actual_disposition": disposition,
        "compatibility_window_state": compatibility_window_state,
        "parity_state": parity_state,
        "verify_materialized_skipped": verify_skipped,
        "verify_materialized_hard_failure_count": verify_hard_failures,
        "runtime_targets": runtime_targets,
        "artifact_paths": {key: str(path) for key, path in artifact_paths.items()},
        "issues": issues,
    }


def select_scenarios(profile: str) -> tuple[MatrixScenario, ...]:
    if profile == "codex":
        return CODEX_SCENARIOS
    if profile == "dual-runtime":
        return DUAL_RUNTIME_SCENARIOS
    return SCENARIOS


def run_host_exercise_matrix(
    modifier_repo_root: pathlib.Path,
    output_dir: pathlib.Path,
    profile: str = "all",
    scenarios: tuple[MatrixScenario, ...] | None = None,
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    scenario_results: list[dict[str, Any]] = []
    matrix_issues: list[str] = []
    active_scenarios = select_scenarios(profile) if scenarios is None else scenarios
    staging_root = host_staging_root(modifier_repo_root)
    staging_root.mkdir(parents=True, exist_ok=True)

    for scenario in active_scenarios:
        scenario_dir = output_dir / scenario.scenario_id
        if scenario_dir.exists():
            shutil.rmtree(scenario_dir)
        scenario_dir.mkdir(parents=True, exist_ok=True)

        host_stage_dir = staging_root / scenario.scenario_id
        if host_stage_dir.exists():
            shutil.rmtree(host_stage_dir)

        host_repo_root = host_stage_dir / "host"
        artifact_dir = scenario_dir / "artifacts"
        host_repo_root.mkdir(parents=True, exist_ok=True)

        create_host_fixture(modifier_repo_root, host_repo_root, scenario)
        init_git_repo(host_repo_root, f"{scenario.scenario_id} baseline")

        outputs = host_exercise_runner.run_host_exercise(
            modifier_repo_root=modifier_repo_root,
            host_repo_root=host_repo_root,
            output_dir=artifact_dir,
            exercise_id=scenario.scenario_id,
            host_reference=scenario.host_reference,
            host_age_posture=scenario.host_age_posture,
            narrative_summary=scenario.narrative_summary,
        )
        artifact_paths = expected_artifact_paths(artifact_dir, scenario.scenario_id)
        artifact_paths.update(outputs)

        summary = scenario_summary(
            modifier_repo_root,
            scenario,
            host_repo_root,
            artifact_paths,
        )
        if summary["issues"]:
            matrix_issues.extend(
                f"{scenario.scenario_id}: {issue}" for issue in summary["issues"]
            )
        scenario_results.append(summary)

    payload = {
        "matrix_id": "host-exercise-matrix",
        "captured_at": utc_now_iso(),
        "modifier_repo_root": str(modifier_repo_root),
        "output_dir": str(output_dir),
        "host_staging_root": str(staging_root),
        "profile": profile,
        "scenario_count": len(scenario_results),
        "status": "issue" if matrix_issues else "ok",
        "scenarios": scenario_results,
        "issues": matrix_issues,
    }
    write_json(output_dir / "matrix-summary.json", payload)
    return payload


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    modifier_repo_root = pathlib.Path(args.repo_root).resolve()
    output_dir = pathlib.Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = (modifier_repo_root / output_dir).resolve()

    payload = run_host_exercise_matrix(modifier_repo_root, output_dir, profile=args.profile)
    if args.strict and payload["status"] != "ok":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
