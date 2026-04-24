# 05 Cross-Layer Integration And Escalation Audit - Task Spec

## Purpose

Audit how the different harness/governance layers should fit together:

- Codex orchestration
- repo-local GSD
- Git / repo-ops
- CI / release / deployment

The goal is to avoid both:

- under-specifying responsibilities so things drift
- overloading one layer with jobs that belong somewhere else

This lane should be launched only after the first four lane outputs exist.

## Core Question

Given the repo's actual needs, what responsibilities belong at each layer, what should be shared, and how should control escalate as project risk and complexity rise?

## Motivating Grounds

This lane exists because the user clarified that the real question is not only:

- “what should GSD do?”

but:

- what should happen at Codex level
- what should happen at GSD/workflow level
- what should happen at Git/repo-operations level
- what should happen at GitHub Actions / CI / deployment level

So this lane is the anti-collapse lane. Its job is to stop the broader audit from quietly turning back into a single-layer answer.

Primary grounds:

- the user's explicit request to think across “different levels and modes of harness”
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- the control and governance docs already present in the repo

## Required Reading

- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/LONG-ARC.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- the launch bundle spec for this audit
- the other lane specs in this bundle
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`

You may also consult current runtime/harness/config files as needed, but this lane should stay integration-focused.

## Specific Questions

1. Which problems should be solved primarily at:
   - Codex instruction/orchestration level
   - GSD workflow/skill level
   - Git/repo-operations level
   - CI/release/deployment level
2. Which problems require layered support rather than single-layer ownership?
3. How should the repo think about:
   - early-stage controls
   - middle-stage controls
   - later high-risk controls
4. How should `LONG-ARC.md` and future-aware doctrine move through all four layers without becoming ambient or redundant?
5. What escalation model is best:
   - warnings
   - visible workflow gates
   - required artifacts
   - helper commands
   - branch/worktree separation
   - CI enforcement
   - release/deploy controls

## Output Requirements

Write:

- a control-surface map by layer
- a responsibility matrix
- escalation guidance by risk/scale/complexity
- recommended near-term integrated roadmap
- anti-patterns to avoid

Include one section called:

- `What should live where`
- `Motivating grounds`

## Anti-Misread Rules

- Do not produce a generic enterprise governance memo.
- Do not assume the answer is “add automation everywhere.”
- Do not ignore the repo's current stage; the answer should be staged, not timelessly maximalist.
