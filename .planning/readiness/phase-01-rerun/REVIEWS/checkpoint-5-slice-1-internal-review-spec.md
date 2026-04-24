# Checkpoint 5 Slice 1 Internal Review Spec

Review the first real Checkpoint 5 implementation slice before any commit.

This is not a soft “does this look okay?” pass. It is a high-expectation reread of whether the current slice is strong enough to count as checkpoint-moving evidence for the planning/research contract chain, while keeping the older partial Track B/C bundle explicitly out of scope unless the current slice directly contradicts it.

## Review Stance

- Review against the strongest justified pre-rerun standard, not against “better than before.”
- Be firm, specific, and scrutiny-resistant.
- Do not reward the slice merely for widening files touched. Ask whether the new producer/consumer contract is actually cleaner, more auditable, and less contradiction-prone.
- Do not ignore runtime/install truth. If the slice claims overlay/materialization discipline but still leaves touched runtime truth effectively ambient, call that out.
- Do not let older partial Track B/C work muddy the verdict. This review is about the current planning/research slice plus the runtime-regression repair that was required to keep repo-local doctrine alive.
- Criticism must be justified in terms of propagation correctness, auditability, runtime/install truth, architectural coherence, future viability, or quality of judgment.
- If the slice is strong enough, say so plainly. If not, say exactly what still blocks commit.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
4. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
5. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
6. [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
7. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)

Then inspect the target slice:

8. [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)
9. [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml)
10. [tooling/portable-gsd/overlay/skills/gsd-rigorous-research/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-rigorous-research/SKILL.md)
11. [tooling/portable-gsd/overlay/skills/gsd-rigorous-research/references/method.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-rigorous-research/references/method.md)
12. [tooling/portable-gsd/overlay/skills/gsd-rigorous-research/references/output-template.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-rigorous-research/references/output-template.md)
13. [tooling/portable-gsd/overlay/skills/gsd-rigorous-research/references/repo-canon.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-rigorous-research/references/repo-canon.md)
14. [tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml)
15. [tooling/portable-gsd/overlay/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-planner.toml)
16. [tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml)
17. [tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md)
18. [tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md)
19. [tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md)
20. [tooling/portable-gsd/overlay/get-shit-done/templates/research.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/research.md)
21. [tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md)

Inspect the live runtime copies only as needed to verify materialization coherence:

22. [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml)
23. [.codex/skills/gsd-rigorous-research/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-rigorous-research/SKILL.md)
24. [.codex/agents/gsd-phase-researcher.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-phase-researcher.toml)
25. [.codex/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-planner.toml)
26. [.codex/agents/gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-plan-checker.toml)
27. [.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md)
28. [.codex/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md)
29. [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md)
30. [.codex/get-shit-done/templates/research.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/research.md)
31. [.codex/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md)

## Explicitly Excluded From This Verdict

These files are currently dirty but belong to the older partial Track B/C carry-forward bundle. Do not treat them as part of this slice unless the target slice directly contradicts them:

- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
- [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py)
- [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml)
- [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml)
- [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md)
- [tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md)

The new entries in:

- [DEFERRED.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/DEFERRED.md)
- [OPPORTUNITIES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/OPPORTUNITIES.md)

are bookkeeping captures, not part of the checkpoint-moving semantic slice.

## Review Questions

- Does the slice now satisfy the accepted Checkpoint 5 planning/research contract scope rather than only touching adjacent prose?
- Is runtime/install truth now materially stronger because the repo-specific `config.toml` and `gsd-rigorous-research` capability are restored through tracked overlay rather than by ad hoc runtime edits?
- Is the `RESEARCH.md` producer/consumer chain now coherent across workflow, template, researcher, and checker?
- Is the richer `CONTEXT.md` consumer contract now materially widened rather than still producer-only?
- Did the slice leave any obvious producer/consumer naming mismatch or legacy-marker contradiction still active?
- Are there any touched runtime surfaces in this slice that still lack adequate tracked overlay ownership?
- Does the path-correction work in `plan-phase.md` actually eliminate stale non-Codex governing-surface references where it matters?
- What is the strongest justified criticism that remains?
- What would still fail later strong audit if this slice were committed now?

## Output

Write:

- [checkpoint-5-slice-1-internal-review-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-slice-1-internal-review-r1.md)

Required sections:

- `Verdict`
- `Blocking Findings`
- `Non-Blocking Findings`
- `What Is Strong`
- `Residual Risks Or Explicit Non-Goals`
- `Change Summary`

Order findings by severity and cite concrete file lines.
