Date: 2026-04-22
Status: landed bounded follow-through

# Seed Migration Detect-Only Harden Follow-Through Implementation

## Landed Revisions

- [e:r:i] `seed_migration_inventory.py` now distinguishes:
  - `no_corpus`
  - `current_only`
  - `surfaced`
  instead of collapsing all quiet states into `dormant`.
- [e:r:i] The helper now records `migration_move_kinds` beside prose `migration_moves`, raising later rewrite-family legibility without folding rewrite into the current slice.
- [e:r:i] The helper now writes a post-write recommendation into the durable report/manifest, so the specialist packet no longer tells a future reader to perform the write that already happened.
- [e:r:i] `project_uplift.py` now carries shared required seed-shape constants plus current-version shape-gap detection inside `seed_corpus_posture`.
- [e:r:i] Uplift-side attention now includes current-version shape gaps instead of treating only legacy or noncurrent vintage as seed posture worth surfacing.
- [e:r:i] The detect-only workflow now narrows supporting reading toward flagged migration candidates.
- [e:r:i] The seed-migration and uplift skill/wrapper text now separates:
  - deeper detect-only packet disclosure
  - durable `--write` side effects

## Proof Surfaces

- [d:r:i] Helper and helper-follow-through proof:
  - [tooling/codex/tests/test_seed_migration_inventory.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_migration_inventory.py)
  - [tooling/codex/tests/test_seed_migration_inventory_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_migration_inventory_follow_through_contract.py)
- [d:r:i] Uplift-side shape-gap proof:
  - [tooling/codex/tests/test_project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_project_uplift.py)
- [d:r:i] Live surfaces:
  - [seed_migration_inventory.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/seed_migration_inventory.py)
  - [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)
  - [seed-migration-inventory.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md)
  - [gsd-seed-migration-inventory/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-seed-migration-inventory/SKILL.md)
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
  - [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)

## Verification

- [d:r:i] Focused tests now prove:
  - helper route-state split
  - post-write durable-report behavior
  - producer-follow-through against the tracked `plant-seed` template
  - uplift-side shape-gap attention
- [d:r:i] The overlay is rematerialized after the workflow/wrapper text changes so live `.codex` carry stays in tune with the tracked overlay contract.
- [d:r:i] Durable uplift memory is refreshed after the helper and uplift-route changes so the current repo remembers the new seed-shape posture fields explicitly.

## Current Consequence

- [d:r:i] The detect-only packet now carries clearer state semantics, tighter producer-follow-through, cleaner durable-memory wording, and a wider uplift-side discovery route for shape gaps.
- [d:r:i] The next adjacent move is now cleaner than it was before this batch:
  - operator-facing pointer disclosure for the specialist packet through `progress` / `resume-project`
  - no rewrite widening
  - no generic wrapper sweep
