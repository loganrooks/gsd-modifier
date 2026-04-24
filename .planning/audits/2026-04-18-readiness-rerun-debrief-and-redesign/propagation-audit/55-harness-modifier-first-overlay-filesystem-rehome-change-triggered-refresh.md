Date: 2026-04-22
Status: active change-triggered refresh

# Harness Modifier First Overlay Filesystem Rehome Change-Triggered Refresh

## Trigger

- [e:c+i] The first specialist overlay source split is now landed through [../intervention-proposals/148-harness-modifier-first-overlay-filesystem-rehome-implementation.md](../intervention-proposals/148-harness-modifier-first-overlay-filesystem-rehome-implementation.md).

## Carriers Refreshed

- [d:r:i] updated source-authority roster carrier:
  - `harness_modifier/overlay/ROSTER.md`
- [d:r:i] updated install-target contract carrier:
  - `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- [d:r:i] updated contract/materialization carrier:
  - `harness_modifier/contract/portable_gsd_contract.py`
- [d:r:i] new modifier-owned workflow and wrapper sources:
  - `harness_modifier/overlay/get-shit-done/workflows/uplift-project.md`
  - `harness_modifier/overlay/get-shit-done/workflows/propagation-review.md`
  - `harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md`
  - `harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md`
  - `harness_modifier/overlay/skills/gsd-propagation-review/SKILL.md`
  - `harness_modifier/overlay/skills/gsd-seed-migration-inventory/SKILL.md`
- [d:r:i] new package-owned helper shim carriers:
  - `harness_modifier/overlay/helpers/project_uplift.py`
  - `harness_modifier/overlay/helpers/audit_refmap.py`
  - `harness_modifier/overlay/helpers/seed_migration_inventory.py`

## Propagation Meaning

- [d:r:i] The first specialist overlay tranche no longer depends on physical co-location between source authority and install target.
- [d:r:i] The overlay manifest now carries explicit source-path indirection, so the install frontier and the source-authority frontier are separate but typed together.
- [d:r:i] The specialist workflow shells and skill wrappers now travel under `harness_modifier/overlay/` while the host repo keeps a stable installer/materialization boundary.
- [d:r:i] The propagation family now has to keep both surfaces explicit:
  - what installs into `.codex`
  - where the authoritative modifier-owned source lives before installation

## Held Later

- [d:r:i] no second overlay tranche in this refresh note itself
- [d:r:i] no overwrite-family workflow/template/reference migration here
- [d:r:i] no compact-prompt split here
- [d:r:i] no runtime/agent/config tranche here
- [d:r:i] no standalone repo split or package/distribution route here
