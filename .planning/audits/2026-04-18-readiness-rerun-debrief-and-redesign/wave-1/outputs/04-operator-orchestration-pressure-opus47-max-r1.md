# Wave-1 Output: Operator Orchestration Pressure

Status: first draft lane output
Date: 2026-04-19
Lane: `operator-orchestration-pressure`
Spec: [`wave-1/specs/04-operator-orchestration-pressure-spec.md`](../specs/04-operator-orchestration-pressure-spec.md)
Packet: [`wave-1/packets/04-operator-orchestration-pressure-packet.md`](../packets/04-operator-orchestration-pressure-packet.md)

Stages consumed:

- Stage 0 spine: read in full.
- Stage 1 operator/orchestration packet: read in full. Where a cited file (`plan-phase.md`, `review.md`) exceeded useful budget, I relied on its header and the passages the Stage-1 surfaces already quote.
- Stage 2 challenge packet: opened and read. The bridge-audit `SYNTHESIS.md`, the Codex-side load-bearing audit, the Checkpoint 3 GSD surface map, and the Surface B prelicensing pass are load-bearing against the operator-pressure reading, so they appear in the alternative-explanation notes rather than as a parallel branch.

---

## Overall Operator-Pressure Judgment

- [d:r:i] Operator and orchestration pressures were real, concrete, and locally load-bearing, but they were mostly `amplifying pressure` rather than `primary causal pressure`. They made existing mapping, doctrine, and intervention-shape weaknesses harder to correct cleanly. They did not by themselves produce the underreach the audit is investigating.
- [d:r:i] The one area where operator pressure is closer to `primary` is `vigilance-heavy launch-truth discipline`. Effective sandbox / approval / model truth depends on an operator manually invoking `capture_launch_truth.py` after each doctrine-sensitive spawn, with no self-proving machinery carrying that burden. That pressure is structural, not mood-based, and shows up directly in artifact truth rather than only in cadence feel. Evidence: [`AI-GUARDRAILS.md:87`](../../../../../AI-GUARDRAILS.md), [`WORKFLOW.md:71-82`](../../../../../WORKFLOW.md), [`checkpoint-4-codex-load-bearing-surfaces-and-seams.md:48,72`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md).
- [d:r:i] Almost every other operator-pressure candidate has a stronger mapping, doctrine, or intervention-shape explanation already on the record in the Stage 2 challenge packet. That is why this lane deliberately avoids collapsing the readiness underreach into `one operator under load`.
- [g:r:i] Failure mode this lane actively refuses: treating operator pressure as a universal solvent that absorbs mapping weakness, closure-biased doctrine, and under-imagined alternatives into one generic `overloaded operator` story. That posture is explicitly named as a failure condition by the charter and by this lane's spec. Sources: [`AUDIT-CHARTER.md:20`](../../governance/AUDIT-CHARTER.md), [`wave-1/specs/04-operator-orchestration-pressure-spec.md:27-29,62-66`](../specs/04-operator-orchestration-pressure-spec.md).
- [g:r:i] Because multiple candidate pressures initially looked `primary`, I opened the Stage 2 challenge packet before finalizing this judgment (as the packet requires). The challenge stage materially downgraded three of them to `amplifying` or `weak/post-hoc`.

---

## Operator-Pressure Register

The register below classifies each observed pressure into one of three tiers:

- `primary causal pressure` — the pressure itself produced a load-bearing underreach-family effect that would not otherwise be present.
- `amplifying pressure` — the pressure made an already-existing mapping, doctrine, or intervention-shape weakness harder to correct, slower to notice, or more expensive to fix.
- `weak / post-hoc explanation` — the pressure is present and describable, but mapping, doctrine, or intervention-shape reasoning explains more of the observed outcome, and this lane should not lean on it.

Each row names: `pressure`, `what it looked like in artifacts`, `tier`, `best alternative explanation on the record`, `evidence that would downgrade it`, `evidence that would upgrade it`.

### OP-01 — Single-operator multi-lane orchestration cadence

- Pressure: one operator running parallel Codex and Claude lanes across `Checkpoint 5`, the `04-17` bridge audit, the `2026-04-18` debrief/redesign workspace, and the commentary corpus in the same multi-week window.
- Artifact signal: the accepted execution-capacity assumption is codified as `one operator orchestrating parallel Codex and Claude lanes over a multi-week budget`, and the charter already flags that assumption as `[d:r:i]` rather than settled. Source: [`AUDIT-CHARTER.md:21`](../../governance/AUDIT-CHARTER.md).
- Tier: `amplifying pressure`.
- Best alternative explanation: much of what looks like cadence strain is really `intervention-shape` debt. `Checkpoint 5` kept subdividing (`R5.16` → `R5.17a-e` → `R5.18a1, a2, b, c, d` → `R5.19a1..a5, b1..b5, c1..c5, d1..d4, e`) primarily because the first boundary was wrong, not because the operator ran out of calendar. The subdivision cascade is visible even in an idealized staffing model. Sources: [`phase-01-rerun/STATUS.md:111-143`](../../../../readiness/phase-01-rerun/STATUS.md), [`checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md:29-198`](../../../../readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md).
- Downgrade signal: if Wave 1 and Wave 2 each close in a single generation without subdivision cascades, cadence load is not doing much load-bearing work.
- Upgrade signal: if a second major checkpoint reopens after fewer-than-expected reviews purely because the operator could not hold the whole surface in one thread.

### OP-02 — Subdivision-into-sublanes as local coping

- Pressure: each time a bounded bundle returned mixed results, the response was to split it (`a/b/c/d/e`, then `a1/a2`, then `d1/d2/d3/d4`). This keeps individual worker prompts inside budget and inside reviewable scope, but it also produces a large per-bundle orchestration surface.
- Artifact signal: the `R5.19` bundle was explicitly described as `parallel family cluster rather than three monolithic lanes` because `proving exclusion and mapping under-considered files is intensive enough that monolithic a/b/c lanes would silently lower rigor`. Source: [`phase-01-rerun/STATUS.md:111-118`](../../../../readiness/phase-01-rerun/STATUS.md).
- Tier: `amplifying pressure` when splitting is driven by real rigor debt; `weak/post-hoc` when it becomes a default cadence move that postpones integration.
- Best alternative explanation: the subdivision is partly a mapping-quality signal. The original Checkpoint 5 scope was `too narrow` (`STATUS.md:16-17`); the corrected scope was still `incomplete on propagation ownership` (`STATUS.md:17-18`). Each split is a response to a mapping gap that the prior split did not yet see. This is not the operator being tired; it is terrain being under-mapped. Sources: [`phase-01-rerun/STATUS.md:14-34`](../../../../readiness/phase-01-rerun/STATUS.md), [`checkpoint-4-codex-load-bearing-surfaces-and-seams.md:44,47`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md).
- Downgrade signal: the Checkpoint-5 split bundle accepted an explicit `boundary challenge checklist` before promoting anything, and the `R5.18a1` decision record dispositions every live kept-out item with owner plus reopen trigger. That level of artifact hygiene is inconsistent with `operator tired and cutting corners`. Sources: [`checkpoint-5-r5-18a-boundary-challenge-checklist.md:4-58`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a-boundary-challenge-checklist.md), [`checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md:24-216`](../../../../readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md).
- Upgrade signal: if this workspace's Wave 1 lanes also cascade into `a1/a2/a3` parallel sublanes without new mapping evidence forcing the split, subdivision is becoming a default cadence move rather than a rigor response.

### OP-03 — Launch-truth protocol depends on vigilance, not machinery

- Pressure: doctrine-sensitive spawned-worker launches rely on the operator remembering to record a pre-spawn `$(date +%s)` boundary, running `capture_launch_truth.py`, and preserving the output in a review artifact. Hooks cannot carry this burden; the capture surface is a Python helper plus an explicit `WORKFLOW.md` protocol.
- Artifact signal: [`WORKFLOW.md:69-82`](../../../../../WORKFLOW.md), [`AI-GUARDRAILS.md:87-100`](../../../../../AI-GUARDRAILS.md), [`checkpoint-5-bounded-follow-through-implementation-note.md:35-36`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md). The Track C launch-truth capture note also admits that the first Checkpoint 5 wave used `--latest N` fallback because the stronger `--since` boundary was not recorded.
- Tier: `primary causal pressure` for this specific lane. Launch-truth gaps are not explained by mapping defects elsewhere; they are explained by the `harness has no self-proving capture` reality plus operator vigilance load.
- Best alternative explanation: Codex-product-side constraint. Subagent behavior reapplies the parent turn's live runtime overrides, so child-config-file settings cannot be treated as effective on their own. [`checkpoint-4-codex-load-bearing-surfaces-and-seams.md:62`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md). That narrows how much any repo-local harness move can do. The operator-pressure reading still survives because nothing about the product limit forces reliance on manual capture; a lightweight spawn-truth capture at review boundaries is available today and has not been made default.
- Downgrade signal: if a post-Checkpoint-5 machinery pass makes `capture_launch_truth.py` run as a review-artifact side effect (hook or worker-return contract), this pressure drops to `amplifying`.
- Upgrade signal: further evidence of launch-settings drift going undetected between worker spawns.

### OP-04 — Session-continuity vigilance across compaction / resume

- Pressure: Codex resumed-session context is not safely equivalent to a fresh session, so the operator has to treat `/status`, resumed threads, and compaction summaries as advisory rather than authoritative. The readiness compact prompt, the `SESSION-REENTRY-CHECKLIST.md`, and the fresh-thread-at-meaningful-checkpoints rule all exist to compensate.
- Artifact signal: [`WORKFLOW.md:126-132`](../../../../../WORKFLOW.md), [`checkpoint-4-codex-load-bearing-surfaces-and-seams.md:50-56`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md).
- Tier: `amplifying pressure`. Continuity posture is `strong enough for long-running planning/audit work only when the package entrypoint, fresh-thread boundary doctrine, and re-entry checklist are actually used`. That is an operator-carried invariant.
- Best alternative explanation: upstream Codex limitations (`#17560`, `#17776`, `#17928`, `#17939`) are the actual primary cause. The pressure on the operator is a consequence of those limits, not of local cadence. Sources: [`checkpoint-4-codex-load-bearing-surfaces-and-seams.md:53-55`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md).
- Downgrade signal: if Wave-1 launches happen fresh-thread by default and the workspace does not depend on resume, this pressure stays at amplifying and can drop toward weak.
- Upgrade signal: a readiness artifact where resumed-session drift actually overwrote a load-bearing checkpoint record without being caught.

### OP-05 — Same-operator authoring / reviewing the framing artifacts

- Pressure: `../../planning-notes/SESSION-FRAMING-BRIEF.md` is a situated operator document whose effective authority is `class-1-adjacent during spec writing and framing disputes`, even though its declared authority is only class-2 (briefing / procedural). The same operator writes the brief, the charter, and the lane specs the brief would have to be tested against.
- Artifact signal: [`WORKSPACE-AUTHORITY-AND-ORGANIZATION.md:163-168`](../../governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md), [`SESSION-FRAMING-BRIEF.md:12-18`](../../planning-notes/SESSION-FRAMING-BRIEF.md).
- Tier: `amplifying pressure`. It amplifies closure-biased framing drift because the brief is the path of least resistance when lanes collide with the charter.
- Best alternative explanation: this is really a `doctrine / authority` issue masquerading as an operator issue. The charter already names it, requires pressure-testing, and demands either corroboration from other evidence families or explicit operator-hypothesis labeling. Sources: [`SESSION-FRAMING-BRIEF.md:13-18,33-38`](../../planning-notes/SESSION-FRAMING-BRIEF.md), [`AUDIT-CHARTER.md:15-16`](../../governance/AUDIT-CHARTER.md).
- Downgrade signal: Wave-1 lanes explicitly separate `brief-supported` from `independently-supported` load-bearing claims.
- Upgrade signal: a Wave-1 lane that adopts a load-bearing claim from the brief without corroboration, without the charter's prestige-challenge treatment, and without an operator-hypothesis label.

### OP-06 — Inherited packet advantage for incumbent proposals

- Pressure: the current workspace has richer prose for `Proposal B-extended` than for `E` or `F`, so the comparison is `partially prelicensed` toward B through `inherited packet advantage`, not only through warranted asymmetry.
- Artifact signal: [`lane-04-surface-b-prelicensing-judgeability-pass.md:46-62`](../../lane-reviews/lane-04-surface-b-prelicensing-judgeability-pass.md).
- Tier: `amplifying pressure`. The pressure exists and is honestly labeled, but the doctrinal reason B is currently favored (bridge-audit `revise + guarded hybrid reseed`) is independently warranted and does not depend on packet polish.
- Best alternative explanation: doctrinal inheritance, not orchestration exhaustion. The bridge audit's program-revision-before-mutation is a real prior finding, and the workspace's richer B ensemble is partly what program-revision-before-mutation looks like when the operator is doing the revision. Sources: [`SYNTHESIS.md:5-17,48-56`](../../../2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md).
- Downgrade signal: a later pass that makes `E` and `F` genuinely judgeable and finds B still favored on the merits.
- Upgrade signal: if Wave-1 lanes adopt B-shaped conclusions without addressing the prelicensing pass' required `review-space check`.

### OP-07 — Operator-driven overlay materialization discipline

- Pressure: the `.codex/*` runtime surfaces are `.gitignore`d, so operator-landed runtime changes are invisible to normal staged-diff review. The operator must manually materialize touched runtime files into tracked overlay under `tooling/portable-gsd/overlay/` to keep the change auditable.
- Artifact signal: [`checkpoint-5-bounded-follow-through-implementation-note.md:28-31`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md), [`checkpoint-5-r5-18b-review-planning-chain-launch-internal-r1.md:28`](../../../../readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18b-review-planning-chain-launch-internal-r1.md), [`checkpoint-5-r5-18c-completion-routing-chain-launch-internal-r1.md:26`](../../../../readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18c-completion-routing-chain-launch-internal-r1.md).
- Tier: `amplifying pressure`. This is a real harness seam (runtime vs. tracked truth), carried by operator vigilance because the machinery does not automate it.
- Best alternative explanation: `git / repo-ops boundary materialization` is already named as a distinct concern family (`R5.7` active slice; `R5.8` branch/worktree seam) and as a `machinery-owned` mapping surface. Sources: [`checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md:164-185`](../../../../readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md), [`checkpoint-4-codex-load-bearing-surfaces-and-seams.md:89-95`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md).
- Downgrade signal: a bounded overlay-materialization helper, a hook, or even a `pre-commit` check that catches `.codex/` edits without overlay mirror.
- Upgrade signal: a future runtime landing that was not mirrored and went uncaught for more than one checkpoint cycle.

### OP-08 — Wave-level meta-workspace accumulation

- Pressure: the `2026-04-18` debrief/redesign workspace itself produced lanes `01`, `02`, `03`, `04`, `05`, each with specs, prompts, reviews, dispositions, and in some cases local subsurface proposals (Surface A, B, C, D, with B splitting further into prelicensing and graded-underreach passes). Those lane numbers sit alongside Wave-1 packets `01-04` that reuse `01-05` naming at a different scope.
- Artifact signal: [`INDEX.md:5-33`](../../INDEX.md).
- Tier: `weak / post-hoc explanation` at the current evidence line. It is easy to narrate `the workspace got big because the operator was overloaded`, but the actual history shows each lane had a specific charter task and produced a dispositioned artifact before the next one launched. The lane-05 comparative disposition also actively rejected broader pre-Wave-1 directory reorganization as not-yet-earned, which is the opposite of a fatigue signal.
- Best alternative explanation: the audit-space has genuinely new objects to govern (contract cross-review, packet manifests, forward-looking `wave-1/` topology) and the incremental shape was chosen deliberately. Sources: [`CURRENT-STATE.md:66-79`](../../CURRENT-STATE.md), [`STATUS.md:66-75`](../../STATUS.md).
- Downgrade signal: workspace keeps accumulating lane artifacts at roughly the current rate without substantive new objects to govern.
- Upgrade signal: a future audit of this workspace judges that the lane-numbering pattern itself was producing motion without progress.

---

## Alternative Explanation Notes

For each major operator-pressure candidate, this section compares operator-pressure reading against the mapping, doctrine, and intervention-shape explanations already on the Stage 2 record.

### A. Mapping-weakness alternative

- [e:c+i] `Checkpoint 4`'s load-bearing Codex audit found that `12 of 24` registered `.toml` agent files still instructed workers to read `./CLAUDE.md`, `.claude/skills/`, and `.agents/skills/`, while their sibling `.md` files had been partially updated toward `AGENTS.md`. That is a runtime-authority drift inside the harness's most load-bearing seam. Sources: [`checkpoint-4-codex-load-bearing-surfaces-and-seams.md:44,47`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md).
- [e:c+i] The home-level `~/.codex/AGENTS.md` still injected Reflect-era workflow text and an obsolete `No hooks support` claim ahead of repo-local doctrine. Sources: [`checkpoint-4-codex-load-bearing-surfaces-and-seams.md:33,45,71`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md).
- [d:r:i] Neither defect is explained by operator overload. A more available operator would have noticed faster; it would not have prevented the defect. The primary load-bearing cause is under-grounded mapping plus runtime-vs-doc drift — exactly the pattern the `04-17` bridge audit also identifies. Source: [`SYNTHESIS.md:26-29`](../../../2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md).
- [d:r:i] The operator-pressure reading only survives here in an amplifying role: the vigilance burden of monitoring the `.md/.toml` split and the home-level `AGENTS.md` injection is what the operator is carrying while the mapping is being repaired.

### B. Doctrine / review-posture alternative

- [e:c+i] `POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:87,132,140` is cited by the charter precisely because it forbids treating `no blockers found` / `safe enough to proceed` as satisfying endpoints. The readiness package itself holds the `canon uplift` response only because the earlier doctrine response `translated a large amount of earned doctrine into safe enough to proceed and patch lightly`. Source: [`PLAN.md:45-49`](../../../../readiness/phase-01-rerun/PLAN.md).
- [d:r:i] That is a review-posture failure, not an operator-bandwidth failure. The original sensitivity verdict was `too narrow and too gate-like` — that reads as closure-biased judgment, and the correction was to rewrite the response as `canon uplift + milestone carry-forward + long-arc steering`. Source: [`PLAN.md:47-48`](../../../../readiness/phase-01-rerun/PLAN.md).
- [d:r:i] Saying `the operator was under pressure, so the first verdict tamed itself` would be a post-hoc explanation. The artifact trail names the real cause: the review posture was not yet strong enough to resist closure bias. That is a `doctrine` explanation.

### C. Intervention-shape alternative

- [e:c+i] The first `Checkpoint 5` implementation was explicitly called `too narrow` — the bounded scope accepted by the first launch spec missed the workflow-chain follow-through the Checkpoint 4 audit had already identified. Source: [`STATUS.md:16-17`](../../../../readiness/phase-01-rerun/STATUS.md).
- [e:c+i] The `R5.18` frontier itself is the current modification frontier, which is why `R5.19` exists as a broader exclusion / modification-consideration lane `parallel to R5.18` rather than downstream of it. Source: [`STATUS.md:111-118`](../../../../readiness/phase-01-rerun/STATUS.md).
- [d:r:i] That is intervention-shape debt, not operator overload. The operator was not running out of time; the intervention unit itself was picked wrong. A `harness-code-first` (Proposal F) or a `Proposal C` mapping-first shape would have changed the first scope choice without changing the number of hours available. Sources: [`PLAN-PROPOSALS.md:88-153,174-195`](../../planning-notes/PLAN-PROPOSALS.md).

### D. Carrier / workflow-surface alternative

- [e:c+i] The Surface D lane-04 pilot added high-force wake logic to `discuss-phase.md` and `context.md` specifically because the ordinary wake language was silently settling future seams. That wake-logic gap is a workflow-carrier defect: the operator (and any downstream agent) had to carry the wake semantics as memory instead of as prompt surface. Sources: [`../../lane-reviews/lane-04-surface-d-high-force-carrier-proposal.md`](../../lane-reviews/lane-04-surface-d-high-force-carrier-proposal.md), [`context.md:66-78`](../../../../../.codex/get-shit-done/workflows/discuss-phase.md).
- [d:r:i] This is the cleanest case where the operator-pressure reading and the carrier-pressure reading actually converge. The workflow files were under-carrying the load, so the operator was compensating. The pilot's fix is machinery, not operator endurance. That is consistent with `amplifying` rather than `primary` operator pressure.

### E. Where operator pressure actually wins the explanation

- Only `OP-03` (launch-truth vigilance) stays `primary` after the challenge. Every other operator pressure either (i) is a visible response to a mapping or doctrine defect already named on the record, or (ii) could be reassigned to machinery without structural repo change.
- `OP-03` survives because the hook surface is experimental, fail-open for many non-Bash tools, concurrent across files, and cannot replace an operator's hand on the `--since` boundary. That leaves the operator as the load-bearing surface until a bounded capture helper promotes to a review-artifact side effect. Sources: [`checkpoint-4-codex-load-bearing-surfaces-and-seams.md:46,73`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md).

---

## Carrier And Workflow Surfaces Under Pressure

This section records the surfaces where pressure is visibly carried and where stronger carrier behavior would materially change the operator burden, along with the reversal cost and the evidence that would count against each intervention.

### C-01 — `.codex/get-shit-done/workflows/discuss-phase.md` + `templates/context.md`

- Current pressure: wake logic for high-force open questions is operator-carried unless the pilot's `current disposition / wake trigger / affected decision surface / next wake point` block is used. Sources: [`discuss-phase.md:82-84`](../../../../../.codex/get-shit-done/workflows/discuss-phase.md), [`context.md:66-78`](../../../../../.codex/get-shit-done/templates/context.md).
- Intervention considered: expand the pilot to require wake-logic for every open question, not only high-force ones.
- Reversal cost: very high. Mandatory wake-logic would re-introduce ceremony that the Surface D pilot deliberately avoided. The pilot passed `anti-ceremony` reread partly because it stayed narrow. Sources: [`lane-04-patched-surface-reread.md:13-19`](../../lane-reviews/lane-04-patched-surface-reread.md).
- Reopening trigger: two or more real phases using the wake-logic block and finding it routinely necessary for non-high-force questions.
- Non-intervention justified for now: yes, because the pilot is still accumulating empirical evidence.

### C-02 — Cross-vendor review prompts (`review.md`) and launch-prompt discipline

- Current pressure: cross-vendor launches need per-lane packet freeze, per-lane SHA recording, per-lane launch-truth capture. Each of those is a separate operator-carried step.
- Intervention considered: a `per-lane launch record` that captures frozen-packet SHA, requested settings, and effective settings as a single review-artifact side effect when a cross-vendor lane is dispatched.
- Reversal cost: medium. If the capture helper becomes noisy or is misread as `machinery proves settings`, it silently weakens the `AI-GUARDRAILS.md:87` honesty rule that forbids treating requested settings as proof. Sources: [`AI-GUARDRAILS.md:87-100`](../../../../../AI-GUARDRAILS.md).
- Reopening trigger: a Wave-1 or Wave-2 launch where effective settings diverged from requested settings and the divergence was not caught until after review.
- Non-intervention justified for now: yes, because the Track C launch-truth helper plus the `AI-GUARDRAILS.md` protocol already carry a bounded version of this.

### C-03 — Audit-workspace authority / force register

- Current pressure: operator-written `../../planning-notes/SESSION-FRAMING-BRIEF.md` has effective class-1-adjacent authority during spec writing, even though its declared authority is class-2.
- Intervention already landed: the Surface A patch added an `Authority / Force Snapshot` and a `Revisability Trigger` to the workspace authority note so that divergence between declared and effective authority is at least auditable. Sources: [`WORKSPACE-AUTHORITY-AND-ORGANIZATION.md:159-184`](../../governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md).
- Residual pressure: load-bearing framing claims from the brief still need either corroboration or explicit `operator-hypothesis` labeling in Wave-1 lanes.
- Reversal cost: low for the current authority-snapshot patch; higher if expanded into generalized `every brief file needs a force register`.
- Reopening trigger: a Wave-1 lane that adopts a load-bearing brief claim without corroboration and without the operator-hypothesis label.

### C-04 — Overlay materialization (`tooling/portable-gsd/overlay/`)

- Current pressure: every `.codex/*` runtime edit needs a tracked overlay mirror so the change is reviewable. This is purely operator-carried today.
- Intervention considered: a pre-commit or `gsd-tools` check that fails if `.codex/*` is edited without a tracked overlay mirror in the same commit.
- Reversal cost: medium. A bad check would block legitimate transient edits; a noisy check would teach the operator to bypass it, weakening the `AI-GUARDRAILS.md:87` posture that hooks should not be substitutes for explicit review boundaries. Sources: [`WORKFLOW.md:160-166`](../../../../../WORKFLOW.md), [`AI-GUARDRAILS.md`](../../../../../AI-GUARDRAILS.md).
- Reopening trigger: a runtime landing missed by the current manual discipline.
- Non-intervention justified for now: yes, because the checkpoint-5 implementation pass already did the overlay materialization manually and the `R5.19` artifact trail dispositioned the broader remainder explicitly.

### C-05 — Wave-1 topology under `wave-1/`

- Current pressure: packets, specs, prompts, outputs, dispositions, and launch-truth captures sit alongside historical lane artifacts at workspace root. The `wave-1/` directory was added specifically so new artifacts do not compound root-level density.
- Intervention considered: retroactive mass move of historical lane artifacts into `legacy/` or `2026-04-17-to-19-setup/` to reduce per-read index size.
- Reversal cost: high. The lane-05 comparative disposition already rejected broad pre-Wave-1 directory reorganization as `not currently earned`. A retroactive mass move would also break reference graphs in dispositioned artifacts unless `audit_refmap.py move` is used with care. Sources: [`CURRENT-STATE.md:66-79`](../../CURRENT-STATE.md), [`.planning/AGENTS.md:42-76`](../../../../../.planning/AGENTS.md).
- Reopening trigger: evidence that Wave-2 planning is being hampered by root-level artifact density even after `wave-1/` absorbs most new artifacts.

### C-06 — Cross-vendor context-window / prompt-length constraint

- Current pressure: the earlier `R5.17e` cross-vendor Opus reread ended with `Prompt is too long`; the `claude-opus-4-6[1m]` rerun completed cleanly. Per-lane packet discipline now records which explicit `1m` selector was used. Source: [`PROTOCOL.md:66-67`](../../../../readiness/phase-01-rerun/PROTOCOL.md).
- Intervention already landed: per-lane packet budgeting (`60k-140k` for substantive lanes; `20k-40k` for adversarial stress tests) plus mandatory recording of the Claude selector and effort actually used. Sources: [`EVIDENCE-ARCHITECTURE.md:100-108`](../../governance/EVIDENCE-ARCHITECTURE.md), [`PROTOCOL.md:59-68`](../../../../readiness/phase-01-rerun/PROTOCOL.md).
- Residual pressure: a lane that exceeds budget through packet drift is still caught after the fact rather than before launch. The ceiling is a harness/machinery limit plus an operator habit; that is partly what this Wave-1 lane's `60k-95k` band exists to test.
- Reopening trigger: a Wave-1 or later lane returning `Prompt is too long` under the current manifest.

---

## Switch-Trigger Register

These triggers move the rerun shape toward stronger workflow, execution-capacity, or harness-facing intervention. Each trigger names the switch direction, the evidence that would count, and the reversal cost of switching.

### ST-01 — Toward Proposal F (harness-code-first)

- Switch evidence: Wave-1 lanes converge on `runtime-authoritative worker drift` or `overlay materialization` as the blocking surface, not doctrine or mapping. Specifically, if more than one Wave-1 lane independently names `.toml` registry alignment, overlay mirror discipline, or launch-truth capture as load-bearing, and if the `Checkpoint 5` follow-through proves insufficient.
- What moves: the rerun shape stops treating `debrief → mapping → doctrine → rerun` as the dominant sequence and promotes a bounded harness intervention wave before Phase 01.
- Reversal cost: high. Harness-code work cannot be un-landed without another lane. A wrong call would widen repo-local scope into implementation work that the `AI-GUARDRAILS.md` solo-developer posture deliberately constrains. Sources: [`AI-GUARDRAILS.md:103-113`](../../../../../AI-GUARDRAILS.md).
- Reopening trigger (for the switch itself): if Proposal F is adopted and the harness change does not materially reduce operator vigilance load in the subsequent two waves, revert posture and reopen Proposal C.

### ST-02 — Toward Proposal C (mapping-heavy lane first)

- Switch evidence: Wave-1 lanes cannot reconcile readiness mapping, docs-refresh terrain, and runtime/harness behavior without opening an ontology-reconciliation sublane; or the mapping-adequacy lane explicitly asks to split.
- What moves: Wave-1 pauses before launching Wave-2 and runs a mapping/topology reconciliation lane first.
- Reversal cost: medium. The cost is schedule drag and possible lane growth. The `PLAN-PROPOSALS.md:79-84` already identifies this as a strong fallback, not a theoretical branch.
- Reopening trigger: if the reconciliation lane bottoms out without producing new mapping evidence.

### ST-03 — Toward Proposal E (execute-and-learn)

- Switch evidence: two or more Wave-1 lanes name execution-friction questions that only a live Phase 01 pass can answer. Specifically, if reviewer observations say mapping / doctrine redesign cannot distinguish `closure bias` from `genuine product uncertainty` without execution signal.
- What moves: the rerun budgets an explicit learning pass with pre-commit friction-capture before the main rerun.
- Reversal cost: high. Spending Phase 01 budget on a learning pass cannot be undone, and noisy execution data can mask doctrine truth.
- Reopening trigger: a failed or ambiguous learning pass whose friction evidence contradicts the current doctrine.

### ST-04 — Toward automated launch-truth capture

- Switch evidence: any Wave-1 launch where effective settings diverge from requested and the divergence is not noticed before review closure.
- What moves: promote `capture_launch_truth.py` from a protocol-grade helper to a review-artifact side effect, either through a post-launch hook or a worker-return contract.
- Reversal cost: medium. If the helper becomes a product rather than evidence, it could quietly be treated as proof of effective settings, which is exactly what `AI-GUARDRAILS.md:87-100` forbids. Any automation needs to keep `requested` and `effective` visibly distinct.
- Reopening trigger: machinery noise, false positives, or silent drift between the capture output and the `state_5.sqlite` truth surface.

### ST-05 — Toward a harness compaction / resume machinery lane

- Switch evidence: more than one load-bearing artifact is lost, distorted, or silently overwritten across a compaction / resume boundary during Wave-1 or Wave-2.
- What moves: promote the current `SESSION-REENTRY-CHECKLIST.md` plus readiness compact prompt into a broader continuity-doctrine lane and consider a dedicated compaction-review artifact.
- Reversal cost: medium. The current continuity posture is working well enough that a premature promotion risks ornamentalizing the compact prompt without fixing the underlying upstream constraint.
- Reopening trigger: Codex product changes that remove the current resume drift, or a resume incident with concrete artifact loss.

### ST-06 — Toward a per-operator / per-lane execution-capacity reopening

- Switch evidence: an accumulated pattern across Wave-1 and Wave-2 where single-operator cadence is demonstrably the blocker, not mapping or doctrine. Concretely: Wave-1 produces strong mapping and strong doctrine, but closure is slipping because reviews cannot be processed fast enough to keep lanes current.
- What moves: the charter's `[d:r:i]` execution-capacity model gets reopened and either budgeted for more operator time or narrowed scope per wave.
- Reversal cost: low for a doctrine update; high if the execution-capacity change drives a scope cut on the substantive audit.
- Reopening trigger: two consecutive waves with lane drift or dispositioned-but-unreviewed output backlog.

---

## Interventions Considered And Rejected

The lane spec requires at least `3` stronger interventions this lane considered and rejected. Five are named below. For each: `why considered`, `upside`, `regret analysis that counted against it`, `reopen signal`.

### RJ-01 — Single sweeping operator-overload diagnosis that explains the whole readiness underreach

- Why considered: it is the shortest possible story and makes a tidy report.
- Upside: easy to communicate; maps onto visible artifact load.
- Regret analysis: it collapses the four axes of `../../governance/EVIDENCE-ARCHITECTURE.md` into one, makes operator pressure a universal solvent, and directly triggers the failure conditions in this lane's spec (`Fails if it reduces the whole readiness initiative to operator overload` and `Fails if it cannot distinguish primary from amplifying pressure`). Sources: [`EVIDENCE-ARCHITECTURE.md:5-12`](../../governance/EVIDENCE-ARCHITECTURE.md), [`wave-1/specs/04-operator-orchestration-pressure-spec.md:62-66`](../specs/04-operator-orchestration-pressure-spec.md).
- Reopen signal: a Wave-2 audit that finds mapping, doctrine, and intervention-shape explanations are secondary under controlled evidence.

### RJ-02 — Immediate global workflow / harness rewrite (full Proposal F now)

- Why considered: it would directly convert operator vigilance into machinery, closing `OP-03`, `OP-04`, and `OP-07` all at once.
- Upside: biggest per-lane reduction in operator vigilance load.
- Regret analysis: it foreclosings bridge-audit continuity (`revise + guarded hybrid reseed`), widens repo-local scope beyond the solo-developer posture, and the lane-05 disposition already rejected pre-Wave-1 large topology moves as `not currently earned`. Sources: [`SYNTHESIS.md:5-17`](../../../2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md), [`CURRENT-STATE.md:66-79`](../../CURRENT-STATE.md), [`AI-GUARDRAILS.md:103-113`](../../../../../AI-GUARDRAILS.md).
- Reopen signal: `ST-01` firing with two independent Wave-1 lanes naming harness as the blocker.

### RJ-03 — Immediate launch-truth automation (promote `capture_launch_truth.py` to hook)

- Why considered: it would demote `OP-03` from `primary` to `amplifying` quickly.
- Upside: cleanest structural fix for the one pressure this lane classifies as primary.
- Regret analysis: official Codex hook maturity is explicitly experimental, Bash-only for tool interception, fail-open for many outputs, and concurrent across files. An early automation risks being treated as proof-of-effective-settings, which directly contradicts `AI-GUARDRAILS.md:87-100`. Sources: [`checkpoint-4-codex-load-bearing-surfaces-and-seams.md:46,73`](../../../../readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md), [`AI-GUARDRAILS.md:87-100`](../../../../../AI-GUARDRAILS.md).
- Reopen signal: `ST-04` fires, or Codex hooks leave experimental status.

### RJ-04 — Subdivide the operator-pressure register into a fine taxonomy (burnout / cadence / context drift / bandwidth / scope creep / attention budget)

- Why considered: it would look more rigorous and would produce more register rows.
- Upside: more granular discussion; more places to anchor future artifacts.
- Regret analysis: exactly the universal-solvent failure mode the spec warns against. A fine operator-pressure taxonomy invites every future lane to route its findings into operator-pressure language, and it would soften the distinction between `primary` and `amplifying` that this lane is specifically designed to hold. Sources: [`wave-1/specs/04-operator-orchestration-pressure-spec.md:14-16,27-29`](../specs/04-operator-orchestration-pressure-spec.md).
- Reopen signal: two or more Wave-1 lanes explicitly asking for finer operator-pressure vocabulary and offering test cases where the current 3-tier classifier fails.

### RJ-05 — Mandate a sublane quota per checkpoint (no more than N sublanes)

- Why considered: it would mechanically stop the `R5.17 → R5.18 → R5.19` subdivision cascade.
- Upside: visible complexity cap.
- Regret analysis: the subdivision cascade was partly a rigor response to real mapping gaps. A quota mandate would mask the underlying defect with fake discipline and would directly violate the `AUDIT-CHARTER.md:14-20` warnings against treating immediate disruption minimization as the right objective. Sources: [`AUDIT-CHARTER.md:14-22`](../../governance/AUDIT-CHARTER.md).
- Reopen signal: a later pattern where subdivision is happening in the absence of new mapping evidence.

### RJ-06 — Treat the `04-17` bridge audit's `revise + guarded hybrid reseed` verdict as untouchable floor

- Why considered: it would reduce subsequent orchestration burden and simplify Wave-1.
- Upside: fewer meta-questions; operator load drops.
- Regret analysis: contradicts `AUDIT-CHARTER.md:8` (the bridge audit's guarded-hybrid verdict is explicitly not an untouchable floor) and would foreclose the critical-inheritance posture the charter mandates. That is doctrine-level harm traded for cadence relief. Sources: [`AUDIT-CHARTER.md:7-10,18`](../../governance/AUDIT-CHARTER.md).
- Reopen signal: a Wave-1 mapping-adequacy lane finds the bridge-audit verdict survives critical inheritance and no further reopening is warranted.

---

## Non-Intervention Ledger

Surfaces this lane deliberately leaves untouched, with the `why` and the reopen trigger:

- `.codex/hooks.json` — not expanded. Hooks remain experimental per Codex feature maturity; the repo's current posture (narrow, deterministic, removable) is correct. Reopen if Codex hooks leave experimental and `PreToolUse` coverage becomes comprehensive.
- `../../planning-notes/SESSION-FRAMING-BRIEF.md` authority class — not re-declared. The Surface A `Authority / Force Snapshot` already handles the divergence between declared and effective authority; redeclaring `class-1` would collapse the separation this workspace is trying to preserve. Reopen if a Wave-1 lane adopts a brief claim as sovereign doctrine without corroboration.
- Historical lane-04 artifacts — not retroactively moved into a `legacy/` directory. The lane-05 disposition rejected broad pre-Wave-1 topology moves; any retroactive move has to go through `audit_refmap.py move` and must be justified by active navigation harm, not by aesthetic preference. Sources: [`CURRENT-STATE.md:66-79`](../../CURRENT-STATE.md), [`.planning/AGENTS.md:42-76`](../../../../../.planning/AGENTS.md).
- `.codex/get-shit-done/workflows/review.md` — not rewritten to mandate per-lane launch-truth capture in the review synthesis. Cross-vendor review is currently adversarial, not proof-of-launch. Mandating launch-truth inside the review synthesis would risk conflating `evidence of settings` with `evidence of judgment`.
- Checkpoint 5 `R5.18a1` / `R5.18a2` boundary decisions — not reopened. The boundary challenge checklist and contradiction ledger are a strong artifact trail and do not themselves display operator-fatigue failure modes; reopening them purely on operator-pressure grounds would be a direct trigger of this lane's failure conditions.

---

## What This Lane Cannot Explain

- [o:r:i] Whether the charter's execution-capacity model (`one operator orchestrating parallel Codex and Claude lanes over a multi-week budget, capable of multi-module repo-local refactors and bounded follow-through`) is itself an operator-hypothesis that earns further scrutiny. The charter already marks it `[d:r:i]`, so this lane cannot resolve it. Sources: [`AUDIT-CHARTER.md:21`](../../governance/AUDIT-CHARTER.md).
- [o:r:i] Whether the operator-pressure reading is distorted by the fact that the same operator is writing this lane output. The Surface A authority-snapshot patch plus the Stage 2 challenge packet provide partial mitigation, but they do not remove situated bias.
- [o:r:i] Whether the `Checkpoint 5` subdivision cascade is `still responding to real mapping gaps` or has started to become `default cadence`. The Wave-1 mapping-adequacy and outcome/underreach lanes have more direct evidence on this than the operator-pressure lane does.
- [o:r:i] Whether the decision to keep `Proposal B-extended` as the working default is load-bearing or cosmetic. The Surface B prelicensing pass already says the next launch-readiness reread must include a `review-space check`; this operator-pressure lane cannot perform that check.
- [o:r:i] Whether the `wave-1/` topology itself will hold up once Wave-2 accumulates. Current evidence says it should; this lane has no privileged view of Wave-2 plausibility.
- [o:r:i] Whether stronger harness interventions would survive the solo-developer risk posture in `AI-GUARDRAILS.md:103-113`. This lane can name the switch triggers but cannot evaluate whether a specific harness move clears the solo-developer guardrails.

---

## Posture Check (self-audit against spec failure conditions)

- `Fails if it reduces the whole readiness initiative to operator overload.` — avoided. Only `OP-03` is `primary`; six of the eight register rows are `amplifying` or `weak/post-hoc`, and the alternative-explanation notes reassign mapping, doctrine, intervention-shape, and carrier explanations explicitly.
- `Fails if it cannot distinguish primary from amplifying pressure.` — avoided. Each register row names tier, evidence that would upgrade it, evidence that would downgrade it, and the strongest competing explanation.
- `Fails if it recommends stronger workflow or harness moves without naming reversal cost and reopening triggers.` — avoided. Every switch-trigger and every carrier-pressure note carries both a reversal cost and a reopening trigger.
- `Fails if it cannot name at least 3 stronger interventions it considered and rejected.` — avoided. Six rejected interventions are listed (`RJ-01` through `RJ-06`).
- `If operator pressure starts explaining everything, open the challenge stage before finalizing judgment.` — honored. Stage 2 was opened before any `primary` classification was locked in, and the challenge material downgraded three candidates from provisional `primary` to `amplifying`.
