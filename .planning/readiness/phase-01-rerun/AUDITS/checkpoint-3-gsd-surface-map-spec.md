# Checkpoint 3 GSD Surface Map Spec

## Purpose

Map the current repo-local GSD harness honestly enough to justify the later Checkpoint 4 excellence-audit envelope.

This lane must not reduce the harness to "a collection of skills" if the real load-bearing unit is broader.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
4. [checkpoint-3.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-3.md)
5. [checkpoint-3-workflow-harness-scope-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-launch-spec.md)

Then inspect the repo-local GSD surface, including at minimum:

- `.codex/get-shit-done/contexts/`
- `.codex/get-shit-done/references/`
- `.codex/get-shit-done/templates/`
- `.codex/get-shit-done/workflows/`
- `.codex/skills/`
- `.codex/agents/`
- `.codex/gsd-local-patches/` where local overlays materially affect the runtime

## Core Questions

- what are the real load-bearing units of the repo-local GSD harness?
- should the later deeper audit reason primarily about:
  - skills
  - workflow stages
  - shared references/templates
  - agent-role contracts
  - cross-layer seams
- where do planning quality, research quality, execution quality, verification quality, and auditability actually live inside this harness?
- what is broad but not load-bearing, and what looks narrow but actually controls a lot?

## Split Rule

If the GSD surface is too broad to map honestly in one pass, do not fake completeness.

Instead:

- write the partial map you can justify
- state that a deeper split is required
- propose the sublanes needed, for example by workflow stage, shared references/templates, or skill family
- explain why the split is load-bearing

## Output

Write:

- [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `GSD Surface Inventory`
- `Candidate Units Of Analysis`
- `Load-Bearing GSD Layers`
- `Broad but Low-Leverage Surfaces`
- `Narrow but High-Leverage Surfaces`
- `Cross-Layer Seams into Codex or repo governance`
- `If a split is required`
- `What Checkpoint 4 must inspect`

## Constraints

- do not patch files
- do not assume the harness can be represented just by listing skills
- cite concrete files and lines

## Lane

- classification: `replanning/revision/gap-filling`
- model / reasoning: `gpt-5.4 xhigh`
