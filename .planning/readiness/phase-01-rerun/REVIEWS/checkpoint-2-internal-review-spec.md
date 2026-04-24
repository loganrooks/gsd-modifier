# Checkpoint 2 Internal Review Spec

Use this as the base spec for independent verification rereads of the Checkpoint 2 governance-doc normalization patch.

## Purpose

Test whether the Checkpoint 2 patch improved ownership, slimness, and abstraction without:

- erasing load-bearing distinctions earned in `05-gap-closure`
- making the governance layer deceptively tidy by removing necessary prompt-time reminders
- collapsing machinery-owned follow-through into prose-only cleanup
- or leaving major duplication/ownership drift unresolved

## Governing Inputs

- [GATES/checkpoint-2.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-2.md)
- [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md)
- [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml)
- [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md)
- [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
- [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
- [AUDITS/checkpoint-1-governance-doc-normalization-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit.md)
- the current patched versions of:
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
  - [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
  - [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
  - [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md)

## Review Task

- verify that detailed claim-marker ownership now sits primarily in `.planning/CLAIM-TYPES.md`
- verify that root and planning `AGENTS.md` still retain enough prompt-time guidance after slimming
- verify that `WORKFLOW.md` kept durable workflow posture while trimming machinery-current detail
- verify that the patch does not erase anti-pass/fail, non-foreclosure, or future-flexibility doctrine
- surface only material findings

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
- state whether cross-vendor review should be run now under Checkpoint 2 policy

## Rerun Guidance

- Reuse this spec for later Checkpoint 2 rereads.
- On reruns, add only a short delta note covering:
  - what changed since the last review
  - the current baseline commit or patch snapshot
  - the new output file path under `REVIEWS/`
