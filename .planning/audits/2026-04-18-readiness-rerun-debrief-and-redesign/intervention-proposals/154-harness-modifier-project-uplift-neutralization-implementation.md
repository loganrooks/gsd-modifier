Date: 2026-04-22
Status: active implementation note

# Harness Modifier Project Uplift Neutralization Implementation

## What Landed

- [d:r:i] The lane-05 reread is now inherited through:
  - [../extraction-audit/launch-truth/05-harness-modifier-project-uplift-neutralization-proposal-reread-launch-truth.md](../extraction-audit/launch-truth/05-harness-modifier-project-uplift-neutralization-proposal-reread-launch-truth.md)
  - [../extraction-audit/outputs/05-harness-modifier-project-uplift-neutralization-proposal-reread-opus47-max-r1.md](../extraction-audit/outputs/05-harness-modifier-project-uplift-neutralization-proposal-reread-opus47-max-r1.md)
  - [../extraction-audit/dispositions/05-harness-modifier-project-uplift-neutralization-proposal-reread-inheritance.md](../extraction-audit/dispositions/05-harness-modifier-project-uplift-neutralization-proposal-reread-inheritance.md)
- [d:r:i] The three typed carriers the lane asked for now live at:
  - [../../../harness_modifier/compatibility/observation.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/compatibility/observation.json)
  - [../../../harness_modifier/compatibility/seed_contract.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/compatibility/seed_contract.json)
  - [../../../harness_modifier/uplift/output_policy.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/output_policy.json)

## Carried Result

- [d:r:i] `project_uplift.py` no longer owns its runtime-discovery directory set as helper-local doctrine; runtime observation now routes through the typed observation carrier and its loader.
- [d:r:i] `project_uplift.py` no longer owns uplift output topology as helper-local doctrine; state heading plus report/manifest/held-later paths now route through the typed uplift output-policy carrier.
- [d:r:i] `project_uplift.py` no longer owns seed contract shape as helper-local doctrine; seed root, current version, required frontmatter keys, and required section headings now route through the typed seed-contract carrier.
- [d:r:i] `seed_migration_inventory.py` now reads the same seed-contract carrier directly instead of depending on `project_uplift.py` constants for seed-shape policy.
- [d:r:i] `harness_canary.py` now reads the same uplift output-policy carrier instead of depending on `project_uplift.py` manifest-path constants.
- [d:r:i] The representative seed-migration manifest fixture now carries `seed_dir_rel_path` explicitly, because the seed-root path is now part of the declared seed-contract surface rather than ambient helper memory.

## Extraction Meaning

- [d:r:i] The modifier-facing payload candidate is now thinner in the exact way lane-05 asked for:
  - runtime discovery posture is typed separately
  - uplift output/path posture is typed separately
  - seed contract shape is typed separately
  - compatibility routing remains declaration-driven rather than re-declared as helper constants
- [d:r:i] This does not yet relocate `project_uplift.py`.
- [d:r:i] This does not yet relocate `seed_migration_inventory.py`.
- [d:r:i] This does not yet reopen `audit_refmap.py`.

## Governance Carry

- [d:r:i] [../../../harness_modifier/overlay/helpers/AUTHORITY-MAP.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/helpers/AUTHORITY-MAP.md) now treats the neutralization preconditions as discharged rather than still pending.
- [d:r:i] [../../../harness_modifier/overlay/ROSTER.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/ROSTER.md) now treats `project_uplift.py` neutralization as landed and narrows the next blocker to post-neutralization payload-home judgment instead of carrier extraction.
- [d:r:i] The matching propagation refresh now lands through [../propagation-audit/57-harness-modifier-project-uplift-neutralization-change-triggered-refresh.md](../propagation-audit/57-harness-modifier-project-uplift-neutralization-change-triggered-refresh.md).

## Exact Next Move

- [d:r:i] Judge `project_uplift.py` again on top of the neutralized carrier split before any later payload relocation is reopened.
- [d:r:i] Keep second overlay tranche movement, overwrite-family source-indirection movement, and standalone repo/package widening explicitly later than that judgment.
