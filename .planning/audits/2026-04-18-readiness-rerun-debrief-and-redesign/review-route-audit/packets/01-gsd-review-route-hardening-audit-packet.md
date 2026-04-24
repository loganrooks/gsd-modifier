Date: 2026-04-22
Status: frozen lane packet

# GSD Review Route Hardening Audit Packet

## Lane Purpose

- [g:r:i] Audit the current repo-local `$gsd-review` route and widen the first hardening shape that would make it carry more of the repo's actual cross-vendor review discipline.

## Why This Lane Exists Now

- [e:c+i] The current overlay-owned review route still carries the older thin pattern: `/tmp` prompt/output files, sequential external invocations, and one final `REVIEWS.md` consumer artifact without durable lane-home, launch-truth, or timing calibration. Sources:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:149)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:157)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:167)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:278)
- [e:c+i] The workspace now has a richer audit-lane pattern library, launch-truth discipline, timing-calibration discipline, and provider-specific failure tooling that the current review route does not yet inherit. Sources:
  - [AUDIT-LANE-PATTERN-LIBRARY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/AUDIT-LANE-PATTERN-LIBRARY.md:31)
  - [AUDIT-LANE-PATTERN-LIBRARY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/AUDIT-LANE-PATTERN-LIBRARY.md:55)
  - [AUDIT-LANE-PATTERN-LIBRARY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/AUDIT-LANE-PATTERN-LIBRARY.md:69)
  - [tooling/codex/run_claude_probe.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/run_claude_probe.py:1)
  - [tooling/codex/extract_stream_text.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/extract_stream_text.py:1)
  - [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:1)
- [d:r:i] The user also raised a more precise concern: a review route should vary with what the crossover is crossing into, and failure should not collapse into empty output when a last recoverable message still exists.

## Read Set

Read these exact files:

1. [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md)
2. [tooling/portable-gsd/overlay/skills/gsd-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-review/SKILL.md)
3. [tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md)
4. [tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md)
5. [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md)
6. [tooling/codex/run_claude_probe.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/run_claude_probe.py)
7. [tooling/codex/extract_stream_text.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/extract_stream_text.py)
8. [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py)
9. [AUDIT-LANE-PATTERN-LIBRARY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/AUDIT-LANE-PATTERN-LIBRARY.md)
10. [LAUNCH-LEDGER.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/root-support/LAUNCH-LEDGER.md)
11. [.planning/HARNESS-IMPROVEMENT-REGISTER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/HARNESS-IMPROVEMENT-REGISTER.md)
12. [entry-uplift-audit/dispositions/23-codex-claude-installation-parity-audit-inheritance.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/entry-uplift-audit/dispositions/23-codex-claude-installation-parity-audit-inheritance.md)
13. [intervention-proposals/134-codex-claude-parity-classification-carrier-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/134-codex-claude-parity-classification-carrier-proposal.md)
14. [intervention-proposals/135-codex-claude-parity-classification-carrier-implementation.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/135-codex-claude-parity-classification-carrier-implementation.md)

## Governing Questions

- [g:r:i] Should the repo harden the existing `$gsd-review` route directly, or is a separate repo-local review-route family warranted?
- [g:r:i] What is the better first-slice structure for:
  - run-home and artifact durability
  - launch-truth
  - timing estimate versus actual
  - provider-shaped runner differences
  - failure-path salvage
  - planner-facing `REVIEWS.md` carry
- [g:r:i] How should the route distinguish reviewer shapes rather than flattening them?
  - `claude` stream-json + salvage
  - `codex` jsonl/last-message + salvage
  - plain stdout/stderr reviewers
- [g:r:i] Which parts belong in a helper/tooling layer, and which should remain workflow/skill contract?
- [g:r:i] What other bounded uplift routes around the review workflow are worth naming now, even if they are not the first live slice?
  - route split by review subject (`phase-plan review` versus `audit/proposal reread` versus other review families)
  - stronger relation between `gsd-review` and repo-local audit-lane discipline
  - propagation and governance surfaces that should change when the route changes
  - later provider-specific salvage or model-truth follow-through beyond the first slice

## Anti-Misread Notes

- [g:r:i] Do not widen this lane into full multi-provider portability.
- [g:r:i] Keep `.codex` and `.claude` as the primary local runtime horizon.
- [g:r:i] Do not treat `capture_launch_truth.py` as the only launch-truth model here; this lane crosses external CLI process truth too.
- [g:r:i] Do not flatten failure handling into a binary success/failure question. The lane should consider what can still be salvaged or preserved when a reviewer partially returns.
- [g:r:i] Do not propose a giant telemetry system as the first slice unless you can justify why the simpler run-home/logging layer would not carry the route far enough.
- [g:r:i] Do not assume the current phase-plan review route is the only review-shaped surface worth improving; the lane may name adjacent review-route opportunities if it keeps their ownership and ordering explicit.

## Output Target

- [d:r:i] Write the lane return to:
  - [../outputs/01-gsd-review-route-hardening-audit-opus47-max-r1.md](../outputs/01-gsd-review-route-hardening-audit-opus47-max-r1.md)
