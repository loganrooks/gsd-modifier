Date: 2026-04-21
Status: landed first slice

# Seed Consumer Carry First Slice Implementation

## Purpose

- [g:r:i] This note records the landed first slice opened in `73`.
- [g:r:i] The target stayed bounded: seed producer/consumer carry is now sharper without widening into seed doctrine-vintage machinery or broader resurfacing routes.

## What Landed

- [e:r:i] The tracked overlay now carries the stronger seed producer/wrapper pair:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/plant-seed.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plant-seed.md)
  - [tooling/portable-gsd/overlay/skills/gsd-plant-seed/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-plant-seed/SKILL.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] `plant-seed` now keeps strengthening meaning in a dedicated `Strengthening Carry` section rather than only as ambient note text.
- [e:r:i] `new-milestone` now treats matching seeds as richer consumer input:
  - it extracts `Why This Matters`
  - it extracts `Strengthening Carry` when present
  - it keeps selected seeds as stronger requirement-shaping context rather than only as idea/trigger rows

## Verification And Recovery Path

- [e:r:i] Focused contract proof now exists in [tooling/codex/tests/test_seed_consumer_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_consumer_follow_through_contract.py), covering:
  - overlay ownership for `plant-seed.md` and `gsd-plant-seed`
  - explicit strengthening-carry section in the seed producer
  - explicit `Why This Matters` and `Strengthening Carry` consumer carry in `new-milestone`
- [e:r:i] The slice became real overlay/materialization carry, not a live-only patch:
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`

## What This Slice Still Holds

- [d:r:i] This slice does not yet add a full doctrine-vintage system for seeds.
- [d:r:i] It does not yet widen seed resurfacing beyond milestone opening.
- [d:r:i] It does not redesign broader deferred-item or backlog families.

## Current Consequence

- [d:r:i] The harness now carries stronger seed producer/consumer meaning rather than only seed existence and trigger timing.
- [d:r:i] The next narrower question becomes which family should inherit next:
  - seed doctrine-vintage
  - broader seed consumers beyond milestone opening
  - or a later wider entry-wrapper retrofit

