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
    from harness_modifier.contract import portable_gsd_contract as pgc
    from tooling.codex import project_uplift as pu
except ModuleNotFoundError:  # direct script invocation by path
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    from harness_modifier.uplift import output_policy as uplift_output_policy
    from harness_modifier.contract import portable_gsd_contract as pgc
    from tooling.codex import project_uplift as pu


RUNTIME_VERSION_REL_PATH = ".codex/get-shit-done/VERSION"
RUNTIME_CONFIG_REL_PATH = ".codex/config.toml"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Report bounded harness canary checks.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    report = subparsers.add_parser("report", help="Emit a bounded harness canary report.")
    report.add_argument("repo_root", nargs="?", default=".")
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


def check_runtime_version_anchor(repo_root: pathlib.Path) -> dict[str, Any]:
    path = repo_root / RUNTIME_VERSION_REL_PATH
    text = read_text(path)
    if text is None:
        return make_check(
            "runtime_version_anchor",
            "issue",
            "canonical runtime version anchor is missing",
            {"expected_path": RUNTIME_VERSION_REL_PATH},
        )
    version = text.strip()
    if not version:
        return make_check(
            "runtime_version_anchor",
            "issue",
            "canonical runtime version anchor is empty",
            {"expected_path": RUNTIME_VERSION_REL_PATH},
        )
    return make_check(
        "runtime_version_anchor",
        "ok",
        "canonical runtime version anchor is present",
        {"path": RUNTIME_VERSION_REL_PATH, "version": version},
    )


def check_manifest_validation(repo_root: pathlib.Path) -> dict[str, Any]:
    report = pgc.build_manifest_validation_report(repo_root)
    hard_failures = report.get("hard_failures", [])
    if hard_failures:
        return make_check(
            "overlay_manifest_contract",
            "issue",
            "overlay manifest contract has hard failures",
            {"hard_failures": hard_failures, "summary": report.get("summary", {})},
        )
    return make_check(
        "overlay_manifest_contract",
        "ok",
        "overlay manifest contract validates cleanly",
        {"summary": report.get("summary", {})},
    )


def check_materialization(repo_root: pathlib.Path) -> dict[str, Any]:
    report = pgc.build_materialization_report(repo_root, pgc.compact_prompt_file(repo_root))
    hard_failures = report.get("hard_failures", [])
    if hard_failures:
        return make_check(
            "post_materialization_coherence",
            "issue",
            "post-materialization coherence has hard failures",
            {"hard_failures": hard_failures, "summary": report.get("summary", {})},
        )
    return make_check(
        "post_materialization_coherence",
        "ok",
        "post-materialization coherence is aligned",
        {"summary": report.get("summary", {})},
    )


def check_runtime_config_reasoning(repo_root: pathlib.Path) -> dict[str, Any]:
    path = repo_root / RUNTIME_CONFIG_REL_PATH
    payload = read_toml(path)
    if payload is None:
        return make_check(
            "runtime_config_reasoning",
            "issue",
            "runtime config is missing",
            {"expected_path": RUNTIME_CONFIG_REL_PATH},
        )
    actual = payload.get("model_reasoning_effort")
    expected = "xhigh"
    if actual != expected:
        return make_check(
            "runtime_config_reasoning",
            "issue",
            "runtime config reasoning default drifted",
            {"path": RUNTIME_CONFIG_REL_PATH, "expected": expected, "actual": actual},
        )
    return make_check(
        "runtime_config_reasoning",
        "ok",
        "runtime config reasoning default matches repo-local policy",
        {"path": RUNTIME_CONFIG_REL_PATH, "expected": expected, "actual": actual},
    )


def check_agent_reasoning(repo_root: pathlib.Path, agent_name: str, expected: str) -> dict[str, Any]:
    rel_path = f".codex/agents/{agent_name}.toml"
    path = repo_root / rel_path
    payload = read_toml(path)
    if payload is None:
        return make_check(
            f"agent_reasoning:{agent_name}",
            "issue",
            "high-stakes agent contract is missing",
            {"path": rel_path, "expected": expected},
        )
    actual = payload.get("model_reasoning_effort")
    if actual != expected:
        return make_check(
            f"agent_reasoning:{agent_name}",
            "issue",
            "high-stakes agent reasoning drifted",
            {"path": rel_path, "expected": expected, "actual": actual},
        )
    return make_check(
        f"agent_reasoning:{agent_name}",
        "ok",
        "high-stakes agent reasoning matches repo-local policy",
        {"path": rel_path, "expected": expected, "actual": actual},
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


def build_report(repo_root: pathlib.Path) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    checks = [
        check_runtime_version_anchor(repo_root),
        check_manifest_validation(repo_root),
        check_materialization(repo_root),
        check_runtime_config_reasoning(repo_root),
    ]
    for agent_name, expected in sorted(pgc.QUALITY_REASONING.items()):
        checks.append(check_agent_reasoning(repo_root, agent_name, expected))
    checks.append(check_uplift_compatibility(repo_root))

    counts = {"ok": 0, "issue": 0, "not_applicable": 0}
    for check in checks:
        counts[check["status"]] = counts.get(check["status"], 0) + 1

    summary_status = "issue" if counts["issue"] else "ok"
    return {
        "repo_root": str(repo_root),
        "summary": {
            "status": summary_status,
            "ok_count": counts["ok"],
            "issue_count": counts["issue"],
            "not_applicable_count": counts["not_applicable"],
            "check_count": len(checks),
        },
        "checks": checks,
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
    payload = build_report(repo_root)
    write_output(payload, args.output, pretty=args.pretty or args.output is not None)
    if args.strict and payload["summary"]["issue_count"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
