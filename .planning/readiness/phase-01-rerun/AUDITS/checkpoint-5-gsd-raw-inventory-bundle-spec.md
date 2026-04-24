# Checkpoint 5 GSD Raw Inventory Bundle Spec

## Purpose

Run the first real iterative high-level GSD mapping pass without freezing a stable ontology too early.

This bundle is not a deep contract zoom and it is not a file-by-file diff. Its job is to broaden the current high-level picture until later ontology synthesis is working from explicit repo evidence rather than from a too-simple seed diagram.

It is explicitly for:

- raw high-level surface inventory
- repo-local runtime reality inventory
- omission and under-consideration detection
- relationship discovery at high level
- intervention-class discovery

It is explicitly not for:

- deep family zooms
- implementation planning
- closure or fix judgment on current readiness findings
- forcing all surfaces into predeclared buckets

## Audit Stance

- terrain-mapping
- completeness-challenge
- anti-premature-ontology
- anti-silent-omission
- anti-simple-picture bias

Main bias risks to resist:

- treating the two current schema docs as already sufficient
- forcing surfaces into predefined families too early
- flattening `cross-cutting`, `ambiguous`, or `unplaced` into fake certainty
- silently dropping sub-workflows, emitted artifacts, or helper/control surfaces because they are awkward to classify

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
4. [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md)
5. [checkpoint-5-gsd-upstream-baseline-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-baseline-schema.md)
6. [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
7. [checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md)
8. [checkpoint-3-gsd-agent-doctrine-and-role-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md)
9. [checkpoint-3-gsd-runtime-config-overlay-truth.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md)
10. [checkpoint-4-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-converged-synthesis.md)

## Bundle Shape

Run these sublanes first, in parallel:

1. [checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces-spec.md)
2. [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md)
3. [checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces-spec.md)
4. [checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces-spec.md)

Then run:

5. [checkpoint-5-gsd-raw-inventory-a5-synthesis-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a5-synthesis-spec.md)

## Stable Output Contract For A1-A4

Every raw inventory sublane must emit a ledger of surfaces using these fields:

- `surface`
- `path`
- `repo-local role as stated by source`
- `reads/expects`
- `emits/returns`
- `downstream consumers`
- `obvious relations`
- `candidate loose tags`
- `intervention status`
- `classification status`
- `confidence`
- `unresolved classification`

`classification status` must allow:

- `placed provisionally`
- `cross-cutting`
- `ambiguous`
- `unplaced`

Do not replace any of those with a fake stable family just to make the output look neat.

## Bundle Questions

- what major high-level surfaces are still missing from the current map?
- what important relationships are still implicit or absent?
- what emitted artifacts or state carriers are missing from the current picture?
- which surfaces are only weakly placed or not placeable yet?
- what intervention classes are present in the repo but underrepresented in the current map?
- what kinds of ontology seem to be emerging from the repo itself?
- what evidence says the current picture is still too simple?

This bundle does **not** by itself settle clean upstream truth. That reconciliation happens later in:

- [checkpoint-5-gsd-hybrid-reconciliation-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-bundle-spec.md)

## Output

This bundle should produce:

- [checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md)
- [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md)
- [checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md)
- [checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md)
- [checkpoint-5-gsd-raw-inventory-a5-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a5-synthesis.md)

## Decision Discipline

- do not treat the current local and upstream schema docs as already-complete truth
- do not treat old Checkpoint 3 or 4 mappings as sovereign ontology
- do not optimize for the smallest inventory that feels plausible
- preserve `cross-cutting`, `ambiguous`, and `unplaced` surfaces explicitly
- if a surface participates in several high-level families, show that rather than forcing exclusivity
- if a surface has no good placement yet, preserve that rather than smoothing it away

## Durability And Read-Set Discipline

- after reading the governing inputs and lane spec, create the output artifact immediately with the required section headings, then revise in place
- prefer `rg`, targeted `nl -ba`, and narrow `sed` windows over broad full-file rereads
- stay within the named governing inputs and primary surfaces unless a concrete classification need forces widening
- if widening is necessary, record the reason in `Path Of Inquiry` rather than letting it happen silently
- if the lane is interrupted or cannot finish, leave a partial artifact on disk with an explicit `Incomplete State` note rather than failing without an output file

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
