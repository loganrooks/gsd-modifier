"""Inject-mode operation kinds and validators for OVERLAY-MANIFEST.json schema v4.

Per ADR-001 (.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md):

- 7 operation kinds form the v4 catalog (§3)
- every operation accepts a universal `marker_key` string field (§3 "Common to all kinds")
- `marker_key` follows the convention GSD_MODIFIER:<carrier-slug>:<op-slug> (§4)
- `marker_key` MUST be globally unique across the manifest (§4); within an entry,
  the SAME key may appear once per runtime materializer (intentional outcome_aligned
  mirroring per §5); the SAME key in two DIFFERENT entries is a collision
- `parity_intent` is REQUIRED for v4 mode: inject entries (§2.3)

This module is parse-time only (Phase 2 Slice 1 boundary): it validates manifest
shape and per-operation field presence/typing. Apply-time and verify-time logic
land in later Phase 2 slices.
"""

from __future__ import annotations

import re
from typing import Any, Callable


OPERATION_KINDS: frozenset[str] = frozenset(
    {
        "section_insert_after",
        "section_replace",
        "step_remove",
        "step_insert_after",
        "include_add",
        "include_remove",
        "block_replace",
    }
)

VALID_PARITY_INTENTS: frozenset[str] = frozenset({"outcome_aligned", "runtime_independent"})

MARKER_KEY_PATTERN: re.Pattern[str] = re.compile(
    r"^GSD_MODIFIER:[a-z0-9-]+(?::[a-z0-9-]+)+$"
)


def format_operation_id(entry_id: str, runtime: str, op_index: int) -> str:
    return f"entry {entry_id!r} runtime {runtime!r} operation #{op_index}"


def _check_required_string(op: dict[str, Any], field: str, op_id: str) -> list[str]:
    value = op.get(field)
    if not isinstance(value, str) or not value:
        return [f"{op_id}: missing or non-string {field!r} field"]
    return []


def validate_marker_key(value: Any, op_id: str) -> list[str]:
    if not isinstance(value, str) or not value:
        return [f"{op_id}: missing or non-string marker_key field"]
    if not MARKER_KEY_PATTERN.match(value):
        return [
            f"{op_id}: marker_key {value!r} does not match required pattern "
            f"{MARKER_KEY_PATTERN.pattern}"
        ]
    return []


def validate_section_insert_after(op: dict[str, Any], op_id: str) -> list[str]:
    errors: list[str] = []
    errors.extend(_check_required_string(op, "tag", op_id))
    errors.extend(_check_required_string(op, "source", op_id))
    return errors


def validate_section_replace(op: dict[str, Any], op_id: str) -> list[str]:
    return _check_required_string(op, "source", op_id)


def validate_step_remove(op: dict[str, Any], op_id: str) -> list[str]:
    return _check_required_string(op, "name", op_id)


def validate_step_insert_after(op: dict[str, Any], op_id: str) -> list[str]:
    errors: list[str] = []
    errors.extend(_check_required_string(op, "after_name", op_id))
    errors.extend(_check_required_string(op, "source", op_id))
    return errors


def validate_include_add(op: dict[str, Any], op_id: str) -> list[str]:
    errors: list[str] = []
    errors.extend(_check_required_string(op, "tag", op_id))
    errors.extend(_check_required_string(op, "line", op_id))
    return errors


def validate_include_remove(op: dict[str, Any], op_id: str) -> list[str]:
    errors: list[str] = []
    errors.extend(_check_required_string(op, "tag", op_id))
    errors.extend(_check_required_string(op, "line", op_id))
    return errors


def validate_block_replace(op: dict[str, Any], op_id: str) -> list[str]:
    errors: list[str] = []
    errors.extend(_check_required_string(op, "start_anchor", op_id))
    errors.extend(_check_required_string(op, "end_anchor", op_id))
    errors.extend(_check_required_string(op, "source", op_id))
    return errors


OPERATION_VALIDATORS: dict[str, Callable[[dict[str, Any], str], list[str]]] = {
    "section_insert_after": validate_section_insert_after,
    "section_replace": validate_section_replace,
    "step_remove": validate_step_remove,
    "step_insert_after": validate_step_insert_after,
    "include_add": validate_include_add,
    "include_remove": validate_include_remove,
    "block_replace": validate_block_replace,
}


def validate_operation(op: Any, op_id: str) -> list[str]:
    """Validate a single operation dict; returns list of error strings (empty == valid)."""
    if not isinstance(op, dict):
        return [f"{op_id}: operation must be an object, got {type(op).__name__}"]
    errors: list[str] = []
    kind = op.get("kind")
    if not isinstance(kind, str) or kind not in OPERATION_KINDS:
        valid = ", ".join(sorted(OPERATION_KINDS))
        errors.append(
            f"{op_id}: missing or invalid kind {kind!r}; expected one of: {valid}"
        )
        errors.extend(validate_marker_key(op.get("marker_key"), op_id))
        return errors
    errors.extend(validate_marker_key(op.get("marker_key"), op_id))
    errors.extend(OPERATION_VALIDATORS[kind](op, op_id))
    return errors


def validate_inject_materializer(
    materializer: dict[str, Any], entry_id: str, runtime: str
) -> tuple[list[str], list[str]]:
    """Validate a mode: inject materializer's operations array.

    Returns (errors, marker_keys) — marker_keys is the ordered list of keys
    declared by this materializer's operations (callers use it to detect
    cross-entry and intra-runtime duplication)."""
    errors: list[str] = []
    marker_keys: list[str] = []
    target = materializer.get("target")
    if not isinstance(target, str) or not target:
        errors.append(
            f"entry {entry_id!r} runtime {runtime!r}: inject materializer is missing or has non-string target"
        )
    operations = materializer.get("operations")
    if not isinstance(operations, list):
        errors.append(
            f"entry {entry_id!r} runtime {runtime!r}: inject materializer must declare an operations list"
        )
        return errors, marker_keys
    if not operations:
        errors.append(
            f"entry {entry_id!r} runtime {runtime!r}: inject materializer operations list is empty"
        )
        return errors, marker_keys
    for op_index, op in enumerate(operations):
        op_id = format_operation_id(entry_id, runtime, op_index)
        errors.extend(validate_operation(op, op_id))
        if isinstance(op, dict):
            mk = op.get("marker_key")
            if isinstance(mk, str) and mk:
                marker_keys.append(mk)
    return errors, marker_keys


def validate_parity_intent(value: Any, entry_id: str) -> list[str]:
    if not isinstance(value, str):
        return [f"entry {entry_id!r}: parity_intent must be a string"]
    if value not in VALID_PARITY_INTENTS:
        valid = ", ".join(sorted(VALID_PARITY_INTENTS))
        return [
            f"entry {entry_id!r}: invalid parity_intent {value!r}; expected one of: {valid}"
        ]
    return []
