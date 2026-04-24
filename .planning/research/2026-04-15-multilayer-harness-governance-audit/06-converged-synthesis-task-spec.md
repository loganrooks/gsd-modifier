# 06 Converged Synthesis - Task Spec

## Purpose

Synthesize the multi-layer audit into one decision artifact that:

- answers the user's larger original question
- integrates the narrower orchestration audit rather than repeating it
- clarifies how repo-operations fits within the broader harness/governance picture
- produces a staged roadmap for near-term, medium-term, and later controls

## Inputs

- `00-launch-bundle-spec.md`
- `01-codex-orchestration-layer-audit.md`
- `02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `03-git-repo-operations-layer-audit.md`
- `04-ci-release-and-deployment-layer-audit.md`
- `05-cross-layer-integration-and-escalation-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`

## Core Questions

1. What did the narrower orchestration/framework audit settle, and what did it leave open?
2. What does the broader multi-layer audit now add?
3. What should the repo change now?
4. What should be designed but deferred?
5. How should the repo stage stronger controls as it grows?
6. How should `LONG-ARC.md` and long-horizon doctrine be integrated day-to-day across layers?

## Motivating Grounds

This synthesis exists to answer the user's larger original question more fully than the narrower orchestration/framework audit could.

The narrower audit was necessary but insufficient because it mostly covered:

- orchestration failure
- lifecycle weakness around `LONG-ARC.md`
- guardrail and command ideas

What it did not fully answer was the larger multi-layer question across:

- Codex
- repo-local GSD
- Git / repo operations
- CI / release / deployment
- and the relationship between those layers

Your synthesis must preserve that distinction and answer the broader ask directly.

## Output Requirements

Write a single synthesis artifact that contains:

- `Integrated diagnosis`
- `What is already strong`
- `What is weak or missing by layer`
- `Near-term changes`
- `Deferred but important changes`
- `Escalation model by risk / blast radius / complexity`
- `How repo-operations fits into the larger stack`
- `Recommended implementation sequence`
- `Source-basis and epistemic limits`

Include one explicit section called:

- `Answer to the original broader ask`
- `Motivating grounds`

That section should answer plainly whether the current harness stack is sufficient, partially sufficient, or insufficient for the vision the user described, and why.

In `Source-basis and epistemic limits`, explicitly distinguish at least:

- claims grounded in repo-internal cited evidence about current repo state
- claims that are mainly repo-specific reasoned recommendations
- claims, if any, that are directly externally grounded

Do not let repo-internal governance analysis read like externally validated universal best practice.

## Anti-Misread Rules

- Do not flatten the lanes into one undifferentiated governance blob.
- Do not lose the distinction between:
  - current repo need
  - future larger-project need
  - permanent design principle
- Do not quietly replace the broader ask with only repo-ops recommendations.
- Do not quietly blur internal evidence, external evidence, and reasoned recommendation into one generic `cited` tone.
