"""Write validated responsible-closure host-exercise packets."""

from __future__ import annotations

import copy
import json
import pathlib
from typing import Any

from harness_modifier.closure import host_exercise_packet
from harness_modifier.compatibility import declaration as compatibility_declaration


def host_exercise_packet_policy() -> dict[str, Any]:
    return host_exercise_packet.load_host_exercise_packet()


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _string_field(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} must be a non-empty string")
    return value


def _validate_string_list(value: Any, field_name: str) -> list[str]:
    if not isinstance(value, list):
        raise ValueError(f"{field_name} must be a list")
    normalized: list[str] = []
    seen: set[str] = set()
    for entry in value:
        if not isinstance(entry, str) or not entry.strip():
            raise ValueError(f"{field_name} entries must be non-empty strings")
        if entry in seen:
            raise ValueError(f"{field_name} entries must be unique")
        seen.add(entry)
        normalized.append(entry)
    return normalized


def _paths_overlap(left: pathlib.Path, right: pathlib.Path) -> bool:
    return left == right or left in right.parents or right in left.parents


def _apply_defaults(payload: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    normalized = copy.deepcopy(payload)
    compatibility = compatibility_declaration.load_declaration()

    normalized.setdefault("packet_version", policy["default_packet_version"])
    normalized.setdefault("bundle_family", policy["bundle_family"])
    normalized.setdefault("exercise_mode", policy["exercise_mode"])
    normalized.setdefault(
        "preflight_reads",
        policy["required_preflight_reads"] + policy["conditional_preflight_reads"],
    )
    normalized.setdefault("abort_conditions", policy["abort_condition_codes"])

    declaration_capture = normalized.setdefault("declaration_capture", {})
    declaration_capture.setdefault("declaration_posture", compatibility["compatibility_posture"])
    declaration_capture.setdefault("observed_basis_runtime", compatibility["runtime_basis"]["runtime"])
    held_annotations = compatibility.get("runtime_held_annotations", [])
    held_annotation_runtime = (
        held_annotations[0]["runtime"] if held_annotations else "not_available"
    )
    declaration_capture.setdefault("held_annotation_runtime", held_annotation_runtime)
    declaration_capture.setdefault(
        "compatibility_window_state",
        compatibility["upstream_compatibility_window"]["state"],
    )
    return normalized


def _validate_declaration_capture(payload: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    declaration_capture = payload.get("declaration_capture")
    if not isinstance(declaration_capture, dict):
        raise ValueError("declaration_capture must be an object")

    unexpected = sorted(set(declaration_capture) - set(policy["declaration_capture_fields"]))
    if unexpected:
        raise ValueError("unexpected declaration_capture fields: " + ", ".join(unexpected))

    for key in policy["declaration_capture_fields"]:
        if key not in declaration_capture:
            raise ValueError(f"missing declaration_capture field: {key}")

    for key in (
        "declaration_posture",
        "observed_basis_runtime",
        "held_annotation_runtime",
        "compatibility_window_state",
        "basis_commit",
    ):
        _string_field(declaration_capture, key)

    basis_commit = declaration_capture["basis_commit"].strip().lower()
    if basis_commit in {"unknown", "not_available"}:
        raise ValueError("declaration_capture.basis_commit must name a known basis commit")

    dirty_worktree = declaration_capture["dirty_worktree"]
    if not isinstance(dirty_worktree, bool):
        raise ValueError("declaration_capture.dirty_worktree must be a boolean")
    if dirty_worktree:
        raise ValueError("first host packet must require a clean worktree")

    return declaration_capture


def _validate_output_targets(payload: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    output_targets = payload.get("output_targets")
    if not isinstance(output_targets, dict):
        raise ValueError("output_targets must be an object")

    unexpected = sorted(set(output_targets) - set(policy["output_pointer_fields"]))
    if unexpected:
        raise ValueError("unexpected output_targets fields: " + ", ".join(unexpected))

    for key in policy["output_pointer_fields"]:
        if key not in output_targets:
            raise ValueError(f"missing output_targets field: {key}")
        _string_field(output_targets, key)
    return output_targets


def validate_host_exercise_packet(payload: dict[str, Any]) -> dict[str, Any]:
    policy = host_exercise_packet_policy()
    normalized = _apply_defaults(payload, policy)

    unexpected_top_level = sorted(
        set(normalized) - set(policy["required_top_level_fields"])
    )
    if unexpected_top_level:
        raise ValueError("unexpected top-level fields: " + ", ".join(unexpected_top_level))

    for key in policy["required_top_level_fields"]:
        if key not in normalized:
            raise ValueError(f"missing required field: {key}")

    for key in (
        "packet_id",
        "target_host_class",
        "host_reference",
        "host_repo_path",
        "runtime_class",
        "host_shape",
        "host_has_reflect_artifacts_rationale",
        "host_age_posture",
    ):
        _string_field(normalized, key)

    packet_version = normalized["packet_version"]
    if not isinstance(packet_version, int) or packet_version < 1:
        raise ValueError("packet_version must be an integer >= 1")

    if normalized["bundle_family"] != policy["bundle_family"]:
        raise ValueError(f"bundle_family must be {policy['bundle_family']!r}")
    if normalized["exercise_mode"] != policy["exercise_mode"]:
        raise ValueError(f"exercise_mode must be {policy['exercise_mode']!r}")
    if normalized["target_host_class"] not in set(policy["target_host_class_vocab"]):
        raise ValueError(
            f"target_host_class must be one of {sorted(policy['target_host_class_vocab'])}"
        )
    if normalized["runtime_class"] not in set(policy["runtime_class_vocab"]):
        raise ValueError(
            f"runtime_class must be one of {sorted(policy['runtime_class_vocab'])}"
        )
    if normalized["host_shape"] not in set(policy["host_shape_vocab"]):
        raise ValueError(f"host_shape must be one of {sorted(policy['host_shape_vocab'])}")
    if normalized["host_age_posture"] not in set(policy["host_age_posture_vocab"]):
        raise ValueError(
            f"host_age_posture must be one of {sorted(policy['host_age_posture_vocab'])}"
        )

    host_repo_path = pathlib.Path(normalized["host_repo_path"]).expanduser().resolve()
    if _paths_overlap(host_repo_path, REPO_ROOT):
        raise ValueError("first host packet must target a repo disjoint from prix-guesser")

    host_has_regular_gsd = normalized["host_has_regular_gsd"]
    if not isinstance(host_has_regular_gsd, bool):
        raise ValueError("host_has_regular_gsd must be a boolean")
    if not host_has_regular_gsd:
        raise ValueError("first host packet requires regular GSD to already be installed")

    host_has_reflect_artifacts = normalized["host_has_reflect_artifacts"]
    if not isinstance(host_has_reflect_artifacts, bool):
        raise ValueError("host_has_reflect_artifacts must be a boolean")
    if host_has_reflect_artifacts:
        raise ValueError("first host packet excludes hosts with Reflect artifacts")

    declaration_capture = _validate_declaration_capture(normalized, policy)

    preflight_reads = _validate_string_list(normalized["preflight_reads"], "preflight_reads")
    allowed_preflight_reads = set(policy["required_preflight_reads"]) | set(
        policy["conditional_preflight_reads"]
    )
    missing_required_reads = sorted(set(policy["required_preflight_reads"]) - set(preflight_reads))
    if missing_required_reads:
        raise ValueError("missing required preflight reads: " + ", ".join(missing_required_reads))
    unexpected_reads = sorted(set(preflight_reads) - allowed_preflight_reads)
    if unexpected_reads:
        raise ValueError("unexpected preflight reads: " + ", ".join(unexpected_reads))

    abort_conditions = _validate_string_list(normalized["abort_conditions"], "abort_conditions")
    expected_abort_conditions = set(policy["abort_condition_codes"])
    if set(abort_conditions) != expected_abort_conditions:
        raise ValueError(
            "abort_conditions must match "
            + ", ".join(sorted(policy["abort_condition_codes"]))
        )

    output_targets = _validate_output_targets(normalized, policy)

    normalized["declaration_capture"] = declaration_capture
    normalized["preflight_reads"] = preflight_reads
    normalized["abort_conditions"] = abort_conditions
    normalized["output_targets"] = output_targets
    return normalized


def render_host_exercise_packet(payload: dict[str, Any]) -> str:
    normalized = validate_host_exercise_packet(payload)
    return json.dumps(normalized, indent=2, sort_keys=True) + "\n"


def write_host_exercise_packet(output_path: pathlib.Path, payload: dict[str, Any]) -> dict[str, Any]:
    normalized = validate_host_exercise_packet(payload)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(normalized, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return normalized
