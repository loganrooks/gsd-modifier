# 04 CI, Release, And Deployment Layer Audit - Task Spec

## Purpose

Audit the CI / GitHub Actions / release / deployment governance layer that this repo does or should have, with special attention to:

- progressive enforcement
- verification
- release safety
- rollback posture
- how automation should support, rather than replace, strong long-horizon judgment

## Core Question

What CI/release/deployment controls should this repo eventually adopt, and which of those are worth introducing now versus later, if the goal is to support a large, long-lived, agent-assisted project with strong quality and future-awareness requirements?

## Motivating Grounds

This lane exists because the user explicitly pushed beyond workflow-only fixes and asked about:

- proper devops and deployment posture
- GitHub Actions and enforcement strategy
- how stronger controls should evolve as the repo grows and risk rises

The narrower orchestration audit treated this as a deferred but real next layer rather than part of the immediate cleanup.

Primary grounds:

- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- current repo governance docs
- the absence or thinness of current CI/release/deployment control surfaces

## Required Reading

- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- any current `.github/` workflows or related automation files if present
- any repo scripts bearing on verification, packaging, release, or setup

## Specific Questions

1. What CI/release/deploy controls are absent but likely needed later?
2. Which of those would already be valuable now?
3. Which controls should wait until:
   - more code exists
   - multiple environments exist
   - deployment is real
   - contributor count or blast radius rises
4. How should CI/release automation interact with:
   - Git discipline
   - GSD workflow
   - Codex/subagent workflows
   - doctrine-sensitive planning changes
5. What anti-hallucination / anti-shortcut checks belong here, if any, versus elsewhere?

## Output Requirements

Write:

- current state and gaps
- near-term recommended CI/release/deploy controls
- later-stage recommended controls
- escalation thresholds for stronger automation
- what should never be left only to CI
- how this layer should support long-horizon project quality

Include one section called:

- `What automation should not pretend to decide`
- `Motivating grounds`

## Anti-Misread Rules

- Do not assume the repo should implement full production DevOps immediately.
- Do not recommend automation for doctrine-sensitive judgment that requires explicit human or research-led review.
- Distinguish:
  - code verification
  - process enforcement
  - release safety
  - doctrinal integrity
