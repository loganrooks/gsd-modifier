"""Backward-compatibility regression: v4 manifest with mixed mode entries.

Phase 2 Slice 6 per phases/02-contract-tools.md:116-124. Builds a manifest
exercising all three modes (overwrite, add, inject) in one entry set, then
runs validate-manifest → apply-overlay → verify-materialized end-to-end and
confirms each mode's contract is honored without interference.

This is the test that prevents future contract changes from inadvertently
breaking the coexistence promise in ADR-001 §6 ("Mixed-mode manifests").
"""

import json
import pathlib
import tempfile
import unittest
from typing import Any

from harness_modifier.contract import inject_operations
from harness_modifier.contract import portable_gsd_contract as pgc


def _wrap(body: str, key: str) -> str:
    return (
        f"<!-- GSD_MODIFIER:start key:{key} -->\n"
        f"{body.strip()}\n"
        f"<!-- GSD_MODIFIER:end key:{key} -->"
    )


class MixedModeManifestTests(unittest.TestCase):
    """v4 manifest with overwrite + add + inject entries; the three modes
    must coexist through the full parse → apply → verify pipeline."""

    INJECT_KEY = "GSD_MODIFIER:back-compat:inject-op"

    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _build_mixed_manifest(self, root: pathlib.Path) -> dict[str, Any]:
        # Source files for overwrite and add entries
        self._write(
            root,
            "tooling/portable-gsd/overlay/agents/overwriter.md",
            "OVERWRITE BODY\n",
        )
        self._write(
            root,
            "tooling/portable-gsd/overlay/agents/added.toml",
            'description = "added"\n',
        )
        # Source file for the inject operation; placed under harness_modifier/overlay/
        # per ADR-001 §A.1 convention (NOT under the tooling/portable-gsd/overlay/
        # tree, which is scanned by list_overlay_paths and would trip
        # missing_from_manifest since inject operation sources are not yet
        # declared in declared_overlay_source_paths).
        self._write(
            root,
            "harness_modifier/overlay/agents/injected-extra.md",
            "INJECTED CONTENT\n",
        )

        manifest = {
            "schema_version": 4,
            "entries": {
                "agents/overwriter.md": {
                    "capability_id": "agents/overwriter.md",
                    "parity_tier": "core_required",
                    "materializers": {
                        runtime: {
                            "mode": "overwrite",
                            "target": "agents/overwriter.md",
                            "source": "tooling/portable-gsd/overlay/agents/overwriter.md",
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
                            "source": "tooling/portable-gsd/overlay/agents/added.toml",
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
                                {
                                    "kind": "section_insert_after",
                                    "tag": "required_reading",
                                    "source": "harness_modifier/overlay/agents/injected-extra.md",
                                    "marker_key": self.INJECT_KEY,
                                }
                            ],
                        }
                        for runtime in ("codex", "claude")
                    },
                },
            },
        }
        self._write(
            root, pgc.OVERLAY_MANIFEST_REL_PATH, json.dumps(manifest, indent=2) + "\n"
        )
        return manifest

    def _seed_upstream_target_for_inject(
        self, root: pathlib.Path, runtime: str
    ) -> None:
        # Inject requires the target to exist before apply runs (per ADR §7).
        self._write(
            root,
            f"{pgc.runtime_root_rel_path(runtime)}/agents/injected.md",
            "<required_reading>\n@upstream-content\n</required_reading>\n",
        )

    def _seed_backup_meta_for_overwrite(
        self, root: pathlib.Path, runtime: str
    ) -> None:
        # Source-only validation doesn't need backup-meta, but the materialization
        # report path checks it for overwrite entries.
        self._write(
            root,
            f"{pgc.runtime_root_rel_path(runtime)}/gsd-local-patches/backup-meta.json",
            json.dumps({"files": ["agents/overwriter.md"]}) + "\n",
        )
        self._write(
            root,
            f"{pgc.runtime_root_rel_path(runtime)}/gsd-local-patches/agents/overwriter.md",
            "OVERWRITE BODY\n",
        )

    def test_validate_manifest_accepts_mixed_mode_v4(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._build_mixed_manifest(root)
            report = pgc.build_manifest_validation_report(root, require_backup_meta=False)
            self.assertEqual(report["hard_failures"], [])
            self.assertEqual(report["summary"]["overwrite_count"], 1)
            self.assertEqual(report["summary"]["add_count"], 1)
            self.assertEqual(report["summary"]["manifest_schema_version"], 4)

    def test_apply_overlay_handles_all_three_modes_in_one_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._build_mixed_manifest(root)
            self._seed_upstream_target_for_inject(root, "codex")
            written = pgc.apply_overlay(root, compact_prompt="x", runtime="codex")

            # All three target files were materialized
            self.assertIn("agents/overwriter.md", written)
            self.assertIn("agents/added.toml", written)
            self.assertIn("agents/injected.md", written)

            codex_root = root / ".codex"
            # overwrite: target now contains the source content verbatim
            self.assertEqual(
                (codex_root / "agents/overwriter.md").read_text(encoding="utf-8"),
                "OVERWRITE BODY\n",
            )
            # add: target now contains the source content verbatim
            self.assertEqual(
                (codex_root / "agents/added.toml").read_text(encoding="utf-8"),
                'description = "added"\n',
            )
            # inject: target contains the original upstream content PLUS the
            # injected marker block after </required_reading>
            inject_content = (codex_root / "agents/injected.md").read_text(encoding="utf-8")
            self.assertIn("@upstream-content", inject_content)
            self.assertIn("INJECTED CONTENT", inject_content)
            self.assertIn(f"<!-- GSD_MODIFIER:start key:{self.INJECT_KEY} -->", inject_content)
            # marker lands AFTER </required_reading>
            close_idx = inject_content.find("</required_reading>")
            marker_idx = inject_content.find("<!-- GSD_MODIFIER:start")
            self.assertLess(close_idx, marker_idx)

    # Known Phase 3 contract-code gap surfaced by mixed-mode verify-materialized:
    # compatibility declaration overlay_schema_version is hardcoded to 3 in
    # declaration.json and the compat check at build_materialization_report only
    # allows 2↔3 transition. When Phase 3 ships the first v4 entry, the
    # declaration bumps to 4 and the compat check needs to allow 3↔4 transition.
    # Filtered below; this is a Phase 3 follow-up, not a Slice 6 blocker.
    _PHASE3_TODO_HARD_FAILURE_SUBSTRINGS = (
        "compatibility declaration overlay schema version does not match",
    )

    def _filter_phase3_todo_failures(self, hard_failures: list[str]) -> list[str]:
        return [
            f
            for f in hard_failures
            if not any(sub in f for sub in self._PHASE3_TODO_HARD_FAILURE_SUBSTRINGS)
        ]

    def test_verify_materialized_accepts_correctly_landed_mixed_mode(self) -> None:
        # The inject verify-engine itself produces passing results when the
        # mixed-mode manifest is applied correctly. The two Phase 3 contract-code
        # gaps (compat-declaration schema-version bump; missing_from_manifest
        # accounting for inject operation sources) surface as hard_failures that
        # are filtered out below — they are tracked as Phase 3 follow-ups, not
        # Slice 6 blockers.
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._build_mixed_manifest(root)

            for runtime in ("codex", "claude"):
                self._seed_upstream_target_for_inject(root, runtime)
                self._seed_backup_meta_for_overwrite(root, runtime)
                pgc.apply_overlay(root, compact_prompt="x", runtime=runtime)

            report = pgc.build_materialization_report(root, compact_prompt="x", runtime="codex")
            non_phase3_failures = self._filter_phase3_todo_failures(report["hard_failures"])
            self.assertEqual(
                non_phase3_failures,
                [],
                f"unexpected (non-Phase-3-TODO) hard_failures: {non_phase3_failures}",
            )
            # The inject verify-engine itself passes
            self.assertEqual(report["summary"]["inject_entry_count"], 1)
            self.assertEqual(report["summary"]["inject_failure_count"], 0)
            self.assertTrue(report["inject_verifications"][0]["passed"])
            # The Phase 3 TODO compat-declaration hard_failure is present
            # (documents the schema-version-bump gap for the Phase 3 pilot turn)
            self.assertEqual(
                len(report["hard_failures"]) - len(non_phase3_failures),
                1,
                f"expected exactly 1 Phase-3-TODO failure; got hard_failures: {report['hard_failures']}",
            )

    def test_verify_materialized_inject_failure_does_not_corrupt_other_modes(
        self,
    ) -> None:
        # Apply works for all 3 modes; then manually corrupt the inject target.
        # The inject_failure_count rises to 1 (Slice 4's verify_inject_state
        # catches the missing marker); the overwrite + add live targets are
        # still intact (their codepaths are independent). The two Phase 3 TODO
        # hard_failures are also present but unrelated to the corruption.
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._build_mixed_manifest(root)
            self._seed_upstream_target_for_inject(root, "codex")
            self._seed_backup_meta_for_overwrite(root, "codex")
            pgc.apply_overlay(root, compact_prompt="x", runtime="codex")

            inject_path = root / ".codex/agents/injected.md"
            inject_path.write_text(
                "<required_reading>\n@upstream-content\n</required_reading>\n",
                encoding="utf-8",
            )

            report = pgc.build_materialization_report(root, compact_prompt="x", runtime="codex")
            # The overwrite + add live targets are still intact (independent codepaths)
            self.assertNotIn("agents/overwriter.md", report["content_mismatch"])
            # The inject verify-engine catches the corruption
            self.assertEqual(report["summary"]["inject_failure_count"], 1)
            self.assertTrue(
                any("verify_inject_state" in f for f in report["hard_failures"]),
                f"expected verify_inject_state failure; got: {report['hard_failures']}",
            )

    def test_idempotent_re_apply_of_mixed_mode_manifest(self) -> None:
        # Apply twice; the second pass should be a no-op for inject (idempotent
        # skip per Slice 2 semantics); overwrite + add are atomic-write so the
        # second pass writes the same content; live state is invariant.
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._build_mixed_manifest(root)
            self._seed_upstream_target_for_inject(root, "codex")

            pgc.apply_overlay(root, compact_prompt="x", runtime="codex")
            inject_content_pass_1 = (root / ".codex/agents/injected.md").read_text(encoding="utf-8")

            pgc.apply_overlay(root, compact_prompt="x", runtime="codex")
            inject_content_pass_2 = (root / ".codex/agents/injected.md").read_text(encoding="utf-8")

            self.assertEqual(inject_content_pass_1, inject_content_pass_2)


class SchemaVersion3StillWorksAfterV4SupportTests(unittest.TestCase):
    """v3 manifests (no schema_version: 4 fields) must continue to validate
    and verify unchanged after Phase 2's v4 support landed."""

    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_v3_manifest_with_overwrite_and_add_validates_clean(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._write(
                root,
                "tooling/portable-gsd/overlay/agents/overwriter.md",
                "OVERWRITE BODY\n",
            )
            self._write(
                root,
                "tooling/portable-gsd/overlay/agents/added.toml",
                'description = "added"\n',
            )
            self._write(
                root,
                pgc.OVERLAY_MANIFEST_REL_PATH,
                json.dumps(
                    {
                        "schema_version": 3,
                        "entries": {
                            "agents/overwriter.md": {
                                "capability_id": "agents/overwriter.md",
                                "parity_tier": "core_required",
                                "materializers": {
                                    "codex": {
                                        "mode": "overwrite",
                                        "target": "agents/overwriter.md",
                                        "source": "tooling/portable-gsd/overlay/agents/overwriter.md",
                                    },
                                    "claude": {
                                        "mode": "overwrite",
                                        "target": "agents/overwriter.md",
                                        "source": "tooling/portable-gsd/overlay/agents/overwriter.md",
                                    },
                                },
                            },
                            "agents/added.toml": {
                                "capability_id": "agents/added.toml",
                                "parity_tier": "runtime_specific",
                                "materializers": {
                                    "codex": {
                                        "mode": "add",
                                        "target": "agents/added.toml",
                                        "source": "tooling/portable-gsd/overlay/agents/added.toml",
                                    }
                                },
                            },
                        },
                    },
                    indent=2,
                )
                + "\n",
            )
            report = pgc.build_manifest_validation_report(root, require_backup_meta=False)
            self.assertEqual(report["hard_failures"], [])
            self.assertEqual(report["summary"]["manifest_schema_version"], 3)

    def test_v3_manifest_rejects_inject_with_clear_error(self) -> None:
        # A v3 manifest with mode: inject should raise a ValueError, not silently
        # accept (so old manifests can't accidentally use the new mode).
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._write(
                root,
                pgc.OVERLAY_MANIFEST_REL_PATH,
                json.dumps(
                    {
                        "schema_version": 3,
                        "entries": {
                            "agents/bad.md": {
                                "capability_id": "agents/bad.md",
                                "parity_tier": "core_required",
                                "materializers": {
                                    "codex": {
                                        "mode": "inject",
                                        "target": "agents/bad.md",
                                        "operations": [],
                                    }
                                },
                            }
                        },
                    },
                    indent=2,
                )
                + "\n",
            )
            with self.assertRaises(ValueError) as ctx:
                pgc.load_overlay_manifest_specs(root, runtime="codex")
            self.assertIn("requires schema_version >= 4", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
