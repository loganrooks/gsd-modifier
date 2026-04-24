Date: 2026-04-21
Status: landed first slice

# Harness-Quality Canary First Slice Implementation

## Purpose

- [g:r:i] This note records the first landed slice of the canary/invariant-assertion family opened in `46`.
- [g:r:i] The target is a bounded machine-checkable runtime/install guard, not whole-harness semantic adjudication.

## What Landed

- [e:r:i] A new repo-local helper now exists at [tooling/codex/harness_canary.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/harness_canary.py).
- [e:r:i] The helper’s first slice checks:
  - canonical runtime version anchor presence at `.codex/get-shit-done/VERSION`
  - overlay manifest contract validation
  - post-materialization coherence
  - top-level runtime config reasoning default
  - selected high-stakes agent reasoning defaults
  - uplift compatibility-anchor freshness when durable uplift memory exists
- [e:r:i] The helper supports a strict mode, so the same bounded report can be used as a real gate when the caller wants one.
- [e:r:i] Unit coverage now exists at [tooling/codex/tests/test_harness_canary.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_harness_canary.py).
- [e:r:i] The helper is now routed in:
  - [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md)
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
  - [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)

## Live Repo Result

- [e:r:i] A frozen strict report now exists at [01-harness-quality-canary-report.json](../harness-improvement-audit/artifacts/01-harness-quality-canary-report.json).
- [e:r:i] The current repo result is clean on the bounded invariant set:
  - `22` checks
  - `0` issues
  - `0` not-applicable rows
- [d:r:i] That makes the canary a useful current baseline rather than only a proposed helper.

## Corrections Surfaced During Landing

- [e:r:i] The first direct script invocation failed because the helper only imported cleanly as a module, not as a repo-local script path.
- [e:r:i] That defect is now corrected inside the helper so both invocation modes work:
  - module path in tests
  - direct repo-local script invocation in operator use

## What This Slice Still Holds

- [d:r:i] This slice still does not claim:
  - structured/prose coherence between propagation `v2` JSON and prose family notes
  - registry freshness or stale-refresh signaling
  - whole-chain integration proof across every helper
  - broader cross-runtime compatibility coverage
- [d:r:i] Those remain later canary growth rather than being smuggled into the first slice.

## Current Consequence

- [d:r:i] The harness now has a real bounded canary for several already-named invariants instead of only doctrine reminding operators to reread runtime files by hand.
- [d:r:i] The next strongest follow-through inside the harness-improvement family is no longer another canary widening pass by default. The next strongest follow-through is the audit-program infrastructure family or the standing self-improvement register family, with lifecycle-carry still explicit as the next larger workflow-touching family.
