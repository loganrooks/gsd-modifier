Date: 2026-04-22
Status: landed change-triggered refresh

# Milestone-Boundary Uplift Shared-Reference Change-Triggered Refresh

## Purpose

- [g:r:i] Record the next bounded `change_triggered_slice_refresh` after the transition/state continuity bridge in `44`.
- [g:r:i] The trigger here is narrower than a new compatibility family.
- [g:r:i] The trigger is that compatibility-family continuity now reaches milestone open and milestone close through one explicit shared reference.

## Trigger

- [e:c+i] [intervention-proposals/123-milestone-boundary-uplift-shared-reference-first-slice-implementation.md](../intervention-proposals/123-milestone-boundary-uplift-shared-reference-first-slice-implementation.md) lands the reread-cleared shared-reference slice from `122`.
- [d:r:i] The propagation pressure is specific:
  - one new overlay-owned reference now materializes into live `.codex`
  - `new-milestone.md` now reads that reference at milestone open
  - `complete-milestone.md` now reads that same reference at milestone close
  - both workflows now widen from `STATE.md` into `UPLIFT-REPORT.md` and `UPLIFT-MANIFEST.json` through one explicit read-only carrier rather than through ambient route memory

## Refresh Result

- [d:r:i] The compatibility-bearing carrier set is now wider than `16`, `17`, `43`, and `44` alone:
  - durable compatibility anchor still lives in uplift memory
  - held runtime annotation still lives beside it without relabeling top-level posture
  - phase-close transition/state continuity still owns preserve-versus-refresh at that boundary
  - milestone open and milestone close now share one explicit uplift-continuity reference instead of relying only on neighboring lifecycle carriers
- [d:r:i] The typed `v2` layer therefore now needs to remember not only:
  - where the compact state digest is declared and refreshed
  - where ordinary re-entry consumers surface current-runtime compatibility movement
- [d:r:i] It now also needs to remember:
  - where milestone-boundary uplift continuity is defined as a reference carrier
  - where milestone-open and milestone-close consume that reference
  - where that shared reference widens toward `STATE.md`, `UPLIFT-REPORT.md`, and `UPLIFT-MANIFEST.json`

## Current Consequence

- [d:r:i] The compatibility family now has five consecutive real refreshes:
  - `16` for the observed-basis anchor
  - `17` for the live consumer-chain follow-through
  - `43` for the held-runtime annotation route
  - `44` for the transition/state continuity bridge
  - `45` for milestone-boundary shared-reference carry
- [d:r:i] Later refreshes should keep distinguishing:
  - durable compatibility anchor
  - live current-runtime consumer carry
  - transition/state continuity carry
  - milestone-boundary shared-reference carry
  - adjacent `health.md` deepen-in-place follow-through still held for later
