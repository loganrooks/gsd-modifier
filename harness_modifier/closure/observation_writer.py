"""Write validated responsible-closure observation records."""

from __future__ import annotations

import copy
import json
import pathlib
from typing import Any

from harness_modifier.closure import observation_record


def observation_record_policy() -> dict[str, Any]:
    return observation_record.load_observation_record()


def _required_top_level_fields() -> tuple[str, ...]:
    policy = observation_record_policy()
    return tuple(policy["required_top_level_fields"])


def _string_field(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} must be a non-empty string")
    return value


def _validate_list_of_dicts(payload: dict[str, Any], key: str) -> list[dict[str, Any]]:
    value = payload.get(key)
    if not isinstance(value, list):
        raise ValueError(f"{key} must be a list")
    for entry in value:
        if not isinstance(entry, dict):
            raise ValueError(f"{key} entries must be objects")
    return value


def _validate_row_subtypes(rows: list[dict[str, Any]], allowed: set[str], field_name: str) -> None:
    for entry in rows:
        subtype = entry.get("signal_subtype")
        if not isinstance(subtype, str) or subtype not in allowed:
            raise ValueError(f"{field_name} signal_subtype must be one of {sorted(allowed)}")


def _validate_expectation_rows(rows: list[dict[str, Any]], policy: dict[str, Any]) -> None:
    allowed_outcomes = set(policy["check_outcome_vocab"])
    allowed_skip_reasons = set(policy["automation_skip_reasons"])
    for entry in rows:
        check_outcome = entry.get("check_outcome")
        if check_outcome is not None and check_outcome not in allowed_outcomes:
            raise ValueError(f"check_outcome must be one of {sorted(allowed_outcomes)}")
        skip_reason = entry.get("skip_reason")
        if skip_reason is not None and skip_reason not in allowed_skip_reasons:
            raise ValueError(f"skip_reason must be one of {sorted(allowed_skip_reasons)}")


def _validate_measurement_provenance(payload: dict[str, Any], policy: dict[str, Any]) -> None:
    provenance = payload.get("measurement_provenance")
    if not isinstance(provenance, dict):
        raise ValueError("measurement_provenance must be an object")
    for key in policy["measurement_provenance_keys"]:
        value = provenance.get(key)
        if value == "not_available":
            continue
        if not isinstance(value, dict):
            raise ValueError(f"measurement_provenance.{key} must be an object or 'not_available'")


def _apply_defaults(payload: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    normalized = copy.deepcopy(payload)
    normalized.setdefault("carrier_version", policy["default_carrier_version"])
    normalized.setdefault("provenance_schema", policy["default_provenance_schema"])
    normalized.setdefault("status", policy["default_status"])
    normalized.setdefault("automation_level", policy["initial_automation_level"])
    normalized.setdefault("bundle_family", policy["bundle_family"])
    return normalized


def validate_observation_record(payload: dict[str, Any]) -> dict[str, Any]:
    policy = observation_record_policy()
    normalized = _apply_defaults(payload, policy)
    allowed_top_level_fields = set(policy["required_top_level_fields"]) | set(policy["optional_fields"])

    unexpected_fields = sorted(set(normalized) - allowed_top_level_fields)
    if unexpected_fields:
        raise ValueError(
            "unexpected top-level fields: " + ", ".join(unexpected_fields)
        )

    for key in _required_top_level_fields():
        if key not in normalized:
            raise ValueError(f"missing required field: {key}")

    for key in (
        "observation_id",
        "provenance_schema",
        "status",
        "observed_at",
        "basis_commit",
        "bundle_family",
        "exercise_id",
        "target_host_class",
        "evidence_family",
        "disposition",
    ):
        _string_field(normalized, key)

    carrier_version = normalized["carrier_version"]
    if not isinstance(carrier_version, int) or carrier_version < 1:
        raise ValueError("carrier_version must be an integer >= 1")

    automation_level = normalized["automation_level"]
    if not isinstance(automation_level, int) or automation_level < 1:
        raise ValueError("automation_level must be an integer >= 1")

    if normalized["provenance_schema"] != policy["default_provenance_schema"]:
        raise ValueError(
            f"provenance_schema must be {policy['default_provenance_schema']!r} for the first slice"
        )
    if normalized["bundle_family"] != policy["bundle_family"]:
        raise ValueError(f"bundle_family must be {policy['bundle_family']!r}")
    if normalized["status"] not in set(policy["status_vocab"]):
        raise ValueError(f"status must be one of {sorted(policy['status_vocab'])}")
    if normalized["evidence_family"] not in set(policy["evidence_family_vocab"]):
        raise ValueError(f"evidence_family must be one of {sorted(policy['evidence_family_vocab'])}")
    if normalized["disposition"] not in set(policy["disposition_vocab"]):
        raise ValueError(f"disposition must be one of {sorted(policy['disposition_vocab'])}")

    if "narrative_summary" in normalized:
        _string_field(normalized, "narrative_summary")

    deployment_rows = _validate_list_of_dicts(normalized, "deployment_context")
    expectation_rows = _validate_list_of_dicts(normalized, "expectation_vs_observation")
    semantic_rows = _validate_list_of_dicts(normalized, "semantic_deviation")
    positive_rows = _validate_list_of_dicts(normalized, "positive_gain")
    _validate_measurement_provenance(normalized, policy)

    # The first slice still expects these carrier families to exist even if a given run
    # has no entries yet.
    _validate_row_subtypes(
        semantic_rows,
        set(policy["semantic_deviation_subtypes"]),
        "semantic_deviation",
    )
    _validate_row_subtypes(
        positive_rows,
        set(policy["positive_gain_subtypes"]),
        "positive_gain",
    )
    _validate_expectation_rows(expectation_rows, policy)

    for key in policy["signal_family_keys"]:
        if key == "measurement_provenance":
            continue
        if key not in normalized:
            raise ValueError(f"missing signal family: {key}")

    # Preserve row families as lists even when currently empty.
    normalized["deployment_context"] = deployment_rows
    normalized["expectation_vs_observation"] = expectation_rows
    normalized["semantic_deviation"] = semantic_rows
    normalized["positive_gain"] = positive_rows
    return normalized


def render_observation_record(payload: dict[str, Any]) -> str:
    normalized = validate_observation_record(payload)
    return json.dumps(normalized, indent=2, sort_keys=True) + "\n"


def write_observation_record(output_path: pathlib.Path, payload: dict[str, Any]) -> dict[str, Any]:
    normalized = validate_observation_record(payload)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(normalized, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return normalized
