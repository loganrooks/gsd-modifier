Date: 2026-04-21
Status: landed first slice

# Strengthening-Opportunity First Slice Implementation

## Purpose

- [g:r:i] This note records the first live harness insertion for the consumer-first strengthening family after proposal `30`, its challenged review pair, and the instruction-surface hardening pass.

## What Landed

- [e:r:i] `discuss-phase` now names `Strengthening Opportunities` as a first-class `future_awareness` bucket and carries that bucket into the generated `CONTEXT.md` shape.
- [e:r:i] `context.md` now gives the bucket a stable section and a bounded definition so it stays distinct from generic open-question routing.
- [e:r:i] `plan-phase` now requires each strengthening item to route through `future_preservation.strengthening_routes` as either an `intensification task` or an `explicit hold-and-seed` path, and it rejects generic carry on that route during plan checking.
- [e:r:i] `phase-prompt.md` now carries `future_preservation.strengthening_routes` in the phase frontmatter contract so the planning surface and downstream consumers share the same field.
- [e:r:i] `plant-seed` now explicitly carries strengthening-origin seeds by recording current strength, bounded intensification move, and optionality effect when a strengthening item is routed out of phase.

## Runtime And Overlay Carry

- [e:r:i] The live runtime surfaces under `.codex/get-shit-done/` and the tracked overlay surfaces under `tooling/portable-gsd/overlay/get-shit-done/` now carry the same strengthening-route behavior.
- [e:r:i] The tracked overlay gained a new `plant-seed.md` workflow file, giving the first slice full tracked carry instead of live-only partial carry.

## Verification

- [e:r:i] `git diff --check` passed for the implementation batch before this note was written.
- [e:r:i] `scan_threshold_language.py` reported a clean result across the touched live and overlay workflow/template surfaces after one inherited `plan-phase` line was corrected.
- [e:r:i] Normalized live-vs-overlay parity checks passed for the placeholderized workflow/template pairs, and direct parity passed for `plant-seed.md`.

## Why This Slice Matters

- [d:r:i] The strengthening family now has direct runtime and artifact carry, not just proposal or review language.
- [d:r:i] It now has real consumer carry in the planning chain:
  - terrain disclosure in `future_awareness`
  - explicit routing in `future_preservation`
  - durable out-of-phase resurfacing through `plant-seed`
- [d:r:i] That makes later evaluation possible on artifacts rather than rhetoric alone.

## What This Still Holds

- [d:r:i] This batch holds the separate reference-surface object as a later adjacent slice.
- [d:r:i] This batch holds the separate `gsd-rigorous-research` mode extension as a later adjacent slice.
- [d:r:i] This batch keeps milestone, transition, and verification carry families for later follow-through rather than absorbing them into the first insertion.

## Current Consequence

- [d:r:i] The next adjacent object for this intervention family is later research-mode / reference-surface shaping on top of an already-landed first slice.
- [d:r:i] The next adjacent object is how to shape the later research-mode / reference-surface follow-through against real strengthening entries produced by actual planning work.
