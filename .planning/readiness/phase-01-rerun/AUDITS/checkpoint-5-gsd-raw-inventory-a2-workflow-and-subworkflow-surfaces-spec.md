# Checkpoint 5 GSD Raw Inventory A2: Workflow And Subworkflow Surfaces

## Purpose

Inventory the main workflow families and the sub-workflows or internal-only flows that make the current high-level picture too simple.

This lane is about the workflow layer as a high-level system, not a deep contract zoom into any one family.

## Audit Stance

- terrain-mapping
- hidden-subflow challenge
- anti-simple-mainline bias

Biases to resist:

- mapping only discuss/plan/execute/review/verify and ignoring internal bridges
- treating internal-only flows as implementation detail instead of topology
- assuming a workflow family is represented just because its headline file is on a diagram

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md)
4. [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md)
5. [checkpoint-5-gsd-upstream-baseline-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-baseline-schema.md)
6. [checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md)

## Primary Surfaces

Inspect at minimum:

- `.codex/get-shit-done/workflows/`
- wrapper-to-workflow references where needed to locate internal bridges

## Questions

- what workflow families exist at high level?
- what sub-workflows or internal-only bridges are load-bearing?
- which workflows emit artifacts or state that the current map underrepresents?
- which flows route to other workflows implicitly?
- which workflow surfaces are missing or weakly placed in the current map?
- which workflow surfaces remain cross-cutting or hard to classify?

## Output

Write:

- [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Workflow Surface Ledger`
- `Internal-Only And Bridge Flows`
- `Emitted Artifact Carriers`
- `Unplaced Or Cross-Cutting Workflow Surfaces`
- `What The Current High-Level Picture Misses`
- `Recommended Additions To The Next Map`

Use the bundle's stable output contract for the surface ledger.

## Constraints

- stay high-level
- do not turn this lane into a family zoom
- cite concrete files and lines
- create the output file early and revise in place
- keep reads focused on the governing inputs, `.codex/get-shit-done/workflows/`, and directly needed wrapper-to-workflow references
- if interrupted, leave a partial artifact with an `Incomplete State` note rather than no file at all

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
