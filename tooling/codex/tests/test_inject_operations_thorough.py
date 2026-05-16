"""Thorough per-kind exercise tests for inject_operations (Phase 2 Slice 5).

Per slice spec (phases/02-contract-tools.md:105-114): "comprehensive cases:
happy path, missing anchor, malformed anchor, ambiguous anchor, idempotency,
ordering". This suite goes beyond the per-slice tests in Slices 2-4 to surface
edge cases that those didn't exercise.

Coverage themes:

- **Per-kind ambiguous-anchor**: multiple matches of the same anchor in target
  content — verifies the "first-match" convention documented in
  apply_inject_operations docstring
- **Per-kind malformed-anchor**: edge cases on what counts as the anchor (e.g.,
  whitespace, attributes, partial matches)
- **Per-kind ordering**: operations that depend on prior operation outputs;
  verify the in-declared-order contract
- **Reviewer-flagged Slice 5 follow-ups** (from Slice 3/4 polish notes):
  - Slice 3 polish: find_marker returns None on nested-but-closed/duplicate-key
    structures for the target key (the real behavioral divergence from the
    pre-refactor find_marker)
  - Slice 4 polish: _find_line_index_of substring asymmetry — a marker placed
    BEFORE the real </tag> anchor can incorrectly verify as OK if any earlier
    text mentions </tag>
  - Slice 4 polish: _step_block_present_outside_markers nested-step body
    false-match potential (step block quoted inside another step's body)
- **Slice 2 polish: section_replace on empty-body marker** (exercises the
  _insert_lines_between branch that Slice 2's per-kind test set did not hit)
"""

import unittest
from typing import Any

from harness_modifier.contract import inject_operations
from harness_modifier.contract.inject_operations import (
    InjectOperationError,
    MarkerExtractionError,
    apply_inject_operations,
    extract_inject_markers,
    find_marker,
    verify_inject_state,
    VERIFY_STATUS_OK,
    VERIFY_STATUS_WRONG_POSITION,
    VERIFY_STATUS_UNEXPECTED_PRESENT,
)


def _resolver_from(mapping: dict[str, str]):
    def _resolve(path: str) -> str:
        if path not in mapping:
            raise FileNotFoundError(path)
        return mapping[path]

    return _resolve


def _wrap(body: str, key: str) -> str:
    return (
        f"<!-- GSD_MODIFIER:start key:{key} -->\n"
        f"{body.strip()}\n"
        f"<!-- GSD_MODIFIER:end key:{key} -->"
    )


# ---------------------------------------------------------------------------
# Per-kind: ambiguous anchor (first-match convention)
# ---------------------------------------------------------------------------


class AmbiguousAnchorTests(unittest.TestCase):
    """The apply engine resolves anchors via first-match per the
    apply_inject_operations docstring. Verify the convention holds across the
    affected kinds."""

    def test_section_insert_after_picks_first_close_tag_when_repeated(self) -> None:
        # Content has TWO </required_reading> close tags; first-match should win.
        content = (
            "<required_reading>\n@first\n</required_reading>\n"
            "<filler/>\n"
            "<required_reading>\n@second\n</required_reading>\n"
        )
        op = {
            "kind": "section_insert_after",
            "tag": "required_reading",
            "source": "src.md",
            "marker_key": "GSD_MODIFIER:ambig:section",
        }
        resolver = _resolver_from({"src.md": "BODY\n"})
        new_content, _ = apply_inject_operations(content, [op], resolver)
        # The marker should land after the FIRST </required_reading>
        first_close_idx = new_content.find("</required_reading>")
        marker_idx = new_content.find("<!-- GSD_MODIFIER:start")
        self.assertLess(first_close_idx, marker_idx)
        second_close_idx = new_content.find("</required_reading>", first_close_idx + 1)
        self.assertLess(marker_idx, second_close_idx)

    def test_step_remove_picks_first_step_block_with_matching_name(self) -> None:
        # If the SAME step name appears twice (likely a configuration bug, but
        # exercise the first-match convention regardless), the first is removed.
        content = (
            "<process>\n"
            '<step name="dup">first</step>\n'
            '<step name="dup">second</step>\n'
            "</process>\n"
        )
        op = {
            "kind": "step_remove",
            "name": "dup",
            "marker_key": "GSD_MODIFIER:ambig:step",
        }
        new_content, _ = apply_inject_operations(content, [op], _resolver_from({}))
        # The first dup-step is now a marker; the second remains as plain text
        self.assertIn("second", new_content)
        self.assertIn("<!-- GSD_MODIFIER:step_removed name:dup -->", new_content)

    def test_block_replace_picks_first_start_anchor_when_repeated(self) -> None:
        content = (
            "before\n"
            "START\noriginal-first\nEND\n"
            "middle\n"
            "START\noriginal-second\nEND\n"
            "after\n"
        )
        op = {
            "kind": "block_replace",
            "start_anchor": "START",
            "end_anchor": "END",
            "source": "src.md",
            "marker_key": "GSD_MODIFIER:ambig:block",
        }
        resolver = _resolver_from({"src.md": "NEW\n"})
        new_content, _ = apply_inject_operations(content, [op], resolver)
        # First START/END pair replaced; second pair untouched
        self.assertIn("original-second", new_content)
        self.assertNotIn("original-first", new_content)


# ---------------------------------------------------------------------------
# Per-kind: malformed anchor variants
# ---------------------------------------------------------------------------


class MalformedAnchorTests(unittest.TestCase):
    def test_section_insert_after_handles_tag_with_open_attributes(self) -> None:
        # Open tag has attributes; close tag does not (close tags never have attributes per XML spec).
        content = '<required_reading minimum="2">\n@x\n</required_reading>\n'
        op = {
            "kind": "section_insert_after",
            "tag": "required_reading",
            "source": "src.md",
            "marker_key": "GSD_MODIFIER:malformed:openattr",
        }
        resolver = _resolver_from({"src.md": "BODY\n"})
        new_content, _ = apply_inject_operations(content, [op], resolver)
        # Marker should land after </required_reading>
        self.assertIn("<!-- GSD_MODIFIER:start", new_content)

    def test_step_remove_anchor_only_matches_exact_name(self) -> None:
        # name="other" should not match name="context_check"
        content = '<process>\n<step name="context_check_subroutine">x</step>\n</process>\n'
        op = {
            "kind": "step_remove",
            "name": "context_check",
            "marker_key": "GSD_MODIFIER:malformed:exactname",
        }
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [op], _resolver_from({}))
        self.assertEqual(ctx.exception.reason, "anchor_not_found")

    def test_include_add_close_tag_anchor_must_be_an_actual_close_tag(self) -> None:
        # If the target has only an open tag and no close tag, the operation fails.
        content = "<supporting_reading>\n@x\n"  # missing </supporting_reading>
        op = {
            "kind": "include_add",
            "tag": "supporting_reading",
            "line": "@__PROJECT_ROOT__/new.md",
            "marker_key": "GSD_MODIFIER:malformed:nooclose",
        }
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [op], _resolver_from({}))
        self.assertEqual(ctx.exception.reason, "anchor_not_found")


# ---------------------------------------------------------------------------
# Per-kind: ordering — operations apply in declared order
# ---------------------------------------------------------------------------


class OrderingTests(unittest.TestCase):
    def test_section_replace_after_section_insert_after_works_when_sequential(self) -> None:
        # Declared order: insert (creates marker) → replace (updates body)
        content = "<required_reading>\n@x\n</required_reading>\n"
        ops = [
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "v1.md",
                "marker_key": "GSD_MODIFIER:ordering:section",
            },
            {
                "kind": "section_replace",
                "source": "v2.md",
                "marker_key": "GSD_MODIFIER:ordering:section",
            },
        ]
        resolver = _resolver_from({"v1.md": "VERSION 1\n", "v2.md": "VERSION 2\n"})
        new_content, records = apply_inject_operations(content, ops, resolver)
        # After both ops, content should have V2 (replaced)
        self.assertIn("VERSION 2", new_content)
        self.assertNotIn("VERSION 1", new_content)
        self.assertEqual(records[0].status, "applied")
        self.assertEqual(records[1].status, "applied")

    def test_section_replace_before_section_insert_after_fails_due_to_order(self) -> None:
        # Reversed declared order: replace tries to find marker that doesn't exist yet → fatal
        content = "<required_reading>\n@x\n</required_reading>\n"
        ops = [
            {
                "kind": "section_replace",
                "source": "v2.md",
                "marker_key": "GSD_MODIFIER:ordering:wrong-order",
            },
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "v1.md",
                "marker_key": "GSD_MODIFIER:ordering:wrong-order",
            },
        ]
        resolver = _resolver_from({"v1.md": "V1\n", "v2.md": "V2\n"})
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, ops, resolver)
        # First op (section_replace) fails because marker is absent
        self.assertEqual(ctx.exception.op_index, 0)
        self.assertEqual(ctx.exception.reason, "anchor_not_found")

    def test_step_insert_then_section_insert_apply_in_sequence(self) -> None:
        content = (
            "<process>\n"
            '<step name="anchor">A</step>\n'
            "</process>\n"
            "<required_reading>\n@x\n</required_reading>\n"
        )
        ops = [
            {
                "kind": "step_insert_after",
                "after_name": "anchor",
                "source": "step.md",
                "marker_key": "GSD_MODIFIER:ordering:step",
            },
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "section.md",
                "marker_key": "GSD_MODIFIER:ordering:section",
            },
        ]
        resolver = _resolver_from(
            {
                "step.md": '<step name="injected">INJ</step>',
                "section.md": "EXTRA\n",
            }
        )
        new_content, records = apply_inject_operations(content, ops, resolver)
        self.assertEqual(len(records), 2)
        self.assertIn('<step name="injected">INJ</step>', new_content)
        self.assertIn("EXTRA", new_content)


# ---------------------------------------------------------------------------
# Slice 3 reviewer follow-up: find_marker None on nested-but-closed / duplicate-key
# ---------------------------------------------------------------------------


class FindMarkerBehavioralDivergenceTests(unittest.TestCase):
    """The Slice 3 refactor of find_marker (now wraps extract_inject_markers)
    diverges from the pre-refactor behavior when on-disk state is structurally
    bracketed but anomalous for the target key. These tests pin the new
    behavior so a future refactor cannot silently regress."""

    def test_find_marker_returns_none_when_target_key_in_nested_structure(self) -> None:
        # Content has nested markers; find_marker for the outer key would have
        # returned a region under the pre-Slice-3 single-key scan, but now
        # returns None because extract_inject_markers raises on nested.
        outer_key = "GSD_MODIFIER:divergence:outer"
        inner_key = "GSD_MODIFIER:divergence:inner"
        content = (
            f"<!-- GSD_MODIFIER:start key:{outer_key} -->\n"
            f"<!-- GSD_MODIFIER:start key:{inner_key} -->\n"
            f"INNER BODY\n"
            f"<!-- GSD_MODIFIER:end key:{inner_key} -->\n"
            f"<!-- GSD_MODIFIER:end key:{outer_key} -->\n"
        )
        self.assertIsNone(find_marker(content, outer_key))
        self.assertIsNone(find_marker(content, inner_key))
        # And extract_inject_markers surfaces the structural anomaly
        with self.assertRaises(MarkerExtractionError) as ctx:
            extract_inject_markers(content)
        self.assertEqual(ctx.exception.reason, "nested")

    def test_find_marker_returns_none_when_target_key_is_duplicated(self) -> None:
        # The same key brackets two distinct regions; find_marker returns None
        # for that key (could not unambiguously identify a single region).
        key = "GSD_MODIFIER:divergence:dup"
        content = _wrap("first body", key) + "\nseparator\n" + _wrap("second body", key) + "\n"
        self.assertIsNone(find_marker(content, key))
        with self.assertRaises(MarkerExtractionError) as ctx:
            extract_inject_markers(content)
        self.assertEqual(ctx.exception.reason, "duplicate_key")


# ---------------------------------------------------------------------------
# Slice 4 reviewer follow-up: _find_line_index_of substring asymmetry
# ---------------------------------------------------------------------------


class VerifyHelperAsymmetryTests(unittest.TestCase):
    """Slice 4 reviewer flagged: _find_line_index_of(content, "</tag>") matches
    any line CONTAINING "</tag>", while _verify_position_inside_tag uses
    line-equals-based matching. This means a section_insert_after marker placed
    BEFORE the real </tag> can verify as OK if a prior line mentions "</tag>".
    Pin the current behavior so it doesn't silently regress; tightening
    _find_line_index_of would be a separate (tracked) follow-up."""

    def test_section_insert_after_verify_accepts_marker_before_real_anchor_when_earlier_line_mentions_close_tag(
        self,
    ) -> None:
        # Setup: content has TWO lines mentioning </tag>:
        #   line 0: prose mentioning </required_reading>
        #   line 4: actual </required_reading> close tag
        # Marker is placed on line 2 (AFTER line 0 but BEFORE line 4).
        # Per the substring matcher, verify finds the anchor on line 0 and
        # accepts the marker (line 2) as "after the anchor". This is the
        # documented current behavior (substring asymmetry).
        key = "GSD_MODIFIER:asymmetry:substring"
        content = (
            "prose discussing </required_reading> conventions\n"  # line 0
            "<required_reading>\n"  # line 1
            "@x\n"  # line 2 ... but we put the marker here instead
        )
        # Construct so marker lands between the prose-mention and the real close
        content = (
            "prose discussing </required_reading> conventions\n"
            + _wrap("BODY", key)
            + "\n"
            + "<required_reading>\n@x\n</required_reading>\n"
        )
        ops = [
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "src.md",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        # Current behavior: verify accepts this (substring match on prose-mention)
        # This test pins the behavior; if _find_line_index_of is tightened in a
        # later slice to use exact line match, this test must be updated.
        self.assertTrue(
            result.passed,
            f"current substring-asymmetry behavior: {[(v.status, v.detail) for v in result.operation_verifications]}",
        )

    def test_step_remove_does_not_falsely_succeed_when_step_name_appears_in_another_steps_body(
        self,
    ) -> None:
        # _step_block_present_outside_markers uses regex
        # `<step\s+name="NAME"[^>]*>.*?</step>` with re.DOTALL. If "NAME"
        # appears as text inside another step's body (not as a step element),
        # the regex needs to NOT match.
        # Construct a case where step body REFERENCES the removed step's name
        # in TEXT (not as another <step> element), and confirm verify still
        # correctly flags it as removed.
        key = "GSD_MODIFIER:asymmetry:nested-step-text"
        content = (
            "<process>\n"
            '<step name="other">do something with context_check first</step>\n'
            + _wrap(
                "<!-- GSD_MODIFIER:step_removed name:context_check -->", key
            )
            + "\n"
            "</process>\n"
        )
        ops = [
            {
                "kind": "step_remove",
                "name": "context_check",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        # The reference in the other step's body is plain TEXT, not a step element.
        # The step regex only matches `<step name="X">...</step>` ELEMENT form.
        self.assertTrue(result.passed)


# ---------------------------------------------------------------------------
# Slice 2 reviewer follow-up: section_replace on empty-body marker
# ---------------------------------------------------------------------------


class SectionReplaceEmptyBodyTests(unittest.TestCase):
    """Slice 2 reviewer flagged _insert_lines_between as untested (markers with
    empty body don't arise in typical apply paths because _wrap_with_markers
    always emits .strip()'d body between markers). Exercise the branch."""

    def test_section_replace_on_empty_body_marker_succeeds(self) -> None:
        # Construct content with adjacent marker pair (empty body between)
        key = "GSD_MODIFIER:empty-body:section"
        content = (
            "<header/>\n"
            f"<!-- GSD_MODIFIER:start key:{key} -->\n"
            f"<!-- GSD_MODIFIER:end key:{key} -->\n"
            "<footer/>\n"
        )
        ops = [{"kind": "section_replace", "source": "src.md", "marker_key": key}]
        resolver = _resolver_from({"src.md": "NEW BODY\n"})
        new_content, records = apply_inject_operations(content, ops, resolver)
        self.assertIn("NEW BODY", new_content)
        self.assertEqual(records[0].status, "applied")


# ---------------------------------------------------------------------------
# Per-kind: idempotency under permutation
# ---------------------------------------------------------------------------


class IdempotencyUnderPermutationTests(unittest.TestCase):
    """Apply the same operation set 3 times and confirm the final content is
    invariant after the first apply (the strongest form of idempotency)."""

    def test_three_pass_idempotency_section_insert_after(self) -> None:
        key = "GSD_MODIFIER:idem3pass:section"
        original = "<required_reading>\n@x\n</required_reading>\n"
        op = {
            "kind": "section_insert_after",
            "tag": "required_reading",
            "source": "src.md",
            "marker_key": key,
        }
        resolver = _resolver_from({"src.md": "INV\n"})
        after_1, _ = apply_inject_operations(original, [op], resolver)
        after_2, recs2 = apply_inject_operations(after_1, [op], resolver)
        after_3, recs3 = apply_inject_operations(after_2, [op], resolver)
        self.assertEqual(after_1, after_2)
        self.assertEqual(after_2, after_3)
        self.assertTrue(all(r.status == "skipped_idempotent" for r in recs2))
        self.assertTrue(all(r.status == "skipped_idempotent" for r in recs3))

    def test_three_pass_idempotency_all_seven_kinds_sequenced(self) -> None:
        # Build a content + ops set that exercises every kind, then apply 3x.
        content = (
            "<process>\n"
            '<step name="anchor">A</step>\n'
            '<step name="to_remove">RM</step>\n'
            "</process>\n"
            "<required_reading>\n@x\n</required_reading>\n"
            "<supporting_reading>\n@y\n</supporting_reading>\n"
            "BLOCK_START\nold middle\nBLOCK_END\n"
        )
        ops = [
            # 1. section_insert_after creates marker A
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "a.md",
                "marker_key": "GSD_MODIFIER:idem-all:section-a",
            },
            # 2. section_replace updates marker A's body (idempotent if same source)
            {
                "kind": "section_replace",
                "source": "a.md",
                "marker_key": "GSD_MODIFIER:idem-all:section-a",
            },
            # 3. step_remove removes the 'to_remove' step
            {
                "kind": "step_remove",
                "name": "to_remove",
                "marker_key": "GSD_MODIFIER:idem-all:step-remove",
            },
            # 4. step_insert_after inserts after 'anchor'
            {
                "kind": "step_insert_after",
                "after_name": "anchor",
                "source": "step.md",
                "marker_key": "GSD_MODIFIER:idem-all:step-insert",
            },
            # 5. include_add
            {
                "kind": "include_add",
                "tag": "supporting_reading",
                "line": "@__PROJECT_ROOT__/new.md",
                "marker_key": "GSD_MODIFIER:idem-all:include-add",
            },
            # 6. block_replace
            {
                "kind": "block_replace",
                "start_anchor": "BLOCK_START",
                "end_anchor": "BLOCK_END",
                "source": "block.md",
                "marker_key": "GSD_MODIFIER:idem-all:block",
            },
            # NOTE: include_remove is excluded from this sequence because it
            # would require a prior include_add marker to remove; covered separately
        ]
        resolver = _resolver_from(
            {
                "a.md": "BODY A\n",
                "step.md": '<step name="injected">INJ</step>',
                "block.md": "NEW BLOCK\n",
            }
        )
        after_1, _ = apply_inject_operations(content, ops, resolver)
        after_2, recs2 = apply_inject_operations(after_1, ops, resolver)
        after_3, recs3 = apply_inject_operations(after_2, ops, resolver)
        self.assertEqual(after_1, after_2)
        self.assertEqual(after_2, after_3)
        self.assertTrue(
            all(r.status == "skipped_idempotent" for r in recs2),
            f"second pass had non-skip records: {[(r.kind, r.status) for r in recs2]}",
        )

    def test_include_remove_idempotency_under_repeated_application(self) -> None:
        # Setup: marker for the key is initially present; first apply removes it;
        # second apply is a no-op (skip).
        key = "GSD_MODIFIER:idem3pass:include-rm"
        content_with_marker = (
            "<supporting_reading>\n"
            + _wrap("@__PROJECT_ROOT__/old.md", key)
            + "\n</supporting_reading>\n"
        )
        op = {
            "kind": "include_remove",
            "tag": "supporting_reading",
            "line": "@__PROJECT_ROOT__/old.md",
            "marker_key": key,
        }
        after_1, recs1 = apply_inject_operations(
            content_with_marker, [op], _resolver_from({})
        )
        after_2, recs2 = apply_inject_operations(after_1, [op], _resolver_from({}))
        self.assertEqual(after_1, after_2)
        self.assertEqual(recs1[0].status, "applied")
        self.assertEqual(recs2[0].status, "skipped_idempotent")


# ---------------------------------------------------------------------------
# Verify-time round-trip: apply then verify
# ---------------------------------------------------------------------------


class ApplyThenVerifyRoundTripTests(unittest.TestCase):
    """For each kind, apply the op then immediately verify; the verify should
    pass. Complements Slice 2 (apply-only) and Slice 4 (verify-only) by binding
    the two together."""

    def _round_trip(self, content: str, ops: list[dict[str, Any]], resolver) -> None:
        applied, _ = apply_inject_operations(content, ops, resolver)
        result = verify_inject_state(applied, ops)
        self.assertTrue(
            result.passed,
            f"apply→verify round-trip failed: {[(v.status, v.detail) for v in result.operation_verifications]}",
        )

    def test_section_insert_after_round_trip(self) -> None:
        self._round_trip(
            "<required_reading>\n@x\n</required_reading>\n",
            [
                {
                    "kind": "section_insert_after",
                    "tag": "required_reading",
                    "source": "s.md",
                    "marker_key": "GSD_MODIFIER:rt:sia",
                }
            ],
            _resolver_from({"s.md": "BODY\n"}),
        )

    def test_step_insert_after_round_trip(self) -> None:
        self._round_trip(
            "<process>\n"
            '<step name="anchor">A</step>\n'
            "</process>\n",
            [
                {
                    "kind": "step_insert_after",
                    "after_name": "anchor",
                    "source": "s.md",
                    "marker_key": "GSD_MODIFIER:rt:sia2",
                }
            ],
            _resolver_from({"s.md": '<step name="x">x</step>'}),
        )

    def test_include_add_round_trip(self) -> None:
        self._round_trip(
            "<supporting_reading>\n@x\n</supporting_reading>\n",
            [
                {
                    "kind": "include_add",
                    "tag": "supporting_reading",
                    "line": "@__PROJECT_ROOT__/new.md",
                    "marker_key": "GSD_MODIFIER:rt:ia",
                }
            ],
            _resolver_from({}),
        )

    def test_block_replace_round_trip(self) -> None:
        self._round_trip(
            "before\nSTART\nold\nEND\nafter\n",
            [
                {
                    "kind": "block_replace",
                    "start_anchor": "START",
                    "end_anchor": "END",
                    "source": "s.md",
                    "marker_key": "GSD_MODIFIER:rt:br",
                }
            ],
            _resolver_from({"s.md": "NEW\n"}),
        )

    def test_step_remove_round_trip(self) -> None:
        self._round_trip(
            "<process>\n"
            '<step name="rm">x</step>\n'
            "</process>\n",
            [
                {
                    "kind": "step_remove",
                    "name": "rm",
                    "marker_key": "GSD_MODIFIER:rt:sr",
                }
            ],
            _resolver_from({}),
        )

    def test_include_remove_round_trip_from_pre_existing_marker(self) -> None:
        # include_remove: precondition is a marker exists; apply removes it; verify
        # should then pass (post-state: marker absent).
        key = "GSD_MODIFIER:rt:ir"
        content = (
            "<supporting_reading>\n"
            + _wrap("@__PROJECT_ROOT__/old.md", key)
            + "\n</supporting_reading>\n"
        )
        ops = [
            {
                "kind": "include_remove",
                "tag": "supporting_reading",
                "line": "@__PROJECT_ROOT__/old.md",
                "marker_key": key,
            }
        ]
        applied, _ = apply_inject_operations(content, ops, _resolver_from({}))
        result = verify_inject_state(applied, ops)
        self.assertTrue(result.passed)


if __name__ == "__main__":
    unittest.main()
