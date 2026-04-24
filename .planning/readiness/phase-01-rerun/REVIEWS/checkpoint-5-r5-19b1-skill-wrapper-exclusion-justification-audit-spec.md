# Checkpoint 5 R5.19b1 Skill / Wrapper Exclusion-Justification Audit Spec

This lane proves or disproves current exclusion / non-modification judgments for repo-local skill and wrapper surfaces relevant to Checkpoint 5.

It is not a patch plan.
It is not the whole `R5.19b` cluster.
It is the skill / wrapper exclusion-proof lane.

## Audit Stance

- post-verificationist
- post-falsificationist
- gap-exposure / completeness-challenge
- anti-regret

Exclusion burden:

- the burden of proof is on non-modification
- a wrapper or skill should not remain excluded just because it is called `thin`, `summary-only`, or `secondary`

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
5. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
6. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
7. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
8. [REVIEWS/checkpoint-5-r5-19b-preserved-exclusion-justification-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b-preserved-exclusion-justification-audit-spec.md)
9. [AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md)

## Candidate Surfaces

- `.codex/skills/gsd-discuss-phase/SKILL.md`
- `.codex/skills/gsd-autonomous/SKILL.md`
- `.codex/skills/gsd-ship/SKILL.md`
- `.codex/skills/gsd-progress/SKILL.md`
- `.codex/skills/gsd-execute-phase/SKILL.md`
- `.codex/skills/gsd-verify-work/SKILL.md`
- `.codex/skills/gsd-research-phase/SKILL.md`
- `.codex/skills/gsd-review/SKILL.md`
- `.codex/skills/gsd-plan-phase/SKILL.md`

## Direct Spot-Check Workflow Surfaces

- `.codex/get-shit-done/workflows/discuss-phase.md`
- `.codex/get-shit-done/workflows/autonomous.md`
- `.codex/get-shit-done/workflows/ship.md`
- `.codex/get-shit-done/workflows/progress.md`
- `.codex/get-shit-done/workflows/execute-phase.md`
- `.codex/get-shit-done/workflows/verify-work.md`
- `.codex/get-shit-done/workflows/research-phase.md`
- `.codex/get-shit-done/workflows/review.md`
- `.codex/get-shit-done/workflows/plan-phase.md`

## Questions

- Which wrapper / skill exclusions survive?
- Which fail?
- Which wrappers are outside the relevant sphere of influence?
- Which wrappers are independently load-bearing even without a traced propagation chain?
- Which wrappers would leave real quality gains on the table if kept out?

## Output

Write:

- [checkpoint-5-r5-19b1-skill-wrapper-exclusion-justification-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b1-skill-wrapper-exclusion-justification-audit-internal-r1.md)

Required sections:

1. `Summary`
2. `Exclusions That Survive`
3. `Exclusions That Fail`
4. `Wrappers That Must Move Into Active Consideration`
5. `Potential Quality Gains Left On The Table`
6. `Read-Set Adequacy`

For each judgment, include:

- propagation-level case
- independent-file case
- sphere-of-influence proof
- direct file-line evidence from the excluded file
- direct file-line evidence from the exclusion source
