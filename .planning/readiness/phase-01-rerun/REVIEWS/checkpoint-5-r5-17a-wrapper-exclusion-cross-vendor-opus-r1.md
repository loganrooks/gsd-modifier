# Checkpoint 5 R5.17a Wrapper-Exclusion Cross-Vendor Opus R1

## Production Qualification

- This artifact was launched from the compact prompt [checkpoint-5-r5-17a-wrapper-exclusion-cross-vendor-compact-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-cross-vendor-compact-prompt.md), not from the original full prompt [checkpoint-5-r5-17a-wrapper-exclusion-cross-vendor-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-cross-vendor-prompt.md).
- The compact prompt delegated most governing-input, target-list, and required-section detail to the on-disk bundle spec and lane spec instead of restating that full structure inline.
- Treat this artifact as a compact-prompt-produced cross-vendor lane output. Before treating any claim here as sovereign, compare it against the original full prompt and lane spec, especially where this artifact widens beyond the original six-wrapper candidate list.

## Frame

- Vendor: Anthropic Claude, Opus 4.6
- Mode: independent cross-vendor lane, launched via `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-cross-vendor-compact-prompt.md`; not produced under the original full cross-vendor prompt conditions
- Governing spec: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-audit-spec.md:1-101`
- Bundle spec: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-17-exclusion-judgment-audit-bundle-spec.md:55-120`
- Stance: post-falsificationist / gap-exposure / anti-regret. Exclusion is treated as a burden-bearing claim, not a neutral default. Sources: `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:132-140`; `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md:89-95`.
- Counterpart: this reread was produced before `checkpoint-5-r5-17a-wrapper-exclusion-audit-internal-r1.md` was read and does not silently defer to it.

## Verdict

- [d:c+r:i] `Disposition: revise-prior-exclusion-boundary.` The bounded R5.16c/R5.16d exclusion frontier — which kept `gsd-review` and `gsd-plan-phase` in scope as `rerun-critical` and sent `gsd-execute-phase` and `gsd-verify-work` back to deferred on a `thin wrapper` / `can remain untouched if workflow consumers are fixed` warrant — does not survive direct file-level reread once exclusion is treated as a burden-bearing claim. Two wrappers inside the stated target set (`gsd-verify-work`, `gsd-execute-phase`) were under-justified rather than safely excluded, and three rerun-critical wrappers outside the audit spec's candidate list (`gsd-autonomous`, `gsd-ship`, `gsd-progress`) are missing entirely and in at least one case carry a live false-framing claim. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md:17-18,36`; `.codex/skills/gsd-verify-work/SKILL.md:48-54`; `.codex/skills/gsd-execute-phase/SKILL.md:49-63,92-94`; `.codex/skills/gsd-autonomous/SKILL.md:48-52`; `.codex/skills/gsd-ship/SKILL.md:48-52`; `.codex/skills/gsd-progress/SKILL.md:48-52`.
- [d:c+r:i] The common-core R5.16d promotion verdict survives: `gsd-review` and `gsd-plan-phase` remain presumptive edit targets. `gsd-research-phase` and `gsd-discuss-phase` remain genuinely defensible exclusions. Sources: `.codex/skills/gsd-review/SKILL.md:3,48-58`; `.codex/skills/gsd-plan-phase/SKILL.md:48-59,68-76`; `.codex/skills/gsd-research-phase/SKILL.md:145-177`; `.codex/skills/gsd-discuss-phase/SKILL.md:67-96`.
- [e:c+r:i] This verdict does not automatically promote a wrapper-family sweep. It promotes a narrower claim: the current exclusion frontier was drawn on heuristic phrasing that did not hold up at file level, and specifically named wrappers must be explicitly dispositioned (`accept`, `revise`, `park`, `reject`) rather than left silently deferred by the current adjudication boundary. Sources: `.planning/readiness/phase-01-rerun/PROTOCOL.md:120-134`; `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:122-130`.

## Exclusion Heuristics Found

Prior lanes used the following exclusion phrases as de facto burden-shifting moves. Each is listed with the file line and what the phrase was made to protect:

1. [e:c:i] `thin mapper` / `can remain untouched if the workflow consumers are fixed` — used at `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-cross-vendor-opus-r1.md:41,83-87` and carried into the bounded adjudication at `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md:18,36`. Protects: scope conservatism and cost control, not evidence discipline.
2. [e:c:i] `secondary alignment surface after workflow changes land` — the gate file itself at `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:62` states this as doctrine. Protects: anti-sprawl and sequencing, but specifically at the cost of treating invocation-surface framing as downstream of workflow content.
3. [e:c:i] `wrapper omission is non-load-bearing` / `more dependent on ambient knowledge` — `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16a-track-b-propagation-audit-internal-r1.md:20-23`. Protects: administrative cheapness; did not demonstrate that ambient knowledge can actually carry the missing doctrine, because the workflow required-reading chain does not itself carry it either (see Invalid Exclusion #1).
4. [e:c:i] `directly contradicted wrappers only` — `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md:39-40,47` and `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md:18,36`. Protects: locality; but uses `directly contradicted` as a scope-narrowing test without defining what would count as direct contradiction beyond verbatim doctrine-naming mismatch.
5. [e:c:i] `wrapper inherits workflow doctrine` — implicit in every prior exclusion warrant: the wrapper loads a workflow file via `<execution_context>`, therefore the doctrine is available transitively. Not verified against the actual required-reading chain of the workflow files (see Invalid Exclusion #1).

The question the R5.17a spec asks, and that prior lanes did not always answer, is whether each of these phrases justifies the specific exclusion it was used to support — not whether the phrase can ever be true. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-17-exclusion-judgment-audit-bundle-spec.md:57-77`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-audit-spec.md:14-22`.

## Invalid Exclusions

Findings below are ordered by severity. `Invalid` means the file itself contradicts the exclusion warrant on direct reread.

### 1. [e:c+r:i] `HIGH` — The `wrapper inherits workflow doctrine` warrant for `gsd-plan-phase --reviews` fails at the workflow layer, not only the wrapper layer.

Evidence: `.codex/skills/gsd-plan-phase/SKILL.md:56-59` loads only `plan-phase.md` and `ui-brand.md` into `<execution_context>`. The wrapper does not expose `planner-reviews.md` in any form, even when the documented `--reviews` flag at `.codex/skills/gsd-plan-phase/SKILL.md:74` is active. The next layer — `plan-phase.md:5-13` — lists `ui-brand.md`, `revision-loop.md`, `gate-prompts.md`, `agent-contracts.md`, and `gates.md` in `<required_reading>`, but NOT `planner-reviews.md`. The plan-checker prompt at `plan-phase.md:823-834` does not read `REVIEWS.md` at all. Meanwhile `planner-reviews.md:7-56` is where the actual load-bearing doctrine lives: lone high-signal criticism preservation, merely-adequate categorization, addressed/deferred/rejected accounting, and the explicit rule that `lack of consensus does not automatically downgrade a criticism` (`planner-reviews.md:29`).

Why the exclusion is invalid, not merely thin: the prior bounded-adjudication argument was that wrappers can be excluded because the workflow they delegate to carries the doctrine. For `--reviews`, neither the wrapper nor its loaded workflow's required_reading chain loads `planner-reviews.md`. The inheritance claim has no transitive carrier. Any orchestrator that reads only what the wrapper loads will not encounter the anti-false-consensus doctrine at all.

Severity: `HIGH`. This is the single most load-bearing review-consumer seam in the rerun chain and is the exact path R5.16c already identified as `--reviews replanning is still an orphaned contract` at its internal r1 line 10-16. The prior call kept `gsd-plan-phase` in scope but stopped at wrapper framing; the invalidity is actually deeper.

### 2. [e:c+r:i] `HIGH` — `gsd-autonomous/SKILL.md` makes a positive false claim about pause behavior.

Evidence: `.codex/skills/gsd-autonomous/SKILL.md:49` says `Pauses only for user decisions (grey area acceptance, blockers, validation requests).` Direct rereads in prior lanes, preserved at `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md:43` citing `.codex/get-shit-done/workflows/autonomous.md:411-472`, show that autonomous mode offers `Continue without validation` for `human_needed` outcomes and `Continue anyway` for `gaps_found` outcomes, then proceeds onward. Neither is a pause. The wrapper description is not vague; it is affirmatively incorrect under the current harness.

Why the exclusion is invalid: `gsd-autonomous` is not in the audit spec's candidate exclusion-target list at `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-audit-spec.md:50-55`. That omission is itself part of what this audit must return. But even setting the read-set gap aside, the wrapper's first-invoked surface is doing active doctrinal work — it is telling operators that autonomous mode will pause on unresolved verification, when in fact it does not. Under the checkpoint-5 exit criterion that `review/closure changes preserve lone strong criticism and distinguish clean completion from debt-carrying completion where rerun quality depends on that distinction` (`.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:96-97`), a wrapper that tells operators the opposite cannot be silently excluded.

Severity: `HIGH`. Autonomous mode is the most user-invisible execution path in the harness; a false description here is the highest-leverage misframing.

### 3. [e:c+r:i] `HIGH` — `gsd-review/SKILL.md` objective still encodes the pre-Track-B generic flow.

Evidence: `.codex/skills/gsd-review/SKILL.md:3` describes the skill as `Request cross-AI peer review of phase plans from external AI CLIs` and `.codex/skills/gsd-review/SKILL.md:48-54` gives `Flow: Detect CLIs → Build review prompt → Invoke each CLI → Collect responses → Write REVIEWS.md`. No mention of `strongest justified criticism`, `merely adequate`, `later-audit risk`, `lone high-signal criticism that must survive lack of consensus`, or the anti-false-consensus synthesis posture. The actual stronger doctrine is in `.codex/get-shit-done/workflows/review.md:237-257` (synthesis categories) and `.codex/get-shit-done/references/planner-reviews.md:7-56` (consumer contract). The wrapper loads only `review.md` at `.codex/skills/gsd-review/SKILL.md:57`; it does not expose `planner-reviews.md` on the downstream side either.

Why invalid (not just under-justified): R5.16d already kept `gsd-review` in the common-core R5.17/R5.18 scope, so strictly this was not a live exclusion at the adjudication boundary. But the bundle spec at `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-17-exclusion-judgment-audit-bundle-spec.md:64-77` explicitly requires treating `first-invoked or expectation-setting` surfaces as burden-bearing. This is a first-invoked review surface whose objective text is still generic; the `Preserve and express earned distinctions explicitly. Do not let repeated naming density, shorthand, or omission quietly choose winners between live branches.` guidance at `AGENTS.md:89` applies directly. The prior lanes should have recorded this as invalidity, not merely partial propagation.

Severity: `HIGH` for `R5.17a` purposes because the wrapper is the operator's first contact with the review posture the rerun depends on.

## Under-Justified Exclusions

These are cases where the exclusion warrant is not falsified outright, but the justification offered does not carry the weight placed on it under the best-possible-outcome standard.

### 4. [e:c+r:i] `HIGH` — `gsd-verify-work/SKILL.md` two-state objective hides debt-carrying completion.

Evidence: `.codex/skills/gsd-verify-work/SKILL.md:48-54` says `Purpose: Confirm what the agent built actually works from user's perspective` and `Output: {phase_num}-UAT.md tracking all test results. If issues found: diagnosed gaps, verified fix plans ready for $gsd-execute-phase`. This encodes exactly two terminal states: clean, or fixable-via-re-execute. The actual workflow path at `.codex/get-shit-done/workflows/verify-work.md:461-483` contains a third path: `audit-open` surfaces items with status `gaps_found` or `human_needed`, presents `Proceed anyway? [Y/n]`, and on confirmation records `acknowledged gaps` and continues. That is the debt-carrying completion state R5.16b (`.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md:31`) and Checkpoint 5 exit criteria (`.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:96-97`) require to be preserved.

Why this is under-justified rather than invalid: the `thin mapper` warrant at `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-cross-vendor-opus-r1.md:41` is the strongest defense. But the wrapper objective is not a mapping — it is a doctrinal assertion about what the output can be. Under the spec question `Which wrappers are still carrying weaker execution / completion / review / closure posture at the invocation layer even if the deeper workflow is stronger?` at `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-audit-spec.md:76-77`, this is a textbook example.

Severity: `HIGH`, but open to a partial defense: if `verify-work.md` itself first grows an explicit third state with a first-class debt carrier (R5.16c Track C trunk), then this wrapper's objective becomes a thin-mapping omission rather than a doctrinal misstatement. Until that lands, exclusion remains under-justified.

### 5. [e:c+r:i] `MEDIUM-HIGH` — `gsd-execute-phase/SKILL.md` generic gate-preservation language.

Evidence: `.codex/skills/gsd-execute-phase/SKILL.md:48-63` frames the skill as `discover plans, analyze dependencies, group into waves, spawn subagents, collect results`, and at `:92-94` instructs `Preserve all workflow gates (wave execution, checkpoint handling, verification, state updates, routing)`. No mention of `human_needed` handling, override-backed deviation accounting, or debt-carrying completion. The directly contradicted workflow lines at `.codex/get-shit-done/workflows/execute-phase.md:1263-1375` are where the `human_needed` → bare-approved → `update_roadmap` path lives. R5.16d at line 18 explicitly pulled this wrapper out of governing scope citing `thin mapper`; R5.16d at line 36 confirmed the downgrade.

Why this is under-justified rather than invalid: the wrapper is genuinely thinner than `gsd-review` or `gsd-verify-work`. Most of its content is Codex adapter boilerplate and flag disambiguation. The `Preserve all workflow gates (…verification, state updates, routing)` line is not false — it is too generic to force the orchestrator to honor the debt distinction, and the distinction does not yet exist at `execute-phase.md` as a first-class carrier. If the R5.18 Track C trunk lands a debt carrier in `execute-phase.md`, then `Preserve all workflow gates` becomes adequate by transitive reference; if it does not, the wrapper's thinness is not a defense, it is a liability. Current exclusion warrant rests on a prospective workflow fix that has not happened yet.

Severity: `MEDIUM-HIGH`, conditional on Track C trunk landing. If it does not, this escalates to `Invalid`.

### 6. [e:c+r:i] `MEDIUM` — `gsd-plan-phase/SKILL.md` flag documentation for `--reviews`.

Evidence: `.codex/skills/gsd-plan-phase/SKILL.md:74` documents the flag as `--reviews — Replan incorporating cross-AI review feedback from REVIEWS.md (produced by $gsd-review)`. The description is technically accurate but bare. It does not tell the orchestrator that this mode has a distinct review-consumer contract at `planner-reviews.md:7-56`, and the `<process>` at `.codex/skills/gsd-plan-phase/SKILL.md:80-83` is the generic `end-to-end` invocation with no mode-specific preamble. This is a subset of Invalid #1, narrower because it concerns the flag doc rather than the `<execution_context>` block.

Severity: `MEDIUM`. Addressable as part of fixing Invalid #1.

## Defensible Exclusions

### 7. [e:c:i] `gsd-research-phase/SKILL.md` is genuinely defensible.

Evidence: `.codex/skills/gsd-research-phase/SKILL.md:74-223` inlines the full spawn contract — `research_type`, `key_insight`, `files_to_read`, `downstream_consumer`, `quality_gate`, and explicit handling of `RESEARCH COMPLETE` / `CHECKPOINT REACHED` / `RESEARCH INCONCLUSIVE` returns. There is no `<execution_context>` pointing to a workflow file that could silently carry different doctrine; the wrapper itself is the workflow. It does not sit on the review/completion/closure seam. The chain-tail debt-completion problem R5.16b describes does not touch it. Prior R5.16d bounded adjudication was right to leave this out.

### 8. [e:c:i] `gsd-discuss-phase/SKILL.md` is genuinely defensible.

Evidence: `.codex/skills/gsd-discuss-phase/SKILL.md:69-74` loads four workflow/template files. `.codex/skills/gsd-discuss-phase/SKILL.md:86-96` contains explicit mode routing with shell config read, and line 94-96 states `**MANDATORY:** The execution_context files listed above ARE the instructions. Read the workflow file BEFORE taking any action. The objective and success_criteria sections in this command file are summaries — the workflow file contains the complete step-by-step process with all required behaviors, config checks, and interaction patterns. Do not improvise from the summary.` This is precisely the doctrine-carrier / wrapper-cannot-substitute discipline the prior lanes' `wrapper inherits workflow doctrine` phrase only gestured at. And the skill does not sit on the review/closure seam. Exclusion is defensible.

## Presumptive Edit Targets

In decreasing order of edit urgency:

1. [d:c+r:i] `gsd-plan-phase/SKILL.md` — add `planner-reviews.md` to `<execution_context>`, expand `--reviews` flag doc to name the anti-false-consensus / lone-high-signal consumer contract, and ensure the invoked workflow layer also loads `planner-reviews.md` in `<required_reading>`. Without the workflow-layer change, the wrapper fix is cosmetic. Sources: `.codex/skills/gsd-plan-phase/SKILL.md:56-59,74`; `.codex/get-shit-done/workflows/plan-phase.md:5-13,823-834`; `.codex/get-shit-done/references/planner-reviews.md:7-56`.
2. [d:c+r:i] `gsd-review/SKILL.md` — lift the review.md synthesis categories into the wrapper `<objective>`, replace the generic `collect responses` flow language with explicit lone-high-signal / merely-adequate / later-audit / divergent-views preservation, and surface the `planner-reviews.md` consumer contract in `<execution_context>` so the review wrapper is honest about who its downstream is. Sources: `.codex/skills/gsd-review/SKILL.md:3,48-58`; `.codex/get-shit-done/workflows/review.md:237-257`; `.codex/get-shit-done/references/planner-reviews.md:7-56`.
3. [d:c+r:i] `gsd-verify-work/SKILL.md` — conditional on the Track C debt-carrier representation landing. Once `verify-work.md` surfaces an explicit debt-carrying third state, rewrite the wrapper `<objective>` to name all three terminal states rather than only `clean` and `fixable-via-execute`. Sources: `.codex/skills/gsd-verify-work/SKILL.md:48-54`; `.codex/get-shit-done/workflows/verify-work.md:461-483`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:96-97`.

## Mandatory Disposition Targets

These wrappers must be explicitly dispositioned under the R5.17/R5.18 boundary — `accept`, `revise`, `park`, or `reject` — rather than left silently deferred. Leaving them silently out of scope is itself a scope decision that needs positive justification under `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:132-140` and `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md:89-95`.

1. [d:c+r:i] `gsd-autonomous/SKILL.md:49` — mandatory, because the wrapper carries a false positive claim about pause behavior. `gsd-autonomous` is not in the audit spec's listed candidate targets. Disposition must be `revise` unless `autonomous.md:411-472` is first rewritten to honor the stated pause claim. Source: `.codex/skills/gsd-autonomous/SKILL.md:48-52`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md:43`.
2. [d:c+r:i] `gsd-ship/SKILL.md:48-52` — mandatory, because `After $gsd-verify-work passes, ship the work` assumes clean-pass semantics while `.codex/get-shit-done/workflows/ship.md:41-46` accepts `status: human_needed` with human approval. Not in candidate list. Source: `.codex/skills/gsd-ship/SKILL.md:48-52`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md:43`.
3. [d:c+r:i] `gsd-progress/SKILL.md:48-52` — mandatory, because `intelligently route to the next action` glosses over the fact that `.codex/get-shit-done/workflows/progress.md:168-203` treats verification debt as warnings-only while `.codex/get-shit-done/bin/lib/roadmap.cjs:185-195` trusts the roadmap checkbox over disk evidence. Not in candidate list. Source: `.codex/skills/gsd-progress/SKILL.md:48-52`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md:29`.
4. [d:c+r:i] `gsd-execute-phase/SKILL.md:92-94` — mandatory on explicit `accept with rationale` or `revise`, because R5.16d downgraded this on a `thin mapper` warrant conditional on future workflow fix. The disposition must be paired with the debt-carrying representation decision in `execute-phase.md`; otherwise it becomes `Invalid` rather than `defer`. Source: `.codex/skills/gsd-execute-phase/SKILL.md:48-94`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md:18,36`.
5. [d:c+r:i] `gsd-verify-work/SKILL.md:48-54` — mandatory on the same conditional basis as `gsd-execute-phase`. Source: see Finding 4 above.

## Direct File-Line Spot Checks

The following reads were executed in this lane and confirm the evidence above. No claim in this report rests solely on inference from prior-lane summaries.

- `.codex/skills/gsd-review/SKILL.md:3` — description string confirmed generic.
- `.codex/skills/gsd-review/SKILL.md:48-58` — objective and execution_context confirmed: loads only `review.md`.
- `.codex/skills/gsd-plan-phase/SKILL.md:56-59` — execution_context confirmed: `plan-phase.md`, `ui-brand.md` only.
- `.codex/skills/gsd-plan-phase/SKILL.md:74` — `--reviews` flag doc confirmed bare.
- `.codex/skills/gsd-execute-phase/SKILL.md:48-94` — objective, execution_context, process confirmed; no debt/override/human_needed naming.
- `.codex/skills/gsd-verify-work/SKILL.md:48-54` — two-state objective confirmed; `fix plans ready for $gsd-execute-phase` framing confirmed.
- `.codex/skills/gsd-discuss-phase/SKILL.md:86-96` — `MANDATORY` workflow-read discipline confirmed.
- `.codex/skills/gsd-research-phase/SKILL.md:74-223` — inlined spawn contract confirmed; no workflow file delegation.
- `.codex/skills/gsd-autonomous/SKILL.md:48-52` — `Pauses only for user decisions (grey area acceptance, blockers, validation requests)` confirmed verbatim.
- `.codex/skills/gsd-ship/SKILL.md:48-52` — `After $gsd-verify-work passes, ship the work` confirmed verbatim.
- `.codex/skills/gsd-progress/SKILL.md:48-52` — `intelligently route to the next action` confirmed verbatim.
- `.codex/skills/gsd-validate-phase/SKILL.md:48-68` — narrower scope confirmed; not currently on the review/closure seam. Defensible exclusion absent new evidence.
- `.codex/get-shit-done/workflows/plan-phase.md:5-13` — `planner-reviews.md` absent from `<required_reading>` confirmed.
- `.codex/get-shit-done/workflows/plan-phase.md:823-834` — checker `<files_to_read>` does not include `REVIEWS.md` confirmed.
- `.codex/get-shit-done/workflows/review.md:237-257` — stronger synthesis categories present confirmed.
- `.codex/get-shit-done/workflows/review.md:266-295` — `Consensus concerns:` user-facing flatten and `Consensus summary synthesized from multiple reviewers` success-criterion confirmed.
- `.codex/get-shit-done/references/planner-reviews.md:7-56` — full lone-high-signal / merely-adequate / addressed/deferred/rejected doctrine present confirmed.
- `.codex/get-shit-done/workflows/verify-work.md:461-483` — `Proceed anyway? [Y/n]` acknowledge-and-continue path confirmed.

## Contested Claims

Not every finding in this lane reaches certainty. The following are left contested rather than flattened.

- [o:c+r:i] Whether `gsd-execute-phase/SKILL.md:92-94` is better classified as `under-justified` or as `defensible given a conditional Track C workflow fix` remains contested. This lane assigns `under-justified`, but the bounded-adjudication argument that the thinness becomes adequate once `execute-phase.md` carries a first-class debt carrier is non-trivial. If the R5.18 Track C trunk lands a debt carrier, this lane should re-examine rather than assume its own verdict governs. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md:18,36`; `.codex/skills/gsd-execute-phase/SKILL.md:92-94`.
- [o:c+r:i] Whether the mandatory-disposition set should include `gsd-autonomous`, `gsd-ship`, and `gsd-progress` as R5.17/R5.18 scope or as a separate R5.19 wrapper-family sweep remains contested. This lane's position is that their invocation-surface framing is already directly contradicted at file level, so mandatory disposition cannot wait for a later lane. The opposing position — that including them expands scope past Checkpoint 5's narrowing intent at `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:79-83` — is credible and should be adjudicated at R5.17d, not resolved here. Sources: `.codex/skills/gsd-autonomous/SKILL.md:49`; `.codex/skills/gsd-ship/SKILL.md:48-52`; `.codex/skills/gsd-progress/SKILL.md:48-52`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:79-102`.
- [o:c+r:i] Whether `directly contradicted` should be defined strictly (verbatim doctrine-name mismatch) or loosely (any invocation-surface claim that misstates live harness behavior) remains contested. R5.16d implicitly used the strict reading. This lane applies the loose reading because the strict reading leaves false positive wrapper claims safely excluded — an outcome the post-falsificationist doctrine at `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:160-167` should refuse. R5.17d should rule on which reading governs. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md:18,36`; `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:160-167`.

## Open Questions

- [o:c+r:i] If `planner-reviews.md` is load-bearing enough that `gsd-plan-phase/SKILL.md` exclusion becomes Invalid when the workflow does not load it, is there a broader read-set invariant the wrappers should enforce — for example, that every reference `X.md` cited by a workflow's downstream output contract must appear in some `<required_reading>` chain reachable from the wrapper? This is a doctrine question larger than R5.17a but the evidence lane surfaced it.
- [o:c+r:i] The audit spec candidate list at `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-audit-spec.md:50-55` omits `gsd-autonomous`, `gsd-ship`, `gsd-progress`, and plausibly `gsd-validate-phase`. Answering the read-set adequacy question in the affirmative (these wrappers are missing) does not by itself decide how the adjudication should respond. It does force R5.17d to acknowledge the gap rather than treat the spec's original candidate list as scope-definitive.
- [o:c+r:i] `gsd-discuss-phase/SKILL.md:94-96` contains the strongest `wrapper-cannot-substitute-for-workflow` discipline in the audited set (`do not improvise from the summary`). Should that language become the standard required `<runtime_note>` pattern for every rerun-critical wrapper? That would reduce the wrapper-framing-drift risk this lane surfaced at its root rather than per-wrapper.
- [o:c+r:i] The prior lanes never explicitly examined `gsd-audit-fix`, `gsd-audit-uat`, `gsd-audit-milestone`, or `gsd-secure-phase` wrapper surfaces, which are review/closure-adjacent. This lane did not examine them either. That is a remaining read-set adequacy gap but does not change the R5.17a verdict.

## Read-Set Adequacy

- [e:c+r:i] The R5.17a audit spec's candidate list was not adequate. It named six wrappers (`gsd-review`, `gsd-plan-phase`, `gsd-execute-phase`, `gsd-verify-work`, `gsd-discuss-phase`, `gsd-research-phase`). Three of the most directly relevant chain-tail completion wrappers (`gsd-autonomous`, `gsd-ship`, `gsd-progress`) were missing despite R5.16b already naming their workflows as cheap-closure consumers. This is not a fatal spec flaw — R5.17a was explicitly about challenging prior exclusions, and this lane flagged the omission through the spec's own `read-set adequacy` question at `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17a-wrapper-exclusion-audit-spec.md:84-86`. But R5.17d must treat the widened set as live, not as out-of-scope by list omission.
- [e:c+r:i] The governing-input set was adequate. The prior exclusion artifacts (R5.16a/b internal + cross-vendor, R5.16c internal, R5.16d internal) together expose the exclusion heuristics cleanly enough to test them. The doctrine docs (`POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`, `AUDIT-COMPARISON-POLICY.md`, `GATES/checkpoint-5.md`, `PROTOCOL.md`) provide the anti-regret frame.
- [e:r:i] What this lane did not do: verify `.codex/get-shit-done/workflows/autonomous.md:411-472` and `.codex/get-shit-done/workflows/ship.md:41-46` line-by-line independently. It relied on the R5.16b citations of those lines, which are themselves direct spot-checks in that prior lane. If R5.17d wants sovereign standing for the `gsd-autonomous` false-claim finding, it should reread those workflow lines directly; the invalidity call at the wrapper layer is independently supported by the wrapper line alone.

## Change Summary

- [e:r:i] The bounded R5.16c/d exclusion frontier is directionally right on `gsd-review` and `gsd-plan-phase` (keep in scope) and on `gsd-research-phase` / `gsd-discuss-phase` (keep excluded). It is not right on `gsd-verify-work` / `gsd-execute-phase` (conditional, not defer), and it silently omits `gsd-autonomous` / `gsd-ship` / `gsd-progress` where invocation-surface misframing is already direct.
- [d:r:i] The narrowest scrutiny-resistant next move for R5.17d is to accept a widened exclusion frontier in which: (a) `gsd-review` / `gsd-plan-phase` remain presumptive edit targets with the workflow-layer `planner-reviews.md` fix treated as co-required; (b) `gsd-verify-work` / `gsd-execute-phase` move from `defer` to `mandatory conditional disposition`; (c) `gsd-autonomous` / `gsd-ship` / `gsd-progress` move from `silently out of scope` to `mandatory explicit disposition`; and (d) the `directly contradicted` test is restated to include invocation-surface claims that misstate live harness behavior, not only verbatim doctrine-name mismatches.
- [d:r:i] This does not promote a full wrapper-family sweep. It promotes a rule about how exclusion is done, plus three explicitly-named wrappers into the disposition ledger. R5.17d should rule on whether that narrowing holds.
