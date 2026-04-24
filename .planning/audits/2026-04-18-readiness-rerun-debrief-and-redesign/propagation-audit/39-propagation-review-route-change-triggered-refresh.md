Date: 2026-04-22
Status: landed change-triggered refresh

# Propagation Review Route Change-Triggered Refresh

## Purpose

- [g:r:i] Record the new operator-facing propagation-review route inside the typed propagation family instead of leaving it as a workflow/skill addition that later operators have to rediscover.

## What Moved

- [e:c+i] The repo now carries:
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md)
  - [gsd-propagation-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-propagation-review/SKILL.md)
  - [97-propagation-review-route-first-slice-proposal.md](../intervention-proposals/97-propagation-review-route-first-slice-proposal.md)
  - [98-propagation-review-route-first-slice-implementation.md](../intervention-proposals/98-propagation-review-route-first-slice-implementation.md)
- [d:r:i] The route binds the first baseline/delta pair back into live operator practice:
  - [95-upstream-pristine-propagation-baseline-first-slice.md](../intervention-proposals/95-upstream-pristine-propagation-baseline-first-slice.md)
  - [96-repo-local-propagation-delta-first-slice.md](../intervention-proposals/96-repo-local-propagation-delta-first-slice.md)

## Registry Consequence

- [d:r:i] The typed `v2` layer should now keep:
  - the new workflow and wrapper as explicit carriers
  - the baseline/delta pair as explicit route inputs
  - the route's contract test as tested behavior evidence
- [d:r:i] This refresh does not widen the whole family again.
- [d:r:i] It records one new operator-facing route that strengthens how later multi-family slices are reviewed.

## Current Consequence

- [d:r:i] Later propagation-sensitive work can now route through one dedicated review surface instead of rebuilding the baseline/delta plus registry packet from chat memory.
