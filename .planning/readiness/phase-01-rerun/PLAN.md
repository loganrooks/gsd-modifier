# Phase 01 Rerun Readiness Plan

Status: active operational sequencing note  
Date: 2026-04-15

This artifact exists to carry the repo from the current governance/process cleanup state to a genuinely rerun-ready Phase 01 starting point.

It is not product canon. It is an execution-readiness plan for the work that must be closed cleanly before a fresh `discuss -> context -> planning` rerun for Phase 01.

If later work materially changes the sequence, update this file explicitly rather than relying on session memory.

## Current Position

- The live project state still says `Phase 01 pre-rerun boundary prepared` and `Replanning required before execution` ([STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:5), [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:30)).
- The current `01-*` bundle remains useful input, but it is not execution-approved steering ([STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:78)).
- Canon uplift work has already been performed against the main planning docs and should now be treated as part of the live canon surface:
  - [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
  - [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)
  - [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
  - [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md)
- The main governance/readiness baselines are now checkpointed, and Checkpoint 0 has been closed through a separate repair plus independent reread sequence:
  - governance baseline: `9d1e22b`
  - readiness baseline: `2ad87fc`
  - governance-audit baseline: `c38ad2a`
- The multi-layer governance audit is now a stable reference surface after its `01`-`06` repair and reread closeout:
  - [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md)
  - [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md)
  - repair commit: `dd3966c`
  - closure evidence: [GATES/checkpoint-0.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-0.md)
- Model-assignment and cross-audit policy now exists and should shape later readiness gates:
  - [01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md)
  - [02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md)
- Current policy carry-forward is:
  - keep `gpt-5.4` as repo default
  - keep `xhigh` for orchestration, exploratory research, canon synthesis, and planning
  - keep `high` for execution, debugging, validation, and verification
  - prefer cross-vendor audit over same-model effort-only reruns for high-stakes review when an external lane is available

## How We Got Here

This repo did not arrive at the current pre-rerun boundary by a straight line.

The important sequence was:

1. the `05-gap-closure` audit moved through remediation, residual-gap, challenge, docket, and sensitivity rounds to map what mature-product futures the canon should preserve
2. the first final sensitivity verdict was too narrow and too gate-like; it translated a large amount of earned doctrine into `safe enough to proceed` and `patch lightly`
3. that framing was explicitly corrected into a broader `canon uplift + milestone carry-forward + long-arc steering` response
4. that broader response was then executed against the live canon docs
5. later work exposed a second problem: even with better canon, the repo's governance/process layer was still not strong enough or clean enough to reliably carry that doctrine through day-to-day planning and delegation

So the repo's current state is not:

- `05-gap-closure is unfinished in the original doctrinal sense`

It is:

- the doctrinal/canon response from `05` largely landed
- the governance/process follow-through required to make that response trustworthy in future work is still open
- the fresh Phase 01 rerun has not happened yet, so the new canon has not yet been consumed by a new `discuss -> context -> planning` loop

This distinction matters. The next work is not mainly another broad mature-product doctrine audit. It is:

- finishing the governance/process cleanup
- verifying that the rerun will consume the uplifted canon honestly
- then actually rerunning Phase 01

## 05 Gap-Closure Carry-Forward Status

### What 05 completed

The `05-gap-closure` trail did successfully produce and land the following:

- stronger canon expression across:
  - [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md)
  - [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)
  - [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
  - [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
- clearer protection for:
  - wrapper-family plurality
  - audience-right staging
  - money-family separation
  - host-identity plurality
  - contribution/discovery status distinctions
  - layered recap/report versus challenge-result versus true event-memory doctrine
- stronger Milestone 2 and long-arc carry-forward than the original narrow sensitivity verdict would have produced

The best summary artifacts for that completed doctrinal shift are:

- [05-post-sensitivity-response-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md)
- [05-canon-uplift-milestone-2-steering-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md)
- [05-canon-uplift-execution-report.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-report.md)

### What 05 intentionally left open

The following were not "missed." They were deliberately preserved as open:

- first low-burden post-private wrapper order
- first bounded audience-right bundle
- later money-family ranking
- later host-identity ranking
- first explicit outward shell
- first true event-memory shell
- exact cadence taxonomy / first mastery read
- whether preserve-only contribution/discovery seams ever become active

These should constrain later work, not be silently closed just to make the docs feel cleaner.

### What is still outstanding from 05 in today's terms

There are three genuine carry-forward obligations still open:

1. the fresh Phase 01 rerun has not yet consumed the uplifted canon
2. the governance/process layer still needs enough cleanup that the rerun will not re-distort or underuse the doctrine `05` earned
3. the older `01-*` bundle still needs to be treated as historical input rather than live steering

### What is not currently required from 05

Unless a later gate proves otherwise, the repo does not currently need:

- another broad `05-gap-closure` mature-product doctrine round
- another full sensitivity round on the same product questions
- another canon-uplift round of the same scale before the rerun

Those would become justified only if:

- governance/process cleanup reveals that the canon uplift was actually inconsistent
- the fresh Phase 01 rerun exposes doctrine gaps large enough that the current canon still cannot steer planning honestly
- later verification shows that preserved-open questions were still quietly collapsed in practice

## Operating Principle

Do not start the fresh Phase 01 rerun while the repo is still carrying unresolved governance/process cleanup that can materially distort:

- what counts as a good planning artifact
- how delegated work is reviewed and checkpointed
- how claim types and source-basis should be interpreted
- where general rules belong versus where lane-specific residue has leaked into standing docs

The relevant question at each gate is not only `can we proceed?`

It is also:

- is this the best work we can reasonably produce at this stage?
- will this survive later stringent audit?
- are we preserving the right future-facing discipline rather than just getting unstuck?

## Model / Audit Integration Principle

Treat the current model-assignment response as live readiness input, not as side research.

For this readiness sequence:

- use the current model policy as already settled unless later evidence materially overturns it
- use cross-vendor audit selectively at load-bearing review boundaries rather than as a blanket ritual
- in this repo's current practical context, `cross-vendor` means an Anthropic Claude lane when available, not an abstract second opinion
- reserve that stronger external reread for artifacts that can materially steer:
  - governance doctrine
  - harness ownership
  - rerun-readiness verdicts
  - doctrine-sensitive Phase 01 planning

Cross-vendor audit is not currently required for:

- mechanical citation repair
- routine readiness status updates
- low-consequence wording cleanup where the governing decision is already settled

Current preferred external model choices from the model-assignment research are:

- `sonnet` for routine external audit where vendor diversity matters but the highest-cost lane is not justified
- `opus` for high-stakes architecture, canon-sensitive planning, harness ownership, rerun-readiness judgment, and stubborn-debug escalation

Do not create a dedicated cross-model-audit skill yet.

First determine whether the needed behavior can be carried cleanly by existing surfaces such as:

- [gsd-review](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md)
- [gsdr-audit](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md)
- standing workflow / AGENTS doctrine
- direct top-level orchestration for bounded high-stakes review

If those surfaces prove insufficient, that is evidence for a focused integration/design pass rather than immediate new-skill creation.

Current accepted carry-forward from the focused cross-model integration research is:

- keep cross-vendor audit as a selective, layered practice rather than a universal harness surface
- keep non-phase doctrine-sensitive rereads under direct top-level Codex orchestration plus Git checkpoint discipline
- keep doctrine-sensitive phase-plan rereads with repo-local regular GSD via `gsd-review`
- treat `gsdr-audit` as Reflect-side precedent only; selectively port protocol ideas later if they close real repo-local gaps
- treat the later likely gap as a repo-local non-phase external-reread protocol/template, not a dedicated new skill by default

## Ordered Sequence

### Checkpoint 0: Close The Active Governance Citation Bundle

Objective:
- repair the currently identified defects in the `2026-04-15-multilayer-harness-governance-audit` bundle
- close the claim-marker / citation / source-basis upgrade wave cleanly

Primary inputs:
- [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md)
- [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md)
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md)

Required work:
- fix stale or mispointed internal file-line citations in `01`-`06`
- align support markers with actual support mode, especially where `c` materially applies
- align basis markers where direct external footnotes are present
- re-review the repaired bundle rather than assuming the first pass is now trustworthy

Quality gate:
- a later reader can audit the load-bearing claims without guessing what the citations were intended to point at
- marker semantics match the current repo-wide scheme
- `06` is genuinely tightened by `08`, not merely cosmetically re-labeled
- the repaired governance audit is trustworthy enough to serve as a stable input to the normalization audit that follows

Checkpoint question:
- if a strong external reviewer reread `01`-`06`, would they find honest epistemic labeling and concrete traceability rather than presentation theater?

Commit boundary:
- do not commit before this repair-and-review loop is complete

Recommended commit split after closure:
1. `docs(governance): tighten claim typing and planning-process rules`
   - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
   - [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
   - [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
   - [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
   - [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md)
   - this readiness package under [.planning/readiness/phase-01-rerun](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun)
2. `docs(research): finalize multi-layer harness governance audit`
   - all files under [2026-04-15-multilayer-harness-governance-audit](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit)

Contingency:
- if repairing `01`-`06` exposes larger incoherence than currently known, stop and open a short corrective note before committing
- if the bundle remains unstable after one corrective pass, do not checkpoint it as if settled

### Checkpoint 1: Governance-Doc Normalization Audit

Objective:
- audit the standing governance docs for abstraction quality, ownership, duplication, and over-specific residue

Primary targets:
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
- [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)

Audit lenses:
- misplaced rule ownership
- general rule versus case-specific residue
- duplicated policy across docs
- prompt-budget / line-budget discipline
- examples replacing the more general rule they should only illustrate
- whether stable rules are expressed as general doctrine or as leftovers from one recent lane
- whether the docs are still capable of faithfully carrying the doctrinal distinctions earned in `05-gap-closure`

Known likely triggers for this audit:
- pushback language in [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:58) appears too narrowly scoped under `Research And Audit Quality`
- root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:104) to [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:106) still contains audit-era case residue (`50+`, mixed-scope architecture lane handling) where more general guidance should likely dominate
- root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141) explicitly says it should stay narrow, stable, and agent-facing, so the audit should measure actual content against that promise

Quality gate:
- each rule lives in the document whose scope actually justifies it
- each rule is stated at the right level of generality
- examples, if retained, are subordinate to the rule rather than replacing it
- root `AGENTS.md` remains slim enough to be realistic prompt-time guidance rather than a mini-handbook
- the governance docs no longer make it likely that a future rerun will flatten preserve-only seams, open questions, or long-arc doctrine through sloppy wording
- if the audit or resulting patch materially changes standing governance/harness doctrine, queue a cross-vendor reread before closure when an external lane is available

Checkpoint question:
- if we stripped the recent audit history from memory, would these governance docs still read as coherent, general operating doctrine rather than lane-specific sediment?

Commit boundary:
- if the audit produces a useful review artifact, checkpoint that artifact before the patch pass if it can stand on its own

Contingency:
- if the audit shows that the main problem is deeper than doc wording, escalate to Checkpoint 2 instead of overfitting the docs

### Checkpoint 2: Governance-Doc Normalization Patch

Objective:
- patch the governance docs based on the normalization audit

Required outcomes:
- move broad rules into broader sections when their current section is too narrow
- replace specific residue with the general rule it instantiates
- cut redundancy without losing meaning
- keep examples sparse and clearly labeled as examples
- preserve the substantive distinctions that `05-gap-closure` worked hard to earn, rather than "slimming" them away

Quality gate:
- the docs are leaner, clearer, and more generally applicable
- no important control has been lost through slimming
- the result is easier to audit, not merely shorter

Checkpoint question:
- did this patch improve the governing doctrine, or just cosmetically trim wording?

Commit boundary:
- separate this patch from the earlier citation-bundle checkpoint if the audit produced a real intermediate reasoning boundary

Contingency:
- if the patch starts to reveal that some standing rule really belongs in repo-local GSD workflow or overlay code, note that explicitly and defer the deeper move to Checkpoint 3

### Checkpoint 3: Workflow / Harness Scope Audit

Objective:
- map the relevant workflow and harness landscape before the deeper excellence audit fixes its scope
- determine what the real unit of analysis should be for the later tandem audit
- if the initial GSD mapping proves the GSD side too broad for one honest pass, complete the deeper GSD mapping and GSD-only synthesis inside Checkpoint 3 rather than pushing that mapping debt into Checkpoint 4

Primary mapping targets:
- top-level Codex orchestration and session continuity surfaces
- repo-local GSD phase flow and critical command families
- review / audit / verification / validation surfaces
- repo-local governance and guardrail docs where the harness is currently being compensated for or steered

Core questions:
- what is the actual landscape we are asking to carry excellent work?
- where are the critical path surfaces?
- where are the likely doctrine-sensitive, review-sensitive, or pass/fail-thin surfaces?
- what deserves deep audit because it is load-bearing, and what is clearly secondary?
- what is the right unit of analysis:
  - individual skills
  - workflow stages
  - runtime/harness layers
  - cross-layer seams

Quality gate:
- the scope artifact justifies the later deeper audit envelope rather than assuming it
- the result is broad enough to avoid blind spots and focused enough to support a serious later audit
- the package can point to a defensible reason why the later deeper audit covers what it covers
- the mapping output is reusable as a later harness-orientation and audit-onboarding asset rather than one-off session waste

Checkpoint question:
- have we actually mapped the landscape we want to judge, or are we still smuggling in assumptions about what is or is not important?

Commit boundary:
- if the scope artifact is independently reviewable, checkpoint it before launching the deeper audit

Current Checkpoint 3 branch:

- the initial Codex map is complete
- the initial GSD map is complete
- the initial GSD map fired the split trigger
- so Checkpoint 3 now owes:
  - deeper GSD mapping sublanes
  - a GSD-only synthesis
  - then the overall workflow / harness scope synthesis

### Checkpoint 4: Phase Workflow / Harness Excellence Audit

Objective:
- review the active phase workflow and the Codex/GSD harness layers together against the same demanding standard used in readiness prep
- test not just whether the machinery can pass a gate, but whether it reliably drives toward the best planning, research, execution, review, and verification work the repo can currently support
- preserve the already-earned GSD split rather than collapsing the repo-local GSD side back into one omnibus audit lane

Primary targets:
- top-level Codex orchestration doctrine in [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- planning/governance doctrine in [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- repo-local GSD runtime under [.codex/get-shit-done](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done)
- repo-local workflow and guardrail docs:
  - [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
  - [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
  - [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)
- the critical phase surfaces and review/checking surfaces, especially:
  - `discuss-phase`
  - `research-phase`
  - `plan-phase`
  - plan checker / verification / validation logic
  - `gsd-review`
  - Codex session continuity and delegation discipline

Checkpoint 4 should therefore be expected to consume the resolved Checkpoint 3 mapping result, including:

- one Codex-side lane for the load-bearing Codex surfaces and Codex↔repo seams justified by Checkpoint 3
- multiple GSD excellence sublanes, because Checkpoint 3 has already justified and resolved a GSD split between:
  - phase-critical workflow chain plus artifact contracts
  - active agent-role contracts plus shared doctrine
  - runtime/config/overlay truth

Do not reopen the already-resolved question of whether Checkpoint 4 should collapse back into one omnibus GSD lane. The accepted Checkpoint 3 result is that the GSD side is split into three coordinated excellence sublanes, unless later evidence shows that resolved map was materially wrong.

Core questions:
- does the current discuss -> research -> planning -> execution -> verification flow reward excellence, or mostly detect obvious failure?
- are there places where pass/fail logic is substituting for stronger opportunity-seeking or doctrine-sensitive review?
- is the plan checker strong enough, or is it too biased toward minimum viability?
- is the verification gate sufficient, or does the repo need a richer excellence-oriented pre-execution review layer?
- does the tandem Codex + repo-local GSD stack actually carry the future-aware discipline earned in `05-gap-closure`, or are docs still doing too much compensating work?

Quality gate:
- the audit produces a concrete view of where the harness is already good enough, where it is merely pass/fail-thin, and where it materially risks weaker product outcomes
- the result distinguishes:
  - doc-level doctrine problems
  - workflow-protocol problems
  - machinery-ownership problems
- the result is strong enough to decide whether actual harness changes are required before rerun

Checkpoint question:
- if strong software engineers, product designers, and external reviewers audited the active phase workflow tomorrow, would they see a system driving toward excellent work, or a system mostly optimized to get to green?

Commit boundary:
- if the audit artifact is independently reviewable, checkpoint it before any harness changes

### Checkpoint 5: Conditional Harness / GSD Follow-Through

This checkpoint is conditional on Checkpoint 4.

Run it only if the tandem workflow/harness audit concludes that important standing controls, review steps, or excellence pressures are being carried by docs because:

- repo-local GSD workflows are missing lifecycle hooks or translation points
- command/skill surfaces are missing an explicit review, reread, or disposition step
- repo-local workflow defaults materially conflict with the repo's rigor bar
- the docs are compensating for harness behavior that should be fixed closer to execution machinery

2026-04-15 reactivation note:

- the first Checkpoint 5 implementation scope was too narrow
- the accepted Checkpoint 4 workflow-chain audit had already identified follow-through on steering translation, research adequacy, permissive closure, and debt-carrying completion
- therefore Checkpoint 5 now includes workflow-chain follow-through and secondary rerun-critical wrapper alignment in addition to the already-started Track A/B/C work
- the controlling artifact for that correction is:
  - [AUDITS/checkpoint-5-reactivated-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-reactivated-launch-spec.md)

2026-04-16 scope-identity note:

- `R5.16` is the completed propagation-audit bundle, not a still-pending next step
- `R5.17` now means the exclusion-judgment audit bundle:
  - wrapper exclusions
  - chain-tail / downstream-consumer exclusions
  - governance / doctrine exclusions
  - adjudication
  - reread
- `R5.18` is the provisional promoted corrective follow-through boundary that will later govern the patch wave
- `R5.19` is the broader exclusion / modification-consideration challenge lane that now runs before or alongside final `R5.18`, because `R5.18` is itself the current modification frontier
- this distinction is intentional:
  - `R5.17` diagnoses whether exclusion judgments were sound
  - `R5.18` carries the actual newly promoted work
  - `R5.19` challenges what that work is currently excluding from modification consideration
  - keeping them separate preserves auditability and prevents the package from collapsing diagnosis into consequence

Likely targets if this becomes necessary:
- [.codex/get-shit-done](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done)
- repo-local overlay under `tooling/portable-gsd/overlay/`
- repo-local compaction-prompt design and Codex config integration, once the stable project-wide control surfaces are clear
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md) only where a doc-level policy truly needs machinery backing
- rerun-critical wrapper alignment under [.codex/skills](/home/rookslog/workspace/projects/prix-guesser/.codex/skills) after workflow changes land

Required work:
- align the phase-critical runtime-authoritative `.toml` worker prompts with the repo’s actual instruction and skill surfaces
- tighten review / closure-pressure harness surfaces so lone strong criticism and debt-carrying completion are handled more explicitly
- define the durable rule for launch/model-truth capture on doctrine-sensitive worker launches
- add workflow-chain follow-through on:
  - `discuss-phase.md`
  - `research-phase.md`
  - `plan-phase.md`
  - `execute-phase.md`
- align rerun-critical wrapper surfaces after workflow changes so invocation-layer doctrine does not lag the updated workflows

Explicitly deferred unless the active work reaches those surfaces directly:
- broad install pinning
- archival provenance replacement
- full path-portability hardening
- broader branch/worktree redesign

Quality gate:
- moved rules or controls downward only where reliability genuinely improves
- the harness now better supports excellent planning/research/review/execution work rather than merely enforcing compliance
- automation is not being used to hide judgment calls that must remain explicit and reviewable
- accepted Checkpoint 4 workflow findings are actually carried into active follow-through rather than being left behind by a narrower launch spec

Checkpoint question:
- is this a real harness defect with a clean ownership story, or are we trying to use machinery to avoid writing clearer doctrine and better review protocols?

Commit boundary:
- keep harness changes separate from governance-doc wording changes unless the coupling is truly inseparable

### Checkpoint 6: Phase 01 Rerun Readiness Verification

Objective:
- verify that the repo is actually ready to rerun Phase 01 rather than merely tired of cleanup

Required checks:
- the active governance/process bundle is cleanly committed
- the governance docs are stable enough not to distort the rerun immediately afterward
- the live canon is still the current source of truth:
  - [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
  - [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)
  - [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
  - [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md)
  - [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- there is a clear statement of what the rerun must consume and what it must not silently inherit from stale `01-*` artifacts
- no unresolved dirty worktree is carrying unrelated concern buckets
- the rerun inputs still preserve the key `05-gap-closure` carry-forward distinctions:
  - open wrapper order
  - open first audience bundle
  - open host-identity and money-family ranking
  - layered recap/report versus challenge-result versus true event-memory
  - official curated library as trust anchor with contribution/discovery status distinctions intact
- the rerun is not being asked to rediscover mature-product doctrine that the canon already settled well enough

Nice-to-have but not necessarily blocking:
- explicit disposition of `scraped-radio` branch/archive posture if it otherwise keeps creating workflow ambiguity ([STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:71))

Quality gate:
- the rerun can begin from a stable doctrine/process surface rather than from unresolved governance churn
- the rerun is positioned to do genuinely better planning work, not just to repeat the same closure/sensitivity labor under a new timestamp
- if the readiness verdict depends on doctrine-sensitive judgment rather than just mechanical closure, a cross-vendor reread should occur before declaring the repo rerun-ready when an external lane is available

Checkpoint question:
- if we reran Phase 01 today, would we be learning product truth, or would we mostly be re-litigating unstable process/governance decisions?

Commit boundary:
- if this verification is captured as an artifact, checkpoint it before running the fresh discuss pass

### Checkpoint 7: Fresh Phase 01 Rerun

Only after Checkpoint 6 is genuinely satisfied:

1. run a fresh discuss pass for Phase 01
2. produce a fresh live `01-CONTEXT.md`
3. produce a fresh Phase 01 plan from that context
4. apply a final pre-execution gate before any execution work begins

Required inputs to the rerun:
- refreshed canon docs
- stable governance/process doctrine
- explicit long-arc doctrine handling
- explicit recognition that older `01-*` artifacts are historical inputs, not execution-approved steering

Final pre-execution gate:
- the new `01-CONTEXT.md` is clearly better than the old pre-rerun bundle
- the new plan reflects current canon and current governance doctrine
- open questions are explicit rather than quietly inherited
- execution scope remains appropriately narrow for Milestone 01
- the rerun uses the stronger canon as a steering advantage rather than regressing to older asymmetries like `challenge` over-weighting, generic `hosted` language, or flattened memory/status vocabulary
- if the fresh Phase 01 plan still carries doctrine-sensitive ambiguity after internal review, run a cross-vendor reread before treating it as execution-approved when an external lane is available

## Cross-Cutting Regression Checks

Run these checks not only at the final rerun gate, but throughout the sequence whenever artifacts are revised, normalized, or translated into planning inputs.

### Canon regressions

- `challenge` should not quietly retake the role of default later wrapper just because it is the easiest shorthand.
- `hosted` should not quietly collapse capability seam, owner model, and obligation profile back into one vague noun.
- `summary` / `replay` should not quietly become closure on first explicit shell or true event-memory doctrine.
- memory surfaces should not collapse back into one flat ledger:
  - player history
  - room/group memory
  - event memory
  - content history/calibration
- `curated`, `reviewed`, and `unsupported` should not collapse back into one discovery or contribution status.
- support, access, and service obligation should not drift back into one pseudo-`premium` ladder.
- preserve-only and reversal-sensitive branches should not disappear simply because a later edit prefers cleaner prose.

### Governance-doc regressions

- root `AGENTS.md` should not reaccrete lane-specific residue when a more general rule would do.
- `.planning/AGENTS.md` should not keep broad conduct rules trapped inside sections that are too narrow in scope.
- examples should not replace the governing rule they only mean to illustrate.
- duplicated policy should not silently diverge across:
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
  - [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
  - [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
  - [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
  - [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)
- slimming should not remove distinctions that are load-bearing for future planning honesty.

### Claim / citation regressions

- load-bearing planning/process artifacts should not slide back into untyped prose when claim status materially matters.
- internal support should not be presented as if it were fresh external grounding.
- markers should not drift away from the actual support mode or actual basis doing the work.
- internal file-line citations should be rechecked after adjacent governance docs move; stale citations are a regression, not cosmetic debt.
- external-comparative supplements should not be treated as if they converted repo-specific judgment into universal best practice automatically.

### Delegation / orchestration regressions

- substantial delegated edits should not be launched into unresolved mixed worktrees.
- auditable baseline discipline should not be relaxed back into "delegate first, sort out attribution later."
- exploratory, ambiguity-heavy, scope-shaping work should not drift back into shallow main-thread local exploration when bounded worker lanes are the better shape.
- returned agent work should not skip explicit disposition:
  - `accept`
  - `revise`
  - `park`
  - `reject`
- requested spawn settings should not be spoken about as if they prove effective launch settings.

### Git / checkpoint regressions

- commits should not slide back into time-based snapshots with no real reasoning boundary.
- meaningful checkpoint boundaries should not be skipped once a coherent reviewable unit exists.
- one active change set should not silently expand into multiple unrelated concern buckets again.
- rerun prep should not proceed on top of unresolved governance/process churn.

### Phase 01 rerun regressions

- the fresh rerun should not treat older `01-*` artifacts as execution-approved steering just because they are detailed.
- the rerun should not re-import already-corrected asymmetries from older language.
- the rerun should not widen Milestone 01 scope by smuggling in Milestone 2 or long-arc futures as if they were immediate commitments.
- `LONG-ARC.md` should not be used as an excuse to import later scope; it should constrain doctrine, not explode the plan.
- the rerun should not rediscover already-earned mature-product doctrine as if it were new uncertain terrain unless a real contradiction has emerged.

## Failure Modes And Branching Logic

If Checkpoint 0 fails:
- do not continue into governance normalization yet
- finish the citation/marker repair until the active bundle is trustworthy enough to cite

If Checkpoint 1 finds mostly doc-local problems:
- proceed to Checkpoint 2

If Checkpoints 1 or 2 suggest deeper workflow/harness quality risk:
- do not jump straight to a full machinery audit or machinery patches; run Checkpoint 3 first

If Checkpoint 3 shows the landscape is broader or differently structured than expected:
- widen or refocus Checkpoint 4 explicitly rather than forcing the old audit shape

If Checkpoint 4 finds mostly process/doctrine improvements but no true machinery ownership problem:
- record the result
- avoid overbuilding the harness
- proceed without forcing Checkpoint 5

If Checkpoint 4 finds real harness ownership problems:
- run Checkpoint 5 before rerun

If Checkpoint 5 improves machinery but still leaves the repo relying on ambient operator memory:
- do not declare success; that is evidence that the follow-through was incomplete

If Checkpoint 6 shows canon still needs another uplift:
- do the targeted canon patch before rerun rather than forcing the rerun to rediscover doctrine

If the rerun's fresh discuss/context step reveals major unresolved product doctrine:
- stop before planning/execution and open the smallest appropriate doctrine-clarification pass

If the rerun starts reintroducing old asymmetries that `05-gap-closure` already corrected:
- stop and classify that as governance/canon regression, not as healthy fresh exploration

## What Is Explicitly Not Required Before The Rerun

Do not use this readiness sequence to smuggle in unrelated expansion such as:

- a new broad product-topology audit
- a full production deployment design
- broad public-hosting or monetization closure
- feature execution unrelated to Phase 01 replanning

Those may matter later, but they are not the current readiness target.

## Immediate Next Action

Immediate next action:
- run Checkpoint 1: governance-doc normalization audit

Until Checkpoints 1 through 6 are genuinely satisfied, do not start the fresh Phase 01 rerun.
