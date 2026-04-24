# Checkpoint 5 R5.16 Spec Bundle Cross-Vendor Review

- checkpoint: 5
- artifact(s) under review: R5.16 propagation-audit bundle spec + all four lane specs and three cross-vendor prompts
- review mode: cross-vendor-reread
- reviewer: Claude Opus 4.6
- model: claude-opus-4.6
- baseline: uncommitted dirty working tree on branch `phase-01-guardrails-rerun-boundary`
- independence relationship: cross-vendor

## Verdict

- status: `provisional`
- explanation: The bundle architecture — four-lane split, anti-regret adjudication, meta-reread — is genuinely strong and well-justified. The seam split correctly separates review/closure-pressure propagation from launch-truth/debt-carrying-completion propagation. The question sets are demanding and mostly well-targeted. However, several concrete spec defects would materially reduce the quality of the resulting audits if launched unchanged. The most serious are missing read surfaces that the implementation spec explicitly names as active scope, an adjudication lane that cannot independently verify the claims it is adjudicating, and a reread lane that is too thin to serve its stated purpose of preventing orchestration interpretation from standing unchallenged. These are fixable defects, not architectural problems. The bundle is close to launch-ready but not yet at the strongest justified standard.

## Highest-Impact Spec Defects

### 1. R5.16b omits `summary.md` template from its read set

The governing implementation spec explicitly names `.codex/get-shit-done/templates/summary.md` as part of the active ownership set for debt-carrying completion (implementation spec lines 91-97, section 6: "Debt-Carrying Completion Boundary"). R5.16b is the lane responsible for auditing whether debt-carrying completion propagates honestly into real consumers. Yet R5.16b's "Candidate Track C Surfaces" (R5.16b spec lines 31-37) and "Live / Downstream Consumers" (R5.16b spec lines 39-47) do not include the summary template.

This is not a minor omission. The summary template is where execution completion gets its final textual representation. If debt-carrying completion can still read as clean completion anywhere in the chain, the summary template is one of the most likely surfaces. The `gsd-executor.toml` (overlay, lines 361-412) references `@__PROJECT_ROOT__/.codex/get-shit-done/templates/summary.md` as the governing template for SUMMARY creation. An auditor following R5.16b's read list will exercise the executor agent and the verifier agent but miss the template that structures how the executor writes its completion artifact.

**Severity:** High — directly undermines the spec's stated audit purpose on debt-carrying completion.

### 2. R5.16c cannot independently verify lane audit claims

R5.16c's governing inputs (R5.16c spec lines 19-35) list the four lane audit outputs, the Checkpoint 3/4 audit surfaces, and the standard readiness doctrine docs. It does not list any of the actual candidate surfaces that R5.16a and R5.16b audited:

- not `review.md` or `planner-reviews.md` (Track B candidates)
- not `WORKFLOW.md`, `AI-GUARDRAILS.md`, `capture_launch_truth.py`, `gsd-executor.toml`, or `gsd-verifier.toml` (Track C candidates)

The adjudicator's stated job includes classifying which claims survive across lanes, testing whether non-promotion is genuinely defensible, and asking whether non-promotion would leave quality gains on the table (R5.16c spec lines 42-47). But the adjudicator has no mechanism to independently spot-check whether a lane audit's reading of a candidate surface was accurate, complete, or fair. If both lane audits miss the same surface or misread the same file, R5.16c will inherit that blind spot unchallenged.

A possible defense: the adjudicator should compare audit *outputs*, not redo the audits. But anti-regret adjudication that relies entirely on the prior audits' source readings — without any ability to verify contested claims against the actual files — is weaker than it needs to be for the role it plays. The adjudicator should at minimum have the dirty candidate surfaces available, even if its primary work is comparative.

R5.16c also does not include the R5.16a and R5.16b *specs themselves* in its read set. This means the adjudicator cannot assess whether the lane findings were constrained or enabled by what the specs forced their auditors to read. If a lane audit missed a surface because the spec did not list it, the adjudicator should be able to notice that.

**Severity:** High — the adjudication's scope judgment will rest on unverifiable trust in the lane readings.

### 3. R5.16d is too thin for its stated purpose

R5.16d exists to "prevent the adjudication's locality/non-promotion judgment from standing as an unchallenged orchestration interpretation" (R5.16d spec line 5). This is the right job description. But the spec is materially thinner than the other three lanes:

- Six questions (R5.16d spec lines 36-41) versus eight in R5.16a (lines 52-59) and R5.16b (lines 51-61).
- No access to the actual candidate surfaces — R5.16d sees only the R5.16c adjudication and its inputs, not the files the adjudication is ultimately about.
- No access to the R5.16a/R5.16b *specs* (only their outputs through R5.16c). This means R5.16d cannot assess whether the adjudication was limited by what the lane specs forced their auditors to read.
- The question set covers bias direction (lines 37-38) and classification quality (line 36), but does not ask whether the adjudication's evidence base was adequate for the confidence of its scope judgment. Nor does it ask whether the lane specs' read-surface omissions propagated into the adjudication's conclusions.
- The output structure ("Where The Adjudication Underreaches" / "Where The Adjudication Overreaches") is a binary frame that may not capture the most likely failure mode: an adjudication that is *adequate on its own terms* but limited by inherited blind spots from the lane specs. No output section explicitly asks what the adjudication *omitted* or what evidence it lacked.

The risk: R5.16d becomes a pro-forma reread that challenges the adjudication's *conclusions* but not the *adequacy of the evidence base* from which those conclusions were drawn.

**Severity:** Medium-high — weakens the meta-review's ability to catch systemic blind spots.

### 4. No spec forces a read of PROTOCOL.md

PROTOCOL.md defines three things directly relevant to these audits:

1. The gap handling rule and disposition ladder (PROTOCOL.md lines 109-136): `accept`, `revise-current`, `reopen-current`, `reactivate-earlier`, `escalate-cross-vendor`, `strategic-opportunity`, `user-consult`, `defer-nonblocking`.
2. The quality standard (PROTOCOL.md lines 140-163): "The target is not mere pass/fail clearance ... high-expectation ... post-verificationist and post-falsificationist."
3. The comparison ledger requirement (PROTOCOL.md lines 85-90): when comparison is needed and what it should record.

None of the four lane specs or the bundle spec include PROTOCOL.md in their governing inputs. The POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md references PROTOCOL.md extensively (doctrine lines 9, 53, 74, 83, 93, 123) and is included in every spec, but including that doctrine note is not a substitute for reading the protocol directly. Auditors will frame their findings without access to the specific disposition ladder the package uses for routing gaps.

**Severity:** Medium — reduces the auditors' ability to classify findings within the package's own disposition framework. Partially mitigated by the doctrine note and the REVIEW-TEMPLATE.md (which includes the ladder, and is referenced in the review prompt but not in the lane specs).

### 5. R5.16b does not force reads of the chain-tail completion consumers it asks about

R5.16b's question 6 asks "Which Track C gaps are truly local to launch-truth and completion consumers, and which point to a wider chain-tail or governance lane?" (R5.16b spec line 60). This is the right question, but the spec's read set does not include the actual chain-tail surfaces. The implementation spec's contested scope decisions (impl spec lines 113-114) specifically name `verify-work.md`, `progress.md`, roadmap completion machinery, and milestone counting as contested chain-tail surfaces.

R5.16b does include `verify-work.md` workflow (item 17) and `gsd-verify-work/SKILL.md` (item 22) in its live consumers, which partially addresses this. But `progress.md` and `complete-milestone.md` are not included. A Track C auditor asked to assess whether debt-carrying completion reaches chain-tail consumers cannot do so without reading those surfaces.

**Severity:** Medium — the question is right but the read set makes it partially unanswerable for the furthest downstream consumers.

## Missing Or Underweighted Read Surfaces

### Concretely missing from R5.16b

| Surface | Why it matters | Implementation spec reference |
| --- | --- | --- |
| `.codex/get-shit-done/templates/summary.md` | Debt-carrying completion's final representation surface; the executor is told to use this template at `gsd-executor.toml` overlay line 365 | Impl spec section 6, lines 91-97 |
| Chain-tail: `.codex/get-shit-done/workflows/progress.md` | One of the explicitly contested chain-tail completion surfaces | Impl spec contested decisions, lines 113-114 |

### Concretely missing from R5.16c

| Surface | Why it matters |
| --- | --- |
| All 7 dirty candidate files (2 Track B overlay + 5 Track C) | Adjudicator cannot spot-check lane audit claims against actual files |
| R5.16a spec and R5.16b spec | Adjudicator cannot assess whether lane findings were constrained by spec-level read-surface omissions |

### Concretely missing from R5.16d

| Surface | Why it matters |
| --- | --- |
| R5.16a spec and R5.16b spec | Rereader cannot assess whether the adjudication inherited read-surface limitations from its input lane specs |

### Missing from all specs

| Surface | Why it matters |
| --- | --- |
| `PROTOCOL.md` | Defines the disposition ladder, gap handling rule, and quality standard that auditors' findings should classify against |

## Epistemic / Scope Bias Risks

### 1. Parallel output structures may produce artificial convergence in R5.16c

R5.16a and R5.16b prescribe nearly identical output section structures: "Blocking Propagation Gaps," "Local But Important Gaps," "Signals That The Problem May Already Be Wider," etc. When R5.16c receives two outputs with parallel structure, the easiest synthesis path is section-by-section comparison. This creates a subtle incentive toward convergence findings (the parallel sections line up neatly) rather than toward discovering gaps that one lane found but the other lane's *structure* was not designed to catch.

This is a real tradeoff: the parallel structure also makes R5.16c's comparative work more tractable. The risk is manageable but the R5.16c spec should explicitly warn the adjudicator not to treat structural parallelism in the outputs as evidence of epistemic convergence.

### 2. The bundle's framing tilts slightly toward locality as the default expectation

The bundle spec (line 3) says "It is not a generic 'review the dirty files' pass." The standing rules (line 71) say "`R5.17` should not be promoted only because widening feels safer." These are correct and well-calibrated guardrails against scope inflation. But the overall framing positions the lane audits as testing whether a *local* problem might be *wider*, rather than neutrally assessing the propagation surface. The R5.16c anti-regret standard (lines 5-6) corrects this by requiring explicit justification for non-promotion. But neither R5.16a nor R5.16b includes a question that asks the auditor to actively look for wider propagation patterns — both ask reactively "which gaps point to a wider lane?" (R5.16a line 58, R5.16b line 60) rather than proactively "are there wider propagation chains that this read set would miss?"

The correction here is modest: add one proactive question to each lane spec about read-surface adequacy.

### 3. R5.16d has structural asymmetry toward accepting the adjudication

R5.16d's question set (lines 36-41) is balanced between underreach and overreach. But its output structure creates a binary frame ("Where The Adjudication Underreaches" / "Where The Adjudication Overreaches") that may not capture the most common failure mode: an adjudication that is *internally coherent* but limited by what evidence was available to it. The spec does not ask "Was the adjudication working from enough evidence to justify the confidence of its scope judgment?" — and the output structure has no section where that finding would naturally land.

### 4. Internal/cross-vendor prompt duplication removes a framing-independence lever

R5.16a's internal spec and cross-vendor prompt are textually near-identical (the only material difference is the output file path). The same holds for R5.16b and R5.16d. This is consistent with the review policy's approach where independence comes from the reviewer/model, not the prompt. But it means both lanes read the same surfaces in the same order and answer the same questions. A spec-level choice to give the cross-vendor prompt a slightly different entry question or a different read ordering could surface different patterns without compromising the comparison. This is a genuine opportunity cost, but not a defect — the current design is defensible under the review policy, and the risk of prompt divergence causing incommensurable outputs is real.

## What Is Already Strong

1. **The four-lane split is well-justified and well-sequenced.** Track B (review/closure-pressure) and Track C (launch-truth/debt-carrying-completion) genuinely address different seam families that can fail differently. The standing rules (bundle spec lines 69-75) correctly prevent R5.16a/R5.16b from prejudging the locality question and reserve that judgment for R5.16c. This architecture should be preserved exactly.

2. **The anti-regret posture in R5.16c is the strongest part of the bundle.** Requiring the adjudicator to explicitly test both promotion and non-promotion, and requiring explicit justification for non-promotion as a scope claim (R5.16c spec lines 5-6, 17), directly addresses the scope-conservative bias pattern identified across earlier checkpoints. The R5.16c question set (lines 39-47) is demanding: "If `R5.17` were not promoted, what likely quality gains, anomaly-accounting work, or under-owned consequences would still be left on the table?" — this is the right question at the right layer.

3. **R5.16d exists at all.** Most audit frameworks stop at adjudication. The reread of the adjudication is a genuine epistemic advance — it prevents the orchestrator's scope interpretation from becoming the unchallenged bottleneck. The concept is right even though the current spec is too thin.

4. **The governing input lists are substantial and mostly well-chosen.** Both R5.16a and R5.16b include the implementation spec, the Checkpoint 4 cross-lane seam synthesis, the post-falsificationist doctrine note, and the audit comparison policy. R5.16c adds the Checkpoint 3 scope maps (items 9-10) to give the adjudicator topology context. This layered read-surface design is well-thought-through.

5. **The question sets are demanding and specific.** R5.16a's questions about consensus flattening (line 53), "merely adequate" operationalization (line 55), and overlay-versus-installed truth (line 57) are specific enough to force real engagement rather than generic approval. R5.16b's questions about requested-versus-effective truth (line 51), debt-carrying completion (lines 53-59), and closure-status taxonomy (lines 55-59) are similarly targeted.

6. **The cross-vendor prompts are correctly self-contained.** Each cross-vendor prompt includes the full governing input list, the full question set, and the full output structure. This means the cross-vendor reviewer can produce a meaningful result without hidden context, which is the right design for vendor independence.

7. **The bundle spec's "Expected Outputs" section (lines 77-85) correctly names all seven output artifacts.** This makes the full audit trail predictable and auditable before any lane launches.

8. **The overlay candidate surface reads in R5.16a and R5.16b include both the dirty overlay candidates and the live installed consumers.** This is the right design for a propagation audit — testing whether changes at the overlay level actually reach the installed runtime.

## What Must Change Before Launch

### 1. Add `summary.md` template to R5.16b's read set

In both `checkpoint-5-r5-16b-track-c-propagation-audit-spec.md` (under "Live / Downstream Consumers") and `checkpoint-5-r5-16b-track-c-propagation-cross-vendor-prompt.md` (same section), add:

```
23. [.codex/get-shit-done/templates/summary.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/summary.md)
```

The implementation spec (section 6, lines 91-97) explicitly names this surface as part of the debt-carrying completion boundary. The `gsd-executor.toml` overlay (line 365) directs the executor to use this template. Omitting it from the Track C audit spec makes the propagation audit unable to test one of the most important downstream representation surfaces.

### 2. Add dirty candidate surfaces and lane specs to R5.16c's governing inputs

In `checkpoint-5-r5-16c-anti-regret-adjudication-spec.md`, after item 15, add:

```
16. [REVIEWS/checkpoint-5-r5-16a-track-b-propagation-audit-spec.md]
17. [REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-spec.md]
18. [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md]
19. [tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md]
20. [WORKFLOW.md]
21. [AI-GUARDRAILS.md]
22. [tooling/codex/capture_launch_truth.py]
23. [tooling/portable-gsd/overlay/agents/gsd-executor.toml]
24. [tooling/portable-gsd/overlay/agents/gsd-verifier.toml]
```

This allows the adjudicator to spot-check contested claims against the actual files and to assess whether lane findings were constrained by spec-level read-surface omissions. The adjudicator should still focus primarily on comparative adjudication; the candidate surfaces are available for verification, not for a third audit pass.

### 3. Strengthen R5.16d

In both `checkpoint-5-r5-16d-adjudication-reread-spec.md` and `checkpoint-5-r5-16d-adjudication-reread-cross-vendor-prompt.md`:

**Additional governing inputs** (after item 13):
```
14. [REVIEWS/checkpoint-5-r5-16a-track-b-propagation-audit-spec.md]
15. [REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-spec.md]
```

Note: the bundle spec is already item 8 in R5.16d.

**Additional questions** (add after line 41):
- Was the adjudication working from enough evidence — both in the lane outputs and in its own reads — to justify the confidence of its scope judgment?
- Did the adjudication adequately test the two-sided anti-regret requirement, or did it classify claims and then default to one side?
- Were any lane audit findings limited by spec-level read-surface omissions that the adjudication should have caught but did not?

**Additional output section** (add after "What The Adjudication Already Gets Right"):
- `Was The Evidence Base Adequate For The Scope Judgment?`

### 4. Add PROTOCOL.md to the bundle spec's governing inputs and propagate

In `checkpoint-5-r5-16-propagation-audit-bundle-spec.md`, governing inputs, add:
```
12. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
```

Then propagate this addition into R5.16a, R5.16b, R5.16c, and R5.16d governing input lists (both internal specs and cross-vendor prompts). The disposition ladder, gap handling rule, and quality standard in PROTOCOL.md should be available to all auditors.

### 5. Add a structural-parallelism warning to R5.16c

In `checkpoint-5-r5-16c-anti-regret-adjudication-spec.md`, in the "Adjudication Stance" section, add:

```
- Do not treat structural parallelism in the R5.16a and R5.16b outputs as evidence of epistemic convergence. Both lane specs prescribe parallel output section structures; findings that appear in matching sections may converge for structural reasons rather than evidential ones. Test convergence by the claim's content and source, not by its location in the output.
```

## What Can Stay As-Is

1. **The internal/cross-vendor prompt near-duplication.** The review policy correctly sources independence from the reviewer, not the prompt. Making the cross-vendor prompts self-contained textual duplicates (with only the output path differing) is the right design choice for this package. The opportunity cost of not using a divergent framing is real but small, and the risk of incommensurable outputs from divergent prompts would be worse.

2. **The parallel output structure across R5.16a and R5.16b.** The convergence risk is real but manageable with the warning added to R5.16c. The adjudication benefit (section-by-section comparison) outweighs the risk. No structural change to the lane output sections is needed.

3. **R5.16a's Track B read set** (with only the PROTOCOL.md addition noted above). The Track B candidate surfaces and live consumers are well-chosen. The review workflow's synthesis logic (overlay `review.md` lines 237-258) is readable through the spec's existing question set. The `planner-reviews.md` reference correctly covers how the planner consumes review output.

4. **R5.16b's Track C read set for the core surfaces** (with the summary template and PROTOCOL.md additions). The existing reads of `gsd-executor.toml`, `gsd-verifier.toml`, `capture_launch_truth.py`, `WORKFLOW.md`, `AI-GUARDRAILS.md`, and the live consumer surfaces are well-chosen.

5. **The Checkpoint 3 surface maps in R5.16c's governing inputs.** Including the broader topology baseline for the adjudicator — but not for the lane auditors — is the right level-of-access design. The lane auditors should stay focused on their seam; the adjudicator needs the wider map to judge locality.

6. **R5.16c's question set and output structure.** The anti-regret adjudication questions are well-calibrated and the output sections ("Convergent Local Gaps," "Convergent Wider-Scope Signals," "Contested Claims," "Case For Keeping The Issue Local," "Case For Wider Promotion," "Is Non-Promotion Defensible?") are well-designed for the adjudication's purpose.

7. **The bundle spec's standing rules (lines 69-75).** These are correctly calibrated and should not be changed.

8. **R5.16a and R5.16b question sets.** The questions are demanding enough to force real engagement. No additional questions are strictly needed beyond the PROTOCOL.md-related disposition capability.

## Change Summary

| # | Change | Files affected | Severity of defect if not fixed | Effort |
| --- | --- | --- | --- | --- |
| 1 | Add `summary.md` template to R5.16b read set | R5.16b spec + cross-vendor prompt | High — misses a primary debt-carrying completion surface | Trivial |
| 2 | Add dirty candidate surfaces + lane specs to R5.16c governing inputs | R5.16c spec | High — adjudicator cannot verify contested claims | Small |
| 3 | Strengthen R5.16d: add lane specs to reads, add evidence-base questions, add output section | R5.16d spec + cross-vendor prompt | Medium-high — meta-review too thin for its stated purpose | Small |
| 4 | Add PROTOCOL.md to bundle spec and propagate to all lane specs/prompts | Bundle spec + all 7 lane/prompt files | Medium — auditors lack the disposition framework | Trivial |
| 5 | Add structural-parallelism warning to R5.16c adjudication stance | R5.16c spec | Low-medium — manageable risk but worth explicit mitigation | Trivial |
