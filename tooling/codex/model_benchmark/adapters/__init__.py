"""Read-only telemetry adapters for model benchmark fixtures."""

from __future__ import annotations

from typing import Any

from tooling.codex.model_benchmark.enums import (
    COMPARABILITY_VALUES,
    CONTENT_CONTRACTS,
    COST_EVIDENCE_MODES,
    EVIDENCE_CLASSES,
    OBSERVATION_STATUSES,
    RELIABILITY_MODES,
    RUNTIME_ITEM_CORRELATION_STATUSES,
)


OUTPUT_SECTIONS = (
    "sessions",
    "entity_edges",
    "turns",
    "model_calls",
    "runtime_response_items",
    "tool_calls",
    "token_observations",
    "observations",
    "parse_diagnostics",
)


def empty_adapter_output(source_kind: str) -> dict[str, Any]:
    output: dict[str, Any] = {"schema_version": "normalized-telemetry-adapter-output/v1", "source_kind": source_kind}
    for section in OUTPUT_SECTIONS:
        output[section] = []
    return output


def _check_enum(value: Any, allowed: frozenset[str], field: str, strict: bool) -> None:
    if value is None:
        return
    if strict and value not in allowed:
        raise ValueError(f"{field} must be one of {sorted(allowed)}")


def _require_mapping(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{field} must be an object")
    return value


def _require(value: dict[str, Any], field: str) -> Any:
    item = value.get(field)
    if item is None:
        raise ValueError(f"{field} is required")
    if isinstance(item, str) and not item.strip():
        raise ValueError(f"{field} is required")
    return item


def _validate_source_ref(value: Any, strict: bool) -> None:
    ref = _require_mapping(value, "source_artifact_ref")
    _require(ref, "artifact_id")
    _require(ref, "source_uri")
    _require(ref, "line_hash")
    if ref.get("line_number") is not None and not isinstance(ref["line_number"], int):
        raise ValueError("source_artifact_ref.line_number must be an integer")
    _check_enum(ref.get("content_contract"), CONTENT_CONTRACTS, "source_artifact_ref.content_contract", strict)


def _validate_observation(row: dict[str, Any], strict: bool) -> None:
    _check_enum(row.get("status"), OBSERVATION_STATUSES, "status", strict)
    _check_enum(row.get("evidence_class"), EVIDENCE_CLASSES, "evidence_class", strict)
    _check_enum(row.get("reliability_mode"), RELIABILITY_MODES, "reliability_mode", strict)
    _check_enum(row.get("content_contract"), CONTENT_CONTRACTS, "content_contract", strict)
    _check_enum(row.get("cost_evidence_mode"), COST_EVIDENCE_MODES, "cost_evidence_mode", strict)
    _check_enum(row.get("comparability"), COMPARABILITY_VALUES, "comparability", strict)
    if "source_artifact_ref" in row:
        _validate_source_ref(row["source_artifact_ref"], strict)


def _validate_runtime_item(row: dict[str, Any], strict: bool) -> None:
    for field in (
        "source_kind",
        "provider_namespace",
        "runtime_namespace",
        "item_type",
        "redaction_state",
        "content_state",
        "source_artifact_ref",
        "provenance",
        "payload",
        "correlation_status",
    ):
        _require(row, field)
    _check_enum(row.get("correlation_status"), RUNTIME_ITEM_CORRELATION_STATUSES, "correlation_status", strict)
    _validate_source_ref(row["source_artifact_ref"], strict)
    _require_mapping(row["provenance"], "provenance")
    payload = _require_mapping(row["payload"], "payload")
    provider_namespace = row.get("provider_namespace")
    runtime_namespace = row.get("runtime_namespace")
    if provider_namespace == "provider.openai" and runtime_namespace == "runtime.codex_cli":
        allowed_payload_namespaces = {"codex"}
    elif provider_namespace == "provider.anthropic" and runtime_namespace == "runtime.claude_code":
        allowed_payload_namespaces = {"anthropic", "claude_code"}
    else:
        allowed_payload_namespaces = set()
    for key in payload:
        if key not in allowed_payload_namespaces:
            raise ValueError("payload namespace does not match provider/runtime namespace")


def validate_adapter_output(output: dict[str, Any], *, strict: bool = True) -> dict[str, Any]:
    """Validate normalized adapter output against first-slice enum contracts."""

    _require_mapping(output, "adapter_output")
    for section in OUTPUT_SECTIONS:
        if section not in output:
            raise ValueError(f"{section} is required")
        if not isinstance(output[section], list):
            raise ValueError(f"{section} must be a list")

    for item in output["runtime_response_items"]:
        _validate_runtime_item(_require_mapping(item, "runtime_response_items[]"), strict)
    for section in ("token_observations", "observations", "parse_diagnostics"):
        for row in output[section]:
            _validate_observation(_require_mapping(row, f"{section}[]"), strict)
    return output
