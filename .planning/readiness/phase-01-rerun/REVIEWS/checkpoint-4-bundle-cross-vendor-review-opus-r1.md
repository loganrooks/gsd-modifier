Key factual claims verified. Now I have enough to write a thorough review. Here is the full cross-vendor reread:

---

# Checkpoint 4 Bundle Cross-Vendor Reread

- checkpoint: `4`
- artifact(s) under review: `Checkpoint 4 audit bundle`
- review mode: `cross-vendor-reread`
- authoring lane: `Checkpoint 4 bundle synthesis`
- reviewer: `Claude`
- model / reasoning or vendor: `claude-opus-4.6`
- baseline commit / artifact snapshot: `cb4daca`
- independence relationship: `cross-vendor`

---

## What This Review Is Trying To Falsify

1. That the six-file Checkpoint 4 audit bundle is closure-ready.
2. That the `open a bounded Checkpoint 5` verdict is actually justified by the evidence rather than by escalation habit.
3. That the bundle preserves cross-lane ambiguity honestly instead of smoothing it away.
4. That the ownership logic (doc-level / workflow-protocol / machinery-owned) is clean enough to survive later scrutiny.
5. That the proposed Checkpoint 5 scope is appropriately bounded.

---

## Findings

Findings in severity order. Each finding is classified as a real problem, a concern, or an observation.

### F1. The bundle never tests the counter-hypothesis that the rerun could succeed without Checkpoint 5 — CONCERN (high)

**File references:** `checkpoint-4-converged-synthesis.md:56-63`, `checkpoint-4-cross-lane-seam-synthesis.md:59-72`, `PLAN.md:579-585`

The converged synthesis arrives at "open a bounded Checkpoint 5" and briefly tests this against the plan's branching logic. But it never seriously asks the opposite question: *could the rerun succeed if these weaknesses were addressed by doctrine/protocol changes alone and Checkpoint 5 were skipped?*

The plan explicitly describes two branches: "record and avoid overbuilding" vs. "open Checkpoint 5." The synthesis dismisses the first branch in two sentences (`checkpoint-4-converged-synthesis.md:62`), stating that `.toml` worker drift and reproducibility "are too concrete to be waved away." That may be true, but the argument is assertion-level, not evidence-level. Specifically:

- The `.toml` worker drift is real (I verified: 12 of 24 files carry legacy refs), but the bundle never quantifies the *consequence*. How many of those 12 are in the phase-critical chain that the rerun will actually exercise? If the rerun only touches `gsd-planner`, `gsd-phase-researcher`, `gsd-plan-checker`, `gsd-executor`, and `gsd-verifier`, the question becomes whether those specific `.toml` files are misaligned — and the runtime lane already confirms model resolution works correctly for the core four. The bundle treats "12 of 24" as if all 12 are equally load-bearing, which overstates the urgency.

- The portable-GSD reproducibility finding (unpinned install, stale provenance) is real but is only rerun-blocking if the repo needs to reinstall before the rerun. If the current checkout is already live and the overlay matches (which the runtime lane confirms: `checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:29`), the reproducibility weakness is future-facing risk, not immediate rerun-blocking risk. The synthesis does not make this temporal distinction.

A stronger synthesis would have tested: "If we fixed the five core-chain `.toml` files and deferred the remaining seven plus reproducibility to post-rerun, would the machinery be strong enough?" That counter-test was never performed, which weakens the verdict's falsifiability.

### F2. The Checkpoint 5 scope is listed but not prioritized or bounded by a stopping rule — CONCERN (medium-high)

**File references:** `checkpoint-4-converged-synthesis.md:75-80`, `checkpoint-4-cross-lane-seam-synthesis.md:59-66`

The converged synthesis proposes three items for Checkpoint 5:
1. Align `.toml` worker prompts
2. Harden portable GSD reproducibility/provenance
3. Decide launch-truth and model-truth capture surfaces

The seam synthesis adds two more conditional candidates: review/closure pressure upgrade and claim-discipline propagation.

The problem: there is no explicit stopping rule for Checkpoint 5. Items 1 and 2 are concrete and bounded. Item 3 is a "decide which surfaces need X" formulation that can expand indefinitely. The conditional candidates from the seam synthesis (review pressure, claim discipline) are explicitly labeled "workflow-protocol" ownership but could easily migrate into Checkpoint 5 during execution because the bundle has already established that these weaknesses interact with the machinery findings.

A strong toolchain designer would want the Checkpoint 5 gate to state: "Checkpoint 5 is complete when [concrete exit criteria]. If work exceeds [N], that is evidence of scope drift, not thoroughness." The current bundle does not provide this, which means the bounded-Checkpoint-5 verdict is only as bounded as later execution discipline makes it.

### F3. Review-pressure and claim-discipline findings are repeated across three files without sharpening — CONCERN (medium)

**File references:** `checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:40-45,65-67`, `checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:42-43,49-51,57-58`, `checkpoint-4-cross-lane-seam-synthesis.md:34-36,52-56`

The workflow-chain lane, the agent-doctrine lane, and the seam synthesis all identify the same two patterns: (a) review is advisory/consensus-biased rather than adversarial, and (b) claim discipline collapses downstream from research. These findings appear in three files with nearly identical phrasing but slightly different source citations.

This repetition does not constitute independent corroboration — it is the same authoring agent making the same observation from overlapping evidence. The seam synthesis (`checkpoint-4-cross-lane-seam-synthesis.md:46-50`) briefly notes this as "the strongest real cross-lane convergence" but then treats convergence as confirmation rather than asking whether the apparent agreement masks a shared blind spot.

The blind spot risk: the review-pressure finding is exclusively about what the *harness prompts say*. Neither lane tested whether, in actual practice, the current advisory posture has already produced weak review outcomes in this repo. The finding is structural (the prompts allow softness) rather than empirical (softness has actually degraded quality). A strong later auditor would ask for at least one concrete example of advisory review producing a demonstrably weaker outcome than the repo's excellence bar demands. The bundle does not provide one.

### F4. The "split/ambiguous" classification is used too often and risks becoming a non-answer — CONCERN (medium)

**File references:** `checkpoint-4-codex-load-bearing-surfaces-and-seams.md:88-96`, `checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:79-87`, `checkpoint-4-cross-lane-seam-synthesis.md:16-25`

Four of the six seams in the seam synthesis carry `split/ambiguous` as either primary or secondary ownership. While the category is defined and used honestly, its prevalence means the bundle's ownership logic is less decisive than it appears. A later auditor looking at the ownership table would see: 2 clean classifications, 4 ambiguous ones — and could reasonably ask whether the audit has genuinely resolved ownership or merely described it.

The most important case is `execution-completion plus verification/UAT closure`, classified as `workflow-protocol` with `doc-level doctrine` secondary. But the converged synthesis (`checkpoint-4-converged-synthesis.md:48`) says the biggest non-machinery deficits include "debt-carrying completion semantics" — which is squarely in the `split/ambiguous` territory the seam synthesis left it in. The synthesis should have forced a sharper ownership call here or explicitly stated why the ambiguity cannot be resolved at this checkpoint.

### F5. The branch/worktree seam is honestly labeled under-evidenced, but the bundle does not say what evidence would resolve it — OBSERVATION (medium)

**File references:** `checkpoint-4-cross-lane-seam-synthesis.md:24-31,43,49`, `checkpoint-4-converged-synthesis.md:28,80`

The bundle correctly labels this seam as under-evidenced and recommends it not become the centerpiece of Checkpoint 5. That is honest. But the bundle also says "unless a narrower follow-up proves it materially defective" without describing what such a follow-up would look like — what specific test, what observable failure mode, what trigger. A later reader cannot act on this guidance because it is a conditional with no operational content.

### F6. The Codex lane's use of unofficial issue evidence is well-qualified but structurally fragile — OBSERVATION (low-medium)

**File references:** `checkpoint-4-codex-load-bearing-surfaces-and-seams.md:18-19,52-55,115-118`

The Codex lane cites four open GitHub issues (`#17560`, `#17776`, `#17928`, `#17939`) as evidence for continuity risk, each with careful qualifiers ("WSL-specific," "not as universal Codex truth," etc.). This is epistemically honest. However, the four issues were all checked on the same date (2026-04-15), and their "still open" status is now the basis for the continuity posture. If any of these issues have been closed or addressed in a newer Codex release since that date, the continuity risk assessment would change. The bundle does not note this temporal fragility or suggest when a re-check would be warranted.

### F7. The converged synthesis does not address whether the internal-verification-agent review has already occurred — OBSERVATION (low)

**File references:** `checkpoint-4-bundle-internal-review-spec.md`, `checkpoint-4-converged-synthesis.md:84-89`

The review spec (`checkpoint-4-bundle-internal-review-spec.md`) calls for an `internal-verification-agent` review at `gpt-5.4 high`. The converged synthesis's readiness handoff says "review the Checkpoint 4 bundle under the strengthened readiness review policy" but does not state whether the internal review has already been completed. The cross-vendor review file (`checkpoint-4-bundle-cross-vendor-review-opus-r1.md`) is empty, confirming this is the first review. The internal review file is not listed in the untracked files from the git status. This means the review sequencing in REVIEW-POLICY.yaml (internal first, then cross-vendor) may not have been followed. This is a process observation, not a content finding — but a later auditor tracking closure hygiene would flag it.

---

## What Is Already Strong

**The four-lane split was the right structural decision.** Checkpoint 3 justified splitting GSD into three sublanes plus a Codex lane, and Checkpoint 4 honored that split without collapsing back. The result is that each lane's findings are actually about different things — workflow contract quality, operative role-contract fidelity, runtime truth, and Codex-side control surfaces. The seam synthesis then meaningfully reconciles them rather than just restating them. This is real audit architecture, not presentation theater.

**Factual claims are well-grounded.** I independently verified the "12 of 24 `.toml` files carry legacy refs" claim (confirmed), the home-level `~/.codex/AGENTS.md` stale content claim (confirmed: Reflect-era commands and "No hooks support" are literally present), and the bundle's description of `config.toml` trust and precedence. The bundle is not bluffing its evidence base.

**The seam synthesis honestly preserves the branch/worktree under-evidenced status.** Many audit bundles would have either silently dropped this seam or promoted it to fill out the finding list. This bundle does neither — it labels it under-evidenced, keeps it visible, and recommends it not drive Checkpoint 5 scope. That is good epistemic hygiene.

**The strongest criticisms are genuinely strong.** The "excellence-capable but not excellence-demanding" formulation (`checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:65`) captures a real structural pattern — the workflow front-loads nuance and then introduces closure-biased exits downstream. This is a non-obvious finding that requires reading across multiple workflow files to see, and the bundle backs it with concrete source references to auto-approved checkpoints, `Proceed anyway` branches, and advisory review.

**The Codex lane's treatment of unofficial evidence is exemplary.** Each GitHub issue is individually qualified, never treated as universal product truth, and used only to support a specific, narrow claim about present-state risk. This is materially better than the typical pattern of either ignoring unofficial evidence entirely or treating it as authoritative.

**The runtime/config lane ran actual spot checks.** This lane did not just read files — it executed `config-get`, `init`, and `resolve-model` commands and reported the actual outputs. That makes its claims about effective runtime state empirically grounded rather than purely inferential.

---

## Gap Classification

| Finding | Classification | Rationale |
| --- | --- | --- |
| F1: Counter-hypothesis (rerun without CP5) not seriously tested | `revise-current` | The converged synthesis should explicitly test whether fixing only the core-chain `.toml` files could satisfy the rerun's immediate needs, deferring broader machinery work. This does not require reopening the lanes — it requires a sharper argument in the synthesis. |
| F2: Checkpoint 5 scope lacks stopping rule / exit criteria | `revise-current` | The bounded-Checkpoint-5 verdict is only meaningful if "bounded" is operationalized. Add concrete exit criteria before closure. |
| F3: Review-pressure finding repeated without empirical grounding | `defer-nonblocking` | The structural finding is sound. Empirical evidence of advisory review producing weak outcomes would strengthen it but is not required for Checkpoint 4 closure — it becomes a Checkpoint 5 or rerun-time concern. |
| F4: `split/ambiguous` used too prevalently | `accept` | The ambiguity appears to be genuine rather than avoidable. The bundle is honest about it. A later checkpoint can force sharper ownership where needed. |
| F5: Branch/worktree under-evidenced seam lacks resolution criteria | `defer-nonblocking` | Not blocking for Checkpoint 4 closure. Should be addressed when/if Checkpoint 5 scope is finalized. |
| F6: Unofficial issue evidence is temporally fragile | `defer-nonblocking` | Honest for now. A re-check before rerun would be prudent but is not a Checkpoint 4 obligation. |
| F7: Internal review sequencing unclear | `defer-nonblocking` | Process hygiene, not content gap. |

---

## Verdict

- status: `provisional`
- explanation:

The bundle is genuinely strong in its factual grounding, its structural architecture, its honest treatment of ambiguity, and its identification of the key weakness patterns (operative worker drift, closure-biased exits, downstream claim-discipline collapse). It is significantly above the "technically passes" threshold.

However, it is not yet closure-ready because the central verdict — "open a bounded Checkpoint 5" — has two weaknesses that would not survive a strong later audit:

1. **The counter-hypothesis was not tested.** The bundle never seriously asks whether fixing only the five core-chain `.toml` files (the roles the rerun will actually exercise) plus a narrow doctrine patch could make the rerun viable without a full Checkpoint 5. That makes the verdict look like escalation-by-default rather than a forced conclusion from the evidence.

2. **"Bounded" is not operationalized.** The proposed Checkpoint 5 has three items, two of which are concrete and one of which ("decide which surfaces need explicit durable capture") is open-ended. Without exit criteria, the "bounded" qualifier is aspirational rather than enforceable.

Both of these can be fixed inside the current checkpoint without reopening the lanes. The converged synthesis needs approximately 2-3 additional paragraphs: one testing the counter-hypothesis, one stating Checkpoint 5 exit criteria, and optionally one distinguishing rerun-blocking from post-rerun machinery improvements.

---

## Required Next Action

- exact next step: Revise `checkpoint-4-converged-synthesis.md` to (a) explicitly test the counter-hypothesis that the rerun could proceed with only core-chain `.toml` alignment and no full Checkpoint 5, and (b) add concrete exit criteria for Checkpoint 5 scope. If the counter-hypothesis survives testing, the verdict may need to change; if it does not, the synthesis is stronger for having tested it.
- owner / lane: The authoring lane (Codex `gpt-5.4 xhigh`) should produce the revision. A second cross-vendor reread is not required for this revision unless the verdict itself changes.
- commit implication: `no commit yet` — revise then re-review, then checkpoint.

---

## Independence Note

- Does this review satisfy the checkpoint's independent-review requirement? **Yes**, subject to the `revise-current` items being addressed. This is a cross-vendor reread by a different model family (Claude Opus 4.6) than the authoring agent (GPT-5.4), providing genuine vendor independence.
- Was a cross-vendor lane available? **Yes** — this review is that lane.
- Which Claude lane was appropriate and why? **claude-opus-4.6** — per REVIEW-POLICY.yaml (`checkpoint "4": preferred_cross_vendor_model: claude-opus-4.6`), this checkpoint involves workflow/harness doctrine reshaping, which the policy correctly routes to the higher-stakes Claude model.
- What did independence add? The cross-vendor lens identified F1 (counter-hypothesis not tested) and F2 (unbounded Checkpoint 5 scope) as weaknesses that the authoring agent's own synthesis did not surface. These are not factual errors — they are structural gaps in the argument that an author immersed in the evidence is less likely to notice. The factual claims all survived independent verification, which increases confidence in the evidence base even while the verdict needs tightening.
