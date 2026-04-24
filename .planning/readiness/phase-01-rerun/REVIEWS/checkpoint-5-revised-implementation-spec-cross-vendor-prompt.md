# Checkpoint 5 Revised Implementation Spec Cross-Vendor Prompt

Review the revised Checkpoint 5 implementation brief before any new harness edits begin.

This is a high-expectation reread of whether the revised implementation spec is now strong enough to govern the first real Checkpoint 5 patch slice. Do not treat it as a generic approval pass.

## Review Stance

- Review against the strongest justified pre-rerun standard, not against "good enough to start editing."
- Be firm, specific, and scrutiny-resistant.
- Do not reward the revised spec merely for naming more files. Ask whether ownership is actually clean and whether contested decisions are explicitly handled.
- Do not be rude or arbitrary.
- Criticism must be justified in terms of propagation correctness, auditability, runtime/install truth, architectural coherence, future viability, or quality of judgment.
- If the revised spec is strong enough, say so plainly. If not, say exactly what still blocks implementation.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
4. [REVIEWS/checkpoint-5-spec-stack-audit-comparison-ledger.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-audit-comparison-ledger.md)
5. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
6. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
7. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
8. [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
9. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)

Then reread the strongest prior comparison artifacts:

10. [REVIEWS/checkpoint-5-spec-stack-gap-exposure-audit-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-audit-r1.md)
11. [REVIEWS/checkpoint-5-spec-stack-gap-exposure-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-cross-vendor-opus-r1.md)
12. [REVIEWS/checkpoint-5-spec-stack-internal-audit-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-internal-audit-r1.md)

Then inspect the live propagation surfaces named by the revised spec:

13. [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)
14. [.codex/get-shit-done/templates/research.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/research.md)
15. [.codex/get-shit-done/templates/phase-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/phase-prompt.md)
16. [.codex/get-shit-done/references/checkpoints.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/checkpoints.md)
17. [.codex/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md)
18. [tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml)
19. [tooling/portable-gsd/overlay/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-planner.toml)
20. [tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml)
21. [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml)
22. [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml)

## Review Questions

- Does the revised spec now own the convergent propagation surfaces explicitly enough to guide implementation?
- Are any still-critical propagation surfaces absent rather than deliberately deferred?
- Are contested claims still visible as contested, or were they silently promoted or silently dropped?
- Is the tracked overlay/materialization rule now strong enough to withstand later audit on reinstallability and reviewable truth?
- Is the `RESEARCH.md` contract now coherent across workflow, template, researcher, and checker?
- Is the `CONTEXT.md` / steering contract now coherent enough, or does the planner-consumer gap remain under-owned?
- Is the debt-carrying completion boundary now explicit enough to govern implementation, even if some larger chain-tail questions remain conditional?
- Is the chosen use of `future_preservation` a real structured carrier or still too prose-dependent?
- Is the wrapper alignment scope now proportionate and honest?
- What is the strongest justified criticism that remains?
- What would still fail later strong audit if implementation starts from this revised spec?

## Output Requirements

Write a review artifact with:

- `Verdict`
- `Blocking Findings`
- `Supported Scope Decisions`
- `Contested Or Residual-Risk Decisions`
- `What Is Already Strong`
- `What Must Change Before Implementation`
- `Change Summary`

Order findings by severity and cite concrete file lines.
