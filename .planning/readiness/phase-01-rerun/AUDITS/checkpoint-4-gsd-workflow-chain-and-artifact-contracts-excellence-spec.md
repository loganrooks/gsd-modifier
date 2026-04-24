# Checkpoint 4 GSD Workflow Chain And Artifact Contracts Excellence Spec

## Purpose

Audit the repo-local GSD phase-critical workflow chain and shared artifact contracts against the repo's excellence bar.

This lane should determine whether the workflow chain rewards strong steering, research, planning, execution, and verification work, or mainly pushes artifacts toward minimal closure.

## Why This Lane Exists Now

Checkpoint 3 already separated the GSD side into:

- workflow chain plus artifact contracts
- agent-role/doctrine contracts
- runtime/config/overlay truth

This lane owns the first of those excellence judgments.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
4. [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
5. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
6. [GATES/checkpoint-4.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md)
7. [AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md)
8. [AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md)
9. [AUDITS/checkpoint-3-gsd-scope-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-scope-synthesis.md)

Then inspect, at minimum:

- `.codex/get-shit-done/workflows/discuss-phase.md`
- `.codex/get-shit-done/workflows/research-phase.md`
- `.codex/get-shit-done/workflows/plan-phase.md`
- `.codex/get-shit-done/workflows/execute-phase.md`
- `.codex/get-shit-done/workflows/verify-work.md`
- `.codex/get-shit-done/templates/context.md`
- `.codex/get-shit-done/templates/phase-prompt.md`
- `.codex/get-shit-done/templates/config.json`
- any directly coupled review/checker/validation workflow files that materially affect the phase-critical chain

## Core Questions

- does the chain reward strong discussion, research, planning, execution, and verification, or mainly create artifact-shaped proof of motion?
- where does pass/fail logic replace opportunity-seeking or doctrine-sensitive pressure?
- is the plan-checking and verification posture strong enough for the repo's standard?
- where do artifact contracts preserve nuance well, and where do they flatten distinctions that later matter?
- what future-aware doctrine or non-decision handling is fragile across the chain?
- what is the strongest justified criticism of this workflow surface?

## Output

Write:

- [checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Current Strengths`
- `Where The Workflow Chain Rewards Excellence`
- `Where The Workflow Chain Settles For Pass/Fail Closure`
- `Artifact Contract Pressure Points`
- `Verification / Review / Completion Pressure`
- `Strongest Justified Criticisms`
- `Strategic Opportunities`
- `Ownership Assessment`
- `Conditional Follow-Through Candidates`

`Ownership Assessment` must classify each material finding as:

- `doc-level doctrine`
- `workflow-protocol`
- `machinery-owned`
- or `split/ambiguous`

## Constraints

- do not judge the agent-role surface here except where it directly shapes the workflow chain
- do not collapse runtime/config truth into this lane
- do not patch files
- do not treat artifact count or phase count as evidence of rigor

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
