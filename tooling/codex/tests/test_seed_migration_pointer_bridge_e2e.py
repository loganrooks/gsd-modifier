import json
import pathlib
import tempfile
import unittest

from tooling.codex import project_uplift as pu
from tooling.codex import seed_migration_inventory as smi


ROOT = pathlib.Path(__file__).resolve().parents[3]
FIXTURE_PATH = ROOT / ".planning" / "audits" / "2026-04-18-readiness-rerun-debrief-and-redesign" / "propagation-audit" / "artifacts" / "07-seed-migration-manifest-shape-fixture.json"


STATE_TEMPLATE = """---
gsd_state_version: 1.0
status: completed
last_updated: "2026-04-22T12:00:00+00:00"
---

# Project State

## Current Position

Status: completed

## Session Continuity

Last session: 2026-04-22T12:00:00+00:00
Stopped at: test
Resume file: None
"""


class SeedMigrationPointerBridgeE2ETests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _minimal_project(self, root: pathlib.Path) -> None:
        self._write(root, ".planning/PROJECT.md", "# Project\n")
        self._write(root, ".planning/ROADMAP.md", "# Roadmap\n")
        self._write(root, ".planning/STATE.md", STATE_TEMPLATE)
        self._write(root, "AGENTS.md", "# Agents\n")
        self._write(root, ".planning/AGENTS.md", "# Planning Agents\n")
        self._write(root, "CLAUDE.md", "# Claude\n")
        self._write(root, ".planning/CLAUDE.md", "# Planning Claude\n")
        self._write(root, ".planning/CLAIM-TYPES.md", "# Claim Types\n")
        self._write(root, ".planning/LONG-ARC.md", "---\ndocument: LONG-ARC\nstatus: canonical\n---\n\n# Long Arc\n")
        self._write(root, ".codex/config.toml", 'model = "gpt-5.4"\n')
        self._write(root, ".codex/gsd-file-manifest.json", json.dumps({"version": "1.38.1"}) + "\n")
        self._write(root, ".codex/get-shit-done/VERSION", "1.38.1\n")
        self._write(root, ".codex/agents/gsd-planner.toml", 'description = "planner"\n')
        self._write(root, ".codex/agents/gsd-plan-checker.toml", 'description = "checker"\n')
        self._write(root, "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json", json.dumps({"schema_version": 2, "entries": {}}) + "\n")
        self._write(
            root,
            "tooling/codex/README.md",
            "# Codex Tooling Notes\n\n## Utilities\n- `audit_refmap.py`\n- `project_uplift.py`\n",
        )
        self._write(
            root,
            "tooling/codex/UPLIFT-HELD-LATER.md",
            "- required-reading installation practice — held\n"
            "- cross-runtime uplift composition — held\n"
            "- upstream-template drift machinery — held\n"
            "- aged-bespoke deep merge — held\n"
            "- audit-subtree aging carry — held\n"
            "- legacy seed corpus migration — partially landed: harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md | intervention-proposals/90-seed-migration-operator-facing-pointer-bridge-implementation.md | propagation-audit/37-seed-migration-operator-facing-pointer-change-triggered-refresh.md\n"
            "- routed-entry hooks beyond `progress` — partially landed: propagation-audit/04-resume-project-second-consumer-implementation.md\n",
        )
        self._write(
            root,
            ".codex/get-shit-done/workflows/discuss-phase.md",
            "# Discuss\n\n### Strengthening Opportunities\n- Keep this route.\n",
        )
        self._write(
            root,
            ".codex/get-shit-done/templates/context.md",
            "# Context\n\n### Strengthening Opportunities\n- Keep this route.\n",
        )
        self._write(
            root,
            ".codex/get-shit-done/workflows/plan-phase.md",
            "# Plan\n\n### Strengthening Opportunities\n- Keep this route.\n",
        )
        self._write(
            root,
            ".codex/skills/gsd-rigorous-research/references/output-template.md",
            "# Output Template\n\n### Strengthening Opportunities\n- Keep this route.\n",
        )
        self._write(root, ".codex/get-shit-done/workflows/verify-phase.md", "# Verify\n")
        self._write(root, ".codex/get-shit-done/templates/verification-report.md", "# Verification Report\n")

    def _write_seed(
        self,
        root: pathlib.Path,
        rel_path: str,
        *,
        seed_id: str,
        title: str,
        version: str | None,
        include_current_shape: bool,
    ) -> None:
        version_line = f"seed_contract_version: {version}\n" if version is not None else ""
        body = [
            "---",
            f"id: {seed_id}",
            version_line.rstrip(),
            "status: dormant",
        ]
        if include_current_shape:
            body.extend(
                [
                    "planted: 2026-04-22",
                    "planted_during: milestone",
                    "trigger_when: later",
                    "scope: Medium",
                ]
            )
        else:
            body.append("trigger_when: later")
        body.extend(
            [
                "---",
                "",
                f"# {seed_id}: {title}",
                "",
                "## Why This Matters",
                "",
                "- Keep the route visible.",
                "",
                "## When to Surface",
                "",
                "- later",
            ]
        )
        if include_current_shape:
            body.extend(
                [
                    "",
                    "## Scope Estimate",
                    "",
                    "- Medium",
                    "",
                    "## Strengthening Carry",
                    "",
                    "- Intensify the route.",
                    "",
                    "## Breadcrumbs",
                    "",
                    "- notes",
                    "",
                    "## Notes",
                    "",
                    "- context",
                ]
            )
        self._write(root, rel_path, "\n".join(body) + "\n")

    def _render_bridge_block(self, workflow_path: pathlib.Path, note: dict) -> str:
        text = workflow_path.read_text(encoding="utf-8")
        block = text.split(
            "Only show these lines when `UPLIFT_NOTE.show_seed_migration_pointer` is `true`:\n\n```markdown\n",
            1,
        )[1].split("\n```", 1)[0]
        for key in (
            "seed_migration_candidate_count",
            "seed_migration_candidate_breakdown",
            "seed_migration_inspect_pointer",
            "seed_migration_write_pointer",
        ):
            block = block.replace("{" + key + "}", str(note[key]))
        return block

    def _normalized_seed_migration_manifest(self, payload: dict) -> dict:
        normalized = json.loads(json.dumps(payload))
        normalized["generated_at"] = "__dynamic__"
        normalized["repo_root"] = "__fixture_root__"
        return normalized

    def test_bridge_chain_matches_shape_fixture_and_render_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root)
            self._write_seed(
                repo_root,
                ".planning/seeds/SEED-001-legacy.md",
                seed_id="SEED-001",
                title="Legacy",
                version=None,
                include_current_shape=False,
            )
            self._write_seed(
                repo_root,
                ".planning/seeds/SEED-002-current-gap.md",
                seed_id="SEED-002",
                title="Current Gap",
                version=smi.CURRENT_SEED_CONTRACT_VERSION,
                include_current_shape=False,
            )
            self._write_seed(
                repo_root,
                ".planning/seeds/SEED-003-old-version.md",
                seed_id="SEED-003",
                title="Old Version",
                version="1",
                include_current_shape=True,
            )

            pu.write_outputs(repo_root, pu.analyze_repo(repo_root))
            note = pu.build_progress_note(repo_root)

            self.assertTrue(note["show_seed_migration_pointer"])
            self.assertEqual(note["seed_migration_candidate_count"], 3)
            self.assertEqual(
                note["seed_migration_candidate_breakdown"],
                "legacy 1 / noncurrent 1 / shape-gap 1",
            )
            self.assertEqual(note["seed_migration_inspect_pointer"], pu.SEED_MIGRATION_SKILL_COMMAND)
            self.assertEqual(note["seed_migration_write_pointer"], pu.SEED_MIGRATION_WRITE_COMMAND)

            for rel_path in (
                "tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md",
                "tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md",
            ):
                rendered = self._render_bridge_block(ROOT / rel_path, note)
                self.assertIn("- Seed migration candidates: 3", rendered)
                self.assertIn(
                    "- Seed migration breakdown: legacy 1 / noncurrent 1 / shape-gap 1",
                    rendered,
                )
                self.assertIn(
                    "- Seed migration inventory: $gsd-seed-migration-inventory",
                    rendered,
                )
                self.assertIn(
                    "- Seed migration write packet: $gsd-seed-migration-inventory --write",
                    rendered,
                )

            analysis = smi.analyze_repo(repo_root)
            written = smi.write_outputs(repo_root, analysis)
            fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
            self.assertEqual(
                self._normalized_seed_migration_manifest(written),
                fixture,
            )


if __name__ == "__main__":
    unittest.main()
