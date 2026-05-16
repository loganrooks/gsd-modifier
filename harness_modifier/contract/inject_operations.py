"""Inject-mode operation kinds, validators, and apply-time engine for OVERLAY-MANIFEST.json schema v4.

Per ADR-001 (.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md):

- 7 operation kinds form the v4 catalog (§3)
- every operation accepts a universal `marker_key` string field (§3 "Common to all kinds")
- `marker_key` follows the convention GSD_MODIFIER:<carrier-slug>:<op-slug> (§4)
- `marker_key` MUST be globally unique across the manifest (§4); within an entry,
  the SAME key may appear once per runtime materializer (intentional outcome_aligned
  mirroring per §5); the SAME key in two DIFFERENT entries is a collision
- `parity_intent` is REQUIRED for v4 mode: inject entries (§2.3)
- apply-time semantics per §7: pre-flight atomicity (all operations computed in-memory
  before any caller-side write); idempotency via marker presence + content comparison;
  fail-loud on anchor-not-found, marker_key conflict, or source resolution failure

This module is split into two phases:

- **Parse-time** (Phase 2 Slice 1): manifest shape and per-operation field validation
- **Apply-time** (Phase 2 Slice 2 — this module section): the pure functions that
  transform target content per the operations array, returning new content + records
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
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


# ---------------------------------------------------------------------------
# Apply-time engine (Phase 2 Slice 2)
# ---------------------------------------------------------------------------


class InjectOperationError(Exception):
    """Fatal failure applying an inject operation.

    Carries marker_key + reason so the caller can produce actionable triage
    messages. op_index is filled in by the dispatcher when known."""

    def __init__(
        self,
        message: str,
        *,
        marker_key: str,
        reason: str,
        op_index: int | None = None,
    ) -> None:
        super().__init__(message)
        self.marker_key = marker_key
        self.reason = reason
        self.op_index = op_index


@dataclass(frozen=True)
class OperationRecord:
    """Record of what a single operation did to the content."""

    marker_key: str
    kind: str
    status: str  # "applied" | "skipped_idempotent"
    op_index: int = 0


@dataclass(frozen=True)
class MarkerRegion:
    """Located <!-- GSD_MODIFIER:start key:KEY --> ... end region.

    Line indices are 0-based and refer to the splitlines(keepends=False)
    view of the source content. `body` is the inclusive content between
    (but not including) the marker lines themselves.
    """

    key: str
    start_line: int
    end_line: int
    body: str


def _start_marker(key: str) -> str:
    return f"<!-- GSD_MODIFIER:start key:{key} -->"


def _end_marker(key: str) -> str:
    return f"<!-- GSD_MODIFIER:end key:{key} -->"


def _wrap_with_markers(body: str, key: str) -> str:
    """Wrap a body string with GSD_MODIFIER start/end markers.

    The body is `.strip()`'d so callers can pass source-file content without
    worrying about trailing newlines; this also gives a stable byte sequence
    for the idempotency comparison."""
    return f"{_start_marker(key)}\n{body.strip()}\n{_end_marker(key)}"


class MarkerExtractionError(Exception):
    """Raised when content contains structurally malformed marker regions.

    `reason` is one of: `nested`, `unbalanced_start`, `unbalanced_end`,
    `mismatched_end`, `duplicate_key`. `line` (1-based) points at the offending
    marker line where applicable; `key` carries the marker key involved."""

    def __init__(
        self,
        message: str,
        *,
        reason: str,
        line: int | None = None,
        key: str | None = None,
    ) -> None:
        super().__init__(message)
        self.reason = reason
        self.line = line
        self.key = key


# Deliberately permissive key capture (\S+): the extractor's job is to SURFACE
# structural anomalies, including markers with malformed keys. A stricter regex
# would silently skip lines that look like markers but have a key violating §4
# convention, hiding the corruption from verify-time triage. Key-format validation
# lives in the parse-time manifest validator (MARKER_KEY_PATTERN above).
_MARKER_START_RE: re.Pattern[str] = re.compile(
    r"^<!-- GSD_MODIFIER:start key:(?P<key>\S+) -->$"
)
_MARKER_END_RE: re.Pattern[str] = re.compile(
    r"^<!-- GSD_MODIFIER:end key:(?P<key>\S+) -->$"
)


def extract_inject_markers(content: str) -> dict[str, MarkerRegion]:
    """Scan content for ALL GSD_MODIFIER marker regions and return a {key: MarkerRegion} dict.

    Insertion order in the returned dict reflects first-occurrence ordering in `content`.

    Detects and raises `MarkerExtractionError` for the following malformed states:

    - **nested** — a new start marker appears before the currently-open marker is closed.
      ADR-001 §4 does not describe nested marker regions; injection regions are flat.
    - **unbalanced_start** — a start marker has no matching end marker before EOF.
    - **unbalanced_end** — an end marker appears with no matching prior start.
    - **mismatched_end** — an end marker's key does not match the currently-open start's key.
    - **duplicate_key** — the same KEY is used for two distinct (separately-bracketed)
      marker regions in the same content; apply-time idempotency would only see the first.

    Consumers:

    - `apply_inject_operations` (Phase 2 Slice 2) calls this indirectly via `find_marker`,
      which catches `MarkerExtractionError` to preserve apply-time tolerance — the engine
      can still write a corrected file even when the prior on-disk state is malformed.
    - `verify_inject_state` (Phase 2 Slice 4) will call this directly so verify-time
      surfaces malformed materialized state as a hard failure (the verify gate is the
      right place for the operator to learn about corruption).
    """
    lines = content.splitlines(keepends=False)
    markers: dict[str, MarkerRegion] = {}
    open_key: str | None = None
    open_line: int | None = None
    for i, raw_line in enumerate(lines):
        line = raw_line.strip()
        start_match = _MARKER_START_RE.match(line)
        end_match = _MARKER_END_RE.match(line)
        if start_match is not None:
            key = start_match.group("key")
            if open_key is not None:
                raise MarkerExtractionError(
                    f"nested marker region detected at line {i + 1}: key {key!r} "
                    f"opens while key {open_key!r} (opened at line {open_line + 1 if open_line is not None else '?'}) "
                    f"is still open; ADR-001 §4 does not support nested regions",
                    reason="nested",
                    line=i + 1,
                    key=key,
                )
            if key in markers:
                raise MarkerExtractionError(
                    f"duplicate marker key {key!r} at line {i + 1}; the same KEY already "
                    f"brackets a region starting at line {markers[key].start_line + 1}",
                    reason="duplicate_key",
                    line=i + 1,
                    key=key,
                )
            open_key = key
            open_line = i
            continue
        if end_match is not None:
            key = end_match.group("key")
            if open_key is None:
                raise MarkerExtractionError(
                    f"unbalanced end marker at line {i + 1}: key {key!r} has no matching "
                    f"prior start marker",
                    reason="unbalanced_end",
                    line=i + 1,
                    key=key,
                )
            if key != open_key:
                raise MarkerExtractionError(
                    f"mismatched end marker at line {i + 1}: end key {key!r} does not "
                    f"match currently-open start key {open_key!r} (opened at line "
                    f"{open_line + 1 if open_line is not None else '?'})",
                    reason="mismatched_end",
                    line=i + 1,
                    key=key,
                )
            body = "\n".join(lines[open_line + 1 : i]) if open_line is not None else ""
            markers[open_key] = MarkerRegion(
                key=open_key,
                start_line=open_line if open_line is not None else i,
                end_line=i,
                body=body,
            )
            open_key = None
            open_line = None
    if open_key is not None:
        raise MarkerExtractionError(
            f"unbalanced start marker at line {open_line + 1 if open_line is not None else '?'}: "
            f"key {open_key!r} was never closed before EOF",
            reason="unbalanced_start",
            line=open_line + 1 if open_line is not None else None,
            key=open_key,
        )
    return markers


def find_marker(content: str, key: str) -> MarkerRegion | None:
    """Locate a single marker region by key.

    Implemented in terms of `extract_inject_markers` (Slice 3 refactor). Returns
    None when the key is absent OR when the content's marker structure is
    malformed in any way (nested, unbalanced, mismatched, or duplicate-key).

    Apply-time semantics: when on-disk state is corrupt for this key, returning
    None causes the per-op apply functions to treat the key as absent and EMIT
    A FRESH marker block. The corrupted on-disk region is NOT removed by apply
    (apply is additive, not corrective). The next verify run will call
    `extract_inject_markers` directly and surface the compounded structural
    anomaly as a hard failure — that is the right gate for operator triage.
    Verify-time callers should therefore invoke `extract_inject_markers`
    directly, never `find_marker`."""
    try:
        markers = extract_inject_markers(content)
    except MarkerExtractionError:
        return None
    return markers.get(key)


_STEP_BLOCK_RE_CACHE: dict[str, re.Pattern[str]] = {}


def _find_step_block(content: str, name: str) -> tuple[int, int] | None:
    """Find <step name="NAME"...>...</step> block; returns (start, end) char offsets."""
    if name not in _STEP_BLOCK_RE_CACHE:
        _STEP_BLOCK_RE_CACHE[name] = re.compile(
            rf'<step\s+name="{re.escape(name)}"[^>]*>.*?</step>',
            re.DOTALL,
        )
    m = _STEP_BLOCK_RE_CACHE[name].search(content)
    if m is None:
        return None
    return (m.start(), m.end())


def _replace_lines(content: str, start_line: int, end_line: int, replacement: str) -> str:
    """Replace lines [start_line, end_line] inclusive with `replacement`.

    Preserves the original content's trailing newline (if any)."""
    lines = content.splitlines(keepends=False)
    new_lines = lines[:start_line] + replacement.splitlines() + lines[end_line + 1 :]
    new_content = "\n".join(new_lines)
    if content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"
    return new_content


def _remove_lines(content: str, start_line: int, end_line: int) -> str:
    """Drop lines [start_line, end_line] inclusive."""
    lines = content.splitlines(keepends=False)
    new_lines = lines[:start_line] + lines[end_line + 1 :]
    new_content = "\n".join(new_lines)
    if content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"
    return new_content


def _raise_marker_conflict(marker_key: str, kind: str) -> None:
    raise InjectOperationError(
        f"marker_key {marker_key!r} is present in the target but its content does not "
        f"match the expected source for kind {kind!r}; this indicates either a configuration "
        f"error (two different operations sharing one key) or a manual edit inside the marker "
        f"region (operator triage required)",
        marker_key=marker_key,
        reason="marker_key_conflict",
    )


def _raise_anchor_not_found(marker_key: str, anchor: str, kind: str) -> None:
    raise InjectOperationError(
        f"anchor {anchor!r} not found in target for kind {kind!r} (marker_key {marker_key!r})",
        marker_key=marker_key,
        reason="anchor_not_found",
    )


def apply_section_insert_after(
    content: str, op: dict[str, Any], source: str
) -> tuple[str, str]:
    marker_key = op["marker_key"]
    tag = op["tag"]
    existing = find_marker(content, marker_key)
    if existing is not None:
        if existing.body.strip() == source.strip():
            return content, "skipped_idempotent"
        _raise_marker_conflict(marker_key, "section_insert_after")
    close_tag = f"</{tag}>"
    idx = content.find(close_tag)
    if idx == -1:
        _raise_anchor_not_found(marker_key, close_tag, "section_insert_after")
    insertion_point = idx + len(close_tag)
    marker_block = _wrap_with_markers(source, marker_key)
    new_content = (
        content[:insertion_point] + "\n" + marker_block + content[insertion_point:]
    )
    return new_content, "applied"


def apply_section_replace(
    content: str, op: dict[str, Any], source: str
) -> tuple[str, str]:
    marker_key = op["marker_key"]
    existing = find_marker(content, marker_key)
    if existing is None:
        raise InjectOperationError(
            f"section_replace requires marker_key {marker_key!r} to already be present "
            f"(prior section_insert_after with the same key must have run)",
            marker_key=marker_key,
            reason="anchor_not_found",
        )
    if existing.body.strip() == source.strip():
        return content, "skipped_idempotent"
    new_body = source.strip()
    return (
        _replace_lines(
            content,
            existing.start_line + 1,
            existing.end_line - 1,
            new_body,
        )
        if existing.end_line > existing.start_line + 1
        else _insert_lines_between(content, existing.start_line, existing.end_line, new_body)
    ), "applied"


def _insert_lines_between(content: str, start_line: int, end_line: int, body: str) -> str:
    """Insert `body` lines between two marker lines (no existing body)."""
    lines = content.splitlines(keepends=False)
    new_lines = lines[: start_line + 1] + body.splitlines() + lines[end_line:]
    new_content = "\n".join(new_lines)
    if content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"
    return new_content


def apply_step_remove(content: str, op: dict[str, Any]) -> tuple[str, str]:
    marker_key = op["marker_key"]
    name = op["name"]
    sentinel = f"<!-- GSD_MODIFIER:step_removed name:{name} -->"
    existing = find_marker(content, marker_key)
    if existing is not None:
        if sentinel in existing.body:
            return content, "skipped_idempotent"
        _raise_marker_conflict(marker_key, "step_remove")
    step_loc = _find_step_block(content, name)
    if step_loc is None:
        _raise_anchor_not_found(marker_key, f'<step name="{name}">', "step_remove")
    start, end = step_loc
    marker_block = _wrap_with_markers(sentinel, marker_key)
    new_content = content[:start] + marker_block + content[end:]
    return new_content, "applied"


def apply_step_insert_after(
    content: str, op: dict[str, Any], source: str
) -> tuple[str, str]:
    marker_key = op["marker_key"]
    after_name = op["after_name"]
    existing = find_marker(content, marker_key)
    if existing is not None:
        if existing.body.strip() == source.strip():
            return content, "skipped_idempotent"
        _raise_marker_conflict(marker_key, "step_insert_after")
    step_loc = _find_step_block(content, after_name)
    if step_loc is None:
        _raise_anchor_not_found(
            marker_key, f'<step name="{after_name}">', "step_insert_after"
        )
    _start, end = step_loc
    marker_block = _wrap_with_markers(source, marker_key)
    new_content = content[:end] + "\n" + marker_block + content[end:]
    return new_content, "applied"


def apply_include_add(content: str, op: dict[str, Any]) -> tuple[str, str]:
    marker_key = op["marker_key"]
    tag = op["tag"]
    line = op["line"]
    existing = find_marker(content, marker_key)
    if existing is not None:
        if existing.body.strip() == line.strip():
            return content, "skipped_idempotent"
        _raise_marker_conflict(marker_key, "include_add")
    close_tag = f"</{tag}>"
    idx = content.find(close_tag)
    if idx == -1:
        _raise_anchor_not_found(marker_key, close_tag, "include_add")
    marker_block = _wrap_with_markers(line, marker_key)
    new_content = content[:idx] + marker_block + "\n" + content[idx:]
    return new_content, "applied"


def apply_include_remove(content: str, op: dict[str, Any]) -> tuple[str, str]:
    marker_key = op["marker_key"]
    line = op["line"]
    existing = find_marker(content, marker_key)
    if existing is None:
        return content, "skipped_idempotent"
    if line.strip() not in existing.body:
        raise InjectOperationError(
            f"include_remove marker_key {marker_key!r} body does not contain expected "
            f"line {line!r}; operator triage required to reconcile manifest with target",
            marker_key=marker_key,
            reason="marker_key_conflict",
        )
    new_content = _remove_lines(content, existing.start_line, existing.end_line)
    return new_content, "applied"


def apply_block_replace(
    content: str, op: dict[str, Any], source: str
) -> tuple[str, str]:
    marker_key = op["marker_key"]
    start_anchor = op["start_anchor"]
    end_anchor = op["end_anchor"]
    existing = find_marker(content, marker_key)
    if existing is not None:
        if existing.body.strip() == source.strip():
            return content, "skipped_idempotent"
        _raise_marker_conflict(marker_key, "block_replace")
    start_idx = content.find(start_anchor)
    if start_idx == -1:
        _raise_anchor_not_found(marker_key, start_anchor, "block_replace")
    if start_anchor == end_anchor:
        # Degenerate same-anchor case (per ADR-001 §A.1 worked example):
        # the "between" region is empty; the operation effectively inserts
        # AFTER the anchor.
        insertion_point = start_idx + len(start_anchor)
        marker_block = _wrap_with_markers(source, marker_key)
        new_content = (
            content[:insertion_point] + "\n" + marker_block + content[insertion_point:]
        )
        return new_content, "applied"
    end_search_start = start_idx + len(start_anchor)
    end_idx = content.find(end_anchor, end_search_start)
    if end_idx == -1:
        _raise_anchor_not_found(marker_key, end_anchor, "block_replace")
    between_start = start_idx + len(start_anchor)
    marker_block = _wrap_with_markers(source, marker_key)
    new_content = (
        content[:between_start] + "\n" + marker_block + "\n" + content[end_idx:]
    )
    return new_content, "applied"


# Per-kind apply dispatch (kind -> (apply_callable, needs_source))
_APPLY_NEEDS_SOURCE: dict[str, tuple[Callable[..., tuple[str, str]], bool]] = {
    "section_insert_after": (apply_section_insert_after, True),
    "section_replace": (apply_section_replace, True),
    "step_remove": (apply_step_remove, False),
    "step_insert_after": (apply_step_insert_after, True),
    "include_add": (apply_include_add, False),
    "include_remove": (apply_include_remove, False),
    "block_replace": (apply_block_replace, True),
}


def apply_inject_operations(
    content: str,
    operations: list[dict[str, Any]],
    source_resolver: Callable[[str], str],
) -> tuple[str, list[OperationRecord]]:
    """Apply all inject operations in declared order; return (new_content, records).

    Pure function: does NOT write files. The caller (portable_gsd_contract.apply_overlay)
    is responsible for atomic write.

    Pre-flight atomicity per ADR-001 §7: all operations are computed in-memory before
    any caller-side write. If any operation raises InjectOperationError, this function
    propagates the exception WITHOUT returning a partial result. The caller can leave
    the on-disk target untouched, satisfying ADR's "no half-migrated file is ever written."

    The source_resolver is a callable that takes the operation's `source` string field
    and returns the source file content. Callers compose it with their own I/O (e.g.,
    `lambda p: (repo_root / p).read_text(encoding='utf-8')`); tests can pass a dict-backed
    closure for synthetic content.

    Anchor-resolution convention: all per-kind apply functions resolve their anchor
    (close tag for section_insert_after / include_add; step name for step_remove /
    step_insert_after; start/end anchor text for block_replace) to the FIRST match in
    the target content. Targets with the same anchor appearing multiple times will
    bind to the first one. ADR-001 §A.1–A.4 carriers do not exhibit multi-occurrence
    anchors; if a future migration surfaces one, the per-kind signature would need
    extension (e.g., an occurrence-index argument or a more specific anchor).
    """
    current = content
    records: list[OperationRecord] = []
    for op_index, op in enumerate(operations):
        if not isinstance(op, dict):
            raise InjectOperationError(
                f"operation #{op_index} is not a dict (got {type(op).__name__})",
                marker_key="",
                reason="malformed_operation",
                op_index=op_index,
            )
        kind = op.get("kind")
        marker_key = op.get("marker_key", "")
        if not isinstance(kind, str) or kind not in _APPLY_NEEDS_SOURCE:
            raise InjectOperationError(
                f"operation #{op_index} has unknown kind {kind!r}",
                marker_key=str(marker_key) if isinstance(marker_key, str) else "",
                reason="unknown_kind",
                op_index=op_index,
            )
        apply_fn, needs_source = _APPLY_NEEDS_SOURCE[kind]
        try:
            if needs_source:
                source_path = op.get("source")
                if not isinstance(source_path, str) or not source_path:
                    raise InjectOperationError(
                        f"operation #{op_index} (kind {kind!r}) requires a non-empty source field",
                        marker_key=str(marker_key),
                        reason="malformed_operation",
                        op_index=op_index,
                    )
                try:
                    source_content = source_resolver(source_path)
                except (FileNotFoundError, IsADirectoryError, OSError) as exc:
                    raise InjectOperationError(
                        f"operation #{op_index} (kind {kind!r}) failed to resolve source "
                        f"{source_path!r}: {exc}",
                        marker_key=str(marker_key),
                        reason="source_missing",
                        op_index=op_index,
                    ) from exc
                current, status = apply_fn(current, op, source_content)
            else:
                current, status = apply_fn(current, op)
        except InjectOperationError as exc:
            if exc.op_index is None:
                exc.op_index = op_index
            raise
        records.append(
            OperationRecord(
                marker_key=str(marker_key),
                kind=kind,
                status=status,
                op_index=op_index,
            )
        )
    return current, records
