Date: 2026-04-22
Status: active change-triggered refresh

# Harness Modifier Project Uplift Neutralization Change-Triggered Refresh

## Trigger

- [e:c+i] The neutralization slice is now landed through [../intervention-proposals/154-harness-modifier-project-uplift-neutralization-implementation.md](../intervention-proposals/154-harness-modifier-project-uplift-neutralization-implementation.md).

## Carriers Refreshed

- [d:r:i] new typed observation carrier:
  - `harness_modifier/compatibility/observation.json`
  - `harness_modifier/compatibility/observation.py`
- [d:r:i] new typed seed-contract carrier:
  - `harness_modifier/compatibility/seed_contract.json`
  - `harness_modifier/compatibility/seed_contract.py`
- [d:r:i] new typed uplift output-policy carrier:
  - `harness_modifier/uplift/output_policy.json`
  - `harness_modifier/uplift/output_policy.py`
- [d:r:i] thinned helper and downstream consumers:
  - `tooling/codex/project_uplift.py`
  - `tooling/codex/seed_migration_inventory.py`
  - `harness_modifier/contract/harness_canary.py`
- [d:r:i] refreshed shape anchor:
  - `propagation-audit/artifacts/07-seed-migration-manifest-shape-fixture.json`

## Propagation Meaning

- [d:r:i] Runtime discovery posture, uplift output topology, and seed-contract shape no longer travel as one helper-local policy blob inside `project_uplift.py`.
- [d:r:i] The modifier layer now has three named policy carriers that can travel, be reread, and later be judged independently of helper relocation appetite.
- [d:r:i] `seed_migration_inventory.py` now consumes the same seed-contract declaration that uplift-side posture scanning uses, so producer and specialist packet no longer mirror seed-shape doctrine through helper-local constants.
- [d:r:i] `harness_canary.py` now consumes the same uplift output-policy declaration that uplift writes use, so canary checks and uplift output topology no longer drift apart through duplicated constants.

## Held Later

- [d:r:i] no later payload relocation judgment inside this refresh itself
- [d:r:i] no second overlay tranche here
- [d:r:i] no overwrite-family source-indirection widening here
- [d:r:i] no standalone repo or npm package split here
