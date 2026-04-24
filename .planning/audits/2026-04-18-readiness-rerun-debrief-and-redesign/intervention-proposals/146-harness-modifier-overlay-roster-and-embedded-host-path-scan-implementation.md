Date: 2026-04-22
Status: landed bounded implementation note

# Harness Modifier Overlay Roster And Embedded Host-Path Scan Implementation

## Landed In This Slice

- [d:r:i] Added the authoritative overlay carrier roster:
  - [harness_modifier/overlay/ROSTER.md](../../../../harness_modifier/overlay/ROSTER.md)
- [d:r:i] Added the contextualized embedded-host-path scan:
  - [../extraction-audit/artifacts/03-overlay-embedded-host-path-scan.md](../extraction-audit/artifacts/03-overlay-embedded-host-path-scan.md)

## What The Roster Freezes

- [e:c+i] The tracked overlay frontier currently has `78` entries declared in [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](../../../../tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json).
- [d:r:i] The frozen classification now reads:
  - `generic`: `7`
  - `shared-boundary`: `69`
  - `host-local`: `2`
- [d:r:i] The roster now keeps the first filesystem-rehome-eligible set explicit instead of ambient:
  - `skills/gsd-uplift-project/SKILL.md`
  - `skills/gsd-propagation-review/SKILL.md`
  - `skills/gsd-seed-migration-inventory/SKILL.md`
  - `get-shit-done/workflows/uplift-project.md`
  - `get-shit-done/workflows/propagation-review.md`
  - `get-shit-done/workflows/seed-migration-inventory.md`

## What The Scan Freezes

- [d:r:i] The live blockers are now explicit and contextualized:
  - host audit-workspace links inside `uplift-project.md` and `propagation-review.md`
  - helper-home drift still pointing at `tooling/codex/*.py`
  - compact-prompt bodies that preserve this host repo's own canon and readiness package
- [d:r:i] The scan explicitly does **not** flatten ordinary `.planning/*.md` canon mentions into extraction blockers.

## Resulting Boundary

- [d:r:i] Immediate filesystem rehome is still not the honest move for the workflow shells themselves.
- [d:r:i] The honest next move is now narrower and cleaner:
  - first abstraction pass on the three specialist workflow shells
  - then first filesystem rehome for the specialist trio
- [d:r:i] Compact prompts, overwrite workflow families, template families, and runtime/agent carriers remain later extraction routes.

## Verification

- [d:r:i] roster is exhaustive against the current overlay manifest
- [d:r:i] scan distinguishes blockers from non-blocking canon references instead of flattening every hit into one class
- [d:r:i] governed extraction state/read surfaces updated in the same slice
- [d:r:i] `audit_refmap verify`
- [d:r:i] `git diff --check`

## Exact Next Move

1. [d:r:i] Use the frozen roster plus scan to author the first overlay filesystem-rehome proposal.
2. [d:r:i] Keep that proposal bounded to the specialist trio only.
3. [d:r:i] Do not reopen compact-prompt split, overwrite-family widening, or standalone repo design inside that next slice.
