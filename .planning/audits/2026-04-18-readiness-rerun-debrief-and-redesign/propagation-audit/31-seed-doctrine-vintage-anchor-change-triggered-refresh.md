Date: 2026-04-21
Status: landed seed doctrine vintage anchor change-triggered refresh

# Seed Doctrine Vintage Anchor Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `30`.
- [g:r:i] The trigger here is a compact compatibility anchor: current seeds now stamp their contract version explicitly, and milestone-open now treats missing markers as `legacy_unversioned` rather than leaving that distinction ambient.

## Trigger

- [e:c+i] The seed family now carries a bounded landed slice through [77-seed-doctrine-vintage-anchor-first-slice-proposal.md](../intervention-proposals/77-seed-doctrine-vintage-anchor-first-slice-proposal.md) and [78-seed-doctrine-vintage-anchor-first-slice-implementation.md](../intervention-proposals/78-seed-doctrine-vintage-anchor-first-slice-implementation.md).
- [e:r:i] That slice changed the propagation field in three concrete ways:
  - `plant-seed` now stamps `seed_contract_version: 2`
  - `new-milestone` now treats missing version markers as `legacy_unversioned`
  - `gsd-plant-seed` keeps the current version anchor explicit at the wrapper boundary

## Refresh Result

- [d:r:i] The typed `v2` declared-contract layer now names the seed doctrine-vintage anchor explicitly instead of leaving current-versus-legacy seed shape as an ambient reading habit.
- [d:r:i] The semantic layer now keeps the version anchor and legacy tolerance inside the existing `plant-seed -> new-milestone` bridge rather than pretending this slice created a separate consumer family.
- [d:r:i] The evidence layer now records the landed `78` implementation note and widened seed contract test as anchors for this slice.
- [d:r:i] The coverage layer now records another real non-uplift `change_triggered_slice_refresh`, so typed `v2` keeps proving itself against seed compatibility carry, not only against seed producer convergence.

## Current Consequence

- [d:r:i] The typed `v2` registry now keeps current-versus-legacy seed shape visible at the main producer and main milestone-open consumer.
- [d:r:i] Later refreshes should follow broader consumer widening, uplift-side seed scanning, and later audit consumer widening rather than reopening the same vintage anchor question.
