Date: 2026-04-22
Status: landed

# Harness Modifier Compatibility Declaration Carrier Change-Triggered Refresh

## Trigger

- [d:r:i] The extraction family landed a new typed portability carrier under `harness_modifier/compatibility/` through [../intervention-proposals/141-harness-modifier-compatibility-declaration-carrier-implementation.md](../intervention-proposals/141-harness-modifier-compatibility-declaration-carrier-implementation.md).

## Propagation Consequence

- [d:r:i] Compatibility semantics are no longer only:
  - buried uplift constants
  - parity-classification rules inside one helper
- [d:r:i] They now also travel through a portable declaration carrier that later standalone extraction and later host installs can reuse unchanged.

## Refreshed Carriers

- [d:r:i] declaration authority:
  - [harness_modifier/compatibility/declaration.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/compatibility/declaration.json:1)
  - [harness_modifier/compatibility/declaration.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/compatibility/declaration.py:1)
- [d:r:i] host-boundary observation consumer:
  - [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:1)
- [d:r:i] materialization/parity consumer:
  - [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/portable_gsd_contract.py:1)
- [d:r:i] durable uplift memory:
  - [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:1)
  - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:1)
  - [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:1)

## Registry / Governance Follow-Through

- [d:r:i] The extraction family now treats the compatibility declaration carrier as the next landed step after the `harness_modifier/` helper rehome.
- [d:r:i] The propagation family should treat this declaration as a declared-contract carrier, not only as uplift memory or parity-example prose.

## Held Later

- [d:r:i] overlay/workflow/skill/template/reference rehome
- [d:r:i] second-host exercise
- [d:r:i] standalone repo split
