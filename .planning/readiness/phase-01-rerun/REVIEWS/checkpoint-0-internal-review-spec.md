# Checkpoint 0 Internal Review Spec

Use this as the base spec for internal verification rereads of Checkpoint 0.

## Purpose

Test whether the repaired `01`-`06` governance audit bundle is now concretely auditable and strong enough to cite downstream without guessing at citation intent, support mode, or source basis.

## Governing Inputs

- [GATES/checkpoint-0.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-0.md)
- [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md)
- [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml)
- [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md)
- [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
- [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
- [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md)
- [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md)
- [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md)

## Target Artifacts

- `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md`

## Review Task

- verify that internal cited claims land on supporting lines rather than blank lines or section headers
- verify that support markers match the actual citation/inference structure
- verify that direct external engagement is marked as direct rather than traceable-only
- verify that `06` meaningfully incorporates the external-comparative tightening from `08`
- surface only real material findings; do not inflate mechanical noise

## Default Lane

- review mode: `internal-verification-agent`
- model / reasoning: `gpt-5.4 high`
- independence relationship: `independent`

## Output Requirements

- write the review artifact under [REVIEWS/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS)
- use [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md)
- cite concrete file lines for any finding
- state the gap classification explicitly
- state whether the independent-review requirement is satisfied
- state whether cross-vendor review was available, whether it was necessary, and why

## Rerun Guidance

- Reuse this spec for later Checkpoint 0 rereads.
- Do not rewrite the whole spec unless the gate scope changes materially.
- For a rerun, add only a short delta note covering:
  - what changed since the last review
  - the current baseline commit or artifact snapshot
  - the new output file path under `REVIEWS/`
