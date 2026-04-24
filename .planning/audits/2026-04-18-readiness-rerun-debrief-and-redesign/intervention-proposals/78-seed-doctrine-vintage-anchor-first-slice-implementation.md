Date: 2026-04-21
Status: landed first slice

# Seed Doctrine Vintage Anchor First Slice Implementation

## Purpose

- [g:r:i] This note records the landed first slice opened in `77`.
- [g:r:i] The target stayed bounded: current seeds now write an explicit contract vintage anchor, and milestone-open now treats missing version markers as legacy-unversioned instead of leaving that compatibility question ambient.

## What Landed

- [e:r:i] The tracked overlay now carries the vintage anchor at the seed producer and seed consumer:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/plant-seed.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plant-seed.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md)
  - [tooling/portable-gsd/overlay/skills/gsd-plant-seed/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-plant-seed/SKILL.md)
- [e:r:i] `plant-seed` now writes `seed_contract_version: 2` into the live seed frontmatter shape.
- [e:r:i] `new-milestone` now names seed contract vintage as part of seed reread and selection context:
  - when present, read `seed_contract_version`
  - when absent, treat the seed as `legacy_unversioned`
  - do not reject older seeds only because the marker is missing
- [e:r:i] `gsd-plant-seed` now keeps that current version anchor explicit at the wrapper boundary too.

## Verification And Recovery Path

- [e:r:i] Focused contract proof still lives in [tooling/codex/tests/test_seed_consumer_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_consumer_follow_through_contract.py), now widened to cover:
  - explicit `seed_contract_version: 2` in `plant-seed`
  - explicit milestone-open reread of `seed_contract_version`
  - explicit legacy tolerance through `legacy_unversioned`
  - explicit current-version language in the wrapper
- [e:r:i] The slice became real overlay/materialization carry, not a live-only patch:
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`

## What This Slice Still Holds

- [d:r:i] This slice does not yet widen `audit.cjs`.
- [d:r:i] It does not yet scan older seed corpora during uplift.
- [d:r:i] It does not yet create a migration helper for legacy seeds.

## Current Consequence

- [d:r:i] The current seed family now distinguishes current-contract seeds from legacy-unversioned ones at the main producer and main milestone-open consumer.
- [d:r:i] The next narrower seed-family question is now cleaner:
  - broader consumer widening
  - uplift-side legacy seed scanning
  - later audit consumer widening
