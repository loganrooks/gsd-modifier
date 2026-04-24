# Checkpoint 3 GSD Agent Doctrine And Role Contracts Spec

## Purpose

Deep-map the active repo-local GSD agent-role contracts and shared doctrine surfaces as part of Checkpoint 3.

This is still mapping work, not the later excellence audit.

## Why This Lane Exists Now

The accepted initial GSD surface map concluded that the repo-local GSD harness was too broad for one honest pass and explicitly recommended a split between:

- phase-critical workflow chain plus artifact contracts
- active agent-role contracts plus shared doctrine
- runtime/config/overlay truth

This lane covers the second of those deeper-mapping units so Checkpoint 3 can finish the GSD-side mapping honestly before the overall scope synthesis runs.

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

- active `.codex/agents/*.md` surfaces relevant to discuss, research, planning, checking, execution, and verification
- `.codex/get-shit-done/references/gates.md`
- `.codex/get-shit-done/references/checkpoints.md`
- `.codex/get-shit-done/references/agent-contracts.md`
- `.codex/get-shit-done/references/verification-patterns.md`

Inspect `.toml` siblings only where they materially affect the runtime seam or reveal drift.

## Core Questions

- where do shared doctrine, gate semantics, and handoff expectations actually live?
- which agent-role contracts are active and load-bearing?
- how do role contracts and shared doctrine jointly shape later planning, checking, execution, and verification quality?
- where is there possible drift between declared role contracts, shared doctrine, and repo governance?
- which seams are reversal-sensitive and therefore require later excellence audit rather than casual assumption?

## Output

Write:

- [checkpoint-3-gsd-agent-doctrine-and-role-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md)

This artifact must be good enough to serve as a direct input to:

- [checkpoint-3-gsd-scope-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-scope-synthesis.md)
- the later Checkpoint 4 excellence-audit lane that covers role contracts, shared doctrine, and repo-governance seams

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Shared Doctrine Map`
- `Active Agent-Role Contract Map`
- `Role Doctrine / Repo Governance Seams`
- `Reversal-Sensitive Boundaries`
- `Broad but Secondary Surfaces`
- `Narrow but Structurally Decisive Surfaces`
- `Implications For The Later Excellence Audit`
- `Open Inquiry Debt`

## Constraints

- do not patch files
- do not treat all agent files as equally important by filename alone
- distinguish operative doctrine from stale or drifted surfaces
- do not smuggle in later Checkpoint 4 conclusions under the guise of mapping
- prefer readiness-package artifacts as authority for why this lane exists; use current thread corrections only if they have not yet been rendered into the package
- cite concrete files and lines

## Lane

- classification: `replanning/revision/gap-filling`
- model / reasoning: `gpt-5.4 xhigh`
