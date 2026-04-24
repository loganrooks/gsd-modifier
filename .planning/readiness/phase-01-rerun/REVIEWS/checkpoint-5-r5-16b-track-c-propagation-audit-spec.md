# Checkpoint 5 R5.16b Track C Propagation Audit Spec

Audit the current Track C candidate surfaces to determine whether launch-truth, closure-status, and debt-carrying-completion changes actually propagate honestly into the real consumers that matter.

This is a seam-specific gap-exposure and completeness-challenge audit. It should not stop at the helper script or at the two overlay agent files.

## Audit Stance

- Audit against the strongest justified pre-rerun standard, not against “better than the old helper/protocol.”
- Treat current capture and closure semantics as possibly directionally improved but still under-owned.
- Look for places where the bundle overstates runtime truth, completion status, or verification confidence.
- Be especially alert to surfaces where debt-carrying completion can still read as clean completion.
- Be firm, specific, and scrutiny-resistant.
- Do not widen scope casually, but do name wider chain-tail or governance consequences when the current consumers clearly under-own them.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
5. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
6. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
7. [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
8. [AUDITS/checkpoint-5-r5-16-propagation-audit-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-16-propagation-audit-bundle-spec.md)
9. [AUDITS/checkpoint-4-cross-lane-seam-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md)
10. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
11. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)

## Candidate Track C Surfaces

12. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
13. [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
14. [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py)
15. [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml)
16. [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml)

## Live / Downstream Consumers

17. [.codex/get-shit-done/workflows/execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md)
18. [.codex/get-shit-done/workflows/verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md)
19. [.codex/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md)
20. [.codex/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md)
21. [.codex/get-shit-done/references/gates.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/gates.md)
22. [.codex/get-shit-done/references/verification-overrides.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/verification-overrides.md)
23. [.codex/get-shit-done/templates/summary.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/summary.md)
24. [.codex/skills/gsd-execute-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-execute-phase/SKILL.md)
25. [.codex/skills/gsd-verify-work/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-verify-work/SKILL.md)

## Questions

- Does the current capture rule distinguish honestly between requested truth, effective truth, and unresolved runtime truth?
- Does the bundle still overstate what `capture_launch_truth.py` can prove?
- Do executor/verifier contract changes propagate the debt-carrying-completion distinction into actual completion consumers?
- Where can mixed or conditional completion still read as clean completion?
- Does the consumer chain preserve the difference between:
  - verified closure
  - mixed closure
  - human-needed closure
  - debt-carrying completion
- Which Track C gaps are truly local to launch-truth and completion consumers, and which point to a wider chain-tail or governance lane?
- Are there important chain-tail, completion, or runtime-truth surfaces missing from this lane's read set that would materially change the scope judgment if added?
- If the bundle stayed local, what likely quality gains or anomaly-accounting work would still be left on the table?

## Output

Write:

- [checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md)

Required sections:

- `Verdict`
- `Blocking Propagation Gaps`
- `Local But Important Gaps`
- `Signals That The Problem May Already Be Wider`
- `What Is Already Strong`
- `What Must Change Before Track C Can Count As Closure-Ready`
- `What Can Remain Local`
- `Change Summary`

Findings must be ordered by severity and cite concrete file lines.
