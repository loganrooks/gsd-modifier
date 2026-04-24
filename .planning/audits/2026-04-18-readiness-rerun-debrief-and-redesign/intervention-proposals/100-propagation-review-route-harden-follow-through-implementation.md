Date: 2026-04-22
Status: landed bounded harden slice

# Propagation Review Route Harden Follow-Through Implementation

## What Landed

- [e:c+i] The route workflow now makes the tool-result-to-disposition bridge explicit in [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md).
- [e:c+i] The route workflow and wrapper now also make durable-note placement more explicit:
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md)
  - [gsd-propagation-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-propagation-review/SKILL.md)
- [e:c+i] Local planning governance now carries the same routing rule in [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md).
- [e:c+i] The operator-routes surface in [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md) now mirrors the same sharpened route posture.
- [e:c+i] The focused route contract test is now wider in [test_propagation_review_route_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_propagation_review_route_contract.py).

## What This Hardens

- [d:r:i] Durable-note carry is less ambient:
  - `outputs/` for preserved external or composite returns
  - `dispositions/` for local inheritance or judgment
  - `*-change-triggered-refresh.md` when the note becomes a new propagation-baseline carrier
- [d:r:i] Claim-type carry is no longer left to operator invention when notes land inside this audit workspace.
- [d:r:i] Clean helper output no longer risks looking like automatic closure:
  - if a tool flags a carrier and the route moves it now, carry it under `Updated In This Slice`
  - if the route holds it, carry the reason under `Held With Explicit Boundary`
  - if tools stay clean but contextual reread still sees a neighboring carrier, keep that carrier explicit rather than silently erasing it

## Verification

- [e:c+i] Focused route contract tests pass in [test_propagation_review_route_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_propagation_review_route_contract.py).
- [e:c+i] Repo-local materialization was rerun through [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh) after the overlay-backed route changes landed.
- [e:c+i] The propagation registry and governance carriers were refreshed in the same slice through [../propagation-audit/40-propagation-review-route-harden-change-triggered-refresh.md](../propagation-audit/40-propagation-review-route-harden-change-triggered-refresh.md).

## Current Consequence

- [d:r:i] The route now carries its outputs, dispositions, and narrower helper semantics more explicitly than the first-slice form.
- [d:r:i] The next adjacent family move is no longer another harden pass by default.
- [d:r:i] The next adjacent family move can now shift back toward later uplift agent-assist or other held-later propagation families on a cleaner operator-facing route.
