Date: 2026-04-22
Status: landed change-triggered slice refresh

# Seed Migration Pointer Bridge Harden Change-Triggered Refresh

## Trigger

- [g:r:i] The landed operator-facing bridge was sharpened inside its own footprint after the bounded Opus reread in lane `05`.

## What Moved

- [e:r:i] `project_uplift.py` now carries:
  - split inspect/write specialist commands
  - compact migration-breakdown disclosure
  - denormalized migration-candidate count plus breakdown inside durable uplift memory
- [e:r:i] `progress.md` and `resume-project.md` now carry the stronger disclosure block:
  - candidate count
  - breakdown
  - inspect command
  - write command
- [e:r:i] Consumer contract tests now prove:
  - conditional gating stays in place
  - disclosed commands stay bound to the specialist wrapper
- [e:r:i] The propagation family now carries one committed shape fixture and one end-to-end bridge-chain test rather than leaving the non-trivial branch entirely synthetic-and-implicit.

## Typed `v2` Consequence

- [d:r:i] The `project_uplift -> progress/resume-project -> seed_migration_inventory` route should now be read as:
  - operator-facing seed posture visibility
  - bounded migration-candidate disclosure
  - inspect/write command split
  - fixture-backed chain proof
- [d:r:i] The seed-migration family now carries a stronger evidence floor without opening rewrite or generic wrapper widening.

## Current Consequence

- [d:r:i] The next adjacent move is one more bounded reread of the hardened bridge before later wider seed-family inheritance opens.
