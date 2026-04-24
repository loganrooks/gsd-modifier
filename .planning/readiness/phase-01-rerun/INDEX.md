# Phase 01 Rerun Readiness Package

This package tracks what must be closed before a fresh Phase 01 rerun can begin.

It exists because the repo now has enough pre-rerun doctrine, governance cleanup, and audit history that a single prose plan is no longer enough to carry the work safely across context compaction.

## Read Order

1. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
2. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
3. [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
4. active gate under [GATES/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES)

Then as needed:

- [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
- [DEFERRED.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/DEFERRED.md)
- [OPPORTUNITIES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/OPPORTUNITIES.md)
- [AUDITS/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS)
- [REVIEWS/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS)
- [RESEARCH-INTAKE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/RESEARCH-INTAKE.md)
- [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md)
- [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml)
- [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md)
- [AUDIT-SPEC-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-SPEC-TEMPLATE.md)
- [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
- [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
- [CLAUDE-REVIEW-COMMANDS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CLAUDE-REVIEW-COMMANDS.md)
- [CHECKPOINT-LEDGER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-LEDGER.md)
- [DEVIATIONS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/DEVIATIONS.md)
- [REGRESSION-CHECKLIST.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REGRESSION-CHECKLIST.md)
- [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)

## Source-Of-Truth Hierarchy

- stable sequence and gate philosophy: `PLAN.md`
- live mutable state: `STATUS.md` + `STATE.yaml`
- checkpoint evidence and verdicts: `GATES/`
- task routing: `TASKS.md`
- deferrals: `DEFERRED.md`
- non-blocking quality upside: `OPPORTUNITIES.md`
- readiness audit specs and outputs: `AUDITS/`
- stored review outputs and reusable review specs: `REVIEWS/`
- research absorption / consequences: `RESEARCH-INTAKE.md`
- checkpoint review expectations: `CHECKPOINT-REVIEW-MATRIX.md`
- machine-readable checkpoint review rules: `REVIEW-POLICY.yaml`
- explicit review spec shape: `REVIEW-TEMPLATE.md`
- explicit audit / adjudication / reread spec shape: `AUDIT-SPEC-TEMPLATE.md`
- epistemic doctrine for post-verificationist / post-falsificationist gap exposure: `POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`
- comparison doctrine for competing audits/reviews: `AUDIT-COMPARISON-POLICY.md`
- concrete Anthropic Claude review invocations: `CLAUDE-REVIEW-COMMANDS.md`
- commit history of readiness boundaries: `CHECKPOINT-LEDGER.md`
- sequence changes: `DEVIATIONS.md`

## Current Active Checkpoint

- `Checkpoint 5`: conditional harness / GSD follow-through
