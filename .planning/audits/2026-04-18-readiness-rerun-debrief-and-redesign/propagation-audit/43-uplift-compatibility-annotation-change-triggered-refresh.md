Date: 2026-04-22
Status: landed change-triggered refresh

# Uplift Compatibility Annotation Change-Triggered Refresh

## Purpose

- [g:r:i] Record the next bounded `change_triggered_slice_refresh` after the compatibility-anchor and consumer follow-through refreshes in `16` and `17`.
- [g:r:i] The trigger here is narrower than a new compatibility family. The trigger is that the existing observed-basis anchor now carries one explicit held runtime annotation inside the same family.

## Trigger

- [e:c+i] [intervention-proposals/116-uplift-compatibility-annotation-first-slice-implementation.md](../intervention-proposals/116-uplift-compatibility-annotation-first-slice-implementation.md) lands the narrower annotation slice.
- [d:r:i] The propagation pressure is specific:
  - `project_uplift.py` now carries two different compatibility-bearing roles:
    - observed `.codex` basis
    - held `.claude` annotation
  - durable uplift memory now preserves both roles
  - read-only current-runtime consumers now surface the held annotation when present

## Refresh Result

- [d:r:i] The active compatibility-bearing carrier set is now wider than the `16` and `17` pairing alone:
  - the observed-basis anchor still lives in durable uplift memory
  - the held runtime annotation now lives beside it without relabeling the top-level posture
  - the read-only consumer chain now surfaces that held annotation too
- [d:r:i] The refresh also has to keep one helper-side asymmetry explicit:
  - runtime detection is wider than held-runtime annotation reading
  - the detection list sees several runtime roots
  - the held annotation reader still names only `.claude`
  - later third-runtime widening should inherit from that explicit asymmetry rather than from an accidental impression of broader live coverage
- [d:r:i] The typed `v2` layer therefore now needs to remember not only:
  - where the compatibility anchor is stored
  - where compatibility movement is surfaced back to operators
- [d:r:i] It now also needs to remember:
  - where held-runtime annotation semantics live
  - which carrier still owns the observed-basis label
  - which file supplies the held runtime annotation source

## Current Consequence

- [d:r:i] The compatibility family now has three consecutive real refreshes:
  - `16` for the initial observed-basis anchor
  - `17` for the live consumer-chain follow-through
  - `43` for the held-runtime annotation route
- [d:r:i] Later refreshes should keep distinguishing:
  - observed-basis runtime truth
  - held runtime annotation
  - wider detection frontier versus narrower annotation-reader coverage
  - wider cross-runtime compatibility claims still held for later
