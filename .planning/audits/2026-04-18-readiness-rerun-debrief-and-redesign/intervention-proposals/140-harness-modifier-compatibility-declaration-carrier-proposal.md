Date: 2026-04-22
Status: accepted bounded proposal

# Harness Modifier Compatibility Declaration Carrier Proposal

## Purpose

- [g:r:i] Land `step 2` from the staged extraction sequence without widening into repo split, package distribution, or a broad support-window claim.
- [g:r:i] The move is to give the later standalone harness-modifier project one typed compatibility artifact that can travel unchanged into other host repos.

## Proposed Move

- [d:r:i] Create one authoritative typed compatibility declaration under `harness_modifier/compatibility/`.
- [d:r:i] Move the current compatibility posture, held-runtime annotation semantics, parity baseline, and compatibility-window posture out of buried helper constants and into that declaration.
- [d:r:i] Wire the current host-boundary consumers to read it:
  - `tooling/codex/project_uplift.py`
  - `harness_modifier/contract/portable_gsd_contract.py`

## Carrier Shape

- [d:r:i] `harness_modifier/compatibility/declaration.json`
  - `compatibility_posture`
  - `runtime_basis`
  - `runtime_held_annotations`
  - `overlay_schema_version`
  - `uplift_manifest_schema_version`
  - `upstream_compatibility_window`
  - `parity_scan_baseline`
  - `check_protocol`
  - `held_later`
- [d:r:i] `harness_modifier/compatibility/declaration.py`
  - bounded loader for the typed declaration

## Why This Slice Travels

- [d:r:i] This is the first extraction artifact whose semantics are not only about this host repo's current file layout.
- [d:r:i] A later standalone modifier project or installer can carry this declaration into another repo with `.codex`, `.claude`, and `get-shit-done` directories without re-deriving the policy from prose.
- [d:r:i] The slice also sharpens the current bundled state by separating:
  - portable compatibility semantics
  - host-project observation of current runtime values

## Boundaries

- [d:r:i] Keep the compatibility posture `observed_basis_only`.
- [d:r:i] Keep `.claude` as a held annotation, not a widened parity claim.
- [d:r:i] Do not claim a support window broader than the observed-basis posture.
- [d:r:i] Do not widen into a separate repo or npm/`npx` package in this slice.

## Propagation Obligations

- [d:r:i] `tooling/codex/project_uplift.py` compatibility block and durable outputs
- [d:r:i] `harness_modifier/contract/portable_gsd_contract.py verify-materialized`
- [d:r:i] focused tests for both consumers
- [d:r:i] extraction-family governance surfaces
- [d:r:i] propagation-family typed registry/evidence surfaces

## Verification And Review Gates

- [d:r:i] typed declaration loads cleanly
- [d:r:i] uplift tests and contract tests pass
- [d:r:i] installer/materialization verification reads the declaration and still passes on the current repo
- [d:r:i] propagation/governance surfaces are refreshed in the same slice

## Held Later

- [d:r:i] overlay/workflow/skill/template/reference rehome
- [d:r:i] second-host dry run
- [d:r:i] standalone repo split
- [d:r:i] npm/`npx` packaging
