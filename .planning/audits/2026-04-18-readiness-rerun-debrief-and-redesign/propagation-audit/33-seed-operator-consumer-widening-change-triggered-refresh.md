Date: 2026-04-22
Status: landed seed operator-consumer widening change-triggered refresh

# Seed Operator-Consumer Widening Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `32`.
- [g:r:i] The trigger here is operator-facing seed visibility: progress and resume now surface seed corpus posture through the existing uplift-note bridge instead of leaving that route implicit.

## Trigger

- [e:c+i] The seed family now carries a bounded landed slice through [81-seed-operator-consumer-widening-first-slice-proposal.md](../intervention-proposals/81-seed-operator-consumer-widening-first-slice-proposal.md) and [82-seed-operator-consumer-widening-first-slice-implementation.md](../intervention-proposals/82-seed-operator-consumer-widening-first-slice-implementation.md).
- [e:r:i] That slice changed the propagation field in three concrete ways:
  - `project_uplift.py` now emits operator-facing seed posture fields in its progress-note payload
  - `progress` now keeps seed posture visible when the seed corpus exists
  - `resume-project` now keeps the same route visible during re-entry

## Refresh Result

- [d:r:i] The typed `v2` declared-contract layer now names operator-facing seed posture visibility explicitly instead of leaving it implied inside the older uplift helper boundary.
- [d:r:i] The semantic layer now keeps `project_uplift -> progress` and `project_uplift -> resume-project` aligned around seed posture visibility rather than treating those edges as generic uplift-note bridges only.
- [d:r:i] The evidence layer now records the landed `82` implementation note and the focused operator-consumer contract test as anchors for this slice.
- [d:r:i] The coverage layer now keeps ordinary operator-facing seed visibility explicit before later audit widening or wider wrapper retrofit inherit next.

## Current Consequence

- [d:r:i] The typed `v2` registry now keeps operator-facing seed posture visible at the helper -> progress/resume bridge.
- [d:r:i] Later refreshes should now follow audit widening, wider entry-wrapper movement, or later legacy-seed migration rather than reopening this same operator-facing seed visibility route.
