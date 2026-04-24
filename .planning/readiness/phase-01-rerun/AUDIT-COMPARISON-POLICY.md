# Audit Comparison Policy

Use this when multiple audits or reviews address the same readiness artifact but were produced under different conditions.

The goal is not to flatten them into a blended verdict. The goal is to compare, qualify, and adjudicate them in a way that survives later scrutiny.

## Core Rule

- [d:c:i] Do not resolve competing audits by simple averaging, by majority vote, or by naive appeal to model prestige, reasoning level, or vendor alone.
- [d:c:i] Compare audits by their production conditions, their self-justification quality, and the survivability of their claims under cross-artifact scrutiny.

## Comparison Axes

### 1. Governing Spec Quality

- [d:c:i] Ask how strong the audit spec or prompt was before asking how strong the resulting audit was.
- [d:c:i] A stronger governing spec:
  - names the relevant source surfaces explicitly
  - forces reads of likely propagation surfaces
  - distinguishes producer, consumer, and representation / chain-tail surfaces when propagation or completion semantics matter
  - gives adjudicators enough direct surfaces to spot-check contested claims
  - gives reread lanes enough material to test evidence-base adequacy rather than only conclusion quality
  - asks whether the spec's own read set may be incomplete
  - distinguishes blockers from non-blockers
  - asks about missing ownership, shared contracts, and deferrals
  - reduces the chance that the reviewer only comments on the most obvious surface

### 2. Epistemic Posture

- [d:c:i] Classify whether the audit was framed mainly as:
  - `verification`
  - `falsification / pressure test`
  - `gap exposure / completeness challenge`
- [d:c:i] Do not assume one posture is always superior.
- [d:c:i] Instead ask what the posture is likely to overcall or undercall:
  - `verification` tends to undercall missing scope and premature closure
  - `falsification` tends to surface neglected risks but can over-promote expansions
  - `gap exposure` tends to best surface under-owned consequences and misclassified deferrals

### 3. Source Coverage

- [d:c:i] Ask whether the audit actually read the surfaces needed to support its claims.
- [d:c:i] An audit that comments on propagation without reading templates, prompts, shared references, or tracked overlays has weaker standing than one that did.

### 4. Independence

- [d:c:i] Independence matters, but only together with spec quality and source coverage.
- [d:c:i] `cross-vendor` is not automatically more trustworthy than `internal`.
- [d:c:i] A weaker cross-vendor prompt can still produce a less reliable result than a stronger internal audit spec.

### 5. Self-Justification Quality

- [d:c:i] Judge how well the audit justifies itself:
  - does it separate observation from inference?
  - does it explain why the cited sources support the conclusion?
  - does it identify where a claim is a stronger extrapolation rather than a direct reading?
  - does it distinguish blocking gaps from meaningful but non-blocking concerns?
  - does it show that the evidence base was adequate for the confidence of its scope judgment?
- [d:c:i] A well-justified audit is not merely well-cited; it shows why the citations bear the weight placed on them.

### 6. Claim Survivability

- [d:c:i] Individual claims should be classified by how they survive comparison:
  - `convergent` — survives across stronger artifacts with different production conditions
  - `supported` — strongly argued in one high-quality artifact and not contradicted elsewhere
  - `contested` — materially disagreed over by strong artifacts
  - `pressure-only` — appears only in a pressure/falsification artifact
  - `weak` — under-argued or unsupported by the cited sources

## Standing Rules

- [d:c:i] Use the strongest available `gap exposure / completeness challenge` artifacts as the main governing comparison set when the question is whether a candidate stack is still incomplete or under-propagated.
- [d:c:i] Use older or weaker-framed audits as supporting or confirming evidence, not as equal governors once a better comparison frame exists.
- [d:c+i] Use pressure-oriented audits as challenge artifacts:
  - do not ignore them
  - do not let them govern directly unless their claims survive comparison against stronger-framed audits

## What To Accept

- [d:c:i] Accept into the next revision first:
  - claims that are `convergent`
  - claims that are `supported` by a strong artifact and not materially contradicted

- [d:c:i] Do not automatically promote:
  - claims that appear only in one audit
  - claims that depend on weaker framing
  - claims that overreach beyond the sources they cite

## Scope-Promotion Judgment

- [d:c+i] When the comparison result is being used to decide whether a wider lane should be promoted, do not treat `keep it local` as the neutral or cheaper default.
- [d:c+i] Ask two separate questions:
  - does the surviving evidence justify wider promotion?
  - is non-promotion actually defensible without leaving likely quality gains, anomaly-accounting work, or under-owned consequences on the table?
- [d:c+i] A locality judgment should therefore be treated as a claim that also needs justification, not merely as the absence of justification for widening.

## What To Record

- [d:c:i] When multiple audits are being compared, write a comparison ledger that records for each artifact:
  - governing spec/prompt
  - epistemic posture
  - source coverage
  - self-justification quality
  - likely bias / blind spot
  - current standing
- [d:c:i] Then classify important claims as:
  - `convergent`
  - `supported`
  - `contested`
  - `pressure-only`
  - `weak`

## What Not To Do

- [d:c:i] Do not collapse disagreement into a fake consensus summary if the disagreement is actually about production conditions or scope.
- [d:c:i] Do not confuse structural parallelism in sibling audit outputs with evidential convergence.
- [d:c:i] Do not treat `xhigh` as dispositive.
- [d:c:i] Do not treat `cross-vendor` as dispositive.
- [d:c:i] Do not keep implementing while the governing comparison is still unresolved on blocking scope questions.
