<!-- This file is updated by the agent at the end of each iteration. Do not edit manually unless recovering from a corrupted state. -->

# Inject Migration State

Last updated: 2026-05-15T23:45:17Z (slice 3 reclassify gsd-plant-seed skill)
Last updated by: inject-migration /goal agent
Schema version: 2

## Current Status

- **Phase**: 0 (`00-surface-cleanup`)
- **Slice within phase**: 4 (slice 3 complete; next is "Reclassify research-phase workflow as modifier-owned" — note: workflow has dual codex+claude materializers per core_required parity_tier)
- **Status**: `in-progress` (one of: `pending`, `in-progress`, `paused-for-operator`, `blocked`, `complete`, `aborted`)
- **Last checkpoint**: `checkpoints/2026-05-15T234517Z-phase00-slice03.md`
- **Last commit**: `bbcbe2307f9cc3749dfc7912a501e06375c95529` (lag-by-one — slice 2's commit reconciled via PROTOCOL.md cold-start step 4; will lag again to slice 3's commit after this turn's atomic commit)
- **Sentinel**: `IN-PROGRESS` (slice 3 succeeded; 3 of 4 stale-deleted carrier reclassifications complete; only `research-phase` workflow remains in slice 4 to complete Phase 0 hard-failure-clearing batch)

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

- **Current task**: executing Phase 0 Slice 4 (reclassify `research-phase` workflow as modifier-owned `mode: add`)
- **Started**: 2026-05-15T23:45:17Z
- **Expected completion**: slice 4 moves `research-phase.md` from `tooling/portable-gsd/overlay/get-shit-done/workflows/` to `harness_modifier/overlay/get-shit-done/workflows/` and flips BOTH codex AND claude materializer entries from `mode: overwrite` to `mode: add` (workflow is `parity_tier: core_required`, so both runtimes have materializer entries)

## Blockers

(none active)

### Resolved blockers

1. ~~**Slice 0 spec contradictions (gsd-debugger + Plan reviewer concur, 2026-05-15)**~~ — **RESOLVED 2026-05-15** by operator resolution commit. Both contradictions addressed:
   - **Contradiction A** (STATE.md placeholder vs read-only slice 0): resolved by revising slice 0 in `phases/00-surface-cleanup.md` to "Reconcile and attest baseline" type with `STATE.md` in declared write set; slice now produces a commit.
   - **Contradiction B** (audit_refmap.py verify gate vs pre-existing baseline): resolved by amending Required Discipline #8 in `GUARDRAILS.md` to allow the documented 8-item known baseline and require slices to not introduce NEW unclassified items.
   - Additional PROTOCOL fixes: cold-start step 4 documents the lag-by-one pattern; cold-start step 7 consults STATE.md → Status as resume authority; per-turn flow reordered to commit STATE.md + checkpoint atomically with slice work; Discipline #5/#9 amended to authorize STATE.md and checkpoint in every slice's write set implicitly.
   - Original hard-stop record preserved: `checkpoints/2026-05-15T225033Z-phase00-slice00.md`.

## Out-Of-Scope Surfaces

(Per GUARDRAILS.md "Sub-Initiative Isolation" — concerns surfaced during iteration that do not belong to this initiative.)

1. **Refmap policy gap (8 unclassified missing local targets, deterministic since 2026-05-08)** — surfaced at slice 0 sanity check. Root cause: (a) `tooling/codex/audit_refmap.py:iter_markdown_files` scans gitignored `.codex/` materialized runtime; (b) `.planning/refmap/audit-refmap-policy.json` missed 8 paths in the 73f130d cleanup. Recommended fix path: architectural fix in `audit_refmap.py` to honor `.gitignore` (reviewer-gated per GUARDRAILS Reviewer-Mediated Continuation table; should be a separate `adversarial-auditor-xhigh`-mediated change outside this initiative). Minimum-policy-patch alternative would entrench tool noise as policy and is rejected per Plan reviewer 2026-05-15.
2. **`classification_counts` drift in `audit-refmap-policy.json:1-5`** — header reports `intentionally_unimported_origin_artifact: 47` but the live gate reports `43`; 4 entries' source/line referents have shifted. Also out-of-scope; should be addressed alongside item #1.

## Counters

- Carriers migrated to `mode: inject`: 0 / target ~25–30
- Carriers reclassified to `mode: add`: 3 / target 4 (Phase 0)
- Carriers staying as `mode: overwrite`: ~5 (lib *.cjs) + others TBD per phase decisions
- Net-new modifier-owned (`mode: add`): 18 (no migration; baseline)
- Inject operation kinds implemented: 0 / target ~7
- Inject unit tests passing: 0 / target TBD
- Bootstrap gate hard_failures: 4 (target: 0 after Phase 0; confirmed by Slice 4's exit verification once all 4 carriers reclassified)
- Phases complete: 0 / 11
- Slices complete: 4

## Recent Checkpoints

| Timestamp | Phase.Slice | Outcome | Note |
|---|---|---|---|
| 2026-05-15T22:50:33Z | 0.0 | paused-for-operator | Hard-stop on slice 0 spec contradictions (gsd-debugger FAIL + Plan FAIL); see `checkpoints/2026-05-15T225033Z-phase00-slice00.md` |
| 2026-05-15T23:35:21Z | 0.0 | success | Slice 0 reconcile and attest baseline; STATE.md ground-truthed against `git rev-parse HEAD`; `audit_refmap.py snapshot .` exit 0 (non-enforcing per Required Discipline #8 known baseline); no reviewer invoked |
| 2026-05-15T23:40:50Z | 0.1 | success | Slice 1 reclassify `gsd-do` skill — moved `SKILL.md` from `tooling/portable-gsd/overlay/skills/gsd-do/` to `harness_modifier/overlay/skills/gsd-do/`; manifest entry flipped to `mode: add` with new `source` path; all 3 verification gates exit 0; no reviewer invoked |
| 2026-05-15T23:43:31Z | 0.2 | success | Slice 2 reclassify `gsd-from-gsd2` skill — used `git mv` for byte-perfect rename (4528 bytes preserved); manifest entry flipped to `mode: add`; all 3 verification gates exit 0; no reviewer invoked |
| 2026-05-15T23:45:17Z | 0.3 | success | Slice 3 reclassify `gsd-plant-seed` skill — `git mv` for byte-perfect rename (3119 bytes preserved); manifest entry flipped to `mode: add`; all 3 verification gates exit 0; no reviewer invoked |

## Reviewer Decisions Log

| Timestamp (ISO-8601 UTC) | Phase.Slice | Reviewer | Verdict | One-line reasoning | Decision taken |
|---|---|---|---|---|---|
| 2026-05-15T22:45:00Z | 0.0 | gsd-debugger | FAIL | `audit_refmap.py verify .` exit 1 deterministically; 8 unclassified items; fix outside slice 0's empty write set | escalated to Plan reviewer per auto-recovery #4 |
| 2026-05-15T22:48:00Z | 0.0 | Plan | FAIL | Slice 0 spec contains internally contradictory directives; route to GUARDRAILS Hard Stops #5 | executed Hard-Stop Protocol; turn ends; goal terminated |

## Auto-Recovery Counters

Tracks resilience of the loop. The 3-consecutive-failure rule fires when any slice's `attempts` here reaches 3.

- Total reviewer invocations: 2
- Reviewer PASS verdicts: 0
- Reviewer FAIL verdicts: 2 (gsd-debugger, Plan)
- Reviewer ESCALATE verdicts: 0
- Reviewer HALT verdicts: 0
- Auto-recovery successes: 0
- Auto-recovery escalations to hard-stop: 1 (this turn)
- Slice-level retries (cumulative): 1 (the `audit_refmap.py verify .` deterministic retry; counted once because outcome was identical)
- Per-slice attempt counts (only for slices not yet completed):
  - phase 0 slice 0: **1 attempt** (hard-stopped before re-attempt; 3-consecutive-failure rule has not yet been reached, but the underlying condition will not change without operator action so re-attempt would also fail)

## Dirty-Worktree Pre-Conditions

For the loop to start cleanly (under normal operation, not paused-for-operator state):

- `git status --short` should show only the temp handoff (`docs/handoff/DELETE-AFTER-INGESTION-...md`) until Phase 0 Slice 6 deletes it
- `git diff --check` should be clean
- `bash scripts/ci/check-deterministic.sh` passed at the most recent commit (last verified: 2026-05-08, exit 0)
- `bash scripts/ci/check-bootstrap.sh` passed at the most recent commit (last verified: 2026-05-08, exit 0; surfaces 4 expected hard_failures from §1.4 of intervention-strategies)
- ~~`python3 tooling/codex/audit_refmap.py verify .` exit 0~~ — KNOWN FAILING since 73f130d (2026-05-08); see Out-Of-Scope Surfaces #1; expected exit 1 with 8 unclassified items until operator addresses

### Current actual worktree (normal operation, post-slice-0)

```
?? docs/handoff/DELETE-AFTER-INGESTION-2026-04-24-release-readiness-and-plan-004.md
```

Only the pre-declared temp-handoff item remains. It is slated for deletion in Phase 0 Slice 6 per the phase plan. All other slice 0 artifacts (STATE.md edits, this slice's checkpoint) were committed atomically with the slice's work per PROTOCOL.md "State-Update Protocol".

## Notes For The Agent

- This file is the canonical source of truth for "where are we". Any divergence from `git log` or filesystem state means the file lies; reconcile by reading the actual repo state and updating this file.
- Update this file ONLY at the end of a turn after the slice's commit lands. Never partial-update.
- If you start a turn and find this file inconsistent with `git log`, log the inconsistency and prefer `git log` as ground truth. Update this file accordingly.
- The `Last commit` field should always match `git rev-parse HEAD`.
- When a reviewer is invoked (per [REVIEWERS.md](REVIEWERS.md)), append a row to `Reviewer Decisions Log` AND record the full verdict block in the slice's checkpoint under `## Reviewer Verdict`.
- The `[GOAL-EVAL]` line at turn end is mandatory — see [PROTOCOL.md](PROTOCOL.md) "Turn-End Discipline" for exact format.
- The 3-consecutive-failure rule: if `Auto-Recovery Counters → Per-slice attempt counts` shows the same slice at 3, the next failure is an automatic hard-stop.
