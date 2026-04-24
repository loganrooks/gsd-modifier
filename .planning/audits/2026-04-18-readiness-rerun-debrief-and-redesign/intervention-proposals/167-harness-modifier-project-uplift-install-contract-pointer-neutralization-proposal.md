Date: 2026-04-23
Status: proposed

# Harness Modifier Project Uplift Install-Contract Pointer Neutralization Proposal

## Role

- [d:r:i] This proposal is the next bounded extraction-family object after the completed lane-`10` closeout of `160`.
- [d:r:i] Its job is to neutralize the remaining install-contract pointer coupling around the overlay-manifest path without widening into relocation, artifact-home movement, or broader packaging appetite.

## Why This Proposal Is Active Now

- [d:r:i] Lane `10` narrowed the remaining coupling in `project_uplift.py` to two materially different residue classes:
  - install-contract pointer coupling
  - held-later artifact-home coupling
- [d:r:i] The install-contract pointer is the sharper adjacent slice because it is a bounded path-owned contract seam rather than an artifact-placement question.
- [d:r:i] Carrying the install-target literal into any later payload-home move would preserve the wrong ownership shape one layer farther out.

## Primary Sites

- [d:r:i] `tooling/codex/project_uplift.py`
  - `OVERLAY_MANIFEST_REL_PATH`
  - `overlay_manifest_rel_path()`
  - `load_overlay_manifest(repo_root)`
- [d:r:i] `harness_modifier/contract/portable_gsd_contract.py`
  - any matching overlay-manifest path anchors or sibling install-contract consumers that still re-declare the same path

## Proposed Neutralization Shape

- [d:r:i] Move the install-contract pointer into one typed contract carrier under `harness_modifier/contract/`.
- [d:r:i] Give that carrier one narrow loader module rather than letting helper code remember the overlay-manifest path directly.
- [d:r:i] Rewire `project_uplift.py` to read the typed value at analysis entry and return that value through `overlay_manifest_rel_path()` rather than through a helper-local constant.
- [d:r:i] Keep single-owner discipline explicit:
  - if a current contract surface already deserves to own the overlay-manifest path anchor, reference it from the new carrier rather than re-declaring the path in two places.

## Questions This Slice Must Answer

### 1. What Is The Right Carrier Home?

- [d:r:i] Keep the answer bounded to install-contract ownership.
- [d:r:i] Do not widen into standalone repo or package-home questions.

### 2. What Rides With The Overlay-Manifest Pointer?

- [d:r:i] Name any narrow sibling install-target pointers that materially share the same contract class.
- [d:r:i] Do not smuggle artifact-home decisions or runtime-parity redesign into the same carrier.

### 3. What Must Stay Unchanged?

- [d:r:i] `project_uplift.py` classification/rendering behavior
- [d:r:i] `seed_migration_inventory.py` downstream posture
- [d:r:i] `harness_canary.py` downstream posture
- [d:r:i] `tooling/codex/UPLIFT-HELD-LATER.md` location
- [d:r:i] all relocation appetite for `project_uplift.py`

## Required Verification Front

- [d:r:i] focused parity coverage proving that:
  - overlay-manifest loading returns the same payload after the carrier read replaces the embedded literal
  - emitted report / manifest / progress-note bytes do not change on representative fixtures
- [d:r:i] install-contract validation and materialization checks must remain clean after the rewire

## Explicitly Out Of Scope

- [d:r:i] held-later artifact-home movement
- [d:r:i] `project_uplift.py` relocation
- [d:r:i] second overlay filesystem tranche
- [d:r:i] overwrite-family source-indirection widening
- [d:r:i] standalone repo boundary
- [d:r:i] npm or `npx` packaging
- [d:r:i] broader `.codex` / `.claude` parity redesign

## Primary Inputs

- [d:r:i] [160-harness-modifier-project-uplift-post-host-planning-shape-payload-home-judgment-proposal.md](160-harness-modifier-project-uplift-post-host-planning-shape-payload-home-judgment-proposal.md)
- [d:r:i] [../extraction-audit/outputs/10-harness-modifier-project-uplift-post-host-planning-shape-payload-home-judgment-reread-opus47-max-r1.md](../extraction-audit/outputs/10-harness-modifier-project-uplift-post-host-planning-shape-payload-home-judgment-reread-opus47-max-r1.md)
- [d:r:i] [../extraction-audit/dispositions/10-harness-modifier-project-uplift-post-host-planning-shape-payload-home-judgment-reread-inheritance.md](../extraction-audit/dispositions/10-harness-modifier-project-uplift-post-host-planning-shape-payload-home-judgment-reread-inheritance.md)
- [d:r:i] [../../../../harness_modifier/overlay/helpers/AUTHORITY-MAP.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/helpers/AUTHORITY-MAP.md)

## Exact Next Move

1. [d:r:i] Cut one narrow install-contract carrier plus loader proposal shape and audit it on a bounded reread basis before implementation.
2. [d:r:i] Keep the held-later artifact-home question explicit through `168`, not inside this slice.
3. [d:r:i] Land the install-contract pointer neutralization with focused parity tests, install/materialization verification, and propagation/governance carry.
