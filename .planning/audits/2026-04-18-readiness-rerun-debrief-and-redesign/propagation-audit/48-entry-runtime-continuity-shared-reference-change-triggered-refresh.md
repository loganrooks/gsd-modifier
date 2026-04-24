Date: 2026-04-22
Status: landed change-triggered refresh

# Entry Runtime Continuity Shared-Reference Change-Triggered Refresh

## Purpose

- [g:r:i] Record the next bounded `change_triggered_slice_refresh` after the repair-facing health harden boundary in `47`.
- [g:r:i] The trigger here is not a broader compatibility-family widening.
- [g:r:i] The trigger is that repo-local entry/runtime continuity now reaches the earliest entry pair through one explicit shared reference.

## Trigger

- [e:c+i] [intervention-proposals/130-entry-runtime-continuity-shared-reference-first-slice-implementation.md](../intervention-proposals/130-entry-runtime-continuity-shared-reference-first-slice-implementation.md) lands the first live slice cleared by `129`.
- [d:r:i] The propagation pressure is specific:
  - one new overlay-owned reference now materializes into live `.codex`
  - `new-project.md` now points at that reference and carries a bounded read-only entry continuity step
  - `ingest-docs.md` now points at the same reference and carries a bounded read-only entry continuity step
  - `mandatory-initial-read.md` remains grammar-only while the sibling reference becomes the explicit continuity carrier

## Refresh Result

- [d:r:i] The compatibility-bearing carrier set is now wider than `16`, `17`, `43`, `44`, `45`, `46`, and `47` alone:
  - durable compatibility anchor still lives in uplift memory
  - held runtime annotation still lives beside it without relabeling top-level posture
  - transition/state continuity still owns preserve-versus-refresh at phase close
  - milestone open and milestone close still share their bounded uplift-continuity reference
  - health still carries repair-facing read-only uplift continuity
  - earliest entry routes now share one explicit entry/runtime continuity reference instead of leaving that carry ambient before later uplift follow-through
- [d:r:i] The typed `v2` layer therefore now needs to remember not only:
  - where current-runtime compatibility anchor and annotation live
  - where ordinary re-entry, lifecycle, milestone-boundary, and repair-facing consumers surface them
- [d:r:i] It now also needs to remember:
  - where entry/runtime continuity is defined as a reference carrier
  - where `new-project.md` and `ingest-docs.md` consume that carrier
  - where that carrier stays read-only and does not widen `mandatory-initial-read.md` into a grammar-plus-content-pointer surface

## Current Consequence

- [d:r:i] The compatibility family now has eight consecutive real refreshes:
  - `16` for the observed-basis anchor
  - `17` for the live consumer-chain follow-through
  - `43` for the held-runtime annotation route
  - `44` for the transition/state continuity bridge
  - `45` for milestone-boundary shared-reference carry
  - `46` for repair-facing health continuity
  - `47` for repair-facing harden follow-through
  - `48` for entry/runtime shared-reference carry
- [d:r:i] Later refreshes should keep distinguishing:
  - durable compatibility anchor
  - live current-runtime consumer carry
  - transition/state continuity carry
  - milestone-boundary shared-reference carry
  - repair-facing health continuity carry
  - earliest-entry shared-reference carry
  - later `update` plus `gsd-update` and `from-gsd2` consumer widening still held for the next branch
