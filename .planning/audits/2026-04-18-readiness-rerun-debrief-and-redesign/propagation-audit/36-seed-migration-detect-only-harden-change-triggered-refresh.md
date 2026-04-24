Date: 2026-04-22
Status: landed change-triggered refresh

# Seed Migration Detect-Only Harden Change-Triggered Refresh

## Why This Refresh Exists

- [d:c+i] The landed detect-only packet was reread under [04-seed-migration-detect-only-first-slice-reread-opus47-max-r1.md](outputs/04-seed-migration-detect-only-first-slice-reread-opus47-max-r1.md), then sharpened inside the same carrier family through [intervention-proposals/88-seed-migration-detect-only-harden-follow-through-implementation.md](../intervention-proposals/88-seed-migration-detect-only-harden-follow-through-implementation.md).
- [d:r:i] The typed `v2` propagation layers should now remember that the helper/workflow/wrapper/uplift cluster carries more than the first landed route:
  - route-state split
  - post-write durable-output state
  - producer-follow-through to `plant-seed`
  - uplift-side shape-gap discovery
  - narrower reading / write guidance

## What Moves In The Typed Registry

- [d:r:i] The seed-migration helper carrier now implies a sharper contract:
  - current seed-shape constants shared with `project_uplift.py`
  - route-state distinctions that separate `no_corpus` from `current_only`
  - post-write durable-output wording
- [d:r:i] The uplift workflow and wrapper carriers now carry a broader discovery relation:
  - legacy
  - noncurrent
  - current-version shape-gap posture
  and a clearer split between deeper packet disclosure and durable write side effects.
- [d:r:i] The evidence layer should now point not only at the first implementation note and tests, but also at the reread inheritance plus the harden follow-through note and the widened tests.

## Current Consequence

- [d:r:i] The next adjacent route after this refresh is no longer another harden pass inside the same helper/workflow cluster.
- [d:r:i] The next adjacent route is the narrower operator-facing bridge the reread and follow-through now cleared:
  - specialist packet pointer disclosure through `progress` / `resume-project`
