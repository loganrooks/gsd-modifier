# Checkpoint 5 GSD Emergent Ontology Spec

## Purpose

Derive candidate top-level ontologies from the repo evidence now on disk instead of imposing one in advance.

This stage should explain which groupings actually emerge, where they overlap, and which surfaces still resist clean placement.

## Preconditions

Do not run this until these exist:

- [checkpoint-5-gsd-raw-inventory-a5-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a5-synthesis.md)
- [checkpoint-5-gsd-relationship-extraction.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-relationship-extraction.md)
- [checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis.md)

## Inputs

1. [checkpoint-5-gsd-high-level-mapping-program-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-high-level-mapping-program-spec.md)
2. [checkpoint-5-gsd-raw-inventory-a5-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a5-synthesis.md)
3. [checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis.md)
4. [checkpoint-5-gsd-relationship-extraction.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-relationship-extraction.md)
5. the current seed schemata for contrast only

## Questions

- what candidate ontologies are actually supported by the evidence?
- what surfaces are best treated as stable high-level families?
- what surfaces remain cross-cutting between families?
- what surfaces are weakly placed or unplaced even after relation extraction?
- what high-level layer ontology is emerging across local runtime, upstream baseline, upstream trajectory, overlay, and readiness-only surfaces?
- where do multiple plausible ontologies compete?
- what working ontology is strong enough to drive the first real high-level map without pretending to finality?

## Output

Write:

- [checkpoint-5-gsd-emergent-ontology.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-emergent-ontology.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Candidate Ontologies`
- `Evidence For Each Ontology`
- `Cross-Cutting Surfaces`
- `Unplaced Or Weakly Placed Surfaces`
- `Ontology Tensions`
- `Recommended Working Ontology For Map V1`

## Constraints

- do not force exclusivity where multi-membership is more truthful
- do not erase unplaced surfaces for neatness
- distinguish a recommended working ontology from a final ontology
- cite the raw-inventory and relationship artifacts directly

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
