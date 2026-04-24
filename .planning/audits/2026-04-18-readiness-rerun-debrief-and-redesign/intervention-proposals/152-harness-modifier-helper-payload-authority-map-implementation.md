Date: 2026-04-22
Status: active implementation note

# Harness Modifier Helper Payload Authority Map Implementation

## What Landed

- [d:r:i] The lane-04 reread is now inherited through:
  - [../extraction-audit/launch-truth/04-harness-modifier-helper-payload-authority-map-reread-launch-truth.md](../extraction-audit/launch-truth/04-harness-modifier-helper-payload-authority-map-reread-launch-truth.md)
  - [../extraction-audit/outputs/04-harness-modifier-helper-payload-authority-map-reread-opus47-max-r1.md](../extraction-audit/outputs/04-harness-modifier-helper-payload-authority-map-reread-opus47-max-r1.md)
  - [../extraction-audit/dispositions/04-harness-modifier-helper-payload-authority-map-reread-inheritance.md](../extraction-audit/dispositions/04-harness-modifier-helper-payload-authority-map-reread-inheritance.md)
- [d:r:i] The bounded helper authority-map artifact now lives at:
  - [../../../harness_modifier/overlay/helpers/AUTHORITY-MAP.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/helpers/AUTHORITY-MAP.md)

## Carried Result

- [d:r:i] `project_uplift.py` is now explicitly treated as the modifier-facing payload candidate, but only after a neutralization slice.
- [d:r:i] `seed_migration_inventory.py` is now explicitly downstream of `project_uplift.py` and cannot lead payload movement.
- [d:r:i] `audit_refmap.py` is now explicitly out of the later payload-movement candidate set and into a sharper repo-local audit-tooling family.
- [d:r:i] The helper-shim layer is now explicitly mixed:
  - temporary bridge for `project_uplift.py`
  - derivative bridge for `seed_migration_inventory.py`
  - stable long-lived source/install boundary for `audit_refmap.py`

## Governance Carry

- [d:r:i] `harness_modifier/overlay/ROSTER.md` now carries the per-helper split rather than leaving helper authority as one blocker row.
- [d:r:i] `.planning/HARNESS-IMPROVEMENT-REGISTER.md` now carries the same split so the next extraction move stays visible outside this subtree.
- [d:r:i] No propagation refresh lands in this slice because no live install/materialization contract moved; the change is extraction/governance authority clarification, not a current runtime contract change.

## Exact Next Move

- [d:r:i] Open a bounded `project_uplift.py` neutralization proposal.
- [d:r:i] Do not combine that neutralization with payload relocation, second overlay tranche movement, overwrite-family source split, or standalone-project widening.
