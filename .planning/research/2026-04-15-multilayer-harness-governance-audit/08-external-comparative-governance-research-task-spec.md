# 08 External Comparative Governance Research - Task Spec

## Purpose

Run a targeted external-comparative research pass that tests the broader prescriptive claims emerging from:

- [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md)

This pass is not meant to re-diagnose the repo's internal current state. That internal diagnosis is already relatively strong.

Its job is to strengthen or weaken the more general governance recommendations by comparing them against direct outside evidence.

## Task Classification And Runtime

- classification: `initial architecture research/planning`
- recommended model: `gpt-5.4`
- recommended reasoning: `xhigh`

## Research Mode

Primary mode:

- `hypothesis testing`

Secondary mode if needed:

- `solution evaluation`

Reason:

- the main question is not "what exists in the repo?"
- it is "which of the governance recommendations in `06` survive stronger external comparison, and which remain only repo-specific reasoned judgment?"

## Core Question

Given the repo's multi-layer governance synthesis, what direct external evidence supports, weakens, qualifies, or contradicts the broader prescriptive claims about:

- where near-term controls should live
- how stronger controls should stage over time
- how long-horizon doctrine should be integrated into day-to-day workflow
- how much should be handled by upper-layer workflow/orchestration versus lower-layer automation

## Motivating Grounds

This pass is justified by three things:

1. the user explicitly challenged the recent audit bundle for relaxing the stronger source-basis standard established during the `05` audit
2. [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md) is strong on repo-state diagnosis, but weaker on externally grounded general prescription
3. the new signal:
   - [2026-04-15-citation-source-basis-enforcement-drift.md](/home/rookslog/workspace/projects/prix-guesser/.planning/knowledge/signals/prix-guesser/2026-04-15-citation-source-basis-enforcement-drift.md)
   records that this exact drift happened in the newer audit bundle

So this pass exists to answer:

- which parts of `06` are strongly supported as repo-internal diagnosis
- which parts are defensible but still mainly repo-specific reasoned recommendation
- which parts gain or lose strength when tested against direct external evidence

## Required Reading

### Current repo diagnosis and recommendations

- [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md)
- [01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md)
- [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md)
- [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md)
- [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md)
- [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md)
- [04-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md)

### Governing source-basis / claim-handling references

- [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md)
- [review-trail-framework.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md)
- `.codex/skills/gsd-rigorous-research/references/method.md`
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)

### Repo canon needed to keep comparison situated

- [.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)
- [.planning/PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
- [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
- [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)

## External Source Strategy

Prefer primary and high-quality sources in roughly this order:

1. official product or vendor docs
   - e.g. official Codex/OpenAI docs, official Git docs, official GitHub docs
2. official workflow / platform docs for tools actually relevant to the stack
3. direct engineering writeups, postmortems, or case studies from credible organizations using comparable agentic or automation-heavy workflows
4. strong technical references that clearly describe tradeoffs rather than generic “best practices”

Avoid or sharply discount:

- SEO-style best-practice blogs
- generic productivity content
- opinion pieces without operational detail
- sources that are not clearly analogous to this repo's scale or posture

## Claims Under Test

At minimum, test these claims from `06`:

1. near-term controls should live mostly in `Codex + GSD + Git`
2. CI should stay narrow for now and release/deploy should remain manual until a real runtime exists
3. stronger controls should escalate by:
   - risk
   - blast radius
   - parallelism
   - environment complexity
   rather than by project age or size alone
4. long-horizon quality depends on explicit handoff contracts between layers
5. the current repo's strongest surface is doctrine definition plus phase-local translation, while the weakest surface is lifecycle carry-forward and boundary materialization

You may add more if later reading shows another claim is equally load-bearing.

## Progressive Disclosure Rule

Yes, use progressive disclosure.

For this artifact:

- do **not** inline the full detailed ontology of claim types and source-basis markers
- do use a compact set of load-bearing inline markers where needed
- point to the durable deeper references above for the fuller semantics

Operationally:

- use the smallest inline notation that makes the epistemic status clear
- prefer the single-letter forms documented in `.planning/AGENTS.md` and `.planning/CLAIM-TYPES.md`, e.g. `[e:c:i]` or `[e:c:i+d]`
- reserve the fuller explanation for one short `Source-basis note` section or appendix

If the detailed references disagree or are uneven:

- prefer `.planning/CLAIM-TYPES.md` for the compact working notation
- prefer [review-trail-framework.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md) for source-basis distinctions
- treat `.codex/skills/gsd-rigorous-research/references/method.md` as useful but currently incomplete on source-basis

## Claim And Source-Basis Handling

For load-bearing claims, expose enough status to distinguish:

- repo-internal cited diagnosis
- external-direct support
- external-traceable support
- reasoned recommendation not yet strongly externally grounded

You do **not** need to mark every sentence.

But for major conclusions, do not let internal support read like external validation.

Minimum expected clarity:

- when a conclusion is mostly repo-state diagnosis, say so
- when a conclusion is strengthened by direct outside sources, say so
- when a conclusion remains mostly reasoned and repo-specific, say so

## Specific Questions

1. Which parts of `06` are already strong enough as internal repo diagnosis that external comparison mostly confirms rather than changes them?
2. Which parts of `06` are currently too internally reasoned to be treated as strong broader guidance?
3. What outside evidence supports or weakens the recommendation that near-term control should live mainly in upper layers rather than CI/deploy?
4. What outside evidence supports or weakens the recommendation to stage stronger controls by risk/blast radius/parallelism rather than repo size alone?
5. What outside evidence exists for integrating long-horizon doctrine into workflow/lifecycle rather than relying on memory or culture alone?
6. Are there externally supported alternative governance shapes that `06` underweighted or ignored?

## Output Requirements

Write:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md`

Required sections:

- `Research frame`
- `Motivating grounds`
- `Source strategy and exclusions`
- `Path of inquiry`
- `Claims under test from 06`
- `External findings`
- `Pressure against 06`
- `What survives strongly`
- `What weakens or remains only repo-specific judgment`
- `Source-basis and epistemic limits`
- `Implication for whether 06 needs revision`
- `Sources`

## Success Condition

At the end, a reader should be able to tell:

- which recommendations from `06` are solid enough to treat as externally strengthened
- which remain mainly internal/reasoned and should be treated more cautiously
- whether `06` itself needs revision, supplementation, or just clearer source-basis labeling

## Anti-Misread Rules

- Do not redo the whole multi-layer audit.
- Do not replace repo-specific judgment with imported generic “best practice” just because it is external.
- Do not assume official docs prove optimal governance; they may prove capability or supported mechanisms, not best overall practice.
- Do not silently flatten external source quality differences.
- Do not let the presence of outside sources create fake closure if the analogy to this repo is weak.
