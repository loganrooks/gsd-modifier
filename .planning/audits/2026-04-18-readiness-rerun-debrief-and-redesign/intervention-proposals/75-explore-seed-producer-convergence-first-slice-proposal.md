Date: 2026-04-21
Status: accepted bounded proposal

# Explore Seed Producer Convergence First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next adjacent lifecycle-carry slice after the landed `73/74` seed producer/consumer bridge.
- [g:r:i] The target is not broader seed doctrine-vintage yet. The target is the remaining stale producer path:
  - `explore`
  - `gsd-explore`
  - current `plant-seed` contract

## Why This Slice Is Real

- [e:c+i] The current repo has no live seed corpus to classify by vintage, so the clearest live drift is not stored seed metadata. It is the still-stale `explore` producer description. Source: [../propagation-audit/outputs/04-seed-vintage-and-consumer-field-sidecar-gpt54-xhigh-r1.md](../propagation-audit/outputs/04-seed-vintage-and-consumer-field-sidecar-gpt54-xhigh-r1.md:6).
- [e:c+i] The live upstream `explore` workflow still describes legacy seed output shape with `.planning/seeds/{slug}.md`, `trigger_condition`, and `planted_date`. Source: [../propagation-audit/outputs/04-seed-vintage-and-consumer-field-sidecar-gpt54-xhigh-r1.md](../propagation-audit/outputs/04-seed-vintage-and-consumer-field-sidecar-gpt54-xhigh-r1.md:8).
- [e:r:i] If that stale producer path stays live, later doctrine-vintage or broader consumer widening would still sit beside a route that can mint mixed seed shapes again.

## Bounded First Slice

- [d:r:i] Keep the slice narrow: one stale producer workflow, one wrapper, one current seed contract.
- [d:r:i] Overlay-own `get-shit-done/workflows/explore.md`.
- [d:r:i] Overlay-own `skills/gsd-explore/SKILL.md`.
- [d:r:i] Make the current route explicit where `explore` proposes seed outputs:
  - use `$gsd-plant-seed`
  - point at the live `SEED-NNN-slug` artifact shape
  - name `trigger_when`
  - name `Why This Matters`
  - name `Strengthening Carry`
- [d:r:i] Explicitly forbid legacy inline seed minting from `explore`.

## Held Later

- [d:r:i] This slice does not yet create a broader seed doctrine-vintage system.
- [d:r:i] It does not yet widen `audit.cjs` or other later seed consumers.
- [d:r:i] It does not widen into a broader entry-wrapper retrofit beyond `gsd-explore`.

## Verification Gates

- [d:r:i] Add a focused contract test that checks:
  - overlay ownership for `explore.md` and `skills/gsd-explore/SKILL.md`
  - explicit `$gsd-plant-seed` routing in the workflow
  - explicit current seed-shape vocabulary in the workflow
  - absence of the stale legacy seed strings
  - explicit current seed-route language in the wrapper
- [d:r:i] Re-materialize the overlay so the live `.codex` frontier carries the same producer convergence.
- [d:r:i] Refresh the propagation carriers because this slice changes one workflow producer, one wrapper, and the edge from `explore` into the current seed producer.

## Current Consequence

- [d:r:i] If this slice lands, the next ownerless seed question becomes cleaner:
  - seed doctrine-vintage
  - broader seed consumers beyond milestone opening
  - later `audit.cjs` widening
