Date: 2026-04-21
Status: landed change-triggered consumer follow-through

# Compatibility Consumer Follow-Through Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `16`.
- [g:r:i] The trigger here is not a new compatibility family. The trigger is the xhigh reread finding that the compatibility anchor had reached durable outputs but had not yet reached the live read-only consumer chain.

## Trigger

- [e:c+i] [intervention-proposals/44-project-uplift-compatibility-consumer-follow-through.md](../intervention-proposals/44-project-uplift-compatibility-consumer-follow-through.md) lands the narrowed correction.
- [d:r:i] The propagation pressure is specific:
  - `project_uplift.py` now routes compatibility-basis movement into `progress-note`
  - `progress` and `resume-project` therefore inherit a live compatibility-drift prompt surface
  - canonical runtime-basis sourcing is sharper than before

## Refresh Result

- [d:r:i] The active compatibility-bearing carrier set is now broader than the earlier `16` slice alone:
  - durable outputs still carry the observed-basis anchor
  - the read-only routed consumers now surface runtime-basis movement too
- [d:r:i] The typed `v2` semantic layer therefore now needs to remember not only where the compatibility anchor is stored, but where it is actively surfaced back to operators.

## Current Consequence

- [d:r:i] The compatibility family now has two consecutive real refreshes:
  - `16` for the initial anchor insertion
  - `17` for the consumer-chain follow-through
- [d:r:i] Later refreshes should keep watching whether compatibility movement remains bounded inside the uplift family or starts earning a broader standalone carrier.
