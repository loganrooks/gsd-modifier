Date: 2026-04-22
Status: active field map

# Harness Extraction Field Map

## Purpose

- [g:r:i] Separate the standalone harness-project question into one explicit field instead of leaving it mixed into uplift, propagation, parity, and host-project governance notes.
- [g:r:i] The task here is not to authorize immediate extraction.
- [g:r:i] The task is to disclose the boundary that a clean later extraction would need to respect.

## Why This Map Opens Now

- [e:c+i] The workspace now carries a real scope-leak pressure: host-project planning doctrine can be read too easily as harness doctrine when both remain co-located. Sources:
  - [136-harness-extraction-escalation-and-scope-boundary-note.md](136-harness-extraction-escalation-and-scope-boundary-note.md)
  - [../workspace-state-audit/dispositions/01-where-are-we-now-horizon-inheritance-and-parallelization-audit-inheritance.md](../workspace-state-audit/dispositions/01-where-are-we-now-horizon-inheritance-and-parallelization-audit-inheritance.md)
- [e:c+i] The modifier layer is now materially larger than repo glue: it already owns overlay deltas, helper tooling, uplift machinery, parity disclosure, propagation review, and dedicated governance carry. Sources:
  - [101-repo-local-workflow-additions-and-propagation-map-orientation.md](101-repo-local-workflow-additions-and-propagation-map-orientation.md)
  - [115-harness-modifier-extraction-and-npx-distribution-route.md](115-harness-modifier-extraction-and-npx-distribution-route.md)
  - [135-codex-claude-parity-classification-carrier-implementation.md](135-codex-claude-parity-classification-carrier-implementation.md)

## Field Split

- [d:r:i] `generic harness carriers`
  - repo-local helper/tooling surfaces that are not about `prix-guesser` product doctrine
  - runtime/install/update/materialization helpers
  - parity and propagation disclosure helpers
  - reusable workflow/skill overlays whose semantics are not tied to one host product
- [d:r:i] `host-project-specific carriers`
  - `prix-guesser` product-planning docs
  - readiness/rerun canon
  - product-side `LONG-ARC`, `ROADMAP`, `STATE`, and room/game doctrine
  - audit families that only exist because of `prix-guesser` readiness history
- [d:r:i] `shared boundary carriers`
  - onboarding/uplift surfaces that must read host-project docs but are still part of the harness-modifier layer
  - propagation/governance surfaces that currently explain both harness behavior and host-repo embedding
  - provider/runtime translation surfaces for `.codex`, `.claude`, and `get-shit-done`

## Boundary Questions The Extraction Must Settle

- [d:r:i] Which overlay-owned workflows and skills are generic harness routes versus host-repo routes?
- [d:r:i] Which helpers belong in a standalone package:
  - `portable_gsd_contract.py`
  - `project_uplift.py`
  - `run_claude_probe.py`
  - `audit_refmap.py`
  - parity / propagation registries and refresh helpers
- [d:r:i] What compatibility declaration shape should the standalone project own for `.codex` and `.claude`?
- [d:r:i] What should the installer/materializer own for `get-shit-done`, and what should still remain upstream responsibility?
- [d:r:i] Which governance/horizon surfaces should move with the standalone project, and which should remain host-repo-local?
- [d:r:i] What migration path would let a host repo move from bundled modifier layer to standalone install without losing local overrides or propagation clarity?

## Likely First Extraction Shapes

- [d:r:i] `separate repo first, package later`
  - cleanest for doctrine/governance separation
  - lets carrier split harden before npm packaging
- [d:r:i] `package plus installer`
  - potentially stronger operator ergonomics later
  - only after compatibility and materialization ownership are clearer
- [d:r:i] `dual-layer shape`
  - standalone repo as source of truth
  - package/installer as distribution channel

## Current Local Reading

- [d:r:i] Extraction now reads as an active harness direction, not only later packaging appetite.
- [d:r:i] Immediate repo split still stays later because current uplift, parity, and propagation contracts are still moving.
- [d:r:i] The next bounded move is not extraction execution. It is an extraction audit that challenges this field map, widens the carrier split, and sharpens what a standalone harness project would actually need to own.
