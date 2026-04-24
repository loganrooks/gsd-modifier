"""Small structured query helpers for model benchmark rebuild parity."""

from __future__ import annotations

import json
import re
import sqlite3
from typing import Any

from tooling.codex.model_benchmark.enums import (
    COMPARABILITY_VALUES,
    CONTENT_CONTRACTS,
    COST_EVIDENCE_MODES,
    EVIDENCE_CLASSES,
    OBSERVATION_STATUSES,
    RELIABILITY_MODES,
)
from tooling.codex.model_benchmark.rebuild import (
    PROVIDER_NEUTRALITY_REQUIRED_FIXTURES,
    _source_set_hash,
    provider_neutrality_gate_status,
)


_HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
_NOT_COLLECTED = "not_collected"
_USAGE_METRIC_PREFIX = "usage."
_LEGACY_SCORE_METRIC = "legacy.score.overall"
_DIAGNOSTIC_METRIC = "source.parse_status"
_DIAGNOSTIC_FIELDS = ("line_number", "status", "error_type", "content_contract")


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


def _check_enum(value: Any, allowed: frozenset[str], field: str, strict: bool) -> None:
    if value is None:
        return
    if strict and value not in allowed:
        raise ValueError(f"{field} must be one of {sorted(allowed)}")


def _validate_observation_row(row: sqlite3.Row, strict: bool) -> None:
    _check_enum(row["status"], OBSERVATION_STATUSES, "status", strict)
    _check_enum(row["evidence_class"], EVIDENCE_CLASSES, "evidence_class", strict)
    _check_enum(row["reliability_mode"], RELIABILITY_MODES, "reliability_mode", strict)
    _check_enum(row["content_contract"], CONTENT_CONTRACTS, "content_contract", strict)
    _check_enum(row["comparability"], COMPARABILITY_VALUES, "comparability", strict)


def _validate_cost_row(row: sqlite3.Row, strict: bool) -> None:
    _check_enum(row["cost_evidence_mode"], COST_EVIDENCE_MODES, "cost_evidence_mode", strict)
    _check_enum(row["comparability"], COMPARABILITY_VALUES, "comparability", strict)


def _validate_usage_payload(payload: dict[str, Any], strict: bool) -> None:
    _check_enum(payload.get("missingness"), OBSERVATION_STATUSES, "missingness", strict)
    _check_enum(payload.get("availability_status"), OBSERVATION_STATUSES, "availability_status", strict)


def _table_json_rows(conn: sqlite3.Connection, sql: str, args: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    return [_json_object(row[0]) for row in conn.execute(sql, args).fetchall()]


def _count_rows(conn: sqlite3.Connection, table: str) -> int:
    return int(conn.execute(f"SELECT COUNT(*) AS count FROM {table}").fetchone()["count"])


def _count_observations(conn: sqlite3.Connection, where: str, args: tuple[Any, ...] = ()) -> int:
    row = conn.execute(f"SELECT COUNT(*) AS count FROM observations WHERE {where}", args).fetchone()
    return int(row["count"])


def _source_artifact_filter(source_artifact_ids: set[int]) -> tuple[str, tuple[Any, ...]]:
    if not source_artifact_ids:
        return "0 = 1", ()
    placeholders = ", ".join("?" for _ in source_artifact_ids)
    return f"source_artifact_id IN ({placeholders})", tuple(sorted(source_artifact_ids))


def _gate_source_artifact_ids_by_fixture(
    conn: sqlite3.Connection,
    provenance: dict[str, Any],
    source_set_hash: str,
    strict: bool,
) -> dict[str, set[int]]:
    raw_mapping = provenance.get("source_artifact_ids_by_fixture")
    if raw_mapping is None:
        return {}
    if not isinstance(raw_mapping, dict):
        if strict:
            raise ValueError("source_artifact_ids_by_fixture must be an object")
        return {}

    mapping: dict[str, set[int]] = {}
    for fixture_id, raw_ids in raw_mapping.items():
        if not isinstance(raw_ids, list):
            if strict:
                raise ValueError("source_artifact_ids_by_fixture values must be arrays")
            continue
        artifact_ids: set[int] = set()
        for raw_id in raw_ids:
            if not isinstance(raw_id, int) or raw_id <= 0:
                if strict:
                    raise ValueError("source_artifact_ids_by_fixture values must contain positive integer ids")
                continue
            artifact_ids.add(raw_id)
        mapping[str(fixture_id)] = artifact_ids

    all_artifact_ids = {artifact_id for artifact_ids in mapping.values() for artifact_id in artifact_ids}
    if not all_artifact_ids:
        return mapping

    placeholders = ", ".join("?" for _ in all_artifact_ids)
    rows = conn.execute(
        f"""
        SELECT id, source_uri, source_hash
        FROM source_artifacts
        WHERE id IN ({placeholders})
        ORDER BY id
        """,
        tuple(sorted(all_artifact_ids)),
    ).fetchall()
    if len(rows) != len(all_artifact_ids):
        if strict:
            raise ValueError("source_artifact_ids_by_fixture references missing source_artifacts")
        return {}

    source_infos = [
        {"source_uri": str(row["source_uri"]), "source_hash": str(row["source_hash"])}
        for row in rows
    ]
    if _source_set_hash(source_infos) != source_set_hash:
        return {}
    return mapping


def _count_fixture_rows(
    conn: sqlite3.Connection,
    table: str,
    fixture_id: str,
    source_artifact_ids: set[int],
    where: str = "1 = 1",
) -> int:
    source_filter, args = _source_artifact_filter(source_artifact_ids)
    rows = conn.execute(
        f"SELECT provenance_json FROM {table} WHERE {where} AND {source_filter}",
        args,
    ).fetchall()
    count = 0
    for row in rows:
        provenance = _json_object(row["provenance_json"])
        if provenance.get("fixture_id") == fixture_id:
            count += 1
    return count


def _status_counts(conn: sqlite3.Connection, sql: str, args: tuple[Any, ...] = ()) -> dict[str, int]:
    rows = conn.execute(sql, args).fetchall()
    return {str(row["status"]): int(row["count"]) for row in rows}


def _usage_missingness_counts(conn: sqlite3.Connection) -> dict[str, int]:
    counts: dict[str, int] = {}
    rows = conn.execute(
        """
        SELECT value_json
        FROM observations
        WHERE metric_id LIKE ?
        ORDER BY id
        """,
        (f"{_USAGE_METRIC_PREFIX}%",),
    ).fetchall()
    for row in rows:
        value = _json_object(row["value_json"])
        missingness = str(value.get("missingness", "unknown"))
        counts[missingness] = counts.get(missingness, 0) + 1
    return dict(sorted(counts.items()))


def _cost_evidence_mode_counts(conn: sqlite3.Connection) -> dict[str, int]:
    counts = {mode: 0 for mode in sorted(COST_EVIDENCE_MODES)}
    rows = conn.execute(
        """
        SELECT cost_evidence_mode, COUNT(*) AS count
        FROM cost_estimates
        GROUP BY cost_evidence_mode
        ORDER BY cost_evidence_mode
        """
    ).fetchall()
    for row in rows:
        counts[str(row["cost_evidence_mode"])] = int(row["count"])
    return counts


def _source_artifacts(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    return [
        {
            "source_kind": str(row["source_kind"]),
            "source_uri": str(row["source_uri"]),
            "source_hash": row["source_hash"],
            "content_contract": str(row["content_contract"]),
        }
        for row in conn.execute(
            """
            SELECT source_kind, source_uri, source_hash, content_contract
            FROM source_artifacts
            ORDER BY id
            """
        ).fetchall()
    ]


def sanitize_diagnostic_payload(value: dict[str, Any], strict: bool) -> dict[str, Any]:
    """Return the report-safe diagnostic subset from a persisted payload."""

    diagnostic = {field: value[field] for field in _DIAGNOSTIC_FIELDS if field in value}
    _check_enum(diagnostic.get("status"), OBSERVATION_STATUSES, "diagnostic.status", strict)
    _check_enum(diagnostic.get("content_contract"), CONTENT_CONTRACTS, "diagnostic.content_contract", strict)
    return diagnostic


def _diagnostics(conn: sqlite3.Connection, strict: bool) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT value_json
        FROM observations
        WHERE metric_id = ? AND status = ?
        ORDER BY id
        """,
        (_DIAGNOSTIC_METRIC, "malformed_source"),
    ).fetchall()
    return [sanitize_diagnostic_payload(_json_object(row["value_json"]), strict) for row in rows]


def _validate_migration_rows(conn: sqlite3.Connection, strict: bool) -> None:
    rows = conn.execute(
        """
        SELECT status, evidence_class, reliability_mode, content_contract, comparability, metric_id, value_json
        FROM observations
        ORDER BY id
        """
    ).fetchall()
    for row in rows:
        _validate_observation_row(row, strict)
        if str(row["metric_id"] or "").startswith(_USAGE_METRIC_PREFIX):
            _validate_usage_payload(_json_object(row["value_json"]), strict)

    rows = conn.execute(
        """
        SELECT status, evidence_class, reliability_mode, content_contract, comparability
        FROM rubric_observations
        ORDER BY id
        """
    ).fetchall()
    for row in rows:
        _validate_observation_row(row, strict)

    for row in conn.execute(
        """
        SELECT cost_evidence_mode, comparability
        FROM cost_estimates
        ORDER BY id
        """
    ).fetchall():
        _validate_cost_row(row, strict)


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
    diagnostics = [
        sanitize_diagnostic_payload(_json_object(row["value_json"]), strict)
        for row in diagnostic_rows
    ]
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


def query_migration_state(
    conn: sqlite3.Connection,
    *,
    strict: bool = True,
) -> dict[str, Any]:
    """Return small v0 compatibility migration counts without raw content."""

    _validate_migration_rows(conn, strict)
    diagnostics = _diagnostics(conn, strict)
    return {
        "v0_compatibility_status": "compatibility_active",
        "registry_hash": _NOT_COLLECTED,
        "source_set_hash": _NOT_COLLECTED,
        "counts": {
            "runs": _count_rows(conn, "runs"),
            "observations": _count_rows(conn, "observations"),
            "legacy_score_observations": _count_observations(conn, "metric_id = ?", (_LEGACY_SCORE_METRIC,)),
            "rubric_observations": _count_rows(conn, "rubric_observations"),
            "cost_estimates": _count_rows(conn, "cost_estimates"),
            "source_artifacts": _count_rows(conn, "source_artifacts"),
            "diagnostics": len(diagnostics),
        },
        "usage_observation_status_counts": _status_counts(
            conn,
            """
            SELECT status, COUNT(*) AS count
            FROM observations
            WHERE metric_id LIKE ?
            GROUP BY status
            ORDER BY status
            """,
            (f"{_USAGE_METRIC_PREFIX}%",),
        ),
        "usage_missingness_counts": _usage_missingness_counts(conn),
        "cost_evidence_mode_counts": _cost_evidence_mode_counts(conn),
        "source_artifacts": _source_artifacts(conn),
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

    fixture_ids = set(provenance.get("fixture_ids", []))
    source_artifact_ids_by_fixture = _gate_source_artifact_ids_by_fixture(
        conn,
        provenance,
        source_set_hash,
        strict,
    )
    all_gate_source_artifact_ids = {
        source_artifact_id
        for source_artifact_ids in source_artifact_ids_by_fixture.values()
        for source_artifact_id in source_artifact_ids
    }
    all_source_filter, all_source_args = _source_artifact_filter(all_gate_source_artifact_ids)
    manual_source_ids = source_artifact_ids_by_fixture.get("manual_run_with_rubric_dimensions", set())
    claude_source_ids = source_artifact_ids_by_fixture.get("claude_local_jsonl_minimal_structure", set())
    provider_source_ids = source_artifact_ids_by_fixture.get("provider_denominator_mismatch", set())
    manual_source_filter, manual_source_args = _source_artifact_filter(manual_source_ids)
    claude_source_filter, claude_source_args = _source_artifact_filter(claude_source_ids)
    provider_source_filter, provider_source_args = _source_artifact_filter(provider_source_ids)

    rubric_observations = _table_json_rows(
        conn,
        f"""
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
        WHERE {manual_source_filter}
        ORDER BY id
        """,
        manual_source_args,
    )

    runtime_response_items = _table_json_rows(
        conn,
        f"""
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
        WHERE {claude_source_filter}
        ORDER BY id
        """,
        claude_source_args,
    )

    diagnostics = _table_json_rows(
        conn,
        f"""
        SELECT value_json
        FROM observations
        WHERE status = ? AND {all_source_filter}
        ORDER BY id
        """,
        ("malformed_source", *all_source_args),
    )

    provider_usage: dict[str, dict[str, Any]] = {}
    rows = conn.execute(
        f"""
        SELECT value_json
        FROM observations
        WHERE entity_type = ? AND {provider_source_filter}
        ORDER BY id
        """,
        ("provider_usage", *provider_source_args),
    ).fetchall()
    for row in rows:
        value = _json_object(row["value_json"])
        provider = str(value.pop("provider"))
        axis = str(value.pop("axis"))
        provider_usage.setdefault(provider, {})[axis] = value

    counts = {
        "manual_run_with_rubric_dimensions.rubric_observations": _count_fixture_rows(
            conn,
            "rubric_observations",
            "manual_run_with_rubric_dimensions",
            manual_source_ids,
        ),
        "claude_local_jsonl_minimal_structure.runtime_items": _count_fixture_rows(
            conn,
            "runtime_response_items",
            "claude_local_jsonl_minimal_structure",
            claude_source_ids,
        ),
        "claude_local_jsonl_minimal_structure.diagnostics": _count_fixture_rows(
            conn,
            "observations",
            "claude_local_jsonl_minimal_structure",
            claude_source_ids,
            "status = 'malformed_source'",
        ),
        "provider_denominator_mismatch.provider_observations": _count_fixture_rows(
            conn,
            "observations",
            "provider_denominator_mismatch",
            provider_source_ids,
            "entity_type = 'provider_usage'",
        ),
    }
    gate_status, required_evidence = provider_neutrality_gate_status(fixture_ids, counts)
    return {
        "rebuild_id": int(rebuild["id"]),
        "schema_version": str(rebuild["schema_version"]),
        "registry_version": str(rebuild["registry_version"]),
        "registry_hash": actual_hash,
        "source_set_hash": source_set_hash,
        "status": str(rebuild["status"]),
        "provider_neutrality_gate": {
            "status": gate_status,
            "required_fixtures": sorted(PROVIDER_NEUTRALITY_REQUIRED_FIXTURES),
            "observed_fixtures": sorted(fixture_ids),
            "source_artifact_ids_by_fixture": {
                fixture_id: sorted(source_artifact_ids)
                for fixture_id, source_artifact_ids in sorted(source_artifact_ids_by_fixture.items())
            },
            "required_evidence": required_evidence,
        },
        "rubric_observations": rubric_observations,
        "runtime_response_items": runtime_response_items,
        "diagnostics": diagnostics,
        "provider_usage_evidence": provider_usage,
    }
