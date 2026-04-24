Date: 2026-04-21
Status: active layered registry policy

# Propagation Registry Generation And Seeding Policy

## Purpose

- [g:r:i] The propagation registry should not be treated as a purely automatic dependency extractor.
- [g:r:i] It should also not remain a single blended surface once the family already carries maintained roster docs, declared contracts, generated evidence, and a richer semantic map.
- [g:r:i] The intended shape is now a layered hybrid:
  - maintained rosters disclose what surfaces exist
  - declared contracts disclose typed local intent
  - generated evidence discloses observed or validated state
  - AI authors the semantic map and the coverage/disposition layer
  - later reread and inheritance still decide what the registry means

## Layer Stack

### L0 Inventory Roster

- [d:r:i] `L0` answers `what maintained surfaces exist under a declared roster frontier?`
- [e:c+i] The upstream shipped-surface roster begins at [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:1).
- [d:r:i] Repo-local maintained docs extend that frontier where upstream inventory cannot see local carriers:
  - [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:53)
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:49)
  - [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:137)
  - workspace governance docs such as [CURRENT-STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/CURRENT-STATE.md:27)
- [d:r:i] `L0` is roster truth, not propagation meaning.

### L1 Declared Contracts

- [d:r:i] `L1` answers `what authored local contract or ownership declaration already exists?`
- [e:c+i] The clearest current prototype is [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json:1) plus [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/portable_gsd_contract.py:1).
- [d:r:i] `L1` should carry declared ownership, add/overwrite typing, and other authored local contracts where they really exist.
- [d:r:i] `L1` should not smuggle in runtime observations or semantic edges.

### L2 AI-Authored Semantic Map

- [d:r:i] `L2` answers `how do these surfaces belong together as propagation families, carriers, and edges?`
- [d:r:i] Family boundaries, row splits, cross-family edges, propagation obligations, direct-consumer versus mirror judgments, and held/open relations remain AI-authored.
- [d:r:i] The current semantic basis remains the prose family in `08-13` plus the lane-03 inheritance note.

### L3 Generated Evidence

- [d:r:i] `L3` answers `what has been observed, validated, sampled, or recorded under the current basis commit?`
- [d:r:i] `L3` is now split into narrower evidence lanes:
  - contract-validation evidence
  - materialization evidence
  - observed runtime evidence
  - producer-scoped report evidence
  - capture / orchestration evidence
  - coherence evidence
- [e:c+i] Current examples include:
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:1)
  - runtime-visibility outputs from [runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/runtime_visibility.py:1)
  - overlay validation/materialization outputs from [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/portable_gsd_contract.py:1)
  - coherence outputs from `manifest_install_coherence.py`
  - launch captures from `capture_launch_truth.py`
- [d:r:i] `L3` points at bounded proofs or observations. It does not own family/edge semantics.

### L4 Operator Control And Inheritance

- [d:r:i] `L4` answers `how should this registry be refreshed, read, inherited, or explicitly refused?`
- [d:r:i] `L4` carries:
  - coverage dispositions
  - refresh kinds
  - refusal surfaces
  - held/open relations
  - inheritance/disposition notes
- [d:r:i] This is where the registry stops being one static JSON and becomes a governed family.

## Seeding Order

- [d:r:i] Future refreshes should seed from `L0` first, join `L1` and `L3`, then write `L2` and `L4`.

### 1. Maintained Inventory Frontier

- [e:c+i] Upstream `docs/INVENTORY.md` declares itself the authoritative roster of shipped surfaces and says new surfaces should land there first, then propagate to broader docs. Source: [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:1).
- [d:r:i] For shipped upstream surfaces, this is now more than a discovery hint. It is a roster frontier that later coverage dispositions should answer back to.

### 2. Local Maintained Roster Surfaces

- [d:r:i] Repo-local maintained docs should seed local-only carriers that upstream inventory cannot see.
- [d:r:i] The current first-slice roster sources are:
  - [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:53) for helper cohort surfaces
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:49) and [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:137) for doctrine-carrying surfaces
  - workspace governance docs for audit-lane and workspace-control carriers

### 3. Declared Contracts

- [d:r:i] Authored contracts should then join the roster frontier where they exist.
- [d:r:i] The current typed contract frontier is still narrow: overlay ownership/materialization is the main declared-contract family.

### 4. Observed And Validated Evidence

- [d:r:i] Observed and validated carriers should then be indexed against the roster and contract surfaces rather than blended into one generic evidence bucket.
- [d:r:i] This means `UPLIFT-MANIFEST.json` is treated as a producer-scoped report with observed inputs, not as a neutral catch-all runtime truth surface.

### 5. Prose Semantic Family

- [d:r:i] The prose family in `08-13` plus the lane-03 inheritance note remains the richer interpretive layer that writes `L2` and `L4`.

## Refresh Kinds

- [d:r:i] The family now distinguishes three refresh kinds:
  - `scheduled whole-registry refresh`
  - `change-triggered slice refresh`
  - `lane-scoped refresh`
- [d:r:i] The current `v2` landing is a `lane-scoped refresh`.
- [d:r:i] Later contract-changing slices should prefer `change-triggered slice refresh` rather than waiting for a whole-family rebuild.

## Required Discipline

- [d:r:i] Do not treat current upstream inventory as proof that the semantic map has already answered back to every roster entry.
- [d:r:i] Do not treat generated hashes, validation passes, or coherence outputs as proof that the semantic field is exhaustively mapped.
- [d:r:i] Every refresh still requires:
  - contextual reread
  - explicit inheritance/disposition
  - named held/open relations
  - explicit refusal of claims the current slice is not making

## Refusals

- [d:r:i] The registry family still refuses:
  - whole-harness auto-extraction as semantic truth
  - declared-contract derivation without an authored contract surface
  - semantic overclaim from validation/coherence tooling
  - cross-runtime topology claims beyond the currently held local open family
  - upstream-pristine drift machinery inside this first typed split

## Current Consequence

- [d:r:i] The current `v1` registry remains the predecessor compact slice.
- [d:r:i] The active next surface is now the layered `v2` first refresh recorded in [15-propagation-registry-v2-layered-first-refresh.md](15-propagation-registry-v2-layered-first-refresh.md).
- [d:r:i] That refresh starts from:
  - maintained upstream and local roster frontiers
  - narrow declared contracts
  - bounded observed/validated evidence
  - then the existing propagation prose family and lane-03 inheritance
