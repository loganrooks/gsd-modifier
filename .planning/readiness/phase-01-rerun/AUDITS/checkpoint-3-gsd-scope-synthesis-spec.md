# Checkpoint 3 GSD Scope Synthesis Spec

## Purpose

Synthesize the initial GSD surface map and the deeper GSD mapping sublanes into the final GSD-side Checkpoint 3 scope result.

This synthesis resolves the GSD mapping envelope before the overall Codex+GSD scope synthesis runs.

## Why This Lane Exists Now

The initial GSD surface map already established that the repo-local GSD side could not be mapped honestly in one pass.

That means Checkpoint 3 now needs an intermediate GSD-only synthesis so the overall Codex+GSD scope synthesis does not have to reason directly over four separate GSD mapping artifacts plus the Codex map at once.

Primary motivating readiness surfaces:

1. [checkpoint-3-workflow-harness-scope-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-launch-spec.md)
2. [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
3. [checkpoint-3.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-3.md)
4. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
5. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
6. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)

The synthesis must still honor the standing claim-typing, source-basis, and research-quality discipline from:

- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)

## Preconditions

Do not run this synthesis until all of the following exist:

- [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
- [checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md)
- [checkpoint-3-gsd-agent-doctrine-and-role-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md)
- [checkpoint-3-gsd-runtime-config-overlay-truth.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md)

## Inputs

- [checkpoint-3-workflow-harness-scope-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-launch-spec.md)
- [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
- [checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md)
- [checkpoint-3-gsd-agent-doctrine-and-role-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md)
- [checkpoint-3-gsd-runtime-config-overlay-truth.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md)
- [checkpoint-3.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-3.md)
- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
- [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
- [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)

## Output

Write:

- [checkpoint-3-gsd-scope-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-scope-synthesis.md)

This artifact must be good enough to serve as a direct input to:

- [checkpoint-3-workflow-harness-scope-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md)
- the later Checkpoint 4 excellence-audit lanes that consume the resolved GSD-side map

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Resolved GSD Harness Map`
- `Why The GSD Split Was Load-Bearing`
- `Final GSD Unit Of Analysis For Checkpoint 4`
- `What Can Stay Out Of Scope For Checkpoint 4`
- `Reversal-Sensitive Boundaries`
- `What Remains Machinery-Owned Follow-Through For Checkpoint 5`
- `Planning Handoff`

## Decision Discipline

- do not collapse the sublane outputs back into one generic GSD summary
- do not optimize for the smallest possible GSD audit envelope
- preserve the distinction between mapped scope and later excellence judgment
- prefer readiness-package artifacts as authority for why this synthesis exists; use current thread corrections only if they have not yet been rendered into the package
- cite the input mapping artifacts and their specific sections or line ranges when making scope claims; do not produce summary claims a later reader cannot trace

## Lane

- classification: `replanning/revision/gap-filling`
- model / reasoning: `gpt-5.4 xhigh`
