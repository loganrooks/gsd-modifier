# Checkpoint 2 Cross-Vendor Review Prompt

You are performing the Checkpoint 2 cross-vendor reread for the Phase 01 rerun readiness package in this repo.

## Review Mode

- Vendor: Anthropic Claude
- Intended lane: `claude-sonnet-4-6 --effort high`
- Checkpoint: `2`
- Purpose: review the current governance-doc normalization patch before checkpoint closure

## Baseline

- Baseline commit before the patch: `97bd603`
- Current patch snapshot: uncommitted working-tree changes in:
  - `AGENTS.md`
  - `.planning/AGENTS.md`
  - `.planning/CLAIM-TYPES.md`
  - `WORKFLOW.md`

## Governing Inputs

Read these first:

1. `AGENTS.md`
2. `.planning/AGENTS.md`
3. `.planning/readiness/phase-01-rerun/GATES/checkpoint-2.md`
4. `.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md`
5. `.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml`
6. `.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md`
7. `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit.md`
8. `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-2-internal-review-r1.md`

Then inspect the current patch against the baseline commit.

## Review Task

Determine whether the current Checkpoint 2 patch:

- improves ownership and slimness without erasing load-bearing distinctions
- moves detailed claim-marker ownership into `.planning/CLAIM-TYPES.md` cleanly
- keeps enough prompt-time guidance in the two `AGENTS.md` files
- keeps `WORKFLOW.md` focused on durable workflow posture rather than current harness-state detail
- preserves the anti-pass/fail, non-foreclosure, and future-flexibility doctrine earned earlier in the repo

Surface only material findings.

Do not suggest gratuitous churn just because a different wording might also work.

## Output Requirements

Write the response as a readiness review artifact in the shape of `.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md`.

Use this header information:

- checkpoint: `Checkpoint 2 - Governance-doc normalization patch`
- artifact(s) under review:
  - `AGENTS.md`
  - `.planning/AGENTS.md`
  - `.planning/CLAIM-TYPES.md`
  - `WORKFLOW.md`
- review mode: `cross-vendor-reread`
- authoring lane: `orchestrator patch lane`
- reviewer: `Claude cross-vendor reviewer`
- model / reasoning or vendor: `claude-sonnet-4-6 high`
- baseline commit / artifact snapshot: `97bd603` plus current uncommitted patch snapshot
- independence relationship: `cross-vendor`

For any material finding:

- cite concrete file lines
- state the gap classification explicitly

If you find no material issues, say so directly.

End by stating:

- whether the patch is `ready-to-carry-forward`
- whether Checkpoint 2 should close now or be revised first
