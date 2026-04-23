#!/usr/bin/env python3
"""Bounded harness-quality canary for machine-checkable runtime invariants."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import tomllib
from typing import Any

try:
    from harness_modifier.uplift import output_policy as uplift_output_policy
    from harness_modifier.compatibility import declaration as compatibility_declaration
    from harness_modifier.contract import portable_gsd_contract as pgc
    from harness_modifier.contract import runtime_visibility as rv
    from tooling.codex import project_uplift as pu
except ModuleNotFoundError:  # direct script invocation by path
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    from harness_modifier.uplift import output_policy as uplift_output_policy
    from harness_modifier.compatibility import declaration as compatibility_declaration
    from harness_modifier.contract import portable_gsd_contract as pgc
    from harness_modifier.contract import runtime_visibility as rv
    from tooling.codex import project_uplift as pu


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Report bounded harness canary checks.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    report = subparsers.add_parser("report", help="Emit a bounded harness canary report.")
    report.add_argument("repo_root", nargs="?", default=".")
    report.add_argument(
        "--runtime",
        choices=tuple(rv.VALID_RUNTIME_SCOPES),
        default="both",
        help="Runtime scope to inspect. Default: both.",
    )
    report.add_argument(
        "--all-supported",
        action="store_true",
        help="Inspect all supported runtimes (equivalent to --runtime both).",
    )
    report.add_argument("--output")
    report.add_argument("--pretty", action="store_true")
    report.add_argument("--strict", action="store_true")
    return parser.parse_args()


def read_text(path: pathlib.Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def read_toml(path: pathlib.Path) -> dict[str, Any] | None:
    text = read_text(path)
    if text is None:
        return None
    return tomllib.loads(text)


def make_check(name: str, status: str, summary: str, details: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "name": name,
        "status": status,
        "summary": summary,
        "details": details or {},
    }


def runtime_check_name(runtime: str, name: str) -> str:
    return f"{runtime}:{name}"


def check_runtime_version_anchor(repo_root: pathlib.Path, runtime: str) -> dict[str, Any]:
    rel_path = compatibility_declaration.version_source(runtime)
    path = repo_root / rel_path
    text = read_text(path)
    if text is None:
        return make_check(
            runtime_check_name(runtime, "runtime_version_anchor"),
            "issue",
            f"{runtime} runtime version anchor is missing",
            {"expected_path": rel_path, "runtime": runtime},
        )
    version = text.strip()
    if not version:
        return make_check(
            runtime_check_name(runtime, "runtime_version_anchor"),
            "issue",
            f"{runtime} runtime version anchor is empty",
            {"expected_path": rel_path, "runtime": runtime},
        )
    return make_check(
        runtime_check_name(runtime, "runtime_version_anchor"),
        "ok",
        f"{runtime} runtime version anchor is present",
        {"path": rel_path, "runtime": runtime, "version": version},
    )


def check_manifest_validation(repo_root: pathlib.Path, runtime: str) -> dict[str, Any]:
    report = pgc.build_manifest_validation_report(repo_root, runtime=runtime)
    hard_failures = report.get("hard_failures", [])
    if hard_failures:
        return make_check(
            runtime_check_name(runtime, "overlay_manifest_contract"),
            "issue",
            f"{runtime} overlay manifest contract has hard failures",
            {"runtime": runtime, "hard_failures": hard_failures, "summary": report.get("summary", {})},
        )
    return make_check(
        runtime_check_name(runtime, "overlay_manifest_contract"),
        "ok",
        f"{runtime} overlay manifest contract validates cleanly",
        {"runtime": runtime, "summary": report.get("summary", {})},
    )


def check_materialization(repo_root: pathlib.Path, runtime: str) -> dict[str, Any]:
    report = pgc.build_materialization_report(repo_root, pgc.compact_prompt_file(repo_root), runtime=runtime)
    hard_failures = report.get("hard_failures", [])
    if hard_failures:
        return make_check(
            runtime_check_name(runtime, "post_materialization_coherence"),
            "issue",
            f"{runtime} post-materialization coherence has hard failures",
            {"runtime": runtime, "hard_failures": hard_failures, "summary": report.get("summary", {})},
        )
    return make_check(
        runtime_check_name(runtime, "post_materialization_coherence"),
        "ok",
        f"{runtime} post-materialization coherence is aligned",
        {"runtime": runtime, "summary": report.get("summary", {})},
    )


def check_runtime_config_reasoning(repo_root: pathlib.Path, runtime: str) -> dict[str, Any]:
    if runtime != "codex":
        return make_check(
            runtime_check_name(runtime, "runtime_config_reasoning"),
            "not_applicable",
            f"{runtime} does not carry the codex-only reasoning-default config surface",
            {"runtime": runtime},
        )
    rel_path = f"{compatibility_declaration.runtime_root(runtime)}/config.toml"
    payload = read_toml(repo_root / rel_path)
    if payload is None:
        return make_check(
            runtime_check_name(runtime, "runtime_config_reasoning"),
            "issue",
            "runtime config is missing",
            {"expected_path": rel_path, "runtime": runtime},
        )
    actual = payload.get("model_reasoning_effort")
    expected = "xhigh"
    if actual != expected:
        return make_check(
            runtime_check_name(runtime, "runtime_config_reasoning"),
            "issue",
            "runtime config reasoning default drifted",
            {"path": rel_path, "expected": expected, "actual": actual, "runtime": runtime},
        )
    return make_check(
        runtime_check_name(runtime, "runtime_config_reasoning"),
        "ok",
        "runtime config reasoning default matches repo-local policy",
        {"path": rel_path, "expected": expected, "actual": actual, "runtime": runtime},
    )


def check_agent_reasoning(repo_root: pathlib.Path, runtime: str, agent_name: str, expected: str) -> dict[str, Any]:
    if runtime != "codex":
        return make_check(
            runtime_check_name(runtime, f"agent_reasoning:{agent_name}"),
            "not_applicable",
            f"{runtime} does not carry the codex-only reasoning-default agent surface for {agent_name}",
            {"runtime": runtime, "expected": expected},
        )
    rel_path = f"{compatibility_declaration.runtime_root(runtime)}/agents/{agent_name}.toml"
    payload = read_toml(repo_root / rel_path)
    if payload is None:
        return make_check(
            runtime_check_name(runtime, f"agent_reasoning:{agent_name}"),
            "issue",
            "high-stakes agent contract is missing",
            {"path": rel_path, "expected": expected, "runtime": runtime},
        )
    actual = payload.get("model_reasoning_effort")
    if actual != expected:
        return make_check(
            runtime_check_name(runtime, f"agent_reasoning:{agent_name}"),
            "issue",
            "high-stakes agent reasoning drifted",
            {"path": rel_path, "expected": expected, "actual": actual, "runtime": runtime},
        )
    return make_check(
        runtime_check_name(runtime, f"agent_reasoning:{agent_name}"),
        "ok",
        "high-stakes agent reasoning matches repo-local policy",
        {"path": rel_path, "expected": expected, "actual": actual, "runtime": runtime},
    )


def check_uplift_compatibility(repo_root: pathlib.Path) -> dict[str, Any]:
    manifest_rel_path = uplift_output_policy.load_output_policy()["manifest_rel_path"]
    manifest_path = repo_root / manifest_rel_path
    if not manifest_path.exists():
        return make_check(
            "uplift_compatibility_anchor",
            "not_applicable",
            "no uplift manifest recorded yet",
            {"manifest_path": manifest_rel_path},
        )
    note = pu.build_progress_note(repo_root)
    details = {
        "manifest_path": manifest_rel_path,
        "compatibility_basis_changed": note.get("compatibility_basis_changed", False),
        "recommend_write": note.get("recommend_write", False),
        "recommendation": note.get("recommendation"),
        "reasons": note.get("reasons", []),
    }
    if note.get("compatibility_basis_changed"):
        return make_check(
            "uplift_compatibility_anchor",
            "issue",
            "uplift compatibility anchor is stale relative to the observed runtime basis",
            details,
        )
    return make_check(
        "uplift_compatibility_anchor",
        "ok",
        "uplift compatibility anchor is aligned with the observed runtime basis",
        details,
    )


def summarize_checks(checks: list[dict[str, Any]]) -> dict[str, Any]:
    counts = {"ok": 0, "issue": 0, "not_applicable": 0}
    for check in checks:
        counts[check["status"]] = counts.get(check["status"], 0) + 1
    return {
        "status": "issue" if counts["issue"] else "ok",
        "ok_count": counts["ok"],
        "issue_count": counts["issue"],
        "not_applicable_count": counts["not_applicable"],
        "check_count": len(checks),
    }


def build_runtime_report(repo_root: pathlib.Path, runtime: str) -> dict[str, Any]:
    checks = [
        check_runtime_version_anchor(repo_root, runtime),
        check_manifest_validation(repo_root, runtime),
        check_materialization(repo_root, runtime),
        check_runtime_config_reasoning(repo_root, runtime),
    ]
    for agent_name, expected in sorted(pgc.QUALITY_REASONING.items()):
        checks.append(check_agent_reasoning(repo_root, runtime, agent_name, expected))
    return {
        "runtime": runtime,
        "profile_name": compatibility_declaration.runtime_profile(runtime)["profile_name"],
        "runtime_root": compatibility_declaration.runtime_root(runtime),
        "version_source": compatibility_declaration.version_source(runtime),
        "manifest_version_source": compatibility_declaration.manifest_version_source(runtime),
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def check_dual_runtime_core_alignment(
    runtime_reports: dict[str, dict[str, Any]],
    runtime_visibility_report: dict[str, Any],
) -> dict[str, Any]:
    required_runtimes = rv.supported_runtime_names()
    if set(runtime_reports) != set(required_runtimes):
        return make_check(
            "dual_runtime_core_alignment",
            "not_applicable",
            "dual-runtime core alignment only applies when both supported runtimes are selected",
            {
                "requested_runtimes": sorted(runtime_reports),
                "required_runtimes": required_runtimes,
            },
        )

    issue_runtimes = sorted(
        runtime
        for runtime, report in runtime_reports.items()
        if report["summary"]["issue_count"] > 0
    )
    parity_state = runtime_visibility_report["parity_state"]
    if issue_runtimes:
        return make_check(
            "dual_runtime_core_alignment",
            "issue",
            "dual-runtime core alignment is blocked by per-runtime failures",
            {
                "issue_runtimes": issue_runtimes,
                "parity_state": parity_state,
                "parity_details": runtime_visibility_report["parity_details"],
            },
        )
    if parity_state != "dual-runtime-aligned":
        return make_check(
            "dual_runtime_core_alignment",
            "issue",
            "dual-runtime scope is present but not yet fully aligned",
            {
                "parity_state": parity_state,
                "parity_details": runtime_visibility_report["parity_details"],
            },
        )
    return make_check(
        "dual_runtime_core_alignment",
        "ok",
        "dual-runtime core alignment is active and conflict-free",
        {
            "parity_state": parity_state,
            "parity_details": runtime_visibility_report["parity_details"],
        },
    )


def build_report(repo_root: pathlib.Path, runtime_scope: str = "both") -> dict[str, Any]:
    repo_root = repo_root.resolve()
    runtimes = rv.runtime_scope_runtimes(runtime_scope)
    runtime_visibility_report = rv.build_report(repo_root, runtime_scope=runtime_scope)
    runtime_reports = {runtime: build_runtime_report(repo_root, runtime) for runtime in runtimes}
    top_level_checks = [
        check_dual_runtime_core_alignment(runtime_reports, runtime_visibility_report),
        check_uplift_compatibility(repo_root),
    ]
    all_checks = [check for report in runtime_reports.values() for check in report["checks"]] + top_level_checks
    summary = summarize_checks(all_checks)
    summary.update(
        {
            "runtime_scope": runtime_scope,
            "parity_state": runtime_visibility_report["parity_state"],
            "runtime_count": len(runtime_reports),
        }
    )
    return {
        "repo_root": str(repo_root),
        "runtime_scope": runtime_scope,
        "parity_state": runtime_visibility_report["parity_state"],
        "runtime_visibility": {
            "summary": runtime_visibility_report["summary"],
            "parity_details": runtime_visibility_report["parity_details"],
        },
        "summary": summary,
        "checks": top_level_checks,
        "runtimes": runtime_reports,
    }


def write_output(payload: dict[str, Any], output: str | None, pretty: bool) -> None:
    text = json.dumps(payload, indent=2 if pretty else None, sort_keys=pretty) + "\n"
    if output is None:
        sys.stdout.write(text)
        return
    path = pathlib.Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path(args.repo_root).resolve()
    runtime_scope = "both" if args.all_supported else args.runtime
    payload = build_report(repo_root, runtime_scope=runtime_scope)
    write_output(payload, args.output, pretty=args.pretty or args.output is not None)
    if args.strict and payload["summary"]["issue_count"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
