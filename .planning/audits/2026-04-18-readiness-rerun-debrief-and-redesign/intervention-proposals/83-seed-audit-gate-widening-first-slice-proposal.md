Date: 2026-04-22
Status: accepted bounded proposal

# Seed Audit Gate Widening First Slice Proposal

## Purpose

- [g:r:i] Open the next adjacent seed-family slice after the landed operator-facing seed consumer widening in `81/82`.
- [g:r:i] The target is the existing open-artifact audit helper and its milestone-close consumer path:
  - `audit.cjs`
  - `complete-milestone`

## Why This Slice Is Real

- [e:c+i] The seed family now preserves richer meaning at the producer and main milestone-open consumer: current-versus-legacy vintage, `Why This Matters`, and explicit `Strengthening Carry` are already part of the live contract. Sources: [73-seed-consumer-carry-first-slice-proposal.md](73-seed-consumer-carry-first-slice-proposal.md), [77-seed-doctrine-vintage-anchor-first-slice-proposal.md](77-seed-doctrine-vintage-anchor-first-slice-proposal.md), [81-seed-operator-consumer-widening-first-slice-proposal.md](81-seed-operator-consumer-widening-first-slice-proposal.md).
- [e:c+i] The later seed sidecar already named `audit.cjs` as the next natural reader to widen because it flattens seed meaning back to id, status, and title. Source: [../propagation-audit/outputs/04-seed-vintage-and-consumer-field-sidecar-gpt54-xhigh-r1.md](../propagation-audit/outputs/04-seed-vintage-and-consumer-field-sidecar-gpt54-xhigh-r1.md:22).
- [e:c+i] `complete-milestone.md` already displays the full audit report and routes acknowledgment/deferment through that operator surface, so leaving the richer seed meaning outside the audit lane keeps milestone-close judgment thinner than it needs to be. Source: [../propagation-audit/outputs/04-seed-vintage-and-consumer-field-sidecar-gpt54-xhigh-r1.md](../propagation-audit/outputs/04-seed-vintage-and-consumer-field-sidecar-gpt54-xhigh-r1.md:17).

## Bounded First Slice

- [d:r:i] Keep the slice narrow:
  - overlay-own `get-shit-done/bin/lib/audit.cjs`
  - preserve milestone-close as the explicit human-facing consumer
  - leave `verify-work` intentionally untouched because its current-phase filter does not consume seed rows
- [d:r:i] Teach `audit.cjs` to keep these seed fields visible in both JSON and human report output:
  - canonical seed id from frontmatter when present
  - contract vintage (`seed_contract_version` or `legacy_unversioned`)
  - `Why This Matters` excerpt
  - `Strengthening Carry` status and excerpt
- [d:r:i] Add one milestone-close reminder so those richer seed lines stay visible during acknowledge/defer judgment instead of being flattened back into bare seed ids.

## Held Later

- [d:r:i] This slice does not widen `verify-work`.
- [d:r:i] It does not yet open the broader entry-wrapper retrofit family.
- [d:r:i] It does not create a standalone legacy-seed migration helper.
- [d:r:i] It does not turn `audit-open` into a full seed-semantic reader for every later workflow.

## Verification Gates

- [d:r:i] Add focused contract coverage for:
  - overlay ownership of `audit.cjs`
  - structured seed rows carrying vintage plus strengthening data
  - human report formatting that keeps those fields visible
  - milestone-close consumer wording that tells operators not to flatten the richer seed lines away
- [d:r:i] Re-materialize the overlay so the live `.codex` runtime carries the same audit helper.
- [d:r:i] Refresh the propagation family because this slice changes one live helper, one consumer reminder, and one overlay ownership contract.

## Current Consequence

- [d:r:i] If this slice lands, milestone-close audit judgment no longer sees seeds as only id/status/title.
- [d:r:i] The next seed-family question then becomes which broader follow-through should inherit after the richer audit helper is live: wider entry-wrapper retrofit, standalone legacy-seed migration, or a later broader audit consumer family beyond milestone-close.
