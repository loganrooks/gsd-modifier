# Checkpoint 5 GSD Raw Inventory A3: Agent, Reference, Template, And Helper Surfaces

## Purpose

Inventory the contract-carrying and helper/control surfaces that support the repo-local GSD runtime but are often collapsed out of high-level diagrams.

This lane exists to stop the high-level picture from becoming wrapper/workflow-only.

## Audit Stance

- terrain-mapping
- contract-carrier exposure
- anti-wrapper/workflow-only bias

Biases to resist:

- treating helper CLI/runtime-control surfaces as mere implementation noise
- treating references/templates as passive docs instead of contract carriers
- flattening agents, references, templates, and helpers into one undifferentiated support bucket

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md)
4. [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md)
5. [checkpoint-5-gsd-upstream-baseline-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-baseline-schema.md)
6. [checkpoint-3-gsd-agent-doctrine-and-role-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md)
7. [checkpoint-3-gsd-runtime-config-overlay-truth.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md)

## Primary Surfaces

Inspect at minimum:

- `.codex/agents/`
- `.codex/get-shit-done/references/`
- `.codex/get-shit-done/templates/`
- `.codex/get-shit-done/bin/`
- `.codex/get-shit-done/bin/lib/`
- discovery/materialization helper docs if needed for helper classification

## Questions

- which surfaces act as formal role contracts, handoff contracts, templates, shared doctrine, or helper/control logic?
- which of these are load-bearing at high level?
- which helper surfaces are currently underrepresented because they look “implementation-level”?
- which contract-carrying surfaces emit or shape downstream artifacts?
- which surfaces remain cross-cutting or weakly placed?
- what does the current high-level map still miss in this layer?

## Output

Write:

- [checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Agent Surface Ledger`
- `Reference And Template Surface Ledger`
- `Helper And Runtime-Control Surface Ledger`
- `Cross-Cutting Contract Carriers`
- `What The Current High-Level Picture Misses`
- `Recommended Additions To The Next Map`

Use the bundle's stable output contract for the ledgers.

## Constraints

- keep the distinction between agents, references/templates, and helper/control surfaces visible
- stay high-level
- cite concrete files and lines
- create the output file early and revise in place
- keep reads focused on the governing inputs and the named agent/reference/template/helper directories
- if interrupted, leave a partial artifact with an `Incomplete State` note rather than no file at all

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
