<!-- This file is updated by the agent at the end of each iteration. Do not edit manually unless recovering from a corrupted state. -->

# Inject Migration State

Last updated: 2026-05-08T00:00:00Z (initial creation; not yet started)
Last updated by: initiative author (manual)
Schema version: 1

## Current Status

- **Phase**: 0 (`00-surface-cleanup`)
- **Slice within phase**: 0 (not started)
- **Status**: `pending` (one of: `pending`, `in-progress`, `paused-for-approval`, `blocked`, `complete`, `aborted`)
- **Last checkpoint**: none yet
- **Last commit**: `f110436` (pre-initiative; the disposition update from §7.1 of orientation)
- **Sentinel**: `NOT-STARTED` (when this becomes `INITIATIVE-COMPLETE`, the loop stops)

## Phase Progress

- [ ] **Phase 0** — Surface cleanup (reclassify 4 stale-deleted carriers; add change-class triggers; delete temp handoff)
- [ ] **Phase 1** — Schema foundation (manifest schema v4 ADR; mode: inject semantics; operation kinds)
- [ ] **Phase 2** — Contract tools (validate/apply/extract/verify functions in portable_gsd_contract.py + unit tests)
- [ ] **Phase 3** — Pilot (migrate `references/mandatory-initial-read.md` end-to-end through both runtimes)
- [ ] **Phase 4** — First wave (4 small references)
- [ ] **Phase 5** — Second wave (5 additive workflows)
- [ ] **Phase 6** — Third wave (3 step-level workflows: health, update, progress)
- [ ] **Phase 7** — Fourth wave (3 large workflows: new-project, discuss-phase, plan-phase) — DEFERRABLE
- [ ] **Phase 8** — Templates and agents (evaluate and migrate viable carriers)
- [ ] **Phase 9** — Codex skill mirrors (decide pre-conversion vs accept-as-is)
- [ ] **Phase 10** — Closeout (retrospective, ROADMAP/STATUS update, archive)

## Active Work

- **Current task**: (none — initiative not started)
- **Started**: (n/a)
- **Expected completion**: (n/a)

## Blockers

(none)

## Counters

- Carriers migrated to `mode: inject`: 0 / target ~25–30
- Carriers reclassified to `mode: add`: 0 / target 4 (Phase 0)
- Carriers staying as `mode: overwrite`: ~5 (lib *.cjs) + others TBD per phase decisions
- Net-new modifier-owned (`mode: add`): 18 (no migration; baseline)
- Inject operation kinds implemented: 0 / target ~7
- Inject unit tests passing: 0 / target TBD
- Bootstrap gate hard_failures: 4 (target: 0 after Phase 0)
- Phases complete: 0 / 11
- Slices complete: 0

## Recent Checkpoints

(none — initiative not started; checkpoints will accumulate under `checkpoints/`)

## Dirty-Worktree Pre-Conditions

For the loop to start cleanly:

- `git status --short` should show only the temp handoff (`docs/handoff/DELETE-AFTER-INGESTION-...md`) until Phase 0 Slice 6 deletes it
- `git diff --check` should be clean
- `bash scripts/ci/check-deterministic.sh` passed at the most recent commit (last verified: 2026-05-08, exit 0)
- `bash scripts/ci/check-bootstrap.sh` passed at the most recent commit (last verified: 2026-05-08, exit 0; surfaces 4 expected hard_failures from §1.4 of intervention-strategies)

## Notes For The Agent

- This file is the canonical source of truth for "where are we". Any divergence from `git log` or filesystem state means the file lies; reconcile by reading the actual repo state and updating this file.
- Update this file ONLY at the end of an iteration after the slice's commit lands. Never partial-update.
- If you start an iteration and find this file inconsistent with `git log`, log the inconsistency and prefer `git log` as ground truth. Update this file accordingly.
- The `Last commit` field should always match `git rev-parse HEAD`.
