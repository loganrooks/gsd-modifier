Date: 2026-04-22
Status: landed bounded follow-through

# Seed Migration Pointer Bridge Harden Follow-Through Implementation

## Landed Revisions

- [e:r:i] `project_uplift.py` now preserves the specialist inspect/write split at the operator-facing bridge:
  - `seed_migration_inspect_pointer`
  - `seed_migration_write_pointer`
- [e:r:i] The bridge now carries a compact migration-breakdown disclosure beside the aggregated candidate count:
  - `seed_migration_candidate_breakdown`
- [e:r:i] Durable uplift memory now preserves:
  - `migration_candidate_count`
  - `migration_candidate_breakdown`
  inside `seed_corpus_posture`
- [e:r:i] The held-later breadcrumb for `legacy seed corpus migration` now points at the fuller landed evidence path instead of stopping at the first workflow landing.
- [e:r:i] A committed representative specialist-packet shape fixture now exists at [../propagation-audit/artifacts/07-seed-migration-manifest-shape-fixture.json](../propagation-audit/artifacts/07-seed-migration-manifest-shape-fixture.json).
- [e:r:i] A focused end-to-end chain test now proves:
  - synthetic mixed-corpus packet shape matches the committed fixture
  - `project_uplift` emits the expected candidate count, breakdown, and split commands
  - the two consumer workflows carry the exact disclosure block that renders those values

## Proof Surfaces

- [d:r:i] Helper and durable-memory carrier:
  - [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)
- [d:r:i] Specialist packet:
  - [seed_migration_inventory.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/seed_migration_inventory.py)
- [d:r:i] Consumers:
  - [progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md)
  - [resume-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md)
- [d:r:i] Contract and end-to-end tests:
  - [test_project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_project_uplift.py)
  - [test_seed_operator_consumer_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_operator_consumer_follow_through_contract.py)
  - [test_seed_migration_inventory_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_migration_inventory_follow_through_contract.py)
  - [test_seed_migration_pointer_bridge_e2e.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_migration_pointer_bridge_e2e.py)

## Verification

- [d:r:i] Focused tests now prove:
  - helper quiet state still keeps bridge disclosure absent
  - legacy-only and current-shape-gap postures still surface the bridge
  - consumer workflows keep the disclosure block under the correct gate
  - specialist wrapper text stays aligned with the helper's disclosed commands
  - the synthetic mixed-corpus packet shape stays frozen and rereadable
- [d:r:i] This slice stays inside the current bridge footprint:
  - no rewrite automation
  - no generic wrapper sweep
  - no broader audit-open widening

## Current Consequence

- [d:r:i] The bridge now gives operators finer control over when to read deeper and when to write durable packet memory.
- [d:r:i] The next adjacent move is a bounded reread of this hardened bridge before any later wider seed-family inheritance opens.
