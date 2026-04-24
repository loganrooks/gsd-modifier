"""Adapter for fixture-backed Claude Code local JSONL structures.

The adapter only reads the caller-provided fixture path. It does not discover
Claude home-state, hooks, plugins, skills, credentials, or raw provider bodies.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from tooling.codex.model_benchmark.adapters import empty_adapter_output


SOURCE_KIND = "runtime.claude_code.local_jsonl"
PROVIDER_NAMESPACE = "provider.anthropic"
RUNTIME_NAMESPACE = "runtime.claude_code"
INTEGRATION_BOUNDARY = "provider_neutrality_rebuild_integration_deferred_to_task_05"

DISALLOWED_PATH_PARTS = frozenset(
    {
        ".claude",
        ".codex",
        "hooks",
        "plugins",
        "skills",
        "credentials",
        "api_keys",
        "raw_api_bodies",
        "secrets",
    }
)
DISALLOWED_HOME_ROOTS = (
    Path.home() / ".claude",
    Path.home() / ".codex",
    Path.home() / ".config" / "claude",
    Path.home() / ".config" / "anthropic",
)
SAFE_ARGUMENT_KEYS = frozenset({"line_count", "mode"})
SAFE_ARGUMENT_MODES = frozenset({"append", "inspect", "overwrite", "read", "write"})
SAFE_RECORD_TYPES = frozenset(
    {
        "message",
        "parse_diagnostic",
        "session",
        "sidechain_agent",
        "thinking_summary",
        "tool",
        "unknown",
    }
)
SAFE_CONTENT_CONTRACTS = frozenset(
    {
        "metadata_only",
        "redacted_content_reference",
        "structural_only",
    }
)
SAFE_REDACTION_STATES = frozenset({"redacted", "synthetic", "unknown"})
SAFE_ROLES = frozenset({"assistant", "system", "tool", "user"})
SAFE_RESULT_STATES = frozenset({"error", "redacted", "success", "synthetic", "unknown"})
SAFE_TOOL_NAMES = frozenset(
    {
        "Bash",
        "Edit",
        "Grep",
        "LS",
        "Read",
        "Task",
        "TodoWrite",
        "Write",
    }
)


def _line_hash(line: str) -> str:
    return f"sha256:{hashlib.sha256(line.encode('utf-8')).hexdigest()}"


def _source_ref(
    path: Path,
    *,
    line_number: int,
    line: str,
    artifact_id: str,
    content_contract: str,
) -> dict[str, Any]:
    return {
        "artifact_id": artifact_id,
        "source_uri": str(path),
        "line_number": line_number,
        "line_hash": _line_hash(line),
        "content_contract": content_contract,
    }


def _provenance(path: Path, line_number: int) -> dict[str, Any]:
    return {
        "adapter": "claude_local",
        "source_path": str(path),
        "line_number": line_number,
        "evidence_class": "synthetic_fixture",
        "reliability_mode": "local_structural_field",
    }


def _reject_disallowed_source_path(path: Path) -> None:
    expanded = path.expanduser()
    resolved = expanded.resolve(strict=False)
    parts = {part.lower() for part in expanded.parts}
    under_disallowed_home_root = any(
        _is_relative_to(resolved, root.expanduser().resolve(strict=False)) for root in DISALLOWED_HOME_ROOTS
    )
    if under_disallowed_home_root or parts.intersection(DISALLOWED_PATH_PARTS):
        raise ValueError(f"disallowed Claude local source path: {path}")


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def _path_shape(value: Any) -> str:
    if not isinstance(value, str) or not value:
        return "not_provided"
    path = Path(value).expanduser()
    if path.is_absolute() or value.startswith("~"):
        return "absolute_or_home_path"
    return "relative_path"


def _sanitized_argument_shape(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {}
    sanitized: dict[str, Any] = {}
    if "path" in value:
        sanitized["path_shape"] = _path_shape(value.get("path"))
    if "line_count" in value and isinstance(value["line_count"], int):
        sanitized["line_count"] = value["line_count"]
    if "mode" in value:
        sanitized["mode"] = value["mode"] if value["mode"] in SAFE_ARGUMENT_MODES else "other"
    return sanitized


def _safe_member(value: Any, allowed: frozenset[str], default: str = "unknown") -> str:
    if isinstance(value, str) and value in allowed:
        return value
    return default


def _safe_record_type(value: Any) -> str:
    return _safe_member(value, SAFE_RECORD_TYPES)


def _safe_tool_name(value: Any) -> str:
    return _safe_member(value, SAFE_TOOL_NAMES, "other")


def _safe_bool(value: Any) -> bool:
    return value is True


def _safe_list_count(value: Any) -> int:
    return len(value) if isinstance(value, list) else 0


def _content_state(record: dict[str, Any]) -> str:
    if record.get("content_ref"):
        return "redacted_reference"
    return record.get("content_state") or "structural_only"


def _runtime_item_id(record: dict[str, Any], artifact_id: str, line_number: int) -> str:
    for field in ("message_id", "tool_call_id", "agent_id", "summary_id", "session_id", "item_id"):
        value = record.get(field)
        if isinstance(value, str) and value:
            return value
    return f"{artifact_id}:line:{line_number}"


def _payload(record: dict[str, Any]) -> dict[str, Any]:
    anthropic_payload: dict[str, Any] = {"record_type": _safe_record_type(record.get("record_type"))}
    if "content_contract" in record:
        anthropic_payload["content_contract"] = _safe_member(record.get("content_contract"), SAFE_CONTENT_CONTRACTS)
    if "redaction_state" in record:
        anthropic_payload["redaction_state"] = _safe_member(record.get("redaction_state"), SAFE_REDACTION_STATES)
    if "role" in record:
        anthropic_payload["role"] = _safe_member(record.get("role"), SAFE_ROLES)
    if "agent_role" in record:
        anthropic_payload["agent_role_present"] = isinstance(record.get("agent_role"), str) and bool(record.get("agent_role"))
    if "thinking_summary_present" in record:
        anthropic_payload["thinking_summary_present"] = _safe_bool(record.get("thinking_summary_present"))
    if "facets" in record:
        anthropic_payload["facets_count"] = _safe_list_count(record.get("facets"))

    runtime_payload: dict[str, Any] = {}
    if "tool_name" in record:
        runtime_payload["tool_name"] = _safe_tool_name(record.get("tool_name"))
    if "argument_shape" in record:
        runtime_payload["argument_shape"] = _sanitized_argument_shape(record.get("argument_shape"))
    if "result_state" in record:
        runtime_payload["result_state"] = _safe_member(record.get("result_state"), SAFE_RESULT_STATES)

    payload: dict[str, Any] = {}
    payload["anthropic"] = anthropic_payload
    if runtime_payload:
        payload["claude_code"] = runtime_payload
    return payload


def _runtime_item(
    *,
    path: Path,
    line_number: int,
    line: str,
    record: dict[str, Any],
    artifact_id: str,
    session_id: str | None,
) -> dict[str, Any]:
    record_type = _safe_record_type(record.get("record_type", "unknown"))
    content_contract = record.get("content_contract", "structural_only")
    return {
        "runtime_item_id": _runtime_item_id(record, artifact_id, line_number),
        "session_id": record.get("session_id") or session_id,
        "model_call_id": None,
        "source_kind": SOURCE_KIND,
        "provider_namespace": PROVIDER_NAMESPACE,
        "runtime_namespace": RUNTIME_NAMESPACE,
        "item_type": record_type,
        "status": record.get("status", "unknown"),
        "role": _safe_member(record.get("role"), SAFE_ROLES) if "role" in record else None,
        "redaction_state": record.get("redaction_state", "synthetic"),
        "content_state": _content_state(record),
        "correlation_status": record.get("correlation_status", "unknown"),
        "source_artifact_ref": _source_ref(
            path,
            line_number=line_number,
            line=line,
            artifact_id=artifact_id,
            content_contract=content_contract,
        ),
        "provenance": _provenance(path, line_number),
        "payload": _payload(record),
    }


def _session_row(path: Path, line_number: int, line: str, record: dict[str, Any], artifact_id: str) -> dict[str, Any]:
    return {
        "session_id": record["session_id"],
        "provider_namespace": PROVIDER_NAMESPACE,
        "runtime_namespace": RUNTIME_NAMESPACE,
        "source_artifact_ref": _source_ref(
            path,
            line_number=line_number,
            line=line,
            artifact_id=artifact_id,
            content_contract=record.get("content_contract", "structural_only"),
        ),
        "provenance": _provenance(path, line_number),
        "payload": {
            "anthropic": {
                "record_type": _safe_record_type(record.get("record_type")),
                "thinking_summary_present": _safe_bool(record.get("thinking_summary_present")),
            }
        },
    }


def _observation(
    *,
    entity_type: str,
    entity_id: str,
    metric_id: str,
    status: str,
    reliability_mode: str,
    comparability: str,
    ref: dict[str, Any],
    provenance: dict[str, Any],
    value: dict[str, Any],
) -> dict[str, Any]:
    return {
        "entity_type": entity_type,
        "entity_id": entity_id,
        "metric_id": metric_id,
        "status": status,
        "evidence_class": "synthetic_fixture",
        "reliability_mode": reliability_mode,
        "content_contract": ref["content_contract"],
        "comparability": comparability,
        "source_artifact_ref": ref,
        "value": value,
        "provenance": provenance,
    }


def _token_observation(session_id: str, ref: dict[str, Any], provenance: dict[str, Any]) -> dict[str, Any]:
    return {
        "entity_type": "session",
        "entity_id": session_id,
        "metric_id": "tokens.reasoning",
        "status": "not_exposed",
        "evidence_class": "synthetic_fixture",
        "reliability_mode": "substitute_signal",
        "content_contract": "metadata_only",
        "cost_evidence_mode": "not_exposed",
        "comparability": "insufficient_evidence",
        "source_artifact_ref": {**ref, "content_contract": "metadata_only"},
        "value": {"tokens": "not_exposed"},
        "provenance": provenance,
    }


def _diagnostic(
    *,
    path: Path,
    line_number: int,
    line: str,
    artifact_id: str,
    record: dict[str, Any],
) -> dict[str, Any]:
    content_contract = record.get("content_contract", "metadata_only")
    ref = _source_ref(
        path,
        line_number=int(record.get("line_number", line_number)),
        line=line,
        artifact_id=artifact_id,
        content_contract=content_contract,
    )
    return {
        "status": record.get("status", "malformed_source"),
        "evidence_class": "synthetic_fixture",
        "reliability_mode": "local_structural_field",
        "content_contract": content_contract,
        "cost_evidence_mode": "not_applicable",
        "comparability": "not_comparable",
        "source_artifact_ref": ref,
        "line_number": ref["line_number"],
        "redaction_state": record.get("redaction_state", "synthetic"),
        "provenance": _provenance(path, line_number),
    }


def normalize_local_jsonl(path: str | Path) -> dict[str, Any]:
    """Normalize a synthetic Claude Code local JSONL fixture."""

    path_obj = Path(path)
    _reject_disallowed_source_path(path_obj)
    output = empty_adapter_output(SOURCE_KIND)
    artifact_id = path_obj.name
    session_id: str | None = None
    first_ref: dict[str, Any] | None = None
    thinking_signal = False

    with open(path_obj, "r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                output["parse_diagnostics"].append(
                    _diagnostic(
                        path=path_obj,
                        line_number=line_number,
                        line=line,
                        artifact_id=artifact_id,
                        record={
                            "status": "malformed_source",
                            "content_contract": "metadata_only",
                            "message": f"invalid JSON: {exc.msg}",
                        },
                    )
                )
                continue
            if not isinstance(record, dict):
                continue

            record_type = str(record.get("record_type", "unknown"))
            content_contract = record.get("content_contract", "structural_only")
            ref = _source_ref(
                path_obj,
                line_number=line_number,
                line=line,
                artifact_id=artifact_id,
                content_contract=content_contract,
            )
            first_ref = first_ref or ref
            provenance = _provenance(path_obj, line_number)

            if record_type == "parse_diagnostic":
                output["parse_diagnostics"].append(
                    _diagnostic(path=path_obj, line_number=line_number, line=line, artifact_id=artifact_id, record=record)
                )
                continue

            if record_type == "session" and isinstance(record.get("session_id"), str):
                session_id = record["session_id"]
                output["sessions"].append(_session_row(path_obj, line_number, line, record, artifact_id))
                output["observations"].append(
                    _observation(
                        entity_type="session",
                        entity_id=session_id,
                        metric_id="session.present",
                        status="measured",
                        reliability_mode="local_structural_field",
                        comparability="surface_semantics_differ",
                        ref=ref,
                        provenance=provenance,
                        value={"present": True},
                    )
                )

            runtime_item = _runtime_item(
                path=path_obj,
                line_number=line_number,
                line=line,
                record=record,
                artifact_id=artifact_id,
                session_id=session_id,
            )
            output["runtime_response_items"].append(runtime_item)
            output["turns"].append(
                {
                    "turn_id": runtime_item["runtime_item_id"],
                    "session_id": runtime_item["session_id"],
                    "turn_index": len(output["turns"]) + 1,
                    "source_artifact_ref": ref,
                    "provenance": provenance,
                    "payload": {"anthropic": {"record_type": _safe_record_type(record_type)}},
                }
            )

            if record_type == "tool":
                output["tool_calls"].append(
                    {
                        "tool_call_id": record.get("tool_call_id") or runtime_item["runtime_item_id"],
                        "session_id": runtime_item["session_id"],
                        "tool_name": _safe_tool_name(record.get("tool_name")),
                        "redaction_state": record.get("redaction_state", "synthetic"),
                        "content_contract": content_contract,
                        "source_artifact_ref": ref,
                        "provenance": provenance,
                        "payload": {"claude_code": {"argument_shape": _sanitized_argument_shape(record.get("argument_shape"))}},
                    }
                )
            elif record_type == "sidechain_agent":
                agent_id = record.get("agent_id") or runtime_item["runtime_item_id"]
                output["entity_edges"].append(
                    {
                        "source_entity_type": "session",
                        "source_entity_id": runtime_item["session_id"],
                        "predicate": "session.has_sidechain_agent",
                        "target_entity_type": "sidechain_agent",
                        "target_entity_id": agent_id,
                        "source_artifact_ref": ref,
                        "payload": {
                            "claude_code": {
                                "agent_role_present": isinstance(record.get("agent_role"), str)
                                and bool(record.get("agent_role"))
                            }
                        },
                        "provenance": provenance,
                    }
                )

            if (
                record_type == "thinking_summary"
                or record.get("thinking_summary_present") is True
                or isinstance(record.get("facets"), list)
            ):
                thinking_signal = True

    if session_id and first_ref:
        output["token_observations"].append(_token_observation(session_id, first_ref, _provenance(path_obj, 1)))
        if thinking_signal:
            output["observations"].append(
                _observation(
                    entity_type="session",
                    entity_id=session_id,
                    metric_id="runtime.reasoning.substitute_signal",
                    status="derived",
                    reliability_mode="substitute_signal",
                    comparability="insufficient_evidence",
                    ref=first_ref,
                    provenance=_provenance(path_obj, 1),
                    value={"signal": "thinking_summary_or_facets_present"},
                )
            )

    return output
