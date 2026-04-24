"""Adapter for synthetic Codex rollout JSONL streams."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from tooling.codex.model_benchmark.adapters import empty_adapter_output


SOURCE_KIND = "runtime.codex_cli.rollout_stream"
PROVIDER_NAMESPACE = "provider.openai"
RUNTIME_NAMESPACE = "runtime.codex_cli"


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
        "adapter": "codex_rollout",
        "source_path": str(path),
        "line_number": line_number,
        "evidence_class": "synthetic_fixture",
        "reliability_mode": "runtime_emitted",
    }


def _observation(
    *,
    entity_type: str,
    entity_id: str,
    metric_id: str,
    status: str,
    ref: dict[str, Any],
    provenance: dict[str, Any],
) -> dict[str, Any]:
    return {
        "entity_type": entity_type,
        "entity_id": entity_id,
        "metric_id": metric_id,
        "status": status,
        "evidence_class": "synthetic_fixture",
        "reliability_mode": "runtime_emitted",
        "content_contract": ref["content_contract"],
        "comparability": "surface_semantics_differ",
        "source_artifact_ref": ref,
        "value": {"present": status == "measured"},
        "provenance": provenance,
    }


def _environment_observations(entity_id: str, ref: dict[str, Any], provenance: dict[str, Any]) -> list[dict[str, Any]]:
    metrics = (
        ("runtime.sandbox", "not_collected", "not_collected"),
        ("runtime.approval_policy", "not_collected", "not_collected"),
        ("runtime.git_state", "not_collected", "not_collected"),
        ("runtime.model", "not_exposed", "not_exposed"),
        ("runtime.reasoning", "not_exposed", "not_exposed"),
    )
    return [
        {
            "entity_type": "session",
            "entity_id": entity_id,
            "metric_id": metric_id,
            "status": status,
            "evidence_class": "synthetic_fixture",
            "reliability_mode": "runtime_emitted",
            "content_contract": ref["content_contract"],
            "comparability": "insufficient_evidence",
            "source_artifact_ref": ref,
            "value": {"state": value},
            "provenance": provenance,
        }
        for metric_id, status, value in metrics
    ]


def _content_state(record: dict[str, Any]) -> str:
    if record.get("record_type") == "turn_context" and record.get("marker") == "compacted":
        return "no_content"
    if "content_ref" in record:
        return "redacted_reference"
    return record.get("content_state") or record.get("redaction_state") or "redacted"


def _runtime_item_type(record: dict[str, Any]) -> str:
    if record.get("record_type") == "turn_context" and record.get("marker") == "compacted":
        return "compaction_marker"
    return record.get("item_type") or record.get("record_type") or "unknown"


def _payload(record: dict[str, Any]) -> dict[str, Any]:
    allowed_keys = (
        "record_type",
        "runtime_item_id",
        "item_type",
        "redaction_state",
        "content_contract",
        "content_ref",
        "correlation_status",
        "marker",
    )
    codex_payload = {key: record[key] for key in allowed_keys if key in record}
    return {"codex": codex_payload}


def _runtime_item(
    *,
    path: Path,
    line_number: int,
    line: str,
    record: dict[str, Any],
    session_id: str | None,
    artifact_id: str,
) -> dict[str, Any]:
    content_contract = record.get("content_contract", "redacted_content_reference")
    runtime_item_id = record.get("runtime_item_id") or f"{artifact_id}:line:{line_number}"
    ref = _source_ref(
        path,
        line_number=line_number,
        line=line,
        artifact_id=artifact_id,
        content_contract=content_contract,
    )
    return {
        "runtime_item_id": runtime_item_id,
        "session_id": session_id,
        "model_call_id": None,
        "source_kind": SOURCE_KIND,
        "provider_namespace": PROVIDER_NAMESPACE,
        "runtime_namespace": RUNTIME_NAMESPACE,
        "item_type": _runtime_item_type(record),
        "status": record.get("status", "unknown"),
        "role": record.get("role"),
        "redaction_state": record.get("redaction_state", "redacted"),
        "content_state": _content_state(record),
        "correlation_status": record.get("correlation_status", "not_applicable"),
        "source_artifact_ref": ref,
        "provenance": _provenance(path, line_number),
        "payload": _payload(record),
    }


def normalize_rollout_jsonl(path: str | Path) -> dict[str, Any]:
    """Normalize a synthetic Codex rollout JSONL stream."""

    path_obj = Path(path)
    output = empty_adapter_output(SOURCE_KIND)
    session_id: str | None = None
    artifact_id = path_obj.name
    first_ref: dict[str, Any] | None = None

    with open(path_obj, "r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                ref = _source_ref(
                    path_obj,
                    line_number=line_number,
                    line=line,
                    artifact_id=artifact_id,
                    content_contract="metadata_only",
                )
                output["parse_diagnostics"].append(
                    {
                        "status": "malformed_source",
                        "evidence_class": "synthetic_fixture",
                        "reliability_mode": "direct_field",
                        "content_contract": "metadata_only",
                        "comparability": "not_comparable",
                        "source_artifact_ref": ref,
                        "line_number": line_number,
                        "provenance": _provenance(path_obj, line_number),
                    }
                )
                continue
            if not isinstance(record, dict):
                continue
            record_type = record.get("record_type")
            content_contract = record.get("content_contract", "redacted_content_reference")
            ref = _source_ref(
                path_obj,
                line_number=line_number,
                line=line,
                artifact_id=artifact_id,
                content_contract=content_contract,
            )
            first_ref = first_ref or ref
            if record_type == "session_meta":
                session_id = record.get("session_id") or session_id
                if isinstance(session_id, str):
                    provenance = _provenance(path_obj, line_number)
                    output["sessions"].append(
                        {
                            "session_id": session_id,
                            "provider_namespace": PROVIDER_NAMESPACE,
                            "runtime_namespace": RUNTIME_NAMESPACE,
                            "source_artifact_ref": ref,
                            "provenance": provenance,
                            "payload": {"codex": {"record_type": record_type}},
                        }
                    )
                    output["observations"].append(
                        _observation(
                            entity_type="session",
                            entity_id=session_id,
                            metric_id="session.present",
                            status="measured",
                            ref=ref,
                            provenance=provenance,
                        )
                    )
                    output["observations"].extend(_environment_observations(session_id, ref, provenance))
                continue
            if record_type in {"runtime_item", "response_item", "turn_context"}:
                runtime_item_id = record.get("runtime_item_id") or f"{artifact_id}:line:{line_number}"
                output["turns"].append(
                    {
                        "turn_id": runtime_item_id,
                        "session_id": session_id,
                        "turn_index": len(output["turns"]) + 1,
                        "source_artifact_ref": ref,
                        "provenance": _provenance(path_obj, line_number),
                        "payload": {"codex": {"record_type": record_type}},
                    }
                )
                output["runtime_response_items"].append(
                    _runtime_item(
                        path=path_obj,
                        line_number=line_number,
                        line=line,
                        record=record,
                        session_id=session_id,
                        artifact_id=artifact_id,
                    )
                )
                if record.get("item_type") == "tool_request":
                    output["tool_calls"].append(
                        {
                            "tool_call_id": record.get("runtime_item_id"),
                            "session_id": session_id,
                            "runtime_item_id": record.get("runtime_item_id"),
                            "tool_namespace": "codex",
                            "tool_name": "unknown",
                            "status": "unknown",
                            "source_artifact_ref": ref,
                            "payload": {"codex": {"record_type": record_type}},
                            "provenance": _provenance(path_obj, line_number),
                        }
                    )

    if first_ref is None:
        first_ref = _source_ref(
            path_obj,
            line_number=1,
            line="",
            artifact_id=artifact_id,
            content_contract="metadata_only",
        )
    output["token_observations"].append(
        {
            "entity_type": "session",
            "entity_id": session_id or "unknown",
            "metric_id": "tokens.local_runtime",
            "status": "not_exposed",
            "evidence_class": "synthetic_fixture",
            "reliability_mode": "runtime_emitted",
            "content_contract": first_ref["content_contract"],
            "cost_evidence_mode": "not_exposed",
            "comparability": "insufficient_evidence",
            "source_artifact_ref": first_ref,
            "value": {"tokens": "not_exposed"},
            "provenance": {"adapter": "codex_rollout"},
        }
    )
    if not output["parse_diagnostics"]:
        output["parse_diagnostics"].append(
            {
                "status": "measured",
                "evidence_class": "synthetic_fixture",
                "reliability_mode": "direct_field",
                "content_contract": first_ref["content_contract"],
                "comparability": "not_comparable",
                "source_artifact_ref": first_ref,
                "message": "parsed",
                "provenance": {"adapter": "codex_rollout"},
            }
        )
    return output
