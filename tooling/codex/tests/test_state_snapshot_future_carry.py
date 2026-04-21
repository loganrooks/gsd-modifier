import json
import pathlib
import subprocess
import tempfile
import unittest


REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
GSD_TOOLS = REPO_ROOT / ".codex" / "get-shit-done" / "bin" / "gsd-tools.cjs"


STATE_WITH_FUTURE_CARRY = """---
gsd_state_version: 1.0
status: planning
last_updated: "2026-04-21T12:00:00+00:00"
---

# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-04-21)

**Core value:** Test project
**Current focus:** Phase 1

## Current Position

Phase: 1 of 4 (Test Phase)
Plan: 0 of TBD in current phase
Status: Replanning required before execution
Last activity: 2026-04-21

Progress: [░░░░░░░░░░] 0%

## Accumulated Context

### Decisions

Recent decisions affecting current work:

- Keep authored circuit-internal recognition as the anchor experience
- Preserve room authority as an explicit later choice

### Blockers/Concerns

- Phase 1 rerun must absorb refreshed canon before execution
- Runtime authority model remains explicit and unresolved

### Future Carry Forward

- Preserve: authored round contract must keep venue-approach clues secondary
- Keep open: room authority runtime choice
- Posture: browser-first host and guest flow remains governing
- Seeded: stronger telemetry route -> seed-telemetry

## Session Continuity

Last session: 2026-04-21 12:00
Stopped at: Prepared the next bounded slice
Resume file: None
"""


class StateSnapshotFutureCarryTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _state_snapshot(self, repo_root: pathlib.Path) -> dict:
        proc = subprocess.run(
            ["node", str(GSD_TOOLS), "state-snapshot", "--cwd", str(repo_root)],
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(proc.stdout)

    def test_state_snapshot_parses_accumulated_context_and_future_carry(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._write(repo_root, ".planning/STATE.md", STATE_WITH_FUTURE_CARRY)

            snapshot = self._state_snapshot(repo_root)

            self.assertEqual(
                snapshot["decisions"],
                [
                    {"decision": "Keep authored circuit-internal recognition as the anchor experience"},
                    {"decision": "Preserve room authority as an explicit later choice"},
                ],
            )
            self.assertEqual(
                snapshot["blockers"],
                [
                    {"text": "Phase 1 rerun must absorb refreshed canon before execution"},
                    {"text": "Runtime authority model remains explicit and unresolved"},
                ],
            )
            self.assertEqual(
                snapshot["future_carry"],
                {
                    "preserve": ["authored round contract must keep venue-approach clues secondary"],
                    "keep_open": ["room authority runtime choice"],
                    "posture": ["browser-first host and guest flow remains governing"],
                    "seeded": ["stronger telemetry route -> seed-telemetry"],
                },
            )
            self.assertEqual(snapshot["session"]["last_date"], "2026-04-21 12:00")
            self.assertEqual(snapshot["session"]["last_session"], "2026-04-21 12:00")
            self.assertEqual(snapshot["session"]["stopped_at"], "Prepared the next bounded slice")
            self.assertEqual(snapshot["session"]["resume_file"], "None")

    def test_overlay_consumers_name_future_carry_surface(self) -> None:
        progress_workflow = (
            REPO_ROOT
            / "tooling"
            / "portable-gsd"
            / "overlay"
            / "get-shit-done"
            / "workflows"
            / "progress.md"
        ).read_text(encoding="utf-8")
        resume_workflow = (
            REPO_ROOT
            / "tooling"
            / "portable-gsd"
            / "overlay"
            / "get-shit-done"
            / "workflows"
            / "resume-project.md"
        ).read_text(encoding="utf-8")

        self.assertIn("## Future Carry Forward", progress_workflow)
        self.assertIn("STATE_SNAPSHOT=$(node", resume_workflow)
        self.assertIn("Future Carry Forward", resume_workflow)


if __name__ == "__main__":
    unittest.main()
