import json
import pathlib
import tempfile
import unittest

from harness_modifier.contract import portable_gsd_contract as pgc
from harness_modifier.contract.runtime_adapters import registry as runtime_adapter_registry


class RuntimeAdapterParityTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _schema3_fixture(self, root: pathlib.Path) -> None:
        self._write(root, "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md", "Plan phase\n")
        self._write(root, "tooling/portable-gsd/overlay/skills/gsd-progress/SKILL.md", "Codex skill\n")
        self._write(
            root,
            "harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md",
            "<execution_context>\n@__PROJECT_ROOT__/.codex/get-shit-done/workflows/uplift-project.md\n</execution_context>\n",
        )
        self._write(
            root,
            "harness_modifier/overlay/commands/gsd/uplift-project.md",
            "<execution_context>\n@__PROJECT_ROOT__/.claude/get-shit-done/workflows/uplift-project.md\n</execution_context>\n",
        )
        self._write(
            root,
            "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
            json.dumps(
                {
                    "schema_version": 3,
                    "entries": {
                        "get-shit-done/workflows/plan-phase.md": {
                            "capability_id": "get-shit-done/workflows/plan-phase.md",
                            "parity_tier": "core_required",
                            "materializers": {
                                "codex": {
                                    "mode": "overwrite",
                                    "target": "get-shit-done/workflows/plan-phase.md",
                                    "source": "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md",
                                },
                                "claude": {
                                    "mode": "overwrite",
                                    "target": "get-shit-done/workflows/plan-phase.md",
                                    "source": "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md",
                                },
                            },
                        },
                        "skills/gsd-progress/SKILL.md": {
                            "capability_id": "skills/gsd-progress/SKILL.md",
                            "parity_tier": "runtime_specific",
                            "materializers": {
                                "codex": {
                                    "mode": "add",
                                    "target": "skills/gsd-progress/SKILL.md",
                                    "source": "tooling/portable-gsd/overlay/skills/gsd-progress/SKILL.md",
                                },
                            },
                        },
                        "entrypoints/gsd-uplift-project": {
                            "capability_id": "entrypoint.gsd-uplift-project",
                            "parity_tier": "core_adapted",
                            "materializers": {
                                "codex": {
                                    "mode": "add",
                                    "target": "skills/gsd-uplift-project/SKILL.md",
                                    "source": "harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md",
                                },
                                "claude": {
                                    "mode": "add",
                                    "target": "commands/gsd/uplift-project.md",
                                    "source": "harness_modifier/overlay/commands/gsd/uplift-project.md",
                                },
                            },
                        },
                    },
                }
            )
            + "\n",
        )
        self._write(root, ".codex/get-shit-done/VERSION", "1.38.3\n")
        self._write(root, ".codex/gsd-file-manifest.json", json.dumps({"version": "1.38.3"}) + "\n")
        self._write(root, ".claude/get-shit-done/VERSION", "1.38.3\n")
        self._write(root, ".claude/gsd-file-manifest.json", json.dumps({"version": "1.38.3"}) + "\n")
        self._write(
            root,
            ".codex/gsd-local-patches/backup-meta.json",
            json.dumps({"files": ["get-shit-done/workflows/plan-phase.md"]}) + "\n",
        )
        self._write(
            root,
            ".claude/gsd-local-patches/backup-meta.json",
            json.dumps({"files": ["get-shit-done/workflows/plan-phase.md"]}) + "\n",
        )
        self._write(root, ".codex/get-shit-done/workflows/plan-phase.md", "Plan phase\n")
        self._write(root, ".claude/get-shit-done/workflows/plan-phase.md", "Plan phase\n")
        self._write(root, ".codex/gsd-local-patches/get-shit-done/workflows/plan-phase.md", "upstream\n")
        self._write(root, ".claude/gsd-local-patches/get-shit-done/workflows/plan-phase.md", "upstream\n")

    def test_runtime_adapter_registry_exposes_codex_and_claude(self) -> None:
        runtimes = runtime_adapter_registry.supported_runtimes()
        self.assertEqual(runtimes, ["codex", "claude"])
        self.assertEqual(runtime_adapter_registry.get_adapter("codex").runtime_root, ".codex")
        self.assertEqual(runtime_adapter_registry.get_adapter("claude").runtime_root, ".claude")

    def test_schema3_manifest_flattens_runtime_specific_targets(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._schema3_fixture(root)

            codex_specs = pgc.load_overlay_manifest_specs(root, runtime="codex")
            claude_specs = pgc.load_overlay_manifest_specs(root, runtime="claude")

            self.assertIn("skills/gsd-uplift-project/SKILL.md", codex_specs)
            self.assertIn("commands/gsd/uplift-project.md", claude_specs)
            self.assertIn("get-shit-done/workflows/plan-phase.md", codex_specs)
            self.assertIn("get-shit-done/workflows/plan-phase.md", claude_specs)
            self.assertNotIn("skills/gsd-uplift-project/SKILL.md", claude_specs)

    def test_claude_materialization_report_accepts_shared_and_adapted_targets(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._schema3_fixture(root)

            written = pgc.apply_overlay(root, pgc.DEFAULT_COMPACT_PROMPT_FILE, runtime="claude")
            report = pgc.build_materialization_report(
                root,
                pgc.DEFAULT_COMPACT_PROMPT_FILE,
                runtime="claude",
            )

            self.assertIn("commands/gsd/uplift-project.md", written)
            self.assertEqual(report["runtime"], "claude")
            self.assertEqual(report["summary"]["content_mismatch_count"], 0)
            self.assertEqual(report["hard_failures"], [])

    def test_claude_manifest_validation_ignores_codex_only_overlay_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._schema3_fixture(root)

            report = pgc.build_manifest_validation_report(root, runtime="claude")

            self.assertEqual(report["missing_from_manifest"], [])
            self.assertEqual(report["hard_failures"], [])


if __name__ == "__main__":
    unittest.main()
