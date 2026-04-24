Date: 2026-04-21
Status: landed update follow-through change-triggered refresh

# Update Follow-Through Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `27`.
- [g:r:i] The trigger here is a runtime/package route move: `update` now inherits the shared read-packet doctrine and keeps structural repair plus later repo-local uplift explicit rather than ambient beside install/version movement.

## Trigger

- [e:c+i] The update family now carries a bounded landed slice through [71-update-follow-through-first-slice-proposal.md](../intervention-proposals/71-update-follow-through-first-slice-proposal.md) and [72-update-follow-through-first-slice-implementation.md](../intervention-proposals/72-update-follow-through-first-slice-implementation.md).
- [e:r:i] That slice changed the propagation field in four concrete ways:
  - the tracked overlay now owns `update.md` and `skills/gsd-update/SKILL.md`
  - the shared mandatory-read reference now reaches `update` as another operator-facing consumer
  - `update` now keeps runtime/package movement, structural repair, and later uplift as separate routes instead of one flatter runtime-success story
  - the `gsd-update` wrapper now keeps runtime/package ownership explicit while routing structural planning issues and later posture refresh separately

## Refresh Result

- [d:r:i] The typed `v2` declared-contract layer now names the update follow-through contract explicitly instead of leaving this route boundary ambient behind one workflow and one wrapper.
- [d:r:i] The semantic layer now keeps `update`, `gsd-update`, the shared mandatory-read reference, and the new update-to-health / update-to-uplift relations explicit.
- [d:r:i] The evidence layer now records the landed `72` implementation note and focused update contract test as anchors for this slice.
- [d:r:i] The coverage layer now records another real non-uplift `change_triggered_slice_refresh`, so typed `v2` keeps proving itself against live onboarding and runtime movement rather than only against earlier repair/migration, initialization, re-entry, compatibility, and lifecycle routes.

## Current Consequence

- [d:r:i] The typed `v2` registry now keeps update-side route separation visible alongside repair/migration and initialization/onboarding entry control instead of leaving runtime movement as another flatter local pocket.
- [d:r:i] Later refreshes should keep following actual movement into seed consumers, wider entry-wrapper retrofit, and any broader repeated-reinstall / compatibility carrier rather than reopening the whole onboarding field in one jump.

