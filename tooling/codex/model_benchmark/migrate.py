"""Compatibility import from v0 benchmark run JSONL into the telemetry store."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from tooling.codex.model_benchmark import schema, store


SOURCE_KIND = "model-benchmark-run/v1-jsonl"
CONTENT_CONTRACT = "metadata_only"
TELEMETRY_FEATURE_FIELDS = tuple(schema.TELEMETRY_DEFAULTS)
RUBRIC_PROVENANCE_FIELDS = ("source", "content_contract", "derived_feature_version")
COST_ESTIMATE_FIELDS = (
    "estimate_status",
    "model",
    "currency",
    "source_url",
    "retrieved_at",
    "effective_date",
    "total_estimated_cost",
    "missing_token_fields",
    "missing_rate_fields",
    "caveat",
)
COST_LINE_ITEM_FIELDS = ("token_field", "tokens", "rate_per_million", "estimated_cost")


def _source_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()}"


def _diagnostic(line_number: int, exc: Exception) -> dict[str, Any]:
    if isinstance(exc, json.JSONDecodeError):
        error_type = "invalid_json"
        message = exc.msg
    else:
        error_type = "schema_validation_failed"
        message = str(exc).split(":", 1)[0]
    return {
        "line_number": line_number,
        "status": "malformed_source",
        "error_type": error_type,
        "message": message,
        "content_contract": CONTENT_CONTRACT,
        "evidence_class": "local_observed",
        "reliability_mode": "direct_field",
    }


def _empty_result(source_uri: str, source_hash: str) -> dict[str, Any]:
    return {
        "source_uri": source_uri,
        "source_hash": source_hash,
        "runs": 0,
        "observations": 0,
        "rubric_observations": 0,
        "legacy_score_observations": 0,
        "cost_estimates": 0,
        "skipped_records": 0,
        "diagnostic_count": 0,
        "diagnostics": [],
    }


def _source_artifact(conn: Any, path: Path, source_hash: str) -> int:
    return store.insert_source_artifact(
        conn,
        {
            "source_kind": SOURCE_KIND,
            "source_uri": str(path),
            "source_hash": source_hash,
            "content_contract": CONTENT_CONTRACT,
            "provenance_json": {
                "importer": "model_benchmark.migrate.import_v0_run_jsonl",
                "schema_version": schema.DEFAULT_SCHEMA_VERSION,
                "content_contract": CONTENT_CONTRACT,
            },
        },
    )


def _line_provenance(line_number: int, **extra: Any) -> dict[str, Any]:
    provenance = {
        "importer": "model_benchmark.migrate.import_v0_run_jsonl",
        "source_schema_version": schema.DEFAULT_SCHEMA_VERSION,
        "line_number": line_number,
        "content_contract": CONTENT_CONTRACT,
    }
    provenance.update(extra)
    return provenance


def _safe_scalar(value: Any) -> Any:
    if isinstance(value, (str, int, float)) or value is None:
        return value
    if isinstance(value, bool):
        return value
    return "redacted"


def _allowlist_mapping(raw: Any, allowed_fields: tuple[str, ...]) -> dict[str, Any]:
    if not isinstance(raw, dict):
        return {}
    return {
        field: _safe_scalar(raw[field])
        for field in allowed_fields
        if field in raw
    }


def _sanitized_telemetry_features(features: dict[str, Any]) -> dict[str, Any]:
    return _allowlist_mapping(features, TELEMETRY_FEATURE_FIELDS)


def _sanitized_rubric_provenance(provenance: dict[str, Any]) -> dict[str, Any]:
    return _allowlist_mapping(provenance, RUBRIC_PROVENANCE_FIELDS)


def _sanitized_cost_estimate(cost_estimate: dict[str, Any]) -> dict[str, Any]:
    sanitized = _allowlist_mapping(cost_estimate, COST_ESTIMATE_FIELDS)
    line_items = cost_estimate.get("line_items")
    if isinstance(line_items, list):
        sanitized["line_items"] = [
            _allowlist_mapping(item, COST_LINE_ITEM_FIELDS)
            for item in line_items
            if isinstance(item, dict)
        ]
    return sanitized


def _persist_diagnostic_observation(
    conn: Any,
    diagnostic: dict[str, Any],
    source_artifact_id: int,
) -> None:
    store.insert_observation(
        conn,
        {
            "entity_type": "source_artifact",
            "entity_id": str(source_artifact_id),
            "metric_id": "source.parse_status",
            "status": "malformed_source",
            "evidence_class": "local_observed",
            "reliability_mode": "direct_field",
            "content_contract": CONTENT_CONTRACT,
            "comparability": "not_comparable",
            "source_artifact_id": source_artifact_id,
            "value_json": {
                "status": "malformed_source",
                "line_number": diagnostic["line_number"],
                "error_type": diagnostic["error_type"],
                "content_contract": CONTENT_CONTRACT,
            },
            "provenance_json": _line_provenance(
                diagnostic["line_number"],
                diagnostic="malformed_source",
            ),
        },
    )


def _usage_observation(
    conn: Any,
    run: dict[str, Any],
    field: str,
    source_artifact_id: int,
    line_number: int,
) -> int:
    value = run["usage"][field]
    status = run["usage"]["usage_metric_status"] if isinstance(value, int) else str(value)
    availability_status = status
    return store.insert_observation(
        conn,
        {
            "entity_type": "run",
            "entity_id": run["run_id"],
            "metric_id": f"usage.{field}",
            "status": status,
            "evidence_class": "local_observed",
            "reliability_mode": "direct_field",
            "content_contract": CONTENT_CONTRACT,
            "comparability": "comparable_with_caveat",
            "source_artifact_id": source_artifact_id,
            "value_json": {
                "value": value,
                "availability_status": availability_status,
                "missingness": status if not isinstance(value, int) else "not_applicable",
                "token_field": field,
            },
            "provenance_json": _line_provenance(line_number),
        },
    )


def _legacy_score_observation(conn: Any, run: dict[str, Any], source_artifact_id: int, line_number: int) -> int:
    legacy_score = run.get("legacy_score")
    if legacy_score is None:
        return 0
    store.insert_observation(
        conn,
        {
            "entity_type": "run",
            "entity_id": run["run_id"],
            "metric_id": "legacy.score.overall",
            "status": "measured",
            "evidence_class": "local_observed",
            "reliability_mode": "manual_label",
            "content_contract": CONTENT_CONTRACT,
            "comparability": "not_comparable",
            "source_artifact_id": source_artifact_id,
            "value_json": {
                "value": legacy_score["overall"],
                "compatibility": "compatibility_only",
                "warning": legacy_score["warning"],
            },
            "provenance_json": _line_provenance(line_number, compatibility="compatibility_only"),
        },
    )
    return 1


def _rubric_observations(conn: Any, run: dict[str, Any], source_artifact_id: int, line_number: int) -> int:
    count = 0
    for observation in run.get("rubric_observations", []):
        store.insert_rubric_observation(
            conn,
            {
                "entity_type": "run",
                "entity_id": run["run_id"],
                "rubric_id": observation["rubric_id"],
                "dimension_id": observation["dimension_id"],
                "status": observation["status"],
                "evidence_class": observation["evidence_class"],
                "reliability_mode": observation["reliability_mode"],
                "content_contract": observation["content_contract"],
                "comparability": observation.get("comparability"),
                "source_artifact_id": source_artifact_id,
                "value_json": {"value": observation["value"]},
                "provenance_json": _line_provenance(
                    line_number,
                    evaluator_id=observation["evaluator_id"],
                    rubric_version=observation["rubric_version"],
                    rubric_provenance=_sanitized_rubric_provenance(observation["provenance"]),
                ),
            },
        )
        count += 1
    return count


def _cost_estimate(conn: Any, run: dict[str, Any], source_artifact_id: int, line_number: int) -> int:
    cost_estimate = run.get("cost_estimate")
    if not isinstance(cost_estimate, dict):
        return 0
    store.insert_cost_estimate(
        conn,
        {
            "run_id": run["run_id"],
            "source_artifact_id": source_artifact_id,
            "cost_evidence_mode": "api_equivalent_estimate",
            "comparability": "comparable_with_caveat",
            "cost_json": _sanitized_cost_estimate(cost_estimate),
            "provenance_json": _line_provenance(
                line_number,
                cost_evidence_mode="api_equivalent_estimate",
                warning="API-equivalent estimate only; not provider-reported cost.",
            ),
        },
    )
    return 1


def _insert_run(conn: Any, run: dict[str, Any], source_artifact_id: int, line_number: int) -> None:
    store.insert_run(
        conn,
        {
            "run_id": run["run_id"],
            "candidate_profile": run["candidate_profile"],
            "model": run["model"],
            "reasoning_effort": run["reasoning_effort"],
            "status": run["status"],
            "run_json": {
                "schema_version": run["schema_version"],
                "task_id": run["task_id"],
                "runtime_provider": run["runtime_provider"],
                "effective_model": run["effective_model"],
                "effective_reasoning_effort": run["effective_reasoning_effort"],
                "qualitative_only": run["qualitative_only"],
                "profile_consistency_status": run["profile_consistency_status"],
                "telemetry_features": _sanitized_telemetry_features(run["telemetry_features"]),
            },
            "source_artifact_id": source_artifact_id,
            "provenance_json": _line_provenance(line_number),
        },
    )


def _import_record(conn: Any, run: dict[str, Any], source_artifact_id: int, line_number: int) -> dict[str, int]:
    _insert_run(conn, run, source_artifact_id, line_number)
    observation_count = 0
    for field in schema.TOKEN_FIELDS:
        _usage_observation(conn, run, field, source_artifact_id, line_number)
        observation_count += 1
    legacy_count = _legacy_score_observation(conn, run, source_artifact_id, line_number)
    observation_count += legacy_count
    return {
        "runs": 1,
        "observations": observation_count,
        "rubric_observations": _rubric_observations(conn, run, source_artifact_id, line_number),
        "legacy_score_observations": legacy_count,
        "cost_estimates": _cost_estimate(conn, run, source_artifact_id, line_number),
    }


def import_v0_run_jsonl(conn: Any, path: str | Path) -> dict[str, Any]:
    """Import model-benchmark-run/v1 JSONL records into a rebuildable SQLite store."""

    path_obj = Path(path)
    source_hash = _source_hash(path_obj)
    source_artifact_id = _source_artifact(conn, path_obj, source_hash)
    result = _empty_result(str(path_obj), source_hash)

    with path_obj.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                raw_record = json.loads(line)
                run = schema.validate_run_record(raw_record)
            except (json.JSONDecodeError, ValueError) as exc:
                diagnostic = _diagnostic(line_number, exc)
                result["skipped_records"] += 1
                result["diagnostics"].append(diagnostic)
                _persist_diagnostic_observation(conn, diagnostic, source_artifact_id)
                result["observations"] += 1
                continue
            counts = _import_record(conn, run, source_artifact_id, line_number)
            for key, value in counts.items():
                result[key] += value

    result["diagnostic_count"] = len(result["diagnostics"])
    return result
