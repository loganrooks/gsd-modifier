# Checkpoint 5 GSD Raw Inventory A5: Synthesis

## Purpose

Synthesize the raw inventory sublanes into one repo-local high-level gap result that is strong enough to drive the next hybrid reconciliation stage.

This synthesis must not freeze a stable ontology yet. It should summarize what is now mapped locally, what is still missing locally, and what kinds of groupings seem to be emerging from repo-local evidence.

## Why This Lane Exists Now

The user explicitly rejected moving into deep zooms because the high-level picture is still too simple.

That means the immediate need is not a family-level contract dive. It is a synthesis of what the current seed maps still miss at high level, so the next map revision can be broader and more honest.

## Preconditions

Do not run this synthesis until all of the following exist:

- [checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md)
- [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md)
- [checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md)
- [checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md)

## Inputs

1. [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md)
2. [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md)
3. [checkpoint-5-gsd-upstream-baseline-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-baseline-schema.md)
4. [checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md)
5. [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md)
6. [checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md)
7. [checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md)

## Questions

- what major high-level surfaces are now clearly represented?
- what major high-level surfaces are still missing from the picture?
- what important relationships are still absent or weakly represented?
- what emitted artifacts or state carriers still need explicit placement?
- what intervention classes are still under-mapped?
- what surfaces are best treated as `cross-cutting`, `ambiguous`, or `unplaced` for now?
- what kinds of ontology seem to be emerging from repo evidence, without freezing them yet?
- what does the next hybrid reconciliation stage have to test before a high-level map can sound like system truth?

## Output

Write:

- [checkpoint-5-gsd-raw-inventory-a5-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a5-synthesis.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `What Is Now Clearly In The High-Level Picture`
- `What Is Still Missing`
- `Missing Relationships`
- `Missing Emitted Artifacts And State Carriers`
- `Under-Mapped Intervention Classes`
- `Cross-Cutting, Ambiguous, And Unplaced Surfaces`
- `Emerging Ontology Signals`
- `Local-Only Limits`
- `What Hybrid Reconciliation Must Test`

## Decision Discipline

- do not force a stable ontology
- do not collapse missing coverage into generic “future work”
- do not quietly discard awkward surfaces
- preserve uncertainty where evidence is still weak
- do not imply that repo-local inventory alone has settled clean upstream truth
- cite the sublane outputs when making synthesis claims

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
