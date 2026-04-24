"""Small structured query helpers for model benchmark rebuild parity."""

from __future__ import annotations

import json
import re
import sqlite3
from typing import Any


_HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")


def _latest_rebuild(conn: sqlite3.Connection) -> sqlite3.Row:
    row = conn.execute(
        """
        SELECT id, schema_version, registry_version, registry_hash, source_set_hash, status, provenance_json
        FROM rebuild_runs
        ORDER BY id DESC
        LIMIT 1
        """
    ).fetchone()
    if row is None:
        raise ValueError("no rebuild_runs are recorded")
    return row


def _json_object(value: str) -> dict[str, Any]:
    loaded = json.loads(value)
    if not isinstance(loaded, dict):
        raise ValueError("stored JSON value must be an object")
    return loaded


def _validate_hash(value: str, field: str, strict: bool) -> None:
    if strict and not _HASH_RE.match(value):
        raise ValueError(f"{field} must be a sha256 hash")


def _table_json_rows(conn: sqlite3.Connection, sql: str, args: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    return [_json_object(row[0]) for row in conn.execute(sql, args).fetchall()]


def query_rebuild_summary(
    conn: sqlite3.Connection,
    *,
    registry_hash: str | None = None,
    strict: bool = True,
) -> dict[str, Any]:
    """Return the latest rebuild parity metadata and parse diagnostics."""

    rebuild = _latest_rebuild(conn)
    actual_hash = str(rebuild["registry_hash"])
    if strict and registry_hash is not None and registry_hash != actual_hash:
        raise ValueError(f"registry_hash mismatch: expected {registry_hash}, found {actual_hash}")

    diagnostic_rows = conn.execute(
        """
        SELECT value_json
        FROM observations
        WHERE status = ?
        ORDER BY id
        """,
        ("malformed_source",),
    ).fetchall()
    diagnostics = [_json_object(row["value_json"]) for row in diagnostic_rows]
    return {
        "rebuild_id": int(rebuild["id"]),
        "schema_version": str(rebuild["schema_version"]),
        "registry_version": str(rebuild["registry_version"]),
        "registry_hash": actual_hash,
        "source_set_hash": str(rebuild["source_set_hash"]),
        "status": str(rebuild["status"]),
        "diagnostic_count": len(diagnostics),
        "diagnostics": diagnostics,
    }


def query_provider_neutrality_gate(
    conn: sqlite3.Connection,
    *,
    registry_hash: str | None = None,
    strict: bool = True,
) -> dict[str, Any]:
    """Return the synthetic provider-neutrality gate evidence summary."""

    rebuild = _latest_rebuild(conn)
    actual_hash = str(rebuild["registry_hash"])
    source_set_hash = str(rebuild["source_set_hash"])
    if strict and registry_hash is not None and registry_hash != actual_hash:
        raise ValueError(f"registry_hash mismatch: expected {registry_hash}, found {actual_hash}")
    _validate_hash(actual_hash, "registry_hash", strict)
    _validate_hash(source_set_hash, "source_set_hash", strict)

    provenance = _json_object(str(rebuild["provenance_json"]))
    if strict and provenance.get("provider_neutrality_gate") is not True:
        raise ValueError("provider_neutrality_gate rebuild provenance is required")

    rubric_observations = _table_json_rows(
        conn,
        """
        SELECT json_object(
            'entity_type', entity_type,
            'entity_id', entity_id,
            'rubric_id', rubric_id,
            'dimension_id', dimension_id,
            'status', status,
            'evidence_class', evidence_class,
            'reliability_mode', reliability_mode,
            'content_contract', content_contract,
            'comparability', comparability,
            'value', json(value_json),
            'provenance', json(provenance_json)
        )
        FROM rubric_observations
        ORDER BY id
        """,
    )

    runtime_response_items = _table_json_rows(
        conn,
        """
        SELECT json_object(
            'source_kind', source_kind,
            'provider_namespace', provider_namespace,
            'runtime_namespace', runtime_namespace,
            'item_type', item_type,
            'status', status,
            'role', role,
            'redaction_state', redaction_state,
            'content_state', content_state,
            'correlation_status', correlation_status,
            'payload', json(payload_json),
            'provenance', json(provenance_json)
        )
        FROM runtime_response_items
        ORDER BY id
        """,
    )

    diagnostics = _table_json_rows(
        conn,
        """
        SELECT value_json
        FROM observations
        WHERE status = ?
        ORDER BY id
        """,
        ("malformed_source",),
    )

    provider_usage: dict[str, dict[str, Any]] = {}
    rows = conn.execute(
        """
        SELECT value_json
        FROM observations
        WHERE entity_type = ?
        ORDER BY id
        """,
        ("provider_usage",),
    ).fetchall()
    for row in rows:
        value = _json_object(row["value_json"])
        provider = str(value.pop("provider"))
        axis = str(value.pop("axis"))
        provider_usage.setdefault(provider, {})[axis] = value

    fixture_ids = set(provenance.get("fixture_ids", []))
    required = {
        "manual_run_with_rubric_dimensions",
        "claude_local_jsonl_minimal_structure",
        "provider_denominator_mismatch",
    }
    gate_status = "passed" if required.issubset(fixture_ids) else "not_passed"
    return {
        "rebuild_id": int(rebuild["id"]),
        "schema_version": str(rebuild["schema_version"]),
        "registry_version": str(rebuild["registry_version"]),
        "registry_hash": actual_hash,
        "source_set_hash": source_set_hash,
        "status": str(rebuild["status"]),
        "provider_neutrality_gate": {
            "status": gate_status,
            "required_fixtures": sorted(required),
            "observed_fixtures": sorted(fixture_ids),
        },
        "rubric_observations": rubric_observations,
        "runtime_response_items": runtime_response_items,
        "diagnostics": diagnostics,
        "provider_usage_evidence": provider_usage,
    }
