Date: 2026-04-22
Status: landed bounded implementation note

# Harness Modifier First Overlay Filesystem Rehome Implementation

## Landed In This Slice

- [d:r:i] The first specialist overlay tranche now lands with authoritative source files under `harness_modifier/overlay/`:
  - `harness_modifier/overlay/get-shit-done/workflows/uplift-project.md`
  - `harness_modifier/overlay/get-shit-done/workflows/propagation-review.md`
  - `harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md`
  - `harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md`
  - `harness_modifier/overlay/skills/gsd-propagation-review/SKILL.md`
  - `harness_modifier/overlay/skills/gsd-seed-migration-inventory/SKILL.md`
- [d:r:i] The stable install targets remain declared in [../../../../tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](../../../../tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json), but those six entries now use explicit source-path indirection into `harness_modifier/overlay/`.
- [d:r:i] The overlay contract helper now treats source authority and install target as separate but typed surfaces:
  - [../../../../harness_modifier/contract/portable_gsd_contract.py](../../../../harness_modifier/contract/portable_gsd_contract.py)
- [d:r:i] The package now owns helper shims for the moved workflow shells:
  - `harness_modifier/overlay/helpers/project_uplift.py`
  - `harness_modifier/overlay/helpers/audit_refmap.py`
  - `harness_modifier/overlay/helpers/seed_migration_inventory.py`

## What Changed In The Authority Map

- [d:r:i] This slice does **not** change the live `.codex` install target paths.
- [d:r:i] It changes the authoritative source home for the first specialist tranche.
- [d:r:i] The new authority split is:
  - source authority: `harness_modifier/overlay/...`
  - install target authority: `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
  - materialization/validation authority: `harness_modifier/contract/portable_gsd_contract.py`
- [d:r:i] That split is cleaner for later standalone extraction because it stops requiring physical co-location between modifier-owned source files and the host repo's overlay install-target mirror.

## Text-Abstraction Follow-Through Landed Here

- [d:r:i] The moved workflow shells no longer carry the earlier host audit-workspace embeds as hard local links.
- [d:r:i] The moved workflow shells no longer point directly at `tooling/codex/*.py` as their authoritative helper home.
- [d:r:i] The route now uses package-owned shims or named host references where the first roster/scan slice had previously marked live blockers.

## Propagation And Test Follow-Through

- [d:r:i] Focused route-contract tests now resolve authoritative source paths through the overlay manifest instead of assuming the source file must physically live under `tooling/portable-gsd/overlay/`.
- [d:r:i] The uplift durable-memory surfaces, extraction state, and propagation registry are refreshed in the same boundary rather than leaving the source split ambient.
- [d:r:i] The old specialist source files under `tooling/portable-gsd/overlay/...` are now removed as source authorities rather than silently duplicated.

## Verification

- [d:r:i] focused route and contract tests over the touched specialist tranche
- [d:r:i] `./scripts/setup-portable-gsd.sh`
- [d:r:i] `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --strict`
- [d:r:i] `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --strict`
- [d:r:i] `python3 tooling/codex/audit_refmap.py verify .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`
- [d:r:i] `git diff --check`

## Exact Next Move

1. [d:r:i] Run one bounded reread over the landed specialist source split.
2. [d:r:i] Use that reread to decide whether the next extraction object is:
   - another generic overlay tranche
   - a narrower classification pass over overwrite-family carriers
   - or a hold boundary before any wider standalone-project movement
3. [d:r:i] Do not widen directly into standalone repo split, npm packaging, or second-host exercise from this implementation note alone.
