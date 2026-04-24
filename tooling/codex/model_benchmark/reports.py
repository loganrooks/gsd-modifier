"""Aggregation helpers for model benchmark run records."""

from __future__ import annotations

from decimal import Decimal
from typing import Any

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


def _cost_value(record: dict[str, Any]) -> Decimal | None:
    cost = record.get("cost_estimate")
    if not isinstance(cost, dict):
        return None
    value = cost.get("total_estimated_cost")
    if value in (None, NOT_AVAILABLE):
        return None
    return Decimal(str(value))


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
                "estimated_cost_total": Decimal("0"),
                "estimated_cost_run_count": 0,
                "score_total": 0.0,
                "score_count": 0,
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

        cost = _cost_value(raw_record)
        if cost is not None:
            group["estimated_cost_total"] += cost
            group["estimated_cost_run_count"] += 1

        score = _score_value(raw_record)
        if score is not None:
            group["score_total"] += score
            group["score_count"] += 1

    summaries = []
    for group in groups.values():
        summary = dict(group)
        summary["average_known_tokens"] = (
            round(group["known_token_total"] / group["known_token_run_count"], 2)
            if group["known_token_run_count"]
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
        for internal in ("estimated_cost_total", "score_total"):
            summary.pop(internal)
        summaries.append(summary)
    return {"groups": sorted(summaries, key=lambda item: (item["task_id"], item["candidate_profile"], item["reasoning_effort"]))}
