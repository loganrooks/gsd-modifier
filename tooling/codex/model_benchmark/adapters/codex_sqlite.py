"""Adapter for synthetic Codex SQLite index exports.

The adapter consumes an explicit fixture export path. It does not discover or
open live Codex home-state databases.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from tooling.codex.model_benchmark.adapters import empty_adapter_output


SOURCE_KIND = "runtime.codex_cli.sqlite_index"
PROVIDER_NAMESPACE = "provider.openai"
RUNTIME_NAMESPACE = "runtime.codex_cli"


def _read_json_object(path: Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def _file_hash(path: Path) -> str:
    return f"sha256:{hashlib.sha256(path.read_bytes()).hexdigest()}"


def _source_ref(path: Path, source: dict[str, Any], *, line_number: int = 1) -> dict[str, Any]:
    artifact = source.get("source_artifact", {})
    if not isinstance(artifact, dict):
        artifact = {}
    source_hash = artifact.get("hash") or _file_hash(path)
    return {
        "artifact_id": artifact.get("artifact_id", path.name),
        "source_uri": str(path),
        "source_hash": source_hash,
        "line_number": line_number,
        "line_hash": _file_hash(path),
        "content_contract": source.get("content_contract", "metadata_only"),
    }


def _provenance(path: Path) -> dict[str, Any]:
    return {
        "adapter": "codex_sqlite",
        "source_path": str(path),
        "evidence_class": "synthetic_fixture",
        "reliability_mode": "local_structural_field",
    }


def _baseline_observation(entity_type: str, entity_id: str, metric_id: str, ref: dict[str, Any]) -> dict[str, Any]:
    return {
        "entity_type": entity_type,
        "entity_id": entity_id,
        "metric_id": metric_id,
        "status": "measured",
        "evidence_class": "synthetic_fixture",
        "reliability_mode": "local_structural_field",
        "content_contract": ref["content_contract"],
        "comparability": "surface_semantics_differ",
        "source_artifact_ref": ref,
        "value": {"present": True},
        "provenance": {"adapter": "codex_sqlite"},
    }


def _environment_observations(entity_id: str, ref: dict[str, Any]) -> list[dict[str, Any]]:
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
            "reliability_mode": "local_structural_field",
            "content_contract": ref["content_contract"],
            "comparability": "insufficient_evidence",
            "source_artifact_ref": ref,
            "value": {"state": value},
            "provenance": {"adapter": "codex_sqlite"},
        }
        for metric_id, status, value in metrics
    ]


def normalize_source_index(path: str | Path) -> dict[str, Any]:
    """Normalize a synthetic Codex SQLite source-index export."""

    path_obj = Path(path)
    source = _read_json_object(path_obj)
    ref = _source_ref(path_obj, source)
    output = empty_adapter_output(SOURCE_KIND)
    output["content_contract"] = ref["content_contract"]

    tables = source.get("tables", {})
    if not isinstance(tables, dict):
        raise ValueError("tables must be an object")

    for index, session in enumerate(tables.get("sessions", []), start=1):
        if not isinstance(session, dict):
            raise ValueError(f"tables.sessions[{index}] must be an object")
        session_id = session.get("session_id")
        if not isinstance(session_id, str) or not session_id:
            raise ValueError(f"tables.sessions[{index}].session_id is required")
        session_ref = dict(ref)
        output["sessions"].append(
            {
                "session_id": session_id,
                "provider_namespace": PROVIDER_NAMESPACE,
                "runtime_namespace": RUNTIME_NAMESPACE,
                "source_artifact_ref": session_ref,
                "provenance": _provenance(path_obj),
                "payload": {"codex": {"table": "sessions", "created_at_present": "created_at" in session}},
            }
        )
        subagent_id = f"{session_id}:subagent:synthetic"
        output["entity_edges"].append(
            {
                "source_entity_type": "session",
                "source_entity_id": session_id,
                "predicate": "session.has_subagent",
                "target_entity_type": "subagent",
                "target_entity_id": subagent_id,
                "source_artifact_ref": session_ref,
                "payload": {"codex": {"edge_source": "sqlite_index_export"}},
                "provenance": _provenance(path_obj),
            }
        )
        output["observations"].append(_baseline_observation("session", session_id, "session.present", ref))
        output["observations"].extend(_environment_observations(session_id, ref))

    for index, item in enumerate(tables.get("runtime_items", []), start=1):
        if not isinstance(item, dict):
            raise ValueError(f"tables.runtime_items[{index}] must be an object")
        runtime_item_id = item.get("item_id") or f"runtime-item-{index}"
        session_id = item.get("session_id")
        output["turns"].append(
            {
                "turn_id": runtime_item_id,
                "session_id": session_id,
                "turn_index": index,
                "source_artifact_ref": ref,
                "provenance": _provenance(path_obj),
                "payload": {"codex": {"table": "runtime_items", "item_id": runtime_item_id}},
            }
        )
        output["runtime_response_items"].append(
            {
                "runtime_item_id": runtime_item_id,
                "session_id": session_id,
                "model_call_id": None,
                "source_kind": SOURCE_KIND,
                "provider_namespace": PROVIDER_NAMESPACE,
                "runtime_namespace": RUNTIME_NAMESPACE,
                "item_type": item.get("item_type", "unknown"),
                "status": item.get("status", "unknown"),
                "role": item.get("role"),
                "redaction_state": item.get("content_state", "redacted"),
                "content_state": item.get("content_state", "redacted"),
                "correlation_status": item.get("correlation_status", "unknown"),
                "source_artifact_ref": ref,
                "provenance": _provenance(path_obj),
                "payload": {"codex": {"table": "runtime_items", "item_id": runtime_item_id}},
            }
        )

    output["token_observations"].append(
        {
            "entity_type": "session",
            "entity_id": output["sessions"][0]["session_id"] if output["sessions"] else "unknown",
            "metric_id": "tokens.local_runtime",
            "status": "not_exposed",
            "evidence_class": "synthetic_fixture",
            "reliability_mode": "local_structural_field",
            "content_contract": ref["content_contract"],
            "cost_evidence_mode": "not_exposed",
            "comparability": "insufficient_evidence",
            "source_artifact_ref": ref,
            "value": {"tokens": "not_exposed"},
            "provenance": {"adapter": "codex_sqlite"},
        }
    )
    output["parse_diagnostics"].append(
        {
            "status": "measured",
            "evidence_class": "synthetic_fixture",
            "reliability_mode": "direct_field",
            "content_contract": ref["content_contract"],
            "comparability": "not_comparable",
            "source_artifact_ref": ref,
            "message": "parsed",
            "provenance": {"adapter": "codex_sqlite"},
        }
    )
    return output
