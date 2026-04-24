Date: 2026-04-22
Status: accepted bounded proposal

# Legacy Seed Corpus Migration Detect-Only First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next adjacent seed-family slice after the landed `83/84` audit-side widening.
- [g:r:i] The target is a specialist detect-only migration packet:
  - inventory older or drifted seed corpora precisely
  - keep rewrite or normalization work separate
  - let uplift point at that packet instead of carrying the whole migration story itself

## Why This Slice Is Real

- [e:r:i] The seed family now keeps current-versus-legacy posture visible at the producer, milestone-open, uplift, operator re-entry, and milestone-close audit surfaces.
- [e:r:i] That visibility still stops at counts, examples, and richer audit rows; there is no dedicated per-seed migration inventory that says what an older corpus would need to join the current contract.
- [e:r:i] The current repo has no live `.planning/seeds/` corpus, which makes this a clean moment to land the specialist detect-only route without dragging local rewrite pressure into the batch.
- [e:r:i] The route should stay explicit about two different carriers:
  - `.planning/seeds/SEED-*.md` as the seed corpus
  - `STATE.md` `Future Carry Forward -> Seeded` lines as a different continuity channel

## Bounded First Slice

- [d:r:i] Keep the slice narrow:
  - one repo-local helper
  - one workflow
  - one wrapper
  - one uplift-route handoff
- [d:r:i] Inventory each seed by:
  - contract vintage
  - missing current-contract frontmatter keys
  - missing current-contract sections
  - bounded migration moves
- [d:r:i] Write durable outputs only when explicitly requested:
  - `.planning/SEED-MIGRATION-REPORT.md`
  - `.planning/SEED-MIGRATION-MANIFEST.json`
- [d:r:i] Keep the route detect-only:
  - no seed rewrites
  - no bulk normalization
  - no milestone-open or audit helper widening in this slice

## Held Later

- [d:r:i] This slice does not rewrite seed files.
- [d:r:i] It does not fold seed migration semantics into everyday `progress` or `resume-project` output.
- [d:r:i] It does not widen `harness_canary.py`, `runtime_visibility.py`, or `manifest_install_coherence.py` into seed-aware helpers.
- [d:r:i] It does not widen broader entry-wrapper retrofit or broader audit-open consumer families.

## Verification Gates

- [d:r:i] Add focused helper tests for:
  - mixed current, legacy-unversioned, and noncurrent seed corpora
  - current-version seeds with contract-shape gaps
  - durable report/manifest writes
- [d:r:i] Add focused contract proof for:
  - overlay ownership of the new workflow and wrapper
  - uplift route language pointing at the specialist inventory packet
  - rewrite staying separate from detect-only
- [d:r:i] Re-materialize the overlay after the workflow and wrapper land.
- [d:r:i] Refresh the propagation family because this slice adds a new helper/workflow/wrapper route and changes the uplift handoff.

## Current Consequence

- [d:r:i] If this slice lands, older projects will have a sharper seed-corpus migration packet without forcing rewrite machinery into uplift, milestone-open, or milestone-close.
- [d:r:i] The next seed-family question then becomes narrower:
  - later rewrite automation
  - later broader audit-open consumer widening
  - later wider entry-wrapper retrofit
