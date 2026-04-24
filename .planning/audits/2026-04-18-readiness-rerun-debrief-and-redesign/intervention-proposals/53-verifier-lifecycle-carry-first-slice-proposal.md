Date: 2026-04-21
Status: active bounded proposal

# Verifier Lifecycle Carry First Slice Proposal

## Purpose

- [g:r:i] Land the first bounded lifecycle-carry slice on the verifier chain so long-horizon and strengthening carry do not intensify only at discuss/plan entry and then thin at verification.
- [g:r:i] The target is not a total lifecycle rewrite. The target is to connect the existing planning-side `future_preservation` contract to the verifier-side workflow, report template, and runtime ownership surfaces.

## Why This Slice Is Real

- [e:c+i] The current planning contract already requires `future_preservation` when `CONTEXT.md` future-awareness is non-empty, and that contract normalizes preserved seams, explicit non-decisions, posture assumptions, and strengthening routes into plan frontmatter. Sources: [/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/phase-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/phase-prompt.md:25), [/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:708), [/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md:65).
- [e:c+i] The long-horizon register already names `verify-phase.md` as the clearest lifecycle-carry thinning point: a phase can verify as behaviorally correct while still collapsing preserved seams or losing strengthening carry. Source: [29-long-horizon-carry-gap-register.md](29-long-horizon-carry-gap-register.md:22).
- [e:c+i] The current tracked overlay owns `gsd-verifier.toml` and `agent-contracts.md`, but it still does not own `get-shit-done/workflows/verify-phase.md` or `get-shit-done/templates/verification-report.md`, so verifier-side lifecycle carry can still drift outside tracked repo-local carry. Source: [/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json:1).

## First Slice

- [d:r:i] Extend verifier-side review so it explicitly loads `future_preservation` from plan frontmatter when present.
- [d:r:i] Add a bounded future-preservation carry review with per-item statuses oriented around:
  - `carried`
  - `thinned`
  - `uncertain`
- [d:r:i] Treat these four item families as the review surface:
  - `protected_seams`
  - `non_decisions`
  - `posture_assumptions`
  - `strengthening_routes`
- [d:r:i] A phase can still satisfy present-tense behavioral truths while thinning future-preservation carry. That should become explicit in verification output rather than remaining ambient.

## Runtime / Contract Surfaces To Move Together

1. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/workflows/verify-phase.md`
2. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/templates/verification-report.md`
3. [d:r:i] `tooling/portable-gsd/overlay/agents/gsd-verifier.toml`
4. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md`
5. [d:r:i] `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`

## Helper / Propagation Follow-Through

- [d:r:i] Refresh `project_uplift.py` so verifier-side lifecycle-carry doctrine participates in the doctrine-reference fingerprint instead of remaining invisible to uplift memory.
- [d:r:i] After the slice lands, treat it as a real change-triggered propagation refresh candidate rather than assuming the existing typed registry already covers it.

## Verification Gates

- [d:r:i] `portable_gsd_contract.py validate-manifest`
- [d:r:i] `./scripts/setup-portable-gsd.sh`
- [d:r:i] `portable_gsd_contract.py verify-materialized`
- [d:r:i] `python3 -m py_compile tooling/codex/project_uplift.py`
- [d:r:i] `python3 -m unittest tooling.codex.tests.test_project_uplift`
- [d:r:i] `audit_refmap.py verify` on the audit root
- [d:r:i] manual reread of the touched verifier-chain surfaces for contract coherence

## Held Later

- [d:r:i] This slice does not yet redesign `transition`, milestone-boundary workflows, `SPEC`, or `STATE/progress`.
- [d:r:i] It does not yet try to auto-adjudicate semantic seam preservation. The verifier still performs contextual review.
- [d:r:i] It does not yet widen into a full lifecycle-carry benchmark family or cross-vendor reread. Those remain later moves after the first slice is live and reviewable.

## Current Consequence

- [d:r:i] If this slice lands, verification will no longer treat long-horizon carry as somebody else’s problem after planning.
- [d:r:i] It will also bring two currently unowned verifier-side runtime carriers under tracked overlay ownership, which is a maintainability and propagation gain even before later lifecycle widening happens.
