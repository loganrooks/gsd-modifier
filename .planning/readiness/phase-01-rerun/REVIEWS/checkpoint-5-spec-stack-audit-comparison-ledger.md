# Checkpoint 5 Spec Stack Audit Comparison Ledger

This ledger compares the current Checkpoint 5 audits by production conditions and self-justification quality.

It does not flatten them into one consensus. It qualifies their standing so the next spec revision can be governed by the strongest surviving claims.

## Compared Artifacts

1. [checkpoint-5-spec-stack-internal-audit-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-internal-audit-r1.md)
2. [checkpoint-5-spec-stack-cross-vendor-review-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-cross-vendor-review-opus-r1.md)
3. [checkpoint-5-spec-stack-falsification-audit-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-falsification-audit-r1.md)
4. [checkpoint-5-spec-stack-gap-exposure-audit-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-audit-r1.md)
5. [checkpoint-5-spec-stack-gap-exposure-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-cross-vendor-opus-r1.md)

## Artifact Standing

| Artifact | Governing spec / framing | Independence | Source coverage | Self-justification | Likely bias / blind spot | Current standing |
| --- | --- | --- | --- | --- | --- | --- |
| `internal-audit-r1` | older general audit spec | internal | broad and useful, but older framing | `medium-strong` | can under-own shared contract consequences because the spec was less explicit | `supporting` |
| `cross-vendor-review-opus-r1` | older cross-vendor review prompt | cross-vendor | broad and useful, but older framing | `strong` | more likely to stop at local propagation fixes rather than wider contract-chain consequences | `supporting` |
| `falsification-audit-r1` | older base spec plus stronger pressure framing | internal | strong on topology and chain-tail rereads | `medium` | can over-promote scope activation because pressure framing rewards challenge more than calibration | `challenge-artifact` |
| `gap-exposure-audit-r1` | superseding gap-exposure spec | internal | strongest explicit propagation and contract reads | `strongest` | can still overcall strictness at the verdict layer | `governing-comparison-set` |
| `gap-exposure-cross-vendor-opus-r1` | superseding gap-exposure cross-vendor prompt | cross-vendor | strongest explicit propagation and contract reads | `strongest` | slightly more permissive on whether implementation may begin before revision | `governing-comparison-set` |

## Comparison Notes

- [d:c:r] `reasoning level` is not treated as dispositive here. It is one production condition among others, and it matters less than the governing spec quality, actual source coverage, and self-justification of the resulting claims.
- [d:c:i] The two `gap-exposure` artifacts carry the highest standing because they were produced under the strongest comparison frame for the actual question: what remains incomplete, under-owned, contradictory, or prematurely deferred in the candidate stack.
- [d:c:i] The older internal and cross-vendor audits remain useful as supporting confirmation signals because they independently surfaced major propagation gaps even before the stronger gap-exposure framing existed.
- [d:c:r] The falsification audit should be treated as a challenge artifact: useful for surfacing possible undercalled scope, but not governing by itself unless its stronger claims survive comparison against the gap-exposure pair.

## Convergent Claims

- [e:c+r:i] The current candidate stack is not complete enough as written to safely govern implementation. This is convergent across all five artifacts.
- [e:c+r:i] The main problem is under-owned propagation, not that the four named workflow seams are fundamentally wrong. This is convergent across all five artifacts.
- [e:c+r:i] Workflow edits need explicit tracked overlay / materialization ownership if they touch gitignored `.codex` runtime surfaces. This is convergent across the older internal audit, older cross-vendor audit, and falsification audit, and consistent with the gap-exposure pair’s broader contract concerns.
- [e:c+r:i] `RESEARCH.md` propagation is incomplete unless the template and runtime-authoritative researcher/checker surfaces are accounted for. This is convergent across the gap-exposure pair and supported by the older cross-vendor audit.
- [e:c+r:i] Richer `CONTEXT.md` / steering semantics are not safe unless planner-side consumption is explicitly handled. This is convergent across the gap-exposure pair and supported by the older internal audit.
- [e:c+r:i] Debt-carrying completion is not just an `execute-phase.md` wording issue; downstream completion semantics and contract surfaces remain relevant. This is convergent across the gap-exposure pair and supported by the older cross-vendor audit.

## Supported But Not Fully Convergent

- [p:r:i] The existing `future_preservation` plan contract is probably the strongest structured carrier for the new steering-traceability obligation. This is strongly argued in the internal gap-exposure audit and not contradicted elsewhere, but it is not yet repeated in the other artifacts.
- [p:r:i] Wrapper alignment is likely lighter than first feared because most wrappers are thin adapters, but it should still remain in the same checkpoint rather than as a distant cleanup. This is supported by the cross-vendor gap-exposure review and the internal gap-exposure audit.

## Contested Claims

- [o:r:i] Whether implementation of the four workflow edits may begin before the spec is revised is contested.
  - the internal gap-exposure and falsification audits say the spec should be revised first
  - the cross-vendor gap-exposure review says implementation of the workflow edits may begin now if propagation ownership is fixed before completion
- [o:r:i] Whether the chain-tail / completion machinery (`verify-work`, phase completion, progress, milestone counting) must be promoted into immediate active scope is contested.
  - the falsification audit pushes hardest here
  - the gap-exposure pair clearly says the completion contract is under-owned, but is less categorical about immediate full promotion
- [o:r:i] Whether `R5.7` is already active rather than conditional is contested.
  - the falsification audit promotes it most strongly
  - the other audits more narrowly require explicit materialization ownership without fully promoting the broader hardening task

## Pressure-Only Or Challenge Claims

- [p:r:i] `gsd-research-phase` should be promoted into active Checkpoint 5 ownership right now.
  - This is argued strongly in the falsification audit.
  - It is not yet repeated in the gap-exposure pair.
  - Current standing: `pressure-only challenge`, not yet governing.
- [p:r:i] The accepted chain tail through `verify-work/UAT`, roadmap completion, progress counting, and milestone counting must all become active scope immediately.
  - This is a powerful challenge from the falsification audit.
  - It has not yet achieved convergence.
  - Current standing: `pressure-only challenge`.

## Weak Or Under-Argued Claims

- [a:r:i] None of the five artifacts contains an obviously frivolous major claim.
- [p:r:i] The weakest major claims are the ones that rely mostly on scope escalation by implication rather than on explicit contract-chain demonstration.
  - those appear mainly in the falsification audit
  - they should be treated as prompts for further adjudication, not immediate scope doctrine

## Working Adjudication Rule

- [d:c:i] For the next Checkpoint 5 spec revision:
  - revise first from the `convergent` set
  - then include `supported but not fully convergent` claims where they strengthen structure without major scope explosion
  - record `contested` claims explicitly as unresolved scope decisions
  - keep `pressure-only challenge` claims visible, but do not let them govern the revision unless later adjudication promotes them
