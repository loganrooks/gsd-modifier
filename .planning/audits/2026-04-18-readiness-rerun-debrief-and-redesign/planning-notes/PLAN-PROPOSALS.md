# Plan Proposals

## Evaluation Lens

Each proposal below is judged against the same questions:

- does it preserve the strongest live framing?
- does it reduce the chance of another tame or under-mapped audit?
- does it keep momentum without collapsing into ornamental prep?
- does it create clear review boundaries?
- does it leave room to escalate if the evidence says the current frame is still too weak?
- does it test, rather than quietly assume, the right unit of intervention?
- does it let runtime / harness evidence force a program-shape change if the docs-only or audit-first frame proves too weak?

## Proposal A: Immediate Main Wave

Shape:
- write one big cross-vendor audit spec now
- ask for mission reconstruction, underreach diagnosis, mapping audit, and rerun design in one sweep
- synthesize after that

Strengths:
- fastest start
- least local orchestration overhead
- useful if urgency dominates and the frame is already stable

Weaknesses:
- high risk of repeating the earlier closure bias
- too much corpus mass for one clean packet
- too easy to get a fluent generic retrospective instead of a sharply staged debrief
- too easy for `no major change needed` to survive on weak burden of proof

Verdict:
- not recommended as the main path

## Proposal B: Balanced Preparatory Phase -> Main Audit Wave -> Synthesis

Shape:
- short preparatory phase to lock framing, questions, corpus architecture, and anti-tame rules
- then launch a multi-lane main wave
- then synthesize and recommend rerun shape

Strengths:
- strong enough to prevent another weakly framed audit
- not so heavy that it delays the substantive work indefinitely
- fits the `04-17` bridge result that called for program revision before mutation
- creates clean later delegation packets
- gives us a place to decide the audit's relationship to the past before the main wave starts speaking in the past's voice

Weaknesses:
- slightly slower to first external lane
- requires discipline to keep the prep phase bounded

Verdict:
- provisional working default
- no longer sufficient as the only evaluated path

Why this remains the working default:
- [e:c+i] The bridge audit already said the next honest move was explicit program revision, not silent continuation or silent restart. Sources: .planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:50, .planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:56, .planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-03-reseed-judgment.md:102, .planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-03-reseed-judgment.md:109.
- [e:c+i] The readiness doctrine itself rejects naive pass/fail closure and insists on stronger gap exposure, anomaly accounting, and anti-regret scope judgment. Sources: .planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:87, .planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:100, .planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:132, .planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:140.
- [d:r:i] The lane-01 and lane-03 Opus results now narrow the right reading further: keep B as the bounded prep-first default, but only as `Proposal B-extended`, with runtime/harness evidence first-class, a widened proposal set, symmetric anti-tame burdens, and explicit execution-capacity assumptions.

## Proposal C: Comparative Mapping First, Then Debrief

Shape:
- first run a strong comparison between:
  - original readiness mapping
  - bridge audit conclusions
  - improved docs corpus
  - desired intervention-ready map
- only after that, run the broader readiness debrief and rerun-design audit

Strengths:
- strongest if mapping weakness is the dominant cause of underreach
- useful if we suspect the first package mostly failed because it could not see enough of the system
- likely best at surfacing unseen leverage points

Weaknesses:
- risks over-explaining every failure as a mapping failure
- can postpone the doctrinal / governance self-critique
- can delay the audit of review posture and closure bias

Verdict:
- strong fallback or intensification path
- best used as a branch inside Proposal B if early prep makes mapping deficiency look dominant

## Proposal D: Maximal Multi-Wave Program

Shape:
- deep prep
- deep mapping
- debrief wave
- doctrine wave
- rerun-design wave
- synthesis

Strengths:
- strongest epistemic coverage
- highest chance of surfacing hidden seams and suppressed opportunities

Weaknesses:
- high coordination overhead
- easiest way to postpone action indefinitely
- can generate a second-order audit labyrinth if not aggressively scoped

Verdict:
- not the default
- reserve for escalation if Proposal B reveals widespread conflict or continuing blind spots

## Proposal E: Execute-And-Learn

Shape:
- run a fresh Phase 01 under explicit learning posture before another large audit wave
- treat real execution friction as first-class evidence
- redesign the rerun program from observed breakdowns rather than from prior doctrine alone

Strengths:
- generates evidence a mapping/debrief lane cannot produce directly
- tests where doctrine, workflow, and runtime diverge under real use
- forces operator-capacity and review-bandwidth questions into the open
- can surface whether the readiness-rerun unit is itself too abstract

Weaknesses:
- risks spending Phase 01 budget on a learning pass rather than on the strongest rerun
- can create noisy evidence if the launch conditions are still too weak
- risks conflating avoidable prep failures with product truth

Verdict:
- real alternative, not rhetorical foil
- not current default while setup revisions 1-6 are still open
- should stay on live switch triggers from the first main-wave lane onward

## Proposal F: Harness-Code-First

Shape:
- treat runtime/harness code as the primary intervention surface
- audit and modify workflow, overlay, skill, reference, and agent surfaces directly
- let doctrine and readiness framing follow from what the runtime actually needs

Strengths:
- acts on the system most likely to carry or block future improvements
- directly tests whether the missing lever is in `.codex/`, overlay, or workflow machinery
- durable if the actual bottleneck is runtime-authoritative behavior rather than descriptive doctrine

Weaknesses:
- risks overcorrecting into machinery when doctrine and review posture still matter
- can blur repo-local versus upstream `gsd` ownership if scoped loosely
- easier to widen into a large implementation program prematurely

Verdict:
- real alternative, not rhetorical foil
- should remain bounded until runtime/harness evidence is packeted as first-class evidence
- should stay on live switch triggers from the first main-wave lane onward

## Recommended Path

- [d:r:i] Recommended path: `Proposal B-extended`.
- [d:r:i] That means:
  - Proposal B remains the working default
  - Proposals E and F remain live evaluated alternatives rather than later afterthoughts
  - runtime / harness evidence is first-class from the start
  - the main-wave design must be able to switch toward C, E, or F if early evidence forces it

In practical terms:

1. finish this preparatory suite
2. widen `PLAN-PROPOSALS.md` and the evidence architecture so the program shape is not silently preselected
3. review and tighten the question set, including symmetric anti-tame burdens and a generative rejected-interventions quota
4. packet runtime / harness evidence as first-class material
5. add an explicit critical-inheritance disposition step to the prep review, including the bridge audit as a candidate underreach artifact rather than a floor
6. use external review to confirm or revise the main lane architecture
7. then launch the main audit wave

## Switch Triggers

Switch from Proposal B-extended toward a stronger Proposal C, E, F, or D if any of the following appear:

- the preparatory cross-review says the current comparison frame is still too weak or too binary
- the first lane finds that major underreach was mostly caused by missing topology rather than review posture
- the docs-refresh corpus and the old readiness mapping cannot even be compared cleanly without an ontology-reconciliation lane
- multiple lanes keep disagreeing because the evidence packets are still under-specified
- early lanes show that runtime / harness divergence is the missing lever and doctrine-only redesign will keep missing it
- early lanes show that execution friction would produce more decisive evidence than another abstract audit pass
- the bridge audit reread looks more like a candidate underreach artifact than a stable program floor

Specific live switch triggers:

- toward Proposal C:
  - runtime / docs / old mapping cannot be reconciled without a mapping-heavy lane first
- toward Proposal E:
  - early lanes keep bottoming out in hypotheses about execution friction that only a live run can test
- toward Proposal F:
  - early lanes converge on runtime/harness code as the primary blocked surface
- toward Proposal D:
  - multiple strong lanes still disagree after B-extended has landed, and the disagreement is evidence-shaped rather than merely stylistic

## Anti-Tame Reminder

- [g:r:i] Do not choose Proposal A or a minimal variant merely because it feels easier to launch.
- [g:r:i] Do not choose Proposal D merely because it sounds maximally serious.
- [g:r:i] Do not let Proposal B become a polite default that wins only because E and F were never made real enough to reject.
- [g:r:i] The right choice is the one that most improves the chance of a genuinely stronger second attempt without exporting another round of underreach.
