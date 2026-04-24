Date: 2026-04-22
Status: landed first slice

# Propagation Review Route First Slice Implementation

## What Landed

- [e:c+i] One new repo-local workflow now carries the route:
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md)
- [e:c+i] One new repo-local skill wrapper now binds that route for operator use:
  - [gsd-propagation-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-propagation-review/SKILL.md)
- [e:c+i] Tracked overlay ownership now includes both surfaces in [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json).

## Route Shape

- [d:r:i] The route is read-only by default.
- [d:r:i] It reads the upstream-pristine baseline plus the repo-local delta layer first:
  - [95-upstream-pristine-propagation-baseline-first-slice.md](95-upstream-pristine-propagation-baseline-first-slice.md)
  - [96-repo-local-propagation-delta-first-slice.md](96-repo-local-propagation-delta-first-slice.md)
- [d:r:i] It then widens through the current typed propagation family only as needed:
  - `propagation-audit/README.md`
  - `artifacts/03-06`
- [d:r:i] It keeps tooling partial:
  - `audit_refmap.py`
  - `project_uplift.py`
  - `runtime_visibility.py`
  - `manifest_install_coherence.py --strict`
  - `harness_canary.py report . --strict`
- [d:r:i] It keeps contextual reread and explicit hold/update disposition sovereign over tool output.

## Why This Raises Carry

- [d:r:i] The repo now has a dedicated operator-facing route for reviewing multi-family contract movement instead of relying on local diff intuition or one audit subtree's memory.
- [d:r:i] The route also keeps progressive disclosure explicit:
  - baseline/delta pair first
  - typed registry widening second
  - older propagation lane history only when the active slice actually needs it

## Verification

- [e:c+i] Focused contract coverage now exists in [test_propagation_review_route_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_propagation_review_route_contract.py).
- [e:c+i] Repo-local materialization was rerun after the overlay changes through [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh).

## Current Consequence

- [d:r:i] The propagation family now has:
  - prose widening and inheritance lanes
  - typed registry `v2`
  - upstream-pristine baseline and repo-local delta pair
  - one operator-facing review route for concrete change-triggered slices
- [d:r:i] The next bounded question is not whether the route exists.
- [d:r:i] The next bounded question is whether an Opus reread over this new route exposes narrower follow-through that should land before any later uplift agent-assist route.
