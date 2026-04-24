# Checkpoint 5 R5.17b Chain-Tail Exclusion Audit Spec

Purpose: challenge prior exclusion judgments that kept chain-tail, representation, routing, and downstream-consumer surfaces out of active Checkpoint 5 scope or treated them as merely later consequences.

This is a direct seam audit of exclusion logic, not a general chain-tail remap.

## Audit Stance

- post-verificationist
- post-falsificationist
- gap-exposure / completeness-challenge
- anti-regret
- very critical toward prior exclusion judgments from earlier `gpt-5.4` lanes

Biases to resist:

- producer-surface privilege
- “not the primary seam” laziness
- deferral-by-distance
- under-reading representation / summary / routing surfaces
- treating downstream distortion as secondary rather than load-bearing

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
5. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
6. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
7. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
8. [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
9. [AUDIT-SPEC-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-SPEC-TEMPLATE.md)
10. [AUDITS/checkpoint-4-cross-lane-seam-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md)
11. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
12. [REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md)
13. [REVIEWS/checkpoint-5-r5-16b-track-c-propagation-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-cross-vendor-opus-r1.md)
14. [REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md)
15. [REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-opus-r1.md)

## Candidate Exclusion Targets

1. [.codex/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md)
2. [.codex/get-shit-done/references/verification-overrides.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/verification-overrides.md)
3. [.codex/get-shit-done/references/checkpoints.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/checkpoints.md)
4. [.codex/get-shit-done/bin/lib/phase.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/phase.cjs)
5. [.codex/get-shit-done/bin/lib/roadmap.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/roadmap.cjs)
6. [.codex/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md)
7. [.codex/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md)
8. [.codex/get-shit-done/workflows/ship.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ship.md)
9. [.codex/get-shit-done/workflows/autonomous.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/autonomous.md)
10. [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml)
11. [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml)

## Questions

- Which prior exclusions of chain-tail or representation surfaces were invalid?
- Which earlier `gpt-5.4` lanes treated downstream consumers as secondary when they were actually routing authority or closure authority?
- Which exclusions relied on values like simplicity or boundedness without showing why exclusion still served the best possible outcome?
- Which surfaces should now be treated as presumptive edit targets because exclusion would knowingly export cheap-closure semantics downstream?
- Which surfaces, if any, still remain defensible exclusions, and on what evidence?
- Did earlier internal lanes under-read the significance of representation/routing surfaces by privileging producer-side doctrine?
- Read-set adequacy question:
  - are there chain-tail or representation surfaces still missing from this lane that would materially alter the exclusion judgment?

## Output

Write:
- [checkpoint-5-r5-17b-chain-tail-exclusion-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17b-chain-tail-exclusion-audit-internal-r1.md)

Include sections:
- invalid exclusions
- under-justified exclusions
- defensible exclusions
- presumptive edit targets
- mandatory disposition targets
- direct spot checks
- package consequences
