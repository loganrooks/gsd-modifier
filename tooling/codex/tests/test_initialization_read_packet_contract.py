import subprocess
import tempfile
import unittest
from pathlib import Path

from tooling.codex.tests.overlay_paths import overlay_entry_mode, overlay_source_path


ROOT = Path(__file__).resolve().parents[3]
NEW_PROJECT = ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md"
GENERATOR = ROOT / "tooling/portable-gsd/overlay/get-shit-done/bin/generate-instruction.cjs"


class InitializationReadPacketContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_initialization_workflows(self) -> None:
        self.assertEqual(overlay_entry_mode("get-shit-done/workflows/new-project.md"), "overwrite")
        self.assertEqual(overlay_entry_mode("get-shit-done/workflows/new-milestone.md"), "overwrite")
        self.assertEqual(overlay_entry_mode("get-shit-done/workflows/ingest-docs.md"), "overwrite")

    def test_initialization_workflows_use_layered_read_packets(self) -> None:
        surfaces = [
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md",
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md",
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md",
        ]
        for path in surfaces:
            content = path.read_text()
            self.assertIn(
                "@__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md",
                content,
            )
            self.assertIn("<supporting_reading>", content)
            self.assertIn("<deeper_reading>", content)

    def test_new_project_and_ingest_keep_uplift_route_explicit(self) -> None:
        new_project = (
            NEW_PROJECT
        ).read_text()
        ingest_docs = (
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md"
        ).read_text()
        self.assertIn("$gsd-uplift-project --write", new_project)
        self.assertIn("$gsd-uplift-project --write", ingest_docs)

    def test_new_project_uses_repo_owned_instruction_generator(self) -> None:
        new_project = NEW_PROJECT.read_text(encoding="utf-8")

        self.assertIn(
            'if [ "$RUNTIME" = "codex" ]; then INSTRUCTION_FILE="AGENTS.md"; else INSTRUCTION_FILE="CLAUDE.md"; fi',
            new_project,
        )
        self.assertNotIn(
            'gsd-sdk query generate-claude-md --output "$INSTRUCTION_FILE"',
            new_project,
        )
        self.assertIn(
            'GSD_INSTRUCTION_GENERATOR="$GSD_RUNTIME_ROOT/get-shit-done/bin/generate-instruction.cjs"',
            new_project,
        )
        self.assertIn(
            'node "$GSD_INSTRUCTION_GENERATOR" --output "$INSTRUCTION_FILE" --runtime "$RUNTIME"',
            new_project,
        )

    def test_instruction_generator_is_materialized_for_supported_runtimes(self) -> None:
        self.assertEqual(overlay_entry_mode("get-shit-done/bin/generate-instruction.cjs"), "add")
        self.assertEqual(
            overlay_source_path("get-shit-done/bin/generate-instruction.cjs"),
            GENERATOR,
        )

    def test_instruction_generator_creates_agents_md(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".planning").mkdir()
            (root / ".planning/PROJECT.md").write_text(
                "# Sample Project\n\n## What This Is\n\nA sample project.\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                ["node", str(GENERATOR), "--output", "AGENTS.md", "--runtime", "codex"],
                cwd=root,
                text=True,
                capture_output=True,
                check=True,
            )

            content = (root / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn('"action": "created"', result.stdout)
            self.assertIn("<!-- GSD:project-start source:PROJECT.md -->", content)
            self.assertIn("## GSD Workflow Enforcement", content)
            self.assertIn("$gsd-quick", content)
            self.assertNotIn("CLAUDE.md Template", content)

    def test_instruction_generator_honors_runtime_selected_output_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".planning").mkdir()
            (root / ".planning/PROJECT.md").write_text(
                "# Sample Project\n\n## What This Is\n\nA sample project.\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                ["node", str(GENERATOR), "--output", "CLAUDE.md", "--runtime", "claude"],
                cwd=root,
                text=True,
                capture_output=True,
                check=True,
            )

            self.assertFalse((root / "AGENTS.md").exists())
            content = (root / "CLAUDE.md").read_text(encoding="utf-8")
            self.assertIn('"action": "created"', result.stdout)
            self.assertIn("Created CLAUDE.md instruction file", result.stdout)
            self.assertIn("<!-- GSD:project-start source:PROJECT.md -->", content)
            self.assertIn("## GSD Workflow Enforcement", content)

    def test_instruction_generator_refreshes_markers_without_overwriting_user_content(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".planning").mkdir()
            (root / ".planning/PROJECT.md").write_text(
                "# First Name\n\n## What This Is\n\nInitial body.\n",
                encoding="utf-8",
            )

            subprocess.run(
                ["node", str(GENERATOR), "--output", "AGENTS.md", "--runtime", "codex"],
                cwd=root,
                text=True,
                capture_output=True,
                check=True,
            )
            agents_path = root / "AGENTS.md"
            agents_path.write_text(
                f"User preface.\n\n{agents_path.read_text(encoding='utf-8')}\nUser suffix.\n",
                encoding="utf-8",
            )
            (root / ".planning/PROJECT.md").write_text(
                "# Second Name\n\n## What This Is\n\nUpdated body.\n",
                encoding="utf-8",
            )

            subprocess.run(
                ["node", str(GENERATOR), "--output", "AGENTS.md", "--runtime", "claude"],
                cwd=root,
                text=True,
                capture_output=True,
                check=True,
            )

            content = agents_path.read_text(encoding="utf-8")
            self.assertIn("User preface.", content)
            self.assertIn("User suffix.", content)
            self.assertIn("**Second Name**", content)
            self.assertIn("Updated body.", content)
            self.assertNotIn("Initial body.", content)


if __name__ == "__main__":
    unittest.main()
