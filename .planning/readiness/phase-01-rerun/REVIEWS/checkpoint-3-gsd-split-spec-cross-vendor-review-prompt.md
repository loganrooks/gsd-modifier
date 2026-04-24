# Checkpoint 3 GSD Split Spec Cross-Vendor Review Prompt

Review the Checkpoint 3 GSD split-spec bundle for adequacy before any deeper GSD mapping lanes are launched.

This is a review of spec quality and readiness-package coherence, not a review of the underlying GSD harness itself.

## Governing Context

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
4. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
5. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
6. [GATES/checkpoint-3.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-3.md)
7. [AUDITS/checkpoint-3-workflow-harness-scope-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-launch-spec.md)
8. [AUDITS/checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)

Then review these target specs:

1. [AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts-spec.md)
2. [AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts-spec.md)
3. [AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth-spec.md)
4. [AUDITS/checkpoint-3-gsd-scope-synthesis-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-scope-synthesis-spec.md)
5. [AUDITS/checkpoint-3-scope-synthesis-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-scope-synthesis-spec.md)

## Review Questions

Assess whether the bundle is strong enough to launch without creating later audit confusion or scope distortion.

Focus on:

- whether the motivating grounds are explicit and properly anchored in readiness-package state
- whether the split is correctly located inside Checkpoint 3 rather than leaked into Checkpoint 4
- whether each sublane is specific enough to avoid overlap while still broad enough to avoid blind spots
- whether the GSD-only synthesis is correctly staged before the overall Codex+GSD synthesis
- whether any important input, output, or constraint is still underspecified
- whether the specs are vulnerable to agents drifting into premature excellence judgment rather than honest mapping
- whether the package state is coherent with the spec bundle

## Output Requirements

Write a review artifact with:

- `Verdict`
- `Findings`
- `What Is Already Strong`
- `What Must Change Before Launch`
- `What Can Wait Until Later`

Findings should be ordered by severity and cite concrete file lines.

If the bundle is launch-ready, say so explicitly.

If not, say exactly what must be fixed before launching the deeper GSD mapping lanes.
