"""API-equivalent cost estimation for benchmark usage records."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
from typing import Any

from tooling.codex.model_benchmark.schema import (
    NOT_AVAILABLE,
    TOKEN_FIELDS,
    normalize_usage_record,
    require_object,
    require_string,
    validate_run_record,
)

RATE_FIELDS = {
    "input_tokens": "input_per_million",
    "cached_input_tokens": "cached_input_per_million",
    "output_tokens": "output_per_million",
    "reasoning_tokens": "reasoning_per_million",
    "initialization_tokens": "input_per_million",
    "tool_result_tokens": "input_per_million",
}

REQUIRED_RATE_METADATA = ("model", "currency", "source_url", "retrieved_at", "effective_date")


def _decimal(value: Any, label: str) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{label} must be numeric")
    if isinstance(value, (int, float, str)):
        try:
            result = Decimal(str(value))
        except Exception as exc:  # pragma: no cover - Decimal error type differs across versions
            raise ValueError(f"{label} must be numeric") from exc
        if result < 0:
            raise ValueError(f"{label} cannot be negative")
        return result
    raise ValueError(f"{label} must be numeric")


def validate_rate_table(rate_table: dict[str, Any]) -> dict[str, Any]:
    table = require_object(rate_table, "rate_table")
    missing = [field for field in REQUIRED_RATE_METADATA if not table.get(field)]
    if missing:
        raise ValueError(f"rate_table missing required metadata: {', '.join(missing)}")
    normalized = dict(table)
    for field in REQUIRED_RATE_METADATA:
        normalized[field] = require_string(normalized[field], f"rate_table.{field}")
    for rate_field in set(RATE_FIELDS.values()):
        if rate_field in normalized and normalized[rate_field] != NOT_AVAILABLE:
            normalized[rate_field] = _decimal(normalized[rate_field], f"rate_table.{rate_field}")
        else:
            normalized[rate_field] = NOT_AVAILABLE
    return normalized


def _line_item(field: str, token_count: int, rate_per_million: Decimal) -> dict[str, Any]:
    raw_cost = Decimal(token_count) * rate_per_million / Decimal(1_000_000)
    return {
        "token_field": field,
        "tokens": token_count,
        "rate_per_million": str(rate_per_million),
        "estimated_cost": str(raw_cost.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)),
    }


def estimate_cost(usage_record: dict[str, Any], rate_table: dict[str, Any]) -> dict[str, Any]:
    usage = normalize_usage_record(usage_record)
    rates = validate_rate_table(rate_table)
    line_items: list[dict[str, Any]] = []
    missing_token_fields: list[str] = []
    missing_rate_fields: list[str] = []
    total = Decimal("0")

    for token_field in TOKEN_FIELDS:
        token_count = usage[token_field]
        if token_count == NOT_AVAILABLE:
            missing_token_fields.append(token_field)
            continue
        rate_field = RATE_FIELDS[token_field]
        rate = rates[rate_field]
        if rate == NOT_AVAILABLE:
            missing_rate_fields.append(rate_field)
            continue
        item = _line_item(token_field, token_count, rate)
        line_items.append(item)
        total += Decimal(item["estimated_cost"])

    if not line_items:
        estimate_status = NOT_AVAILABLE
        total_value: str | Decimal = NOT_AVAILABLE
    elif missing_token_fields or missing_rate_fields:
        estimate_status = "partial"
        total_value = total.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    else:
        estimate_status = "estimated"
        total_value = total.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)

    return {
        "estimate_status": estimate_status,
        "model": rates["model"],
        "currency": rates["currency"],
        "source_url": rates["source_url"],
        "retrieved_at": rates["retrieved_at"],
        "effective_date": rates["effective_date"],
        "total_estimated_cost": str(total_value) if total_value != NOT_AVAILABLE else NOT_AVAILABLE,
        "line_items": line_items,
        "missing_token_fields": sorted(set(missing_token_fields)),
        "missing_rate_fields": sorted(set(missing_rate_fields)),
        "caveat": "API-equivalent estimate only; not direct ChatGPT or Codex plan quota burn.",
    }


def _rate_rows(raw_rate_table: dict[str, Any]) -> list[dict[str, Any]]:
    table = require_object(raw_rate_table, "rate_table")
    if "rates" in table:
        rates = table["rates"]
        if not isinstance(rates, list):
            raise ValueError("rate_table.rates must be a list")
        return rates
    return [table]


def select_rate_table(run: dict[str, Any], raw_rate_table: dict[str, Any]) -> dict[str, Any]:
    target_model = run.get("effective_model")
    if target_model in (None, NOT_AVAILABLE):
        target_model = run.get("model")
    matching = [
        rate for rate in _rate_rows(raw_rate_table) if isinstance(rate, dict) and rate.get("model") == target_model
    ]
    if not matching:
        raise ValueError(f"no rate table found for model {target_model}")
    if len(matching) > 1:
        raise ValueError(f"multiple rate tables found for model {target_model}")
    return matching[0]


def attach_cost_estimate(run: dict[str, Any], rate_table: dict[str, Any]) -> dict[str, Any]:
    normalized = validate_run_record(run)
    selected_rates = select_rate_table(normalized, rate_table)
    estimated = dict(normalized)
    estimated["cost_estimate"] = estimate_cost(normalized["usage"], selected_rates)
    return estimated
