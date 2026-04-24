# Wave-1 Comparative Disposition: Opus R1

Status: first comparative disposition  
Date: 2026-04-20

## Scope

- outputs under review:
  - [01-mission-reconstruction-opus47-max-r1.md](../outputs/01-mission-reconstruction-opus47-max-r1.md)
  - [02-outcome-and-underreach-audit-opus47-max-r1.md](../outputs/02-outcome-and-underreach-audit-opus47-max-r1.md)
  - [03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md](../outputs/03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md)
  - [04-operator-orchestration-pressure-opus47-max-r1.md](../outputs/04-operator-orchestration-pressure-opus47-max-r1.md)
- launch basis:
  - frozen prompt/spec/packet commit `f548a48`
  - launch/output recording commit `9c8aaa9`

## Overall Judgment

- [d:r:i] The first four Wave-1 Opus lanes are strong enough to accept as substantive evidence rather than reroll immediately.
- [d:r:i] Their strongest convergence is not a single recommendation. It is a clarified causal stack:
  - the readiness package had a larger implicit mission than its explicit rerun-facing mission admitted
  - it achieved real doctrine/governance/mapping gains
  - it still underreached in visible places where doctrine translated back down into lighter closure or narrower intervention
  - the map was not directionally wrong, but it was structurally under-mapped at several runtime-authoritative seams
  - operator pressure amplified those weaknesses but generally did not cause them
- [d:r:i] This is enough to move the workspace past `first-lane execution` and into Wave-2 shaping, but not enough to skip comparative inheritance work. The outputs should be inherited, not merely admired.

## What Converged

### 1. The package was bigger than a rerun-prep checklist

- [d:r:i] The mission lane argues that the package was a four-layer structural intervention: doctrine preservation, governance normalization, harness-ownership realignment, then rerun.
- [d:r:i] The outcome lane independently supports that scale judgment by treating doctrine/governance gains and runtime-carrier gains as real outcomes rather than local polish.
- [d:r:i] Accepted consequence: future lanes should stop talking about the package as if it were mainly `docs cleanup before rerun`.

### 2. The package was neither `mostly fine` nor `mostly churn`

- [d:r:i] The outcome lane is right to reject both simplifications.
- [d:r:i] The mission lane's tension analysis explains why both simplifications fail: a real anti-closure package can still get trapped in recursive inward motion.
- [d:r:i] Accepted consequence: later synthesis should preserve both the real gains and the named underreaches rather than flattening toward acquittal or failure theater.

### 3. Mapping is not sufficient

- [d:r:i] The mapping lane's central verdict, `directionally adequate and structurally under-mapped`, is the strongest concise formulation on the board right now.
- [d:r:i] The lane's runtime-local emphasis also matters: upstream docs refresh is real but does not close repo-local runtime adequacy.
- [d:r:i] I locally verified the lane's strongest concrete runtime claim: `13/31` `.codex/agents/*.toml` files still reference `CLAUDE.md`.
- [d:r:i] Accepted consequence: no later lane should treat upstream docs quality or bridge-audit corroboration as enough to declare runtime-local mapping strong enough for structural intervention.

### 4. Operator pressure is mostly amplifying, not primary

- [d:r:i] The operator lane usefully blocks a lazy explanatory fallback.
- [d:r:i] Its narrow exception also matters: launch-truth vigilance is genuinely closer to a primary pressure because the machinery still depends on manual capture and explicit protocol discipline.
- [d:r:i] Accepted consequence: operator pressure should remain in the causal stack, but mostly as a multiplier of mapping / doctrine / intervention-shape weaknesses rather than as the dominant cause.

## Highest-Signal Contributions By Lane

### Mission Reconstruction

- [d:r:i] Highest-signal contribution: explicit mission and implicit load-bearing mission diverged, and the implicit mission kept winning locally.
- [d:r:i] This gives the workspace a much stronger explanation for why rerun readiness kept receding without reducing the package to incompetence or drift.

### Outcome And Underreach Audit

- [d:r:i] Highest-signal contribution: underreach is not one thing. The lane's split among mapping-heavy, judgment-heavy, and interaction-heavy failures is more useful than a flat `package underreached` verdict.
- [d:r:i] I also locally verified the lane's strongest propagation claim: `.codex/` still has zero matches for `post-verificationist`, `post-falsificationist`, `gap-exposure`, `completeness-challenge`, and `anti-regret`.

### Mapping Adequacy And Comparative Mapping

- [d:r:i] Highest-signal contribution: it keeps `mapping adequacy` and `comparative mapping` distinct and refuses to let docs refresh launder runtime gaps.
- [d:r:i] The live-probed runtime claims materially strengthen this lane relative to a purely document-comparative version.

### Operator Orchestration Pressure

- [d:r:i] Highest-signal contribution: it narrows operator-pressure explanation instead of inflating it.
- [d:r:i] That narrowing matters because it keeps Wave 2 from turning into a soft `the operator was overloaded` absolution lane.

## Accepted Inheritance

- [d:r:i] Accept all four outputs as substantive Wave-1 evidence.
- [d:r:i] Do not reroll any of the four lanes immediately.
- [d:r:i] Treat the mapping lane and the operator lane as jointly decisive for what should happen next:
  - stronger runtime-authority and materialization concerns are real
  - but the workspace still has not earned a blanket switch to `Proposal F`
  - the right next move is to let Wave 2 pressure suppressed opportunities and rerun shape with these findings in hand

## Narrow Corrections To Carry Forward

- [d:r:i] The mission lane's theory-of-change analysis should not be mistaken for a full rerun-shape recommendation. That belongs later.
- [d:r:i] The outcome lane's `16` underreaches are useful, but later lanes should avoid turning the register into a hidden scoring ladder.
- [d:r:i] The mapping lane's runtime probes are strong, but later lanes should still distinguish `runtime drift found` from `full harness-code-first switch justified`.
- [d:r:i] The operator lane should not be allowed to quietly downgrade launch-truth machinery pressure back into a mere hygiene issue.

## What This Disposition Settles

- [d:r:i] First-lane execution has succeeded; the workspace no longer lacks substantive Wave-1 returns.
- [d:r:i] No immediate first-lane reroll is warranted.
- [d:r:i] The strongest next object is now Wave 2 planning:
  - `suppressed-opportunity-and-non-intervention`
  - `rerun-design`

## What Remains Open

- [o:r:i] Whether the `13/31` stale `.toml` runtime-authority problem is severe enough to trigger an early bounded `Proposal F` move before broader Wave-2 synthesis.
- [o:r:i] Whether the bridge audit's `guarded hybrid reseed` verdict should now be classified as merely `partially under-carried` or more strongly as a tame program-level underreach.
- [o:r:i] Whether Wave 2 should be Opus-only first or whether at least one counterpart review lane should be launched in parallel to resist a single-model Wave-2 groove.

## Immediate Next Move

- [d:r:i] Write Wave-2 lane specs against these four accepted returns rather than against the older contract/manifests alone.
- [d:r:i] The next two specs should inherit this disposition explicitly so they start from converged first-lane findings rather than reconstructing them from scratch.
