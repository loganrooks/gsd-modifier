# Checkpoint 5 Spec Stack Audit Spec

Audit the current Checkpoint 5 candidate spec stack before any widened workflow or wrapper implementation lands.

This is a pre-implementation audit of scope, propagation, and hidden dependency handling. It is not permission to rewrite the checkpoint from scratch without justification.

## Audit Stance

- Audit against the strongest justified pre-rerun standard, not against “good enough to start editing.”
- Be firm, specific, and scrutiny-resistant when the candidate stack is still too narrow, too ad hoc, or silently dropping propagation consequences.
- Do not be rude or arbitrarily harsh.
- Try seriously to falsify the candidate stack before declaring it strong enough to guide implementation.
- Criticism must be justified in terms of rigor, propagation correctness, auditability, architectural soundness, future viability, or quality of judgment.
- Do not treat `has a spec` as sufficient if the spec still leaves inter-surface consequences unowned.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
4. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
5. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
6. [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
7. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
8. [AUDITS/checkpoint-5-reactivated-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-reactivated-launch-spec.md)
9. [AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md)

Then audit the current candidate stack:

10. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
11. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
12. [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
13. [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py)
14. [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md)
15. [tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md)
16. [tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml)
17. [tooling/portable-gsd/overlay/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-planner.toml)
18. [tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml)
19. [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml)
20. [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml)

Read the likely propagation surfaces before judging whether the spec is complete enough:

21. [.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md)
22. [.codex/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md)
23. [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md)
24. [.codex/get-shit-done/workflows/execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md)
25. [.codex/get-shit-done/templates/context.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/context.md)
26. [.codex/skills/gsd-discuss-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md)
27. [.codex/skills/gsd-plan-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-plan-phase/SKILL.md)
28. [.codex/skills/gsd-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md)
29. [.codex/skills/gsd-execute-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-execute-phase/SKILL.md)

## Audit Questions

- Is the current candidate stack still too narrow for the changes it is implicitly proposing?
- If `discuss-phase`, `CONTEXT.md`, or open-question handling changes, what else must change so downstream stages do not silently misread or ignore the new semantics?
- If `research-phase` changes its adequacy/disposition contract, do planning, validation, review, or agent-role surfaces also need updates?
- If `plan-phase` closure pressure changes, what else in execution, verification, wrapper skills, or review doctrine must change so the system remains internally coherent?
- If `execute-phase` starts distinguishing clean completion from debt-carrying completion more sharply, what tracking, review, or package consequences must be updated too?
- Are any currently deferred items actually active dependencies of the candidate changes rather than true later work?
- Is wrapper alignment really secondary for this candidate stack, or are there wrapper-first invocation risks that make some wrapper changes primary now?
- Does the current spec overfit to the four named workflows while missing shared references, templates, agent prompts, or overlays that would need to move in tandem?
- Are the current readiness package updates truthful and sufficient, or is the package still lagging the real candidate state?
- What is the strongest justified criticism of this candidate stack?
- What is merely adequate here but should be stronger before implementation begins?
- What would likely fail later stringent audit by strong engineers, product developers, or external rereads?
- What meaningful quality opportunity is currently being left unused?

## Output

Write:

- [checkpoint-5-spec-stack-internal-audit-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-internal-audit-r1.md)

Required sections:

- `Verdict`
- `Findings`
- `What Is Already Strong`
- `What Must Change Before Implementation`
- `What Can Remain Deferred`
- `Propagation Consequences`
- `Change Summary`

Findings must be ordered by severity and cite concrete file lines.

If the candidate stack is strong enough to guide implementation, say so explicitly.
If not, say exactly what must change before any workflow or wrapper patching proceeds.
