Date: 2026-04-21
Status: active local map

# Project-Uplift Producer / Consumer And Impact Map

## Purpose

- [g:r:i] This note is the first concrete local map in the propagation-audit family.
- [g:r:i] It does not try to map the whole harness at once. It uses the hardened uplift example to make producer, consumer, mirror, and held-neighbor relations explicit before any wider challenge lane opens.

## Path Of Inquiry

- [d:r:i] The current map was built from:
  - the hardened helper and its tests
  - the tracked overlay workflow and skill
  - the tracked overlay `progress` consumer
  - the durable uplift outputs under `.planning/`
  - the materialization path through `scripts/setup-portable-gsd.sh`
  - the then-current absence of any `resume-project` uplift consumer
  - the earlier Checkpoint-3 contract-mapping frame

## Route Map

| Surface | Role | Carry Type | What It Carries Now | Propagation Consequence |
|---|---|---|---|---|
| `tooling/codex/project_uplift.py` | primary producer | authoritative logic surface | carrier sampling, posture classification, report/manifest/state rendering, `progress-note` bridge | when uplift semantics move, this is the first surface that must move |
| doctrine/runtime input carrier cohort sampled by the helper | primary inputs | sampled source surfaces | AGENTS / CLAUDE, `CLAIM-TYPES.md`, `LONG-ARC.md`, tooling inventory, runtime config, runtime agent contracts, strengthening carriers, active phase `CONTEXT.md` | when the helper changes what it samples or how it interprets the cohort, the workflow, tests, and durable output schema should be reread |
| `tooling/portable-gsd/overlay/get-shit-done/workflows/uplift-project.md` | direct consumer | operator entry workflow | invokes `project_uplift.py detect`, interprets JSON, presents posture, routes next action | if helper CLI flags, JSON fields, or output posture semantics change, this workflow must stay in tune |
| `tooling/portable-gsd/overlay/skills/gsd-uplift-project/SKILL.md` | wrapper consumer | invocation / routing mirror | routes user invocation to the live workflow and controls default `--write` posture | usually stable unless the workflow name, entry contract, or write policy changes |
| `tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md` | direct consumer | read-only routed consumer | calls `project_uplift.py progress-note` and surfaces `Uplift Posture` inside ordinary progress routing | if manifest/progress-note fields or recommendation semantics change, this workflow must move with them |
| `.planning/UPLIFT-MANIFEST.json` | primary durable output | structured memory | authoritative stored uplift posture, fingerprints, pending proposal routes, held-later families | if schema or field meanings change, helper, workflow prose, progress consumer, and tests all need reread |
| `.planning/UPLIFT-REPORT.md` | durable narrative output | operator-facing mirror | human-readable uplift disposition on the same analyzed basis | if narrative sections or recommendation vocabulary change, scan and review gates should reread it |
| `.planning/STATE.md` uplift section | durable continuity output | compact carry-forward mirror | terse uplift memory for ordinary project-state rereads | if the compact continuity contract changes, `resume-project` and other state readers become relevant neighbors |
| `scripts/setup-portable-gsd.sh` | materialization carrier | overlay -> live bridge | patches tracked overlay files into live `.codex/` runtime | when tracked overlay workflow/consumer surfaces change, rerun materialization and verify the live runtime |
| live `.codex/` copies of `uplift-project.md`, `progress.md`, and `gsd-uplift-project/SKILL.md` | live consumers | materialized runtime surfaces | actual runtime execution surfaces used by repo-local GSD | do not hand-patch these; verify they re-materialize from overlay carry |
| `tooling/codex/tests/test_project_uplift.py` | verification consumer | behavioral gate | synthetic checks for classification, output writing, doctrine drift, marker hashing, runtime agent globbing | if helper behavior changes and tests do not, the propagation path is incomplete |
| `tooling/codex/README.md` | inventory mirror | tooling discovery surface | tells later operators this helper exists and what contract it currently carries | should move when helper capability or neighboring held-later reference changes materially |
| `tooling/codex/UPLIFT-HELD-LATER.md` | held-family registry | explicit non-absorption carrier | names the uplift families the current slice keeps visible instead of silently absorbing | should move when the held-later boundary itself changes, not for routine runtime output refresh |

## What Moved Together In The Harden Slice

- [e:r:i] The harden slice propagated across the core producer/consumer chain rather than stopping at the helper:
  - helper logic
  - overlay workflow
  - overlay `progress` consumer
  - widened tests
  - durable outputs
  - tooling inventory
  - held-later registry
  - governance/instruction surfaces that now name contract propagation as a first-rank obligation
- [d:r:i] This means the current harden slice is already stronger than a local-code-only change, but it still does not amount to whole-network proof.

## Surfaces That Stayed Stable On Purpose

- [d:r:i] `tooling/portable-gsd/overlay/skills/gsd-uplift-project/SKILL.md` stayed almost unchanged because the invocation contract did not widen; it still delegates to the workflow and carries the same detect-only / explicit-write posture.
- [d:r:i] `resume-project.md` did not change because the current slice still keeps `progress` as the only live routed consumer.
- [d:r:i] Additive install routes, cross-runtime reconciliation, upstream-template drift machinery, audit-aging carry, and wider entry hooks remain explicit held families rather than accidental omissions.

## Impact Map By Change Type

### If Classification Or Signal Semantics Change

- [d:r:i] Reread and likely update:
  - `project_uplift.py`
  - `test_project_uplift.py`
  - `uplift-project.md`
  - `progress.md`
  - `UPLIFT-MANIFEST.json` schema / field meanings
  - `UPLIFT-REPORT.md`
  - `STATE.md` uplift section
- [d:r:i] Also reread the active local family artifacts that describe the baseline:
  - `39`
  - `40`
  - `42`

### If Carrier Inventory Or Fingerprint Semantics Change

- [d:r:i] Reread and likely update:
  - helper carrier specs and hashing functions
  - widened tests
  - `UPLIFT-MANIFEST.json`
  - workflow prose that names the returned fields
  - `UPLIFT-HELD-LATER.md` if the held boundary also changes
- [d:r:i] Materialization should be rerun if the changed carrier also affects overlay-backed runtime surfaces.

### If CLI Flags Or Write Policy Change

- [d:r:i] Reread and likely update:
  - `uplift-project.md`
  - `gsd-uplift-project/SKILL.md`
  - any consumer or operator doc that recommends detect-only vs write behavior
  - tests that assume current write posture

### If Durable Output Schema Changes

- [d:r:i] Reread and likely update:
  - helper render/write functions
  - `progress-note`
  - `progress.md`
  - `STATE.md` uplift section contract
  - local family docs that treat the manifest as authoritative structured memory

## Current Thin Spots

- [d:r:i] At the time this map was written, `progress` was the only live routed consumer. That asymmetry is what later opened `03`.
- [d:r:i] See `04` for the landed second-consumer follow-through that resolves this specific thin spot through `resume-project`.
- [d:r:i] The current map is still local to the uplift example. The broader network question remains open: how many other workflow / output / registry families should be mapped in the same producer / consumer / mirror / held-neighbor form?

## Current Consequence

- [d:r:i] The propagation family now has its first explicit local impact map instead of only a seed concern.
- [d:r:i] The strongest next local follow-through identified here is now carried in `03` and landed in `04`.
