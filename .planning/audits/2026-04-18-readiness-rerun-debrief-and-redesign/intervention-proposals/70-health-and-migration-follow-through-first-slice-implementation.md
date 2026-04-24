Date: 2026-04-21
Status: landed first slice

# Health And Migration Follow-Through First Slice Implementation

## Purpose

- [g:r:i] This note records the landed first slice opened in `69`.
- [g:r:i] The target stayed bounded: repair and migration surfaces now carry stronger follow-through without widening yet into runtime update or full wrapper-family retrofit.

## What Landed

- [e:r:i] The tracked overlay now owns the current repair and migration carriers:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/health.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/health.md)
  - [tooling/portable-gsd/overlay/skills/gsd-health/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-health/SKILL.md)
  - [tooling/portable-gsd/overlay/skills/gsd-from-gsd2/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-from-gsd2/SKILL.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] `health` now inherits the shared mandatory-read doctrine explicitly:
  - `required_reading`
  - `supporting_reading`
  - `deeper_reading`
- [e:r:i] The route split is now stated where repair and migration pressure actually lives:
  - `health` now keeps structural repair distinct from later repo-local runtime, governing-doc, or doctrine uplift
  - missing planning state still routes to `new-project` or `ingest-docs` rather than to uplift
  - `from-gsd2` now runs structural health validation after migration and keeps later uplift separate instead of flattening the whole entry job into format conversion

## Verification And Recovery Path

- [e:r:i] Focused contract proof now exists in [tooling/codex/tests/test_health_and_migration_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_health_and_migration_follow_through_contract.py), covering:
  - overlay ownership for `health.md`, `gsd-health`, and `gsd-from-gsd2`
  - layered packet doctrine plus explicit uplift-route separation in `health.md`
  - explicit structural-health plus later-uplift follow-through in the two skill wrappers
- [e:r:i] The slice became real overlay/materialization carry, not a live-only patch:
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`

## What This Slice Still Holds

- [d:r:i] This slice does not yet widen into `update`.
- [d:r:i] It does not yet auto-launch uplift from `health` or `from-gsd2`.
- [d:r:i] It does not yet widen across every remaining repair, migration, or entry wrapper.

## Current Consequence

- [d:r:i] The harness now carries stronger follow-through across repair and migration entry surfaces instead of letting those routes stop at structural repair or format conversion alone.
- [d:r:i] The next narrower question is which adjacent onboarding family should inherit after this:
  - `update`
  - seed-consumer carry
  - or a later wider entry-wrapper retrofit
