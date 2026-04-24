# Checkpoint 4 GSD Agent Doctrine And Role Contracts Excellence Spec

## Purpose

Audit the active repo-local GSD agent-role contracts and shared doctrine surfaces against the repo's excellence bar.

This lane should determine whether the operative prompts and shared doctrine actually push workers toward rigorous, future-aware, high-quality work or whether they still leave too much to luck, politeness, or pass/fail completion bias.

## Why This Lane Exists Now

Checkpoint 3 established that this is a distinct GSD surface, not just part of workflow files or runtime configuration.

If the agent-role contracts are weak, the repo can have clean workflow files and still produce thin output.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
4. [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)
5. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
6. [GATES/checkpoint-4.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md)
7. [AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md)
8. [AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md)
9. [02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md)

Then inspect, at minimum:

- repo-local GSD agent definitions under `.codex/get-shit-done/agents/`
- repo-local GSD workflow prompt injections that materially shape those roles
- any shared reference files or prompt fragments that those workers actually inherit
- repo-local review surfaces such as `gsd-review` that materially shape reread pressure

## Core Questions

- do the operative worker contracts actually carry the repo's rigor bar, claim discipline, pushback duty, and future-aware doctrine?
- where do role prompts still reward mere completion over high-quality judgment?
- is review pressure explicit enough, or still too polite and forgiving by default?
- are there places where worker prompts are under-specified relative to the repo's demands?
- what is genuinely strong here, and what is still too thin to survive later expert scrutiny?
- what is the strongest justified criticism of the current role/doctrine surface?

## Output

Write:

- [checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Current Strengths`
- `Where Role Contracts Carry The Quality Bar Well`
- `Where Role Contracts Still Encourage Thinness`
- `Pushback / Review / Claim-Discipline Assessment`
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

- do not treat undocumented aspiration as effective doctrine
- distinguish what workers are actually likely to receive from what surrounding docs say in principle
- do not patch files
- do not collapse runtime launch truth into this lane except where it changes which doctrine actually reaches workers

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
