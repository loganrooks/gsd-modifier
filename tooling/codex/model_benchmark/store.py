"""SQLite cache skeleton for model benchmark telemetry.

Raw artifacts remain the durable evidence. This store is a rebuildable query
cache over normalized entities, observations, registry metadata, and provenance.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
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


SCHEMA_VERSION = "model-benchmark-store/v1"


_DDL = (
    """
    CREATE TABLE IF NOT EXISTS store_metadata (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS source_artifacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_kind TEXT NOT NULL,
        source_uri TEXT NOT NULL,
        source_hash TEXT,
        content_contract TEXT NOT NULL,
        provenance_json TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS task_definitions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id TEXT NOT NULL UNIQUE,
        task_json TEXT NOT NULL,
        source_artifact_id INTEGER,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS task_instances (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_instance_id TEXT NOT NULL UNIQUE,
        task_definition_id INTEGER,
        instance_json TEXT NOT NULL,
        source_artifact_id INTEGER,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (task_definition_id) REFERENCES task_definitions(id),
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_id TEXT NOT NULL UNIQUE,
        task_instance_id INTEGER,
        candidate_profile TEXT,
        model TEXT,
        reasoning_effort TEXT,
        status TEXT,
        run_json TEXT NOT NULL,
        source_artifact_id INTEGER,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (task_instance_id) REFERENCES task_instances(id),
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL,
        run_id INTEGER,
        provider_namespace TEXT NOT NULL,
        runtime_namespace TEXT NOT NULL,
        session_json TEXT NOT NULL,
        source_artifact_id INTEGER,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (run_id) REFERENCES runs(id),
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS turns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        turn_id TEXT NOT NULL,
        session_id INTEGER,
        turn_index INTEGER,
        turn_json TEXT NOT NULL,
        source_artifact_id INTEGER,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (session_id) REFERENCES sessions(id),
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS model_calls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        call_id TEXT,
        session_id INTEGER,
        turn_id INTEGER,
        provider_namespace TEXT NOT NULL,
        runtime_namespace TEXT NOT NULL,
        model TEXT,
        status TEXT,
        payload_json TEXT NOT NULL,
        source_artifact_id INTEGER,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (session_id) REFERENCES sessions(id),
        FOREIGN KEY (turn_id) REFERENCES turns(id),
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS runtime_response_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER,
        turn_id INTEGER,
        model_call_id INTEGER,
        source_artifact_id INTEGER NOT NULL,
        source_kind TEXT NOT NULL,
        provider_namespace TEXT NOT NULL,
        runtime_namespace TEXT NOT NULL,
        item_type TEXT NOT NULL,
        status TEXT,
        role TEXT,
        redaction_state TEXT NOT NULL,
        content_state TEXT NOT NULL,
        correlation_status TEXT NOT NULL,
        payload_json TEXT NOT NULL,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (session_id) REFERENCES sessions(id),
        FOREIGN KEY (turn_id) REFERENCES turns(id),
        FOREIGN KEY (model_call_id) REFERENCES model_calls(id),
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS tool_calls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tool_call_id TEXT,
        session_id INTEGER,
        turn_id INTEGER,
        runtime_item_id INTEGER,
        tool_namespace TEXT,
        tool_name TEXT,
        status TEXT,
        payload_json TEXT NOT NULL,
        source_artifact_id INTEGER,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (session_id) REFERENCES sessions(id),
        FOREIGN KEY (turn_id) REFERENCES turns(id),
        FOREIGN KEY (runtime_item_id) REFERENCES runtime_response_items(id),
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS entity_edges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_entity_type TEXT NOT NULL,
        source_entity_id TEXT NOT NULL,
        predicate TEXT NOT NULL,
        target_entity_type TEXT NOT NULL,
        target_entity_id TEXT NOT NULL,
        source_artifact_id INTEGER,
        payload_json TEXT NOT NULL,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS observations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_type TEXT NOT NULL,
        entity_id TEXT NOT NULL,
        metric_id TEXT,
        status TEXT NOT NULL,
        evidence_class TEXT NOT NULL,
        reliability_mode TEXT NOT NULL,
        content_contract TEXT NOT NULL,
        comparability TEXT,
        source_artifact_id INTEGER NOT NULL,
        value_json TEXT NOT NULL,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS rubric_observations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_type TEXT NOT NULL,
        entity_id TEXT NOT NULL,
        rubric_id TEXT NOT NULL,
        dimension_id TEXT NOT NULL,
        status TEXT NOT NULL,
        evidence_class TEXT NOT NULL,
        reliability_mode TEXT NOT NULL,
        content_contract TEXT NOT NULL,
        comparability TEXT,
        source_artifact_id INTEGER NOT NULL,
        value_json TEXT NOT NULL,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS cost_estimates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_id TEXT NOT NULL,
        source_artifact_id INTEGER NOT NULL,
        cost_evidence_mode TEXT NOT NULL,
        comparability TEXT,
        cost_json TEXT NOT NULL,
        provenance_json TEXT NOT NULL,
        FOREIGN KEY (source_artifact_id) REFERENCES source_artifacts(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS registries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        registry_id TEXT NOT NULL,
        registry_version TEXT NOT NULL,
        registry_hash TEXT NOT NULL UNIQUE,
        canonical_json TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS rebuild_runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        schema_version TEXT NOT NULL,
        registry_version TEXT NOT NULL,
        registry_hash TEXT NOT NULL,
        source_set_hash TEXT NOT NULL,
        status TEXT NOT NULL,
        started_at TEXT DEFAULT CURRENT_TIMESTAMP,
        completed_at TEXT,
        provenance_json TEXT NOT NULL
    )
    """,
)


def connect(path: str | Path) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    initialize(conn)
    return conn


def initialize(conn: sqlite3.Connection) -> None:
    conn.execute("PRAGMA foreign_keys = ON")
    for statement in _DDL:
        conn.execute(statement)
    conn.execute(
        "INSERT OR REPLACE INTO store_metadata(key, value) VALUES (?, ?)",
        ("schema_version", SCHEMA_VERSION),
    )
    conn.commit()


def schema_version(conn: sqlite3.Connection) -> str:
    row = conn.execute("SELECT value FROM store_metadata WHERE key = ?", ("schema_version",)).fetchone()
    if row is None:
        raise ValueError("schema_version is not recorded")
    return str(row["value"])


def _require(row: dict[str, Any], field: str) -> Any:
    value = row.get(field)
    if value is None:
        raise ValueError(f"{field} is required")
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{field} is required")
    return value


def _require_json(value: Any, field: str) -> str:
    _require({field: value}, field)
    if isinstance(value, str):
        try:
            json.loads(value)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{field} must be JSON text or a JSON-serializable value") from exc
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def _check_enum(value: str | None, allowed: frozenset[str], field: str, strict: bool) -> None:
    if value is None:
        return
    if strict and value not in allowed:
        raise ValueError(f"{field} must be one of {sorted(allowed)}")


def insert_source_artifact(conn: sqlite3.Connection, row: dict[str, Any], strict: bool = True) -> int:
    _check_enum(str(_require(row, "content_contract")), CONTENT_CONTRACTS, "content_contract", strict)
    cursor = conn.execute(
        """
        INSERT INTO source_artifacts(source_kind, source_uri, source_hash, content_contract, provenance_json)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            _require(row, "source_kind"),
            _require(row, "source_uri"),
            row.get("source_hash"),
            _require(row, "content_contract"),
            _require_json(row.get("provenance_json"), "provenance_json"),
        ),
    )
    conn.commit()
    return int(cursor.lastrowid)


def insert_runtime_response_item(conn: sqlite3.Connection, row: dict[str, Any], strict: bool = True) -> int:
    for field in (
        "source_kind",
        "provider_namespace",
        "runtime_namespace",
        "item_type",
        "redaction_state",
        "content_state",
        "source_artifact_id",
        "payload_json",
        "provenance_json",
        "correlation_status",
    ):
        _require(row, field)
    if row.get("status") is None and row.get("role") is None:
        raise ValueError("status or role is required")
    _check_enum(str(row["correlation_status"]), RUNTIME_ITEM_CORRELATION_STATUSES, "correlation_status", strict)
    cursor = conn.execute(
        """
        INSERT INTO runtime_response_items(
            session_id,
            turn_id,
            model_call_id,
            source_artifact_id,
            source_kind,
            provider_namespace,
            runtime_namespace,
            item_type,
            status,
            role,
            redaction_state,
            content_state,
            correlation_status,
            payload_json,
            provenance_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            row.get("session_id"),
            row.get("turn_id"),
            row.get("model_call_id"),
            row["source_artifact_id"],
            row["source_kind"],
            row["provider_namespace"],
            row["runtime_namespace"],
            row["item_type"],
            row.get("status"),
            row.get("role"),
            row["redaction_state"],
            row["content_state"],
            row["correlation_status"],
            _require_json(row.get("payload_json"), "payload_json"),
            _require_json(row.get("provenance_json"), "provenance_json"),
        ),
    )
    conn.commit()
    return int(cursor.lastrowid)


def _validate_observation_enums(row: dict[str, Any], strict: bool) -> None:
    _check_enum(str(row["status"]), OBSERVATION_STATUSES, "status", strict)
    _check_enum(str(row["evidence_class"]), EVIDENCE_CLASSES, "evidence_class", strict)
    _check_enum(str(row["reliability_mode"]), RELIABILITY_MODES, "reliability_mode", strict)
    _check_enum(str(row["content_contract"]), CONTENT_CONTRACTS, "content_contract", strict)
    _check_enum(row.get("comparability"), COMPARABILITY_VALUES, "comparability", strict)


def insert_observation(conn: sqlite3.Connection, row: dict[str, Any], strict: bool = True) -> int:
    for field in (
        "entity_type",
        "entity_id",
        "status",
        "evidence_class",
        "reliability_mode",
        "content_contract",
        "source_artifact_id",
        "value_json",
        "provenance_json",
    ):
        _require(row, field)
    _validate_observation_enums(row, strict)
    cursor = conn.execute(
        """
        INSERT INTO observations(
            entity_type,
            entity_id,
            metric_id,
            status,
            evidence_class,
            reliability_mode,
            content_contract,
            comparability,
            source_artifact_id,
            value_json,
            provenance_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            row["entity_type"],
            row["entity_id"],
            row.get("metric_id"),
            row["status"],
            row["evidence_class"],
            row["reliability_mode"],
            row["content_contract"],
            row.get("comparability"),
            row["source_artifact_id"],
            _require_json(row.get("value_json"), "value_json"),
            _require_json(row.get("provenance_json"), "provenance_json"),
        ),
    )
    conn.commit()
    return int(cursor.lastrowid)


def insert_cost_estimate(conn: sqlite3.Connection, row: dict[str, Any], strict: bool = True) -> int:
    for field in ("run_id", "source_artifact_id", "cost_evidence_mode", "cost_json", "provenance_json"):
        _require(row, field)
    _check_enum(str(row["cost_evidence_mode"]), COST_EVIDENCE_MODES, "cost_evidence_mode", strict)
    _check_enum(row.get("comparability"), COMPARABILITY_VALUES, "comparability", strict)
    cursor = conn.execute(
        """
        INSERT INTO cost_estimates(
            run_id,
            source_artifact_id,
            cost_evidence_mode,
            comparability,
            cost_json,
            provenance_json
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            row["run_id"],
            row["source_artifact_id"],
            row["cost_evidence_mode"],
            row.get("comparability"),
            _require_json(row.get("cost_json"), "cost_json"),
            _require_json(row.get("provenance_json"), "provenance_json"),
        ),
    )
    conn.commit()
    return int(cursor.lastrowid)


def insert_registry(conn: sqlite3.Connection, row: dict[str, Any]) -> int:
    for field in ("registry_id", "registry_version", "registry_hash", "canonical_json"):
        _require(row, field)
    cursor = conn.execute(
        """
        INSERT INTO registries(registry_id, registry_version, registry_hash, canonical_json)
        VALUES (?, ?, ?, ?)
        """,
        (
            row["registry_id"],
            row["registry_version"],
            row["registry_hash"],
            _require_json(row.get("canonical_json"), "canonical_json"),
        ),
    )
    conn.commit()
    return int(cursor.lastrowid)


def insert_rebuild_run(conn: sqlite3.Connection, row: dict[str, Any]) -> int:
    for field in (
        "schema_version",
        "registry_version",
        "registry_hash",
        "source_set_hash",
        "status",
        "provenance_json",
    ):
        _require(row, field)
    cursor = conn.execute(
        """
        INSERT INTO rebuild_runs(
            schema_version,
            registry_version,
            registry_hash,
            source_set_hash,
            status,
            completed_at,
            provenance_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            row["schema_version"],
            row["registry_version"],
            row["registry_hash"],
            row["source_set_hash"],
            row["status"],
            row.get("completed_at"),
            _require_json(row.get("provenance_json"), "provenance_json"),
        ),
    )
    conn.commit()
    return int(cursor.lastrowid)
