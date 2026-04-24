"""Fixture-local rebuild helpers for the model benchmark SQLite cache."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Any

from tooling.codex.model_benchmark import manifest, store


HASH_ALGORITHM = "sha256"
PROVIDER_NEUTRALITY_REQUIRED_FIXTURES = frozenset(
    {
        "manual_run_with_rubric_dimensions",
        "claude_local_jsonl_minimal_structure",
        "provider_denominator_mismatch",
    }
)


def _hash_bytes(value: bytes) -> str:
    return f"{HASH_ALGORITHM}:{hashlib.sha256(value).hexdigest()}"


def _json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _source_kind(registry: dict[str, Any]) -> str:
    source_kinds = registry.get("source_kinds") or []
    if not source_kinds:
        raise ValueError("registry must declare at least one source_kind")
    return str(source_kinds[0]["id"])


def _metric_id(registry: dict[str, Any]) -> str | None:
    metrics = registry.get("metrics") or []
    return str(metrics[0]["id"]) if metrics else None


def _source_set_hash(source_infos: list[dict[str, str]]) -> str:
    payload = [
        {"source_uri": info["source_uri"], "source_hash": info["source_hash"]}
        for info in sorted(source_infos, key=lambda item: item["source_uri"])
    ]
    return _hash_bytes(_json_dumps(payload).encode("utf-8"))


def _parse_jsonl_diagnostics(path: Path) -> list[dict[str, Any]]:
    diagnostics: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                diagnostics.append(
                    {
                        "source_path": path.name,
                        "line_number": line_number,
                        "status": "malformed_source",
                        "evidence_class": "synthetic_fixture",
                        "reliability_mode": "direct_field",
                        "content_contract": "metadata_only",
                        "cost_evidence_mode": "not_applicable",
                        "comparability": "not_comparable",
                        "message": f"invalid JSON: {exc.msg}",
                    }
                )
                continue
            if not isinstance(value, dict):
                diagnostics.append(
                    {
                        "source_path": path.name,
                        "line_number": line_number,
                        "status": "malformed_source",
                        "evidence_class": "synthetic_fixture",
                        "reliability_mode": "direct_field",
                        "content_contract": "metadata_only",
                        "cost_evidence_mode": "not_applicable",
                        "comparability": "not_comparable",
                        "message": "JSONL row must be an object",
                    }
                )
    return diagnostics


def _fixture_identity(path: Path) -> tuple[str, str]:
    parent = path.parent.name
    if path.name == "manual_run.json" and parent == "manual_run_with_rubric_dimensions":
        return parent, "benchmark.manual_run"
    if path.name == "session.jsonl" and parent == "claude_local_jsonl_minimal_structure":
        return parent, "runtime.claude_code.local_jsonl"
    if path.name == "expected_normalized.json" and parent == "provider_denominator_mismatch":
        return parent, "provider.usage_fixture"
    if path.name == "stream.jsonl" and parent == "codex_rollout_redacted_stream":
        return parent, "runtime.codex_cli.rollout_stream"
    return parent, path.suffix.lstrip(".") or "unknown"


def _registry_source_kinds(registry: dict[str, Any]) -> set[str]:
    return {str(item["id"]) for item in registry.get("source_kinds", [])}


def _insert_rubric_observation(conn: sqlite3.Connection, row: dict[str, Any]) -> int:
    cursor = conn.execute(
        """
        INSERT INTO rubric_observations(
            entity_type,
            entity_id,
            rubric_id,
            dimension_id,
            status,
            evidence_class,
            reliability_mode,
            content_contract,
            comparability,
            source_artifact_id,
            value_json,
            provenance_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            row["entity_type"],
            row["entity_id"],
            row["rubric_id"],
            row["dimension_id"],
            row["status"],
            row["evidence_class"],
            row["reliability_mode"],
            row["content_contract"],
            row.get("comparability"),
            row["source_artifact_id"],
            _json_dumps(row["value_json"]),
            _json_dumps(row["provenance_json"]),
        ),
    )
    conn.commit()
    return int(cursor.lastrowid)


def _insert_manual_rubrics(conn: sqlite3.Connection, path: Path, source_artifact_id: int) -> int:
    payload = json.loads(path.read_text(encoding="utf-8"))
    count = 0
    for observation in payload.get("rubric_observations", []):
        _insert_rubric_observation(
            conn,
            {
                "entity_type": "run",
                "entity_id": payload["run_id"],
                "rubric_id": observation["rubric_id"],
                "dimension_id": observation["dimension_id"],
                "status": observation["status"],
                "evidence_class": observation["evidence_class"],
                "reliability_mode": observation["reliability_mode"],
                "content_contract": observation["content_contract"],
                "comparability": observation["comparability"],
                "source_artifact_id": source_artifact_id,
                "value_json": {"value": observation.get("value")},
                "provenance_json": {
                    "fixture_id": "manual_run_with_rubric_dimensions",
                    "source_path": str(path),
                },
            },
        )
        count += 1
    return count


def _insert_claude_jsonl(conn: sqlite3.Connection, path: Path, source_artifact_id: int) -> dict[str, int]:
    inserted_items = 0
    inserted_diagnostics = 0
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                record = {
                    "record_type": "parse_diagnostic",
                    "line_number": line_number,
                    "status": "malformed_source",
                    "redaction_state": "synthetic",
                    "content_contract": "metadata_only",
                    "message": f"invalid JSON: {exc.msg}",
                }
            if not isinstance(record, dict):
                continue
            record_type = str(record.get("record_type", "unknown"))
            if record_type == "parse_diagnostic":
                diagnostic = {
                    "source_path": path.name,
                    "line_number": int(record.get("line_number", line_number)),
                    "status": record.get("status", "malformed_source"),
                    "evidence_class": "synthetic_fixture",
                    "reliability_mode": "local_structural_field",
                    "content_contract": record.get("content_contract", "metadata_only"),
                    "cost_evidence_mode": "not_applicable",
                    "comparability": "not_comparable",
                    "redaction_state": record.get("redaction_state", "synthetic"),
                }
                store.insert_observation(
                    conn,
                    {
                        "entity_type": "source_artifact",
                        "entity_id": str(source_artifact_id),
                        "metric_id": "source.parse_status",
                        "status": diagnostic["status"],
                        "evidence_class": diagnostic["evidence_class"],
                        "reliability_mode": diagnostic["reliability_mode"],
                        "content_contract": diagnostic["content_contract"],
                        "comparability": diagnostic["comparability"],
                        "source_artifact_id": source_artifact_id,
                        "value_json": diagnostic,
                        "provenance_json": {
                            "fixture_id": "claude_local_jsonl_minimal_structure",
                            "line_number": line_number,
                        },
                    },
                )
                inserted_diagnostics += 1
                continue
            store.insert_runtime_response_item(
                conn,
                {
                    "session_id": None,
                    "turn_id": None,
                    "model_call_id": None,
                    "source_artifact_id": source_artifact_id,
                    "source_kind": "runtime.claude_code.local_jsonl",
                    "provider_namespace": "provider.anthropic",
                    "runtime_namespace": "runtime.claude_code",
                    "item_type": record_type,
                    "status": record.get("status", "unknown"),
                    "role": record.get("role"),
                    "redaction_state": record.get("redaction_state", "synthetic"),
                    "content_state": "redacted_reference" if record.get("content_ref") else "structural_only",
                    "correlation_status": "unknown",
                    "payload_json": {
                        "claude": {
                            "record_type": record_type,
                            "content_contract": record.get("content_contract", "structural_only"),
                        }
                    },
                    "provenance_json": {
                        "fixture_id": "claude_local_jsonl_minimal_structure",
                        "source_path": str(path),
                        "line_number": line_number,
                    },
                },
            )
            inserted_items += 1
    return {"runtime_items": inserted_items, "diagnostics": inserted_diagnostics}


def _insert_provider_usage(conn: sqlite3.Connection, path: Path, source_artifact_id: int) -> int:
    payload = json.loads(path.read_text(encoding="utf-8"))
    observations = payload.get("observations", {})
    count = 0
    metric_by_axis = {
        "input_tokens": "tokens.input",
        "cache_read_tokens": "tokens.cache_read",
        "reasoning_tokens": "tokens.reasoning",
        "cost": "cost.total",
        "quota": "quota.status",
    }
    for provider, axes in observations.items():
        if not isinstance(axes, dict):
            continue
        for axis, value in axes.items():
            if not isinstance(value, dict):
                continue
            status = str(value.get("status", "measured"))
            metric_id = metric_by_axis.get(axis, f"provider.{axis}")
            cost_mode = value.get("cost_evidence_mode")
            store.insert_observation(
                conn,
                {
                    "entity_type": "provider_usage",
                    "entity_id": str(provider),
                    "metric_id": metric_id,
                    "status": status,
                    "evidence_class": "synthetic_fixture",
                    "reliability_mode": "provider_emitted" if provider == "openai" else "estimated_from_pricing",
                    "content_contract": payload.get("content_contract", "metadata_only"),
                    "comparability": "provider_semantics_differ",
                    "source_artifact_id": source_artifact_id,
                    "value_json": {"provider": provider, "axis": axis, **value},
                    "provenance_json": {
                        "fixture_id": "provider_denominator_mismatch",
                        "source_path": str(path),
                    },
                },
            )
            if axis == "cost" and cost_mode:
                store.insert_cost_estimate(
                    conn,
                    {
                        "run_id": f"{provider}-fixture",
                        "source_artifact_id": source_artifact_id,
                        "cost_evidence_mode": cost_mode,
                        "comparability": "provider_semantics_differ",
                        "cost_json": {"provider": provider, **value},
                        "provenance_json": {"fixture_id": "provider_denominator_mismatch"},
                    },
                )
            count += 1
    return count


def rebuild_fixture_sources(
    conn: sqlite3.Connection,
    registry: dict[str, Any],
    source_paths: list[str | Path],
) -> dict[str, Any]:
    """Rebuild a fixture-local cache slice from JSONL sources.

    This intentionally does not implement a broad adapter framework. It records
    registry/source parity and metadata-only parse diagnostics for local
    fixtures.
    """

    if "registry_hash" not in registry:
        registry = manifest.validate_manifest(registry)

    store.insert_registry(
        conn,
        {
            "registry_id": registry["registry_id"],
            "registry_version": registry["registry_version"],
            "registry_hash": registry["registry_hash"],
            "canonical_json": manifest.canonical_json(registry),
        },
    )

    source_infos: list[dict[str, str]] = []
    diagnostics: list[dict[str, Any]] = []
    source_kind = _source_kind(registry)
    metric_id = _metric_id(registry)
    for raw_path in source_paths:
        path = Path(raw_path)
        source_bytes = path.read_bytes()
        source_hash = _hash_bytes(source_bytes)
        source_infos.append({"source_uri": str(path), "source_hash": source_hash})
        source_artifact_id = store.insert_source_artifact(
            conn,
            {
                "source_kind": source_kind,
                "source_uri": str(path),
                "source_hash": source_hash,
                "content_contract": "metadata_only",
                "provenance_json": {"created_by": "model_benchmark.rebuild_fixture_sources"},
            },
        )
        for diagnostic in _parse_jsonl_diagnostics(path):
            diagnostics.append(diagnostic)
            store.insert_observation(
                conn,
                {
                    "entity_type": "source_artifact",
                    "entity_id": str(source_artifact_id),
                    "metric_id": metric_id,
                    "status": diagnostic["status"],
                    "evidence_class": diagnostic["evidence_class"],
                    "reliability_mode": diagnostic["reliability_mode"],
                    "content_contract": diagnostic["content_contract"],
                    "comparability": diagnostic["comparability"],
                    "source_artifact_id": source_artifact_id,
                    "value_json": diagnostic,
                    "provenance_json": {
                        "source_path": diagnostic["source_path"],
                        "line_number": diagnostic["line_number"],
                    },
                },
            )

    source_hash = _source_set_hash(source_infos)
    rebuild_id = store.insert_rebuild_run(
        conn,
        {
            "schema_version": store.SCHEMA_VERSION,
            "registry_version": registry["registry_version"],
            "registry_hash": registry["registry_hash"],
            "source_set_hash": source_hash,
            "status": "completed",
            "completed_at": "1970-01-01T00:00:00Z",
            "provenance_json": {
                "source_count": len(source_infos),
                "diagnostic_count": len(diagnostics),
            },
        },
    )
    return {
        "rebuild_id": rebuild_id,
        "schema_version": store.SCHEMA_VERSION,
        "registry_version": registry["registry_version"],
        "registry_hash": registry["registry_hash"],
        "source_set_hash": source_hash,
        "diagnostics": diagnostics,
    }


def rebuild_provider_neutrality_gate(
    conn: sqlite3.Connection,
    registry: dict[str, Any],
    source_paths: list[str | Path],
    *,
    strict: bool = True,
) -> dict[str, Any]:
    """Rebuild the synthetic provider-neutrality gate fixture set.

    This is deliberately fixture-scoped. It proves the strict
    manifest/rebuild/query path for non-Codex shapes without introducing live
    provider adapters or a broad ingestion framework.
    """

    if "registry_hash" not in registry:
        registry = manifest.validate_manifest(registry)

    declared_source_kinds = _registry_source_kinds(registry)
    source_infos: list[dict[str, str]] = []
    fixture_ids: list[str] = []
    counts = {"rubric_observations": 0, "runtime_items": 0, "diagnostics": 0, "provider_observations": 0}

    store.insert_registry(
        conn,
        {
            "registry_id": registry["registry_id"],
            "registry_version": registry["registry_version"],
            "registry_hash": registry["registry_hash"],
            "canonical_json": manifest.canonical_json(registry),
        },
    )

    for raw_path in source_paths:
        path = Path(raw_path)
        fixture_id, source_kind = _fixture_identity(path)
        if strict and source_kind not in declared_source_kinds:
            raise ValueError(f"undeclared source_kind: {source_kind}")
        source_bytes = path.read_bytes()
        source_hash = _hash_bytes(source_bytes)
        source_infos.append({"source_uri": str(path), "source_hash": source_hash})
        fixture_ids.append(fixture_id)
        content_contract = "metadata_only"
        if fixture_id == "manual_run_with_rubric_dimensions":
            content_contract = "derived_features_only"
        elif fixture_id == "claude_local_jsonl_minimal_structure":
            content_contract = "structural_only"
        source_artifact_id = store.insert_source_artifact(
            conn,
            {
                "source_kind": source_kind,
                "source_uri": str(path),
                "source_hash": source_hash,
                "content_contract": content_contract,
                "provenance_json": {
                    "created_by": "model_benchmark.rebuild_provider_neutrality_gate",
                    "fixture_id": fixture_id,
                },
            },
        )
        if fixture_id == "manual_run_with_rubric_dimensions":
            counts["rubric_observations"] += _insert_manual_rubrics(conn, path, source_artifact_id)
        elif fixture_id == "claude_local_jsonl_minimal_structure":
            claude_counts = _insert_claude_jsonl(conn, path, source_artifact_id)
            counts["runtime_items"] += claude_counts["runtime_items"]
            counts["diagnostics"] += claude_counts["diagnostics"]
        elif fixture_id == "provider_denominator_mismatch":
            counts["provider_observations"] += _insert_provider_usage(conn, path, source_artifact_id)
        else:
            for diagnostic in _parse_jsonl_diagnostics(path):
                counts["diagnostics"] += 1
                store.insert_observation(
                    conn,
                    {
                        "entity_type": "source_artifact",
                        "entity_id": str(source_artifact_id),
                        "metric_id": "source.parse_status",
                        "status": diagnostic["status"],
                        "evidence_class": diagnostic["evidence_class"],
                        "reliability_mode": diagnostic["reliability_mode"],
                        "content_contract": diagnostic["content_contract"],
                        "comparability": diagnostic["comparability"],
                        "source_artifact_id": source_artifact_id,
                        "value_json": diagnostic,
                        "provenance_json": {"fixture_id": fixture_id},
                    },
                )

    source_hash = _source_set_hash(source_infos)
    gate_passed = PROVIDER_NEUTRALITY_REQUIRED_FIXTURES.issubset(set(fixture_ids))
    rebuild_id = store.insert_rebuild_run(
        conn,
        {
            "schema_version": store.SCHEMA_VERSION,
            "registry_version": registry["registry_version"],
            "registry_hash": registry["registry_hash"],
            "source_set_hash": source_hash,
            "status": "completed",
            "completed_at": "1970-01-01T00:00:00Z",
            "provenance_json": {
                "provider_neutrality_gate": True,
                "gate_status": "passed" if gate_passed else "not_passed",
                "fixture_ids": sorted(set(fixture_ids)),
                **counts,
            },
        },
    )
    return {
        "rebuild_id": rebuild_id,
        "schema_version": store.SCHEMA_VERSION,
        "registry_version": registry["registry_version"],
        "registry_hash": registry["registry_hash"],
        "source_set_hash": source_hash,
        "provider_neutrality_gate": {"status": "passed" if gate_passed else "not_passed"},
        **counts,
    }
