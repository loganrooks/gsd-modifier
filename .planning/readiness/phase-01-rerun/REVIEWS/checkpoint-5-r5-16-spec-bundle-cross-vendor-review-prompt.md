# Checkpoint 5 R5.16 Spec Bundle Cross-Vendor Review Prompt

Review the newly written `R5.16` propagation-audit spec bundle itself.

The question is not merely whether these specs are coherent enough to run. The question is whether they are the strongest justified audit prompts we should be using before launching a high-stakes Checkpoint 5 propagation bundle.

This is a review of prompt quality, scope discipline, epistemic posture, and likely audit yield.

## Review Stance

- Review against the strongest justified pre-rerun standard, not against “good enough to launch.”
- Do not assume a spec is strong just because it is detailed.
- Do not assume a spec is weak just because it is scoped.
- Test whether the specs:
  - read the right surfaces
  - ask the right questions
  - distinguish local and wider consequences responsibly
  - preserve anti-regret pressure
  - avoid smuggling orchestration bias into the audit design
- Be firm, specific, and scrutiny-resistant.
- Criticism must be justified with respect to audit quality, rigor, likely epistemic yield, propagation awareness, and later audit survivability.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
5. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
6. [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md)
7. [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml)
8. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
9. [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
10. [AUDITS/checkpoint-4-cross-lane-seam-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md)
11. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)

Then review the spec bundle under audit:

12. [AUDITS/checkpoint-5-r5-16-propagation-audit-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-16-propagation-audit-bundle-spec.md)
13. [REVIEWS/checkpoint-5-r5-16a-track-b-propagation-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16a-track-b-propagation-audit-spec.md)
14. [REVIEWS/checkpoint-5-r5-16a-track-b-propagation-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16a-track-b-propagation-cross-vendor-prompt.md)
15. [REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-spec.md)
16. [REVIEWS/checkpoint-5-r5-16b-track-c-propagation-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-cross-vendor-prompt.md)
17. [REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-spec.md)
18. [REVIEWS/checkpoint-5-r5-16d-adjudication-reread-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-spec.md)
19. [REVIEWS/checkpoint-5-r5-16d-adjudication-reread-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-cross-vendor-prompt.md)

Where relevant, also inspect the actual candidate/lived surfaces those specs point to, to judge whether the prompt bundle is reading enough:

20. [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md)
21. [tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md)
22. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
23. [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
24. [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py)
25. [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml)
26. [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml)

## Questions

- Are these the best justified specs we could reasonably launch now, or are they still thin, biased, or under-specified?
- Does the seam split make sense, or does it still hide important cross-seam propagation surfaces?
- Are the governing reads strong enough, or do the specs omit important sources they should force auditors to inspect?
- Do the prompts ask sufficiently demanding questions, or do they still risk “passable” reviews?
- Do `R5.16c` and `R5.16d` actually protect against scope-conservative orchestration bias, or do they still leave that bottleneck too weakly challenged?
- Where do the specs overconstrain the output structure in a way that may reduce epistemic yield?
- Where are the specs too generic, too brief, too repetitive, or too loose?
- Which changes would most materially improve the quality of the audits before launch?
- What would likely fail later stringent audit if we launched these prompts unchanged?

## Output

Write:

- [checkpoint-5-r5-16-spec-bundle-cross-vendor-review-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16-spec-bundle-cross-vendor-review-opus-r1.md)

Required sections:

- `Verdict`
- `Highest-Impact Spec Defects`
- `Missing Or Underweighted Read Surfaces`
- `Epistemic / Scope Bias Risks`
- `What Is Already Strong`
- `What Must Change Before Launch`
- `What Can Stay As-Is`
- `Change Summary`

Findings should be ordered by severity and cite concrete file lines.
