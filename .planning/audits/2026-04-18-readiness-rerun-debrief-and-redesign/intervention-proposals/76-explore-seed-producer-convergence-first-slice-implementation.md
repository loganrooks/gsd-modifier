Date: 2026-04-21
Status: landed first slice

# Explore Seed Producer Convergence First Slice Implementation

## Purpose

- [g:r:i] This note records the landed first slice opened in `75`.
- [g:r:i] The target stayed bounded: the stale `explore` seed producer route is now converged onto the live `plant-seed` contract without widening into seed doctrine-vintage or broader consumer expansion.

## What Landed

- [e:r:i] The tracked overlay now owns the current `explore` producer pair:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/explore.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/explore.md)
  - [tooling/portable-gsd/overlay/skills/gsd-explore/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-explore/SKILL.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] `explore` now routes selected seed outputs through the current seed contract instead of minting an older inline seed file shape:
  - `$gsd-plant-seed`
  - `SEED-NNN-slug`
  - `trigger_when`
  - `Why This Matters`
  - `Strengthening Carry`
- [e:r:i] `gsd-explore` now keeps that same route explicit at the wrapper boundary instead of leaving the workflow to imply one current path while the wrapper silently tolerates legacy inline seed minting.

## Verification And Recovery Path

- [e:r:i] Focused contract proof now exists in [tooling/codex/tests/test_explore_seed_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_explore_seed_follow_through_contract.py), covering:
  - overlay ownership for `explore.md` and `gsd-explore`
  - explicit `$gsd-plant-seed` routing plus current seed-shape vocabulary in `explore.md`
  - absence of `trigger_condition`, `planted_date`, and `.planning/seeds/{slug}.md`
  - explicit current seed-route language in the wrapper
- [e:r:i] The slice became real overlay/materialization carry, not a live-only patch:
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`

## What This Slice Still Holds

- [d:r:i] This slice does not yet create seed doctrine-vintage markers or compatibility handling for older seed corpora.
- [d:r:i] It does not yet widen the consumer field beyond the current `plant-seed -> new-milestone` bridge.
- [d:r:i] It does not widen seed interpretation inside `audit.cjs`.

## Current Consequence

- [d:r:i] The harness no longer carries one current seed contract beside one stale `explore` producer description.
- [d:r:i] The next narrower seed-family question is now cleaner:
  - doctrine-vintage
  - broader consumers
  - later audit consumer widening
