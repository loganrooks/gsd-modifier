Date: 2026-04-22
Status: landed first slice

# Seed Audit Gate Widening First Slice Implementation

## Landed Surfaces

- [d:r:i] Overlay-owned audit helper:
  - [tooling/portable-gsd/overlay/get-shit-done/bin/lib/audit.cjs](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/bin/lib/audit.cjs)
- [d:r:i] Existing milestone-close consumer reminder:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md)
- [d:r:i] Overlay ownership contract:
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [d:r:i] Focused contract proof:
  - [tooling/codex/tests/test_seed_audit_gate_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_audit_gate_follow_through_contract.py)

## What Changed

- [e:r:i] `audit.cjs` now prefers the canonical frontmatter seed id when present instead of flattening identity back into the filename stem.
- [e:r:i] Seed rows now carry:
  - `contract_vintage`
  - `why_this_matters_excerpt`
  - `strengthening_carry_status`
  - `strengthening_carry_excerpt`
- [e:r:i] The human audit report now keeps vintage and strengthening visibility explicit, and it surfaces short `why:` / `carry:` lines when present instead of flattening seeds back into bare id/status/title.
- [e:r:i] `complete-milestone.md` now tells the operator to keep surfaced contract-vintage and strengthening-carry lines visible during acknowledgment or deferment rather than compressing the decision back to bare seed ids.

## Intentional Non-Moves

- [d:r:i] `verify-work` stayed untouched in this slice.
  - it does invoke `audit-open --json`
  - but its current-phase gate filters only UAT, verification, and CONTEXT rows
  - seed widening there would have been extra movement without real local consumer use
- [d:r:i] Wider entry-wrapper retrofit remains later-family work.
- [d:r:i] Standalone legacy-seed migration remains later-family work.

## Verification

- [d:r:i] Focused contract test now stages the overlay audit helper with its runtime-lib siblings and proves the widened JSON/report output on a temporary seed corpus.
- [d:r:i] Overlay ownership is now explicit for `get-shit-done/bin/lib/audit.cjs`.
- [d:r:i] The slice is paired with a propagation refresh so the helper and milestone-close consumer relation do not stay ambient.

## Current Consequence

- [d:r:i] The seed family now keeps richer meaning visible at:
  - the producer
  - milestone-open selection
  - uplift/re-entry operator surfaces
  - milestone-close audit judgment
- [d:r:i] The next seed-family inheritance question should now move beyond this helper toward a broader carrier choice rather than revisiting whether milestone-close can see seed vintage and strengthening carry at all.
