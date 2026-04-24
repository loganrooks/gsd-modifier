Date: 2026-04-22
Status: accepted bounded proposal

# Propagation Review Route First Slice Proposal

## Purpose

- [g:r:i] Add one operator-facing propagation-review route so multi-family contract changes are reviewed through a consistent baseline/delta/carrier packet instead of relying only on memory, ad hoc reread, or local diff intuition.

## Why This Slice Now

- [d:c+i] The workspace now has:
  - an upstream-pristine baseline via [95-upstream-pristine-propagation-baseline-first-slice.md](95-upstream-pristine-propagation-baseline-first-slice.md)
  - a repo-local delta layer via [96-repo-local-propagation-delta-first-slice.md](96-repo-local-propagation-delta-first-slice.md)
  - a typed `v2` propagation family under `propagation-audit/artifacts/03-06`
- [d:r:i] What is still thinner than it should be is the operator-facing route that tells later work how to use those layers on a concrete change-triggered slice.

## Proposed First Slice

- [d:r:i] Add one repo-local workflow:
  - `propagation-review.md`
- [d:r:i] Add one repo-local skill wrapper:
  - `gsd-propagation-review`
- [d:r:i] Keep the route hybrid:
  - baseline/delta docs disclose the field
  - typed registry surfaces disclose current carrier/evidence layers
  - local tools widen visibility where they fit
  - contextual reread plus explicit hold/update disposition remain sovereign

## What The Route Should Do

- [d:r:i] Take one concrete contract-changing slice as input.
- [d:r:i] Map:
  - direct producers
  - direct consumers
  - narrative mirrors
  - runtime and registry carriers
  - durable outputs and state surfaces
  - intentionally held neighbors
- [d:r:i] Say whether each important carrier belongs to:
  - upstream-pristine baseline
  - repo-local delta
  - mixed baseline-plus-delta widening
- [d:r:i] Use repo-local tooling only as partial visibility, never as total proof.
- [d:r:i] Keep the route read-only by default, with an explicit durable-note option when the caller wants it.

## Expected Gains

- [d:r:i] Better maintainability when live slices widen across several families.
- [d:r:i] Better control over what to reread in detail and what to keep at packet level.
- [d:r:i] Cleaner propagation discipline for future workflow/skill/helper additions.
- [d:r:i] A more reusable operator route than relying on one audit subtree's memory.

## Held Later

- [d:r:i] No automatic dependency extraction in this slice.
- [d:r:i] No new diff helper in this slice.
- [d:r:i] No dedicated uplift agent-assist in this slice.
- [d:r:i] No broad wrapper rewrite or new telemetry family in this slice.

## Verification Gates

- [d:r:i] Overlay ownership must include the new workflow and skill.
- [d:r:i] A focused contract test should prove:
  - the route exists in the tracked overlay
  - the workflow reads the baseline/delta pair
  - the workflow names the bounded runtime/install gate tools
  - the skill keeps the route read-only by default and specialist handoffs explicit
- [d:r:i] Repo-local materialization should be rerun after landing the overlay slice.

## Current Consequence

- [d:r:i] The next concrete move after this proposal is implementation of the first route slice, not another abstract propagation widening pass.
