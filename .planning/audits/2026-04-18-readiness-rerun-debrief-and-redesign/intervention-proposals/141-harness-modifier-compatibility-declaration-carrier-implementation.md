Date: 2026-04-22
Status: landed

# Harness Modifier Compatibility Declaration Carrier Implementation

## Purpose

- [g:r:i] Land the typed compatibility carrier that can later travel with a standalone harness-modifier project or into other host repos without re-deriving the policy from uplift prose or materialization helper constants.

## Landed Shape

- [d:r:i] The authoritative compatibility carrier now lives at [harness_modifier/compatibility/declaration.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/compatibility/declaration.json:1).
- [d:r:i] The loader for that carrier now lives at [harness_modifier/compatibility/declaration.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/compatibility/declaration.py:1).
- [d:r:i] The declaration now carries:
  - `compatibility_posture`
  - `runtime_basis`
  - `runtime_held_annotations`
  - `overlay_schema_version`
  - `uplift_manifest_schema_version`
  - `upstream_compatibility_window`
  - `parity_scan_baseline`
  - `check_protocol`
  - `held_later`

## Consumer Follow-Through

- [d:r:i] [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:1) now reads the declaration rather than owning the posture/annotation constants itself.
- [d:r:i] The durable uplift outputs now surface the declaration path and declaration-bound compatibility semantics in:
  - [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:1)
  - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:1)
  - [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:1)
- [d:r:i] [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/portable_gsd_contract.py:1) now reads the same declaration for:
  - typed parity baseline rules
  - compatibility declaration echo inside `verify-materialized`
  - overlay-schema alignment to the declaration

## Why This Matters For Later Extraction

- [d:r:i] This is now the first compatibility artifact intended to travel unchanged if the modifier layer moves into its own repo.
- [d:r:i] It sharpens the later install story for other host repos with `.codex`, `.claude`, and `get-shit-done` carriers by separating:
  - what the modifier layer declares
  - what the current host repo happens to observe today

## Explicit Boundary

- [d:r:i] The slice still does not widen into:
  - standalone repo split
  - npm/`npx` packaging
  - `.claude` full-materialization claim
  - a broader support window than `observed_basis_only`

## Verification

- [d:r:i] typed declaration loader compiled and loaded cleanly
- [d:r:i] focused uplift and portable-contract tests passed
- [d:r:i] post-materialization verification now echoes the declaration and still passes on the current repo
- [d:r:i] durable uplift outputs were refreshed after the carrier landed

## Held Later

- [d:r:i] overlay/workflow/skill/template/reference carrier rehome
- [d:r:i] second-host dry run
- [d:r:i] standalone repo boundary design
- [d:r:i] npm/`npx` packaging
