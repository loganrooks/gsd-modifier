---
reviewer: adversarial-auditor-xhigh (Reviewer B, same-vendor critical read)
gate_event: phase-3 boundary; bash scripts/ci/check-bootstrap.sh exit 1 (repeated)
reviewer_a: gsd-debugger ESCALATE
triangulation_pair: REVIEWERS.md → "Gate failure" row
date: 2026-05-16
---

# Reviewer B Findings — Phase 3 Boundary Bootstrap Gate Failure

## Scope of this review

Per REVIEWERS.md:109 the gate-failure triangulation pair is `gsd-debugger` (A) → `adversarial-auditor-xhigh` reviewing the debugger's hypothesis (B). I am reviewing Reviewer A's diagnosis and recommendation, not authorizing Phase 3 closure. Phase 3 closure is `trajectory-verifier`'s gate per REVIEWERS.md:105 ("Phase boundary | trajectory-verifier"), with adversarial audit as the *next* triangulator if the verifier escalates.

The question put to me is narrower than "should Phase 3 close": it is "is Reviewer A's diagnosis sound enough to forward to `trajectory-verifier` with the composite-gate failure flagged and recorded, or is the bootstrap exit 1 itself a halting condition that the debugger missed?"

## Verdict shape

PASS on Reviewer A's hypothesis. The diagnosis is grounded; the recommendation is correctly bounded inside the debugger's lane; the next reviewer is correctly named. I attach three concerns the next reviewer must engage rather than inherit silently.

## Grounded findings

### F1 — Pilot materialization obligation: direct contract gates discharge it. PASS.

**What.** Three independent direct gates (not the composite script) attest the pilot carrier is materialized and verified end-to-end:

- `./scripts/setup-portable-gsd-runtime.sh --runtime both` exit 0; both runtime post-materialization reports `hard_failures: []` and `inject_failure_count: 0` for the pilot carrier.
- `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict` exit 0; top-level `hard_failures: []`; both runtime entries for `mandatory-initial-read.md` pass the `GSD_MODIFIER:references-mandatory-initial-read:extended-content` marker verification.
- `python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict` exit 0; `parity_state: dual-runtime-aligned`; `unknown_live_drift: 0`; `inject_failure_count: 0` for both runtimes.

**Why it matters.** Ground (1) — phase plan exit criteria. `phases/03-pilot.md:108-111` decomposes EC into "pilot carrier materialized correctly under both runtimes (visual inspection + `verify-materialized` exit 0)" *and* "Bootstrap gate exit 0 with `hard_failures: []`". The first conjunct is unambiguously satisfied by direct evidence. The second is the contested one.

**Confidence.** High on materialization; medium on whether it satisfies EC3's intent (see F2/F3).

**What would dissolve.** Nothing — direct gate evidence stands.

### F2 — `check-bootstrap.sh` failure is broad-discover over-aggregation, not pilot defect. PASS with caveat.

**What.** `scripts/ci/check-bootstrap.sh:9-16` runs `setup-portable-gsd-runtime.sh`, then `python3 -m unittest discover -s tooling/codex/tests`, then the four contract/canary/refmap/diff gates. `set -euo pipefail` (line 2) means the unittest failure short-circuits before the later contract gates run. Two of the six failures are directly verifiable as stale-after-Phase-0 tests:

- `test_health_and_migration_follow_through_contract.py:14` asserts `skills/gsd-from-gsd2/SKILL.md` is `overwrite`; `OVERLAY-MANIFEST.json:948-957` shows it as `mode: add` sourced from `harness_modifier/overlay/...`.
- `test_health_and_migration_follow_through_contract.py:33-36` reads `tooling/portable-gsd/overlay/skills/gsd-from-gsd2/SKILL.md`, which Phase 0 Slice 2 `git mv`'d out of that path (STATE.md:101).
- `test_seed_consumer_follow_through_contract.py:13,38` mirror the same pattern for `gsd-plant-seed` against `OVERLAY-MANIFEST.json:981-990`.

These two test files are unambiguously stale relative to the Phase 0 reclassification that completed before Phase 3 began. The pilot did not cause them; they were already failing.

**Caveat.** The other two failures (`test_seed_audit_gate_follow_through_contract`, `test_transition_uplift_continuity`) are characterized in STATE.md:42 as "runtime-state-dependent" and "out of scope unless they change shape or block the pilot directly". I did not read those test files in this audit. See F3.

**Why it matters.** Ground (1) and ground (5). EC3 literal text vs EC3 intent is the live decision. Ground (5): if we accept "composite exit 1 doesn't matter when the parts we care about pass" as a precedent without bounding, we erode future gate signal — a real future regression could hide inside the same shape.

**Confidence.** High on the two reclassification-stale tests. Medium on the other two being independent of the pilot (see F3).

**What would dissolve the caveat.** Trajectory-verifier directly reading the seed-audit and transition-uplift test bodies and confirming their assertions do not transit through the materialized `mandatory-initial-read.md` content.

### F3 — Membership of the baseline failure set shifted across runs; treat that as something for `trajectory-verifier` to examine, not as a settled question. QUALITY concern.

**What.** STATE.md:42 records:

> "after Slice 3 bootstrap retry, full discover shows the same non-pilot class with a refreshed member list: reclassified-source stale tests for `gsd-from-gsd2` and `gsd-plant-seed`, plus runtime-state-dependent failures in the seed-audit helper and transition/uplift continuity. The current run did not reproduce the previously named state-snapshot future-carry failure."

Pre-Phase-2 baseline was 5 failures; the current set is 6, with `test_state_snapshot_future_carry` dropping and two new runtime-state-dependent failures appearing. The set is consistent with the *class* label "non-pilot baseline" but is not byte-identical to prior runs. Reviewer A's framing inherits this characterization without independently testing it.

**Why it matters.** Ground (4) — methodology discipline (calibrated language, model verification). The phrase "documented non-pilot baseline" is doing more work in Reviewer A's reasoning than the evidence directly supports, because the membership shifted and the new members are runtime-state-dependent — i.e., they execute against the materialized `.codex` surface that the pilot just modified. A parsimonious explanation is "these helpers have always been flaky against materialized state"; a less parsimonious but not-yet-excluded explanation is "the injected reading-packet block in the materialized `mandatory-initial-read.md` is perturbing a downstream helper that reads it".

**Confidence.** Medium that the helpers are independent of the pilot; medium that they are not. This is exactly the kind of "is the gate failure load-bearing" question that justifies passing the decision to `trajectory-verifier` rather than resolving it inside the debugger lane.

**What would dissolve.** Either (a) trajectory-verifier reading the seed-audit and transition-uplift test bodies and confirming they do not read materialized `mandatory-initial-read.md`, or (b) reverting the pilot in a scratch worktree and confirming the same failures still occur (probably overkill for this gate, but mentioned for completeness).

**Suggested direction.** Have `trajectory-verifier` cite the two runtime-state-dependent test files at file:line when it discharges (or refuses) EC3.

### F4 — Phase 0 boundary precedent applies, but should be invoked explicitly, not silently inherited. QUALITY.

**What.** Phase 0's boundary triangulation (`checkpoints/2026-05-16T002240Z-phase00-boundary.md`; STATE.md:106; Reviewer Decisions Log 2026-05-16T00:22:00Z) accepted a `trajectory-verifier` ESCALATE → `adversarial-auditor-xhigh` PASS with the reasoning that "the verifier's recommendation to redefine EC2 as canary source-layer assertion is correct reading of EC2's intent, not goalpost-moving". That precedent — reading EC intent rather than literal script exit when the composite gate over-aggregates — is the precedent Reviewer A is implicitly leaning on.

**Why it matters.** Ground (4) — methodology discipline. Implicit precedent inheritance is a register-level erosion: if Phase 3 closes by silently relying on Phase 0's "we read EC intent here" move without naming it, the precedent becomes load-bearing across the initiative without anyone having committed to it as policy. Whoever ratifies Phase 3 closure (next-reviewer trajectory-verifier or its triangulator) should cite the Phase 0 precedent explicitly and either ratify it as a general rule or scope it tightly to "composite gate exit 1 attributable to demonstrably pre-existing baseline plus direct gates green".

**What would dissolve.** Boundary checkpoint or Phase 3 closure text that explicitly names the Phase 0 precedent and either (i) bounds it to this case or (ii) elevates it to a general disposition rule for this initiative.

**Suggested direction.** One sentence in the boundary checkpoint: "EC3's literal text ('Bootstrap gate exit 0') is satisfied by intent — zero materialization hard failures across direct contract gates — per the Phase 0 boundary precedent (2026-05-16T00:22:00Z). The composite script's failure is non-pilot test staleness pre-recorded as OOS." That sentence does the calibration work without inflation.

### F5 — Reviewer A's "split the script OR clean up the stale tests" remediation is correctly framed but should not be left as a perpetual deferral. QUALITY.

**What.** Reviewer A: "the smallest remediation is outside the boundary write set: either split/scope `scripts/ci/check-bootstrap.sh` so bootstrap/materialization is separable from full regression, or update the stale non-pilot full-discover tests for `gsd-from-gsd2`, `gsd-plant-seed`, seed-audit, and transition/uplift via a separate reviewer-mediated cleanup slice." This is correct — the fix is outside the slice's write set, so `gsd-debugger` properly did not act.

**Why it matters.** Ground (5) — risk to delivery. If neither remediation lands before Phase 4 begins, every subsequent inject-migration phase boundary will hit the same composite-gate exit 1 and require the same triangulation. That is a recurring cost the initiative is silently signing up for. STATE.md OOS #3 already records the bootstrap-blocker as an open follow-up since Phase 0; the gsd-from-gsd2 / gsd-plant-seed stale tests are not yet recorded as a separate OOS item even though they have been failing since Phase 0 Slice 2/3.

**Confidence.** High that the cost will recur. Medium that it will hide a real regression.

**What would dissolve.** A new OOS item explicitly tracking the four stale full-discover tests (two reclassification-stale, two runtime-state-dependent) with named owner/timing for cleanup, OR a commitment from operator to split `check-bootstrap.sh` before Phase 4 boundary.

**Suggested direction.** Add OOS #5 "stale full-discover tests against post-Phase-0 reclassification + runtime-state-dependent baseline (4 items)" alongside the boundary closure, so the recurring-cost is logged rather than re-discovered.

## What works well

- Reviewer A correctly stays in the debugger's lane and explicitly names `trajectory-verifier/adversarial-auditor-xhigh judgment` as the appropriate decision authority. No scope creep, no implicit waiver.
- Reviewer A's EVIDENCE bullets cite manifest and test file:line directly; the stale-test claim is independently verifiable, which I did.
- The recommendation "do not make code/test changes inside the boundary write set" is correctly bounded by GUARDRAILS forbidden-action #15 and Required-Discipline #6.
- The pilot's *direct* contract-gate evidence is unusually strong — three independent gates (setup, verify-materialized, harness_canary) all attest the same outcome with `hard_failures: []` and `inject_failure_count: 0`. This is exactly the kind of direct evidence that makes the composite-script-exit-1 question a calibration question rather than a substantive one.

## Convergent risks

F2 + F3 + F5 cluster on the same underlying weakness: **the initiative is relying on "this is pre-existing baseline" as a load-bearing claim without a structural mechanism that distinguishes pre-existing baseline from new regression**. STATE.md OOS #3 has been carrying this since Phase 0. The composite gate's broad-discover step will keep over-aggregating until someone either splits it or cleans the stale tests. Each phase boundary will repeat this triangulation. Treat as one issue, not three.

F1 + F4 cluster on a different axis: **EC3 intent vs literal text is being decided ad-hoc per phase**. Phase 0 set a precedent; Phase 3 needs to either invoke that precedent explicitly or set its own. Future inject-migration phases will hit the same question.

## Steelman residue

- My F3 caveat (runtime-state-dependent failures might not be pilot-independent) is real but probably weak: `verify-materialized` already attests the materialized files are byte-correct against contract, and `harness_canary` already attests dual-runtime alignment. If the injected block were perturbing a downstream helper that reads `mandatory-initial-read.md`, the more parsimonious place to surface it would be one of those gates — not specifically the seed-audit gate (which operates on seed lifecycle, not initial-read content) or transition-uplift continuity (which operates on phase-complete behavior). The hidden-interaction story requires a long causal chain I cannot construct from the evidence I have. F3 is appropriately registered as a "trajectory-verifier should cite these test bodies at file:line" check, not as a blocker. Calibrating: low likelihood the pilot is causing these; the value of F3 is forcing the next reviewer to do the file:line read rather than inheriting the "non-pilot baseline" label.
- My F4 (Phase 0 precedent should be named) could be read as register-policing over substance. The defensible counter: implicit precedent is how the team converges on consistent practice, and forcing every phase to re-litigate the EC-intent-vs-literal question is more overhead than signal. I hold the finding because explicit naming costs one sentence and makes the precedent auditable, but the severity is `quality`, not `blocking`.
- My F5 (recurring cost should be tracked) verges on taste — the team may consciously prefer rolling baseline acknowledgment over a structural fix while the initiative is still in flight. The defensible counter: until the initiative stabilizes (post-Phase 4 or Phase 5), structural fixes to test infrastructure compete with the actual migration work. Hold as `quality` because the cost is real but the timing is the team's call.
- I considered escalating to FAIL on the grounds that EC3 literal text is unsatisfied. I rejected that framing because (i) my role is reviewing the debugger's hypothesis, not the phase-boundary decision; (ii) the Phase 0 precedent already disposed of this shape; (iii) FAIL here would force a remediation outside the boundary write set, which is exactly what GUARDRAILS forbidden-action #15 routes through `Plan` reviewer. ESCALATE is the wrong verdict for the same reason — Reviewer A *already* ESCALATED, and this is the B reviewer's turn to either ratify or refute the hypothesis. PASS with concerns forwarded to `trajectory-verifier` is the calibrated answer.

## What this audit cannot tell you

- Whether `test_seed_audit_gate_follow_through_contract` and `test_transition_uplift_continuity` are *actually* independent of the pilot's materialized content. I did not read those test bodies. Trajectory-verifier should.
- Whether splitting `check-bootstrap.sh` would surface other latent assumptions in the script's downstream gates. Out of scope for plan-level review.
- Whether the operator considers the Phase 0 EC-intent precedent a one-off or a general rule. That is an operator decision, not a reviewer one.
- Substantive correctness of the schema v4 inject mechanism. That is the cross-vendor reviewer's job and the contract tests'.

## Verdict block

```text
VERDICT: PASS
REASONING: Reviewer A's diagnosis is grounded and correctly bounded. The pilot's materialization obligation is discharged by three independent direct contract gates (`setup-portable-gsd-runtime.sh` exit 0 with `hard_failures: []` and `inject_failure_count: 0` for both runtimes; `verify-materialized --all-supported --strict` exit 0; `harness_canary.py report --all-supported --strict` exit 0 with `parity_state: dual-runtime-aligned`). The composite `check-bootstrap.sh` exit 1 is attributable to broad-discover over-aggregation: two failures (`test_health_and_migration_follow_through_contract`, `test_seed_consumer_follow_through_contract`) are directly verifiable as stale-after-Phase-0 reclassification (assertions expect `overwrite` and read paths that Phase 0 Slices 2-3 `git mv`'d out); two more are characterized in STATE.md:42 as runtime-state-dependent baseline. Reviewer A correctly identifies that waiving EC3's literal text is a trajectory-verifier/adversarial-auditor judgment, not a debugger judgment, and correctly stays in lane. This verdict authorizes forwarding the diagnosis to `trajectory-verifier`; it does NOT close Phase 3. Three concerns the next reviewer must engage rather than inherit silently: (a) the runtime-state-dependent failures (seed-audit, transition-uplift) should be cited at file:line and confirmed independent of the pilot's materialized `mandatory-initial-read.md` content, not inherited as "baseline" via label; (b) the Phase 0 boundary precedent for reading EC intent over literal composite-script exit should be named explicitly in any closure text, not silently inherited; (c) the recurring-cost remediation Reviewer A recommends (split `check-bootstrap.sh` or clean stale tests) should be tracked as an OOS item before Phase 4 begins, or the same triangulation will recur at every subsequent phase boundary.
RECOMMENDATION: Concur with Reviewer A. Invoke `trajectory-verifier` for Phase 3 boundary with this triangulation result and Reviewer A's diagnosis as input. The verifier must (1) cite `test_seed_audit_gate_follow_through_contract` and `test_transition_uplift_continuity` at file:line and verify their independence from the pilot's materialized content; (2) explicitly invoke or refuse the Phase 0 boundary precedent (2026-05-16T00:22:00Z) for reading EC3 intent over literal exit code; (3) require the boundary checkpoint/STATE record both the composite-gate failure and these three caveats. If the verifier rejects closure, the smallest remediation remains outside the boundary write set: a separate reviewer-mediated cleanup slice for the four stale full-discover tests, or a `Plan`-reviewed split of `scripts/ci/check-bootstrap.sh` into materialization-only and full-regression gates. Either way, add a new STATE.md OOS entry tracking the stale full-discover test set so the recurring cost is logged.
EVIDENCE:
- `scripts/ci/check-bootstrap.sh:2,9-16` — `set -euo pipefail`; runtime setup → broad unittest discovery → contract/canary/refmap/diff gates; unittest failure short-circuits before contract gates run.
- `phases/03-pilot.md:108-111` — EC requires "pilot materialized correctly under both runtimes (visual inspection + `verify-materialized` exit 0)" AND "Bootstrap gate exit 0 with `hard_failures: []`"; first conjunct directly satisfied; second is the contested clause.
- `phases/03-pilot.md:119-125` — boundary command list including `check-bootstrap.sh` and `harness_canary.py`.
- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json:322-353` — pilot carrier `get-shit-done/references/mandatory-initial-read.md` is `mode: inject` for both Codex and Claude with `marker_key: GSD_MODIFIER:references-mandatory-initial-read:extended-content` and `parity_intent: outcome_aligned`.
- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json:948-957` — `skills/gsd-from-gsd2/SKILL.md` is `mode: add` sourced from `harness_modifier/overlay/...`; contradicts the test's `overwrite` assertion and the test's read path.
- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json:981-990` — `skills/gsd-plant-seed/SKILL.md` is `mode: add` sourced from `harness_modifier/overlay/...`; same shape.
- `tooling/codex/tests/test_health_and_migration_follow_through_contract.py:14` — asserts `gsd-from-gsd2/SKILL.md` is `overwrite`; stale.
- `tooling/codex/tests/test_health_and_migration_follow_through_contract.py:33-36` — reads from `tooling/portable-gsd/overlay/skills/gsd-from-gsd2/SKILL.md`; the file was `git mv`'d out by Phase 0 Slice 2 (STATE.md:101).
- `tooling/codex/tests/test_seed_consumer_follow_through_contract.py:13,38` — same shape for `gsd-plant-seed` (Phase 0 Slice 3, STATE.md:102).
- `STATE.md:42` — operator decision (2026-05-16T19:20Z) explicitly records pre-existing full-discover baseline failures as OUT OF SCOPE for this initiative unless they change shape or block the pilot directly; notes membership "refreshed" after Slice 3 retry.
- `STATE.md:90` — Bootstrap/materialization hard_failures counter records 0/0 target met via direct gates; explicitly notes the composite `check-bootstrap.sh` still exits 1 due to non-pilot baseline; disposition triangulated by gsd-debugger ESCALATE + adversarial-auditor-xhigh PASS at Slice 3.
- `STATE.md:106` and Reviewer Decisions Log 2026-05-16T00:22:00Z — Phase 0 boundary precedent for reading EC intent over literal composite-script exit when over-aggregation is established.
- `checkpoints/2026-05-16T203147Z-phase03-slice35.md:33-35` — focused runtime-visibility tests, direct `harness_canary.py report --all-supported --strict` exit 0, `verify-materialized --all-supported --strict` exit 0 with `hard_failures: []` and both runtimes `inject_failure_count: 0`.
- `decisions/PILOT-DEBRIEF-mandatory-initial-read.md:32-37,68-76` — debrief explicitly characterizes `check-bootstrap.sh` as a composite gate that cannot be treated as a single clean signal for this pilot; names the four full-discover failures by category.
- `REVIEWERS.md:105,109` — phase-boundary belongs to `trajectory-verifier` (with adversarial audit as next triangulator); gate-failure pair is gsd-debugger → adversarial-auditor-xhigh reviewing the debugger's hypothesis. This audit is the latter; phase-boundary close remains the former's call.
- `GUARDRAILS.md:53,64` — forbidden-action #15 (no acting outside slice write set without `Plan` reviewer); Required Discipline #6 (write set is bounded). Both correctly observed by Reviewer A in declining to edit stale tests inside this boundary.
```
