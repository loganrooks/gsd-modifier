"""Static YAML manifest validation for model benchmark telemetry registries."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

import yaml

from tooling.codex.model_benchmark.enums import (
    COMPARABILITY_VALUES,
    CONTENT_CONTRACTS,
    COST_EVIDENCE_MODES,
    EVIDENCE_CLASSES,
    OBSERVATION_STATUSES,
    RAW_CONTENT_CONTRACTS,
    RELIABILITY_MODES,
)


SCHEMA_VERSION = "telemetry-plugin-manifest/v1"
HASH_ALGORITHM = "sha256"
_HASH_FIELD = "registry_hash"
_LIST_SECTIONS = ("source_kinds", "namespaces", "predicates", "metrics", "rubrics", "emits")


def _require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    return value


def _require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{label} must be a list")
    return value


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def _ids_for(section: list[Any], section_name: str) -> set[str]:
    ids: set[str] = set()
    for index, raw_item in enumerate(section, start=1):
        item = _require_object(raw_item, f"{section_name}[{index}]")
        item_id = _require_string(item.get("id"), f"{section_name}[{index}].id")
        if item_id in ids:
            raise ValueError(f"duplicate {section_name} id: {item_id}")
        ids.add(item_id)
    return ids


def _require_enum(item: dict[str, Any], field: str, allowed: frozenset[str], label: str) -> str:
    value = _require_string(item.get(field), f"{label}.{field}")
    if value not in allowed:
        raise ValueError(f"{label}.{field} must be one of {sorted(allowed)}")
    return value


def _validate_raw_content_policy(item: dict[str, Any], label: str) -> None:
    content_contract = item.get("content_contract")
    if content_contract not in RAW_CONTENT_CONTRACTS:
        return
    if item.get("raw_content_consent") is not True or not item.get("retention_policy"):
        raise ValueError(f"{label} raw content contracts require explicit consent and retention_policy")


def _normalize_dimension_ids(raw_dimensions: Any, label: str) -> list[dict[str, Any]]:
    dimensions = _require_list(raw_dimensions, f"{label}.dimensions")
    seen: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for index, raw_dimension in enumerate(dimensions, start=1):
        dimension = dict(_require_object(raw_dimension, f"{label}.dimensions[{index}]"))
        dimension_id = _require_string(dimension.get("id"), f"{label}.dimensions[{index}].id")
        if dimension_id in seen:
            raise ValueError(f"duplicate {label}.dimensions id: {dimension_id}")
        seen.add(dimension_id)
        dimension["id"] = dimension_id
        normalized.append(dimension)
    return normalized


def _normalize_manifest(raw_manifest: dict[str, Any]) -> dict[str, Any]:
    manifest = copy.deepcopy(_require_object(raw_manifest, "manifest"))
    schema_version = _require_string(manifest.get("schema_version"), "schema_version")
    if schema_version != SCHEMA_VERSION:
        raise ValueError(f"schema_version must be {SCHEMA_VERSION}")

    normalized: dict[str, Any] = {
        "schema_version": schema_version,
        "registry_id": _require_string(manifest.get("registry_id"), "registry_id"),
        "registry_version": _require_string(manifest.get("registry_version"), "registry_version"),
    }

    for section_name in _LIST_SECTIONS:
        normalized[section_name] = _require_list(manifest.get(section_name), section_name)

    source_kind_ids = _ids_for(normalized["source_kinds"], "source_kinds")
    namespace_ids = _ids_for(normalized["namespaces"], "namespaces")
    predicate_ids = _ids_for(normalized["predicates"], "predicates")
    metric_ids = _ids_for(normalized["metrics"], "metrics")
    rubric_ids = _ids_for(normalized["rubrics"], "rubrics")

    for index, metric in enumerate(normalized["metrics"], start=1):
        label = f"metrics[{index}]"
        _require_enum(metric, "status", OBSERVATION_STATUSES, label)
        _require_enum(metric, "evidence_class", EVIDENCE_CLASSES, label)
        _require_enum(metric, "reliability_mode", RELIABILITY_MODES, label)
        _require_enum(metric, "content_contract", CONTENT_CONTRACTS, label)
        _require_enum(metric, "cost_evidence_mode", COST_EVIDENCE_MODES, label)
        _require_enum(metric, "comparability", COMPARABILITY_VALUES, label)
        _validate_raw_content_policy(metric, label)

    for index, rubric in enumerate(normalized["rubrics"], start=1):
        rubric["dimensions"] = _normalize_dimension_ids(rubric.get("dimensions"), f"rubrics[{index}]")

    for index, emission in enumerate(normalized["emits"], start=1):
        label = f"emits[{index}]"
        emission = _require_object(emission, label)
        source_kind = _require_string(emission.get("source_kind"), f"{label}.source_kind")
        if source_kind not in source_kind_ids:
            raise ValueError(f"{label} undeclared source_kind: {source_kind}")
        namespace = _require_string(emission.get("namespace"), f"{label}.namespace")
        if namespace not in namespace_ids:
            raise ValueError(f"{label} undeclared namespace: {namespace}")
        predicate = _require_string(emission.get("predicate"), f"{label}.predicate")
        if predicate not in predicate_ids:
            raise ValueError(f"{label} undeclared predicate: {predicate}")
        metric_id = emission.get("metric_id")
        if metric_id is not None:
            metric_id = _require_string(metric_id, f"{label}.metric_id")
            if metric_id not in metric_ids:
                raise ValueError(f"{label} undeclared metric_id: {metric_id}")
        rubric_id = emission.get("rubric_id")
        if rubric_id is not None:
            rubric_id = _require_string(rubric_id, f"{label}.rubric_id")
            if rubric_id not in rubric_ids:
                raise ValueError(f"{label} undeclared rubric_id: {rubric_id}")
        _require_enum(emission, "status", OBSERVATION_STATUSES, label)
        _require_enum(emission, "reliability_mode", RELIABILITY_MODES, label)
        _require_enum(emission, "content_contract", CONTENT_CONTRACTS, label)
        _validate_raw_content_policy(emission, label)

    return normalized


def validate_manifest(raw_manifest: dict[str, Any]) -> dict[str, Any]:
    """Validate a loaded manifest object and attach its registry hash."""

    normalized = _normalize_manifest(raw_manifest)
    normalized[_HASH_FIELD] = registry_hash(normalized)
    return normalized


def load_manifest(path: str | Path) -> dict[str, Any]:
    """Load and validate a static YAML telemetry plugin manifest."""

    path_obj = Path(path)
    with path_obj.open("r", encoding="utf-8") as handle:
        try:
            loaded = yaml.safe_load(handle)
        except yaml.YAMLError as exc:
            raise ValueError(f"{path_obj}: invalid YAML: {exc}") from exc
    return validate_manifest(loaded)


def canonical_json(manifest: dict[str, Any]) -> str:
    """Return deterministic canonical JSON for registry hashing/storage."""

    payload = copy.deepcopy(_require_object(manifest, "manifest"))
    payload.pop(_HASH_FIELD, None)
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def canonical_json_bytes(manifest: dict[str, Any]) -> bytes:
    return canonical_json(manifest).encode("utf-8")


def registry_hash(manifest: dict[str, Any]) -> str:
    digest = hashlib.sha256(canonical_json_bytes(manifest)).hexdigest()
    return f"{HASH_ALGORITHM}:{digest}"
