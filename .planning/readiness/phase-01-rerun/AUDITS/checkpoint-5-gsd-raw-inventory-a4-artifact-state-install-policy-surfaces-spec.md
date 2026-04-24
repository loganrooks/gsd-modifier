# Checkpoint 5 GSD Raw Inventory A4: Artifact, State, Install, And Policy Surfaces

## Purpose

Inventory the artifact/state carriers, install/materialization layers, and policy/readiness surfaces that shape the repo-local GSD system at high level.

This lane exists to stop the topology from reducing the system to executable flows while leaving artifact/state and policy layers vague.

## Audit Stance

- terrain-mapping
- layer-seam exposure
- anti-runtime-only bias

Biases to resist:

- treating `.planning` outputs as generic byproducts rather than topology
- treating install/materialization as a footnote
- treating repo policy and readiness-package control surfaces as either runtime canon or irrelevant

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
4. [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md)
5. [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md)
6. [checkpoint-5-gsd-upstream-baseline-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-baseline-schema.md)
7. [checkpoint-3-gsd-runtime-config-overlay-truth.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md)

## Primary Surfaces

Inspect at minimum:

- `.planning/config.json`
- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/STATE.md`
- active phase-artifact naming and emitted artifact carriers
- `scripts/setup-portable-gsd.sh`
- `tooling/portable-gsd/overlay/`
- `.codex/config.toml`
- `.codex/gsd-file-manifest.json`
- readiness-package control surfaces under `.planning/readiness/phase-01-rerun/` where needed

## Questions

- what artifact/state carriers are load-bearing at high level?
- what install/materialization layers exist, and how do they relate?
- what policy or readiness control surfaces shape the system without being runtime canon?
- which surfaces are currently underrepresented in the high-level map?
- which surfaces remain ambiguous or cross-cutting?
- what intervention classes become visible only when these layers are treated explicitly?

## Output

Write:

- [checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Artifact And State Surface Ledger`
- `Install And Materialization Surface Ledger`
- `Policy And Readiness Surface Ledger`
- `Cross-Layer Seams`
- `What The Current High-Level Picture Misses`
- `Recommended Additions To The Next Map`

Use the bundle's stable output contract for the ledgers.

## Constraints

- do not collapse runtime canon, tracked overlay canon, live materialized runtime, and readiness-package control surfaces into one layer
- stay high-level
- cite concrete files and lines
- create the output file early and revise in place
- keep reads focused on the governing inputs and the named artifact/state/install/policy surfaces
- if interrupted, leave a partial artifact with an `Incomplete State` note rather than no file at all

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
