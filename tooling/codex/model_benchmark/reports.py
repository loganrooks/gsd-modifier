"""Aggregation helpers for model benchmark run records."""

from __future__ import annotations

from decimal import Decimal
from typing import Any

from tooling.codex.model_benchmark.enums import (
    COMPARABILITY_VALUES,
    CONTENT_CONTRACTS,
    COST_EVIDENCE_MODES,
    EVIDENCE_CLASSES,
    OBSERVATION_STATUSES,
    RELIABILITY_MODES,
)
from tooling.codex.model_benchmark import query
from tooling.codex.model_benchmark.schema import NOT_AVAILABLE, total_known_tokens, validate_run_record


def _key(record: dict[str, Any]) -> tuple[str, str, str]:
    return (record["task_id"], record["candidate_profile"], record["reasoning_effort"])


def _score_value(record: dict[str, Any]) -> float | None:
    score = record.get("score")
    if not isinstance(score, dict):
        return None
    value = score.get("overall")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)
    return None


def _numeric_value(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _cost_value(record: dict[str, Any]) -> Decimal | None:
    cost = record.get("cost_estimate")
    if not isinstance(cost, dict):
        return None
    value = cost.get("total_estimated_cost")
    if value in (None, NOT_AVAILABLE):
        return None
    return Decimal(str(value))


def _cost_status(record: dict[str, Any]) -> str | None:
    cost = record.get("cost_estimate")
    if not isinstance(cost, dict):
        return None
    value = cost.get("estimate_status")
    return value if isinstance(value, str) else None


def summarize_runs(records: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[tuple[str, str, str], dict[str, Any]] = {}
    for raw_record in records:
        record = validate_run_record(raw_record)
        group = groups.setdefault(
            _key(record),
            {
                "task_id": record["task_id"],
                "candidate_profile": record["candidate_profile"],
                "reasoning_effort": record["reasoning_effort"],
                "run_count": 0,
                "completed_count": 0,
                "qualitative_only_count": 0,
                "known_token_total": 0,
                "known_token_run_count": 0,
                "reasoning_token_total": 0,
                "reasoning_token_run_count": 0,
                "estimated_cost_total": Decimal("0"),
                "estimated_cost_run_count": 0,
                "partial_cost_count": 0,
                "score_total": 0.0,
                "score_count": 0,
                "rubric_dimensions": {},
                "statuses": {},
            },
        )
        group["run_count"] += 1
        group["statuses"][record["status"]] = group["statuses"].get(record["status"], 0) + 1
        if record["status"] == "completed":
            group["completed_count"] += 1
        if record["qualitative_only"]:
            group["qualitative_only_count"] += 1

        token_total = total_known_tokens(record["usage"])
        if isinstance(token_total, int):
            group["known_token_total"] += token_total
            group["known_token_run_count"] += 1

        reasoning_tokens = record["usage"].get("reasoning_tokens", NOT_AVAILABLE)
        if isinstance(reasoning_tokens, int):
            group["reasoning_token_total"] += reasoning_tokens
            group["reasoning_token_run_count"] += 1

        cost = _cost_value(raw_record)
        if cost is not None:
            group["estimated_cost_total"] += cost
            group["estimated_cost_run_count"] += 1
        if _cost_status(raw_record) == "partial":
            group["partial_cost_count"] += 1

        score = _score_value(raw_record)
        if score is not None:
            group["score_total"] += score
            group["score_count"] += 1

        for observation in record.get("rubric_observations", []):
            dimension_id = observation["dimension_id"]
            dimension = group["rubric_dimensions"].setdefault(
                dimension_id,
                {
                    "dimension_id": dimension_id,
                    "rubric_ids": set(),
                    "evaluator_ids": set(),
                    "rubric_versions": set(),
                    "status_counts": {},
                    "value_total": 0.0,
                    "value_count": 0,
                },
            )
            dimension["rubric_ids"].add(observation["rubric_id"])
            dimension["evaluator_ids"].add(observation["evaluator_id"])
            dimension["rubric_versions"].add(observation["rubric_version"])
            dimension["status_counts"][observation["status"]] = (
                dimension["status_counts"].get(observation["status"], 0) + 1
            )
            value = _numeric_value(observation.get("value"))
            if value is not None:
                dimension["value_total"] += value
                dimension["value_count"] += 1

    summaries = []
    for group in groups.values():
        summary = dict(group)
        summary["average_known_tokens"] = (
            round(group["known_token_total"] / group["known_token_run_count"], 2)
            if group["known_token_run_count"]
            else NOT_AVAILABLE
        )
        summary["reasoning_token_total"] = (
            group["reasoning_token_total"] if group["reasoning_token_run_count"] else NOT_AVAILABLE
        )
        summary["average_reasoning_tokens"] = (
            round(group["reasoning_token_total"] / group["reasoning_token_run_count"], 2)
            if group["reasoning_token_run_count"]
            else NOT_AVAILABLE
        )
        summary["total_estimated_cost"] = str(group["estimated_cost_total"].quantize(Decimal("0.000001")))
        summary["average_estimated_cost"] = (
            str((group["estimated_cost_total"] / group["estimated_cost_run_count"]).quantize(Decimal("0.000001")))
            if group["estimated_cost_run_count"]
            else NOT_AVAILABLE
        )
        summary["average_score"] = (
            round(group["score_total"] / group["score_count"], 3) if group["score_count"] else NOT_AVAILABLE
        )
        if group["score_count"]:
            summary["legacy_score_label"] = "compatibility-only"
        rubric_dimension_summaries = {}
        for dimension_id, dimension in sorted(group["rubric_dimensions"].items()):
            rubric_dimension_summaries[dimension_id] = {
                "dimension_id": dimension_id,
                "rubric_ids": sorted(dimension["rubric_ids"]),
                "evaluator_ids": sorted(dimension["evaluator_ids"]),
                "rubric_versions": sorted(dimension["rubric_versions"]),
                "status_counts": dict(sorted(dimension["status_counts"].items())),
                "average_value": (
                    round(dimension["value_total"] / dimension["value_count"], 3)
                    if dimension["value_count"]
                    else NOT_AVAILABLE
                ),
                "value_count": dimension["value_count"],
            }
        if rubric_dimension_summaries:
            summary["quality_summary_source"] = "rubric_dimensions"
            summary["rubric_dimension_summaries"] = rubric_dimension_summaries
        elif group["score_count"]:
            summary["quality_summary_source"] = "legacy_score_compatibility"
        else:
            summary["quality_summary_source"] = NOT_AVAILABLE
        for internal in ("estimated_cost_total", "score_total", "rubric_dimensions"):
            summary.pop(internal)
        summaries.append(summary)
    return {"groups": sorted(summaries, key=lambda item: (item["task_id"], item["candidate_profile"], item["reasoning_effort"]))}


def _check_enum(value: Any, allowed: frozenset[str], field: str, strict: bool) -> None:
    if value is None:
        return
    if strict and value not in allowed:
        raise ValueError(f"{field} must be one of {sorted(allowed)}")


def _validate_report_diagnostic(diagnostic: dict[str, Any], strict: bool) -> None:
    _check_enum(diagnostic.get("status"), OBSERVATION_STATUSES, "status", strict)
    _check_enum(diagnostic.get("evidence_class"), EVIDENCE_CLASSES, "evidence_class", strict)
    _check_enum(diagnostic.get("reliability_mode"), RELIABILITY_MODES, "reliability_mode", strict)
    _check_enum(diagnostic.get("content_contract"), CONTENT_CONTRACTS, "content_contract", strict)
    _check_enum(diagnostic.get("cost_evidence_mode"), COST_EVIDENCE_MODES, "cost_evidence_mode", strict)
    _check_enum(diagnostic.get("comparability"), COMPARABILITY_VALUES, "comparability", strict)


def telemetry_rebuild_report(
    query_output: dict[str, Any],
    *,
    registry_hash: str | None = None,
    strict: bool = True,
) -> dict[str, Any]:
    """Render a small report from rebuild query output with parity checks."""

    actual_hash = query_output.get("registry_hash")
    if strict and registry_hash is not None and registry_hash != actual_hash:
        raise ValueError(f"registry_hash mismatch: expected {registry_hash}, found {actual_hash}")
    diagnostics = query_output.get("diagnostics", [])
    if not isinstance(diagnostics, list):
        raise ValueError("diagnostics must be a list")
    for diagnostic in diagnostics:
        if not isinstance(diagnostic, dict):
            raise ValueError("diagnostics entries must be objects")
        _validate_report_diagnostic(diagnostic, strict)
    safe_diagnostics = [
        query.sanitize_diagnostic_payload(diagnostic, strict)
        for diagnostic in diagnostics
    ]
    return {
        "registry_hash": actual_hash,
        "registry_version": query_output.get("registry_version"),
        "source_set_hash": query_output.get("source_set_hash"),
        "status": query_output.get("status"),
        "diagnostic_count": len(safe_diagnostics),
        "diagnostics": safe_diagnostics,
    }


def telemetry_migration_report(conn: Any, *, strict: bool = True) -> dict[str, Any]:
    """Render a small v0 compatibility report from the telemetry store."""

    state = query.query_migration_state(conn, strict=strict)
    return {
        "v0_compatibility_status": state["v0_compatibility_status"],
        "registry_hash": state["registry_hash"],
        "source_set_hash": state["source_set_hash"],
        "counts": state["counts"],
        "usage_observation_status_counts": state["usage_observation_status_counts"],
        "usage_missingness_counts": state["usage_missingness_counts"],
        "cost_evidence_mode_counts": state["cost_evidence_mode_counts"],
        "source_artifact_count": state["counts"]["source_artifacts"],
        "diagnostic_count": state["diagnostic_count"],
        "diagnostics": state["diagnostics"],
    }
