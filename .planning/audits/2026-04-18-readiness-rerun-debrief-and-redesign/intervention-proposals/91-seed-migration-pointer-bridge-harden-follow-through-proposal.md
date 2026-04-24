Date: 2026-04-22
Status: accepted bounded follow-through proposal

# Seed Migration Pointer Bridge Harden Follow-Through Proposal

## Purpose

- [g:r:i] Tighten the landed operator-facing seed-migration bridge inside its own footprint before any wider wrapper or rewrite family inherits next.

## Proposed Revisions

- [d:r:i] Preserve the inspect/write split at the consumer surface instead of collapsing operator disclosure into the write-form command.
- [d:r:i] Preserve migration-difficulty visibility by surfacing a compact breakdown beside the aggregated candidate count.
- [d:r:i] Bind the helper's disclosed commands back to the specialist wrapper contract with an explicit test.
- [d:r:i] Prove consumer-side gating at the workflow layer rather than relying only on helper-side tests.
- [d:r:i] Preserve the aggregated migration-candidate count in durable uplift memory.
- [d:r:i] Route the held-later breadcrumb through the fuller landed evidence trail instead of leaving it frozen at the first workflow landing.
- [d:r:i] Commit one representative `SEED-MIGRATION-MANIFEST.json` shape fixture and one end-to-end chain test so the bridge has a stronger exercised evidence floor.

## Non-Moves

- [d:r:i] Do not open rewrite or normalization automation for actual seed files in this slice.
- [d:r:i] Do not widen generic entry wrappers in this slice.
- [d:r:i] Do not broaden audit-open beyond the already-landed milestone-close seed route in this slice.

## Proof Surfaces

- [d:r:i] Helper: `tooling/codex/project_uplift.py`
- [d:r:i] Specialist packet: `tooling/codex/seed_migration_inventory.py`
- [d:r:i] Consumers:
  - `tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md`
  - `tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md`
- [d:r:i] Contract tests:
  - `tooling/codex/tests/test_project_uplift.py`
  - `tooling/codex/tests/test_seed_operator_consumer_follow_through_contract.py`
  - `tooling/codex/tests/test_seed_migration_inventory_follow_through_contract.py`
- [d:r:i] New exercised-evidence target:
  - `propagation-audit/artifacts/07-seed-migration-manifest-shape-fixture.json`

## Current Consequence

- [d:r:i] The next slice should widen evidence, operator control, and cross-surface binding inside the landed bridge rather than opening a fresh seed-family lane.
