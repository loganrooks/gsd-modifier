# Checkpoint 3 Scope Synthesis Spec

## Purpose

Synthesize the Codex and GSD mapping outputs into the actual Checkpoint 3 workflow / harness scope audit.

## Preconditions

Do not run this synthesis until:

- the Codex surface map exists
- the initial GSD surface map exists
- if the initial GSD mapping fired the split trigger, the deeper GSD sublane outputs exist
- if the initial GSD mapping fired the split trigger, the GSD-only synthesis exists

## Inputs

- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [checkpoint-3-workflow-harness-scope-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-launch-spec.md)
- [checkpoint-3-codex-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-codex-surface-map.md)
- [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
- [checkpoint-3-gsd-scope-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-scope-synthesis.md)
- [checkpoint-3.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-3.md)
- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)

## Output

Write:

- [checkpoint-3-workflow-harness-scope-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Integrated Harness Map`
- `Recommended Unit Of Analysis For Checkpoint 4`
- `Why this envelope is defensible`
- `What looks broad but is not load-bearing`
- `What looks narrow but is actually load-bearing`
- `What remains machinery-owned follow-through for Checkpoint 5`
- `How Checkpoint 3 resolved the GSD split`
- `Planning Handoff`

## Decision Discipline

- do not optimize for the smallest possible audit envelope
- do not choose a unit of analysis just because it is easiest to inspect
- if the initial GSD mapping fired the split trigger, treat the GSD-only synthesis as a required input rather than smoothing the split away
- cite the input mapping artifacts and their specific sections or line ranges when making scope claims; do not produce summary claims a later reader cannot trace

## Lane

- classification: `replanning/revision/gap-filling`
- model / reasoning: `gpt-5.4 xhigh`
