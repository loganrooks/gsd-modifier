# Checkpoint 5 R5.17a Wrapper-Exclusion Audit Spec

Purpose: challenge prior exclusion judgments that kept wrapper / invocation surfaces out of active Checkpoint 5 scope or treated them as low-consequence alignment surfaces.

This is a direct seam audit of exclusion logic, not a general wrapper refresh.

## Audit Stance

- post-verificationist
- post-falsificationist
- gap-exposure / completeness-challenge
- anti-regret
- very critical toward prior exclusion judgments from earlier `gpt-5.4` lanes

Biases to resist:

- wrapper-dismissal bias
- “thin mapper” laziness
- scope-conservative defaulting
- over-tidiness that turns “inspect carefully” into “leave untouched”
- false confidence that deeper workflow fixes automatically clear first-invoked surfaces

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
5. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
6. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
7. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
8. [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
9. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
10. [REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md)
11. [REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-opus-r1.md)
12. [REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md)
13. [REVIEWS/checkpoint-5-r5-16d-adjudication-reread-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-cross-vendor-opus-r1.md)

## Prior Exclusion Artifacts Under Audit

Read these as objects of critique, not as governing truth:

1. [REVIEWS/checkpoint-5-r5-16a-track-b-propagation-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16a-track-b-propagation-audit-internal-r1.md)
2. [REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md)
3. [REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md)
4. [REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md)

## Candidate Exclusion Targets

1. [.codex/skills/gsd-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md)
2. [.codex/skills/gsd-plan-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-plan-phase/SKILL.md)
3. [.codex/skills/gsd-execute-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-execute-phase/SKILL.md)
4. [.codex/skills/gsd-verify-work/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-verify-work/SKILL.md)
5. [.codex/skills/gsd-discuss-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md)
6. [.codex/skills/gsd-research-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-research-phase/SKILL.md)

## Live / Downstream Consumers

1. [.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md)
2. [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md)
3. [.codex/get-shit-done/workflows/execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md)
4. [.codex/get-shit-done/workflows/verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md)
5. [.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md)
6. [.codex/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md)

## Questions

- Which prior wrapper exclusions relied mainly on heuristic phrases like `thin wrapper`, `only a mapper`, or `secondary alignment surface`?
- For each such exclusion, what actual values was the exclusion protecting:
  - evidence discipline
  - anti-sprawl
  - cost control
  - false-authority avoidance
  - something else?
- Did the earlier `gpt-5.4` reasoning justify why exclusion would still lead toward the best possible outcome, or did it justify only why exclusion was administratively cheaper or cleaner?
- Which wrappers are first-invoked or expectation-setting enough that exclusion should have required stronger justification than it received?
- Which wrappers are still carrying weaker execution / completion / review / closure posture at the invocation layer even if the deeper workflow is stronger?
- Which wrappers should be treated as:
  - presumptive edit targets
  - mandatory explicit-disposition targets
  - genuinely defensible exclusions
- Where did earlier internal lanes under-read wrapper significance because they treated invocation framing as less operative than runtime logic?
- Are there wrapper surfaces whose exclusion would knowingly export doctrine lag or user/orchestrator misframing into the rerun?
- Read-set adequacy question:
  - are there rerun-critical wrappers missing from this lane’s read set whose omission would materially weaken the exclusion judgment?

## Output

Write:
- [checkpoint-5-r5-17a-wrapper-exclusion-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-audit-internal-r1.md)

Include sections:
- exclusion heuristics found
- invalid exclusions
- under-justified exclusions
- defensible exclusions
- presumptive edit targets
- mandatory disposition targets
- open questions
- direct file-line spot checks
