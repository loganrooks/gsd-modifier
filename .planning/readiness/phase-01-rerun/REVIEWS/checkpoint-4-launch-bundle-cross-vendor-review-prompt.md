# Checkpoint 4 Launch Bundle Cross-Vendor Review Prompt

Review the Checkpoint 4 workflow / harness excellence-audit spec bundle before it is checkpointed or used to launch any Checkpoint 4 audit lanes.

This is a cross-vendor adequacy review of the launch bundle, not a replacement audit.

## Review Stance

- Review against a high bar, not a minimal pass bar.
- Be firm, specific, and justified when the bundle is settling for adequacy.
- Do not be rude or arbitrarily harsh.
- Try seriously to falsify launch-readiness before declaring the bundle strong.
- Do not treat `technically covers the lanes` as sufficient if a stronger and clearer bundle was reasonably achievable.
- Criticism should be justified in terms of rigor, auditability, future viability, architectural soundness, or quality of judgment.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
4. [GATES/checkpoint-4.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md)
5. [AUDITS/checkpoint-3-workflow-harness-scope-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md)
6. [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md)
7. [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml)

Then review this bundle:

- [AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md)
- [AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams-spec.md)
- [AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence-spec.md)
- [AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence-spec.md)
- [AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence-spec.md)
- [AUDITS/checkpoint-4-cross-lane-seam-synthesis-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis-spec.md)
- [AUDITS/checkpoint-4-converged-synthesis-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-converged-synthesis-spec.md)

## Review Questions

- does the bundle preserve the accepted Checkpoint 3 envelope rather than quietly collapsing it?
- does each lane own a genuinely distinct excellence question, or is the split still fuzzy?
- is the seam synthesis strong enough to decide doc vs protocol vs machinery ownership rather than just aggregating notes?
- is the converged synthesis strong enough to justify whether Checkpoint 5 opens?
- does the Codex lane correctly require official and recent qualified unofficial evidence where that matters?
- are the strongest justified criticism and strategic opportunity surfaces explicit enough across the bundle?
- what is the strongest justified criticism of this launch bundle?
- what is merely acceptable here but should be stronger?
- what would fail later stringent audit by strong engineers, designers, or researchers?
- what quality opportunity is being left unused?

## Output Requirements

Emit the full review as markdown to stdout using the structure from [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md).

Do not modify repo files directly for this review. The caller will persist the output to the intended review artifact path.
