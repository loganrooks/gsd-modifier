# Readiness Plan Deviations

This file records meaningful sequence changes instead of letting them disappear into silent plan edits.

## Deviation Types

Use one or more of:

- `operational-restructure`
  Control surfaces changed, but the sequence did not.
- `sequence-reorder`
  Checkpoint order or dependency order changed.
- `upstream-reactivation`
  A later finding reopened an earlier checkpoint or prior doctrine/harness layer.
- `new-blocker`
  A newly recognized blocker changed what must happen next.
- `strategic-opportunity`
  A non-blocking but high-upside finding changed what should be tracked for best later outcomes.
- `evidence-overturn`
  New evidence materially changed what the package believed.
- `user-directed-change`
  The user explicitly changed the route or priority.

## Logging Format

For each deviation, record:

- type:
- date:
- trigger:
- effect on sequence:
- package surfaces changed:
- whether user consultation was required:

## 2026-04-15

- type: `operational-restructure`
- date: 2026-04-15
- trigger: top-level readiness plan was too fragile to survive context compaction as a single file
- effect on sequence: none
- package surfaces changed:
  - `PLAN.md`
  - `STATUS.md`
  - `STATE.yaml`
  - gate files
  - task tracking
  - deferrals
  - checkpoint logging
- whether user consultation was required: no

- type: `evidence-overturn`, `upstream-reactivation`, `user-directed-change`
- date: 2026-04-15
- trigger: the accepted Checkpoint 4 workflow-chain findings and later user challenge showed that the first Checkpoint 5 launch spec had overgeneralized a Checkpoint 3 scoping heuristic and dropped workflow follow-through that had already been earned
- effect on sequence: Checkpoint 5 remains active but its scope widens from Track A/B/C only into `Track A/B/C + workflow-chain follow-through + secondary rerun-critical wrapper alignment`; the existing Checkpoint 5 reviews become partial historical evidence instead of closure evidence
- package surfaces changed:
  - `AUDITS/checkpoint-5-reactivated-launch-spec.md`
  - `AUDITS/checkpoint-5-bounded-follow-through-launch-spec.md`
  - `GATES/checkpoint-5.md`
  - `STATUS.md`
  - `TASKS.md`
  - `STATE.yaml`
  - `PLAN.md`
  - `CHECKPOINT-LEDGER.md`
  - Checkpoint 5 implementation/review notes
- whether user consultation was required: yes

- type: `operational-restructure`, `new-blocker`, `user-directed-change`
- date: 2026-04-15
- trigger: the user interrupted a costly cross-vendor rerun attempt after artifact-first review discipline was violated; the failure was later recorded as `cross-vendor-review-artifact-authority-failure`
- effect on sequence: the checkpoint now preserves the first internal and cross-vendor reviews as pre-reactivation historical evidence, requires artifact-first review handling going forward, and does not erase the failed rerun-handling episode during correction
- package surfaces changed:
  - `DEVIATIONS.md`
  - `STATUS.md`
  - Checkpoint 5 reactivation records
- whether user consultation was required: yes
