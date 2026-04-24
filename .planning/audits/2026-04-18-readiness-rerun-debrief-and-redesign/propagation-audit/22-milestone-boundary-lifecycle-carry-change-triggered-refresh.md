Date: 2026-04-21
Status: landed milestone-boundary change-triggered refresh

# Milestone Boundary Lifecycle Carry Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `21`.
- [g:r:i] The trigger here is a lifecycle-carry contract move across milestone-open and milestone-close workflow surfaces, not another uplift-only or install-only movement.

## Trigger

- [e:c+i] The milestone-boundary lifecycle family now carries a bounded landed slice through [59-milestone-boundary-lifecycle-carry-first-slice-proposal.md](../intervention-proposals/59-milestone-boundary-lifecycle-carry-first-slice-proposal.md) and [60-milestone-boundary-lifecycle-carry-first-slice-implementation.md](../intervention-proposals/60-milestone-boundary-lifecycle-carry-first-slice-implementation.md).
- [e:r:i] That slice changed the propagation field in four concrete ways:
  - the overlay frontier now owns `new-milestone.md` as an explicit milestone-opening carry surface rather than ambient live drift
  - the overlay frontier now owns `complete-milestone.md` as an explicit milestone-close carry surface rather than ambient live drift
  - the milestone-opening workflow now rereads `.planning/LONG-ARC.md` and `Future Carry Forward` before requirements shaping and roadmapping
  - the milestone-close workflow now rereads `.planning/LONG-ARC.md` and `Future Carry Forward` before archival/project-evolution cleanup

## Refresh Result

- [d:r:i] The typed `v2` semantic layer now names the milestone-boundary carriers and edges explicitly instead of leaving milestone-open and milestone-close carry compressed under the broader lifecycle family label.
- [d:r:i] The declared-contract layer now names the milestone-boundary future-carry contract rather than leaving it ambient in two widened workflow files.
- [d:r:i] The evidence layer now records the landed `60` implementation note as the current anchor for this slice.
- [d:r:i] The coverage layer now records a sixth real non-uplift `change_triggered_slice_refresh`, so typed `v2` has now survived uplift-anchor, consumer-chain, threshold-helper, verifier-lifecycle, setup/materialization, transition-lifecycle, and milestone-boundary movement rather than only abstract redesign.

## Current Consequence

- [d:r:i] The typed `v2` registry now keeps milestone-open and milestone-close carry movement visible alongside the verifier and transition bridges rather than treating later lifecycle carry as one undifferentiated block.
- [d:r:i] The propagation family now has a clearer multi-boundary lifecycle example for later refreshes to inherit from.
- [d:r:i] Later refreshes should keep following actual contract movement into `SPEC`, `STATE/progress` consumer readout, and seed-consumer carry rather than reopening the whole lifecycle field in one jump.
