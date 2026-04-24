# Checkpoint 5 Revised Implementation Spec — Cross-Vendor Reread (Claude Opus R1)

Reviewer: Claude Opus 4.6 (cross-vendor)
Date: 2026-04-15
Under review: [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
Governing policy: [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)

---

## Verdict

**PASS — strong enough to govern the first implementation slice.** The revised spec directly addresses all six convergent blocking gaps from the prior audit round. Propagation ownership is now explicit rather than implied. Contested claims remain contested. The two forced binary design decisions (planner contract width, debt-carrying propagation boundary) are real governance instruments, not prose hedges. The scope is honest about what it does and does not own.

No finding in this review rises to a blocking threshold. The residual risks below are addressable during implementation without spec revision, provided the implementer reads them. They would not survive later strong audit if silently ignored.

---

## Blocking Findings

None.

---

## Supported Scope Decisions

1. **Revise-first posture is correct.** The comparison ledger's convergent finding was that the original spec under-owned propagation. Revising the spec before patching is the right sequence and produces a cleaner audit trail than patching first and retrofitting ownership. The spec is self-consistent on this point. Sources: [impl-spec:19-25](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:19), [ledger:34](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-audit-comparison-ledger.md:34), [status:17-21](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md:17).

2. **The overlay pairing rule (§1) is well-drawn.** The clause "when such a portable overlay surface exists or can be added cleanly" correctly handles the fact that not all `.codex/` files currently have overlay counterparts. The rule is strong enough to prevent the original audit failure mode (runtime-only patches that don't survive reinstall) without mandating unnecessary overlay proliferation. Sources: [impl-spec:29-36](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:29), [setup-portable-gsd.sh:15-31](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:15).

3. **Forcing binary design decisions on planner width and debt-carrying boundary (§3, §6) is the right governance instrument.** The prior audits converged on these as under-owned. The revised spec does not attempt to pre-decide them; it forces the implementer to make a named, auditable choice. This is better than either premature prescription or silent deferral. Sources: [impl-spec:65-68](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:65), [impl-spec:95-98](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:95), [cross-vendor-r1:40-42](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-cross-vendor-opus-r1.md:40), [cross-vendor-r1:53](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-cross-vendor-opus-r1.md:53).

4. **`future_preservation` as default traceability carrier (§4) is the right call.** The mechanism already exists in the plan template with structured sub-fields (`protected_seams`, `non_decisions`, `posture_assumptions`), and the planner/checker prompts already know how to enforce it. Building on this is strictly preferable to inventing a parallel trace system. Sources: [impl-spec:72-74](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:72), [phase-prompt.md:25-28](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/phase-prompt.md:25), [gap-exposure-r1:35](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-audit-r1.md:35).

5. **Wrapper alignment as lighter near-contemporaneous verification (§7) is proportionate.** Inspection of the four named skill wrappers confirms the cross-vendor R1 assessment: they are thin adapters with `@`-references that auto-load workflow files. The only wrapper content that could lag is the `description` frontmatter. Patching only on active contradiction is the right scope. Sources: [impl-spec:100-107](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:100), [cross-vendor-r1:96-102](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-cross-vendor-opus-r1.md:96).

6. **Explicit non-goals are honest and well-bounded.** The deferred set (install pinning, archival provenance, path-portability, branch/worktree redesign, omnibus skill audit, new machine trace subsystem) is preserved from earlier checkpoints without silent expansion. Sources: [impl-spec:115-118](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:115).

7. **Review expectations gate is self-enforcing.** The spec requires its own reread acceptance before any patches count as checkpoint-moving evidence. This prevents the failure mode where implementation starts from an unapproved spec. Sources: [impl-spec:122-128](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:122).

---

## Contested Or Residual-Risk Decisions

### CR-1: `execute-phase.md` has no overlay counterpart (Residual risk — low)

[e:c+r:i] The spec's §1 requires paired overlay/materialization for every touched runtime surface. The spec's §6 names `.codex/get-shit-done/workflows/execute-phase.md` as active scope. But the current overlay tree does not contain an `execute-phase.md`:

```
tooling/portable-gsd/overlay/get-shit-done/workflows/
├── discuss-phase.md
├── discuss-phase-assumptions.md
├── discuss-phase-power.md
├── plan-phase.md
├── quick.md
├── research-phase.md
├── review.md
└── settings.md
```

The §1 clause "or can be added cleanly" covers this — the implementation would simply create a new overlay. But the spec does not acknowledge that this surface currently has no overlay, leaving the implementer to discover the gap. This is not blocking because the rule is clear enough to handle it, but it would be cleaner to note it.

Similarly, several reference and template files named in §5-§6 (`checkpoints.md`, `agent-contracts.md`, `ui-brand.md`, `summary.md`) have no overlay counterparts. The spec's clause handles this, but an implementer would benefit from knowing which surfaces need new overlays.

Sources: [impl-spec:29-36](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:29), [impl-spec:88-93](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:88), overlay tree inspection.

### CR-2: `agent-contracts.md` named for debt-carrying but not for research disposition (Residual risk — low)

[e:c+r:i] The spec names `agent-contracts.md` in §6 as part of the debt-carrying completion ownership set (line 92). But `agent-contracts.md` is also the canonical reference for research completion markers (`## RESEARCH COMPLETE`, `## RESEARCH BLOCKED`). If §2's research disposition changes add or modify markers, `agent-contracts.md` needs updating for that reason too — but it does not appear in §2's ownership list (lines 40-46).

An implementer working on §2 in isolation could patch the researcher, template, and checker while leaving the contract reference stale for research markers. This is a cross-reference gap, not a conceptual one.

Sources: [impl-spec:40-46](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:40), [impl-spec:88-93](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:88), [agent-contracts.md:13](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:13).

### CR-3: `the agent's Discretion` / `Claude's Discretion` naming mismatch not noted (Residual risk — medium)

[e:c+r:i] The internal gap-exposure audit identified a concrete naming mismatch: `templates/context.md` (the producer) writes `### the agent's Discretion` (line 43), while the planner .toml (the consumer) parses `## Claude's Discretion` (planner:69 per gap-exposure-r1). This is a pre-existing parse-boundary issue, not one introduced by the revised spec.

However, the revised spec's §3 forces a binary decision on planner contract widening — and that decision directly implicates this mismatch. If the implementer widens the planner's `<context_fidelity>` contract to include richer sections but doesn't resolve the naming mismatch, the widened contract would still silently drop the discretion section because the header names don't match.

The spec should have noted this as a known inconsistency to resolve as part of the planner contract decision. Its absence doesn't block the spec from governing implementation, but the implementer must be aware of it.

Sources: [context-template.md:43](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/context.md:43), [gap-exposure-r1:11](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-audit-r1.md:11), [impl-spec:65-68](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:65).

### CR-4: Chain-tail completion surfaces remain correctly contested

[o:c+r:i] The spec (§8, line 111) preserves the contested status of `verify-work.md`, `progress.md`, roadmap completion, and milestone counting. This is the right disposition given the comparison ledger — the falsification audit pushed hardest here but hasn't achieved convergence. The spec's conditional-widening rule ("check whether the chosen debt-carrying representation leaves those surfaces contradictory; only then should the checkpoint widen further") is a legitimate governance boundary. Sources: [impl-spec:111](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:111), [ledger:51-53](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-audit-comparison-ledger.md:51).

### CR-5: R5.7 and `gsd-research-phase` correctly deferred

[o:c:i] R5.7 portable reproducibility hardening and `gsd-research-phase` skill promotion are correctly preserved at their prior standing (contested, pressure-only respectively). Neither was silently promoted or dropped. Sources: [impl-spec:112-113](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:112), [ledger:54-63](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-audit-comparison-ledger.md:54).

---

## What Is Already Strong

1. **All six convergent blocking gaps from the prior round are now explicitly owned.** The comparison ledger's convergent claim set — RESEARCH.md propagation, CONTEXT.md consumption, overlay pairing, auto/default chain, debt-carrying completion, `future_preservation` traceability — is now either directly named as active scope or forced into a named binary decision. This is the primary test for the revision, and it passes. Sources: [ledger:34-39](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-audit-comparison-ledger.md:34), [impl-spec:29-98](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:29).

2. **The ownership lists are concrete, not aspirational.** Each section names specific files by full path. A later auditor can read the spec's §1-§7 ownership lists, check the patch set, and verify coverage without guesswork. This is materially better than the original spec, which named only four workflow files.

3. **The forced binary decisions are well-structured.** Both the planner contract width decision (§3, lines 65-68) and the debt-carrying boundary decision (§6, lines 95-98) present exactly two options with named consequences. The implementer cannot drift into an unnamed middle ground. This is real governance.

4. **Contested scope decisions survived revision without contamination.** Three contested items from the comparison ledger appear in §8 with their prior standing preserved and their conditional-widening triggers intact. No silent promotions, no silent drops. The spec earns the trust it claims.

5. **The stale skill reference is correctly separated.** Line 69 makes the `plan-phase.md` stale skill-path fix a distinct patch item, not a buried side-effect of the steering traceability change. This was specifically requested by the cross-vendor R1 review (PG-4, line 73).

6. **Auto/default pressure is scoped as a chain-level contract.** §5 names five surfaces across the chain (discuss-phase, plan-phase, checkpoints.md, executor .toml, ui-brand.md) rather than treating it as a discuss-phase-only note. This directly addresses the internal gap-exposure audit's gap 3. Sources: [impl-spec:78-84](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:78), [gap-exposure-r1:13](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-audit-r1.md:13).

7. **Citation discipline is maintained.** Every factual claim and ownership assertion cites specific source files and prior review artifacts. The citation chain from the comparison ledger through the spec to the live surfaces is traceable. The earlier stale `WORKFLOW.md:94` citation noted by the gap-exposure audit is no longer present in the revised spec.

---

## What Must Change Before Implementation

Nothing must change in the spec itself. The findings below should be communicated to the implementer as known conditions:

1. **The implementer must be aware that `execute-phase.md`, `checkpoints.md`, `agent-contracts.md`, `ui-brand.md`, and `summary.md` currently have no overlay counterparts.** The spec's §1 rule handles this ("or can be added cleanly"), but the implementer should decide early which of these need new overlays vs. which are non-portable reference files that live only in `.codex/`. This is an implementation-time decision, not a spec defect.

2. **The implementer must resolve the `the agent's Discretion` / `Claude's Discretion` naming mismatch as part of the §3 planner contract decision.** The mismatch is pre-existing but directly load-bearing on the planner contract width choice. If the planner contract is widened to consume richer steering, the naming must be synchronized. If the narrower option is chosen, the mismatch remains but is less consequential.

3. **The implementer should treat `agent-contracts.md` as a shared propagation surface across both §2 (research disposition) and §6 (debt-carrying completion), not only §6.** Any new or modified completion/disposition markers from either change must be reflected in the contract reference.

---

## Change Summary

| Prior Gap (from comparison ledger) | Status in Revised Spec | Assessment |
|---|---|---|
| RESEARCH.md propagation under-owned | §2 names template, researcher, checker | **Resolved** |
| CONTEXT.md consumption gap | §3 forces binary decision on planner width | **Resolved** |
| Overlay pairing not required | §1 makes pairing mandatory | **Resolved** |
| Auto/default chain-level ownership | §5 names five chain surfaces | **Resolved** |
| Debt-carrying completion under-propagated | §6 names full ownership set, forces boundary decision | **Resolved** |
| `future_preservation` underused | §4 names it as default carrier | **Resolved** |
| Stale skill reference bundled | §3 line 69 separates it | **Resolved** |
| Wrapper alignment scope unclear | §7 scopes as lighter verification | **Resolved** |
| Chain-tail completion surfaces | §8 preserves as contested | **Correctly deferred** |
| R5.7 portable hardening | §8 preserves as contested | **Correctly deferred** |
| `gsd-research-phase` skill | §8 preserves as pressure-only | **Correctly deferred** |

| Residual Risk | Severity | Who Must Address |
|---|---|---|
| Execute-phase and reference files lack overlays | Low | Implementer — decide per §1 rule |
| `agent-contracts.md` not in §2 ownership | Low | Implementer — cross-reference §2 and §6 |
| `the agent's Discretion` naming mismatch | Medium | Implementer — resolve as part of §3 decision |
| `templates/context.md` not in §3 ownership | Low | Non-issue — template is already ahead of workflow |

**Bottom line:** The revised spec is strong enough to govern implementation. It addressed all convergent blocking gaps from the prior audit round, preserved contested items honestly, and created real governance instruments for the two key design decisions. The residual risks are below the blocking threshold and are addressable during implementation. Start the implementation slice.
