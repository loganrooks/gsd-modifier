"""Apply-time tests for inject_operations (Phase 2 Slice 2).

One happy-path + one idempotency + at least one fatal-failure test per kind.
Plus dispatcher tests for sequencing and pre-flight atomicity.

Synthetic content; no filesystem I/O — source_resolver is dict-backed.
"""

import unittest
from typing import Any

from harness_modifier.contract import inject_operations
from harness_modifier.contract.inject_operations import (
    InjectOperationError,
    OperationRecord,
    apply_inject_operations,
)


def _resolver_from(mapping: dict[str, str]):
    def _resolve(source_path: str) -> str:
        if source_path not in mapping:
            raise FileNotFoundError(source_path)
        return mapping[source_path]

    return _resolve


def _start(key: str) -> str:
    return f"<!-- GSD_MODIFIER:start key:{key} -->"


def _end(key: str) -> str:
    return f"<!-- GSD_MODIFIER:end key:{key} -->"


def _wrap(body: str, key: str) -> str:
    return f"{_start(key)}\n{body.strip()}\n{_end(key)}"


# ---------------------------------------------------------------------------
# section_insert_after
# ---------------------------------------------------------------------------


class SectionInsertAfterTests(unittest.TestCase):
    KEY = "GSD_MODIFIER:test-carrier:section-op"

    def _op(self) -> dict[str, Any]:
        return {
            "kind": "section_insert_after",
            "tag": "required_reading",
            "source": "src.md",
            "marker_key": self.KEY,
        }

    def test_happy_path_inserts_after_close_tag(self) -> None:
        content = "<header/>\n<required_reading>\n@docs/foo.md\n</required_reading>\n<footer/>\n"
        resolver = _resolver_from({"src.md": "EXTRA CONTENT\n"})
        new_content, records = apply_inject_operations(content, [self._op()], resolver)
        self.assertIn(_start(self.KEY), new_content)
        self.assertIn("EXTRA CONTENT", new_content)
        self.assertIn(_end(self.KEY), new_content)
        # Marker block lands AFTER </required_reading>
        close_idx = new_content.find("</required_reading>")
        start_idx = new_content.find(_start(self.KEY))
        self.assertLess(close_idx, start_idx)
        self.assertEqual(records[0].status, "applied")

    def test_idempotency_skip_when_marker_present_with_matching_content(self) -> None:
        original_content = (
            "<required_reading>\n@x\n</required_reading>\n"
            + _wrap("EXTRA CONTENT", self.KEY)
            + "\n"
        )
        resolver = _resolver_from({"src.md": "EXTRA CONTENT\n"})
        new_content, records = apply_inject_operations(original_content, [self._op()], resolver)
        self.assertEqual(new_content, original_content)
        self.assertEqual(records[0].status, "skipped_idempotent")

    def test_fatal_marker_present_with_different_content(self) -> None:
        original_content = (
            "<required_reading>\n@x\n</required_reading>\n"
            + _wrap("DIFFERENT CONTENT", self.KEY)
            + "\n"
        )
        resolver = _resolver_from({"src.md": "EXTRA CONTENT\n"})
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(original_content, [self._op()], resolver)
        self.assertEqual(ctx.exception.reason, "marker_key_conflict")
        self.assertEqual(ctx.exception.marker_key, self.KEY)

    def test_fatal_anchor_not_found(self) -> None:
        content = "<other_tag>x</other_tag>\n"
        resolver = _resolver_from({"src.md": "EXTRA\n"})
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [self._op()], resolver)
        self.assertEqual(ctx.exception.reason, "anchor_not_found")


# ---------------------------------------------------------------------------
# section_replace
# ---------------------------------------------------------------------------


class SectionReplaceTests(unittest.TestCase):
    KEY = "GSD_MODIFIER:test-carrier:section-replace-op"

    def _op(self) -> dict[str, Any]:
        return {
            "kind": "section_replace",
            "source": "src.md",
            "marker_key": self.KEY,
        }

    def test_happy_path_replaces_body_between_markers(self) -> None:
        content = (
            "<header/>\n" + _wrap("OLD BODY", self.KEY) + "\n<footer/>\n"
        )
        resolver = _resolver_from({"src.md": "NEW BODY\n"})
        new_content, records = apply_inject_operations(content, [self._op()], resolver)
        self.assertIn("NEW BODY", new_content)
        self.assertNotIn("OLD BODY", new_content)
        self.assertIn(_start(self.KEY), new_content)
        self.assertIn(_end(self.KEY), new_content)
        self.assertEqual(records[0].status, "applied")

    def test_idempotency_skip_when_content_already_matches(self) -> None:
        content = (
            "<header/>\n" + _wrap("NEW BODY", self.KEY) + "\n<footer/>\n"
        )
        resolver = _resolver_from({"src.md": "NEW BODY\n"})
        new_content, records = apply_inject_operations(content, [self._op()], resolver)
        self.assertEqual(new_content, content)
        self.assertEqual(records[0].status, "skipped_idempotent")

    def test_fatal_when_marker_absent(self) -> None:
        # section_replace requires a prior section_insert_after to have landed.
        content = "<header/>\n<footer/>\n"
        resolver = _resolver_from({"src.md": "NEW BODY\n"})
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [self._op()], resolver)
        self.assertEqual(ctx.exception.reason, "anchor_not_found")


# ---------------------------------------------------------------------------
# step_remove
# ---------------------------------------------------------------------------


class StepRemoveTests(unittest.TestCase):
    KEY = "GSD_MODIFIER:test-carrier:step-remove-op"

    def _op(self) -> dict[str, Any]:
        return {
            "kind": "step_remove",
            "name": "context_check",
            "marker_key": self.KEY,
        }

    def test_happy_path_removes_step_and_leaves_sentinel_marker(self) -> None:
        content = (
            "<process>\n"
            '<step name="prior">do prior</step>\n'
            '<step name="context_check">check context</step>\n'
            '<step name="later">do later</step>\n'
            "</process>\n"
        )
        new_content, records = apply_inject_operations(content, [self._op()], _resolver_from({}))
        self.assertNotIn("check context", new_content)
        self.assertIn("<!-- GSD_MODIFIER:step_removed name:context_check -->", new_content)
        self.assertIn(_start(self.KEY), new_content)
        self.assertEqual(records[0].status, "applied")

    def test_idempotency_skip_when_marker_with_sentinel_present(self) -> None:
        content = (
            "<process>\n"
            '<step name="prior">do prior</step>\n'
            + _wrap("<!-- GSD_MODIFIER:step_removed name:context_check -->", self.KEY)
            + "\n"
            '<step name="later">do later</step>\n'
            "</process>\n"
        )
        new_content, records = apply_inject_operations(content, [self._op()], _resolver_from({}))
        self.assertEqual(new_content, content)
        self.assertEqual(records[0].status, "skipped_idempotent")

    def test_fatal_anchor_not_found(self) -> None:
        content = "<process><step name=\"other\">x</step></process>\n"
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [self._op()], _resolver_from({}))
        self.assertEqual(ctx.exception.reason, "anchor_not_found")

    def test_fatal_marker_present_with_wrong_sentinel(self) -> None:
        content = (
            "<process>\n"
            + _wrap("DIFFERENT SENTINEL", self.KEY)
            + "\n</process>\n"
        )
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [self._op()], _resolver_from({}))
        self.assertEqual(ctx.exception.reason, "marker_key_conflict")


# ---------------------------------------------------------------------------
# step_insert_after
# ---------------------------------------------------------------------------


class StepInsertAfterTests(unittest.TestCase):
    KEY = "GSD_MODIFIER:test-carrier:step-insert-op"

    def _op(self) -> dict[str, Any]:
        return {
            "kind": "step_insert_after",
            "after_name": "anchor",
            "source": "src.md",
            "marker_key": self.KEY,
        }

    def test_happy_path_inserts_after_anchor_step(self) -> None:
        content = (
            "<process>\n"
            '<step name="anchor">A</step>\n'
            '<step name="later">B</step>\n'
            "</process>\n"
        )
        resolver = _resolver_from({"src.md": '<step name="injected">INJ</step>'})
        new_content, _ = apply_inject_operations(content, [self._op()], resolver)
        self.assertIn('<step name="injected">INJ</step>', new_content)
        anchor_close = new_content.find('<step name="anchor">A</step>') + len(
            '<step name="anchor">A</step>'
        )
        injected = new_content.find('<step name="injected">INJ</step>')
        self.assertLess(anchor_close, injected)

    def test_idempotency_skip_when_marker_matches(self) -> None:
        content = (
            "<process>\n"
            '<step name="anchor">A</step>\n'
            + _wrap('<step name="injected">INJ</step>', self.KEY)
            + "\n</process>\n"
        )
        resolver = _resolver_from({"src.md": '<step name="injected">INJ</step>'})
        new_content, records = apply_inject_operations(content, [self._op()], resolver)
        self.assertEqual(new_content, content)
        self.assertEqual(records[0].status, "skipped_idempotent")

    def test_fatal_anchor_not_found(self) -> None:
        content = "<process></process>\n"
        resolver = _resolver_from({"src.md": '<step name="x">x</step>'})
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [self._op()], resolver)
        self.assertEqual(ctx.exception.reason, "anchor_not_found")


# ---------------------------------------------------------------------------
# include_add
# ---------------------------------------------------------------------------


class IncludeAddTests(unittest.TestCase):
    KEY = "GSD_MODIFIER:test-carrier:include-add-op"

    def _op(self) -> dict[str, Any]:
        return {
            "kind": "include_add",
            "tag": "supporting_reading",
            "line": "@__PROJECT_ROOT__/docs/new.md",
            "marker_key": self.KEY,
        }

    def test_happy_path_inserts_line_inside_tag(self) -> None:
        content = "<supporting_reading>\n@existing\n</supporting_reading>\n"
        new_content, _ = apply_inject_operations(content, [self._op()], _resolver_from({}))
        self.assertIn("@__PROJECT_ROOT__/docs/new.md", new_content)
        # Line lands BEFORE </supporting_reading> (inside the tag)
        new_line_idx = new_content.find("@__PROJECT_ROOT__/docs/new.md")
        close_idx = new_content.find("</supporting_reading>")
        self.assertLess(new_line_idx, close_idx)

    def test_idempotency_skip_when_marker_present_with_matching_line(self) -> None:
        content = (
            "<supporting_reading>\n"
            "@existing\n"
            + _wrap("@__PROJECT_ROOT__/docs/new.md", self.KEY)
            + "\n</supporting_reading>\n"
        )
        new_content, records = apply_inject_operations(content, [self._op()], _resolver_from({}))
        self.assertEqual(new_content, content)
        self.assertEqual(records[0].status, "skipped_idempotent")

    def test_fatal_anchor_not_found(self) -> None:
        content = "<other>x</other>\n"
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [self._op()], _resolver_from({}))
        self.assertEqual(ctx.exception.reason, "anchor_not_found")


# ---------------------------------------------------------------------------
# include_remove
# ---------------------------------------------------------------------------


class IncludeRemoveTests(unittest.TestCase):
    KEY = "GSD_MODIFIER:test-carrier:include-remove-op"

    def _op(self) -> dict[str, Any]:
        return {
            "kind": "include_remove",
            "tag": "supporting_reading",
            "line": "@__PROJECT_ROOT__/docs/old.md",
            "marker_key": self.KEY,
        }

    def test_happy_path_removes_marker_block(self) -> None:
        content = (
            "<supporting_reading>\n"
            + _wrap("@__PROJECT_ROOT__/docs/old.md", self.KEY)
            + "\n</supporting_reading>\n"
        )
        new_content, records = apply_inject_operations(content, [self._op()], _resolver_from({}))
        self.assertNotIn("@__PROJECT_ROOT__/docs/old.md", new_content)
        self.assertNotIn(_start(self.KEY), new_content)
        self.assertEqual(records[0].status, "applied")

    def test_idempotency_skip_when_marker_already_absent(self) -> None:
        content = "<supporting_reading>\n@other\n</supporting_reading>\n"
        new_content, records = apply_inject_operations(content, [self._op()], _resolver_from({}))
        self.assertEqual(new_content, content)
        self.assertEqual(records[0].status, "skipped_idempotent")

    def test_fatal_when_marker_body_does_not_contain_expected_line(self) -> None:
        content = (
            "<supporting_reading>\n"
            + _wrap("@something_else", self.KEY)
            + "\n</supporting_reading>\n"
        )
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [self._op()], _resolver_from({}))
        self.assertEqual(ctx.exception.reason, "marker_key_conflict")


# ---------------------------------------------------------------------------
# block_replace
# ---------------------------------------------------------------------------


class BlockReplaceTests(unittest.TestCase):
    KEY = "GSD_MODIFIER:test-carrier:block-replace-op"

    def _op(self, *, start_anchor="START_ANCHOR", end_anchor="END_ANCHOR") -> dict[str, Any]:
        return {
            "kind": "block_replace",
            "start_anchor": start_anchor,
            "end_anchor": end_anchor,
            "source": "src.md",
            "marker_key": self.KEY,
        }

    def test_happy_path_replaces_between_anchors_preserving_them(self) -> None:
        content = "header\nSTART_ANCHOR\nold middle\nEND_ANCHOR\nfooter\n"
        resolver = _resolver_from({"src.md": "NEW CONTENT\n"})
        new_content, _ = apply_inject_operations(content, [self._op()], resolver)
        self.assertIn("START_ANCHOR", new_content)
        self.assertIn("END_ANCHOR", new_content)
        self.assertIn("NEW CONTENT", new_content)
        self.assertNotIn("old middle", new_content)

    def test_idempotency_skip_when_content_already_matches(self) -> None:
        body = "NEW CONTENT"
        content = (
            "header\nSTART_ANCHOR\n" + _wrap(body, self.KEY) + "\nEND_ANCHOR\nfooter\n"
        )
        resolver = _resolver_from({"src.md": "NEW CONTENT\n"})
        new_content, records = apply_inject_operations(content, [self._op()], resolver)
        self.assertEqual(new_content, content)
        self.assertEqual(records[0].status, "skipped_idempotent")

    def test_fatal_start_anchor_not_found(self) -> None:
        content = "no anchors here\n"
        resolver = _resolver_from({"src.md": "x"})
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [self._op()], resolver)
        self.assertEqual(ctx.exception.reason, "anchor_not_found")

    def test_fatal_end_anchor_not_found_after_start(self) -> None:
        content = "header\nSTART_ANCHOR\nbody\nfooter (no end anchor)\n"
        resolver = _resolver_from({"src.md": "x"})
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, [self._op()], resolver)
        self.assertEqual(ctx.exception.reason, "anchor_not_found")

    def test_degenerate_same_anchor_inserts_after_anchor(self) -> None:
        # Per ADR-001 §A.1 worked example: start_anchor == end_anchor →
        # the "between" region is empty; effectively insert AFTER the anchor.
        content = "before\nUNIQUE_ANCHOR\nafter\n"
        resolver = _resolver_from({"src.md": "INJECTED\n"})
        op = self._op(start_anchor="UNIQUE_ANCHOR", end_anchor="UNIQUE_ANCHOR")
        new_content, _ = apply_inject_operations(content, [op], resolver)
        self.assertIn("UNIQUE_ANCHOR", new_content)
        self.assertIn("INJECTED", new_content)
        anchor_idx = new_content.find("UNIQUE_ANCHOR")
        injected_idx = new_content.find("INJECTED")
        self.assertLess(anchor_idx, injected_idx)


# ---------------------------------------------------------------------------
# Dispatcher (apply_inject_operations) integration tests
# ---------------------------------------------------------------------------


class DispatcherIntegrationTests(unittest.TestCase):
    def test_multi_op_sequence_applies_in_declared_order(self) -> None:
        content = (
            "<process>\n"
            '<step name="a">A</step>\n'
            '<step name="anchor">ANCHOR</step>\n'
            "</process>\n"
            "<required_reading>\n@x\n</required_reading>\n"
        )
        ops = [
            {
                "kind": "step_insert_after",
                "after_name": "anchor",
                "source": "step.md",
                "marker_key": "GSD_MODIFIER:dispatch:step1",
            },
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "section.md",
                "marker_key": "GSD_MODIFIER:dispatch:section1",
            },
        ]
        resolver = _resolver_from(
            {
                "step.md": '<step name="injected">INJ</step>',
                "section.md": "EXTRA SECTION\n",
            }
        )
        new_content, records = apply_inject_operations(content, ops, resolver)
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0].op_index, 0)
        self.assertEqual(records[1].op_index, 1)
        self.assertEqual(records[0].kind, "step_insert_after")
        self.assertEqual(records[1].kind, "section_insert_after")
        self.assertIn('<step name="injected">INJ</step>', new_content)
        self.assertIn("EXTRA SECTION", new_content)

    def test_failure_mid_sequence_does_not_return_partial_result(self) -> None:
        # Pre-flight atomicity per ADR-001 §7: if any op raises, we never return
        # a partial result. The dispatcher propagates the exception.
        content = "<required_reading>\n@x\n</required_reading>\n"
        ops = [
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "ok.md",
                "marker_key": "GSD_MODIFIER:atomicity:ok",
            },
            {
                "kind": "section_insert_after",
                "tag": "nonexistent_tag",
                "source": "bad.md",
                "marker_key": "GSD_MODIFIER:atomicity:bad",
            },
        ]
        resolver = _resolver_from({"ok.md": "OK\n", "bad.md": "BAD\n"})
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, ops, resolver)
        self.assertEqual(ctx.exception.reason, "anchor_not_found")
        self.assertEqual(ctx.exception.op_index, 1)
        self.assertEqual(ctx.exception.marker_key, "GSD_MODIFIER:atomicity:bad")

    def test_source_missing_raises_with_source_missing_reason(self) -> None:
        content = "<required_reading>\n@x\n</required_reading>\n"
        ops = [
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "does_not_exist.md",
                "marker_key": "GSD_MODIFIER:missing-src:op",
            }
        ]
        resolver = _resolver_from({})
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, ops, resolver)
        self.assertEqual(ctx.exception.reason, "source_missing")
        self.assertEqual(ctx.exception.op_index, 0)

    def test_unknown_kind_raises_unknown_kind_reason(self) -> None:
        content = "x\n"
        ops = [{"kind": "not_a_real_kind", "marker_key": "GSD_MODIFIER:unknown:op"}]
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(content, ops, _resolver_from({}))
        self.assertEqual(ctx.exception.reason, "unknown_kind")

    def test_empty_operations_returns_content_unchanged(self) -> None:
        content = "untouched\n"
        new_content, records = apply_inject_operations(content, [], _resolver_from({}))
        self.assertEqual(new_content, content)
        self.assertEqual(records, [])

    def test_full_idempotency_round_trip(self) -> None:
        # Apply once, then apply the SAME ops to the result; the second pass
        # should be a complete no-op (all records skipped_idempotent).
        content = (
            "<process>\n"
            '<step name="anchor">A</step>\n'
            "</process>\n"
            "<required_reading>\n@x\n</required_reading>\n"
            "<supporting_reading>\n@y\n</supporting_reading>\n"
        )
        ops = [
            {
                "kind": "step_insert_after",
                "after_name": "anchor",
                "source": "step.md",
                "marker_key": "GSD_MODIFIER:roundtrip:step",
            },
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "section.md",
                "marker_key": "GSD_MODIFIER:roundtrip:section",
            },
            {
                "kind": "include_add",
                "tag": "supporting_reading",
                "line": "@__PROJECT_ROOT__/docs/new.md",
                "marker_key": "GSD_MODIFIER:roundtrip:include",
            },
        ]
        resolver = _resolver_from(
            {
                "step.md": '<step name="injected">INJ</step>',
                "section.md": "EXTRA\n",
            }
        )
        applied_content, first_records = apply_inject_operations(content, ops, resolver)
        self.assertTrue(all(r.status == "applied" for r in first_records))
        replayed_content, second_records = apply_inject_operations(
            applied_content, ops, resolver
        )
        self.assertEqual(replayed_content, applied_content)
        self.assertTrue(all(r.status == "skipped_idempotent" for r in second_records))


class OperationRecordContractTests(unittest.TestCase):
    def test_record_fields_populated(self) -> None:
        content = "<required_reading>\n@x\n</required_reading>\n"
        op = {
            "kind": "section_insert_after",
            "tag": "required_reading",
            "source": "src.md",
            "marker_key": "GSD_MODIFIER:record-test:op",
        }
        _, records = apply_inject_operations(
            content, [op], _resolver_from({"src.md": "Y\n"})
        )
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record.marker_key, "GSD_MODIFIER:record-test:op")
        self.assertEqual(record.kind, "section_insert_after")
        self.assertEqual(record.status, "applied")
        self.assertEqual(record.op_index, 0)

    def test_record_is_frozen(self) -> None:
        record = OperationRecord(
            marker_key="k", kind="step_remove", status="applied", op_index=0
        )
        with self.assertRaises(Exception):  # FrozenInstanceError under dataclass
            record.status = "skipped_idempotent"  # type: ignore[misc]


class MalformedOperationGuardTests(unittest.TestCase):
    def test_non_dict_operation_raises_malformed_operation(self) -> None:
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations("x\n", ["not a dict"], _resolver_from({}))  # type: ignore[list-item]
        self.assertEqual(ctx.exception.reason, "malformed_operation")

    def test_source_required_op_missing_source_raises(self) -> None:
        op = {
            "kind": "section_insert_after",
            "tag": "tag",
            "marker_key": "GSD_MODIFIER:missing-source-field:op",
        }
        with self.assertRaises(InjectOperationError) as ctx:
            apply_inject_operations(
                "<tag></tag>\n", [op], _resolver_from({})
            )
        self.assertEqual(ctx.exception.reason, "malformed_operation")


if __name__ == "__main__":
    unittest.main()
