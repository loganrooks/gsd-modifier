Date: 2026-04-22
Status: landed change-triggered refresh

# Transition-State Uplift Continuity Change-Triggered Refresh

## Purpose

- [g:r:i] Record the next bounded `change_triggered_slice_refresh` after the compatibility-family annotation slice in `43`.
- [g:r:i] The trigger here is not a new compatibility family. The trigger is that the existing observed-basis-plus-held-annotation chain now has an explicit transition/state continuity bridge.

## Trigger

- [e:c+i] [intervention-proposals/121-transition-state-uplift-continuity-first-slice-implementation.md](../intervention-proposals/121-transition-state-uplift-continuity-first-slice-implementation.md) lands the first ≤2-carrier consumer-chain slice cleared by `119` and sharpened by lane `12`.
- [d:r:i] The propagation pressure is specific:
  - `templates/state.md` now declares a top-level `Project Uplift` continuity slot
  - `project_uplift.py` now fills that declared slot in place rather than relying on undeclared placement
  - `transition.md` now owns preserve-versus-refresh handling for the compact uplift digest at phase close
  - the `gsd-tools.cjs phase complete` seam is now proved to preserve that block rather than left as ambient confidence

## Refresh Result

- [d:r:i] The active compatibility-bearing carrier set is now wider than `16`, `17`, and `43` alone:
  - the observed-basis anchor still lives in durable uplift memory
  - the held runtime annotation still lives beside it without relabeling top-level posture
  - the read-only consumer chain now includes phase-close continuity through the transition/state pair
- [d:r:i] The typed `v2` layer therefore now needs to remember not only:
  - where compatibility anchor and held annotation are stored
  - where current-runtime movement is surfaced back to operators
- [d:r:i] It now also needs to remember:
  - where the top-level state slot is declared
  - where preserve-versus-refresh is owned
  - where the CLI preservation seam is directly proved

## Current Consequence

- [d:r:i] The compatibility family now has four consecutive real refreshes:
  - `16` for the observed-basis anchor
  - `17` for the live consumer-chain follow-through
  - `43` for the held-runtime annotation route
  - `44` for the transition/state continuity bridge
- [d:r:i] Later refreshes should keep distinguishing:
  - durable compatibility anchor
  - live current-runtime consumer carry
  - transition/state continuity carry
  - broader shared-reference or health-side consumer widening still held for later priority choice
