<!-- This file is updated by the agent at the end of each iteration. Do not edit manually unless recovering from a corrupted state. -->

# Inject Migration State

Last updated: 2026-05-15T00:00:00Z (rebuilt around `/goal` + reviewer-mediated checkpoints; still not started)
Last updated by: initiative author (manual)
Schema version: 2

## Current Status

- **Phase**: 0 (`00-surface-cleanup`)
- **Slice within phase**: 0 (not started)
- **Status**: `pending` (one of: `pending`, `in-progress`, `paused-for-operator`, `blocked`, `complete`, `aborted`)
- **Last checkpoint**: none yet
- **Last commit**: (set by next iteration's reconciliation to `git rev-parse HEAD`)
- **Sentinel**: `NOT-STARTED` (when this becomes `INITIATIVE-COMPLETE`, the `/goal` evaluator terminates the goal)

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

## Reviewer Decisions Log

(no decisions yet — initiative not started)

<!-- Format (append-only; one row per reviewer invocation):
| Timestamp (ISO-8601 UTC) | Phase.Slice | Reviewer | Verdict | One-line reasoning | Decision taken |
|---|---|---|---|---|---|
| 2026-05-15T14:32:00Z | 1.2 | adversarial-auditor-xhigh | PASS | ADR-001 scope sound; risks honestly enumerated | proceeded to commit; logged in checkpoints/2026-05-15T143200Z-phase01-slice02.md |
-->

## Auto-Recovery Counters

Tracks resilience of the loop. The 3-consecutive-failure rule fires when any slice's `attempts` here reaches 3.

- Total reviewer invocations: 0
- Reviewer PASS verdicts: 0
- Reviewer FAIL verdicts: 0
- Reviewer ESCALATE verdicts: 0
- Reviewer HALT verdicts: 0
- Auto-recovery successes: 0 (a gate failed but the recovery pattern in GUARDRAILS.md restored green)
- Auto-recovery escalations to hard-stop: 0
- Slice-level retries (cumulative): 0
- Per-slice attempt counts (only for slices not yet completed): (none)

## Dirty-Worktree Pre-Conditions

For the loop to start cleanly:

- `git status --short` should show only the temp handoff (`docs/handoff/DELETE-AFTER-INGESTION-...md`) until Phase 0 Slice 6 deletes it
- `git diff --check` should be clean
- `bash scripts/ci/check-deterministic.sh` passed at the most recent commit (last verified: 2026-05-08, exit 0)
- `bash scripts/ci/check-bootstrap.sh` passed at the most recent commit (last verified: 2026-05-08, exit 0; surfaces 4 expected hard_failures from §1.4 of intervention-strategies)

## Notes For The Agent

- This file is the canonical source of truth for "where are we". Any divergence from `git log` or filesystem state means the file lies; reconcile by reading the actual repo state and updating this file.
- Update this file ONLY at the end of a turn after the slice's commit lands. Never partial-update.
- If you start a turn and find this file inconsistent with `git log`, log the inconsistency and prefer `git log` as ground truth. Update this file accordingly.
- The `Last commit` field should always match `git rev-parse HEAD`.
- When a reviewer is invoked (per [REVIEWERS.md](REVIEWERS.md)), append a row to `Reviewer Decisions Log` AND record the full verdict block in the slice's checkpoint under `## Reviewer Verdict`.
- The `[GOAL-EVAL]` line at turn end is mandatory — see [PROTOCOL.md](PROTOCOL.md) "Turn-End Discipline" for exact format.
- The 3-consecutive-failure rule: if `Auto-Recovery Counters → Per-slice attempt counts` shows the same slice at 3, the next failure is an automatic hard-stop.
