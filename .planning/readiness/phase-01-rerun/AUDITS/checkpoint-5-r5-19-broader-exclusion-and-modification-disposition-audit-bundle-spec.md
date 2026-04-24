# Checkpoint 5 R5.19 Broader Exclusion / Modification-Consideration Audit Bundle Spec

This bundle exists to answer a broader question than `R5.18`.

`R5.18` decides the corrective patch frontier for the current Checkpoint 5 wave.
`R5.19` challenges the broader perimeter that `R5.18` would otherwise inherit:

- what repo-local GSD and adjacent governance surfaces are currently excluded from modification consideration for this phase
- why they are excluded
- whether those exclusions are defensible, under-justified, merely habitual, or not even yet consciously made

This bundle is not a patch plan.
It is not a fallback inside `R5.18`.
It is a precursor / parallel challenge bundle whose outputs must be available before the final `R5.18` implementation boundary hardens.

The core burden in `R5.19` is not merely:

- "what else exists?"

It is:

- "what is currently excluded from modification consideration?"
- "what is the real evidence for that exclusion?"
- "does the exclusion survive both propagation-level and independent-surface scrutiny?"
- "does the exclusion leave meaningful quality gains on the table?"

## Exclusion Burden Rule

Exclusion is not a neutral default in this bundle.

The burden of proof is on non-modification.

To keep a file out of active modification consideration for Checkpoint 5, the package must be able to show at least one of these with direct evidence:

1. the file is outside the relevant sphere of influence
   - it is not materially implicated by propagation / contract / routing / invocation / summary consequences
   - and it is not independently load-bearing enough to warrant direct evaluation against current standards
2. the file may be relevant, but leaving it untouched in this phase does not sacrifice material quality
   - the lost quality gains are minor, bounded, and explicitly accepted
   - the owner and reopen trigger are named

If the package cannot make one of those cases, the file should not remain a clean exclusion.

It must instead be treated as one of:

- `mandatory explicit disposition`
- `scope-gating only`
- `qualified pressure only`
- `not yet meaningfully considered`

## Audit Stance

- post-verificationist
- post-falsificationist
- gap-exposure / completeness-challenge
- anti-regret

Biases this bundle must resist:

- boundedness bias masquerading as evidence
- omnibus-sprawl bias masquerading as rigor
- inherited-exclusion bias
- file-familiarity bias
- pass/fail closure bias
- treating `not currently patched` as equivalent to `defensibly excluded`

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
11. [AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md)
12. [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
13. [AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md)
14. [REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md)
15. [REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md)

## Surface Universe

The bundle should treat the following as the default audit universe for modification-consideration questions:

- `.codex/skills/`
- `.codex/get-shit-done/workflows/`
- `.codex/get-shit-done/references/`
- `.codex/get-shit-done/templates/`
- `.codex/get-shit-done/bin/lib/`
- `.codex/agents/`
- `tooling/portable-gsd/overlay/agents/`
- repo-level governance or runtime-control surfaces already entangled with Checkpoint 5:
  - [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
  - [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
  - [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)
- readiness governance surfaces when they are being used as reasons to exclude edits:
  - [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
  - [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md)
  - [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml)
  - [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)

The bundle must not silently narrow this universe to only current `R5.18` files.

## Bundle Lanes

### `R5.19b` Preserved-Exclusion / Outside-Phase Justification Audit Cluster

Purpose:

- directly challenge the current preserved exclusions, later-checkpoint deferrals, and outside-phase judgments
- determine which exclusions are defensible, which are under-justified, and which are currently invalid

Priority:

- This is the first burden-bearing cluster in the bundle.
- The user has explicitly promoted the broader question as an exclusion-burden challenge, not merely an inventory exercise.
- Because proving exclusion is intensive, operational launch should split this cluster by surface family rather than rely on one monolithic lane.

Operational split:

- `R5.19b1` skill / wrapper exclusion-justification audit
- `R5.19b2` workflow exclusion-justification audit
- `R5.19b3` reference / template exclusion-justification audit
- `R5.19b4` bin / agent / overlay / runtime-control exclusion-justification audit
- `R5.19b5` governance / readiness-authority / conditional-lane exclusion-justification audit

Umbrella anchor:

- [checkpoint-5-r5-19b-preserved-exclusion-justification-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b-preserved-exclusion-justification-audit-spec.md)

### `R5.19a` Full Surface Disposition Inventory Audit Cluster

Purpose:

- inventory the relevant repo-local GSD and adjacent governance surfaces
- classify each file's current modification-consideration status for Checkpoint 5
- make explicit whether the file is:
  - in first-wave corrective scope
  - mandatory explicit disposition
  - scope-gating only
  - governing-only / authority-not-edit-now
  - preserved exclusion
  - qualified pressure
  - outside Checkpoint 5
  - not yet meaningfully considered

Priority:

- This cluster should run in parallel with the `R5.19b` hard-exclusion cluster.
- File-level disposition inventory across the mapped surface is too large to treat as one monolithic lane without lowering rigor.

Operational split:

- `R5.19a1` skill / wrapper disposition inventory
- `R5.19a2` workflow disposition inventory
- `R5.19a3` reference / template disposition inventory
- `R5.19a4` bin / agent / overlay / runtime-control disposition inventory
- `R5.19a5` governance / readiness-authority disposition inventory

Umbrella anchor:

- [checkpoint-5-r5-19a-full-surface-disposition-inventory-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19a-full-surface-disposition-inventory-audit-spec.md)

### `R5.19c` Unconsidered / Under-Considered Surface Gap Audit Cluster

Purpose:

- find surfaces that are currently outside modification consideration not because they survived scrutiny, but because they were never properly challenged
- identify the strongest missing surfaces and the consequences of leaving them unchallenged

Priority:

- This cluster should also run in parallel with `R5.19a` and `R5.19b`.
- Omitted-surface challenge is not a lightweight synthesis layer; it needs family-level rereads to avoid inheriting the same blind spots as the current exclusions.

Operational split:

- `R5.19c1` skill / wrapper omitted-surface gap audit
- `R5.19c2` workflow omitted-surface gap audit
- `R5.19c3` reference / template omitted-surface gap audit
- `R5.19c4` bin / agent / overlay / runtime-control omitted-surface gap audit
- `R5.19c5` governance / readiness-authority omitted-surface gap audit

Umbrella anchor:

- [checkpoint-5-r5-19c-unconsidered-surface-gap-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19c-unconsidered-surface-gap-audit-spec.md)

### `R5.19d` Adjudication Cluster

Purpose:

- compare the completed `R5.19a` inventory, `R5.19b` hard-exclusion proof, and `R5.19c` omitted-surface challenge outputs
- determine which current classifications fail, which exclusions survive, which omissions must now feed `R5.18`, and which items remain contested
- produce an operational consequence layer that `R5.18` can consume without flattening the broader challenge back into a pile of family artifacts

Priority:

- This cluster should not be monolithic.
- The combined `R5.19a/b/c` output stack is too large to adjudicate responsibly in one lane without recreating the same context and flattening risks the family split was meant to avoid.

Operational split:

- `R5.19d1` skills + workflows adjudication
- `R5.19d2` references/templates + bin/agents/overlays/runtime-control adjudication
- `R5.19d3` governance / readiness-authority / conditional-lane adjudication
- `R5.19d4` operational-consequences synthesis across `d1/d2/d3`

### `R5.19e` Adjudication Reread

Purpose:

- reread the `R5.19d1/d2/d3/d4` adjudication stack before it is allowed to revise `R5.18`
- check whether the adjudication undercalled scope, over-tidied tensions, or reintroduced exclusion by synthesis habit

Priority:

- `R5.19e` should use the split `R5.19d` adjudications as its primary evidence rather than reopening raw `R5.19a/b/c` family outputs unless it can explicitly prove the adjudication stack insufficient.

## What This Bundle Is Explicitly Not

- not a request to patch every file it names
- not a license to flatten all surfaced files into first-wave `R5.18`
- not a substitute for later adjudication
- not a way to silently demote `R5.18`; instead it is a challenge input that `R5.18` must consume

## Success Condition

After `R5.19a-e`, the package should be able to answer all of these concretely:

1. What files are currently excluded from modification consideration for Checkpoint 5?
2. Which of those exclusions are defensible?
3. Which are merely inherited from earlier narrowing doctrine?
4. Which files have not yet been meaningfully considered at all?
5. Which broader surfaces must now feed the final `R5.18` implementation boundary?
6. Which exclusions still leave meaningful quality gains on the table, and why would keeping them excluded nevertheless be justified?
7. For every defended exclusion, what is the actual proof that the file lies outside the relevant sphere of influence?
8. Which contested or omitted surfaces must now become explicit `R5.18` scope-gating decisions rather than disappearing by silence?
