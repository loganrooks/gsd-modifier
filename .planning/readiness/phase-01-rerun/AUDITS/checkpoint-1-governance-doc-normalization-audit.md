# Checkpoint 1 Governance-Doc Normalization Audit

## Research Frame
- Mode: `synthesis`
- Question:
  - Are the standing governance docs expressed at the right level of abstraction and ownership to carry the repo's doctrine rigorously into the rerun sequence?
- Scope:
  - root governance layer and planning-local governance layer
  - document ownership, abstraction level, duplication, residue, and likely machinery-owned spillover
  - readiness framing from the Checkpoint 1 spec, gate, and plan
  - doctrinal fidelity against the stronger standard set by `05-gap-closure`
- Non-goals:
  - do not patch governance docs in this lane
  - do not redesign the GSD/Codex harness in this lane
  - do not update readiness package state
- Stop condition:
  - a Checkpoint 2 patch pass can act from this artifact without guessing what belongs where or why
- Lane / independence:
  - `replanning/revision/gap-filling`
  - `authoring` lane per the Checkpoint 1 spec ([checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:133))

## Artifacts Read
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:1)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:1)
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:1)
- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:1)
- [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:1)
- [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md:1)
- [checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:1)
- [checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md:1)
- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:130)
- [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md:1)
- [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml:1)
- [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md:22)
- [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml:3)
- [05-post-sensitivity-response-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md:28)
- [05-canon-uplift-milestone-2-steering-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md:46)
- [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:1)
- [review-trail-framework.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md:27)

## Path Of Inquiry
- Entry point:
  - Start from the Checkpoint 1 question and gate: determine whether each rule lives in the document whose scope justifies it, and whether the docs would still read as coherent doctrine if recent audit memory disappeared ([checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:7), [checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md:27), [checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md:34)).
- Branches considered:
  - whether the core problem was doctrinal regression or mainly ownership/duplication drift
  - whether repeated rules were intentional prompt-time summaries or competing canonical owners
  - whether current hook/config notes belong in workflow docs or in a deeper harness/config surface
  - whether references to prior audit artifacts were durable methodology or lane sediment
- Branches pursued:
  - compare each document's stated scope to its actual contents
  - compare repeated rule clusters across docs: claim typing, checkpoint/delegation policy, artifact taxonomy, hooks/config posture
  - cross-check whether the standing layer still preserves the anti-pass/fail and non-foreclosure standard earned in `05-gap-closure`
  - use the multi-layer governance synthesis to separate doc-owned cleanup from machinery-owned follow-through
- Branches deferred or abandoned:
  - actual patch wording and patch sequencing beyond checkpoint-ready units
  - redesign of hook/config/template surfaces
  - remote host verification, hook implementation review, or CI implementation detail
- Unexpected branches / reframings:
  - the main issue is not that the docs flattened the doctrine earned in `05-gap-closure`; it is that several rules now have too many owners at mismatched levels of specificity
  - some duplication is justified and should survive; the problem is not overlap in itself, but overlap without a clear detailed owner

## Assumptions Surfaced
- `[a:c+r:i]` Document scope statements are the primary signal for ownership in this audit, because each target doc now explicitly states what kind of governance it is supposed to carry ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:9), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:5), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:5)).
  - Why it matters: the normalization question is mostly an ownership question.
  - What could weaken it: a newer governing artifact explicitly redefining the owners.
- `[d:c:i]` Checkpoint 1 is meant to normalize docs before deeper harness scoping, so machinery-owned concerns should be recorded rather than prematurely solved here ([checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:11), [checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:24), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:240)).
  - Why it matters: it prevents this audit from collapsing Checkpoint 3 into markdown cleanup.
- `[d:c:i]` `05-gap-closure` already set the governing standard for doctrinal fidelity: preserve open branches, avoid pass/fail closure, and reduce future distortion from naming density and silence ([05-post-sensitivity-response-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md:52), [05-post-sensitivity-response-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md:77), [05-canon-uplift-milestone-2-steering-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md:58), [05-canon-uplift-milestone-2-steering-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md:103)).
  - Why it matters: this audit should not reopen canon doctrine unless the standing governance docs have undercut that standard.
- `[a:c+r:i]` `.planning/CLAIM-TYPES.md` is the intended durable home for detailed marker semantics, because it names itself as the deeper reference and already points back to the AGENTS docs rather than the reverse ([.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md:3), [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md:12)).
  - Why it matters: it gives Checkpoint 2 a plausible owner for the detailed legend.
  - What could weaken it: an explicit repo decision that the detailed legend must remain duplicated in prompt-time docs.

## Evidence Base
### Direct evidence
- `[e:c:i]` The five target docs have explicit and different scopes:
  - root `AGENTS.md` should stay narrow, stable, and agent-facing ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141))
  - `.planning/AGENTS.md` exists to keep planning/audit/canon work rigorous without bloating root ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:9))
  - `WORKFLOW.md` owns broader git, devops, and artifact process ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:5))
  - `AI-GUARDRAILS.md` is broader than `AGENTS.md` and carries signoff/guardrail rationale ([AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:5))
  - `ARTIFACT-GOVERNANCE.md` owns artifact classes, retention, and workspace-readiness doctrine ([ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:3))
- `[e:c:i]` The standing docs do preserve the key `05-gap-closure` anti-flattening doctrine:
  - root `AGENTS.md` rejects thin pass/fail closure and warns against umbrella terms and silent winner-selection ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:49), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:102))
  - `.planning/AGENTS.md` explicitly rejects `safe enough to proceed` closure and requires future-flexibility statusing ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:162), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:178))
  - those standing rules track the `05` response plan and uplift proposal rather than undercutting them ([05-post-sensitivity-response-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md:58), [05-post-sensitivity-response-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md:114), [05-canon-uplift-milestone-2-steering-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md:92))
- `[e:c:i]` The most obvious normalization clusters are repeated at multiple ownership levels:
  - detailed claim-marker legend in root `AGENTS.md`, `.planning/AGENTS.md`, and `.planning/CLAIM-TYPES.md` ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:70), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:86), [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md:18))
  - checkpoint/delegation sequencing in root `AGENTS.md`, `.planning/AGENTS.md`, and `WORKFLOW.md` ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:124), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:47), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:49))
  - artifact taxonomy/staleness rules in `.planning/AGENTS.md` and `ARTIFACT-GOVERNANCE.md` ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:29), [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:7), [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:66))
- `[e:c:i]` Both AGENTS files still point to `review-trail-framework.md` as a detailed reference even though that file explicitly governs the next layer of artifacts for one dated exploratory audit, not a durable repo-wide process surface ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:93), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:156), [review-trail-framework.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md:31))
- `[e:c:i]` `WORKFLOW.md` currently mixes durable workflow doctrine with machinery-current implementation detail in its hook pilot and GSD config notes ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:140), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:146))
- `[e:c:i]` The multi-layer governance synthesis independently diagnosed the broader weakness as under-specified handoffs between layers, not absence of doctrine, and explicitly kept some surfaces open for later harness work ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:149), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:167), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:263))

### Inference and interpretation
- `[e:c+r:i]` The governance layer is not failing because it forgot the repo's doctrine; it is failing normalization because several important rules now have too many owners, too much duplicated detail, or too much lane-shaped residue for docs that claim to be stable ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:9), [checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md:27))
- `[e:c+r:i]` Checkpoint 2 should therefore be a targeted normalization and owner-selection pass, not a fresh doctrine rewrite or a hidden Checkpoint 3 harness redesign ([checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:11), [checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:24), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:132))
- `[a:c+r:i]` The most durable shape appears to be:
  - detailed semantics and large taxonomies get one owner
  - AGENTS docs keep scoped prompt-time reminders
  - machinery-current pilot/config details move toward a deeper harness/config surface
  - workflow docs keep only the durable posture for those surfaces

### Unknowns
- `[o:c:i]` It is still open whether `WORKFLOW.md` should retain a slim summary of current hooks/config posture or whether that should move entirely into a deeper harness surface during Checkpoint 3 ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:146), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:175))
- `[o:c:i]` It is still open how much of `.planning/AGENTS.md` should keep a compressed artifact taxonomy versus only a pointer to `ARTIFACT-GOVERNANCE.md`; the current evidence supports normalization, but not one exact compression shape ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:29), [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:7))
- `[o:c:i]` The exact machinery/home for issue or PR templates, review routing, verify entrypoints, and non-phase external reread protocol remains open and belongs to later harness scoping rather than this audit ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:146), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:173))

## Dependencies And Relations
| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Claim-typing owner | `AGENTS.md`, `.planning/AGENTS.md`, `.planning/CLAIM-TYPES.md` | audit readability, prompt budget, Checkpoint 2 patch scope | high |
| Checkpoint/delegation owner | `AGENTS.md`, `.planning/AGENTS.md`, `WORKFLOW.md` | agent behavior, checkpoint discipline, verification boundaries | medium |
| Artifact taxonomy owner | `.planning/AGENTS.md`, `ARTIFACT-GOVERNANCE.md` | planning hygiene, statusing, artifact retention interpretation | medium |
| Hook/config posture | `WORKFLOW.md`, current harness state, later Checkpoint 3 scoping | stale-doc risk, machinery/doc boundary, future workflow design | high |

## Integrated Decision Structure
- `[e:c:i]` Normalization verdict: the standing governance layer is doctrinally strong enough to carry the repo's current anti-pass/fail and non-foreclosure doctrine, but it is not yet normalized enough in ownership, slimness, and residue control to be the final rerun-ready governance layer ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:49), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:178), [checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:7))
- `[e:c:i]` The highest-value Checkpoint 2 work is normalization, not doctrinal substitution: choose clearer detailed owners, shrink prompt-time duplicates, and remove residue that depends on one recent audit lane or one current machinery state ([checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md:27), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:132))
- `[a:c+r:i]` The machinery-shaped surfaces exposed here should be handed forward to Checkpoint 3 rather than normalized away inside prose, unless the Checkpoint 2 patch reveals that the standing docs truly cannot state a durable posture without them ([checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:26), [checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md:43), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:263))

## Document-by-document findings
### `AGENTS.md`
1. Classification: `cross-doc normalization`
   - The detailed claim-marker and source-basis legend is duplicated here even though root `AGENTS.md` says broader detail belongs elsewhere and `.planning/CLAIM-TYPES.md` already exists as the deeper reference ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:70), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141), [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md:3)).
   - Evidence is mixed: root `AGENTS.md` should still carry the high-level requirement to expose claim status and basis when it matters, but it does not need to be a full co-owner of the legend.
2. Classification: `cross-doc normalization`
   - The delegation/checkpoint block is more detailed than a root runtime summary needs and substantially overlaps both `.planning/AGENTS.md` and `WORKFLOW.md` ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:124), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:47), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:58)).
   - Evidence is mixed: hard root guardrails such as "do not delegate into an unresolved mixed worktree" should remain prompt-time visible; the full sequencing should not have three detailed owners.
3. Classification: `doc-local cleanup`
   - The `50+` player-count and mixed-scope architecture-lane lines read like lane-shaped residue inside a file that promises to stay narrow, stable, and agent-facing ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:104), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:106), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:263)).
   - Evidence is mixed: the learned risk is real, but the present wording is more case-shaped than the durable rule it is trying to protect.
4. Classification: `cross-doc normalization`
   - The "current detailed reference points" list still includes the dated `review-trail-framework.md`, which explicitly governs one exploratory audit's review-trail artifacts, not a stable repo-wide governance surface ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:93), [review-trail-framework.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md:31)).

### `.planning/AGENTS.md`
1. Classification: `cross-doc normalization`
   - The artifact-class and staleness block substantially duplicates `ARTIFACT-GOVERNANCE.md` instead of specializing planning-local behavior ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:29), [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:7), [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:78)).
   - Evidence is mixed: a subtree-local reminder is useful; the current block is larger than a reminder and reads like a second taxonomy owner.
2. Classification: `cross-doc normalization`
   - `.planning/AGENTS.md` is a more plausible home than root for planning-process claim typing, but the current detailed legend still overlaps too heavily with `.planning/CLAIM-TYPES.md` and carries the same audit-era reference list as root ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:86), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:156), [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md:12)).
   - Evidence is mixed: planning-local work needs more inline epistemic guidance than root; it still does not need a fully duplicated detailed legend if `CLAIM-TYPES.md` remains the durable reference.
3. Classification: `doc-local cleanup`
   - The pushback rule is sectioned under `Research And Audit Quality`, even though root `AGENTS.md` now frames pushback as a repo-wide quality rule for substantive work ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:60), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:59)).
   - Evidence is mixed: the current text is correct for research and audit work; the issue is section framing, not missing doctrine.
4. Classification: `strategic-opportunity`
   - The future-flexibility and canon-response sections are doing high-value doctrinal work and should survive normalization, but they may deserve sharper separation from the more mechanical artifact-discipline material so the file's highest-value rules stay easy to find ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:162), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:176)).

### `WORKFLOW.md`
1. Classification: `cross-doc normalization`
   - `WORKFLOW.md` is the most natural detailed owner for checkpoint/delegation sequencing, but the same policy is repeated elsewhere. Checkpoint 2 should normalize around that owner instead of maintaining three near-owners ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:45), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:58), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:124), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:47)).
2. Classification: `machinery-owned follow-through`
   - The hooks posture section mixes durable workflow doctrine with current pilot implementation details: exact hook events, config filename, and syntax migration guidance ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:146), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:147), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:150)).
   - Evidence is mixed: the durable rule belongs here, because hook posture is workflow policy; the current pilot manifest is closer to harness state and should inform Checkpoint 3.
3. Classification: `machinery-owned follow-through`
   - The GSD-specific note about the current `.planning/config.json` `branching_strategy` value is operationally useful today but is also machinery-current state that will stale faster than the rest of the workflow doctrine ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:138), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:140), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:175)).
   - Evidence is mixed: the repo does need a standing statement that branch discipline currently relies on repo convention; the raw config value is the unstable part.

### `AI-GUARDRAILS.md`
- No material normalization blocker found.
- The file stays at the right abstraction level for signoff boundaries, safe autonomy, research hygiene, and honesty, and its overlap with `AGENTS.md` reads as rationale plus guardrail rather than competing ownership ([AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:3), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:15), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:39), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:87)).

### `ARTIFACT-GOVERNANCE.md`
1. Classification: `strategic-opportunity`
   - The core artifact taxonomy, staleness protocol, and workspace-readiness rules are well-owned here and should stay here; the only mild durability risk is the `Repo-specific current guidance` block, which mixes durable retention doctrine with currently-hot examples ([ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:7), [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:66), [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:125)).
   - Evidence is mixed: this is explicitly repo-specific guidance, so it is not misplaced; it is simply the most likely part of the document to age fastest.

## Cross-document duplication and ownership drift
| Cluster | Current owners | Normalization verdict |
| --- | --- | --- |
| Claim typing and source-basis semantics | `AGENTS.md`, `.planning/AGENTS.md`, `.planning/CLAIM-TYPES.md`, plus standing references to `review-trail-framework.md` | Too many owners. Keep the detailed legend in `.planning/CLAIM-TYPES.md`, keep scoped reminders in AGENTS docs, and stop using the dated audit framework as a standing owner. |
| Checkpoint and delegation sequencing | `AGENTS.md`, `.planning/AGENTS.md`, `WORKFLOW.md` | Normalize around `WORKFLOW.md` as the detailed owner. Keep only concise, scoped prompt-time summaries in the AGENTS docs. |
| Artifact taxonomy and staleness rules | `.planning/AGENTS.md`, `ARTIFACT-GOVERNANCE.md` | `ARTIFACT-GOVERNANCE.md` should stay canonical. `.planning/AGENTS.md` should keep only planning-local deltas or pointers. |
| Hook/config posture | `WORKFLOW.md` plus current harness/config state | Split durable workflow posture from current pilot/config inventory. The latter is a Checkpoint 3 concern. |

- Evidence is mixed across the whole cluster analysis: some duplication is intentional and worth preserving for prompt-time visibility. The normalization problem is not "remove all overlap"; it is "stop making multiple files detailed co-owners of the same rule."

## Scope Expansions And Deferrals
- Defer:
  - actual patch wording and final phrasing choices for Checkpoint 2
  - validation of remote host branch-protection state
  - whether hooks/config posture gets a dedicated harness-status doc
- Follow-and-mark:
  - use `.planning/CLAIM-TYPES.md` as the likely detailed owner for claim-marker semantics in Checkpoint 2, but do not treat that owner choice as settled until the patch pass actually lands
- Revisit later:
  - issue / PR / MR templates, review routing, verify entrypoint, and non-phase external reread protocol in Checkpoint 3 or later, not as hidden sub-work of Checkpoint 1 ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:167), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:173))

## Likely Checkpoint 2 patch units
1. `claim-typing owner normalization`
   - compress root and planning AGENTS to policy reminders
   - keep detailed syntax and semantics in `.planning/CLAIM-TYPES.md`
   - remove or relocate standing references to the dated `review-trail-framework.md`
2. `checkpoint/delegation owner normalization`
   - designate `WORKFLOW.md` as the detailed sequence owner
   - leave only scoped prompt-time constraints in `AGENTS.md`
   - leave only true planning-local deltas in `.planning/AGENTS.md`
3. `artifact-governance boundary cleanup`
   - compress `.planning/AGENTS.md` artifact taxonomy and staleness restatement into pointers plus planning-local exceptions, if any
4. `root AGENTS residue cleanup`
   - generalize or relocate the `50+` and mixed-scope architecture-lane lines so the root doc better matches its own slimness promise
5. `workflow doctrine versus machinery split`
   - keep the durable workflow posture on hooks/config
   - slim or relocate current pilot/config specifics that are really harness-state notes

## Potential machinery-owned issues to carry into Checkpoint 3
1. Classification: `machinery-owned follow-through`
   - Hook pilot ownership is not just a wording problem. The repo likely needs a deeper home for current hook inventory, pilot status, and config-specific migration notes, while `WORKFLOW.md` keeps only the durable posture ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:146), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:263)).
2. Classification: `machinery-owned follow-through`
   - Branch/worktree operating rules still look under-materialized as machinery and workflow boundary surfaces. `06-converged-synthesis.md` keeps naming explicit branch/worktree rules as an open gap, which suggests Checkpoint 3 should inspect the harness and repo-ops surface rather than expecting prose alone to solve it ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:138), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:256), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:301)).
3. Classification: `machinery-owned follow-through`
   - Issue / PR / MR templates, review-owner routing, and linked issue-to-review artifacts are now explicitly named in `06-converged-synthesis.md` as governance surfaces that appear once remote review becomes real. They are not Checkpoint 1 doc-cleanup items, but they should be on the Checkpoint 3 map ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:146), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:167), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:267)).
4. Classification: `machinery-owned follow-through`
   - The canonical local verify entrypoint and later branch or PR CI surface remain open. Checkpoint 1 should not recast that as a prose problem, but Checkpoint 3 should keep it visible as a missing boundary surface ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:143), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:177), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:312)).
5. Classification: `machinery-owned follow-through`
   - The repo-local non-phase external-reread protocol/template remains explicitly deferred in the readiness plan. That is a later follow-through lane, not a Checkpoint 1 doc patch ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:173), [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md:34)).

## What can close now
- `[e:c:i]` The current evidence does not justify reopening `05-gap-closure` canon doctrine. The standing governance layer mostly preserves the stronger anti-pass/fail and non-foreclosure standard; the main issue is normalization, not doctrinal collapse ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:49), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:178), [05-post-sensitivity-response-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md:58))
- `[e:c:i]` Checkpoint 2 can proceed as a bounded governance-doc normalization patch focused on owner selection, slimness, and residue control rather than product doctrine ([checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:11), [checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md:27))
- `[e:c:i]` `AI-GUARDRAILS.md` and the core of `ARTIFACT-GOVERNANCE.md` can be treated as mostly stable owners rather than primary patch hotspots ([AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:3), [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:7))

## What must stay open
- `[o:c:i]` Exact patch wording and final owner boundaries remain for Checkpoint 2; this audit identifies the hotspots, not the final phrasing.
- `[o:c:i]` Whether hook/config pilot detail can be adequately slimmed inside `WORKFLOW.md` or needs a deeper harness-status surface remains open for Checkpoint 3 ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:146), [checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md:43)).
- `[o:c:i]` Branch/worktree rules, template/routing surfaces, verify-entrypoint ownership, and non-phase external reread protocol remain open machinery-follow-through questions rather than Checkpoint 1 closure items ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:301), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:173))
- `[o:c:i]` Review closure remains open until an independent reviewer rereads this audit; for Checkpoint 1, internal verification is the default and cross-vendor reread is strongly preferred if the audit materially changes standing governance or harness doctrine ([checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:139), [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md:24), [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md:49), [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml:49))

## Planning Handoff
- Treat the patch hotspots as:
  - `AGENTS.md`
  - `.planning/AGENTS.md`
  - `WORKFLOW.md`
- Treat `AI-GUARDRAILS.md` and `ARTIFACT-GOVERNANCE.md` as mostly stable unless the patch reveals narrow wording drift that must be corrected for consistency.
- Preserve as decided during Checkpoint 2:
  - anti-pass/fail doctrine
  - non-foreclosure and future-flexibility distinctions
  - human-signoff boundaries
  - artifact taxonomy as a concept
- Keep open during Checkpoint 2:
  - hook/config implementation ownership
  - branch/worktree and template/routing machinery surfaces
  - verify/CI and non-phase external-reread follow-through
- Review handoff:
  - this artifact is ready for independent review as Checkpoint 1 authoring output
  - do not close Checkpoint 1 on authoring alone
  - if the later patch materially reshapes standing governance or harness doctrine, prefer cross-vendor review before closure rather than relying only on same-vendor agreement ([CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md:51), [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md:54))

## Sources
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:1)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:1)
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:1)
- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:1)
- [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:1)
- [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md:1)
- [checkpoint-1-governance-doc-normalization-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit-spec.md:1)
- [checkpoint-1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-1.md:1)
- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:130)
- [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md:1)
- [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml:1)
- [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md:1)
- [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml:1)
- [05-post-sensitivity-response-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md:28)
- [05-canon-uplift-milestone-2-steering-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md:46)
- [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:1)
- [review-trail-framework.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md:27)
