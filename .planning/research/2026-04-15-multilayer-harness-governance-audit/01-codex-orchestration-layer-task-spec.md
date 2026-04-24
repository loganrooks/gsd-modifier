# 01 Codex Orchestration Layer Audit - Task Spec

## Purpose

Audit the Codex-layer control surface for this repo:

- subagent delegation defaults
- task-boundary handling
- context pressure and context loss
- task-transition hygiene
- runtime verification discipline
- hooks and visible guardrails

The goal is to determine whether the current Codex-layer operating model is capable of supporting the repo's required rigor and future-aware posture, and what should change.

## Core Question

At the Codex orchestration layer, what is already working, what is structurally weak, and what mechanisms should be changed so the main thread behaves more like a strong orchestrator and less like a shallow do-everything worker?

## Motivating Grounds

This lane exists because the current session exposed a specifically Codex-layer failure pattern:

- exploratory and scope-shaping work stayed in the main thread too long
- delegation happened too late
- task transitions were not cleanly dispositioned
- the user explicitly said the orchestrator should have used subagents more and should not have proceeded across buckets with a messy tree

Primary grounds:

- `.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`

Your output must keep those motivating grounds visible rather than drifting into generic Codex advice.

## Required Reading

- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `.codex/hooks.json`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md`

## Specific Questions

1. What Codex-layer behaviors currently rely too much on prompt discipline rather than explicit operating structure?
2. Where should subagent-first behavior become a default rather than a conversational preference?
3. What task-transition or disposition controls are still missing at the orchestration layer?
4. What should remain prompt/policy-level versus hook-level versus command-level?
5. What failure modes still threaten long-horizon work:
   - shallow exploration
   - context flattening
   - hidden assumption carry-over
   - task drift
   - ambiguous acceptance state

## Output Requirements

Write:

- current Codex-layer strengths
- current Codex-layer weaknesses
- recommended near-term changes
- recommended later changes
- mechanisms grouped by:
  - prompt/policy
  - hook
  - command/skill
  - runtime verification / reporting
- how those changes help preserve `LONG-ARC.md` and future-aware rigor

Include one section called:

- `What should not be solved at the Codex layer`
- `Motivating grounds`

## Anti-Misread Rules

- Do not audit Git/CI/deploy deeply here; flag handoff points to other lanes instead.
- Do not assume a hook is better just because it feels enforceable.
- Do not recommend broad blocking hooks for nuanced doctrine or task-boundary questions without strong justification.
- Distinguish `main-thread orchestration discipline` from `subagent capability`.
