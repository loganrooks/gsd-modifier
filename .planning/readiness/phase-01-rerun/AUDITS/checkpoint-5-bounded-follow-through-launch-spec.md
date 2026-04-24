# Checkpoint 5 Bounded Follow-Through Launch Spec

## Purpose

Translate the accepted Checkpoint 4 verdict into a bounded implementation checkpoint.

This checkpoint exists because Checkpoint 4 found real harness ownership problems, but it also made clear that not every related hardening opportunity belongs in the pre-rerun path.

## Status Note

This initial launch-spec scope is now partially superseded by:

- [checkpoint-5-reactivated-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-reactivated-launch-spec.md)

Keep this file as the historical record of the first narrower Checkpoint 5 envelope. Do not use it by itself as the current closure authority.

## Governing Inputs

- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
- [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
- [AUDITS/checkpoint-4-cross-lane-seam-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md)
- [AUDITS/checkpoint-4-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-converged-synthesis.md)
- [REVIEWS/checkpoint-4-bundle-cross-vendor-review-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-4-bundle-cross-vendor-review-opus-r1.md)
- [REVIEWS/checkpoint-4-bundle-internal-review-r2.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-4-bundle-internal-review-r2.md)

## Initial Accepted Checkpoint 5 Scope

Checkpoint 5 is bounded to three tracks:

1. `phase-critical runtime-authoritative worker alignment`
2. `review / closure-pressure follow-through on rerun-relevant harness surfaces`
3. `durable launch/model-truth capture rule for doctrine-sensitive worker launches`

## Explicitly Deferred Unless Reactivated

Do not silently absorb these into Checkpoint 5 unless active work directly reaches them:

- broad install pinning
- archival provenance replacement
- full path-portability hardening
- broad branch/worktree redesign
- downstream claim-discipline propagation across every later artifact family

If any of those become necessary, record that explicitly in readiness state rather than widening this checkpoint by drift.

## Track A: Phase-Critical Runtime-Authoritative Worker Alignment

### Intent

Align the actual registered `.toml` worker prompts for the phase-critical chain with the repo’s real instruction and skill surfaces, so the runtime-authoritative path stops lagging behind the human-facing `.md` files and repo doctrine.

### Write scope

- [.codex/agents/gsd-phase-researcher.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-phase-researcher.toml)
- [.codex/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-planner.toml)
- [.codex/agents/gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-plan-checker.toml)
- [.codex/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-executor.toml)
- [.codex/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-verifier.toml)

### Required outcome

- phase-critical `.toml` prompts no longer tell workers to read `./CLAUDE.md` as the governing project surface
- legacy `.claude/skills` / `.agents/skills` guidance is removed or replaced with the repo’s real skill/instruction discovery surfaces
- the updated prompts clearly route workers toward repo `AGENTS.md` and `.planning/AGENTS.md` where relevant
- changes stay bounded to instruction-surface alignment rather than rewriting the whole agent doctrine

### Non-goals

- do not patch every `.toml` in the repo
- do not try to solve home-level `~/.codex/AGENTS.md` from this write scope
- do not redesign agent roles

## Track B: Review / Closure-Pressure Follow-Through

### Intent

Tighten the harness surfaces that currently underweight lone strong criticism or let closure read cleaner than it is, but only on rerun-relevant surfaces.

### Write scope

- [.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md)
- [.codex/get-shit-done/references/planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/planner-reviews.md)

### Required outcome

- cross-AI review prompt explicitly asks for strongest justified criticism, what is merely adequate, and what would fail later stringent audit
- review synthesis preserves lone high-signal criticisms rather than treating reviewer overlap as the only route to importance
- planner reread mode does not require consensus before a high-severity criticism can become must-address
- changes remain review/protocol-focused and do not silently widen into global execution/UAT redesign

### Non-goals

- do not redesign the entire execution-phase closure model in this track
- do not turn review into blanket blocking automation
- do not patch unrelated review surfaces unless the current changes cannot work without them

## Track C: Durable Launch / Model-Truth Capture Rule

### Intent

Make the repo’s launch-truth rule more durable than “remember to query sqlite,” while staying lightweight and reviewable.

### Preferred shape

- a small repo-local helper or protocol surface that makes doctrine-sensitive launch-truth capture easier and more repeatable
- minimal doc updates only where they are inseparable from making that helper/protocol usable

### Likely write scope

- repo-local helper under `tooling/` or `scripts/`
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)

### Required outcome

- doctrine-sensitive worker launches have a clear, reviewable capture rule
- the rule is easier to follow than ad hoc sqlite querying, but still honest about effective-vs-requested settings
- the change does not pretend to automate away judgment

### Non-goals

- do not build a heavy launch-management subsystem
- do not claim this solves all Codex runtime truth or parent-override behavior

## Quality Bar

- prefer the smallest changes that materially improve reliability
- do not widen scope just because more hardening would be nice
- do not leave a track half-finished if the current bundle would still fail later audit on the same seam
- keep the pre-rerun boundary explicit: if something is valuable but not rerun-blocking, record it as deferred or opportunity rather than smuggling it in

## Stopping Rule

Checkpoint 5 is ready for review when:

- Track A aligns the phase-critical runtime-authoritative worker surface cleanly
- Track B strengthens rerun-relevant review pressure without broad redesign
- Track C gives doctrine-sensitive launches a durable capture rule
- any broader portability/provenance work is either untouched or explicitly recorded as reactivated scope

## Review Expectation

Checkpoint 5 is a major checkpoint. It should receive:

- independent internal review
- cross-vendor reread strongly preferred, likely `claude-opus-4.6`, if ownership or boundary questions remain load-bearing at closure
