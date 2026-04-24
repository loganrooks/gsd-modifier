Date: 2026-04-22
Status: frozen lane spec

# GSD Review Route Hardening Audit Spec

## Task

- [g:r:i] Audit the current repo-local `$gsd-review` route and produce the sharpest bounded first-slice hardening shape for this repo.

## Required Judgment Shape

- [g:r:i] Judge the route as an operator and planner-carry surface, not only as a command that can produce a `REVIEWS.md` file.
- [g:r:i] Keep provider-shaped differences explicit.
- [g:r:i] Keep failure-path salvage explicit.
- [g:r:i] Keep lane-home and launch-truth discipline explicit.
- [g:r:i] Keep the planner consumer contract explicit so later replanning can still use the route cleanly.
- [g:r:i] Name adjacent review-workflow uplift opportunities when they materially sharpen the route family, while still distinguishing:
  - what should land in the first live slice
  - what should remain a later adjacent route

## Avoid

- [g:r:i] Do not collapse the answer into “existing route is fine” or “replace it entirely” without mapping the concrete route family.
- [g:r:i] Do not respond with generic “better logging” or “more telemetry” language if a narrower structure can be named.
- [g:r:i] Do not treat all vendors as one runner shape.
- [g:r:i] Do not over-widen into generic cloud/distribution/platform parity.
- [g:r:i] Do not let one gating question consume the larger shaping question of how to make the route carry more of the review/audit discipline already earned elsewhere in the harness.

## Output Shape

Return markdown with exactly these sections:

```markdown
# GSD Review Route Audit

## Current Route Reading
- ...

## Keep Versus Replace
- ...

## Reviewer Shapes
- ...

## First-Slice Hardening Shape
- ...

## Helper Versus Workflow Split
- ...

## Failure Salvage And Last-Message Recovery
- ...

## Other Review Workflow Uplift Routes
- ...

## Verification And Review Gates
- ...

## Held Later
- ...

## Exact Next Move
- ...
```

## Strength Of Recommendation

- [g:r:i] If the current route should be hardened in place, say so directly.
- [g:r:i] If a helper-backed layer should be introduced, say what it owns and what it does not own.
- [g:r:i] If the route should preserve multiple runner kinds, say which ones.
- [g:r:i] If the route should preserve different artifact homes, say which ones.
