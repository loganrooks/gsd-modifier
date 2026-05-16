"""Verify-time tests for inject_operations (Phase 2 Slice 4).

Per slice spec (phases/02-contract-tools.md:85-103):
- All operations landed → pass
- Missing marker → fail
- Partial application → fail (some ops landed, others not)
- Content drifted in non-marker region → pass (modifier doesn't own that region)

Plus per-kind verify coverage and structural-corruption surfacing (Slice 3 strict path).
"""

import json
import pathlib
import tempfile
import unittest
from typing import Any

from harness_modifier.contract import inject_operations
from harness_modifier.contract import portable_gsd_contract as pgc
from harness_modifier.contract.inject_operations import (
    VERIFY_STATUS_ANCHOR_MISSING,
    VERIFY_STATUS_MARKER_CORRUPTION,
    VERIFY_STATUS_MISSING_MARKER,
    VERIFY_STATUS_OK,
    VERIFY_STATUS_UNEXPECTED_PRESENT,
    VERIFY_STATUS_WRONG_POSITION,
    verify_inject_state,
)


def _wrap(body: str, key: str) -> str:
    return (
        f"<!-- GSD_MODIFIER:start key:{key} -->\n"
        f"{body}\n"
        f"<!-- GSD_MODIFIER:end key:{key} -->"
    )


class SpecMandatedCasesTests(unittest.TestCase):
    """Per slice spec line 92: all-landed pass; missing-marker fail; partial-app
    fail; non-marker drift pass."""

    def test_all_operations_landed_passes(self) -> None:
        key_section = "GSD_MODIFIER:all-landed:section"
        key_include = "GSD_MODIFIER:all-landed:include"
        content = (
            "<required_reading>\n@x\n</required_reading>\n"
            + _wrap("INSERTED CONTENT", key_section)
            + "\n<supporting_reading>\n@y\n"
            + _wrap("@__PROJECT_ROOT__/new.md", key_include)
            + "\n</supporting_reading>\n"
        )
        ops = [
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "extra.md",
                "marker_key": key_section,
            },
            {
                "kind": "include_add",
                "tag": "supporting_reading",
                "line": "@__PROJECT_ROOT__/new.md",
                "marker_key": key_include,
            },
        ]
        result = verify_inject_state(content, ops)
        self.assertTrue(
            result.passed,
            f"expected pass; got: {[(v.status, v.detail) for v in result.operation_verifications]}",
        )
        self.assertIsNone(result.extraction_error)
        for v in result.operation_verifications:
            self.assertEqual(v.status, VERIFY_STATUS_OK)

    def test_missing_marker_fails(self) -> None:
        key = "GSD_MODIFIER:missing:op"
        # Marker not present in content at all
        content = "<required_reading>\n@x\n</required_reading>\n"
        ops = [
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "extra.md",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_MISSING_MARKER)

    def test_partial_application_fails(self) -> None:
        key_present = "GSD_MODIFIER:partial:present"
        key_absent = "GSD_MODIFIER:partial:absent"
        content = (
            "<required_reading>\n@x\n</required_reading>\n"
            + _wrap("BODY", key_present)
            + "\n<supporting_reading>\n@y\n</supporting_reading>\n"
        )
        ops = [
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "extra.md",
                "marker_key": key_present,
            },
            {
                "kind": "include_add",
                "tag": "supporting_reading",
                "line": "@__PROJECT_ROOT__/x.md",
                "marker_key": key_absent,
            },
        ]
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        # First op verified, second missing
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_OK)
        self.assertEqual(result.operation_verifications[1].status, VERIFY_STATUS_MISSING_MARKER)

    def test_non_marker_region_drift_passes(self) -> None:
        # Modifier doesn't own non-marker content; drift there is OK.
        key = "GSD_MODIFIER:nonmarker-drift:op"
        content = (
            "<header>UPSTREAM REWROTE THIS HEADER</header>\n"
            "<required_reading>\n@completely_new_upstream_include\n</required_reading>\n"
            + _wrap("OUR CONTRIBUTION", key)
            + "\n<footer>UPSTREAM ADDED A FOOTER</footer>\n"
        )
        ops = [
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "extra.md",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertTrue(result.passed)


class PerKindVerifyTests(unittest.TestCase):
    def test_section_insert_after_wrong_position_fails(self) -> None:
        # Marker exists but appears BEFORE </tag>, not after
        key = "GSD_MODIFIER:wrongpos:section"
        content = (
            _wrap("BODY", key)
            + "\n<required_reading>\n@x\n</required_reading>\n"
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
        self.assertFalse(result.passed)
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_WRONG_POSITION)

    def test_section_replace_marker_present_passes(self) -> None:
        key = "GSD_MODIFIER:sectionreplace:op"
        content = "<header/>\n" + _wrap("REPLACED BODY", key) + "\n<footer/>\n"
        ops = [
            {"kind": "section_replace", "source": "src.md", "marker_key": key}
        ]
        result = verify_inject_state(content, ops)
        self.assertTrue(result.passed)

    def test_step_remove_present_step_outside_marker_fails(self) -> None:
        key = "GSD_MODIFIER:stepremove:op"
        # Marker exists with correct sentinel BUT the original step is still elsewhere
        content = (
            "<process>\n"
            + _wrap(
                "<!-- GSD_MODIFIER:step_removed name:context_check -->", key
            )
            + "\n"
            + '<step name="context_check">still here</step>\n'
            + "</process>\n"
        )
        ops = [
            {
                "kind": "step_remove",
                "name": "context_check",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_UNEXPECTED_PRESENT)

    def test_step_remove_marker_missing_sentinel_fails(self) -> None:
        key = "GSD_MODIFIER:stepremove:bad-sentinel"
        content = (
            "<process>\n"
            + _wrap("DIFFERENT SENTINEL", key)
            + "\n</process>\n"
        )
        ops = [
            {
                "kind": "step_remove",
                "name": "context_check",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_MARKER_CORRUPTION)

    def test_step_insert_after_anchor_missing_fails(self) -> None:
        key = "GSD_MODIFIER:stepinsert:anchormissing"
        content = "<process>\n" + _wrap('<step name="injected">INJ</step>', key) + "\n</process>\n"
        ops = [
            {
                "kind": "step_insert_after",
                "after_name": "nonexistent_anchor",
                "source": "step.md",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_ANCHOR_MISSING)

    def test_step_insert_after_correctly_positioned_passes(self) -> None:
        key = "GSD_MODIFIER:stepinsert:ok"
        content = (
            "<process>\n"
            '<step name="anchor">A</step>\n'
            + _wrap('<step name="injected">INJ</step>', key)
            + "\n</process>\n"
        )
        ops = [
            {
                "kind": "step_insert_after",
                "after_name": "anchor",
                "source": "step.md",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertTrue(result.passed)

    def test_include_add_outside_tag_fails(self) -> None:
        # Marker is outside the <supporting_reading> body
        key = "GSD_MODIFIER:include:outside"
        content = (
            "<supporting_reading>\n@x\n</supporting_reading>\n"
            + _wrap("@__PROJECT_ROOT__/new.md", key)
            + "\n"
        )
        ops = [
            {
                "kind": "include_add",
                "tag": "supporting_reading",
                "line": "@__PROJECT_ROOT__/new.md",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_WRONG_POSITION)

    def test_include_add_wrong_line_in_marker_body_fails(self) -> None:
        key = "GSD_MODIFIER:include:wrongline"
        content = (
            "<supporting_reading>\n"
            + _wrap("@WRONG_LINE", key)
            + "\n</supporting_reading>\n"
        )
        ops = [
            {
                "kind": "include_add",
                "tag": "supporting_reading",
                "line": "@__PROJECT_ROOT__/expected.md",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_MARKER_CORRUPTION)

    def test_include_remove_marker_absent_passes(self) -> None:
        # Inverse semantics: include_remove expects the marker to be ABSENT post-apply
        key = "GSD_MODIFIER:includeremove:ok"
        content = "<supporting_reading>\n@y\n</supporting_reading>\n"
        ops = [
            {
                "kind": "include_remove",
                "tag": "supporting_reading",
                "line": "@__PROJECT_ROOT__/old.md",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertTrue(result.passed)
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_OK)

    def test_include_remove_marker_still_present_fails(self) -> None:
        # The apply step did NOT remove the marker, so verify fails
        key = "GSD_MODIFIER:includeremove:notremoved"
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
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_UNEXPECTED_PRESENT)

    def test_block_replace_correctly_positioned_passes(self) -> None:
        key = "GSD_MODIFIER:blockreplace:ok"
        content = (
            "before\nSTART_ANCHOR\n"
            + _wrap("REPLACEMENT", key)
            + "\nEND_ANCHOR\nafter\n"
        )
        ops = [
            {
                "kind": "block_replace",
                "start_anchor": "START_ANCHOR",
                "end_anchor": "END_ANCHOR",
                "source": "src.md",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertTrue(result.passed)

    def test_block_replace_anchor_missing_fails(self) -> None:
        key = "GSD_MODIFIER:blockreplace:anchormissing"
        content = (
            "before\n"
            + _wrap("REPLACEMENT", key)
            + "\nafter (no anchors)\n"
        )
        ops = [
            {
                "kind": "block_replace",
                "start_anchor": "MISSING_START",
                "end_anchor": "MISSING_END",
                "source": "src.md",
                "marker_key": key,
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        self.assertEqual(result.operation_verifications[0].status, VERIFY_STATUS_ANCHOR_MISSING)


class StructuralCorruptionTests(unittest.TestCase):
    """verify-time is the strict gate per ADR §8 + Slice 3 split."""

    def test_nested_markers_surface_as_extraction_error(self) -> None:
        content = (
            "<!-- GSD_MODIFIER:start key:GSD_MODIFIER:outer:op -->\n"
            "<!-- GSD_MODIFIER:start key:GSD_MODIFIER:inner:op -->\n"
            "BODY\n"
            "<!-- GSD_MODIFIER:end key:GSD_MODIFIER:inner:op -->\n"
            "<!-- GSD_MODIFIER:end key:GSD_MODIFIER:outer:op -->\n"
        )
        ops = [
            {
                "kind": "section_replace",
                "source": "src.md",
                "marker_key": "GSD_MODIFIER:outer:op",
            }
        ]
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        self.assertEqual(result.extraction_error, "nested")
        self.assertEqual(result.operation_verifications, [])

    def test_duplicate_key_in_content_surfaces_as_extraction_error(self) -> None:
        key = "GSD_MODIFIER:dup:op"
        content = _wrap("body 1", key) + "\n---\n" + _wrap("body 2", key) + "\n"
        ops = [{"kind": "section_replace", "source": "src.md", "marker_key": key}]
        result = verify_inject_state(content, ops)
        self.assertFalse(result.passed)
        self.assertEqual(result.extraction_error, "duplicate_key")


class VerifyResultContractTests(unittest.TestCase):
    def test_empty_operations_returns_passed_true(self) -> None:
        content = "anything\n"
        result = verify_inject_state(content, [])
        self.assertTrue(result.passed)
        self.assertEqual(result.operation_verifications, [])
        self.assertIsNone(result.extraction_error)

    def test_operation_verifications_are_in_op_index_order(self) -> None:
        key_a = "GSD_MODIFIER:order:a"
        key_b = "GSD_MODIFIER:order:b"
        content = (
            "<required_reading>\n@x\n</required_reading>\n"
            + _wrap("A", key_a)
            + "\n<supporting_reading>\n"
            + _wrap("@__PROJECT_ROOT__/b.md", key_b)
            + "\n</supporting_reading>\n"
        )
        ops = [
            {
                "kind": "section_insert_after",
                "tag": "required_reading",
                "source": "a.md",
                "marker_key": key_a,
            },
            {
                "kind": "include_add",
                "tag": "supporting_reading",
                "line": "@__PROJECT_ROOT__/b.md",
                "marker_key": key_b,
            },
        ]
        result = verify_inject_state(content, ops)
        self.assertEqual(len(result.operation_verifications), 2)
        self.assertEqual(result.operation_verifications[0].op_index, 0)
        self.assertEqual(result.operation_verifications[1].op_index, 1)

    def test_result_is_frozen(self) -> None:
        result = verify_inject_state("x\n", [])
        with self.assertRaises(Exception):
            result.passed = False  # type: ignore[misc]


class MaterializationReportIntegrationTests(unittest.TestCase):
    """build_materialization_report wires verify_inject_state in via inject entries."""

    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _setup_v4_inject_manifest(self, root: pathlib.Path, marker_key: str) -> None:
        manifest = {
            "schema_version": 4,
            "entries": {
                "agents/injected.md": {
                    "capability_id": "agents/injected.md",
                    "parity_tier": "core_required",
                    "parity_intent": "outcome_aligned",
                    "materializers": {
                        runtime: {
                            "mode": "inject",
                            "target": "agents/injected.md",
                            "operations": [
                                {
                                    "kind": "section_insert_after",
                                    "tag": "required_reading",
                                    "source": "tooling/portable-gsd/overlay/extra.md",
                                    "marker_key": marker_key,
                                }
                            ],
                        }
                        for runtime in ("codex", "claude")
                    },
                }
            },
        }
        self._write(
            root, pgc.OVERLAY_MANIFEST_REL_PATH, json.dumps(manifest, indent=2) + "\n"
        )

    def test_materialization_report_passes_for_correctly_landed_inject(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            key = "GSD_MODIFIER:integration:landed"
            self._setup_v4_inject_manifest(repo_root, key)
            # The on-disk target has the marker landed
            self._write(
                repo_root,
                ".codex/agents/injected.md",
                "<required_reading>\n@x\n</required_reading>\n"
                + _wrap("INSERTED CONTENT", key)
                + "\n",
            )
            self._write(
                repo_root,
                ".claude/agents/injected.md",
                "<required_reading>\n@x\n</required_reading>\n"
                + _wrap("INSERTED CONTENT", key)
                + "\n",
            )
            report = pgc.build_materialization_report(repo_root, compact_prompt="x")
            self.assertEqual(report["inject_failures"], [])
            self.assertEqual(report["summary"]["inject_failure_count"], 0)
            self.assertEqual(report["summary"]["inject_entry_count"], 1)
            self.assertTrue(report["inject_verifications"][0]["passed"])

    def test_materialization_report_surfaces_missing_inject_marker_as_hard_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            key = "GSD_MODIFIER:integration:missing"
            self._setup_v4_inject_manifest(repo_root, key)
            # On-disk target lacks the expected marker
            self._write(
                repo_root,
                ".codex/agents/injected.md",
                "<required_reading>\n@x\n</required_reading>\nNO MARKER HERE\n",
            )
            report = pgc.build_materialization_report(repo_root, compact_prompt="x")
            self.assertEqual(report["summary"]["inject_failure_count"], 1)
            self.assertTrue(
                any("verify_inject_state" in f for f in report["hard_failures"]),
                f"expected hard_failure to mention verify_inject_state; got: {report['hard_failures']}",
            )


if __name__ == "__main__":
    unittest.main()
