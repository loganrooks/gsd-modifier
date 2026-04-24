"""Schema validation and normalization for model benchmark records.

The schema is intentionally provider-neutral. Codex CLI, Claude Code, and later
runtime adapters should preserve their raw evidence separately, then normalize
into this record shape for cross-run comparison.
"""

from __future__ import annotations

import copy
from typing import Any

from tooling.codex.model_benchmark.enums import (
    COMPARABILITY_VALUES,
    CONTENT_CONTRACTS,
    EVIDENCE_CLASSES,
    OBSERVATION_STATUSES,
    RELIABILITY_MODES,
)

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
DEFAULT_SCHEMA_VERSION = "model-benchmark-run/v1"

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


def _require_enum(value: Any, allowed: frozenset[str], label: str) -> str:
    normalized = require_string(value, label)
    if normalized not in allowed:
        raise ValueError(f"{label} must be one of {sorted(allowed)}")
    return normalized


def _normalize_rubric_value(value: Any, label: str) -> int | float | str:
    if value == NOT_AVAILABLE:
        return NOT_AVAILABLE
    if isinstance(value, bool):
        raise ValueError(f"{label} must be a number or {NOT_AVAILABLE}")
    if isinstance(value, (int, float)):
        return value
    raise ValueError(f"{label} must be a number or {NOT_AVAILABLE}")


def normalize_legacy_score(raw_score: Any) -> dict[str, Any] | None:
    """Normalize legacy scalar score compatibility data without making it canonical."""

    if raw_score is None:
        return None
    score = require_object(raw_score, "score")
    if "overall" not in score:
        return None
    value = score["overall"]
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("score.overall must be numeric for legacy compatibility")
    return {
        "overall": float(value),
        "metric_id": "legacy.score.overall",
        "compatibility": "compatibility_only",
        "warning": "legacy scalar score is compatibility-only; canonical quality uses rubric_observations",
    }


def normalize_rubric_observation(raw_observation: Any, index: int = 1) -> dict[str, Any]:
    observation = copy.deepcopy(require_object(raw_observation, f"rubric_observations[{index}]"))
    label = f"rubric_observations[{index}]"

    normalized = {
        "rubric_id": require_string(observation.get("rubric_id"), f"{label}.rubric_id"),
        "dimension_id": require_string(observation.get("dimension_id"), f"{label}.dimension_id"),
        "evaluator_id": require_string(observation.get("evaluator_id"), f"{label}.evaluator_id"),
        "rubric_version": require_string(observation.get("rubric_version"), f"{label}.rubric_version"),
        "value": _normalize_rubric_value(observation.get("value"), f"{label}.value"),
        "status": _require_enum(observation.get("status"), OBSERVATION_STATUSES, f"{label}.status"),
        "evidence_class": _require_enum(
            observation.get("evidence_class"), EVIDENCE_CLASSES, f"{label}.evidence_class"
        ),
        "reliability_mode": _require_enum(
            observation.get("reliability_mode"), RELIABILITY_MODES, f"{label}.reliability_mode"
        ),
        "content_contract": _require_enum(
            observation.get("content_contract"), CONTENT_CONTRACTS, f"{label}.content_contract"
        ),
        "provenance": require_object(observation.get("provenance"), f"{label}.provenance"),
    }
    comparability = observation.get("comparability")
    if comparability is not None:
        normalized["comparability"] = _require_enum(comparability, COMPARABILITY_VALUES, f"{label}.comparability")
    return normalized


def normalize_rubric_observations(raw_observations: Any) -> list[dict[str, Any]]:
    if raw_observations is None:
        return []
    if not isinstance(raw_observations, list):
        raise ValueError("rubric_observations must be a list")
    return [
        normalize_rubric_observation(observation, index)
        for index, observation in enumerate(raw_observations, 1)
    ]


def validate_run_record(record: dict[str, Any], profile_registry: Any | None = None) -> dict[str, Any]:
    normalized = copy.deepcopy(require_object(record, "run_record"))
    missing = [field for field in REQUIRED_RUN_FIELDS if field not in normalized]
    if missing:
        raise ValueError(f"run_record missing required fields: {', '.join(missing)}")

    normalized["schema_version"] = require_string(
        normalized.get("schema_version", DEFAULT_SCHEMA_VERSION), "schema_version"
    )

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
    normalized["legacy_score"] = normalize_legacy_score(normalized.get("score"))
    normalized["rubric_observations"] = normalize_rubric_observations(normalized.get("rubric_observations"))

    effective_model = normalized.get("effective_model", NOT_AVAILABLE)
    effective_reasoning = normalized.get("effective_reasoning_effort", NOT_AVAILABLE)
    normalized["effective_model"] = effective_model or NOT_AVAILABLE
    normalized["effective_reasoning_effort"] = effective_reasoning or NOT_AVAILABLE
    normalized["qualitative_only"] = normalized["effective_model"] == NOT_AVAILABLE or normalized["effective_reasoning_effort"] == NOT_AVAILABLE
    normalized["profile_consistency_status"] = normalized.get("profile_consistency_status", "not_checked")
    if profile_registry is not None:
        from tooling.codex.model_benchmark.profiles import validate_run_profile_consistency

        normalized = validate_run_profile_consistency(normalized, profile_registry)
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
