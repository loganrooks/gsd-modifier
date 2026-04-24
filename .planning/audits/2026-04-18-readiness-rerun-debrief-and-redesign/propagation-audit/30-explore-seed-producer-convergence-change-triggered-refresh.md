Date: 2026-04-21
Status: landed explore-seed producer convergence change-triggered refresh

# Explore Seed Producer Convergence Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `29`.
- [g:r:i] The trigger here is a stale seed-producer correction: `explore` and `gsd-explore` now route selected seed outputs through the current `plant-seed` contract instead of describing legacy inline seed minting.

## Trigger

- [e:c+i] The seed family now carries a bounded landed slice through [75-explore-seed-producer-convergence-first-slice-proposal.md](../intervention-proposals/75-explore-seed-producer-convergence-first-slice-proposal.md) and [76-explore-seed-producer-convergence-first-slice-implementation.md](../intervention-proposals/76-explore-seed-producer-convergence-first-slice-implementation.md).
- [e:r:i] That slice changed the propagation field in four concrete ways:
  - the tracked overlay now owns `explore.md` and `skills/gsd-explore/SKILL.md`
  - `explore` now routes seed outputs through `$gsd-plant-seed`
  - the wrapper keeps that current route explicit too
  - the seed family now has an explicit upstream ideation producer edge into the current `plant-seed` producer instead of leaving that relation ambient or stale

## Refresh Result

- [d:r:i] The typed `v2` declared-contract layer now names the `explore` seed-producer convergence contract explicitly instead of leaving this producer correction ambient behind one workflow patch and one wrapper line.
- [d:r:i] The semantic layer now keeps `explore`, `gsd-explore`, and the `explore -> plant-seed` route explicit alongside the existing `plant-seed -> new-milestone` consumer bridge.
- [d:r:i] The evidence layer now records the sidecar mapping memo, landed `76` implementation note, and focused explore-seed contract test as anchors for this slice.
- [d:r:i] The coverage layer now records another real non-uplift `change_triggered_slice_refresh`, so typed `v2` keeps proving itself against live producer convergence rather than only against downstream seed consumption.

## Current Consequence

- [d:r:i] The typed `v2` registry now keeps the ideation-side seed producer correction visible instead of leaving the seed family split between one current producer and one stale upstream output description.
- [d:r:i] Later refreshes should now follow actual movement into seed doctrine-vintage, broader consumers, and later `audit.cjs` widening rather than revisiting stale producer cleanup again.
