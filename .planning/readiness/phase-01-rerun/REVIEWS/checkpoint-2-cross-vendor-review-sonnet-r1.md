# Checkpoint 2 Cross-Vendor Review — R1

## Header

- checkpoint:
  `Checkpoint 2 - Governance-doc normalization patch`
- artifact(s) under review:
  - `AGENTS.md`
  - `.planning/AGENTS.md`
  - `.planning/CLAIM-TYPES.md`
  - `WORKFLOW.md`
- review mode:
  `cross-vendor-reread`
- authoring lane:
  `orchestrator patch lane`
- reviewer:
  `Claude cross-vendor reviewer`
- model / reasoning or vendor:
  `claude-sonnet-4-6 high`
- baseline commit / artifact snapshot:
  `97bd603` plus current uncommitted patch snapshot
- independence relationship:
  `cross-vendor`

## Review Questions

- What is this review trying to falsify?
  Whether the patch improved ownership and slimness at the cost of erasing load-bearing distinctions, left material doc-doctrine drift unresolved, or converted machinery-owned follow-through into deceptively tidy prose cleanup.
- Which gate exit criteria are being tested?
  Docs are leaner, clearer, and more generally applicable; no important control lost through slimming; result is easier to audit, not merely shorter ([checkpoint-2.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-2.md:19)).
- Which quality questions are being tested?
  Whether the patch improved doctrine rather than only trimming text, and whether it preserved the distinctions `05-gap-closure` worked to earn ([checkpoint-2.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-2.md:23)).
- Which regressions are most relevant here?
  (a) Prompt-time reminders stripped below actionable usefulness; (b) anti-pass/fail or non-foreclosure doctrine quietly lost in slimming; (c) semantic ownership gaps between trimmed AGENTS prompts and the CLAIM-TYPES reference; (d) WORKFLOW.md durable posture collateral-damaged by machinery-state removal.

## Findings

No material findings.

Verification trail from this pass:

### Claim-typing owner normalization

The detailed legend is now held in `.planning/CLAIM-TYPES.md` ([.planning/CLAIM-TYPES.md](../../.planning/CLAIM-TYPES.md:17)). Both AGENTS files carry compact, structurally parallel prompt-time reminders — type, support, basis codes; join rule; internal citation expectation; external footnote expectation; pointer to CLAIM-TYPES.md for detail ([AGENTS.md](../../AGENTS.md:70), [.planning/AGENTS.md](../../.planning/AGENTS.md:72)). The reminders are short enough to stay prompt-budget-friendly while retaining the minimum an agent needs to apply the markers without stopping to consult the reference file.

The dated `review-trail-framework.md` reference has been removed from all three claim-typing surfaces — root `AGENTS.md`, `.planning/AGENTS.md`, and `.planning/CLAIM-TYPES.md` — exactly as the Checkpoint 1 audit recommended ([checkpoint-1-governance-doc-normalization-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit.md:134)).

### Checkpoint-commit and delegation content from `.planning/AGENTS.md`

The deleted block (checkpoint boundary types, delegation flow, anti-time-only-commit rule) was already the detailed content of `WORKFLOW.md`'s `Commits` and `Delegated work checkpoints` sections at baseline — before this patch touched those sections. The patch did not move this content to WORKFLOW.md; WORKFLOW.md was already the detailed owner. The deletion from `.planning/AGENTS.md` is normalization without content loss ([WORKFLOW.md](../../WORKFLOW.md:49), [WORKFLOW.md](../../WORKFLOW.md:56)).

Root `AGENTS.md` independently carries the hard agent-facing delegation constraints (baseline before delegation, do not delegate into an unresolved worktree, disposition before committing, prefer checkpoint boundaries between findings and fixes), which correctly remain prompt-visible ([AGENTS.md](../../AGENTS.md:111)).

### Artifact Discipline section slim in `.planning/AGENTS.md`

The new pointer to `ARTIFACT-GOVERNANCE.md` is accurate — that file holds the full taxonomy, staleness protocol, workspace-readiness rule, and generated-corpus policy ([ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:7)). The rules kept inline in `.planning/AGENTS.md` are the planning-local behavior deltas: keep classes distinct, no silent promotion, no exploratory-to-canon without explicit step, mark superseded relationships, prefer status notes over deletion, no unmanaged corpora ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:32)). This is the compression shape the Checkpoint 1 audit recommended — pointer plus planning-local exceptions, not a second taxonomy owner ([checkpoint-1-governance-doc-normalization-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-1-governance-doc-normalization-audit.md:137)).

### `50+` player-count residue generalization in root `AGENTS.md`

The two case-shaped lines (`Distinguish "general architectural exposure" from "large-scale player-count / massive-room research"` and `Questions about 50+ or larger player support often require...`) have been replaced with durable general rules: distinguish general architectural questions from scale-specific topology/latency/large-room questions; scope external-research-dependent lanes explicitly rather than smuggling them into generic architecture discussion ([AGENTS.md](../../AGENTS.md:91)). The learned rule survives in a form that does not depend on the specific case that produced it.

### WORKFLOW.md machinery-state removal

The pinned config value (`git.branching_strategy` set to `none`) has been replaced with a durable posture — treat GSD config as harness-state, verify when it matters, enforce branch discipline by convention until automation changes intentionally ([WORKFLOW.md](../../WORKFLOW.md:140)). The durable rule about updating both WORKFLOW.md and AGENTS.md when branch automation is introduced is preserved.

The specific hook pilot inventory (SessionStart + PreToolUse hooks listed by event name) has been replaced with a pointer to `.codex/hooks.json` as harness-state ([WORKFLOW.md](../../WORKFLOW.md:148)). All durable hook posture rules remain: hooks are not the primary enforcement layer, use the new config path, keep them short and deterministic, do not use them as a substitute for protection/CI/doc boundaries, remove quickly when noisy ([WORKFLOW.md](../../WORKFLOW.md:147)).

### Anti-pass/fail, non-foreclosure, and future-flexibility doctrine

All three are intact. Root `AGENTS.md` still carries the anti-thin-closure rule and the warning against umbrella-term collapse and silent winner-selection between live branches ([AGENTS.md](../../AGENTS.md:49), [AGENTS.md](../../AGENTS.md:89)). `.planning/AGENTS.md` still carries the future-flexibility statusing section requiring at least five distinct categories, the canon-and-roadmap response rules requiring explicit uplift proposals, and the reject-premature-closure doctrine ([.planning/AGENTS.md](../../.planning/AGENTS.md:84), [.planning/AGENTS.md](../../.planning/AGENTS.md:98)). None of this was trimmed.

## Minor Observation (Non-Blocking)

**Styling variance in the preference statement.** Root `AGENTS.md` writes the preference line as `[type:support:basis]` (descriptive labels) while `.planning/AGENTS.md` writes `[t:s:b]` (compact aliases). Both reminder blocks define the same codes; both point to `.planning/CLAIM-TYPES.md` for detail. An agent reading both files will see slightly different notation in the preference line but the same operative rule. This is a trivial stylistic inconsistency, not a material gap, and does not warrant a revision pass.

## Gap Classification

- Checkpoint 2 patch cross-vendor reread result:
  `accept`

No material gap found. The minor observation is below the revision threshold.

## Verdict

- status:
  `ready-to-carry-forward`
- explanation:
  The patch executes all five normalization units the Checkpoint 1 audit identified: claim-typing owner consolidation, dated-reference removal, checkpoint/delegation duplicate removal, root residue generalization, and WORKFLOW.md machinery-current split. All four patched files are now leaner, clearer, and more generally applicable than at baseline. No load-bearing distinction from `05-gap-closure` was erased. The machinery-owned follow-through items (branch/worktree machinery, template/routing surfaces, verify-entrypoint, non-phase external-reread protocol) remain correctly open for Checkpoint 3 rather than falsely closed here. Cross-vendor independence has been satisfied.

## Required Next Action

- exact next step:
  Commit the current patch as a distinct Checkpoint 2 closure commit. Advance checkpoint status to closed. Proceed to Checkpoint 3 (Workflow / Harness Scope Audit).
- owner / lane:
  readiness/orchestrator lane
- commit implication:
  `checkpoint now`

## Independence Note

- Does this review satisfy the checkpoint's independent-review requirement?
  Yes. Checkpoint 2 is a major checkpoint requiring an independent reviewer for closure. This is a cross-vendor reread from an Anthropic Claude lane, independent of the Codex/GPT internal-verification pass that produced `checkpoint-2-internal-review-r1.md`. The matrix and policy mark cross-vendor as conditionally triggered when the patch touches load-bearing `05-gap-closure` distinctions while removing specificity from standing governance docs ([CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md:62), [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml:60)). That trigger applied here and the cross-vendor pass was correctly invoked.
- Was a cross-vendor lane available?
  Yes. Claude is the current cross-vendor family per `REVIEW-POLICY.yaml` ([REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml:8)).
- If cross-vendor was available, which Claude lane was appropriate here and why?
  `claude-sonnet-4-6` is proportionate. The patch normalizes ownership and slims specificity rather than reshaping core doctrine, harness ownership, or making a high-cost go/no-go judgment. The matrix escalation criterion for `claude-opus-4.6` (patch materially changes doctrine, or feels deceptively tidy after removing a lot of specificity) does not apply: the specificity removed was machinery-current state and over-detailed duplication, not doctrine ([CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md:68)).
- If not used, why not?
  N/A — cross-vendor lane was used.
- If used, what did independence add?
  The cross-vendor pass confirmed that the checkpoint commit taxonomy content deleted from `.planning/AGENTS.md` was already present in `WORKFLOW.md` at baseline — verified directly by diffing WORKFLOW.md against its pre-patch state rather than relying on the internal reviewer's characterization. It also independently confirmed that `.planning/CLAIM-TYPES.md` is fully adequate as the detailed reference owner, with no gaps between what the AGENTS reminder blocks imply and what CLAIM-TYPES.md actually delivers. No new material findings were produced, which is itself confirmatory evidence rather than absence of effort.
