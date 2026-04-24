# Checkpoint 5 R5.18 Launch Bundle Spec

Purpose: split `R5.18` into a small implementation bundle so the patch wave does not collapse boundary decisions, patch-now trunks, and contradiction-ledger obligations into one blurry spec.

## Why Split

The revised `R5.18` boundary now contains three different kinds of work:

1. boundary decisions that must be made before patching
2. convergent patch-now trunks
3. post-patch integration / ledger / review obligations

One monolithic implementation spec would recreate the exact failure mode that `R5.17` and `R5.19` were commissioned to expose:

- flattening unlike evidence grades into one patch wave
- letting unresolved boundary choices govern by omission
- hiding contradiction ownership inside implementation prose

## Bundle Shape

### `R5.18a1`

Current-wave boundary and contradiction-ledger decisions.

This lane resolves:

- `gsd-research-phase`
- `ship.md`
- `autonomous.md`
- non-TDD `checkpoints.md`
- `summary.md`
- router-pair treatment
- `gates.md` / `revision-loop.md` / `gate-prompts.md`
- live researcher/planner/checker pairing
- `.codex/agents/gsd-code-reviewer.toml`
- active-slice vs parked-remainder treatment for `R5.7`
- explicit park-or-reactivate treatment for `R5.8`
- non-doctrinal status of the new exclusion heuristics
- contradiction-ledger entries for all non-first-wave live items

### `R5.18a2`

Named-later-lane and quiet-drop adjudication.

This lane resolves:

- live config/default posture alignment
- lifecycle-wide carry-forward outside `progress` / `transition`
- cheap helper/mechanical disposition ergonomics
- canonical local verify plus narrow repo-integrity CI
- remote review-owner routing / issue-PR-MR templates / linked review artifacts
- worker-first exploration / one-active-substantive-task machinery
- any other broader 2026-04-15 remainder that `R5.18a1` leaves outside the current wave
- the challenge rows from [checkpoint-5-r5-18a-boundary-challenge-checklist.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a-boundary-challenge-checklist.md)

### `R5.18b`

Review / planning consumer-chain corrective wave.

This lane implements the convergent review/planning trunk and any router surfaces that `R5.18a1` explicitly promotes into the same wave, subject to any restrictions or later-lane naming from `R5.18a2`.

### `R5.18c`

Completion / routing / runtime-authority corrective wave.

This lane implements the convergent chain-tail trunk plus any live `.codex/agents` runtime counterparts or adjacent reference/runtime files that `R5.18a1` explicitly promotes, subject to any restrictions or later-lane naming from `R5.18a2`.

### `R5.18d`

Integration, ledger, and checkpoint-review preparation.

This lane verifies that:

- `R5.18a1/a2` decisions were actually carried into `b/c`
- contradiction-ledger entries exist for every kept-out live item
- wrapper/routing asymmetries are either paired or explicitly defended
- package truth is updated
- the resulting patch set is reviewable under Checkpoint 5 closure rules

## Refinement Level

This is refined enough.

It is more refined than one monolithic `R5.18` spec, but less fragmented than turning every live boundary file into its own mini-lane.

The correct refinement level here is:

- two decision lanes
- two patch waves
- one integration / review-prep lane

Not:

- one giant implementation spec
- and not ten tiny specs that would destroy coherence

## Sequencing

1. run `R5.18a1`
2. run `R5.18a2`
3. then run `R5.18b` and `R5.18c` in parallel where `R5.18a1` allows and `R5.18a2` does not reopen or relocate the surface
4. then run `R5.18d`
5. then internal and cross-vendor review of the resulting patch set

## Governing Inputs

1. [checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md)
2. [checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md)
3. [checkpoint-5-r5-19e-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19e-adjudication-reread-internal-r1.md)
4. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
5. [checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-launch-spec.md)
6. [checkpoint-5-r5-18a2-later-lane-and-quiet-drop-adjudication-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a2-later-lane-and-quiet-drop-adjudication-spec.md)
7. [checkpoint-5-r5-18-vs-2026-04-15-governance-audit-split-synthesis-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-split-synthesis-internal-r1.md)
8. [checkpoint-5-r5-18a-boundary-challenge-checklist.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a-boundary-challenge-checklist.md)
