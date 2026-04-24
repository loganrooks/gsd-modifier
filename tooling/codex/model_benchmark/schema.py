"""Schema validation and normalization for model benchmark records.

The schema is intentionally provider-neutral. Codex CLI, Claude Code, and later
runtime adapters should preserve their raw evidence separately, then normalize
into this record shape for cross-run comparison.
"""

from __future__ import annotations

import copy
from typing import Any


NOT_AVAILABLE = "not_available"
ALLOWED_REASONING = {"low", "medium", "high", "xhigh", NOT_AVAILABLE}
ALLOWED_RUNTIME_PROVIDERS = {"codex_cli", "claude_code", "api", "manual", NOT_AVAILABLE}
ALLOWED_METRIC_STATUS = {"measured", "estimated", "derived", NOT_AVAILABLE}
ALLOWED_RUN_STATUS = {
    "completed",
    "access_failed",
    "routing_unproven",
    "quota_blocked",
    "execution_failed",
    "verification_failed",
}
ALLOWED_GRANULARITY = {
    "session",
    "run",
    "task",
    "turn",
    "agent",
    "tool_call",
    "file_diff",
    "config_profile",
    "intervention_window",
    NOT_AVAILABLE,
}

REQUIRED_RUN_FIELDS = (
    "run_id",
    "task_id",
    "candidate_profile",
    "model",
    "reasoning_effort",
    "runtime_provider",
    "status",
    "usage",
)

TOKEN_FIELDS = (
    "input_tokens",
    "cached_input_tokens",
    "output_tokens",
    "reasoning_tokens",
    "initialization_tokens",
    "tool_result_tokens",
)

TELEMETRY_DEFAULTS: dict[str, Any] = {
    "trace_id": NOT_AVAILABLE,
    "parent_trace_id": NOT_AVAILABLE,
    "agent_role": NOT_AVAILABLE,
    "intervention_id": NOT_AVAILABLE,
    "metric_granularity": "run",
    "provenance": NOT_AVAILABLE,
    "derived_feature_version": NOT_AVAILABLE,
}


def require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    return value


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def normalize_metric_value(value: Any, label: str) -> int | str:
    if value == NOT_AVAILABLE or value is None:
        return NOT_AVAILABLE
    if isinstance(value, bool):
        raise ValueError(f"{label} must be an integer or {NOT_AVAILABLE}")
    if isinstance(value, int):
        if value < 0:
            raise ValueError(f"{label} cannot be negative")
        return value
    raise ValueError(f"{label} must be an integer or {NOT_AVAILABLE}")


def normalize_usage_record(raw_usage: Any) -> dict[str, Any]:
    usage = copy.deepcopy(require_object(raw_usage, "usage"))
    for field in TOKEN_FIELDS:
        usage[field] = normalize_metric_value(usage.get(field, NOT_AVAILABLE), f"usage.{field}")

    metric_status = usage.get("usage_metric_status", NOT_AVAILABLE)
    if metric_status not in ALLOWED_METRIC_STATUS:
        raise ValueError(f"usage.usage_metric_status must be one of {sorted(ALLOWED_METRIC_STATUS)}")
    usage["usage_metric_status"] = metric_status

    for field in ("quota_delta", "status_before", "status_after"):
        if field not in usage:
            usage[field] = NOT_AVAILABLE
    return usage


def normalize_telemetry_features(raw_features: Any) -> dict[str, Any]:
    features = copy.deepcopy(raw_features or {})
    if not isinstance(features, dict):
        raise ValueError("telemetry_features must be an object")
    for key, default in TELEMETRY_DEFAULTS.items():
        features.setdefault(key, default)
    if features["metric_granularity"] not in ALLOWED_GRANULARITY:
        raise ValueError(f"telemetry_features.metric_granularity must be one of {sorted(ALLOWED_GRANULARITY)}")
    return features


def validate_run_record(record: dict[str, Any]) -> dict[str, Any]:
    normalized = copy.deepcopy(require_object(record, "run_record"))
    missing = [field for field in REQUIRED_RUN_FIELDS if field not in normalized]
    if missing:
        raise ValueError(f"run_record missing required fields: {', '.join(missing)}")

    for field in ("run_id", "task_id", "candidate_profile", "model"):
        normalized[field] = require_string(normalized[field], field)

    reasoning_effort = require_string(normalized["reasoning_effort"], "reasoning_effort")
    if reasoning_effort not in ALLOWED_REASONING:
        raise ValueError(f"reasoning_effort must be one of {sorted(ALLOWED_REASONING)}")
    normalized["reasoning_effort"] = reasoning_effort

    runtime_provider = require_string(normalized["runtime_provider"], "runtime_provider")
    if runtime_provider not in ALLOWED_RUNTIME_PROVIDERS:
        raise ValueError(f"runtime_provider must be one of {sorted(ALLOWED_RUNTIME_PROVIDERS)}")
    normalized["runtime_provider"] = runtime_provider

    status = require_string(normalized["status"], "status")
    if status not in ALLOWED_RUN_STATUS:
        raise ValueError(f"status must be one of {sorted(ALLOWED_RUN_STATUS)}")
    normalized["status"] = status

    normalized["usage"] = normalize_usage_record(normalized["usage"])
    normalized["telemetry_features"] = normalize_telemetry_features(normalized.get("telemetry_features"))

    effective_model = normalized.get("effective_model", NOT_AVAILABLE)
    effective_reasoning = normalized.get("effective_reasoning_effort", NOT_AVAILABLE)
    normalized["effective_model"] = effective_model or NOT_AVAILABLE
    normalized["effective_reasoning_effort"] = effective_reasoning or NOT_AVAILABLE
    normalized["qualitative_only"] = normalized["effective_model"] == NOT_AVAILABLE or normalized["effective_reasoning_effort"] == NOT_AVAILABLE
    return normalized


def total_known_tokens(usage: dict[str, Any]) -> int | str:
    total = 0
    saw_known = False
    for field in TOKEN_FIELDS:
        value = usage.get(field, NOT_AVAILABLE)
        if isinstance(value, int):
            total += value
            saw_known = True
    return total if saw_known else NOT_AVAILABLE
