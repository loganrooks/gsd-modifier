Date: 2026-04-22
Status: active bounded audit family

# Review Route Audit

## Purpose

- [g:r:i] This subtree audits and sharpens the repo-local cross-vendor review route centered on `$gsd-review`.
- [d:r:i] Its focus is not generic multi-provider parity.
- [d:r:i] Its focus is the repo-local review route as an operator surface:
  - review-run home
  - prompt and output durability
  - launch-truth and timing calibration
  - provider-shaped runner differences
  - failure-path salvage
  - planner-consumer carry into `REVIEWS.md`

## Current Lane

- [d:r:i] Lane `01` is completed:
  - [outputs/01-gsd-review-route-hardening-audit-opus47-max-r1.md](outputs/01-gsd-review-route-hardening-audit-opus47-max-r1.md)
  - [launch-truth/01-gsd-review-route-hardening-audit-launch-truth.md](launch-truth/01-gsd-review-route-hardening-audit-launch-truth.md)
  - [dispositions/01-gsd-review-route-hardening-audit-inheritance.md](dispositions/01-gsd-review-route-hardening-audit-inheritance.md)

## Expected Artifact Pattern

- [d:r:i] packet
- [d:r:i] spec
- [d:r:i] prompt
- [d:r:i] launch-truth
- [d:r:i] output
- [d:r:i] inheritance

## Current Consequence

- [d:r:i] The next move inside this family is no longer another widening lane on the same question.
- [d:r:i] The next move is the accepted first live slice:
  - harden the existing `gsd-review` route directly
  - use a helper-backed run-home / launch-truth / salvage layer beneath it
  - keep subject-keyed route splitting and larger telemetry / parity widening explicit as later adjacent routes
- [d:r:i] That first live slice is now explicit as a governed intervention object too:
  - [../intervention-proposals/143-gsd-review-helper-backed-run-home-first-slice-proposal.md](../intervention-proposals/143-gsd-review-helper-backed-run-home-first-slice-proposal.md)
  - [../intervention-proposals/145-gsd-review-helper-backed-run-home-first-slice-implementation.md](../intervention-proposals/145-gsd-review-helper-backed-run-home-first-slice-implementation.md)
  - [../propagation-audit/53-review-route-helper-backed-run-home-first-slice-change-triggered-refresh.md](../propagation-audit/53-review-route-helper-backed-run-home-first-slice-change-triggered-refresh.md)
