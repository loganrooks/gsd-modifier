# Checkpoint 1 Governance-Doc Normalization Audit Spec

Use this as the base spec for Checkpoint 1 audit runs.

## Purpose

Determine whether the standing governance-doc layer is carrying repo doctrine at the right level of generality, in the right documents, without duplicated policy, audit-era residue, or misplaced rules that should live elsewhere.

This is not a patch pass.

Its job is to produce a justified normalization verdict that can cleanly drive:

- [Checkpoint 2](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-2.md) governance-doc normalization patching
- later [Checkpoint 3](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-3.md) workflow / harness scoping

## Research Frame

- Mode: `synthesis`
- Question:
  - are the current governance docs expressed at the right level of abstraction and ownership to carry the repo's doctrine rigorously into the rerun sequence?
- Scope:
  - root governance layer and planning-local governance layer
  - document ownership, abstraction level, duplication, residue, and likely machinery-owned spillover
- Non-goals:
  - do not patch the docs in this lane
  - do not redesign the GSD/Codex harness in this lane
  - do not pre-empt the later workflow / harness scope audit by assuming the harness is only a set of skills
- Stop condition:
  - a later patch pass could act from this artifact without guessing what belongs where or why

## Governing Inputs

- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
  - package-wide sequence and why Checkpoint 1 exists before later harness work
- [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
  - current blocker and immediate next action
- [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
  - machine-readable checkpoint state and commit expectations
- [GATES/checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md)
  - official objective, exit criteria, quality questions, and reopen triggers
- [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md)
  - review depth expectations for Checkpoint 1
- [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml)
  - independence rule and cross-vendor posture for checkpoint closure
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
  - root runtime doctrine, slimness expectation, and current signs of lane-shaped residue
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
  - planning-local doctrine and current section/ownership boundaries
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
  - repo workflow, git/checkpoint policy, verification, continuity, and hooks posture
- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
  - signoff, autonomy boundaries, and planning/research hygiene
- [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)
  - artifact classes, retention, and workspace-readiness doctrine
- [05-post-sensitivity-response-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md)
  - why narrow pass/fail framing was rejected
- [05-canon-uplift-milestone-2-steering-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md)
  - stronger doctrine-carrying standard that governance docs should not undercut
- [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md)
  - prior diagnosis that the governance/process layer was not yet strong enough

## Target Documents

- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`

## Audit Lenses

- rule ownership:
  - does this rule live in the document whose scope actually justifies it?
- abstraction quality:
  - is the rule stated generally enough to endure beyond the lane that produced it?
- residue detection:
  - is a recent audit/example/lane standing in for the governing rule it only illustrates?
- duplication:
  - is the same policy duplicated across docs at mismatched levels of specificity?
- slimness / prompt-budget discipline:
  - especially for `AGENTS.md` files, is the instruction earning its token cost?
- doctrinal fidelity:
  - do these docs preserve the distinctions earned in `05-gap-closure`, or do they quietly flatten them back into umbrella language or pass/fail framing?
- ownership spillover:
  - does any rule appear to belong not in a doc at all, but in a deeper workflow/template/harness surface?

## Path Of Inquiry Requirements

Make the inquiry path visible:

- entry point
- branches considered
- branches pursued
- branches deferred or abandoned
- unexpected reframings

Do not just deliver findings without showing how the envelope was inspected.

## Output Requirements

Write the output to:

- [checkpoint-1-governance-doc-normalization-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit.md)

Use the lightweight `gsd-rigorous-research` output shape, plus these required sections:

- `Document-by-document findings`
- `Cross-document duplication and ownership drift`
- `Likely Checkpoint 2 patch units`
- `Potential machinery-owned issues to carry into Checkpoint 3`
- `What can close now`
- `What must stay open`
- `Planning handoff`

For each material finding:

- cite concrete file lines
- classify whether it is:
  - `doc-local cleanup`
  - `cross-doc normalization`
  - `machinery-owned follow-through`
  - `strategic-opportunity`

## Decision Discipline

- do not recommend patching just because text feels untidy
- do not collapse later harness questions into doc cleanup just because markdown is easier to edit than machinery
- do not assume a rule belongs deeper in the harness unless the current evidence supports that escalation
- if the evidence is mixed, say so plainly

## Default Lane

- lane type: `replanning/revision/gap-filling`
- model / reasoning: `gpt-5.4 xhigh`
- independence relationship for this authoring lane: `authoring`

## Review Handoff

This audit does not close Checkpoint 1 by itself.

After the audit is written:

- run an independent review before closing Checkpoint 1
- keep the review artifact under [../REVIEWS/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS)
- if accepted, use the audit to drive Checkpoint 2 patching
- if the audit points strongly to machinery-owned issues, record that explicitly but still keep those follow-through questions for Checkpoint 3 and later unless Checkpoint 1 itself must be reopened
