Date: 2026-04-22
Status: accepted bounded proposal

# Propagation Review Route Harden Follow-Through Proposal

## Purpose

- [g:r:i] Sharpen the newly landed `propagation-review` route at the points the first reread left thinner:
  - durable-note carry
  - tool-result-to-disposition carry
  - slightly wider focused contract-test coverage

## Why This Slice Now

- [d:c+i] The route itself is now landed through [97-propagation-review-route-first-slice-proposal.md](97-propagation-review-route-first-slice-proposal.md), [98-propagation-review-route-first-slice-implementation.md](98-propagation-review-route-first-slice-implementation.md), and [../propagation-audit/39-propagation-review-route-change-triggered-refresh.md](../propagation-audit/39-propagation-review-route-change-triggered-refresh.md).
- [d:c+i] The first bounded reread is now also inherited through [../propagation-audit/outputs/07-propagation-review-route-reread-opus47-max-r1.md](../propagation-audit/outputs/07-propagation-review-route-reread-opus47-max-r1.md) and [../propagation-audit/dispositions/07-propagation-review-route-reread-inheritance.md](../propagation-audit/dispositions/07-propagation-review-route-reread-inheritance.md).
- [d:r:i] That reread no longer leaves the next move ambiguous:
  - do not jump yet to later uplift agent-assist
  - first harden the route that is supposed to keep later multi-family change under control

## Proposed Follow-Through

- [d:r:i] Add explicit route-local guidance for where durable notes should live when they are written.
- [d:r:i] Add explicit route-local guidance for how partial tool results shape `Updated In This Slice` versus `Held With Explicit Boundary`.
- [d:r:i] Slightly widen the focused contract test so output-shape and durable-note carry are part of the tested frontier, not only the original five invariants.
- [d:r:i] Carry the same sharpened doctrine into the local planning governance note and the operator-routes README surface.

## Held Later

- [d:r:i] No uplift agent-assist in this slice.
- [d:r:i] No broader pristine-diff or freshness-signal family in this slice.
- [d:r:i] No attempt to turn `propagation-review` into a whole propagation engine in this slice.

## Verification Gates

- [d:r:i] Focused contract tests for the route must pass after the harden slice lands.
- [d:r:i] Repo-local materialization must be rerun after overlay-backed route changes land.
- [d:r:i] Propagation registry and governance carriers must be refreshed in the same slice instead of left ambient.

## Current Consequence

- [d:r:i] The next concrete move after this proposal is the bounded harden implementation, not another route-review loop.
