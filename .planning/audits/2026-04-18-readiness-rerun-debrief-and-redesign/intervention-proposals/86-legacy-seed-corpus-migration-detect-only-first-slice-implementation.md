Date: 2026-04-22
Status: landed first slice

# Legacy Seed Corpus Migration Detect-Only First Slice Implementation

## Landed Surfaces

- [d:r:i] Specialist detect-only helper:
  - [tooling/codex/seed_migration_inventory.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/seed_migration_inventory.py)
- [d:r:i] Focused helper proof:
  - [tooling/codex/tests/test_seed_migration_inventory.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_migration_inventory.py)
- [d:r:i] Specialist workflow and wrapper:
  - [seed-migration-inventory.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md)
  - [gsd-seed-migration-inventory/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-seed-migration-inventory/SKILL.md)
- [d:r:i] Uplift-route handoff and focused contract proof:
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
  - [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)
  - [tooling/codex/tests/test_seed_migration_inventory_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_migration_inventory_follow_through_contract.py)

## What Changed

- [e:r:i] The new helper now inventories seed corpora by:
  - contract vintage
  - missing current-contract frontmatter keys
  - missing current-contract sections
  - bounded migration moves
- [e:r:i] The helper can now write:
  - `.planning/SEED-MIGRATION-REPORT.md`
  - `.planning/SEED-MIGRATION-MANIFEST.json`
  when the operator wants durable migration-planning memory.
- [e:r:i] The uplift route now points at the specialist packet when legacy or noncurrent seed posture surfaces, so uplift can keep posture visible without pretending counts/examples are the whole migration story.
- [e:r:i] The held-later register now records legacy seed corpus migration as partially landed through the specialist detect-only route instead of keeping the whole family as an undifferentiated hold.

## Intentional Non-Moves

- [d:r:i] This slice does not rewrite seed files.
- [d:r:i] It does not widen `progress` or `resume-project`.
- [d:r:i] It does not widen `audit.cjs` again.
- [d:r:i] It does not treat `STATE.md` `Future Carry Forward -> Seeded` lines as the same carrier as `.planning/seeds/SEED-*.md`.
- [d:r:i] It does not widen canary, runtime-visibility, or manifest-coherence helpers into seed-aware checks.

## Verification

- [d:r:i] Focused helper coverage now proves:
  - mixed vintage corpora
  - current-version shape gaps
  - durable report/manifest writes
- [d:r:i] Focused contract coverage now proves:
  - overlay ownership for the new workflow and wrapper
  - uplift-route handoff into the specialist inventory packet
  - rewrite staying separate from detect-only
- [d:r:i] The overlay is re-materialized after the workflow and wrapper land so live `.codex` carry stays in tune with tracked overlay ownership.

## Current Consequence

- [d:r:i] The seed family now has a specialist detect-only migration packet instead of stopping at posture visibility alone.
- [d:r:i] The next adjacent seed-family questions are cleaner:
  - later rewrite or normalization family
  - later broader audit-open consumer widening
  - later wider entry-wrapper retrofit
