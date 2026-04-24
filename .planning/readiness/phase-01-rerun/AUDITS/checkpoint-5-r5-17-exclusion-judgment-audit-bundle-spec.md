# Checkpoint 5 R5.17 Exclusion-Judgment Audit Bundle Spec

This bundle exists to challenge prior scope-exclusion judgments, especially those produced by earlier `gpt-5.4` lanes, before Checkpoint 5 proceeds on the assumption that those exclusions were sound.

It is not a generic harness audit and not a generic “review the reviews” pass.

Its job is narrower and harsher:

1. identify the exclusion heuristics that were actually used
2. test whether those heuristics were justified or merely convenient
3. inspect the excluded surfaces directly rather than trusting prior exclusion summaries
4. compare the exclusion-audit lanes without flattening their tensions
5. reread that comparison before any new exclusion judgment is allowed to govern scope

## Why Split The Bundle

One blob exclusion audit would be too weak.

The earlier exclusion logic did not operate in one place or one form. It appeared across different surface families:

- wrapper / invocation-surface exclusions
- chain-tail / representation / downstream-consumer exclusions
- doctrine / governance / naming / “not runtime-authoritative” exclusions

Those families fail differently and require different read sets.

So `R5.17` is split into:

- `R5.17a` wrapper-exclusion audit
- `R5.17b` chain-tail / representation exclusion audit
- `R5.17c` governance / doctrine exclusion audit
- `R5.17d` adjudication of the three exclusion lanes
- `R5.17e` reread of that adjudication

## Governing Inputs

Read these before any lane-specific work:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md)
4. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
5. [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
6. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
7. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
8. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
9. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
10. [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
11. [AUDIT-SPEC-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-SPEC-TEMPLATE.md)
12. [AUDITS/checkpoint-4-cross-lane-seam-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md)
13. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
14. [REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md)
15. [REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-opus-r1.md)
16. [REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md)
17. [REVIEWS/checkpoint-5-r5-16d-adjudication-reread-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-cross-vendor-opus-r1.md)

## Exclusion Heuristics Under Audit

The bundle should treat these as burden-bearing claims, not as neutral defaults:

- `thin wrapper`
- `only a wrapper`
- `only a mapper`
- `secondary alignment surface`
- `not runtime-authoritative`
- `not the primary seam`
- `local, not wider`
- `can remain deferred`
- `just naming`
- `just prompt language`
- `not yet forced by evidence`

The question is not whether these phrases can ever be true.

The question is whether they were justified in the specific exclusions they were used to support, under the repo’s anti-regret and best-possible-outcome standard.

## Lanes

### `R5.17a`

- spec: [checkpoint-5-r5-17a-wrapper-exclusion-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-audit-spec.md)
- cross-vendor prompt: [checkpoint-5-r5-17a-wrapper-exclusion-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-cross-vendor-prompt.md)
- focus: wrapper / invocation-surface exclusions

### `R5.17b`

- spec: [checkpoint-5-r5-17b-chain-tail-exclusion-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17b-chain-tail-exclusion-audit-spec.md)
- cross-vendor prompt: [checkpoint-5-r5-17b-chain-tail-exclusion-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17b-chain-tail-exclusion-cross-vendor-prompt.md)
- focus: chain-tail / representation / downstream-consumer exclusions

### `R5.17c`

- spec: [checkpoint-5-r5-17c-governance-exclusion-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17c-governance-exclusion-audit-spec.md)
- cross-vendor prompt: [checkpoint-5-r5-17c-governance-exclusion-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17c-governance-exclusion-cross-vendor-prompt.md)
- focus: doctrine / governance / naming / “not operative enough” exclusions

### `R5.17d`

- spec: [checkpoint-5-r5-17d-exclusion-adjudication-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17d-exclusion-adjudication-spec.md)
- cross-vendor prompt: [checkpoint-5-r5-17d-exclusion-adjudication-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17d-exclusion-adjudication-cross-vendor-prompt.md)
- focus: compare the three exclusion-audit lanes and determine which exclusions fail, which survive, and which remain contested

### `R5.17e`

- spec: [checkpoint-5-r5-17e-exclusion-adjudication-reread-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-spec.md)
- cross-vendor prompt: [checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-prompt.md)
- focus: challenge the adjudication before its new exclusion consequences govern next edits

## Standing Rules

- Do not treat exclusion as a neutral default.
- Do not treat a surface as safely excludable merely because it is small, indirect, or mostly declarative.
- If a surface is a first-invoked or first-read surface, the burden of exclusion is higher.
- If a surface shapes status vocabulary, routing authority, or what the harness claims it is doing, the burden of exclusion is higher.
- If a prior lane excluded a surface based on a heuristic phrase, the audit should test the phrase against the file itself.
- If a lane concludes that a surface should remain excluded, it must justify:
  - why exclusion is still compatible with the best-possible-outcome standard
  - why exclusion will not knowingly export avoidable audit pain, doctrine drift, or quality loss

## Expected Outputs

- [checkpoint-5-r5-17a-wrapper-exclusion-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-audit-internal-r1.md)
- [checkpoint-5-r5-17a-wrapper-exclusion-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-cross-vendor-opus-r1.md)
- [checkpoint-5-r5-17b-chain-tail-exclusion-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17b-chain-tail-exclusion-audit-internal-r1.md)
- [checkpoint-5-r5-17b-chain-tail-exclusion-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17b-chain-tail-exclusion-cross-vendor-opus-r1.md)
- [checkpoint-5-r5-17c-governance-exclusion-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17c-governance-exclusion-audit-internal-r1.md)
- [checkpoint-5-r5-17c-governance-exclusion-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17c-governance-exclusion-cross-vendor-opus-r1.md)
- [checkpoint-5-r5-17d-exclusion-adjudication-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17d-exclusion-adjudication-internal-r1.md)
- [checkpoint-5-r5-17d-exclusion-adjudication-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17d-exclusion-adjudication-cross-vendor-opus-r1.md)
- [checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md)
- [checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-r1.md)
