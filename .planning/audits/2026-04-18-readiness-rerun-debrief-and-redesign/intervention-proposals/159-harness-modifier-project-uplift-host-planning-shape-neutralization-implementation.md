Date: 2026-04-22
Status: landed

# Harness Modifier Project Uplift Host-Planning-Shape Neutralization Implementation

## Role

- [d:r:i] This slice lands the third bounded neutralization tranche cleared by `158` plus extraction lane `09`.
- [d:r:i] Its job is to externalize the remaining host-planning-shape surface still embedded inside `project_uplift.py` without widening into relocation, install-contract pointer work, or adjacent helper movement.

## What Landed

### Typed State-Section Carrier

- [d:r:i] The top-level `Project Uplift` state-slot shape now lives under:
  - [../../../../harness_modifier/uplift/state_section.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/state_section.json)
  - [../../../../harness_modifier/uplift/state_section.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/state_section.py)
- [d:r:i] That carrier now owns:
  - `.planning/STATE.md` path anchor
  - ordered selector vocabulary
  - label schema
  - sibling-marker insertion points

### Typed Phase-Layout Carrier

- [d:r:i] The phase-discovery grammar now lives under:
  - [../../../../harness_modifier/uplift/phase_layout.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/phase_layout.json)
  - [../../../../harness_modifier/uplift/phase_layout.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/phase_layout.py)
- [d:r:i] That carrier now owns:
  - `.planning/phases` root anchor
  - document-glob map for `context`, `plan`, and `summary`
  - phase-name delimiter
  - numeric phase-segment delimiter

### Narrow State Writer

- [d:r:i] The `STATE.md` renderer/updater now lives under:
  - [../../../../harness_modifier/uplift/state_writer.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/state_writer.py)
- [d:r:i] The module now keeps the split lane `09` asked for:
  - distinct render entry
  - distinct update entry
  - helper-side selector dispatch in code rather than data tuples
  - shared heading ownership still routed through [../../../../harness_modifier/uplift/output_policy.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/output_policy.json)

### Helper Rewire

- [d:r:i] [../../../../tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py) no longer keeps:
  - `STATE.md` path anchor
  - insertion-marker names
  - state-slot label order
  - phase-root path anchor
  - phase document globs
  - phase-prefix grammar
  as helper-local literals.
- [d:r:i] The helper now:
  - builds typed state-section values
  - delegates `Project Uplift` slot rendering/update to `state_writer.py`
  - reads plan/summary/context discovery through the phase-layout carrier

### Focused Parity Frontier

- [d:r:i] [../../../../tooling/codex/tests/test_project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_project_uplift.py) now holds the sharpened boundary directly:
  - phase-layout carrier shape
  - state-section carrier shape
  - insert-before-sibling behavior
  - replace-in-place behavior
  - trailing-append behavior
  - phase count parity
  - latest-context sort parity across decimal phase prefixes

## What Stays Later

- [d:r:i] No `project_uplift.py` relocation yet.
- [d:r:i] No `seed_migration_inventory.py` relocation yet.
- [d:r:i] No `harness_canary.py` follow-through inside this tranche.
- [d:r:i] No install-contract pointer neutralization for `OVERLAY_MANIFEST_REL_PATH` yet.
- [d:r:i] No second overlay filesystem tranche.
- [d:r:i] No overwrite-family source split.
- [d:r:i] No standalone repo or npm/`npx` distribution move.

## Verification

- [e:r:i] `python3 -m py_compile tooling/codex/project_uplift.py harness_modifier/uplift/state_section.py harness_modifier/uplift/phase_layout.py harness_modifier/uplift/state_writer.py`
- [e:r:i] `python3 -m unittest tooling.codex.tests.test_project_uplift`

## Exact Next Move

- [d:r:i] Reopen the payload-home judgment on top of all three landed neutralization tranches instead of widening directly into relocation, install-contract pointer work, or another adjacent extraction family.
