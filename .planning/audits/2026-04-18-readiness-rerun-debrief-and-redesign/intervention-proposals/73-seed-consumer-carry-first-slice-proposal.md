Date: 2026-04-21
Status: accepted bounded proposal

# Seed Consumer Carry First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next adjacent onboarding and lifecycle-carry slice after the landed update follow-through in `71` and `72`.
- [g:r:i] The target is the seed producer/consumer bridge:
  - `plant-seed`
  - `new-milestone`

## Why This Slice Is Real

- [e:r:i] The harness already preserves seed existence and trigger timing, and `new-milestone` already scans matching seeds.
- [e:r:i] What still thins is the richer meaning of those seeds:
  - bounded motivation
  - strengthening carry
  - optionality-preserving intent that should still matter when the seed resurfaces later
- [e:r:i] Right now that meaning is partly ambient. `plant-seed` can note strengthening routes, but only as an optional note. `new-milestone` extracts idea, trigger, and planted-during context, but not the richer strengthening carry explicitly.
- [e:r:i] That leaves the consumer bridge weaker than it could be exactly where long-horizon and self-overcoming intent should remain sharper.

## Bounded First Slice

- [d:r:i] Keep the slice narrow: one producer, one primary consumer, one wrapper.
- [d:r:i] Strengthen `plant-seed` so it carries an explicit `Strengthening Carry` section instead of leaving that meaning ambient inside generic notes.
- [d:r:i] Strengthen `new-milestone` so its seed scan extracts:
  - `Why This Matters`
  - `Strengthening Carry` when present
- [d:r:i] Keep milestone-open routing explicit:
  - matching seeds stay optional and selected by route
  - selected seeds become stronger requirement-shaping context
  - unselected seeds remain untouched

## Held Later

- [d:r:i] This slice does not yet invent a full doctrine-vintage system for seeds.
- [d:r:i] It does not yet widen seed resurfacing beyond milestone opening.
- [d:r:i] It does not redesign broader deferred-item or backlog families.

## Verification Gates

- [d:r:i] Add a focused contract test that checks:
  - overlay ownership for `plant-seed.md` and `skills/gsd-plant-seed/SKILL.md`
  - explicit strengthening-carry section in the seed producer
  - explicit consumer extraction of `Why This Matters` and `Strengthening Carry` in `new-milestone`
- [d:r:i] Re-materialize the overlay so the live `.codex` frontier carries the same producer/consumer bridge.
- [d:r:i] Refresh propagation carriers because this slice changes one producer workflow, one wrapper, and the milestone-open consumer relation.

## Current Consequence

- [d:r:i] If this slice lands, the next ownerless question is no longer whether seeds exist. It becomes whether later seed doctrine-vintage, broader seed consumers, or wider entry-wrapper retrofit should inherit next.

