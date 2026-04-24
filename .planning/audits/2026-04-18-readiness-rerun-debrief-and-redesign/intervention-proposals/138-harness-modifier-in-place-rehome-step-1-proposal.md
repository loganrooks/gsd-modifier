Date: 2026-04-22
Status: active bounded proposal

# Harness Modifier In-Place Rehome Step 1 Proposal

## Purpose

- [g:r:i] Land `step 1` from the extraction audit without yet splitting into a new repo or package.
- [g:r:i] The move is path- and ownership-oriented, not semantic widening.

## Proposed Move

- [d:r:i] Create one top-level importable `harness_modifier/` directory inside this repo.
- [d:r:i] Move the current generic harness carriers into that directory while keeping them git-tracked in this repo.
- [d:r:i] Keep the old `tooling/codex/*.py` paths only as thin compatibility shims during this first rehome step.
- [d:r:i] Leave shared-boundary helpers explicit about their host-contract reads rather than pretending they are pure generic carriers.

## Candidate First-Slice Contents

- [d:r:i] `harness_modifier/contract/`
  - `portable_gsd_contract.py`
  - `ensure_gsd_sdk_runtime.py`
  - `manifest_install_coherence.py`
  - `runtime_visibility.py`
  - `harness_canary.py`
- [d:r:i] `harness_modifier/capture/`
  - `run_claude_probe.py`
  - `capture_launch_truth.py`
  - `capture_runtime_visibility_snapshot.py`
  - `extract_stream_text.py`
- [d:r:i] later `harness_modifier/overlay/`
  - the overlay-owned workflow / skill / template / reference surfaces that are generic harness carriers rather than host-product doctrine
- [d:r:i] keep explicit shared-boundary holdouts for now:
  - `project_uplift.py`
  - `audit_refmap.py`
  - `seed_migration_inventory.py`
  - host wrapper files
  - host compact-prompt content

## Why This First

- [d:r:i] This forces the carrier split into the filesystem instead of leaving it only in prose.
- [d:r:i] It exposes lingering host-project leakage inside what is currently treated as modifier code.
- [d:r:i] It keeps extraction pressure moving without freezing a standalone repo or package contract too early.

## What This Proposal Does Not Authorize

- [d:r:i] No new repo.
- [d:r:i] No npm package.
- [d:r:i] No installer/distribution branding choice.
- [d:r:i] No support-window widening.
- [d:r:i] No `.claude` full-materialization claim.

## Propagation Obligations

- [d:r:i] `scripts/setup-portable-gsd.sh`
- [d:r:i] import paths across `harness_modifier/*` plus the thin `tooling/codex/*.py` shims
- [d:r:i] tests covering the moved helpers
- [d:r:i] propagation registry `v2` carrier locations
- [d:r:i] any workflow/skill docs that mention the moved helper paths
- [d:r:i] governed docs that point to the moved carriers

## Verification And Review Gates

- [d:r:i] path moves only for this slice; no silent semantic changes
- [d:r:i] focused test pass for the moved helpers
- [d:r:i] `./scripts/setup-portable-gsd.sh`
- [d:r:i] `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --strict`
- [d:r:i] `audit_refmap.py verify`
- [d:r:i] `git diff --check`
- [d:r:i] explicit propagation refresh note for the rehome slice

## Held Later

- [d:r:i] compatibility declaration carrier (`step 2`)
- [d:r:i] second-host dry run (`step 3`)
- [d:r:i] standalone repo extraction (`step 4`)
- [d:r:i] second real host (`step 5`)
- [d:r:i] package/distribution reopening (`step 6`)
