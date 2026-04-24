# Audit Spec Template

Use this when writing a reusable audit spec, adjudication spec, reread spec, or cross-vendor review prompt for the readiness package.

The goal is not just to produce a readable prompt. The goal is to produce a spec that is hard to under-scope, hard to misread, and hard to launch with avoidable blind spots.

## Core Standard

- Write the spec so a later strong reviewer would struggle to find missing read surfaces, missing evidence-base questions, or under-described scope boundaries.
- Treat spec-writing as a load-bearing design task, not as prompt boilerplate.
- A strong spec should make it difficult for a later reviewer to say:
  - the lane could not read what it needed
  - the adjudicator could not verify what it was adjudicating
  - the reread could not test whether the adjudication had enough evidence
  - the output structure created misleading convergence

## Required Sections

### 1. Purpose And Scope Claim

State:

- what seam, artifact family, or scope claim the spec is for
- whether it is:
  - a direct seam audit
  - an adjudication
  - a reread / meta-review
  - a bundle anchor
- what it is explicitly not

The scope claim should be narrow enough to be auditable and strong enough to be honest about what it governs.

### 2. Audit Stance

State the governing posture explicitly:

- post-verificationist
- post-falsificationist
- gap-exposure / completeness-challenge
- anti-regret, if scope judgment is involved

Also state the main bias risks the lane should resist:

- scope-conservative bias
- scope-inflation bias
- consensus flattening
- pass/fail closure bias
- false convergence from output structure

### 3. Governing Inputs

At minimum, reusable readiness audit specs should normally read:

1. `AGENTS.md`
2. `.planning/AGENTS.md`
3. `STATUS.md`
4. `TASKS.md`
5. the active gate file
6. `PROTOCOL.md`
7. `POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`
8. `AUDIT-COMPARISON-POLICY.md`
9. the governing implementation / launch / synthesis spec for the checkpoint

If one of these is intentionally omitted, the spec should justify the omission.

### 4. Surface Map By Role

Do not give the lane an undifferentiated file list.

Separate surfaces by role, for example:

- candidate / edited surfaces
- live or installed downstream consumers
- chain-tail / representation surfaces
- shared contract / reference surfaces
- lane-spec surfaces
- direct verification / spot-check surfaces

This forces the writer to ask whether the lane can actually trace producer -> consumer -> chain-tail effects rather than just reread the nearest edited files.

### 5. Questions

Questions should not only ask whether the current candidate is good.

They should also ask:

- what remains under-owned?
- what remains under-propagated?
- what still reads cleaner or more complete than it really is?
- what wider consequences are signaled?
- what direct spot-checks should challenge the lane's own likely blind spots?

Every load-bearing spec should also include an explicit read-set adequacy question, for example:

- Are there important surfaces missing from this lane's read set that would materially change the scope judgment if added?

### 6. Output Shape

Output sections should help later comparison, but must not silently bias it.

If parallel output structures are used across sibling lanes:

- preserve them only when comparison value outweighs convergence risk
- warn the adjudicator not to treat structural parallelism as evidential convergence

### 7. Cross-Vendor Prompt Strategy

Cross-vendor prompts should usually stay self-contained and closely comparable to the internal spec.

- Prefer comparability by default.
- Divergent cross-vendor framing is allowed only when the point is explicitly to test prompt-framing effects rather than model/vendor independence alone.

## Lane-Type Addenda

### A. Direct Seam Audit

A direct seam audit should be able to answer:

- what changed upstream?
- where are the real consumers?
- where does the change get represented or summarized?
- what chain-tail surfaces might still misstate the new doctrine?

Typical mandatory reads:

- dirty candidate surfaces
- live consumer surfaces
- chain-tail or summary surfaces
- shared contracts / references

### B. Adjudication

An adjudication should not read only prior lane outputs.

It should also read:

- the lane specs themselves
- enough direct candidate surfaces to spot-check contested claims

Otherwise it cannot tell whether a lane finding was constrained by the spec rather than by the artifact.

An adjudication should ask both:

- is wider promotion justified?
- is non-promotion actually defensible?

### C. Reread / Meta-Review

A reread should not only challenge the adjudication's conclusion.

It should also ask:

- did the adjudication have enough evidence for the confidence of its scope judgment?
- were any lane findings limited by spec-level omissions?
- did the adjudication truly test both sides of the anti-regret question?

The reread output should include an explicit evidence-base adequacy section.

## Pre-Launch Self-Audit Checklist

Before launching any high-stakes spec or bundle, answer these:

1. Does the spec read `PROTOCOL.md`, or is it relying on indirect doctrine only?
2. Can the lane read both the producer and the real downstream consumers?
3. If the lane comments on completion or closure semantics, does it read the representation or summary surface too?
4. If the lane comments on chain-tail consequences, does it read at least one true chain-tail surface rather than only the nearest workflow?
5. If the lane adjudicates other audits, can it directly spot-check contested claims against real files?
6. If the lane rereads an adjudication, can it judge whether the adjudication had enough evidence to justify its confidence?
7. Does the question set ask what the spec itself may be missing?
8. Does the output structure help comparison without creating false convergence pressure?
9. Are cross-vendor prompts self-contained and comparable for the intended kind of independence?
10. If this spec launched unchanged, what is the strongest justified criticism a later Opus-style reread would make?

If the answer to any of these is weak or unclear, revise the spec before launch.

## Minimal Skeleton

```md
# <Checkpoint / Lane Name>

<Purpose and honest scope claim>

## Audit Stance
- ...

## Governing Inputs
1. ...

## Candidate Surfaces
1. ...

## Live / Downstream Consumers
1. ...

## Chain-Tail / Representation Surfaces
1. ...

## Questions
- ...

## Output
- ...
```

Use this skeleton as a floor, not a ceiling.
