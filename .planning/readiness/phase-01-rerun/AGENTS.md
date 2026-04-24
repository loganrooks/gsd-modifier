# AGENTS.md

This file applies when working inside `.planning/readiness/phase-01-rerun/`.

Read it after:

- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)

This subtree is a readiness-control package, not product canon.

## Package Purpose

- keep Phase 01 rerun preparation explicit across context compaction
- make checkpoint status, open tasks, deferrals, and commit boundaries visible
- stop readiness work from drifting back into ambient session memory

## Required Read Order

When entering this subtree, read in this order:

1. [INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md)
2. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
5. the active checkpoint file under [GATES/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES)
6. [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md) and [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml) when deciding review depth or closure

## Update Protocol

- Keep `PLAN.md` stable unless the sequence or gate philosophy changes.
- Update `STATUS.md` and `STATE.yaml` whenever:
  - the active checkpoint changes
  - a blocking finding appears or is cleared
  - commit readiness changes
  - the immediate next action changes
- Update the active gate file whenever a checkpoint is reviewed, reopened, or closed.
- Record meaningful sequence changes in `DEVIATIONS.md`, not only by silently editing `PLAN.md`.
- Record checkpoint commits in `CHECKPOINT-LEDGER.md`.
- Put non-blocking carry-forward items in `DEFERRED.md`, not in `STATUS.md`.
- Put non-blocking but meaningful quality-upside items in `OPPORTUNITIES.md` rather than losing them inside review prose.

## Package Rules

- Do not treat this package as canon. It tracks readiness work around canon and governance.
- Do not open a later checkpoint as if active while an earlier blocking checkpoint remains unresolved.
- Do not mark a checkpoint `done` only because it is unblocked; record whether it is merely acceptable, strong, or truly ready to carry forward.
- If a new finding changes the sequence materially, update `PLAN.md`, `STATUS.md`, `STATE.yaml`, and `DEVIATIONS.md` in the same change.
- If a delegated worker edits readiness-relevant artifacts, update this package after reviewing and dispositioning the worker output.
- Do not let the same lane both author and solely close a major checkpoint. Use an independent reviewer and follow `REVIEW-POLICY.yaml`.
