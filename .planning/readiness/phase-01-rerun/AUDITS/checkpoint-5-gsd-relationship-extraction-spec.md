# Checkpoint 5 GSD Relationship Extraction Spec

## Purpose

Extract the major high-level relationships across the raw inventory so the next ontology pass is based on explicit system relations rather than on isolated node lists.

This stage exists after raw inventory and before ontology synthesis.

## Preconditions

Do not run this until these exist:

- [checkpoint-5-gsd-raw-inventory-a5-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a5-synthesis.md)
- [checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis.md)
- [checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md)
- [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md)
- [checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md)
- [checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md)

## Inputs

1. [checkpoint-5-gsd-high-level-mapping-program-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-high-level-mapping-program-spec.md)
2. [checkpoint-5-gsd-raw-inventory-a5-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a5-synthesis.md)
3. [checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis.md)
4. the four raw-inventory ledgers

## Questions

- what are the main invocation relationships?
- what surfaces read, write, emit, consume, route, or summarize other surfaces?
- what high-level contract or handoff relationships exist?
- what install/materialization relationships shape the runtime?
- what relationships differ by layer between local runtime, clean upstream baseline, and later upstream trajectory?
- what policy/readiness relationships shape the system without being runtime canon?
- which surfaces participate in several relation types and therefore should remain cross-cutting?

## Output

Write:

- [checkpoint-5-gsd-relationship-extraction.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-relationship-extraction.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Relation Type Glossary`
- `High-Level Relation Ledger`
- `Cross-Cutting Surfaces`
- `Relationship Clusters`
- `What The Raw Inventory Still Leaves Implicit`
- `Implications For Ontology Synthesis`

## Constraints

- stay high-level
- do not freeze families yet
- preserve many-to-many relationships rather than simplifying them away
- preserve layer-sensitive relationships instead of collapsing them into one undifferentiated graph
- cite concrete files and lines

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
