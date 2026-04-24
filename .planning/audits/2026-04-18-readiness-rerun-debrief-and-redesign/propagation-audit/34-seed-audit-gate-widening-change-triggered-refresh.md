Date: 2026-04-22
Status: landed change-triggered refresh

# Seed Audit Gate Widening Change-Triggered Refresh

## Trigger

- [g:r:i] The trigger here is a seed-family helper/consumer move: `audit.cjs` now keeps seed contract vintage, Why This Matters, and Strengthening Carry visible in both structured output and the human audit report, and `complete-milestone.md` now tells operators not to flatten those richer seed lines away during acknowledgment or deferment.

## What Moved

- [d:r:i] Helper surface:
  - `tooling/portable-gsd/overlay/get-shit-done/bin/lib/audit.cjs`
- [d:r:i] Consumer reminder:
  - `tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md`
- [d:r:i] Overlay ownership:
  - `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- [d:r:i] Focused proof:
  - `tooling/codex/tests/test_seed_audit_gate_follow_through_contract.py`

## Propagation Consequence

- [d:r:i] The typed `v2` propagation layer should now keep one more live seed route explicit:
  - `plant-seed -> audit-open helper -> milestone-close`
- [d:r:i] `verify-work` remains a named neighboring consumer of `audit-open`, but it stays intentionally untouched in this slice because its current-phase gate does not consume seed rows.

## Registry Refresh

- [d:r:i] Refresh the typed `v2` registry surfaces so they now keep:
  - the overlay-owned audit helper
  - the helper contract for richer seed audit rows
  - the milestone-close consumer relation
  - the intentionally untouched verify-work boundary

## Current Consequence

- [d:r:i] The propagation family now carries an eighteenth non-uplift change-triggered refresh.
- [d:r:i] The next seed-family inheritance question can move on from whether audit-open still flattens seed meaning and instead ask which broader carrier family should widen next.
