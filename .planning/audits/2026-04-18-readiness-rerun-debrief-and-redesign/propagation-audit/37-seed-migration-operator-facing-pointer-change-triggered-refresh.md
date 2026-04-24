Date: 2026-04-22
Status: landed change-triggered refresh

# Seed Migration Operator-Facing Pointer Change-Triggered Refresh

## Why This Refresh Exists

- [d:c+i] The landed harden slice in [intervention-proposals/88-seed-migration-detect-only-harden-follow-through-implementation.md](../intervention-proposals/88-seed-migration-detect-only-harden-follow-through-implementation.md) explicitly cleared the next adjacent move: bounded specialist-packet disclosure through `progress` / `resume-project`.
- [d:c+i] That bridge is now landed in [intervention-proposals/90-seed-migration-operator-facing-pointer-bridge-implementation.md](../intervention-proposals/90-seed-migration-operator-facing-pointer-bridge-implementation.md).

## What Moves In The Typed Registry

- [d:r:i] The `project_uplift.py -> progress/resume-project` bridge now carries more than seed posture visibility.
- [d:r:i] That bridge now also carries:
  - specialist packet candidate counts
  - specialist command disclosure
  - bounded pointer surfacing only when migration candidates are present
- [d:r:i] The workflow consumers now imply a narrower operator contract:
  - keep the packet easy to find
  - keep it detect-only
  - do not blur packet disclosure into rewrite pressure or a generic wrapper sweep

## Current Consequence

- [d:r:i] The next adjacent route after this refresh is no longer “surface the packet at ordinary operator touchpoints.”
- [d:r:i] The next adjacent route is a bounded reread of the landed bridge before any later entry-wrapper widening, broader audit-open consumer widening, or rewrite/normalization family inherits next.
