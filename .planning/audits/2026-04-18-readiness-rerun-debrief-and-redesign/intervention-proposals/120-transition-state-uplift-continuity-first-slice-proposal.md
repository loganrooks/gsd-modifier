Date: 2026-04-22
Status: active bounded proposal

# Transition-State Uplift Continuity First Slice Proposal

## Purpose

- [g:r:i] Open the first ≤2-carrier implementation proposal cleared by the classification return in `119`.
- [g:r:i] Keep the slice inside:
  - `transition.md`
  - `templates/state.md`
- [g:r:i] The target is not to widen compatibility claims.
- [g:r:i] The target is to keep the compact uplift/compatibility digest from disappearing or becoming ambient when state continuity is regenerated at phase boundaries.

## Why This Slice Opens First

- [e:c+i] `119` ranks the first candidate pair as:
  - `transition.md`
  - `templates/state.md`
  Source:
  - [119-uplift-consumer-chain-asymmetry-classification-return.md](119-uplift-consumer-chain-asymmetry-classification-return.md)
- [e:c+i] The live project state already carries a compact `Project Uplift` digest:
  - last uplift class
  - compatibility posture
  - observed runtime basis
  - held runtime annotation
  - current recommendation
  Source:
  - [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- [e:c+i] The state template still does not own that continuity shape, while `transition.md` already owns compact phase-close carry through `Future Carry Forward`. Sources:
  - [tooling/portable-gsd/overlay/get-shit-done/templates/state.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/state.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md)

## Proposed Slice

- [d:r:i] Add a compact top-level `## Project Uplift` continuity block to the state template so later state regeneration does not rely on one-off local memory.
- [d:r:i] Keep that block adjacent to `Accumulated Context`, not nested inside it.
- [d:r:i] Treat ownership explicitly:
  - the template declares the section as a placeholder
  - the helper fills it in place during `--write`
- [d:r:i] Teach `transition.md` to handle the compact uplift block through one bounded continuity step, not as an ambient side effect and not by folding it into `load_future_preservation_carry` or `review_accumulated_context`.
- [d:r:i] Split the continuity step into two explicit paths:
  - preserve path:
    - when observed runtime basis and held runtime annotation still match the block, keep the block in place
  - refresh path:
    - when runtime movement is detected inside the phase, rerun `$gsd-uplift-project --write` before transition closes so the block reflects current values
- [d:r:i] Keep the slice read-only in character:
  - no new write-recommending compatibility dispatcher
  - no matrix or version-window claim
  - no route translation
  - no structural promotion of scalar summary fields into a broader compatibility table
- [d:r:i] Keep the `gsd-tools.cjs phase complete` interaction explicit:
  - its basic state edits must preserve the `Project Uplift` section across transition

## What The Slice Should Carry

- [d:r:i] `compatibility_posture: observed_basis_only` remains the top-level discipline.
- [d:r:i] The compact state continuity block should stay summary-shaped, mirroring the current operator-facing uplift digest rather than turning `STATE.md` into a second manifest.
- [d:r:i] The block should preserve the existing distinction between:
  - observed runtime basis
  - held runtime annotation
  - current recommendation
- [d:r:i] The template placeholder should pin the minimum scalar field set:
  - last uplift class
  - compatibility posture
  - observed runtime basis
  - held runtime annotation
  - current recommendation
- [d:r:i] The block should remain small enough to sit beside `Future Carry Forward` rather than competing with it.
- [d:r:i] `beside` means an adjacent top-level section, not a nested sub-block under `Accumulated Context`.
- [d:r:i] The scalar-summary versus structural-manifest split must remain durable through this consumer surface:
  - `STATE.md` carries the compact scalar digest
  - `UPLIFT-MANIFEST.json` remains the typed structural carrier

## What This Slice Does Not Authorize

- [d:r:i] No widening of `compatibility_drift_reasons`.
- [d:r:i] No structural-row promotion inside `STATE.md`.
- [d:r:i] No standalone compatibility carrier.
- [d:r:i] No `.claude` translation or parity claim.
- [d:r:i] No third-runtime annotation surfacing through the state-continuity block.
- [d:r:i] No widening of the state block into a shared-reference surface for milestone-boundary carriers.
- [d:r:i] No extraction or npm/`npx` implementation work.

## Verification Gates

- [d:r:i] `STATE.md` continuity should no longer depend on ambient local uplift memory.
- [d:r:i] The template and transition workflow should preserve the compact uplift digest without duplicating `UPLIFT-MANIFEST.json`.
- [d:r:i] The slice must keep summary shape distinct from structural manifest shape.
- [d:r:i] The slice must preserve `compatibility_posture: observed_basis_only`.
- [d:r:i] The slice must keep family-6 and later extraction pressure outside the implementation boundary.
- [d:r:i] The slice must keep the transition/state test frontier bounded to this pair of carriers rather than widening across the whole consumer field.
- [d:r:i] The slice must extend the compatibility-family consumer-chain refresh on top of `43`, not backfill that movement into lifecycle-carry `21`.

## Current Consequence

- [d:r:i] The cross-runtime family now has its first concrete ≤2-carrier implementation proposal candidate.
- [d:r:i] After the lane-12 reread and local inheritance, the next move is no longer another proposal loop.
- [d:r:i] The next move is the bounded implementation slice itself on:
  - `transition.md`
  - `templates/state.md`
