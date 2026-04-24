Date: 2026-04-22
Status: landed

# Harness Modifier Project Uplift Host-Doctrine Catalog Neutralization Implementation

## Role

- [d:r:i] This slice lands the second bounded neutralization tranche cleared by `156` plus extraction lane `07`.
- [d:r:i] Its job is to externalize the remaining host-doctrine carrier catalog and host-facing uplift vocabulary that were still embedded inside `project_uplift.py`, while keeping relocation and planning-writer neutralization explicitly later.

## What Landed

### Typed Host-Doctrine Catalog

- [d:r:i] The file and marker carrier payload now lives under:
  - [../../../../harness_modifier/uplift/carrier_catalog.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/carrier_catalog.json)
  - [../../../../harness_modifier/uplift/carrier_catalog.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/carrier_catalog.py)
- [d:r:i] The catalog now carries:
  - stable file-carrier rows
  - marker-carrier rows
  - the runtime-agent registry shape as a named sibling object
  - explicit ordering rule `stable_by_key_within_section`

### Typed Host-Facing Vocabulary

- [d:r:i] The rerun-boundary phrases, skill-command tokens, and operator-facing uplift recommendation sentences now live under:
  - [../../../../harness_modifier/uplift/vocabulary.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/vocabulary.json)
  - [../../../../harness_modifier/uplift/vocabulary.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/vocabulary.py)
- [d:r:i] The carrier now owns:
  - rerun-boundary phrase patterns
  - uplift detect/write command strings
  - seed-migration inspect/write command strings
  - phase-boundary note sentences
  - report/state/progress recommendation sentences

### Helper Rewire

- [d:r:i] [../../../../tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py) now reads the catalog and vocabulary carriers instead of re-declaring those surfaces as helper-local constants.
- [d:r:i] The helper now keeps helper-local only what lane `07` said should remain local:
  - classification logic
  - fingerprinting logic
  - drift-reason composition
  - report/manifest rendering structure
  - progress-note label fields
  - planning-writer and phase-scanner reach
  - `OVERLAY_MANIFEST_REL_PATH`

### Focused Test Frontier

- [d:r:i] [../../../../tooling/codex/tests/test_project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_project_uplift.py) now proves the sharpened frontier directly:
  - carrier loader shape
  - canonical section ordering
  - absent-additive stability across no-op catalog reordering
  - doctrine-reference hash stability across no-op catalog reordering
  - carrier fingerprint stability across no-op catalog reordering
  - recommendation and drift-reason equivalence across no-op catalog reordering

## What Stays Later

- [d:r:i] No `project_uplift.py` relocation yet.
- [d:r:i] No `seed_migration_inventory.py` relocation yet.
- [d:r:i] No `.planning/STATE.md` writer or `.planning/phases/` scanner neutralization yet.
- [d:r:i] No install-contract pointer neutralization for `OVERLAY_MANIFEST_REL_PATH` yet.
- [d:r:i] No second overlay filesystem tranche.
- [d:r:i] No overwrite-family source split.
- [d:r:i] No standalone repo or npm/`npx` distribution move.

## Verification

- [e:r:i] `python3 -m py_compile tooling/codex/project_uplift.py harness_modifier/uplift/carrier_catalog.py harness_modifier/uplift/vocabulary.py`
- [e:r:i] `python3 -m unittest tooling.codex.tests.test_project_uplift`

## Exact Next Move

- [d:r:i] Reopen the post-neutralization payload-home judgment on top of this cleaner second neutralization tranche rather than widening into another adjacent extraction family.
