Date: 2026-04-22
Status: landed orientation note

# Repo-Local Workflow Additions And Propagation Map Orientation

## Purpose

- [g:r:i] Keep three live operator questions explicit in one compact place instead of leaving them distributed across chat memory:
  - which repo-local workflows were actually added beyond pristine upstream GSD
  - whether workflow-surface expansion of that kind looks promising here
  - how the stable upstream propagation map and the evolving repo-local propagation map currently relate

## Repo-Local Workflow Additions

- [e:c+i] Repo-local GSD now carries three workflow additions that pristine upstream does not ship:
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md:1)
  - [seed-migration-inventory.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md:1)
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:1)
- [e:c+i] The upstream-pristine baseline explicitly excludes repo-local-only workflows such as `uplift-project.md` and `seed-migration-inventory.md`, which keeps the stable/original map readable as a separate surface instead of silently absorbing local additions. Source: [95-upstream-pristine-propagation-baseline-first-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/95-upstream-pristine-propagation-baseline-first-slice.md:119).
- [e:c+i] The repo-local delta explicitly records the same three families as local additions or local operator-facing widening:
  - uplift composition layer
  - seed specialist route
  - propagation review route
  Sources:
  - [96-repo-local-propagation-delta-first-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/96-repo-local-propagation-delta-first-slice.md:29)
  - [96-repo-local-propagation-delta-first-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/96-repo-local-propagation-delta-first-slice.md:40)
  - [96-repo-local-propagation-delta-first-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/96-repo-local-propagation-delta-first-slice.md:99)

## Why These Workflow Additions Look Promising

- [d:c+i] `uplift-project` is promising because it keeps project-uplift composition explicit without absorbing specialist-owner routes, while still producing durable report/manifest/state outputs when the operator wants them. Sources:
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md:24)
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md:104)
- [d:c+i] `seed-migration-inventory` is promising because it creates a sharper specialist packet for legacy/drifted seed posture without collapsing directly into rewrite automation or broader normalization. Sources:
  - [seed-migration-inventory.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md:23)
  - [seed-migration-inventory.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md:79)
  - [seed-migration-inventory.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md:91)
- [d:c+i] `propagation-review` is promising because it binds concrete contract-changing slices to the baseline/delta pair, typed registry widening, partial-tool visibility, explicit hold/update disposition, and bounded verification instead of leaving that propagation labor to local memory. Sources:
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:39)
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:58)
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:133)

## Stable And Evolving Propagation Maps

- [e:c+i] The stable/original propagation map is now carried explicitly by the upstream-pristine baseline artifact at [95-upstream-pristine-propagation-baseline-first-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/95-upstream-pristine-propagation-baseline-first-slice.md:8).
- [e:c+i] The evolving repo-local map is now carried explicitly by the delta artifact at [96-repo-local-propagation-delta-first-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/96-repo-local-propagation-delta-first-slice.md:8).
- [e:c+i] The richer working propagation family still lives in the typed `v2` registry and refresh surfaces rather than only in the operator-facing baseline/delta pair. Sources:
  - [96-repo-local-propagation-delta-first-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/96-repo-local-propagation-delta-first-slice.md:61)
  - [03-propagation-registry-v2-declared-contracts.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/artifacts/03-propagation-registry-v2-declared-contracts.json)
  - [06-propagation-registry-v2-coverage-and-refresh.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/artifacts/06-propagation-registry-v2-coverage-and-refresh.json)

## How Propagation Mapping Is Currently Updated

- [e:c+i] The current method is change-triggered and inheritance-driven rather than static:
  - prose widening and inheritance lanes
  - typed registry `v2` refreshes
  - change-triggered slice refresh notes
  - operator-facing review through `$gsd-propagation-review`
  Sources:
  - [96-repo-local-propagation-delta-first-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/96-repo-local-propagation-delta-first-slice.md:69)
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:5)
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:123)

## Current Consequence

- [d:r:i] The workflow-addition question no longer needs to be answered from memory:
  - current repo-local additions are explicit
  - the stable/original versus evolving/local propagation split is explicit
  - the updating method is explicit
- [d:r:i] The next adjacent route can therefore narrow onto the remaining live question inside this family: how repo-local uplift should later use bounded agent-assist without dissolving the composition layer.
