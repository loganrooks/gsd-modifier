# Checkpoint 3 GSD Runtime Config Overlay Truth Spec

## Purpose

Deep-map the repo-local GSD runtime/config/overlay truth surface as part of Checkpoint 3.

This lane exists to make the actual harness surface legible before the later excellence audit judges it.

## Why This Lane Exists Now

The accepted initial GSD surface map concluded that the repo-local GSD harness was too broad for one honest pass and explicitly recommended a split between:

- phase-critical workflow chain plus artifact contracts
- active agent-role contracts plus shared doctrine
- runtime/config/overlay truth

This lane covers the third of those deeper-mapping units so Checkpoint 3 can finish the GSD-side mapping honestly before the overall scope synthesis runs.

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

- `scripts/setup-portable-gsd.sh`
- `.codex/gsd-local-patches/backup-meta.json`
- `.planning/config.json`
- `.codex/get-shit-done/templates/config.json`
  Inspect this file as the stock baseline for overlay comparison; workflow-chain implications belong to the workflow/artifact-contract lane.
- the runtime surfaces that resolve active agents or config behavior
- `.codex/agents/*.md`
- representative `.codex/agents/*.toml` files where runtime drift or dual-authority is plausible

## Core Questions

- what is the actual runtime and overlay truth surface for repo-local GSD in this repo?
- which local overlays materially change upstream behavior?
- where do config, install, runtime resolution, and agent-surface drift create reversal-sensitive seams?
- what should later Checkpoint 4 treat as declared doctrine versus actual runtime behavior that must be verified?
- where are the narrow but high-consequence surfaces that could mislead later auditors if left fuzzy?

## Output

Write:

- [checkpoint-3-gsd-runtime-config-overlay-truth.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md)

This artifact must be good enough to serve as a direct input to:

- [checkpoint-3-gsd-scope-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-scope-synthesis.md)
- the later Checkpoint 4 excellence-audit lane that covers runtime truth, config truth, overlay truth, and resolution seams

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Runtime And Overlay Truth Map`
- `Config Surface Map`
- `Agent-Surface And Resolution Seams`
- `Reversal-Sensitive Boundaries`
- `Broad but Secondary Surfaces`
- `Narrow but Structurally Decisive Surfaces`
- `Implications For The Later Excellence Audit`
- `Open Inquiry Debt`

## Constraints

- do not patch files
- do not assume declared config surfaces equal effective runtime behavior
- do not smuggle in later Checkpoint 4 conclusions under the guise of mapping
- prefer readiness-package artifacts as authority for why this lane exists; use current thread corrections only if they have not yet been rendered into the package
- cite concrete files and lines

## Lane

- classification: `replanning/revision/gap-filling`
- model / reasoning: `gpt-5.4 xhigh`
