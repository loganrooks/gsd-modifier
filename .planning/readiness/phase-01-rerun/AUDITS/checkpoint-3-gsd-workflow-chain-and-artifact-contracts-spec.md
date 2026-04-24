# Checkpoint 3 GSD Workflow Chain And Artifact Contracts Spec

## Purpose

Deep-map the repo-local GSD phase-critical workflow chain and its shared artifact contracts as part of Checkpoint 3.

This is still mapping work, not the later excellence audit.

## Why This Lane Exists Now

The accepted initial GSD surface map concluded that the repo-local GSD harness was too broad for one honest pass and explicitly recommended a split between:

- phase-critical workflow chain plus artifact contracts
- active agent-role contracts plus shared doctrine
- runtime/config/overlay truth

This lane covers the first of those deeper-mapping units so Checkpoint 3 can finish the GSD-side mapping honestly before the overall scope synthesis runs.

Primary motivating readiness surfaces:

1. [checkpoint-3-workflow-harness-scope-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-launch-spec.md)
2. [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
3. [checkpoint-3.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-3.md)
4. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
5. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
6. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
4. [checkpoint-3.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-3.md)
5. [checkpoint-3-workflow-harness-scope-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-launch-spec.md)
6. [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
7. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
8. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
9. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)

Then inspect, at minimum:

- `.codex/get-shit-done/workflows/discuss-phase.md`
- `.codex/get-shit-done/workflows/research-phase.md`
- `.codex/get-shit-done/workflows/plan-phase.md`
- `.codex/get-shit-done/workflows/execute-phase.md`
- `.codex/get-shit-done/workflows/verify-work.md`
- `.codex/get-shit-done/templates/context.md`
- `.codex/get-shit-done/templates/phase-prompt.md`
- `.codex/get-shit-done/templates/config.json`
  Inspect this file for its artifact-contract role in the workflow chain, not as the final runtime/overlay truth surface.

## Core Questions

- where does the phase-critical lifecycle actually live?
- how do steering, research, planning, execution, and verification connect across artifacts?
- which shared artifact contracts are genuinely load-bearing for later excellence judgment?
- where are the preserve-only seams, future-awareness seams, gate seams, and handoff seams in this chain?
- what in this chain is broad but secondary, and what is narrow but structurally decisive?

## Output

Write:

- [checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md)

This artifact must be good enough to serve as a direct input to:

- [checkpoint-3-gsd-scope-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-scope-synthesis.md)
- the later Checkpoint 4 excellence-audit lane that covers the workflow chain and artifact-contract surface

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Phase-Critical Workflow Map`
- `Artifact Contract Map`
- `Preserve-Only And Future-Awareness Seams`
- `Broad but Secondary Surfaces`
- `Narrow but Structurally Decisive Surfaces`
- `Implications For The Later Excellence Audit`
- `Open Inquiry Debt`

## Constraints

- do not patch files
- do not judge whether the chain is excellent yet; map what it is and where later scrutiny should concentrate
- do not smuggle in later Checkpoint 4 conclusions under the guise of mapping
- prefer readiness-package artifacts as authority for why this lane exists; use current thread corrections only if they have not yet been rendered into the package
- cite concrete files and lines

## Lane

- classification: `replanning/revision/gap-filling`
- model / reasoning: `gpt-5.4 xhigh`
