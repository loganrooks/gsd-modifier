# Checkpoint 5 R5.19a Full Surface Disposition Inventory Audit Spec

This spec is the umbrella anchor for the `R5.19a` full-surface disposition inventory cluster.

Operational launch should not rely on one monolithic lane.

The family-split operational lanes are:

- `R5.19a1` skill / wrapper disposition inventory
- `R5.19a2` workflow disposition inventory
- `R5.19a3` reference / template disposition inventory
- `R5.19a4` bin / agent / overlay / runtime-control disposition inventory
- `R5.19a5` governance / readiness-authority disposition inventory

This umbrella spec defines the shared standard those family lanes must follow.

The original monolithic output target remains only as a possible later synthesis artifact, not the primary launch shape.

It inventories the broader repo-local GSD and adjacent governance surface so the package can say, file by file, what is currently under modification consideration for Checkpoint 5 and what is not.

It is not a patch plan.
It is not an exclusion-justification lane by itself.
It is the inventory and classification lane that later lanes will challenge.

Exclusion is not the default success state of this inventory.

If a file cannot yet be shown to be outside the relevant sphere of influence, do not classify it as `preserved_exclusion`.

## Audit Stance

- post-verificationist
- post-falsificationist
- gap-exposure / completeness-challenge
- anti-regret

Biases to resist:

- assuming current `R5.18` buckets are already the whole relevant universe
- treating category-level exclusion as enough without file-level classification
- mistaking prior silence for defensible exclusion
- omitting files because they feel secondary or familiar

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
5. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
6. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
7. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
8. [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
9. [AUDITS/checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
10. [AUDITS/checkpoint-3-workflow-harness-scope-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md)
11. [AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md)
12. [REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md)
13. [REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md)
14. [AUDITS/checkpoint-5-r5-19-broader-exclusion-and-modification-disposition-audit-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-19-broader-exclusion-and-modification-disposition-audit-bundle-spec.md)

## Surface Families To Inventory

Inventory every file under:

1. `.codex/skills/`
2. `.codex/get-shit-done/workflows/`
3. `.codex/get-shit-done/references/`
4. `.codex/get-shit-done/templates/`
5. `.codex/get-shit-done/bin/lib/`
6. `.codex/agents/`
7. `tooling/portable-gsd/overlay/agents/`

Also inventory the adjacent governance/runtime-control files that already bear on Checkpoint 5 scope:

8. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
9. [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
10. [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)
11. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
12. [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md)
13. [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml)
14. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)

## Required Classification Labels

Every inventoried file must receive exactly one current disposition label:

- `first_wave_r5_18`
- `mandatory_explicit_disposition`
- `scope_gating_only`
- `governing_authority_not_edit_now`
- `preserved_exclusion`
- `qualified_pressure_only`
- `outside_checkpoint_5`
- `not_yet_meaningfully_considered`

For each file, also record:

- current basis or rationale
- whether the rationale is explicit or inferred
- whether the file was directly challenged in `R5.17`
- whether its relevance is:
  - `propagation_linked`
  - `independent_surface`
  - `both`
- whether current exclusion, if any, is actually proven
- confidence level

## Questions

- What is the full current file-level modification-consideration map for Checkpoint 5?
- Which files are currently excluded from modification consideration because `R5.18` does not name them?
- Which files are excluded by explicit rationale, and which are excluded only by inheritance or omission?
- Which files matter because they are part of a propagation / contract chain?
- Which files matter because they are independently load-bearing even if they are not obvious downstream consumers of another changed file?
- Which files are currently treated as governing authority instead of patch targets, and why?
- Which files have not yet been meaningfully considered at all?
- Are there important files outside the current `R5.18` buckets that should obviously be in Bucket 2 or Bucket 3?
- Is the current package using a category label like `thin wrapper`, `governing only`, or `outside current seam` to do file-level exclusion work it has not earned?
- For each file currently treated as excluded, what is the concrete proof that it lies outside the relevant sphere of influence?

## Output

Write:

- [checkpoint-5-r5-19a-full-surface-disposition-inventory-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19a-full-surface-disposition-inventory-audit-internal-r1.md)

Required sections:

1. `Summary`
2. `Method And Read Coverage`
3. `Disposition Counts By Surface Family`
4. `Full Disposition Inventory`
5. `Files Currently Excluded From Modification Consideration`
6. `Files Not Yet Meaningfully Considered`
7. `Strongest Misclassification Risks`
8. `Read-Set Adequacy`

In `Full Disposition Inventory`, use a table with at least:

- path
- family
- current disposition
- basis
- explicit_or_inferred
- directly_challenged_in_r5_17
- relevance_mode
- exclusion_proven
- confidence

## Anti-Misread Rule

Do not silently narrow the inventory to files already mentioned in `R5.18`.

If the audit cannot meaningfully classify a file, label it `not_yet_meaningfully_considered` rather than forcing it into a cleaner category.

If a file is currently excluded but the evidence for exclusion is weak, inherited, or absent, do not clean it up by calling it `preserved_exclusion`.
Use `not_yet_meaningfully_considered`, `qualified_pressure_only`, or `mandatory_explicit_disposition` instead.
