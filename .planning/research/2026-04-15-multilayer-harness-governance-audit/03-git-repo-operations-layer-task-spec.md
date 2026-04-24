# 03 Git And Repo-Operations Layer Audit - Task Spec

## Purpose

Audit the Git- and repo-operations layer for this repo:

- change-set discipline
- branch/worktree strategy
- task-boundary and checkpoint practice
- review/merge expectations
- operational hygiene for a large, long-lived, agent-assisted repo

This is the `repo operations / production governance` slice, but it must be treated as one lane inside the broader harness audit rather than the whole job.

## Core Question

What Git and repo-operations discipline should this repo adopt so that planning, canon, research, implementation, and subagent work stay reviewable, revertible, and long-horizon-safe as the repo grows?

## Motivating Grounds

This lane exists because the recent failure was not only orchestration-deep but version-control-deep:

- the working tree accumulated multiple unresolved logical change sets
- task transitions were not checkpointed
- the user explicitly reframed the problem as a Git working-tree / version-control problem, not just a vague process issue

Primary grounds:

- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-execution-report.md`

## Required Reading

- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-execution-report.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
- relevant repo Git state and existing branch posture

## Specific Questions

1. What Git disciplines should become explicit repo rules now?
2. When should same-checkout path-based commits be acceptable, and when should separate branches/worktrees be mandatory?
3. What acceptance/disposition rules should exist for subagent-returned work?
4. What PR/review/merge expectations are needed for a repo with heavy planning/canon/audit work as well as later code?
5. What should be enforced by:
   - norms/docs
   - helper commands
   - branch/worktree policy
   - CI checks

## Output Requirements

Write:

- current Git/repo-ops strengths
- current weak points
- recommended near-term rules
- recommended later rules as repo complexity rises
- branch/worktree strategy guidance
- checkpoint/park/accept/revise guidance
- how this layer supports long-horizon quality, not just cleanliness

Include one section called:

- `Progressive governance by risk and blast radius`
- `Motivating grounds`

## Anti-Misread Rules

- Do not collapse Git hygiene into “clean working tree.”
- Do not assume production-grade branch protections are needed immediately if lighter discipline would be better now.
- Do not drift into CI/deployment implementation details beyond what this layer genuinely owns.
