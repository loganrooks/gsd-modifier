Date: 2026-04-20
Status: targeted reread disposition

# Live-Only Agent Targeted Reread Disposition

## Purpose

- [g:r:i] This note resolves the first two targeted rereads named by [12-live-only-agent-cohort-matrix.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/12-live-only-agent-cohort-matrix.md:1): `gsd-debug-session-manager` first, then `gsd-pattern-mapper`.

## `gsd-debug-session-manager`

- [d:r:i] Reclassify from `strong orphan-suspicion carry` to `active skill-routed live-only carry`.
- [e:c+i] The current local harness still routes this agent through the repo-local debug skill rather than through the narrower `get-shit-done/` workflow subset. Sources: [.codex/skills/gsd-debug/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-debug/SKILL.md:66), [.codex/skills/gsd-debug/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-debug/SKILL.md:199), [.codex/skills/gsd-debug/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-debug/SKILL.md:256), [.codex/skills/gsd-debug/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-debug/SKILL.md:277).
- [d:r:i] Current consequence: no cleanup or retirement pressure is earned for `gsd-debug-session-manager` in the repo-local harness.

## `gsd-pattern-mapper`

- [d:r:i] Reclassify from vague `weakly routed` to `planner-adjacent authority-gap carry`.
- [e:c+i] The current local repo still carries pattern-mapper pressure through the phase-planning surface, but less directly than the active cohort. It remains present on disk, remains profiled in runtime model profiles, and still leaves artifact pressure through `PATTERNS.md` handling. Sources: [.codex/agents/gsd-pattern-mapper.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.toml:1), [.codex/get-shit-done/bin/lib/model-profiles.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/model-profiles.cjs:22), [.codex/get-shit-done/bin/lib/init.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/init.cjs:289), [.codex/get-shit-done/bin/lib/init.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/init.cjs:318).
- [d:r:i] Current consequence: no cleanup or retirement pressure is earned for `gsd-pattern-mapper` either. The stronger pressure is later authority/routing clarification, not deletion.

## Resulting Cleanup Judgment

- [d:r:i] No stale-agent cleanup is currently earned from this targeted reread.
- [d:r:i] The stronger immediate carry is:
  - keep the live-only cohort intact for now
  - move next to selected-lane snapshot discipline
  - then revisit manifest/install coherence on the corrected baseline

## What This Rejects

- [d:r:i] Reject the earlier temptation to treat `gsd-debug-session-manager` as a live cleanup candidate just because it disappeared from the narrower `get-shit-done/` read surface.
- [d:r:i] Reject broad stale-agent cleanup as the current second-tranche move.

## Immediate Next Move

- [g:r:i] Land selected-lane runtime snapshot discipline next, now that the strongest current live-only cohort no longer carries an immediate retirement story.
