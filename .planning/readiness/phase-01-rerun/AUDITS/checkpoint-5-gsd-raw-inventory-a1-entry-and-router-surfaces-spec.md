# Checkpoint 5 GSD Raw Inventory A1: Entry And Router Surfaces

## Purpose

Inventory the top-level entry, command, wrapper, and routing surfaces that introduce users or orchestrators into repo-local GSD.

This lane exists to answer the user's criticism that the current map still leaves too many skills as vague leftovers.

This is a high-level inventory lane, not a deep zoom.

## Audit Stance

- terrain-mapping
- omission challenge
- anti-leftover-bucket

Biases to resist:

- listing only the most famous workflow wrappers
- flattening routers and meta-entry surfaces into ordinary skills
- treating unplaced skills as irrelevant instead of as a signal that the high-level map is incomplete

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md)
4. [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md)
5. [checkpoint-5-gsd-upstream-baseline-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-baseline-schema.md)

## Primary Surfaces

Inspect at minimum:

- `.codex/skills/`
- repo-local command/help/router surfaces under `.codex/get-shit-done/` that directly route users into workflows
- discovery or inventory surfaces if they affect what counts as visible entry

## Questions

- what are the real entry surfaces into repo-local GSD here?
- which skills are direct workflow wrappers?
- which skills are routers, meta-entrypoints, control surfaces, or management shells?
- which entry surfaces emit or depend on important artifacts or state?
- which entry surfaces are missing from the current map?
- which entry surfaces do not fit any clean current family?

## Output

Write:

- [checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Entry Surface Ledger`
- `Router And Meta-Entry Surfaces`
- `Unplaced Or Weakly Placed Entry Surfaces`
- `What The Current High-Level Picture Misses`
- `Recommended Additions To The Next Map`

Use the bundle's stable output contract for the surface ledger.

## Constraints

- do not perform deep workflow-internal tracing beyond what is needed to classify the entry surface at high level
- do not assume all skills are equivalent wrappers
- cite concrete files and lines
- create the output file early and revise in place
- keep reads focused on the governing inputs, `.codex/skills/`, and directly needed router/help/control surfaces
- if interrupted, leave a partial artifact with an `Incomplete State` note rather than no file at all

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
