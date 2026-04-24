# Checkpoint 5 R5.16 Propagation-Audit Bundle Spec

This bundle exists to test whether the active Track B / Track C candidate changes are genuinely local and sufficient, or whether they expose a wider harness/governance lane that should be promoted before Checkpoint 5 can close.

It is not a generic “review the dirty files” pass. It is a post-verificationist / post-falsificationist propagation and anti-regret bundle that:

1. audits Track B review-consumer propagation
2. audits Track C launch-truth / closure-consumer propagation
3. adjudicates whether the surviving gaps are local or wider
4. rereads that adjudication so the orchestrator’s locality judgment does not stand unchallenged

## Why Split The Bundle

- The active candidate bundle currently combines two different seam families:
  - review / closure-pressure propagation
  - launch-truth / debt-carrying-completion propagation
- Those families can fail differently.
- Splitting by seam is therefore more rigorous than one blur lane.
- The split is not by model/vendor. Each seam lane can still be read by both:
  - internal `gpt-5.4 xhigh`
  - cross-vendor `Claude Opus`
- The adjudication should then compare the seam-lane findings and explicitly test both:
  - whether wider promotion is warranted
  - whether non-promotion is genuinely defensible under an anti-regret quality standard

## Governing Inputs

Read these before any lane-specific work:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md)
4. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
5. [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
6. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
7. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
8. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
9. [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
10. [AUDITS/checkpoint-4-cross-lane-seam-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md)
11. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
12. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)

## Lanes

### `R5.16a`

- spec: [checkpoint-5-r5-16a-track-b-propagation-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16a-track-b-propagation-audit-spec.md)
- cross-vendor prompt: [checkpoint-5-r5-16a-track-b-propagation-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16a-track-b-propagation-cross-vendor-prompt.md)
- focus: review / closure-pressure propagation into real review consumers

### `R5.16b`

- spec: [checkpoint-5-r5-16b-track-c-propagation-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-spec.md)
- cross-vendor prompt: [checkpoint-5-r5-16b-track-c-propagation-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-cross-vendor-prompt.md)
- focus: launch-truth, closure-status, and debt-carrying-completion propagation into real consumers

### `R5.16c`

- spec: [checkpoint-5-r5-16c-anti-regret-adjudication-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-spec.md)
- cross-vendor prompt: [checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-prompt.md)
- focus: anti-regret adjudication of `a` and `b`, explicitly testing both promotion and non-promotion

### `R5.16d`

- internal reread spec: [checkpoint-5-r5-16d-adjudication-reread-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-spec.md)
- cross-vendor reread prompt: [checkpoint-5-r5-16d-adjudication-reread-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-cross-vendor-prompt.md)
- focus: challenge the adjudication itself before its scope judgment can govern next moves

## Standing Rules

- Do not let `R5.16a` or `R5.16b` implicitly settle whether the issue is local or wider. That is `R5.16c`’s job.
- Do not let `R5.16c` implicitly settle scope alone. That adjudication must itself be reread through `R5.16d`.
- `R5.17` should not be promoted only because widening feels safer.
- `R5.17` should also not be withheld merely because keeping scope local is cheaper.
- The right standard is anti-regret:
  - does wider promotion solve a real under-owned problem?
  - is non-promotion genuinely defensible without leaving likely quality gains or anomaly-accounting work on the table?

## Expected Outputs

- [checkpoint-5-r5-16a-track-b-propagation-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16a-track-b-propagation-audit-internal-r1.md)
- [checkpoint-5-r5-16a-track-b-propagation-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16a-track-b-propagation-cross-vendor-opus-r1.md)
- [checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md)
- [checkpoint-5-r5-16b-track-c-propagation-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-cross-vendor-opus-r1.md)
- [checkpoint-5-r5-16c-anti-regret-adjudication-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md)
- [checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-opus-r1.md)
- [checkpoint-5-r5-16d-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md)
- [checkpoint-5-r5-16d-adjudication-reread-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-cross-vendor-opus-r1.md)
