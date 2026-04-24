# Lane 01: Opus 4.7 Audit-Setup Cross-Review

Status: cross-review artifact
Reviewer: Opus 4.7 (1M context)
Date: 2026-04-18
Target: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/`

Read set (repo-local paths only; no raw Codex logs):
- full contents of this directory (INDEX, AUDIT-CHARTER, CURRENT-STATE, ONBOARDING, SESSION-FRAMING-BRIEF, QUESTION-SET, EVIDENCE-ARCHITECTURE, PLAN-PROPOSALS, STATUS, OPUS-CROSS-REVIEW-SPEC, LAUNCH-LEDGER, lane-01 launch prompt)
- `.planning/readiness/phase-01-rerun/PLAN.md`
- `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`
- `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md`
- `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-03-reseed-judgment.md`
- `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-12-opus47-courageous-docs-refresh-recommendation.md`

## Overall Judgment

The setup is materially better than the original readiness-package framing, and it has already done real anti-closure work: it rejects docs sovereignty, names critical inheritance, imposes burden-of-proof on tame recommendations, and refuses to let the bridge audit silently widen Checkpoint 5. That is not nothing.

But it is not yet strong enough to justify launching the main audit wave. The setup carries three structural biases that, if unfixed, will reproduce exactly the kind of underreach the workspace exists to prevent:

1. It silently inherits the `04-17` bridge audit's scope as a floor, even while claiming to critically question the readiness package's own closure logic.
2. Its comparison model is triadic (old mapping / improved docs / wanted map) but excludes the runtime/harness code itself as a first-class evidence axis, which is the single surface most likely to contain the gap both prior mapping attempts missed.
3. It assumes the right next move is another readiness-style audit wave. It never exposes "execute first, learn from friction" or "change harness code directly" as competing program shapes, and it does not argue those away; it just doesn't see them.

Against the spec's own "do not accept `no further prep needed` without explicit burden of proof" rule, the setup has not yet met that burden. Concrete revisions are named below. After those revisions, the main wave is justified. Before them, launching it prematurely exports closure bias one more time.

The `../planning-notes/SESSION-FRAMING-BRIEF.md` is honest about being situated but still ends up as the load-bearing authority a later lane is most likely to trust by default. That is a risk worth correcting, not a disqualification.

## Framing Strengths

These are strengths that measurably raise audit quality, not decorative virtues:

- **Triadic comparison model instead of binary.** `EVIDENCE-ARCHITECTURE.md:5-11` explicitly refuses the "did readiness match the docs?" framing and inserts the unrealized intervention-ready map as a third axis. This is a real upgrade over the bridge audit's frame.
- **Critical inheritance named as operational stance.** `AUDIT-CHARTER.md:15` routes four dispositions (preserve / reinterpret / supersede / drop) and `QUESTION-SET.md:37-43` asks the question. This is stronger than the bridge audit's implicit "preserve what works."
- **Burden-of-proof flipped on tame recommendations.** `QUESTION-SET.md:88-95` is a five-point test for any "leave it untouched" call. That test is real, even if it is asymmetric (see §8).
- **Refusal to let Checkpoint 5 silently widen.** `AUDIT-CHARTER.md:23` preserves the bridge audit's only genuinely load-bearing guardrail — not reopening already-resolved scope by implication — without using it as a pretext to freeze everything.
- **Explicit self-flagging of the session brief as situated.** `SESSION-FRAMING-BRIEF.md:12-16` refuses to pass itself off as neutral evidence. That is epistemically honest and unusual.
- **Packeting discipline codified up front.** `EVIDENCE-ARCHITECTURE.md:83-85` names the 60k–140k band, bans completeness theater, and requires strong contrary evidence in lanes making "mapping is sufficient" claims. This forecloses the worst single-prestige-dump failure mode.
- **Plan Proposal B correctly rejects A and D as defaults** for the right reasons (A: inherits corpus-dump failure; D: coordination labyrinth).

## Framing Weaknesses

### 1. Bridge-audit scope treated as floor, not as finding

This is the most load-bearing weakness. `AUDIT-CHARTER.md:6-7` and `CURRENT-STATE.md:9-12` adopt the bridge audit's verdict ("revise + guarded hybrid reseed"; "not directionally wrong"; "under-grounded but not wrong") as settled starting ground. `AUDIT-CHARTER.md:21` makes "do not mutate the readiness package" a non-goal, citing `lane-03-reseed-judgment.md`.

But the bridge audit was itself produced under the same doctrine the new audit is now trying to escape. Its conclusions are moderate-revision recommendations. If the readiness package underreached, the bridge audit's "small hybrid reseed + bounded reconciliation subphase" recommendation is itself a candidate artifact of that underreach pattern, not a neutral starting point. The new workspace rebels against readiness-package closure bias while silently inheriting bridge-audit closure bias.

The test here: the charter permits questioning whether `05-gap-closure` was tame, but it does not permit questioning whether the bridge audit's verdict itself was tame. That asymmetry is not argued for. It should be.

### 2. Triadic comparison excludes runtime/harness code as evidence

`EVIDENCE-ARCHITECTURE.md:5-9` names three axes:
1. original readiness mapping/doctrine
2. revised docs corpus
3. wanted intervention-ready map

Missing axis: **runtime/harness code as first-class evidence** — `.codex/skills/`, `.codex/get-shit-done/`, agent frontmatter, workflow template files, hook scripts, skill `SKILL.md` files, overlay sources. Family D in `EVIDENCE-ARCHITECTURE.md:59-65` names *governance docs only* (AGENTS.md, WORKFLOW.md, AI-GUARDRAILS.md, ARTIFACT-GOVERNANCE.md); it does not name the shipped harness that those docs describe.

This matters because the dominant mapping failure mode for systems like this is not "docs disagree" but "both the mapping docs and the improved docs describe a system that diverges from what actually runs." The improved docs refresh (`lane-12-opus47-courageous-docs-refresh-recommendation.md:43-79`) explicitly added mechanical doc-parity tests *precisely because* drift-from-runtime is the failure mode that re-drifts every release. If the new audit does not treat runtime as first-class evidence, it cannot detect a case where the old mapping and the improved docs both describe `.planning/`-shaped doctrine while the actual weakness lives in `.codex/skills/` or the Codex overlay layer.

`EVIDENCE-ARCHITECTURE.md:105-106` says lanes can be "widened to direct runtime or docs-vs-runtime evidence if needed." That is back-foot. It needs to be front-foot.

### 3. "Readiness rerun" as unit smuggles in the answer

The entire workspace is named and scoped around redoing a readiness-package attempt better. That is a meaningful choice that is never argued for. Four candidate shapes that the charter does not evaluate:

- **execute-and-learn**: run a fresh Phase 01 imperfectly under explicit learning posture, let real execution friction expose the actual harness/mapping gaps, then redesign from observed evidence
- **harness-code first**: modify `.codex/skills/`, `.codex/get-shit-done/`, workflow templates, and overlay code directly, with docs as downstream consequence
- **operator-capacity first**: diagnose review-bandwidth, taste, and decision-pattern constraints at the operator level and design around them
- **abandon readiness-rerun as a unit**: conclude that the readiness-package idiom (checkpoints, seams, doctrine rounds) is itself a closure-bias amplifier and stop doing them

None of these may survive scrutiny. But they are not in the option space the setup evaluates. "Do a better readiness attempt" is assumed, not earned. That is quiet minimal-change bias, one level up from the one the charter correctly identifies.

### 4. Vocabulary lock-in

The setup inherits post-falsificationist / anti-regret / seam-category / preserve-only-vs-reversal-sensitive / inheritance-disposition vocabulary from the readiness doctrine (`POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md` throughout). That vocabulary is genuinely sophisticated, and the setup uses it capably. But if the vocabulary itself is part of what produced tame closure — because it makes moderate, locality-respecting, non-promotion-defending judgments feel rigorously categorized rather than weak — importing it wholesale will reproduce the same failure. The new audit should audit the vocabulary, not only the conclusions reached inside it.

No question in `../planning-notes/QUESTION-SET.md` tests this. The closest is the "critical inheritance audit" (`QUESTION-SET.md:37-43`) but it asks about *parts* to preserve/supersede, not about the doctrine's language as a whole.

### 5. Single-reviewer prestige-model path

The setup names this cross-review as an Opus 4.7 xhigh single-artifact step (`OPUS-CROSS-REVIEW-SPEC.md:7`). The doctrine `POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:104-113` explicitly bans letting a single aggressive artifact become sovereign. That creates a structural tension: the cross-review mechanism is the exact shape the doctrine warns against. The setup does not address this tension. It should either:
- commission parallel cross-reviews (e.g., two independent lanes with a later adjudication), or
- explicitly demote any single cross-review output to "challenge input, not governing doctrine," including this one.

### 6. "Agentic execution capacity" gestured at but never specified

`AUDIT-CHARTER.md:16` and `SESSION-FRAMING-BRIEF.md:25` both warn that ordinary human-timeline assumptions should not quietly narrow the feasible intervention set. Good. But neither states the assumed execution model. What is the working assumption? Single-operator orchestrating parallel Claude+Codex lanes on a weeks-scale budget capable of multi-module refactors? A solo week-scale human effort? Something else? Without stating this, the disclaimer is not load-bearing. Later lanes proposing a small intervention can still say "larger was considered and felt too big" without a test of whether "too big" was measured against a realistic agentic budget or a defaulted human one.

### 7. No structural forcing function for suppressed-opportunity generation

`QUESTION-SET.md:45-50` asks about suppressed opportunities. But it asks *as a question to answer*, not *as a quota to meet*. A compliant-but-tame lane can answer "we did not identify significant suppressed opportunities beyond those the bridge audit already named" and be technically responsive while reproducing closure bias. The strongest generative version — "each lane must identify at least N interventions it considered and rejected, with explicit regret analysis per intervention" — is not in the spec. It should be.

## Session-Brief Distortions Or Limits

`../planning-notes/SESSION-FRAMING-BRIEF.md` does its job but also does too much. Specific issues:

- **"Preserve multiple excellent future options" is open enough to justify any moderate intervention.** The framing is abstract — it does not name which futures are currently at risk of foreclosure or what an option-preserving vs option-closing recommendation would concretely look like. A later lane can align with this framing by recommending almost anything.
- **"Critical inheritance" is doing philosophical work without operational tests.** The brief tells a later reviewer that the right relationship to the past is "critical inheritance." It does not provide a test for when a specific inheritance-disposition call is right. Without that, the phrase functions as a consolation frame that licenses moderate moves.
- **The "agentic execution" pointer is a gesture, not a spec.** As noted in §6 above, the brief signals that larger interventions may be tractable but does not specify the assumed execution model. This weakens the load-bearing anti-human-timeline doctrine at exactly the point where it needs teeth.
- **The brief positions itself as the primary session-record surrogate.** `SESSION-FRAMING-BRIEF.md:9` says it should be read as the primary session-level briefing artifact. Combined with the spec's instruction to not read raw Codex logs, that gives this artifact more gravitational pull than its author intended. An external reviewer who treats it as situated but de facto load-bearing is acting reasonably. The setup should either produce a bounded `SESSION-EXTRACTS.md` with verbatim quotes on load-bearing claims, or de-emphasize the brief's authority more forcefully than its own hedging already does.
- **The framing additions themselves have low falsifiability.** "The first readiness package likely underreached in part because its map of the harness was too weak" (`SESSION-FRAMING-BRIEF.md:22`) is phrased as diagnosis but is not falsifiable as stated. What evidence would refute it? If the answer is "none of the evidence we plan to read can refute it," the framing is premise-smuggling.

The brief should either be rewritten to make each framing addition falsifiable, or explicitly demoted to "operator hypothesis, not audit premise." The current posture — "situated but still primary" — is the worst of both.

## Missing Questions

The current question set is good but has specific gaps. The following questions are load-bearing and not in `../planning-notes/QUESTION-SET.md`:

1. **Was the bridge audit's verdict itself tame?** If it was produced under the same doctrine that produced the readiness underreach, its "small hybrid reseed + bounded reconciliation subphase" recommendation is a candidate artifact of that pattern, not a neutral premise.

2. **Is "another readiness attempt" even the right shape?** Name and evaluate at least three alternatives: execute-and-learn, harness-code-first, operator-capacity-first. Do not assume the answer.

3. **Where did the mapping agree with the docs and both disagree with the runtime?** This is the failure mode the triadic comparison cannot see. The improved docs refresh explicitly added doc-parity tests because this is the dominant drift mode in the shipped `gsd` corpus (`lane-12-opus47-courageous-docs-refresh-recommendation.md:70-79`).

4. **What surfaces were invisible to both the readiness mapping and the improved docs?** `.codex/skills/`, `.codex/get-shit-done/workflows/`, overlay sources, hook scripts, agent frontmatter contents (not just names), SKILL.md files — are any of these not read by either map?

5. **Is the underreach an operator/review-bandwidth pattern rather than a mapping pattern?** The readiness package was produced by one operator with one reviewer pool. If the dominant cause is not mapping weakness but operator-bandwidth or operator-taste constraint, no mapping intervention will fix it. At minimum name this hypothesis so later lanes can falsify or sustain it.

6. **What execution-capacity assumption is the rerun designed against?** State it concretely. Single-operator agentic Claude+Codex lanes, weeks-scale, multi-module refactors permitted? Something else? Without this, "feasible" is undefined.

7. **What would falsify the framing additions in `../planning-notes/SESSION-FRAMING-BRIEF.md`?** For each bullet under "Core Framing Additions," what evidence would force its retraction? If the answer is "nothing in the evidence architecture can touch it," the framing is a premise.

8. **For each piece of readiness doctrine, what inheritance disposition applies?** Not "which parts?" — that lets the audit cite general categories. Require an explicit matrix: e.g., `POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md` → preserve / reinterpret / supersede / drop, with reasoning per disposition. `QUESTION-SET.md:77-87` promises the register but no question forces it at element granularity.

9. **What rerun design would be proposed if the `04-17` bridge audit had not happened?** A thought-experiment that forces the audit to disambiguate which constraints are earned doctrine versus bridge-audit inheritance.

10. **Is the post-falsificationist vocabulary itself a closure-bias amplifier?** Sophisticated, locality-respecting categorization language can make tame recommendations feel rigorous. Test the language, not only the outputs.

## Plan-Proposal Critique

The current proposals (A: immediate wave; B: balanced prep + wave + synth; C: mapping-first; D: maximal multi-wave) all share an assumption: the path to a better readiness is more readiness-style audit work. The anti-tame reminder at the end of `PLAN-PROPOSALS.md:128-132` forbids picking A for easiness or D for seriousness-theater, but does not require evaluating proposals that fall outside the audit-first paradigm.

### Missing: Proposal E — Execute-and-Learn

Run a fresh Phase 01 explicitly as a learning instrument. Accept that the execution will be imperfect. Use the concrete friction points (where doctrine was unworkable, where the harness refused to support what the plan needed, where review bandwidth collapsed, where the runtime diverged from the plan) as first-class evidence for the readiness rerun design. Then redesign from that evidence.

Strengths:
- generates evidence that no mapping audit can produce
- defeats the failure mode where both maps agree but neither matches runtime
- forces the operator/bandwidth question into the open
- makes the rerun design answerable to something other than prior doctrine

Weaknesses:
- risks spending Phase 01 budget on a learning exercise instead of shipping product
- creates a commit record on the main branch that later lanes must respect
- less neat than an audit wave

Verdict: at minimum this proposal must be named, evaluated, and argued-against explicitly before being excluded. The current setup does not even see it.

### Missing: Proposal F — Harness-Code-First

Treat the harness itself (`.codex/skills/`, `.codex/get-shit-done/`, workflow templates, overlay, hooks, agent files) as the primary intervention surface. Propose concrete code-level changes (new skills, modified workflows, replaced SKILL.md files, restructured overlay boundaries) and let docs follow. This flips the common assumption that the harness is downstream of doctrine.

Strengths:
- directly modifies the system whose behavior the readiness package was trying to improve
- makes improvements durable against future doctrine drift
- measurable: code either compiles, runs, and passes tests, or it doesn't
- the improved docs refresh already showed that locking doc truth to runtime via tests is tractable; the symmetrical move is locking harness behavior to explicit design rather than accrued tradition

Weaknesses:
- risks over-investing in machinery that doctrine should own
- ownership boundary with upstream `gsd` is nontrivial

Verdict: must also be named and evaluated. The existing Checkpoint 5 work already moves partly in this direction; the new audit should be able to propose expanding that, not just refining doctrine around it.

### Revised Recommended Path

- Extend `../planning-notes/PLAN-PROPOSALS.md` to include E and F as evaluated proposals, not footnotes.
- Keep B as a plausible default, but require the main wave spec to spell out why E and F were rejected if they are rejected.
- Preserve the B→C switch trigger and add B→E and B→F switch triggers: for E, "early lanes cannot answer mapping questions without runtime evidence that only execution produces"; for F, "early lanes converge on `the harness itself is the missing lever`."

### On the Current B Recommendation

Proposal B is not wrong. It is the right default *inside the audit-first paradigm*. But the recommendation that B is the right choice `PLAN-PROPOSALS.md:52-57` rests on an unargued assumption that the audit-first paradigm is correct. Until E and F are evaluated, that recommendation is under-argued.

## Evidence-Architecture Critique

Strong parts, preserved:
- packeting bands (`EVIDENCE-ARCHITECTURE.md:83-85`)
- explicit "don't dump the whole corpus" rule
- named families with roles
- explicit anti-false-convergence guidance for sibling lanes

Weaknesses:

1. **Missing family: runtime/harness code.** Create Family F explicitly: `.codex/skills/*/SKILL.md`, `.codex/get-shit-done/workflows/*.md`, `.codex/get-shit-done/agents/*.md`, `.codex/get-shit-done/references/*.md`, hook scripts, overlay sources. This is the single largest evidence gap.

2. **Missing family: operator/behavioral signal.** If underreach is partly a pattern of operator-taste, review-bandwidth, or decision-cadence constraint, neither docs nor runtime evidence will surface it. Candidate signals: commit cadence, decision-reversal history in `STATE.md`, how many successive lanes ran on the same doctrine before a contradiction was admitted, which classes of recommendation the operator consistently rejected. A single bounded lane can cover this without ballooning scope.

3. **Family E (session framing) is load-bearing but soft.** As noted in §Session-Brief above, the brief's authority is higher than its evidential rigor justifies. Bound this family more tightly: require any load-bearing claim sourced to Family E to be either (a) corroborated from Family A-D or (b) flagged as operator-hypothesis.

4. **No explicit lower bound on packet size.** The 60k-140k band is a ceiling. For sharp single-claim lanes, 20-40k is often stronger. State this.

5. **"Strongest contrary evidence" rule is asserted but not operationalized.** `EVIDENCE-ARCHITECTURE.md:85` says lanes making "mapping is sufficient" or "no change needed" claims should receive strongest contrary evidence too. There is no mechanism. Require the lane task-spec template to include a "challenge packet" section naming, by path, the strongest contrary artifact that lane must read.

6. **Packeting is designed for content, not for position.** No rule yet about ordering: when a lane is reading Family A (old readiness) and Family C (improved docs), which should it read first? Order effects are real in single-pass audits. Recommend: require lanes to read the stronger-contrary evidence *first*, so their summary of the weaker side is produced under already-internalized counter-pressure.

7. **Bridge-audit Family B is treated as settled history, not as a candidate finding itself.** Per §1 above, the bridge audit's conclusions should be read as candidate under-reach artifacts, not as scope constraints. Update Family B's role accordingly.

## Tame-Recommendation Failure Modes

The existing burden-of-proof rule (`QUESTION-SET.md:88-95`) is a five-point test for any "leave untouched / leave local / out of scope" claim. It is real. It is also insufficient against these modes:

1. **Technically-answered, structurally-tame.** A lane can respond to all five questions with short, formally-adequate answers and still recommend minimal change. "Surface was adequately mapped for scope. Upside considered and rated lower-priority. Opportunity cost is modest. Execution would require cross-team coordination. Trigger to reopen: next major feature push." All compliant; all tame. Mitigation: require not just *answers* but *specific artifacts or observations* supporting each answer, with citations.

2. **Asymmetric burden.** The rule applies only to "leave untouched" calls. No symmetric rule requires every *intervention* recommendation to state what futures it forecloses and what reversal triggers exist. This silently favors moderate-sized interventions (no burden of proof from either direction) over large ones (trigger review concerns from one direction) and against non-intervention (triggers this rule). Mitigation: extend the burden symmetrically — every intervention recommendation must also answer what futures it forecloses, what reversal costs accrue, what signal would indicate it was wrong.

3. **Nothing forces surfacing of opportunities the audit did not consider.** "Don't know what you don't know" defenses work. Mitigation: add a quota — every lane must identify ≥3 interventions it considered and rejected, with named regret analysis per rejection. This is generative anti-tame.

4. **Non-promotion defaults live in the frame, not only the conclusion.** The doctrine (`POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:132-140`) asserts non-promotion is not a neutral default, but the evidence architecture still packetizes *per question*, which is a non-promotion-shaped structure. A question that is not asked cannot be answered. Mitigation: before packeting, run an adversarial "what questions are we not asking and why" pass against the question set.

5. **Prestige cross-review as tame-recommendation shield.** A single-reviewer Opus/Claude output saying "the frame is sufficient" satisfies the letter of cross-vendor audit without satisfying its intent (the doctrine explicitly warns against sovereign single-artifact cross-review). This cross-review itself is at risk of being used this way. Mitigation: explicitly demote any single cross-review (including this one) to challenge-input-only status; require parallel independent cross-reviews before any "launch justified" decision is structurally binding.

6. **Compliance-with-doctrine as tameness amplifier.** A lane that follows every rule in `POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md` and `AUDIT-COMPARISON-POLICY.md` produces a document that looks rigorous. The doctrine is necessary; it is not sufficient. Mitigation: require each lane's synthesis section to include a "doctrine-independent check" paragraph — what would this recommendation look like stated without the doctrine's vocabulary, to a reviewer who has never read it?

## Recommended Revisions Before Main Wave

Order roughly by leverage:

1. **Add Proposals E (execute-and-learn) and F (harness-code-first) to `../planning-notes/PLAN-PROPOSALS.md`**, evaluate honestly, name explicit switch triggers for each. Do not rubber-stamp B; argue for it against the fuller option set.

2. **Extend the comparison model to four axes.** Runtime/harness code becomes the fourth axis in `EVIDENCE-ARCHITECTURE.md:5-9`. Create explicit Family F for runtime evidence. Update `../planning-notes/QUESTION-SET.md` mapping-adequacy questions to require runtime-vs-map reconciliation per family.

3. **Re-open the bridge audit as candidate under-reach artifact, not scope constraint.** Rewrite `AUDIT-CHARTER.md:6-7` and `CURRENT-STATE.md:9-12` so bridge conclusions are read as prior findings under the same doctrine that produced the original underreach, discoverable rather than axiomatic. Add explicit question 9 from §Missing Questions.

4. **Add generative anti-tame quota.** Every main-wave lane must identify ≥3 interventions considered and rejected, with named regret analysis. Add to `QUESTION-SET.md:76-87` and to the lane task-spec template.

5. **Make the burden-of-proof rule symmetric.** Apply it to every intervention recommendation (what futures does this foreclose, reversal cost, refutation signal), not only to "leave alone" calls. Update `QUESTION-SET.md:88-95`.

6. **Name the assumed execution-capacity model concretely.** State in `../governance/AUDIT-CHARTER.md` or `../planning-notes/SESSION-FRAMING-BRIEF.md`: single-operator orchestrating parallel Claude+Codex lanes over weeks-scale budget, capable of multi-module refactors, bounded upstream `gsd` ownership, explicit budget of N cross-vendor audits. Without this, the anti-human-timeline disclaimer has no teeth.

7. **Demote single-reviewer cross-reviews.** Any single cross-review output (including this one) is challenge-input, not governing conclusion. Either commission parallel independent cross-reviews before "launch justified" becomes binding, or explicitly allow the operator to accept the risk in writing. Update `../review-specs/OPUS-CROSS-REVIEW-SPEC.md` and `../governance/AUDIT-CHARTER.md` accordingly.

8. **Supplement or bound `../planning-notes/SESSION-FRAMING-BRIEF.md`.** Either (a) produce a bounded `SESSION-EXTRACTS.md` with verbatim quotes on each load-bearing framing claim, or (b) explicitly rewrite each bullet in "Core Framing Additions" to be falsifiable (what evidence would refute it?). Do not leave framing claims as situated-but-authoritative.

9. **Require inheritance-disposition matrix at element granularity.** Not "which parts to preserve?" but a table: element × {preserve, reinterpret, supersede, drop} × rationale. Apply to the top ~15 load-bearing readiness doctrines/artifacts. Add to `QUESTION-SET.md:37-43`.

10. **Add operator/behavioral evidence lane.** A single bounded lane examining whether underreach correlates with operator-bandwidth or decision-cadence patterns. Does not need to be large; needs to exist so the mapping-failure hypothesis is not uncontested.

11. **Order effects in packeting.** Require lanes with "is mapping sufficient?" claims to read the strongest contrary evidence (runtime, docs-vs-runtime drift evidence, unexplored surfaces) *before* reading the mapping they are evaluating. Update `../governance/EVIDENCE-ARCHITECTURE.md`.

12. **Audit the vocabulary.** Add a single short diagnostic question in `../planning-notes/QUESTION-SET.md`: "restate this lane's recommendation in language that does not use post-falsificationist / anti-regret / seam-category / inheritance terms. Does the recommendation survive translation?"

## Whether Launch Is Justified Yet

**No. Not yet.**

The setup is close. It has done substantial anti-closure work, and its bones are better than the readiness-package's own framing was. A rushed "yes" on the grounds that "the setup looks more organized than what produced the underreach" would itself reproduce the tame-recommendation failure mode the setup is trying to escape. Organization is not a substitute for corrected biases.

Specifically, under the spec's own `If Recommending No Major Revision` clause (`OPUS-CROSS-REVIEW-SPEC.md:73-79`), launch would require justifying:

- **why the current frame is strong enough** — it is not, per §§Framing Weaknesses 1-7
- **why the current question set is not leaving material gains on the table** — it is, per §Missing Questions items 1-10
- **why the current plan architecture is not prematurely narrowing the rerun** — it is, per §Plan-Proposal Critique (Proposals E and F not evaluated)
- **why a stronger preparatory phase is unlikely to materially improve the second attempt** — the revisions in §Recommended Revisions 1-6 are high-leverage and bounded; a stronger prep phase is likely to materially improve outcomes

None of these burdens are met. Launch must wait for at least the high-leverage revisions (1-6 above). Revisions 7-12 are strongly preferred but not strict blockers.

After those revisions, launch is justified, and the B→E and B→F switch triggers should be live from the first lane forward.

One last explicit note, per the spec's required posture:

- **Human-timeline bias**: present in the unspecified execution-capacity assumption (§Framing Weaknesses 6). Addressed by revision 6.
- **Prestige-model bias**: present in the single-Opus-cross-review path (§Framing Weaknesses 5). This review itself is at risk of being used as sovereign-by-style. Addressed by revision 7.
- **Quiet minimal-change bias**: present most sharply in (a) treating the bridge-audit verdict as floor (§Framing Weaknesses 1), and (b) assuming "another readiness attempt" is the right unit (§Framing Weaknesses 3). Addressed by revisions 1 and 3.

Naming the stronger program shape concretely: the strongest available program shape is **Proposal B-extended**: the current B preparatory phase plus revisions 1–6, with Proposals E and F on live switch triggers, runtime/harness code as first-class evidence, symmetric burden of proof, and generative anti-tame opportunity quotas. That is what a genuinely harder second attempt looks like without collapsing into D-shaped labyrinthine coordination.

Do not launch the main wave yet. Land revisions 1–6, then launch.
