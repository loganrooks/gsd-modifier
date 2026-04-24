Date: 2026-04-21
Status: accepted bounded proposal

# Seed Doctrine Vintage Anchor First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next adjacent seed-family slice after the landed `75/76` producer convergence batch.
- [g:r:i] The target is not broader consumer widening yet. The target is a compact vintage anchor:
  - stamp current seed shape explicitly
  - keep milestone-open tolerant of older unversioned seeds

## Why This Slice Is Real

- [e:c+i] The producer convergence sidecar found no live repo-local seed corpus to classify, which means this is the cleanest time to stamp the current shape before more seeds accrue under the current contract. Source: [../propagation-audit/outputs/04-seed-vintage-and-consumer-field-sidecar-gpt54-xhigh-r1.md](../propagation-audit/outputs/04-seed-vintage-and-consumer-field-sidecar-gpt54-xhigh-r1.md:6).
- [e:r:i] The current `plant-seed` contract now carries richer meaning, but it does not yet write an explicit contract vintage marker into the seed file itself.
- [e:r:i] `new-milestone` already reads seeds from disk, but it does not yet say how to treat a missing version marker. Without that explicit tolerance, later compatibility work stays more ambient than it should.

## Bounded First Slice

- [d:r:i] Keep the slice narrow: one producer, one primary consumer, one wrapper.
- [d:r:i] Add `seed_contract_version: 2` to the current `plant-seed` frontmatter shape.
- [d:r:i] Teach `new-milestone` to extract seed contract vintage when present and to treat a missing version marker as `legacy_unversioned`, not as an error.
- [d:r:i] Keep this visible in operator selection context so later readers can tell whether a matched seed is current-contract or legacy-unversioned.
- [d:r:i] Keep the wrapper explicit that current seed creation writes the version anchor.

## Held Later

- [d:r:i] This slice does not yet widen `audit.cjs`.
- [d:r:i] It does not yet add uplift-side seed vintage scanning.
- [d:r:i] It does not yet create a larger seed migration helper or rewrite older seed corpora.

## Verification Gates

- [d:r:i] Extend the focused seed contract proof so it checks:
  - `seed_contract_version: 2` in the producer
  - explicit milestone-open tolerance for missing version markers as `legacy_unversioned`
  - current-version language in the wrapper
- [d:r:i] Re-materialize the overlay so the live `.codex` frontier carries the same seed vintage anchor.
- [d:r:i] Refresh the propagation carriers because this slice changes the seed producer/consumer contract while keeping the same bounded family.

## Current Consequence

- [d:r:i] If this slice lands, later seed doctrine-vintage and compatibility work starts from a seed family that already distinguishes current-contract seeds from legacy-unversioned ones at the main producer and main consumer.
