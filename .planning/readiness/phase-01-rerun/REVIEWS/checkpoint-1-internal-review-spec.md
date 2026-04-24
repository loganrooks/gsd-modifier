# Checkpoint 1 Internal Review Spec

Use this as the base spec for independent verification rereads of the Checkpoint 1 governance-doc normalization audit.

## Purpose

Test whether the Checkpoint 1 audit is strong enough to guide Checkpoint 2 patching without:

- guessing at owner boundaries
- overstating machinery-owned follow-through
- under-specifying the real normalization hotspots
- or quietly reintroducing pass/fail thinness into governance doctrine

## Governing Inputs

- [GATES/checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md)
- [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md)
- [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml)
- [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md)
- [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
- [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
- [checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md)
- [checkpoint-1-governance-doc-normalization-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit.md)

## Review Task

- verify that the audit distinguishes:
  - doc-local cleanup
  - cross-doc normalization
  - machinery-owned follow-through
  - strategic-opportunity
- verify that its main hotspots are concretely supported by file-line citations
- verify that it identifies likely Checkpoint 2 patch units clearly enough to guide a bounded patch pass
- verify that it does not quietly collapse Checkpoint 3 scoping into markdown cleanup
- surface only material findings; do not inflate stylistic noise

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

- Reuse this spec for later Checkpoint 1 rereads.
- On reruns, add only a short delta note covering:
  - what changed since the last review
  - the current baseline commit or artifact snapshot
  - the new output file path under `REVIEWS/`
