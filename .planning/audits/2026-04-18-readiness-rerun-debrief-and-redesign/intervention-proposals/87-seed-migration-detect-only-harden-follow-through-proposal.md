Date: 2026-04-22
Status: accepted bounded follow-through

# Seed Migration Detect-Only Harden Follow-Through Proposal

## Why This Slice Exists Now

- [d:c+i] The bounded Opus reread in [propagation-audit/outputs/04-seed-migration-detect-only-first-slice-reread-opus47-max-r1.md](../propagation-audit/outputs/04-seed-migration-detect-only-first-slice-reread-opus47-max-r1.md) widened the landed detect-only packet without reopening rewrite or generic wrapper sweep.
- [d:c+i] The reread named a compact revision set inside the current slice:
  - post-write state in the durable report/manifest
  - producer-follow-through between `plant-seed` and the helper's required-shape lists
  - route-state disambiguation
  - uplift handoff coverage for current-version shape gaps
  - narrower supporting-reading and wrapper guidance
  Sources: [../propagation-audit/outputs/04-seed-migration-detect-only-first-slice-reread-opus47-max-r1.md](../propagation-audit/outputs/04-seed-migration-detect-only-first-slice-reread-opus47-max-r1.md:151), [../propagation-audit/dispositions/04-seed-migration-detect-only-first-slice-reread-inheritance.md](../propagation-audit/dispositions/04-seed-migration-detect-only-first-slice-reread-inheritance.md:19).

## Proposed Revisions

- [d:r:i] Add post-write state handling to `seed_migration_inventory.py` so the durable report/manifest describe the written state instead of preserving pre-write recommendation text.
- [d:r:i] Centralize required seed-shape constants in `project_uplift.py`, reuse them from `seed_migration_inventory.py`, and add a contract test that ties those constants back to the tracked `plant-seed` producer template.
- [d:r:i] Split migration helper `route_state` so `no_corpus` and `current_only` stop collapsing into one quiet state.
- [d:r:i] Teach uplift-side seed attention to include current-version shape gaps, not only legacy or noncurrent vintage.
- [d:r:i] Narrow the detect-only workflow's supporting-reading packet toward flagged migration candidates rather than the whole corpus.
- [d:r:i] Separate "deeper detect-only packet" from "durable write" in the skill/wrapper guidance so disclosure and write side effects stop being one bundled operator choice.

## Intentional Non-Moves

- [d:r:i] This slice does not open rewrite or normalization automation.
- [d:r:i] It does not widen `progress` or `resume-project` yet.
- [d:r:i] It does not widen `audit.cjs`, `verify-work`, canary, runtime-visibility, or manifest-coherence helpers into seed-aware migration consumers.
- [d:r:i] It does not yet change the held-later pointer shape beyond the existing `partially landed` pointer.

## Current Consequence

- [d:r:i] If this follow-through lands cleanly, the next adjacent move should be the narrower operator-facing bridge the reread identified:
  - `progress` / `resume-project` pointer disclosure for the specialist packet
  - no execution widening
  - no rewrite widening
