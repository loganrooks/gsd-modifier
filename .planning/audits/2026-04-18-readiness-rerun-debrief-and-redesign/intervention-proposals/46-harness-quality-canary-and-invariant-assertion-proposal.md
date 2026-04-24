Date: 2026-04-21
Status: active proposal

# Harness-Quality Canary And Invariant Assertion Proposal

## Purpose

- [g:r:i] This proposal defines the first bounded canary family for the harness.
- [g:r:i] The target is not whole-harness semantic adjudication. The target is a machine-checkable guard against silent regressions in the runtime/install surfaces where this workspace already carries explicit invariants.

## Proposed First Slice

- [d:r:i] Add a repo-local helper:
  - `tooling/codex/harness_canary.py`
- [d:r:i] The first slice should check a bounded invariant set:
  1. canonical runtime version anchor exists at `.codex/get-shit-done/VERSION`
  2. overlay manifest contract validates
  3. post-materialization overlay coherence still holds
  4. top-level `.codex/config.toml` reasoning default remains the repo-local expected value
  5. selected high-stakes agent `.toml` reasoning values remain aligned with installer defaults
  6. if durable uplift memory exists, the uplift compatibility anchor is not stale relative to the current observed runtime basis
- [d:r:i] The helper should emit a compact JSON report with typed checks plus a summary, and support a strict exit mode when the caller wants an actual gate.

## Why This Slice

- [d:r:i] The workspace now already has named invariants but no single standing surface that rechecks them together after later contract movement.
- [d:r:i] This first slice raises robustness and maintainability without claiming to understand the whole propagation graph or the whole prose layer.
- [d:r:i] It also turns several already-landed helper families into a more usable operator surface:
  - `portable_gsd_contract.py`
  - `project_uplift.py`
  - runtime version anchors

## What This Slice Does Not Try To Do

- [d:r:i] It does not replace contextual reread.
- [d:r:i] It does not claim full structured/prose coherence.
- [d:r:i] It does not prove propagation completeness.
- [d:r:i] It does not subsume the typed propagation registry.
- [d:r:i] It does not replace later chain-level integration testing.

## Held For Later

- [d:r:i] Later canary growth may add:
  - structured/prose coherence between propagation `v2` JSON and prose family notes
  - registry freshness / stale-refresh signals
  - compact-prompt carry checks
  - broader cross-helper chain assertions
  - broader compatibility / cross-runtime checks
- [d:r:i] Those stay later because the first slice should remain narrow enough to land, test, and operate quickly.

## Verification Shape

- [d:r:i] The first slice should ship with:
  - unit tests for a clean repo fixture
  - unit tests for at least one real regression signal
  - one frozen report artifact on this repo after the helper lands
  - README and doctrine routing so later operators know when to use it

## Current Consequence

- [d:r:i] If accepted, this family should land before wider lifecycle-carry edits because it strengthens the harness against silent runtime drift while later families are still moving.
