Date: 2026-04-21
Status: landed spec lifecycle change-triggered refresh

# SPEC Lifecycle Carry Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `23`.
- [g:r:i] The trigger here is an upstream lifecycle contract move: the spec producer pair and the first downstream discuss consumer now move together instead of leaving the spec boundary narrower than the later lifecycle chain.

## Trigger

- [e:c+i] The spec lifecycle family now carries a bounded landed slice through [63-spec-lifecycle-carry-first-slice-proposal.md](../intervention-proposals/63-spec-lifecycle-carry-first-slice-proposal.md) and [64-spec-lifecycle-carry-first-slice-implementation.md](../intervention-proposals/64-spec-lifecycle-carry-first-slice-implementation.md).
- [e:r:i] That slice changed the propagation field in four concrete ways:
  - the overlay frontier now owns `get-shit-done/workflows/spec-phase.md` and `get-shit-done/templates/spec.md` as explicit lifecycle carriers instead of upstream-only background
  - the spec template now keeps bounded `Future-Aware Notes` explicit when long-arc doctrine materially constrains the phase
  - `spec-phase.md` now reads `.planning/LONG-ARC.md` and writes those notes as part of the upstream spec contract
  - `discuss-phase.md` now reads `SPEC.md`, adds it to canonical refs, and seeds `future_awareness` from `Future-Aware Notes` when present

## Refresh Result

- [d:r:i] The typed `v2` semantic layer now keeps the spec producer pair explicit alongside the discuss consumer instead of letting `SPEC` remain a prose-only claim about discuss behavior.
- [d:r:i] The declared-contract layer now names the spec future-carry contract explicitly rather than leaving it ambient across one workflow claim and one template omission.
- [d:r:i] The evidence layer now records the landed `64` implementation note and focused spec/discuss contract test as the current anchors for this slice.
- [d:r:i] The coverage layer now records an eighth real non-uplift `change_triggered_slice_refresh`, so typed `v2` continues to prove itself against live upstream-to-downstream contract movement instead of staying centered on later lifecycle bridges only.

## Current Consequence

- [d:r:i] The typed `v2` registry now keeps the spec producer boundary visible alongside verifier, transition, milestone-boundary, and first-read consumer movement rather than leaving upstream spec carry ambient behind one template file and one unfulfilled workflow claim.
- [d:r:i] Later refreshes should keep following actual contract movement into seed consumers and broader read-order / relevance-control surfaces rather than reopening the whole lifecycle field in one jump.
