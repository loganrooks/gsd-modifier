# Evidence Architecture

## Comparison Model

- [d:r:i] The comparison space for this audit is not binary.
- [d:r:i] The working model is four-axis:
  1. original readiness mapping and doctrine
  2. the `04-17` bridge audit and its guarded-hybrid verdict as prior findings, not untouchable floor
  3. revised docs / current improved terrain map
  4. runtime / harness code and workflow behavior as first-class evidence

- [d:r:i] The still-unrealized intervention-ready map remains the comparative horizon across all four axes rather than a fifth sibling corpus.

This matters because asking only `did readiness match the docs?` or `are the docs better now?` is weaker than asking `are we now mapped strongly enough across doctrine, bridge findings, docs terrain, and runtime behavior to support ambitious structural intervention without avoidable foreclosure?`

## Corpus Sizing

- [e:b:i] Rough in-session byte-count sizing on `2026-04-18`:
  - `.planning/readiness/phase-01-rerun/` is about `316` files and roughly `840k` raw tokens
  - `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/` markdown set is about `38` files and roughly `110k` raw tokens
  - combined raw mass is roughly `950k` tokens before prompt wrapper, new instructions, or further comparison material
- [d:r:i] Conclusion: do not dump the full corpus into one audit lane, even if a model can technically hold it. Packet by question.

## Evidence Families

### Family A: Readiness Core

- `.planning/readiness/phase-01-rerun/PLAN.md`
- `.planning/readiness/phase-01-rerun/STATUS.md`
- `.planning/readiness/phase-01-rerun/PROTOCOL.md`
- `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`
- selected checkpoints, review matrices, and key audit artifacts

Role:
- reconstruct mission, doctrine, sequencing, and prior self-understanding

### Family B: `04-17` Bridge Audit

- `INDEX.md`
- `PROGRAM.md`
- `STATUS.md`
- `SYNTHESIS.md`
- `lane-02-docs-vs-readiness-crosswalk.md`
- `lane-03-reseed-judgment.md`

Role:
- preserve the bridge audit as major prior finding
- keep its guarded-hybrid result visible without treating it as axiomatic floor
- allow the bridge verdict itself to be re-audited as a candidate underreach artifact
- prevent false amnesia
- show how the first comparison was framed

### Family C: Later Docs-Refresh Work

- `lane-07-upstream-docs-update-proposal-opus-1m-r1.md`
- `lane-12-opus47-courageous-docs-refresh-recommendation.md`
- `lane-14-opus47-pr4-continuation-report.md`
- `lane-15-opus47-single-pr-description.md`

Role:
- show how the improved docs terrain map evolved after the bridge audit
- establish that the docs work was not static and not purely conservative

### Family D: Live Repo Governance

- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`

Role:
- constrain present audit design
- ensure this workspace obeys current repo doctrine

### Family E: Session Framing And Operator Pressure

- [SESSION-FRAMING-BRIEF.md](../planning-notes/SESSION-FRAMING-BRIEF.md)
- later clarifications captured into repo-local briefing artifacts
- raw logs only if a narrow dispute later requires targeted verification

Role:
- carry the live anti-tame, anti-foreclosure, anti-human-timeline framing that is not fully codified elsewhere yet
- note that this family is interpretive and situated, not neutral transcript evidence
- require later lanes to either corroborate load-bearing Family E claims from other families or flag them explicitly as operator-hypothesis support only

### Family F: Runtime / Harness Code

- `.codex/skills/*/SKILL.md`
- `.codex/get-shit-done/workflows/*.md`
- `.codex/get-shit-done/references/*.md`
- `tooling/portable-gsd/overlay/**`
- runtime-authoritative agent / wrapper / command surfaces that actually steer execution, review, or closure

Role:
- test where docs, bridge findings, and runtime behavior diverge
- surface load-bearing behavior that neither readiness doctrine nor later docs-refresh prose can settle by description alone
- make runtime-authoritative behavior a front-foot evidence family rather than a late widening move

## Recommended Packeting Discipline

- [g:r:i] Keep most substantive lanes in the rough band of `60k-140k` input tokens, unless a narrower packet is clearly better.
- [g:r:i] For sharp single-claim or stress-test lanes, prefer `20k-40k` when that yields a cleaner adversarial packet.
- [g:r:i] Packet for question-fit, not for completeness theater.
- [g:r:i] Any lane asked to make a strong judgment about `no change`, `no new lane`, or `mapping is sufficient` should receive the strongest contrary evidence too, not only the most convenient local packet.
- [g:r:i] Lanes making `mapping is sufficient` or similar claims should explicitly name a `challenge packet` rather than only an evidence packet.
- [g:r:i] Where order effects matter, read the strongest contrary evidence before the mapping or doctrine being evaluated, so the lane's baseline summary is produced under live counter-pressure.

## Candidate Lane Families

1. `mission-reconstruction`
2. `outcome-and-underreach-audit`
3. `mapping-adequacy-audit`
4. `comparative-mapping-audit`
5. `suppressed-opportunity-audit`
6. `rerun-design-audit`
7. `synthesis`
8. `operator-orchestration-pressure-audit`

## Lane-Specific Evidence Notes

- `mission-reconstruction`
  Heavy on Family A, light on B/C.

- `outcome-and-underreach-audit`
  Heavy on Family A, selected B, selected operator framing.

- `mapping-adequacy-audit`
  Heavy on A/B/C/F; runtime-vs-map reconciliation is first-class, not optional widening.

- `comparative-mapping-audit`
  Heavy on B/C/F, selective A.

- `suppressed-opportunity-audit`
  Heavy on A/F plus current conversation framing; include anti-regret doctrine.

- `operator-orchestration-pressure-audit`
  Light but explicit lane for operator-bandwidth, decision-cadence, and orchestration-pattern hypotheses when mapping failure alone is too easy an answer.

- `rerun-design-audit`
  Consume outputs of the earlier lanes rather than the entire raw corpus if possible.

## What This Architecture Is Trying To Avoid

- one huge prestige-model dump that returns a fluent but poorly packeted summary
- false convergence caused by giving sibling lanes the same impoverished structure
- treating the bridge audit as if it already closed the question it only partially opened
- treating the improved docs corpus as the whole answer
- treating raw Codex logs as a default evidence family when a distilled repo-local session brief would do the job better
