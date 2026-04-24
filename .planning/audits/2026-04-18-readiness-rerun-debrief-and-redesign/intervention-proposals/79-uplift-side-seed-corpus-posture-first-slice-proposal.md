Date: 2026-04-22
Status: accepted bounded proposal

# Uplift-Side Seed Corpus Posture First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next adjacent seed-family slice after the landed `77/78` producer-plus-milestone vintage anchor batch.
- [g:r:i] The target is project-wide visibility, not migration:
  - teach uplift to see current versus legacy seed posture across the repo
  - preserve that posture in durable uplift memory
  - keep any later seed rewrite or migration route separate

## Why This Slice Is Real

- [e:r:i] `plant-seed` and `new-milestone` now distinguish current-contract from legacy-unversioned seed shape, but project uplift still cannot see a seed corpus at all.
- [e:r:i] That means an older or mixed seed corpus can remain invisible during repo-wide onboarding or uplift even though milestone-open now has bounded compatibility rules.
- [e:r:i] The current repo has no seed corpus, which makes this a clean time to land posture scanning before mixed real project histories accumulate under the refreshed contract.

## Bounded First Slice

- [d:r:i] Keep the slice narrow:
  - helper
  - uplift workflow
  - uplift wrapper
  - durable uplift outputs
- [d:r:i] Scan `.planning/seeds/SEED-*.md` and classify the current seed corpus as:
  - no seed corpus
  - current-contract only
  - legacy-unversioned present
  - noncurrent versions present
- [d:r:i] Preserve counts and small bounded examples in uplift memory.
- [d:r:i] Treat seed posture movement like compatibility movement for the purpose of refreshing durable uplift memory.
- [d:r:i] Keep migration or rewrite separate from detect-only.

## Held Later

- [d:r:i] This slice does not rewrite seed files.
- [d:r:i] It does not add broader seed-consumer widening beyond the current milestone-open consumer.
- [d:r:i] It does not widen `audit.cjs`.
- [d:r:i] It does not create a standalone seed migration helper.

## Verification Gates

- [d:r:i] Extend project uplift tests so they cover:
  - seed corpus posture classification
  - legacy-unversioned detection
  - durable uplift-memory refresh routing after seed corpus movement
- [d:r:i] Refresh the live uplift outputs with `--write`.
- [d:r:i] Refresh the propagation registry because this slice changes helper/workflow/wrapper/output carry for the uplift family.

## Current Consequence

- [d:r:i] If this slice lands, project uplift will stop flattening seed compatibility into local milestone-open knowledge and start carrying it as project-wide onboarding posture too.
