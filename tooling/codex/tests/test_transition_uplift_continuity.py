import json
import pathlib
import subprocess
import tempfile
import textwrap
import unittest


REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
GSD_TOOLS = REPO_ROOT / ".codex" / "get-shit-done" / "bin" / "gsd-tools.cjs"


STATE_WITH_PROJECT_UPLIFT = """---
gsd_state_version: 1.0
status: in progress
last_updated: "2026-04-22T12:00:00+00:00"
---

# Project State

## Current Position

Phase: 1 of 2 (Test Phase)
Plan: 1 of 1 in current phase
Status: In progress
Last activity: 2026-04-22

Progress: [█████░░░░░] 50%

## Accumulated Context

### Future Carry Forward

- Preserve: keep uplift continuity explicit at phase close

## Project Uplift

Last uplift pass: 2026-04-22T12:00:00+00:00
Last uplift class: cross-runtime uplift
Compatibility posture: observed_basis_only
Observed runtime basis: 1.38.3
Held runtime annotation: .claude 1.34.2 (held_annotation)
Current recommendation: Continue with ordinary routing; uplift memory keeps this posture explicit.

## Session Continuity

Last session: 2026-04-22T12:00:00+00:00
Stopped at: finishing Phase 1
Resume file: None
"""


ROADMAP = """# Roadmap

## Phase 1: Test Phase

- [ ] Phase 1: Test Phase

**Plans:** 0/1 plans pending

## Phase 2: Next Phase

- [ ] Phase 2: Next Phase

**Plans:** 0/0 plans pending

| Phase | Plans | Status | Completed |
|-------|-------|--------|-----------|
| 1 Test Phase | 0/1 | In Progress |  |
| 2 Next Phase | 0/0 | Pending |  |
"""


class TransitionUpliftContinuityTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _minimal_phase_project(self, root: pathlib.Path) -> None:
        self._write(root, ".planning/STATE.md", STATE_WITH_PROJECT_UPLIFT)
        self._write(root, ".planning/ROADMAP.md", ROADMAP)
        self._write(root, ".planning/PROJECT.md", "# Project\n")
        self._write(root, ".planning/phases/01-test-phase/01-PLAN.md", "# Plan\n")
        self._write(
            root,
            ".planning/phases/01-test-phase/01-SUMMARY.md",
            "---\ncompletion_mode: clean_completion\n---\n\n# Summary\n",
        )

    def test_phase_complete_preserves_project_uplift_section(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_phase_project(repo_root)

            proc = subprocess.run(
                ["node", str(GSD_TOOLS), "phase", "complete", "1", "--cwd", str(repo_root)],
                check=True,
                capture_output=True,
                text=True,
            )
            payload = json.loads(proc.stdout)

            state_text = (repo_root / ".planning/STATE.md").read_text(encoding="utf-8")
            self.assertEqual(payload["next_phase"], "2")
            self.assertIn("## Project Uplift", state_text)
            self.assertIn("Compatibility posture: observed_basis_only", state_text)
            self.assertIn("Held runtime annotation: .claude 1.34.2 (held_annotation)", state_text)
            self.assertIn("Phase: 2 of 2 (next phase)", state_text)

    def test_transition_workflow_names_uplift_continuity_step(self) -> None:
        workflow = (
            REPO_ROOT
            / "tooling"
            / "portable-gsd"
            / "overlay"
            / "get-shit-done"
            / "workflows"
            / "transition.md"
        ).read_text(encoding="utf-8")

        self.assertIn('<step name="review_project_uplift_continuity">', workflow)
        self.assertIn('project_uplift.py" progress-note', workflow)
        self.assertIn("## Project Uplift", workflow)

    def test_write_outputs_prefers_project_uplift_before_deferred_items(self) -> None:
        from tooling.codex import project_uplift as pu

        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            state_text = textwrap.dedent(
                """\
                ---
                gsd_state_version: 1.0
                status: completed
                last_updated: "2026-04-22T12:00:00+00:00"
                ---

                # Project State

                ## Current Position

                Status: completed

                ## Accumulated Context

                ### Future Carry Forward

                - Preserve: keep uplift explicit

                ## Deferred Items

                None yet.

                ## Session Continuity

                Last session: 2026-04-22T12:00:00+00:00
                Stopped at: test
                Resume file: None
                """
            )
            self._write(repo_root, ".planning/STATE.md", state_text)
            self._write(repo_root, ".planning/PROJECT.md", "# Project\n")
            self._write(repo_root, ".planning/ROADMAP.md", "# Roadmap\n")
            self._write(repo_root, "AGENTS.md", "# Agents\n")
            self._write(repo_root, ".planning/AGENTS.md", "# Planning Agents\n")
            self._write(repo_root, "CLAUDE.md", "# Claude\n")
            self._write(repo_root, ".planning/CLAUDE.md", "# Planning Claude\n")
            self._write(repo_root, ".planning/CLAIM-TYPES.md", "# Claim Types\n")
            self._write(repo_root, ".planning/LONG-ARC.md", "---\ndocument: LONG-ARC\nstatus: canonical\n---\n\n# Long Arc\n")
            self._write(repo_root, ".codex/config.toml", 'model = "gpt-5.4"\n')
            self._write(repo_root, ".codex/gsd-file-manifest.json", json.dumps({"version": "1.38.3"}) + "\n")
            self._write(repo_root, ".codex/get-shit-done/VERSION", "1.38.3\n")
            self._write(repo_root, ".codex/agents/gsd-planner.toml", 'description = "planner"\n')
            self._write(repo_root, ".codex/agents/gsd-plan-checker.toml", 'description = "checker"\n')
            self._write(repo_root, "tooling/codex/README.md", "# Codex Tooling Notes\n\n## Utilities\n- `project_uplift.py`\n")
            self._write(repo_root, "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json", json.dumps({"schema_version": 1, "entries": {}}) + "\n")
            self._write(repo_root, "tooling/codex/UPLIFT-HELD-LATER.md", "- cross-runtime uplift composition — held\n")
            self._write(repo_root, ".codex/get-shit-done/workflows/discuss-phase.md", "### Strengthening Opportunities\n- keep\n")
            self._write(repo_root, ".codex/get-shit-done/templates/context.md", "### Strengthening Opportunities\n- keep\n")
            self._write(repo_root, ".codex/get-shit-done/workflows/plan-phase.md", "### Strengthening Opportunities\n- keep\n")
            self._write(repo_root, ".codex/skills/gsd-rigorous-research/references/output-template.md", "### Strengthening Opportunities\n- keep\n")
            self._write(repo_root, ".codex/get-shit-done/workflows/verify-phase.md", "## Future-Preservation Carry Review\n- carried\n")
            self._write(repo_root, ".codex/get-shit-done/templates/verification-report.md", "## Future-Preservation Carry\n- carried\n")

            pu.write_outputs(repo_root, pu.analyze_repo(repo_root))

            updated = (repo_root / ".planning/STATE.md").read_text(encoding="utf-8")
            self.assertLess(updated.index("## Project Uplift"), updated.index("## Deferred Items"))


if __name__ == "__main__":
    unittest.main()
