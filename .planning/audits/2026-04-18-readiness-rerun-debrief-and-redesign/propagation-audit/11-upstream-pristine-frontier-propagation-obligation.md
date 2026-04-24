Date: 2026-04-21
Status: active frontier note

# Upstream-Pristine Frontier Propagation Obligation

## Purpose

- [g:r:i] This note names the propagation obligation that appears when upstream pristine GSD content shifts before repo-local overlay carry is applied.
- [g:r:i] The goal is not to widen into full upstream-template drift machinery. The goal is to stop upstream-pristine pressure from remaining ambient.

## Frontier

- [e:c+i] The local installer still begins with an upstream pristine install via `npx get-shit-done-cc --codex --local` before any repo-local overlay or reasoning defaults are applied [e:c+i]. Source: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:19).
- [e:c+i] `portable_gsd_contract.py` then validates the tracked overlay contract against that installed frontier and distinguishes hard failures such as `backup_overlay_not_overwrite`, `overwrite_missing_backup`, and `add_path_in_backup` [e:c+i]. Source: [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:137).
- [e:c+i] The repo therefore already has two linked install frontiers in practice:
  - upstream-pristine content and its backup-carried overwrite record
  - repo-local overlay content and its manifest typing

## Propagation Obligation

- [d:r:i] When upstream pristine content shifts in a way that affects tracked local carriers, propagation work should not stop at `rerun installer`.
- [d:r:i] The stronger obligation is:
  1. detect which pristine files shifted
  2. check whether any tracked overlay entries now collide or need retagging
  3. revalidate the overlay manifest against backup-carried overwrite truth
  4. decide whether any doctrine, workflow, or runtime capability description must move with that upstream shift
- [d:r:i] This is narrower than full upstream-drift machinery and stronger than treating upstream change as a silent background fact.

## What This Does Not Yet Do

- [d:r:i] This note does not yet automate pristine-diff detection.
- [d:r:i] It does not yet solve aged-bespoke merge or whole-template reconciliation.
- [d:r:i] Those remain later-family work.

## Current Consequence

- [d:r:i] The install/materialization family now has a named upstream-pristine propagation obligation rather than only a local overlay contract.
