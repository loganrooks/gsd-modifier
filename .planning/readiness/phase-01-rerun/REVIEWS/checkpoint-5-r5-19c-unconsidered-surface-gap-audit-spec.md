# Checkpoint 5 R5.19c Unconsidered / Under-Considered Surface Gap Audit Spec

This spec is the umbrella anchor for the `R5.19c` unconsidered / under-considered surface gap cluster.

Operational launch should not rely on one monolithic lane.

The family-split operational lanes are:

- `R5.19c1` skill / wrapper omitted-surface gap audit
- `R5.19c2` workflow omitted-surface gap audit
- `R5.19c3` reference / template omitted-surface gap audit
- `R5.19c4` bin / agent / overlay / runtime-control omitted-surface gap audit
- `R5.19c5` governance / readiness-authority omitted-surface gap audit

This umbrella spec defines the shared standard those family lanes must follow.

The original monolithic output target remains only as a possible later synthesis artifact, not the primary launch shape.

This lane asks a harder question than “which current exclusions are defensible?”

It asks:

- what files or surface families have not yet been meaningfully considered for modification at all
- which of those omissions matter most to Checkpoint 5 quality
- whether the current package is mistaking “not discussed” for “not relevant”

It is not a full inventory lane and not a patch plan.
It is the omitted-surface challenge lane.

One of its jobs is to catch files that are currently being treated as excluded without ever having been proven outside the relevant sphere of influence.

## Audit Stance

- post-verificationist
- post-falsificationist
- gap-exposure / completeness-challenge
- anti-regret

Biases to resist:

- assuming earlier audit family boundaries already cover the full relevant universe
- assuming that because a file was in the mapping, it was meaningfully considered
- scope inflation without consequence ranking
- treating “not part of the obvious chain” as equivalent to “not worth direct evaluation”

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
5. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
6. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
7. [AUDITS/checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
8. [AUDITS/checkpoint-3-workflow-harness-scope-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md)
9. [AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md)
10. [AUDITS/checkpoint-5-r5-19-broader-exclusion-and-modification-disposition-audit-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-19-broader-exclusion-and-modification-disposition-audit-bundle-spec.md)
11. [REVIEWS/checkpoint-5-r5-19a-full-surface-disposition-inventory-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19a-full-surface-disposition-inventory-audit-internal-r1.md) if available

## Candidate Gap Families

At minimum challenge these omitted-surface families:

- repo-local GSD files that appeared in mapping but never became direct Checkpoint 5 audit targets
- files currently classified only by family heuristic rather than direct reread
- wrapper-family or chain-tail-adjacent files that surfaced in one lane but were held out for production-condition or scope reasons
- adjacent governance/runtime-control files entangled with Checkpoint 5 but not clearly classified

## Questions

- Which surfaces have not been meaningfully considered for modification at all?
- Which of those omissions are benign, and which are now load-bearing?
- Which omitted surfaces matter because they sit on:
  - invocation boundaries
  - closure / routing boundaries
  - summary / reporting boundaries
  - doctrine propagation boundaries
- Which omitted surfaces matter because they are independently load-bearing even without a currently traced propagation dependency?
- Which omitted surfaces should be added to `R5.18` Bucket 2 or Bucket 3?
- Which omitted surfaces should instead become a separate later lane, and why?
- Which omitted surfaces are currently receiving de facto exclusion without any real proof that they lie outside the relevant sphere of influence?

## Output

Write:

- [checkpoint-5-r5-19c-unconsidered-surface-gap-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19c-unconsidered-surface-gap-audit-internal-r1.md)

Required sections:

1. `Summary`
2. `Strongest Omitted Surface Families`
3. `Concrete Files Not Yet Meaningfully Considered`
4. `Benign Omissions`
5. `Omissions That Must Feed R5.18`
6. `Omissions That Represent Independent-File Quality Opportunities`
7. `Omissions That Should Stay Separate`
8. `Read-Set Adequacy`
