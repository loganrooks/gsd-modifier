"""Smoke tests for OVERLAY-MANIFEST.json schema v4 (`mode: inject`) parser path.

Phase 2 Slice 1 boundary: parser-only. These tests exercise schema recognition,
per-operation validation, marker_key uniqueness, and parity_intent requirements.
Apply-time and verify-time inject logic land in Phase 2 Slices 2-4.
"""

import json
import pathlib
import tempfile
import unittest
from typing import Any

from harness_modifier.contract import inject_operations
from harness_modifier.contract import portable_gsd_contract as pgc


def _write_json(root: pathlib.Path, rel_path: str, payload: Any) -> None:
    path = root / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _build_inject_op(
    *, kind: str = "block_replace", marker_key: str | None = None, **extra: Any
) -> dict[str, Any]:
    if marker_key is None:
        marker_key = "GSD_MODIFIER:test-carrier:default-op"
    op: dict[str, Any] = {"kind": kind, "marker_key": marker_key}
    if kind == "section_insert_after":
        op.setdefault("tag", "required_reading")
        op.setdefault("source", "harness_modifier/overlay/x.md")
    elif kind == "section_replace":
        op.setdefault("source", "harness_modifier/overlay/x.md")
    elif kind == "step_remove":
        op.setdefault("name", "context_check")
    elif kind == "step_insert_after":
        op.setdefault("after_name", "anchor_step")
        op.setdefault("source", "harness_modifier/overlay/x.md")
    elif kind == "include_add":
        op.setdefault("tag", "supporting_reading")
        op.setdefault("line", "@__PROJECT_ROOT__/docs/x.md")
    elif kind == "include_remove":
        op.setdefault("tag", "supporting_reading")
        op.setdefault("line", "@__PROJECT_ROOT__/docs/x.md")
    elif kind == "block_replace":
        op.setdefault("start_anchor", "start-text")
        op.setdefault("end_anchor", "end-text")
        op.setdefault("source", "harness_modifier/overlay/x.md")
    op.update(extra)
    return op


def _v4_manifest_with_inject_entry(
    *,
    entry_id: str = "agents/sample.md",
    parity_intent: str | None = "outcome_aligned",
    parity_tier: str = "core_required",
    op: dict[str, Any] | None = None,
    runtimes: tuple[str, ...] = ("codex", "claude"),
) -> dict[str, Any]:
    op = op or _build_inject_op()
    entry: dict[str, Any] = {
        "capability_id": entry_id,
        "parity_tier": parity_tier,
        "materializers": {
            runtime: {
                "mode": "inject",
                "target": entry_id,
                "operations": [op],
            }
            for runtime in runtimes
        },
    }
    if parity_intent is not None:
        entry["parity_intent"] = parity_intent
    return {"schema_version": 4, "entries": {entry_id: entry}}


class V4SchemaParserTests(unittest.TestCase):
    def test_v4_manifest_with_inject_entry_parses_cleanly(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            _write_json(
                repo_root,
                pgc.OVERLAY_MANIFEST_REL_PATH,
                _v4_manifest_with_inject_entry(),
            )

            specs = pgc.load_overlay_manifest_specs(repo_root, runtime="codex")

            self.assertIn("agents/sample.md", specs)
            spec = specs["agents/sample.md"]
            self.assertEqual(spec["mode"], "inject")
            self.assertEqual(spec["source_path"], "")
            self.assertEqual(spec["source_rel_path"], "")
            self.assertEqual(len(spec["operations"]), 1)
            self.assertEqual(spec["operations"][0]["kind"], "block_replace")

    def test_validate_manifest_accepts_v4_inject_entry(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            _write_json(
                repo_root,
                pgc.OVERLAY_MANIFEST_REL_PATH,
                _v4_manifest_with_inject_entry(),
            )

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertEqual(report["hard_failures"], [])
            self.assertEqual(report["summary"]["manifest_schema_version"], 4)

    def test_v4_manifest_rejects_inject_entry_without_parity_intent(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            _write_json(
                repo_root,
                pgc.OVERLAY_MANIFEST_REL_PATH,
                _v4_manifest_with_inject_entry(parity_intent=None),
            )

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertTrue(
                any("missing parity_intent" in failure for failure in report["hard_failures"]),
                f"expected missing-parity_intent failure; got: {report['hard_failures']}",
            )

    def test_v4_manifest_rejects_invalid_parity_intent_value(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            _write_json(
                repo_root,
                pgc.OVERLAY_MANIFEST_REL_PATH,
                _v4_manifest_with_inject_entry(parity_intent="bogus_value"),
            )

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertTrue(
                any("invalid parity_intent" in f for f in report["hard_failures"]),
                f"expected invalid-parity_intent failure; got: {report['hard_failures']}",
            )

    def test_v4_manifest_rejects_operation_with_unknown_kind(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            bad_op = {"kind": "nonexistent_kind", "marker_key": "GSD_MODIFIER:test:bad"}
            _write_json(
                repo_root,
                pgc.OVERLAY_MANIFEST_REL_PATH,
                _v4_manifest_with_inject_entry(op=bad_op),
            )

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertTrue(
                any("invalid kind 'nonexistent_kind'" in f for f in report["hard_failures"]),
                f"expected invalid-kind failure; got: {report['hard_failures']}",
            )

    def test_v4_manifest_rejects_operation_missing_required_field(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            bad_op = {
                "kind": "section_insert_after",
                "marker_key": "GSD_MODIFIER:test:missing-field",
                "source": "harness_modifier/overlay/x.md",
            }
            _write_json(
                repo_root,
                pgc.OVERLAY_MANIFEST_REL_PATH,
                _v4_manifest_with_inject_entry(op=bad_op),
            )

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertTrue(
                any("missing or non-string 'tag' field" in f for f in report["hard_failures"]),
                f"expected missing-tag failure; got: {report['hard_failures']}",
            )

    def test_v4_manifest_rejects_operation_with_missing_marker_key(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            bad_op = {"kind": "step_remove", "name": "x"}
            _write_json(
                repo_root,
                pgc.OVERLAY_MANIFEST_REL_PATH,
                _v4_manifest_with_inject_entry(op=bad_op),
            )

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertTrue(
                any("missing or non-string marker_key" in f for f in report["hard_failures"]),
                f"expected missing-marker_key failure; got: {report['hard_failures']}",
            )

    def test_v4_manifest_rejects_marker_key_with_invalid_format(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            bad_op = _build_inject_op(marker_key="not-a-valid-key")
            _write_json(
                repo_root,
                pgc.OVERLAY_MANIFEST_REL_PATH,
                _v4_manifest_with_inject_entry(op=bad_op),
            )

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertTrue(
                any("does not match required pattern" in f for f in report["hard_failures"]),
                f"expected marker_key-format failure; got: {report['hard_failures']}",
            )

    def test_v4_manifest_rejects_duplicate_marker_key_across_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            shared_key = "GSD_MODIFIER:duplicate-key:test"
            payload = {
                "schema_version": 4,
                "entries": {
                    "agents/first.md": {
                        "capability_id": "agents/first.md",
                        "parity_tier": "core_required",
                        "parity_intent": "outcome_aligned",
                        "materializers": {
                            runtime: {
                                "mode": "inject",
                                "target": "agents/first.md",
                                "operations": [_build_inject_op(marker_key=shared_key)],
                            }
                            for runtime in ("codex", "claude")
                        },
                    },
                    "agents/second.md": {
                        "capability_id": "agents/second.md",
                        "parity_tier": "core_required",
                        "parity_intent": "outcome_aligned",
                        "materializers": {
                            runtime: {
                                "mode": "inject",
                                "target": "agents/second.md",
                                "operations": [_build_inject_op(marker_key=shared_key)],
                            }
                            for runtime in ("codex", "claude")
                        },
                    },
                },
            }
            _write_json(repo_root, pgc.OVERLAY_MANIFEST_REL_PATH, payload)

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertTrue(
                any("used by multiple entries" in f for f in report["hard_failures"]),
                f"expected cross-entry marker_key collision; got: {report['hard_failures']}",
            )

    def test_v4_manifest_rejects_intra_runtime_duplicate_marker_key(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            shared_key = "GSD_MODIFIER:same-entry:dup"
            payload = {
                "schema_version": 4,
                "entries": {
                    "agents/sample.md": {
                        "capability_id": "agents/sample.md",
                        "parity_tier": "runtime_specific",
                        "parity_intent": "runtime_independent",
                        "materializers": {
                            "codex": {
                                "mode": "inject",
                                "target": "agents/sample.md",
                                "operations": [
                                    _build_inject_op(marker_key=shared_key),
                                    _build_inject_op(
                                        kind="include_add", marker_key=shared_key
                                    ),
                                ],
                            }
                        },
                    }
                },
            }
            _write_json(repo_root, pgc.OVERLAY_MANIFEST_REL_PATH, payload)

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertTrue(
                any(
                    "appears 2 times in operations list" in f
                    for f in report["hard_failures"]
                ),
                f"expected intra-runtime duplicate failure; got: {report['hard_failures']}",
            )

    def test_v4_manifest_allows_shared_marker_key_across_runtimes_within_entry(self) -> None:
        # outcome_aligned semantics: codex + claude both declare the same operation
        # with the same marker_key (intentional mirroring per ADR-001 §5).
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            shared_key = "GSD_MODIFIER:shared-mirror:op"
            payload = _v4_manifest_with_inject_entry(
                op=_build_inject_op(marker_key=shared_key),
            )
            _write_json(repo_root, pgc.OVERLAY_MANIFEST_REL_PATH, payload)

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertEqual(
                report["hard_failures"],
                [],
                f"outcome_aligned mirroring should not flag duplicate marker_key; got: {report['hard_failures']}",
            )

    def test_v3_manifest_rejects_mode_inject(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            payload = _v4_manifest_with_inject_entry()
            payload["schema_version"] = 3
            _write_json(repo_root, pgc.OVERLAY_MANIFEST_REL_PATH, payload)

            with self.assertRaises(ValueError) as ctx:
                pgc.load_overlay_manifest_specs(repo_root, runtime="codex")

            self.assertIn("requires schema_version >= 4", str(ctx.exception))

    def test_v4_manifest_with_mixed_modes(self) -> None:
        # An overwrite + add + inject mixed manifest validates as long as each entry
        # is independently well-formed.
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            source_rel = "tooling/portable-gsd/overlay/agents/overwriter.md"
            (repo_root / source_rel).parent.mkdir(parents=True, exist_ok=True)
            (repo_root / source_rel).write_text("overwriter body\n", encoding="utf-8")
            add_source_rel = "tooling/portable-gsd/overlay/agents/added.toml"
            (repo_root / add_source_rel).parent.mkdir(parents=True, exist_ok=True)
            (repo_root / add_source_rel).write_text("added\n", encoding="utf-8")
            payload = {
                "schema_version": 4,
                "entries": {
                    "agents/overwriter.md": {
                        "capability_id": "agents/overwriter.md",
                        "parity_tier": "core_required",
                        "materializers": {
                            runtime: {
                                "mode": "overwrite",
                                "target": "agents/overwriter.md",
                                "source": source_rel,
                            }
                            for runtime in ("codex", "claude")
                        },
                    },
                    "agents/added.toml": {
                        "capability_id": "agents/added.toml",
                        "parity_tier": "runtime_specific",
                        "materializers": {
                            "codex": {
                                "mode": "add",
                                "target": "agents/added.toml",
                                "source": add_source_rel,
                            }
                        },
                    },
                    "agents/injected.md": {
                        "capability_id": "agents/injected.md",
                        "parity_tier": "core_required",
                        "parity_intent": "outcome_aligned",
                        "materializers": {
                            runtime: {
                                "mode": "inject",
                                "target": "agents/injected.md",
                                "operations": [
                                    _build_inject_op(
                                        marker_key="GSD_MODIFIER:mixed-mode-test:inject-op"
                                    )
                                ],
                            }
                            for runtime in ("codex", "claude")
                        },
                    },
                },
            }
            _write_json(repo_root, pgc.OVERLAY_MANIFEST_REL_PATH, payload)

            report = pgc.build_manifest_validation_report(repo_root, require_backup_meta=False)

            self.assertEqual(report["hard_failures"], [])
            self.assertEqual(report["summary"]["overwrite_count"], 1)
            self.assertEqual(report["summary"]["add_count"], 1)


class PerOperationKindValidatorTests(unittest.TestCase):
    """Each operation kind's validator gets exercised for happy + sad paths."""

    def _validate(self, op: dict[str, Any]) -> list[str]:
        return inject_operations.validate_operation(op, op_id="test-op")

    def test_section_insert_after_happy_path(self) -> None:
        self.assertEqual(self._validate(_build_inject_op(kind="section_insert_after")), [])

    def test_section_replace_happy_path(self) -> None:
        self.assertEqual(self._validate(_build_inject_op(kind="section_replace")), [])

    def test_step_remove_happy_path(self) -> None:
        self.assertEqual(self._validate(_build_inject_op(kind="step_remove")), [])

    def test_step_insert_after_happy_path(self) -> None:
        self.assertEqual(self._validate(_build_inject_op(kind="step_insert_after")), [])

    def test_include_add_happy_path(self) -> None:
        self.assertEqual(self._validate(_build_inject_op(kind="include_add")), [])

    def test_include_remove_happy_path(self) -> None:
        self.assertEqual(self._validate(_build_inject_op(kind="include_remove")), [])

    def test_block_replace_happy_path(self) -> None:
        self.assertEqual(self._validate(_build_inject_op(kind="block_replace")), [])

    def test_marker_key_pattern_accepts_documented_examples(self) -> None:
        examples = [
            "GSD_MODIFIER:workflows-new-project:supporting-reading",
            "GSD_MODIFIER:workflows-health:remove-context-check",
            "GSD_MODIFIER:references-mandatory-initial-read:add-content",
            "GSD_MODIFIER:references-mandatory-initial-read:extended-content",
        ]
        for example in examples:
            self.assertEqual(
                inject_operations.validate_marker_key(example, "test-op"),
                [],
                f"ADR-001 §4 example {example!r} should validate",
            )

    def test_marker_key_pattern_rejects_uppercase_and_missing_segments(self) -> None:
        bad = [
            "",
            "GSD_MODIFIER:",
            "GSD_MODIFIER:only-one-segment",
            "GSD_MODIFIER:UPPER:case",
            "wrong-prefix:carrier:op",
        ]
        for example in bad:
            errors = inject_operations.validate_marker_key(example, "test-op")
            self.assertNotEqual(errors, [], f"{example!r} should NOT validate")

    def test_operation_kinds_match_adr_catalog(self) -> None:
        # Sanity check: the 7 kinds enumerated in ADR-001 §3 catalog.
        self.assertEqual(
            inject_operations.OPERATION_KINDS,
            frozenset(
                {
                    "section_insert_after",
                    "section_replace",
                    "step_remove",
                    "step_insert_after",
                    "include_add",
                    "include_remove",
                    "block_replace",
                }
            ),
        )


if __name__ == "__main__":
    unittest.main()
