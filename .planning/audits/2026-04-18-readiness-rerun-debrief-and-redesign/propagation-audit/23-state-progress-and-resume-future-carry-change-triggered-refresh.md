Date: 2026-04-21
Status: landed state/progress/resume change-triggered refresh

# State / Progress / Resume Future-Carry Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `22`.
- [g:r:i] The trigger here is a first-read consumer contract move across the state helper plus the routed `progress` and `resume-project` surfaces, not another uplift-only or boundary-only movement.

## Trigger

- [e:c+i] The first-read consumer family now carries a bounded landed slice through [61-state-progress-and-resume-future-carry-consumer-proposal.md](../intervention-proposals/61-state-progress-and-resume-future-carry-consumer-proposal.md) and [62-state-progress-and-resume-future-carry-consumer-implementation.md](../intervention-proposals/62-state-progress-and-resume-future-carry-consumer-implementation.md).
- [e:r:i] That slice changed the propagation field in four concrete ways:
  - the overlay frontier now owns `get-shit-done/bin/lib/state.cjs` as an explicit helper carrier instead of ambient live drift
  - the helper now keeps decisions, blockers, future-carry buckets, and session continuity explicit for the current template-aligned state shape
  - `progress.md` now surfaces live `Future Carry Forward` carry when present
  - `resume-project.md` now uses the structured state snapshot as a re-entry companion and surfaces `Future Carry Forward` explicitly when present

## Refresh Result

- [d:r:i] The typed `v2` semantic layer now keeps the state helper explicit alongside the two first-read consumer workflows instead of treating consumer-side state carry as one blended workflow-only row.
- [d:r:i] The declared-contract layer now names the first-read consumer future-carry contract explicitly rather than leaving it ambient inside one helper file plus two workflow surfaces.
- [d:r:i] The evidence layer now records the landed `62` implementation note and focused helper test as the current anchors for this slice.
- [d:r:i] The coverage layer now records a seventh real non-uplift `change_triggered_slice_refresh`, so typed `v2` continues to prove itself against live contract movement instead of staying a redesign artifact only.

## Current Consequence

- [d:r:i] The typed `v2` registry now keeps first-read consumer carry visible alongside verifier, transition, and milestone-boundary movement rather than letting the consumer bridge disappear inside local prose edits.
- [d:r:i] Later refreshes should keep following actual contract movement into `SPEC`, seed consumers, and broader read-order / relevance-control surfaces rather than reopening the whole lifecycle field in one jump.
