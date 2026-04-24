"""Fixture-local rebuild helpers for the model benchmark SQLite cache."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Any

from tooling.codex.model_benchmark import manifest, store


HASH_ALGORITHM = "sha256"


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
