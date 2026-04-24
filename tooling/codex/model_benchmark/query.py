"""Small structured query helpers for model benchmark rebuild parity."""

from __future__ import annotations

import json
import sqlite3
from typing import Any


def _latest_rebuild(conn: sqlite3.Connection) -> sqlite3.Row:
    row = conn.execute(
        """
        SELECT id, schema_version, registry_version, registry_hash, source_set_hash, status
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
