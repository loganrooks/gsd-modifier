import json
import pathlib
import tempfile
import unittest

from tooling.codex import project_uplift as pu


STATE_TEMPLATE = """---
gsd_state_version: 1.0
status: {status}
last_updated: "2026-04-21T12:00:00+00:00"
---

# Project State

## Current Position

Status: {status}

## Session Continuity

Last session: 2026-04-21T12:00:00+00:00
Stopped at: test
Resume file: None
"""


class ProjectUpliftTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _minimal_project(self, root: pathlib.Path, status: str = "completed") -> None:
        self._write(root, ".planning/PROJECT.md", "# Project\n")
        self._write(root, ".planning/ROADMAP.md", "# Roadmap\n")
        self._write(root, ".planning/STATE.md", STATE_TEMPLATE.format(status=status))
        self._write(root, "AGENTS.md", "# Agents\n")
        self._write(root, ".planning/AGENTS.md", "# Planning Agents\n")
        self._write(root, ".codex/config.toml", 'model = "gpt-5.4"\n')
        self._write(root, ".codex/agents/gsd-planner.toml", 'description = "planner"\n')
        self._write(root, ".codex/agents/gsd-plan-checker.toml", 'description = "checker"\n')

    def test_detect_classifies_vanilla_project(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")

            analysis = pu.analyze_repo(repo_root)

            self.assertEqual(analysis["project_class"], "vanilla uplift")
            self.assertTrue(analysis["recommend_detect_only"])
            self.assertIn("Claim Types", analysis["absent_additive_carriers"])
            self.assertIn("Root CLAUDE", analysis["pending_doctrine_sensitive_proposals"])

    def test_detect_classifies_lightly_aged_project(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write(repo_root, "CLAUDE.md", "# Claude\n")
            self._write(repo_root, ".planning/CLAUDE.md", "# Planning Claude\n")
            self._write(repo_root, ".planning/CLAIM-TYPES.md", "# Claim Types\n")
            self._write(repo_root, ".planning/LONG-ARC.md", "# Long Arc\n")
            self._write(repo_root, "tooling/codex/README.md", "# Tooling\n")

            analysis = pu.analyze_repo(repo_root)

            self.assertEqual(analysis["project_class"], "lightly aged uplift")
            self.assertTrue(analysis["recommend_detect_only"])
            self.assertEqual(analysis["absent_additive_carriers"], [])
            self.assertIn("Discuss Strengthening Route", analysis["pending_doctrine_sensitive_proposals"])

    def test_write_outputs_and_progress_note_detect_doctrine_change(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write(repo_root, "CLAUDE.md", "# Claude\n")
            self._write(repo_root, ".planning/CLAUDE.md", "# Planning Claude\n")
            self._write(repo_root, ".planning/CLAIM-TYPES.md", "# Claim Types\n")
            self._write(repo_root, ".planning/LONG-ARC.md", "# Long Arc\n")
            self._write(repo_root, "tooling/codex/README.md", "# Tooling\n")
            self._write(
                repo_root,
                ".codex/get-shit-done/workflows/discuss-phase.md",
                "Strengthening Opportunities\n",
            )
            self._write(
                repo_root,
                ".codex/get-shit-done/templates/context.md",
                "Strengthening Opportunities\n",
            )
            self._write(
                repo_root,
                ".codex/get-shit-done/workflows/plan-phase.md",
                "Strengthening Opportunities\n",
            )
            self._write(
                repo_root,
                ".codex/skills/gsd-rigorous-research/references/output-template.md",
                "Strengthening Opportunities\n",
            )

            analysis = pu.analyze_repo(repo_root)
            written = pu.write_outputs(repo_root, analysis)
            self.assertEqual(written["report_path"], ".planning/UPLIFT-REPORT.md")
            self.assertTrue((repo_root / ".planning/UPLIFT-MANIFEST.json").exists())
            self.assertIn("## Project Uplift", (repo_root / ".planning/STATE.md").read_text(encoding="utf-8"))

            note = pu.build_progress_note(repo_root)
            self.assertTrue(note["show"])
            self.assertFalse(note["recommend_detect_only"])

            self._write(repo_root, "AGENTS.md", "# Agents changed\n")
            changed_note = pu.build_progress_note(repo_root)
            self.assertTrue(changed_note["recommend_detect_only"])
            self.assertTrue(changed_note["doctrine_reference_changed"])


if __name__ == "__main__":
    unittest.main()
