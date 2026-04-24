Date: 2026-04-21
Status: landed first change-triggered v2 refresh

# Compatibility Anchor Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the first real `change_triggered_slice_refresh` after the typed `v2` propagation split landed in `15`.
- [g:r:i] The trigger here is the project-uplift compatibility anchor slice, not a synthetic registry exercise.

## Trigger

- [e:r:i] The uplift producer now writes an explicit observed-basis compatibility block into its durable outputs. See [43-project-uplift-compatibility-anchor-slice.md](../intervention-proposals/43-project-uplift-compatibility-anchor-slice.md).
- [d:r:i] That changed contract widens the propagation field in three concrete ways:
  - runtime-version anchors are no longer only ambient facts
  - `UPLIFT-MANIFEST.json` now carries explicit compatibility structure, not only uplift posture
  - `UPLIFT-REPORT.md` and `STATE.md` now mirror that compatibility anchor in operator-facing form

## Refresh Result

- [d:r:i] The typed `v2` registry now answers back to that slice by making the compatibility-bearing carriers and edges more explicit.
- [d:r:i] The refresh is still bounded:
  - it does not invent a new standalone family
  - it does not widen into a whole compatibility matrix
  - it does not treat the uplift anchor as final whole-network compatibility truth

## What Moved

- [e:r:i] The semantic map now names the runtime version sources and the uplift durable outputs more explicitly as propagation carriers.
- [e:r:i] The evidence index now includes the current runtime manifest and runtime version anchors as distinct observed-runtime evidence rows.
- [e:r:i] The coverage/refresh control surface no longer leaves `compatibility surface` as a flat held pressure. The held pressure is narrower now: wider compatibility-window carry and any later standalone compatibility carrier.

## Current Consequence

- [d:r:i] The typed `v2` split has now survived one real slice refresh on live repo-local contract change.
- [d:r:i] The next registry refresh should again be triggered by an actual contract move rather than by abstract appetite for a bigger map.
