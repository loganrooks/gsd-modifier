Date: 2026-04-22
Status: landed uplift seed corpus posture change-triggered refresh

# Uplift Seed Corpus Posture Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `31`.
- [g:r:i] The trigger here is uplift-side seed visibility: project uplift now records current-versus-legacy seed corpus posture instead of leaving seed compatibility only at milestone-open.

## Trigger

- [e:c+i] The uplift family now carries a bounded landed slice through [79-uplift-side-seed-corpus-posture-first-slice-proposal.md](../intervention-proposals/79-uplift-side-seed-corpus-posture-first-slice-proposal.md) and [80-uplift-side-seed-corpus-posture-first-slice-implementation.md](../intervention-proposals/80-uplift-side-seed-corpus-posture-first-slice-implementation.md).
- [e:r:i] That slice changed the propagation field in four concrete ways:
  - `project_uplift.py` now scans seed corpus posture
  - `uplift-project` now presents seed posture explicitly
  - `gsd-uplift-project` now keeps that route explicit at the wrapper boundary
  - durable uplift outputs now preserve seed posture

## Refresh Result

- [d:r:i] The typed `v2` declared-contract layer now names uplift-side seed corpus posture explicitly instead of leaving this visibility route ambient inside helper prose.
- [d:r:i] The semantic layer now keeps the helper, uplift workflow, uplift wrapper, and uplift outputs aligned around seed posture rather than treating seed compatibility as only a milestone-open concern.
- [d:r:i] The evidence layer now records the landed `80` implementation note and focused uplift test file as anchors for this slice.
- [d:r:i] The coverage layer now records another real non-uplift `change_triggered_slice_refresh`, so typed `v2` keeps proving itself against project-wide seed posture carry, not only seed producer or milestone-open movement.

## Current Consequence

- [d:r:i] The typed `v2` registry now keeps uplift-side seed posture visible at the helper/workflow/wrapper/output cluster.
- [d:r:i] Later refreshes should now follow broader seed consumer widening, later audit widening, or wider entry-wrapper movement rather than reopening the same uplift-side seed visibility question.
