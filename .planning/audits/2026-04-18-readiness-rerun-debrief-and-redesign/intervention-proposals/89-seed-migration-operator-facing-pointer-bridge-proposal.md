Date: 2026-04-22
Status: accepted bounded follow-through

# Seed Migration Operator-Facing Pointer Bridge Proposal

## Why This Slice Exists Now

- [d:c+i] The landed detect-only seed-migration packet now carries sharper route-state, post-write durable-output wording, producer-follow-through, and uplift-side current-version shape-gap discovery through [87-seed-migration-detect-only-harden-follow-through-proposal.md](87-seed-migration-detect-only-harden-follow-through-proposal.md) and [88-seed-migration-detect-only-harden-follow-through-implementation.md](88-seed-migration-detect-only-harden-follow-through-implementation.md).
- [d:c+i] The next adjacent move cleared by that harden slice was narrower than wrapper widening or rewrite logic:
  - keep the specialist packet specialist-owned
  - disclose it to ordinary operators when seed-migration candidates are present
  - do not blur detect-only disclosure into auto-write pressure
  Sources: [88-seed-migration-detect-only-harden-follow-through-implementation.md](88-seed-migration-detect-only-harden-follow-through-implementation.md:31), [../propagation-audit/36-seed-migration-detect-only-harden-change-triggered-refresh.md](../propagation-audit/36-seed-migration-detect-only-harden-change-triggered-refresh.md:32).

## Proposed Revisions

- [d:r:i] Extend `project_uplift.py` progress-note output with specialist-packet disclosure fields:
  - `show_seed_migration_pointer`
  - `seed_migration_candidate_count`
  - `seed_migration_pointer`
- [d:r:i] Treat migration candidates as the bounded union of:
  - legacy-unversioned seeds
  - noncurrent-version seeds
  - current-version shape-gap seeds
- [d:r:i] Teach `progress.md` and `resume-project.md` to surface the packet pointer only when the helper says it should surface.
- [d:r:i] Keep the surfaced pointer narrow and specialist-owned:
  - command disclosure only
  - no generic rewrite wording
  - no auto-write implication

## Intentional Non-Moves

- [d:r:i] This slice does not widen the seed-migration route into `verify-work`, `audit.cjs`, milestone-close, or other adjacent consumers.
- [d:r:i] It does not add a generic wrapper sweep across unrelated entry surfaces.
- [d:r:i] It does not reopen rewrite or normalization automation.
- [d:r:i] It does not collapse the specialist packet into ordinary uplift recommendation text.

## Current Consequence

- [d:r:i] If this bridge lands cleanly, ordinary re-entry surfaces will disclose the specialist packet when the repo actually carries migration candidates, while the detect-only route stays specialist-owned and bounded.
- [d:r:i] The next adjacent move after that bridge should be a bounded reread of the landed bridge before any later entry-wrapper widening or broader seed-consumer expansion inherits next.
