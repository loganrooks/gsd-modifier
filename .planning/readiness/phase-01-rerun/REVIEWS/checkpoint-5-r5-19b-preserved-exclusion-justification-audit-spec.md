# Checkpoint 5 R5.19b Preserved-Exclusion Justification Audit Spec

This artifact is the umbrella burden spec for the `R5.19b` exclusion-justification cluster.

Operational launch should use narrower family-split lanes (`R5.19b1...R5.19b5`) rather than one monolithic pass, unless a later adjudication explicitly wants a whole-cluster reread.

The cluster directly challenges the current preserved exclusions, later-checkpoint deferrals, and outside-phase judgments that keep files out of active Checkpoint 5 modification consideration.

It is not a full-surface inventory lane.
It is not a patch plan.
It is the exclusion-burden umbrella spec.

It should assume by default that exclusion is difficult to justify once a file either:

- carries a live propagation / contract consequence, or
- is independently load-bearing enough that leaving it unexamined can leave real quality gains on the table

The burden of proof is on exclusion / non-modification.

For an exclusion to survive, the audit should require the defending case to prove:

1. the file is outside the relevant sphere of influence, or
2. leaving it untouched in this phase sacrifices no material quality gain worth owning now

If neither case can be shown, the exclusion should fail or be downgraded to a non-clean status such as `mandatory explicit disposition` or `not yet meaningfully considered`.

No exclusion survives here on category reasoning alone.

To defend a surviving exclusion, the lane must cite:

1. the file itself
   - where its own semantics, role, or content indicate low or bounded relevance
2. the exclusion source
   - where the package, spec, or rule is currently excluding or deferring it
3. the consequence argument
   - why leaving it untouched does not materially distort the current checkpoint

## Audit Stance

- post-verificationist
- post-falsificationist
- gap-exposure / completeness-challenge
- anti-regret

Biases to resist:

- treating “later lane” as a sufficient reason by itself
- reusing older anti-omnibus doctrine as if it were still sovereign after `R5.17`
- defending exclusions with category language instead of file-line grounding
- scope-inflation by attacking every exclusion equally without consequence analysis
- forgetting the independent-file question because a file is not obviously in a propagation chain

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
5. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
6. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
7. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
8. [AUDITS/checkpoint-5-reactivated-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-reactivated-launch-spec.md)
9. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
10. [AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md)
11. [OPPORTUNITIES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/OPPORTUNITIES.md)
12. [AUDITS/checkpoint-5-r5-19-broader-exclusion-and-modification-disposition-audit-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-19-broader-exclusion-and-modification-disposition-audit-bundle-spec.md)

## Candidate Exclusion Sources

Challenge at least these exclusion sources directly:

- `R5.18` Bucket 5 preserved exclusions and qualified pressure
- `R5.18` Bucket 4 governing-authority-not-edit-now judgments
- `R5.7` / `R5.8` / `R5.9` / `R5.10` conditionals where they function as current non-modification decisions
- the reactivated anti-omnibus rule against exhaustive skill-family audit
- the implementation spec’s explicit non-goals around omnibus skill-family audit, broader branch/worktree redesign, provenance hardening, and path portability

## Direct Spot-Check Surfaces

This lane must directly inspect the files it is judging, not only the artifacts that excluded them.

At minimum it should directly inspect:

- `.codex/skills/gsd-discuss-phase/SKILL.md`
- `.codex/skills/gsd-autonomous/SKILL.md`
- `.codex/skills/gsd-ship/SKILL.md`
- `.codex/skills/gsd-progress/SKILL.md`
- `.codex/get-shit-done/workflows/discuss-phase.md`
- `.codex/get-shit-done/workflows/autonomous.md`
- `.codex/get-shit-done/workflows/ship.md`
- `.codex/get-shit-done/workflows/progress.md`
- `.codex/get-shit-done/references/checkpoints.md`
- any portability / branch-worktree / launch-truth surface the current package is treating as preserved exclusion

If the lane defends additional exclusions beyond this starter set, it must directly inspect those files too.

## Questions

- Which current exclusions are positively defensible?
- Which exclusions are under-justified or stale products of earlier narrowing doctrine?
- Which files are being kept out of modification consideration by category labels rather than direct evidence?
- Which “later lane” deferrals are honest, and which are really active non-modification decisions that now need stronger defense?
- Which exclusions can remain outside `R5.18` even if `R5.19` becomes active?
- Which exclusions should now move into `R5.18` Bucket 2 or Bucket 3?
- For each load-bearing exclusion judgment, what is the direct evidence for exclusion?
- For each load-bearing exclusion judgment, what is the propagation / interconnection consequence of keeping it out?
- For each load-bearing exclusion judgment, what is the independent-file case for evaluating or modifying it even if no upstream change directly forces it?
- What meaningful quality gains would be left on the table by preserving the exclusion?
- If the exclusion is still defended anyway, why is that loss acceptable at this stage?
- Has the defending case actually proved the file lies outside the relevant sphere of influence, or is it relying on habit, prior narrowing, or category language?

## Output

Write:

- [checkpoint-5-r5-19b-preserved-exclusion-justification-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b-preserved-exclusion-justification-audit-internal-r1.md)

Required sections:

1. `Summary`
2. `Exclusion Judgments That Survive`
3. `Exclusion Judgments That Fail`
4. `Under-Justified Exclusions`
5. `Files That Must Move Into Active Consideration`
6. `Files That Can Stay Out, With Reasons`
7. `Potential Quality Gains Currently Left On The Table`
8. `Read-Set Adequacy`

For each exclusion judgment discussed in sections 2-6, explicitly distinguish:

- `propagation-level case`
- `independent-file case`
- `sphere-of-influence proof`
- `direct file-line evidence from the excluded file`
- `direct file-line evidence from the exclusion source`

Do not treat absence of one as proof of absence of the other.
