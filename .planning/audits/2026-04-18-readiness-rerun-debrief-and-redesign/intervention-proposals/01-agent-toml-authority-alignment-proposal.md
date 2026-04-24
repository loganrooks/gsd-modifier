Date: 2026-04-20
Status: draft bounded proposal

# Agent TOML Authority Alignment Proposal

## Purpose

- [g:r:i] This proposal defines a bounded follow-through candidate for the most direct runtime-authority gap currently visible in the repo-local harness: registered `.toml` agent contracts that can drift away from the repo’s actual doctrine, skill/runtime surfaces, and high-stakes operating posture.

## Why This Proposal Exists

- [e:c+i] Checkpoint 4’s sharpest Codex-side criticism was runtime-authoritative worker drift: the registry points at `.codex/agents/*.toml`, so those files carry real spawned-worker behavior even when human reviewers are more likely to read nicer `.md` surfaces or root doctrine docs. Sources: [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:70), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:78), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:91), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:99).
- [e:c+i] The completed companion layer routes any `spawned agent / authority / model / reasoning` goal directly to `.codex/config.toml` and `.codex/agents/*.toml` before nicer wrapper prose. Sources: [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:22), [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:35), [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:60).
- [e:c+i] The runtime/materialization companion then confirms why: live `.codex/config.toml` registers the `.toml` files directly, making them effective spawn/runtime authority surfaces. Sources: [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:40), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:57), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:79).

## Bounded Scope

- [d:r:i] Limit the first alignment pass to the high-stakes planning/execution/verification cohort:
  - `.codex/agents/gsd-planner.toml`
  - `.codex/agents/gsd-plan-checker.toml`
  - `.codex/agents/gsd-executor.toml`
  - `.codex/agents/gsd-verifier.toml`
- [d:r:i] This is intentionally narrower than “all agents.” The proposal targets the cohort most likely to steer canon, plans, execution behavior, and verification truth before widening to other roles.

## Proposed Move

### 1. Establish An Alignment Checklist

- [d:r:i] For each high-stakes `.toml` file, check whether its `developer_instructions` surface:
  - directs the agent to root `AGENTS.md`
  - directs the agent to `.planning/AGENTS.md` when `.planning/` artifacts are in scope
  - points the agent at repo-local `.codex/skills/` and repo-local `get-shit-done` references/workflows rather than stale/foreign surfaces
  - reflects the repo’s anti-threshold quality bar and current runtime doctrine where relevant
  - does not contradict the actual repo-local install/materialization posture

### 2. Align The Cohort To One Runtime Doctrine

- [d:r:i] Rewrite only the mismatched parts of the `.toml` cohort so the runtime-authoritative instructions and the repo’s human-readable doctrine stop pulling in different directions.
- [d:r:i] Keep the move doctrinal, not stylistic. The goal is not prose uniformity. The goal is authority convergence at the runtime-owned seam.

### 3. Add A Small Drift Check

- [d:r:i] Pair the alignment pass with a lightweight reviewable check, for example a bounded artifact that records:
  - which high-stakes `.toml` files were aligned
  - which doctrine surfaces they are expected to honor
  - which remaining agents are still out of scope
- [d:r:i] This should be a narrow drift check, not a magical auto-sync system that rewrites agent prompts invisibly.

## Explicit Non-Goals

- [d:r:i] Do not widen this first pass to every agent role.
- [d:r:i] Do not redesign the whole agent system.
- [d:r:i] Do not assume `.md` companion files or stable docs should become the runtime source of truth by themselves.
- [d:r:i] Do not treat launch-truth capture as solved by this proposal; that is a separate bounded surface.

## Why This Bounded Shape Is Stronger

- [d:r:i] It attacks the most direct runtime-authority gap first.
- [d:r:i] It stays small enough to verify concretely.
- [d:r:i] It avoids the weak move of “write more docs” when the problem is a runtime-owned contract surface.
- [d:r:i] It can later widen to other agents only if the first cohort actually improves carry and reduces doctrine/runtime divergence.

## Success Signals

- [d:r:i] A later reader can compare the four `.toml` files against repo doctrine and see materially less drift.
- [d:r:i] High-stakes spawned agents no longer route themselves toward stale or foreign control surfaces.
- [d:r:i] Review of planning/execution/verification returns depends less on operator memory of repo-specific corrections.

## Ceremony Risk Check

- [d:r:i] This proposal fails if it only makes the `.toml` files look more polished while leaving actual runtime doctrine drift intact.
- [d:r:i] It also fails if it widens immediately into a repo-wide agent rewrite before the high-stakes cohort shows real leverage.

## Next Disposition Question

- [g:r:i] The next decision on this proposal should be whether to accept a bounded cohort alignment pass now, revise the scope or verification rule, or hold it behind some narrower precondition.
