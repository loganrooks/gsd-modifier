# Checkpoint 5 Spec Stack Gap-Exposure Cross-Vendor Prompt

Audit the current Checkpoint 5 candidate spec stack before any widened workflow or wrapper implementation lands.

This is a completeness-challenge and gap-exposure audit. It is not merely a closure-verification pass, and it is not a Popperian falsification exercise in the narrow sense. The task is to surface what remains unowned, under-specified, contradictory, prematurely deferred, or insufficiently propagated across the harness.

## Audit Stance

- Audit against the strongest justified pre-rerun standard, not against “good enough to start editing.”
- Treat the candidate stack as something that may be directionally right but still incomplete, internally inconsistent, or under-propagated.
- Look for missing ownership, not just for outright contradiction.
- Be firm, specific, and scrutiny-resistant when the candidate stack still leaves meaningful work unnamed.
- Do not be rude or arbitrarily harsh.
- Criticism must be justified in terms of rigor, propagation correctness, auditability, architectural soundness, future viability, or quality of judgment.
- Do not reward a candidate stack merely for having explicit scope if that scope still leaves shared consequences unowned.
- Do not assume every gap must block progress; classify what is truly pre-implementation critical versus what can remain explicit later work.

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
10. [REVIEWS/checkpoint-5-spec-stack-gap-exposure-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-audit-spec.md)

Then audit the current candidate stack:

11. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
12. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
13. [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
14. [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py)
15. [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md)
16. [tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md)
17. [tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml)
18. [tooling/portable-gsd/overlay/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-planner.toml)
19. [tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml)
20. [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml)
21. [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml)

Read the likely propagation surfaces before judging completeness:

22. [.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md)
23. [.codex/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md)
24. [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md)
25. [.codex/get-shit-done/workflows/execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md)
26. [.codex/get-shit-done/templates/context.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/context.md)
27. [.codex/get-shit-done/templates/research.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/research.md)
28. [.codex/get-shit-done/templates/phase-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/phase-prompt.md)
29. [.codex/get-shit-done/references/checkpoints.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/checkpoints.md)
30. [.codex/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md)
31. [.codex/get-shit-done/references/ui-brand.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/ui-brand.md)
32. [.codex/skills/gsd-discuss-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md)
33. [.codex/skills/gsd-plan-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-plan-phase/SKILL.md)
34. [.codex/skills/gsd-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md)
35. [.codex/skills/gsd-execute-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-execute-phase/SKILL.md)

## Gap-Exposure Questions

- Where does the candidate stack still under-own propagation burdens created by its own requested changes?
- Which surfaces are being treated as secondary or deferred even though they are active semantic dependencies of the proposed changes?
- Which semantics would become contradictory if only the four named workflow files changed?
- Where does the current stack still confuse:
  - runtime truth vs tracked reinstallable truth
  - workflow prose vs agent/runtime contract
  - clean completion vs debt-carrying completion
  - preserved openness vs unresolved ambiguity
- If `CONTEXT.md` semantics change, which downstream consumers would still parse the old contract?
- If `RESEARCH.md` semantics change, which orchestrators, templates, checkers, or agent contracts would still enforce incompatible expectations?
- If planning closure pressure changes, which shared checkpoint, reference, or UI surfaces would still normalize the old permissive behavior?
- If execution completion semantics change, which verifier, summary, state, or checkpoint surfaces would still misclassify the result?
- Which currently deferred items are probably misclassified and should be promoted into active Checkpoint 5 ownership?
- Which currently active items are actually downstream consequences that should be named separately rather than hidden inside a large patch?
- What is the strongest justified challenge to the claim that the candidate stack is complete enough to guide implementation?
- What remains merely adequate here but should be stronger before implementation begins?
- What later audit failure is most likely if implementation starts from this stack unchanged?
- What important quality opportunity is being left unused right now?

## Output Requirements

Write a review artifact with:

- `Verdict`
- `Blocking Gaps`
- `Propagation Gaps`
- `Misclassified Deferrals / Scope Decisions`
- `What Is Already Strong`
- `What Must Change Before Implementation`
- `What Can Remain Deferred`
- `Shared Contract Consequences`
- `Change Summary`

Findings should be ordered by severity and cite concrete file lines.

If the candidate stack is strong enough to guide implementation, say so explicitly.
If not, say exactly what must change before any workflow or wrapper patching proceeds.
