# 07 Spec Bundle Validation - Task Spec

## Purpose

Validate the multi-layer harness governance audit bundle before the actual audit lanes are launched.

This is a spec-quality and framing-quality check, not the substantive audit itself.

## Task Classification And Runtime

- classification: `initial architecture research/planning`
- recommended model: `gpt-5.4`
- recommended reasoning: `xhigh`

## Validation Question

Does the current spec bundle:

- trace each lane back to clear motivating grounds
- cover the user's broader ask without collapsing it into only repo-ops or only GSD
- avoid important scope gaps, ambiguity, or lane-overlap problems
- give future lane workers enough context to produce high-quality, repo-grounded outputs

## Validation Stance

Treat this as a skeptical quality gate, not a ratification exercise.

You are not being asked to approve the bundle unless it clearly earns approval.

Prefer this posture:

- try to find the strongest reasons the bundle might still be underframed, ambiguous, overlapping, or incomplete
- treat `not launch-ready` as a completely acceptable outcome if the evidence supports it
- do not protect the current bundle from criticism just because it already exists
- do not assume every current lane is necessary, properly split, or correctly scoped

## Required Reading

- `AGENTS.md`
- `.planning/AGENTS.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-task-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-task-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-task-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-task-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-task-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis-task-spec.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/LONG-ARC.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`

## Validation Criteria

Check at least:

1. `Motivating grounds traceability`
   - Does each lane clearly justify itself from user concerns and repo artifacts?
   - Is the broader ask preserved, not silently narrowed?

2. `Coverage`
   - Are any important layers or control levers missing?
   - Does the bundle really cover:
     - Codex
     - repo-local GSD
     - Git / repo ops
     - CI / release / deployment
     - cross-layer integration

3. `Lane separation`
   - Are responsibilities distinct enough to avoid mushy overlap?
   - Is any lane too broad or underframed?
   - Should any lane be merged, split differently, or removed?

4. `Reading sufficiency`
   - Will lane workers have enough repo-local context to work rigorously?
   - Are there critical files missing from required reading?

5. `Anti-misread quality`
   - Are the specs still vulnerable to the kinds of misreadings that already hurt earlier audit rounds?
   - Are loaded terms or boundaries still ambiguous?
   - Do the specs expose source-basis clearly enough to stop internal support from masquerading as external grounding?

6. `Synthesis readiness`
   - If the five lanes return, will the synthesis spec be able to answer the user's original broader question without guesswork?
7. `Bias check`
   - Does any wording in the bundle subtly push workers toward affirming the current frame instead of testing it?
   - Are there places where the specs assume the answer instead of investigating it?

## Required Output

Write:

- `.planning/research/2026-04-15-multilayer-harness-governance-audit/07-spec-bundle-validation-output.md`

Include:

- concise verdict:
  - `launch-ready`
  - `launch-ready with minor fixes`
  - `not launch-ready`
- findings ordered by severity
- exact spec gaps or ambiguities
- recommended fixes before launch
- explicit judgment on whether motivating-ground traceability is sufficient
- explicit judgment on whether source-basis exposure is sufficient

## Anti-Misread Rules

- Do not perform the substantive audit itself.
- Do not suggest widening scope casually.
- Do not act like the job is to endorse the current architecture of the bundle.
- Distinguish:
  - missing layer
  - missing file in reading list
  - lane overlap
  - wording ambiguity
  - merely optional nice-to-have
