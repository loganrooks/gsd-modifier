Date: 2026-04-21
Status: landed first slice

# State / Progress / Resume Future-Carry Consumer Implementation

## Purpose

- [g:r:i] This note records the landed first-read consumer slice opened in `61`.
- [g:r:i] The target stayed bounded: make carried context show up more clearly and more durably in the first-read consumer layer instead of leaving it as producer-side memory plus operator inference.

## What Landed

- [e:r:i] The tracked overlay now owns the state consumer helper carrier that previously sat outside repo-local overlay ownership:
  - [tooling/portable-gsd/overlay/get-shit-done/bin/lib/state.cjs](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/bin/lib/state.cjs)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] `state-snapshot` now keeps the current template-aligned accumulated-context consumer buckets explicit instead of dropping them:
  - `decisions`
  - `blockers`
  - `future_carry`
  - `session`
- [e:r:i] The helper now parses `### Decisions`, `### Blockers/Concerns`, `### Future Carry Forward`, and `## Session Continuity` from the current state template shape rather than assuming older section headings only.
- [e:r:i] `progress.md` now treats `Future Carry Forward` as an explicit report section when any bucket remains live.
- [e:r:i] `resume-project.md` now loads the structured state snapshot as a re-entry companion and surfaces `Future Carry Forward` explicitly when present instead of leaving it to reader memory.

## Verification And Recovery Path

- [e:r:i] The new helper owner became a real overlay/materialization move, not a live-only patch:
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`
- [e:r:i] Focused helper proof now exists in [tooling/codex/tests/test_state_snapshot_future_carry.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_state_snapshot_future_carry.py), covering:
  - current-template decisions parsing
  - blockers parsing
  - future-carry bucket parsing
  - session-continuity parsing
  - workflow-consumer contract presence
- [e:r:i] Live runtime reread now shows the current repo state snapshot carries decisions, blockers, and session continuity again, with `future_carry` remaining empty on this repo until the state file itself carries live entries.

## What This Slice Still Holds

- [d:r:i] This slice does not widen into a whole `state-snapshot` / `state json` parity rewrite.
- [d:r:i] It does not try to settle every current-position parsing weakness in the helper.
- [d:r:i] It does not yet widen into `SPEC`, seed consumers, or broader first-read control-surface redesign.

## Current Consequence

- [d:r:i] Lifecycle carry now has a first-read consumer bridge instead of stopping at producer-side lifecycle boundaries.
- [d:r:i] The next narrower lifecycle question is no longer whether the first-read consumers should inherit at all.
- [d:r:i] The next narrower lifecycle question is which later surface should inherit next after this bridge:
  - `SPEC`
  - seed consumers
  - or broader read-order / relevance-control surfaces
