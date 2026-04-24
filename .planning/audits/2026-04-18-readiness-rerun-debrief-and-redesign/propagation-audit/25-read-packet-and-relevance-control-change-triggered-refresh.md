Date: 2026-04-21
Status: landed read-packet and relevance-control change-triggered refresh

# Read-Packet And Relevance-Control Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `24`.
- [g:r:i] The trigger here is a shared reading-contract move: the repo-local mandatory-read reference now declares layered packet tiers, and the current operator-facing re-entry workflows inherit that contract explicitly instead of leaving entry reading posture ambient.

## Trigger

- [e:c+i] The read-packet family now carries a bounded landed slice through [65-read-packet-and-relevance-control-first-slice-proposal.md](../intervention-proposals/65-read-packet-and-relevance-control-first-slice-proposal.md) and [66-read-packet-and-relevance-control-first-slice-implementation.md](../intervention-proposals/66-read-packet-and-relevance-control-first-slice-implementation.md).
- [e:r:i] That slice changed the propagation field in four concrete ways:
  - the overlay frontier now owns `get-shit-done/references/mandatory-initial-read.md` as an explicit shared contract surface instead of one upstream-only line
  - the shared reference now distinguishes `required_reading`, `supporting_reading`, and `deeper_reading`
  - `progress.md` now keeps structured extracts as the primary route and widens by route rather than by reflex
  - `resume-project.md` and `uplift-project.md` now keep layered re-entry packets explicit instead of flattening broader rereads into startup context

## Refresh Result

- [d:r:i] The typed `v2` declared-contract layer now names the read-packet tier contract explicitly rather than leaving reading control ambient across one generic reference and several workflow habits.
- [d:r:i] The semantic layer now keeps the shared mandatory-read reference plus the three operator-facing workflow consumers explicit.
- [d:r:i] The evidence layer now records the landed `66` implementation note and focused read-packet contract test as anchors for this slice.
- [d:r:i] The coverage layer now records a ninth real non-uplift `change_triggered_slice_refresh`, so typed `v2` continues to prove itself against live reading-control movement rather than only against lifecycle carry or compatibility routes.

## Current Consequence

- [d:r:i] The typed `v2` registry now keeps shared reading-control doctrine visible alongside lifecycle and uplift movement instead of leaving operator read-packet posture ambient behind one small reference file and a few route-specific workflow habits.
- [d:r:i] Later refreshes should keep following actual movement into initialization surfaces, seed consumers, and wider packet retrofits rather than reopening the full entry/routing field in one jump.
