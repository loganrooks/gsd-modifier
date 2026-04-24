Date: 2026-04-21
Status: landed initialization and ingest read-packet change-triggered refresh

# Initialization And Ingest Read-Packet Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `25`.
- [g:r:i] The trigger here is a second reading-contract move: the shared mandatory-read reference now reaches initialization and doc-ingest workflows, and the repo-local uplift route is kept explicit where older or vanilla project posture can surface during those workflows.

## Trigger

- [e:c+i] The initialization/onboarding family now carries a bounded landed slice through [67-initialization-and-ingest-read-packet-first-slice-proposal.md](../intervention-proposals/67-initialization-and-ingest-read-packet-first-slice-proposal.md) and [68-initialization-and-ingest-read-packet-first-slice-implementation.md](../intervention-proposals/68-initialization-and-ingest-read-packet-first-slice-implementation.md).
- [e:r:i] That slice changed the propagation field in four concrete ways:
  - the tracked overlay now owns `new-project.md` and `ingest-docs.md` alongside `new-milestone.md`
  - the shared mandatory-read reference now reaches initialization and ingest consumers instead of only re-entry consumers
  - `new-project` now keeps existing-project refresh pressure explicit as `progress -> uplift` rather than reopening initialization
  - `ingest-docs` now keeps planning-doc merge distinct from later repo-local uplift instead of blending those routes

## Refresh Result

- [d:r:i] The typed `v2` declared-contract layer now names the initialization/ingest read-packet contract explicitly rather than leaving the second packet family ambient behind one shared reference and three workflow habits.
- [d:r:i] The semantic layer now keeps `new-project`, `new-milestone`, and `ingest-docs` explicit as additional reading-control consumers, plus their explicit shared-reference and bounded uplift-route relations.
- [d:r:i] The evidence layer now records the landed `68` implementation note and focused initialization contract test as anchors for this slice.
- [d:r:i] The coverage layer now records a tenth real non-uplift `change_triggered_slice_refresh`, so typed `v2` continues to prove itself against live onboarding movement rather than only against re-entry, lifecycle carry, or compatibility routes.

## Current Consequence

- [d:r:i] The typed `v2` registry now keeps layered reading control visible across both re-entry and the primary initialization/doc-ingest surfaces instead of leaving initialization as a flatter untyped pocket.
- [d:r:i] Later refreshes should keep following actual movement into `health`, `from-gsd2`, seed consumers, and any later wider packet retrofit rather than reopening the whole onboarding field in one jump.
