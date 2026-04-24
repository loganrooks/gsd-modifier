# Checkpoint 4 Launch Bundle Cross-Vendor Review

## Header

- checkpoint: 4 (launch bundle adequacy review, not closure review)
- artifact(s) under review:
  - [checkpoint-4-workflow-harness-excellence-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md)
  - [checkpoint-4-codex-load-bearing-surfaces-and-seams-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams-spec.md)
  - [checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence-spec.md)
  - [checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence-spec.md)
  - [checkpoint-4-gsd-runtime-config-overlay-truth-excellence-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence-spec.md)
  - [checkpoint-4-cross-lane-seam-synthesis-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis-spec.md)
  - [checkpoint-4-converged-synthesis-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-converged-synthesis-spec.md)
- review mode: `cross-vendor-reread`
- authoring lane: `gpt-5.4 xhigh` (Codex orchestrator)
- reviewer: `claude-opus-4.6` (Claude Code)
- baseline commit / artifact snapshot: `7e2234b` (head of `phase-01-guardrails-rerun-boundary`)
- independence relationship: `cross-vendor`

## Review Questions

- What is this review trying to falsify?
  Whether this seven-document launch bundle is strong enough to guide the Checkpoint 4 audit lanes toward genuinely excellent, ownership-separating, scrutiny-resistant work, or whether it is merely structurally complete while leaving enough ambiguity or weakness to produce a thin Checkpoint 4 result.

- Which gate exit criteria are being tested?
  The Checkpoint 4 gate exit criteria ([GATES/checkpoint-4.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md:36), lines 36-41) require the audit to clearly distinguish doc-level, workflow-protocol, and machinery-ownership problems, be strong enough to decide whether harness changes are needed before rerun, and give a defensible answer about whether the workflow drives excellence versus minima. This review tests whether the specs, as written, can reliably produce outputs that satisfy those criteria.

- Which quality questions are being tested?
  The quality questions from [GATES/checkpoint-4.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md:44), lines 44-48: would strong engineers/designers/researchers see a workflow aiming at excellence; does the audit preserve the distinction between improving review quality and over-automating judgment; is the ownership story clean enough for later scrutiny.

- Which regressions are most relevant here?
  Checkpoint 3 envelope collapse. The readiness plan warns explicitly against collapsing the three-sublane GSD split back into one omnibus lane ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:386), line 386). Also: scope creep into machinery patching, which the launch spec correctly forbids but which the seam and converged synthesis could quietly encourage.

- What is the strongest justified criticism of this bundle?
  See Finding 1 below.

- What is merely adequate here but should be stronger?
  See Findings 3, 5, and 6 below.

- What would fail later stringent audit by strong engineers, designers, or researchers?
  See Finding 2 below.

- What meaningful quality opportunity is being left unused?
  See Findings 4, 7, and the Strategic Opportunities section.

## Findings

### Finding 1: The seam synthesis spec is under-specified for its pivotal role

Severity: high

The seam synthesis is the artifact where four independent lane outputs must become a coherent ownership and risk picture. It is the single place where lane-level disagreement about the same surface gets resolved or preserved. It is arguably the most judgment-heavy artifact in the bundle.

Yet it is the thinnest spec (69 lines vs. 75-92 lines for lane specs). It has no `Constraints` section, unlike every lane spec. It does not explicitly require the synthesis to:

- trace whether lane-local findings actually agree or disagree about the same seam
- surface cases where one lane's "strong" finding is contradicted by another lane's evidence
- distinguish "lanes didn't mention this seam" from "lanes found this seam healthy"
- test whether the four-lane split itself created blind spots at the boundaries

The required output sections include "Where Doc, Protocol, And Machinery Interact Cleanly" but not a symmetric section for where they interact badly or where the interaction is still unclear. The "Where Ownership Is Still Ambiguous Or Split" section partially covers this, but the framing creates an asymmetry: clean interaction gets a named section, messy interaction gets folded into "ambiguous."

The seam synthesis spec also lacks explicit instructions for handling the case where a seam doesn't surface cleanly in any one lane's output. Some seams may fall between lanes. The spec assumes the lane outputs will neatly feed evidence into each seam, but the reality is that the hardest ownership questions will be the ones where no single lane owns enough evidence to make the call.

Standard not met: the seam synthesis spec should be at least as carefully specified as the lane specs, and arguably more so, because it is doing harder judgment work.

### Finding 2: The launch spec introduces a seventh mandatory seam not present in the accepted Checkpoint 3 envelope

Severity: medium-high

The accepted Checkpoint 3 scope audit ([checkpoint-3-workflow-harness-scope-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md:59), line 59) lists six mandatory seams for Checkpoint 4:

1. future-awareness and canonical-ref continuity
2. AGENTS/governance reach into operative workers
3. named-agent authority and reasoning-policy truth
4. continuity under compaction or resume
5. execution-completion plus verification or UAT closure
6. branch/worktree boundary materialization

The launch spec ([checkpoint-4-workflow-harness-excellence-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md:69), line 69) adds a seventh: `verify/CI ownership`.

This addition is not justified against the accepted Checkpoint 3 result. It may be a reasonable refinement — CI is mentioned in the Codex surface map — but it appears without explanation. The readiness plan is explicit that Checkpoint 4 should consume the resolved Checkpoint 3 mapping result ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:378), lines 378-386), and the scope audit is explicit that widening the envelope should be justified ([checkpoint-3-workflow-harness-scope-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md:114), line 114).

The risk is not that verify/CI ownership is a bad seam to check, but that adding a seam without justification sets a precedent for quiet envelope expansion. If this seam is load-bearing, explain why Checkpoint 3 missed it. If it is a reasonable refinement, say so and name the evidence.

Standard not met: changes to the accepted Checkpoint 3 envelope should be explicitly justified, not silently introduced.

### Finding 3: The converged synthesis spec does not connect its verdict to the PLAN.md failure-mode branching logic

Severity: medium

The readiness plan has a detailed "Failure Modes And Branching Logic" section ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:564), lines 564-597) with explicit branching for what happens depending on Checkpoint 4 outcomes. The converged synthesis spec requires a `Checkpoint 5 Decision` section with three explicit options (lines 53-57), which is good.

But the spec does not require the converged synthesis to explicitly map its findings to the PLAN.md branching logic. This matters because the branching logic distinguishes between "mostly process/doctrine improvements" (skip Checkpoint 5), "real harness ownership problems" (run Checkpoint 5), and "harness improved but ambient operator memory still required" (Checkpoint 5 follow-through was incomplete). The converged synthesis should demonstrate that its verdict is consistent with these branches, not just produce a verdict in isolation.

The spec also does not require the converged synthesis to address the PLAN.md's cross-cutting regression checks ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:498), lines 498-562) or to test whether the Checkpoint 4 audit process itself introduced regressions (e.g., treating a machinery problem as a doc problem just because the lane structure made doc problems easier to see).

Standard not met: the converged synthesis should explicitly trace to the readiness plan's branching logic, not just produce a standalone verdict.

### Finding 4: No explicit lane-boundary management protocol for concurrent execution

Severity: medium

The four initial lanes are specified to run concurrently (the launch spec says "Launch lanes 1 through 4 first," implying parallel execution). Each lane spec has a boundary rule: Lane 2 says "do not judge the agent-role surface here except where it directly shapes the workflow chain" (line 76); Lane 3 says "do not collapse runtime/config truth into this lane except where it changes which doctrine actually reaches workers" (line 69); Lane 4 says "do not assume documented config or overlay intent equals runtime truth" (line 66).

These are good exclusion rules, but they are one-directional. There is no protocol for what happens when:

- Lane 2 discovers evidence that materially changes what Lane 3 should inspect
- Two lanes reach contradictory conclusions about the same surface
- A finding falls cleanly between two lanes and neither claims it

The spec assumes the seam synthesis will retroactively resolve these tensions. That is reasonable but could be made explicit. If the lanes run concurrently without any communication channel, and then the seam synthesis must reconcile them, the seam synthesis spec needs to be strong enough to handle that reconciliation work — which connects back to Finding 1.

Standard not met: the bundle should either include an inter-lane escalation protocol or explicitly require the seam synthesis to handle the full reconciliation burden and specify how.

### Finding 5: Lane output section requirements lack structured classification expectations

Severity: medium-low

Every lane spec requires an "Ownership Assessment" section but does not specify what that section must contain. The Checkpoint 4 gate ([GATES/checkpoint-4.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md:37), lines 37-39) requires the audit to clearly distinguish doc-level, workflow-protocol, and machinery-ownership problems. The launch spec requires the same at line 19-21.

But no lane spec explicitly requires its Ownership Assessment to use that three-way classification. A lane could produce a narrative ownership assessment that sounds reasonable but doesn't actually separate the three categories in a way the seam synthesis or converged synthesis can consume. Similarly, "Strongest Justified Criticisms" appears in every spec but nowhere says what makes a criticism "strongest" versus merely present. This could lead to flat lists rather than a prioritized, consequential assessment.

Standard not met: if the three-way doc/protocol/machinery classification is central to the Checkpoint 4 verdict, it should be structurally required in the lane outputs, not just hoped for.

### Finding 6: The Codex lane spec references potentially absent or conditional inputs without qualification

Severity: low-medium

The Codex lane spec lists as governing inputs:

- `[03-compaction-context-response.md]` (line 39)
- `[SESSION-REENTRY-CHECKLIST.md]` (line 40)

These are presented at the same level as AGENTS.md and the readiness plan. If these files do not exist or have been superseded, the executing agent has no instruction about how to proceed. The spec says "Read these first" (line 28) for the entire list, which implies they all must exist.

More broadly, the Codex lane spec instructs the auditor to inspect "relevant official Codex documentation" and "recent still-relevant unofficial issue/discussion evidence" (lines 48-49). This is the right requirement, but the spec does not give the auditor any guidance about what constitutes "still-relevant" unofficial evidence, how to assess whether an issue or discussion applies to the current Codex version, or what the expected source-basis annotation should be for unofficial evidence. The constraints section (lines 82-83) says "keep unofficial-source applicability qualified" and "do not treat stale user reports as present truth," which is directionally correct but thin compared to the repo's usual epistemic hygiene standards.

Standard not met: the spec should distinguish required inputs (must exist) from conditional inputs (use if available) and give sharper unofficial-evidence qualification guidance.

### Finding 7: No explicit regression-check requirement across the bundle

Severity: medium-low

The readiness plan has extensive cross-cutting regression checks ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:498), lines 498-562) covering canon, governance-doc, claim/citation, delegation/orchestration, git/checkpoint, and Phase 01 rerun regressions. These are highly relevant to Checkpoint 4 work, especially the governance-doc regressions and the delegation/orchestration regressions.

No lane spec and no synthesis spec explicitly requires checking its own outputs against these regression lists. The converged synthesis could produce a verdict that inadvertently introduces a regression the plan has already flagged — for example, treating a machinery defect as a doc problem (a reopen trigger from [GATES/checkpoint-4.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md:56), line 56) without realizing the plan would classify that as a regression.

Standard not met: the bundle should require at least the converged synthesis (and ideally the seam synthesis) to explicitly check their conclusions against the PLAN.md regression lists.

## What Is Already Strong

The following aspects of the bundle are genuinely strong and should be preserved through any revision:

1. **The four-lane structure is well-justified and clearly derived.** The launch spec explicitly traces the lane decomposition to the accepted Checkpoint 3 result and preserves the GSD split. The lane boundaries are defensible and avoid the omnibus-audit failure mode. This is the bundle's strongest structural feature.

2. **The split rule is excellent.** The launch spec's split rule (lines 87-94) — if a lane is too broad, stop and say so explicitly, name the split, justify it — is exactly the kind of honesty-forcing mechanism that prevents bluffed completeness. This should be preserved.

3. **The non-goals are well-calibrated.** The launch spec's global non-goals (lines 97-102) correctly forbid patching files, deciding Checkpoint 5 must open just because machinery is interesting, and accepting "good enough to pass" as closure. These non-goals directly address the most likely failure modes of a harness audit.

4. **The Codex lane's external evidence requirement is a real quality addition.** Requiring official and recent qualified unofficial Codex sources, with explicit source-basis and qualification, is the right standard for a lane that is auditing Codex behavior in a repo-specific context. This is stronger than purely introspective analysis.

5. **The converged synthesis's forced Checkpoint 5 decision is well-structured.** Requiring one of three explicit options prevents the common failure mode of a synthesis that describes problems but defers all decisions.

6. **The launch order constraint is correct.** Requiring lanes 1-4 before seam synthesis, and seam synthesis before converged synthesis, prevents premature convergence.

7. **The model/reasoning assignments are appropriate.** `gpt-5.4 xhigh` for authoring and synthesis, `gpt-5.4 high` for internal review, and `claude-opus-4.6` for cross-vendor closure review matches the repo's model policy and the stakes of this work.

## Gap Classification

### Finding 1 (seam synthesis spec under-specification)
Classification: `revise-current`
The seam synthesis spec should gain: a Constraints section parallel to the lane specs; explicit instructions for handling lane disagreement, lane silence, and between-lane findings; a symmetric section for messy ownership interactions alongside the clean-interaction section; explicit instructions for testing whether the four-lane split created boundary blind spots. This is the highest-priority revision because the seam synthesis is where the hardest judgment happens.

### Finding 2 (unjustified seventh seam)
Classification: `revise-current`
Either justify the `verify/CI ownership` seam against the accepted Checkpoint 3 result with explicit evidence, or remove it. If justifying, explain what changed between the scope audit and the launch spec that makes this seam mandatory. If the answer is "it was always implicitly present in execution-completion plus verification/UAT closure," then consolidate rather than adding a seventh seam.

### Finding 3 (converged synthesis disconnected from PLAN.md branching)
Classification: `revise-current`
Add explicit requirements to the converged synthesis spec: the verdict must map to the PLAN.md failure-mode branching logic (lines 564-597), and the readiness handoff must address the PLAN.md cross-cutting regression checks (lines 498-562) relevant to Checkpoint 4 conclusions.

### Finding 4 (no inter-lane communication protocol)
Classification: `strategic-opportunity`
Not blocking if the seam synthesis spec is strengthened per Finding 1. If the seam synthesis is properly equipped to handle full reconciliation, the absence of an inter-lane communication protocol is a pragmatic concession rather than a gap. Track this as a quality opportunity: if Checkpoint 4 execution reveals lane-boundary confusion, this would become a lesson for future multi-lane audit bundles.

### Finding 5 (unstructured ownership classification)
Classification: `revise-current`
Add a requirement to each lane's Ownership Assessment section: findings must use the doc-level / workflow-protocol / machinery-ownership classification from the Checkpoint 4 gate and launch spec. The seam synthesis and converged synthesis should be able to consume these classifications structurally, not retroactively interpret narrative prose.

### Finding 6 (Codex lane conditional inputs)
Classification: `defer-nonblocking`
The executing agent can handle missing inputs pragmatically. But the spec should still distinguish "required" from "conditional" in the governing inputs list. This is a cleanliness issue, not a blocker.

### Finding 7 (no regression-check requirement)
Classification: `revise-current`
Add a requirement to the converged synthesis spec (and optionally the seam synthesis spec) to check conclusions against the PLAN.md cross-cutting regression checks. At minimum, the converged synthesis should explicitly address governance-doc and delegation/orchestration regressions as they apply to Checkpoint 4 findings.

## Verdict

- status: `provisional`
- explanation:
  The bundle is structurally sound and correctly derived from the accepted Checkpoint 3 envelope. The four-lane decomposition, launch order, split rule, non-goals, and forced Checkpoint 5 decision are genuine strengths. The bundle is not thin — it shows real thought about what each lane should audit and how the synthesis stages should converge.

  However, the bundle has a real asymmetry: the lane specs are well-specified while the synthesis specs — where the hardest judgment work happens — are under-specified. Finding 1 (seam synthesis) is the most consequential gap because it directly affects whether the Checkpoint 4 audit can produce a coherent ownership picture or will produce four good lane reports that are hard to reconcile. Findings 2, 3, 5, and 7 are individually smaller but collectively represent a pattern of the bundle being more careful about what each lane should do than about how findings should be connected, classified, and verified against the readiness plan.

  This bundle is close to launch-ready. The revisions needed are targeted: strengthen the seam synthesis spec, justify or consolidate the seventh seam, require structured ownership classification in lane outputs, and connect the converged synthesis to the PLAN.md branching logic and regression checks. None of these require rethinking the bundle's architecture.

  A strong external auditor would accept the lane specs. That same auditor would flag the synthesis specs as adequate but weaker than the rest of the bundle, which is exactly the wrong place to be thin.

## Required Next Action

- exact next step: Revise the bundle to address Findings 1, 2, 3, 5, and 7 before launching any Checkpoint 4 audit lane. Finding 4 should be tracked as a strategic opportunity. Finding 6 can be deferred.
- owner / lane: authoring orchestrator (`gpt-5.4 xhigh`)
- commit implication: fix then commit (the revised bundle should be committed as a clean launch-ready checkpoint before any lane execution begins)

## Independence Note

- Does this review satisfy the checkpoint's independent-review requirement?
  This is a pre-launch bundle review, not a closure review. The Checkpoint 4 closure review is a separate future artifact. This review satisfies the cross-vendor adequacy check for the launch bundle. It does not satisfy and is not intended to satisfy Checkpoint 4's closure-time independent-review requirement.
- Was a cross-vendor lane available?
  Yes.
- If cross-vendor was available, which Claude lane was appropriate here and why?
  `claude-opus-4.6`. This review is assessing whether the bundle is strong enough to guide high-stakes workflow/harness audit work that can materially reshape machinery ownership decisions and affect rerun readiness. That matches the REVIEW-POLICY.yaml's preferred model for Checkpoint 4 ([REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml:99), line 99).
- If used, what did independence add?
  The cross-vendor reviewer identified a structural asymmetry (synthesis specs thinner than lane specs) and an envelope-expansion issue (seventh seam) that a same-vendor reread might have accepted as reasonable refinements rather than examining critically. The review also identified a missing connection between the converged synthesis and the readiness plan's branching logic, which is a gap that the authoring model is less likely to catch because it was also the model that wrote both documents.
