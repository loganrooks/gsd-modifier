# Checkpoint 3 Scope Audit Cross-Vendor Review (Claude Code Opus R1)

Reviewer: Claude Opus 4.6 (Claude Code, independent cross-vendor reread)
Date: 2026-04-15
Target: [AUDITS/checkpoint-3-workflow-harness-scope-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md)

Prior reviews consulted after forming independent assessment:
- [checkpoint-3-internal-review-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-3-internal-review-r1.md) (verdict: revise before close)
- [checkpoint-3-scope-audit-cross-vendor-review-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-3-scope-audit-cross-vendor-review-opus-r1.md) (verdict: closure-ready)

## Verdict

**Closure-ready after two minor repairs.** The artifact's substantive content is strong: it correctly integrates both upstream maps without reopening the split, produces an explicit and traceable Checkpoint 4 envelope, keeps Checkpoint 5 properly conditional, and does not smuggle excellence judgment into the scoping pass. Two bounded repairs are needed before closure, neither of which changes the envelope, the seam set, or the overall structure.

This verdict partially disagrees with both prior reviews. The internal review's Finding 1 (High) identifies a real process gap but misattributes it: the conflict between the scope audit and stale STATUS.md/TASKS.md entries is a readiness-package housekeeping obligation, not a content defect in the scope audit itself. The Opus R1 review's "closure-ready, no must-change items" verdict is substantively correct but overlooks a mispointed citation and does not address the branch/worktree seam routing that the internal review flagged.

## Findings

### F1. Mispointed citation on the execution-completion reversal-sensitive boundary (Must fix, Low effort)

Line 44 claims execution completion and verification closure is reversal-sensitive and cites `checkpoint-3-codex-surface-map.md:68, lines 68-70`. Those lines in the Codex map actually describe hook coverage gaps, compaction/resume continuity, and the Codex-to-GSD seam inspection obligation:

> - Inspect hook coverage gaps.
> - Inspect continuity under compaction and resume.
> - Inspect the Codex-to-GSD seam as a seam...

The Codex map does not have an explicit execution-completion reversal claim in that range. The correct Codex-side anchor for execution-completion concerns is weaker: the closest relevant Codex-map content is the general Codex-to-GSD seam obligation at line 70 and the spawn/inheritance concern at line 66. The GSD synthesis citation at `checkpoint-3-gsd-scope-synthesis.md:50-51, 87` is correctly placed.

The fix is to either (a) replace the Codex-map citation with the correct line range or (b) downgrade the Codex support code on that claim from `[o:c+r:i]` to `[o:c+r:i]` with a narrower Codex-map citation acknowledging the Codex side contributes general seam context rather than direct completion semantics. This is the same citation issue the internal review flagged (Finding 3, Low) and that the Opus R1 review did not address.

### F2. Branch/worktree boundary materialization routing is implicit rather than explicit (Must fix, Low effort)

STATUS.md:50-55 names `branch/worktree boundary materialization` as one of the machinery-shaped follow-through surfaces Checkpoint 3 must examine before closing. The scope audit routes this into a combined Checkpoint 5 item at line 91 (`Completion, verify-routing, and worktree-boundary ownership`) and the mandatory Checkpoint 4 seam check for `execution-completion plus verification or UAT closure` at line 59 partially covers related territory. But the audit never explicitly resolves the STATUS.md blocker — it neither argues that worktree-boundary materialization is subsumed by the existing seam set nor adds it as a named Checkpoint 4 seam check.

The GSD synthesis (lines 95) already positioned this as a Checkpoint 5 candidate, so the scope audit is following its resolved input. But the scope audit's job is also to close the Checkpoint 3 gate, and the gate's live blocker list (STATUS.md:50-55) names this surface. The fix is a one-sentence explicit routing note: either (a) add a sentence in the seam-checks section (line 59) noting that branch/worktree boundary materialization is traced through the execution-completion seam plus conditional Checkpoint 5 follow-through, or (b) add it as a sixth named seam check with appropriately narrow scope.

This is the same concern the internal review raised (Finding 2, Medium). The internal review was right to flag it; I disagree only about severity. The scope audit already addresses the substance — the routing exists across lines 59, 91, and the GSD synthesis — but the explicit resolution is missing.

### F3. STATUS.md and TASKS.md are stale relative to completed work (Process observation, not a scope-audit defect)

The internal review's Finding 1 (High) correctly notes that STATUS.md:39-40 and TASKS.md:11-13 still list R3.3 (deeper GSD mapping), R3.4 (GSD synthesis), and R3.5 (overall scope synthesis) as "not started" while the scope audit presents itself as the final synthesis consuming those completed artifacts. The internal review calls this a canon conflict that the scope audit should reconcile.

I disagree about attribution. The scope audit is not the right place to fix this. STATUS.md and TASKS.md are readiness-package tracking documents; they should be updated when the underlying work completes, not embedded as reconciliation prose inside the scope audit. The GSD synthesis exists, has 119 lines of substantive resolved content, and the scope audit correctly treats it as an input. The staleness is real and should be fixed alongside or immediately after closure, but it is a package-housekeeping obligation, not a scope-audit content defect.

### F4. Seam-check lane concentration could be more explicit (Can wait)

The Opus R1 review's F1 correctly notes that some mandatory seam checks have natural primary homes (compaction/resume is primarily Codex, execution-completion is primarily GSD workflow chain) but the scope audit says "across all four lanes" without lane-concentration guidance. I agree this is not a blocker — Checkpoint 4 should resolve tactical allocation when it designs its own audit passes.

### F5. Defensibility argument is institutional rather than independently substantive (Can wait)

The Opus R1 review's F4 correctly observes that the "Why this envelope is defensible" section (lines 61-66) argues conformance to the readiness plan, launch spec, and closure standard rather than independently arguing why this decomposition is right for this repo's actual quality risks. This is a legitimate observation but a fair scoping choice: the scope audit's job under the synthesis spec is to integrate upstream maps into a justified envelope under the existing plan, not to re-derive the plan.

### F6. No direct citation of the three deeper GSD sublane artifacts (Can wait)

The Opus R1 review's F5 notes that the scope audit only cites the GSD-only synthesis rather than the three deeper sublane artifacts directly, creating a two-hop citation chain. The synthesis spec (line 22-23) explicitly authorized this structure by listing the GSD synthesis as the input. Transitivity holds because the GSD synthesis's own claim markers trace back to the sublanes with line numbers. Not a problem for closure.

## What Is Already Strong

1. **Integration discipline is correct.** The artifact takes the Codex map and the resolved GSD synthesis as settled inputs and does not reopen the split. The path of inquiry (lines 12-16) makes the dependency explicit. The planning handoff (lines 102-114) locks the decision forward with a clear reopen trigger. This is the primary thing the synthesis spec requires and the primary thing this review needed to verify.

2. **The Checkpoint 4 envelope is explicit and traceable.** Four named lanes, five named seam checks, each with file-path and line-number citations to the upstream mapping artifacts. A Checkpoint 4 launcher can read lines 52-59 alone and know what to audit, what lanes to open, and what seams to trace.

3. **Checkpoint 5 is properly conditional.** Every Checkpoint 5 item (lines 87-92) uses conditional phrasing (`remains conditional`, `if later audit confirms`, `stays conditional`, `if Checkpoint 4 finds`, `should stay conditional rather than assumed`). No item presumes Checkpoint 5 will fire. The list of likely machinery buckets is specific enough to be useful and narrow enough not to pre-commit. This directly answers one of the review questions: the machinery-owned follow-through boundary is correctly conditional rather than prematurely widened.

4. **Future-flexibility categories are explicit and correctly used.** The artifact uses all five categories required by `.planning/AGENTS.md:84-94`: direct doctrine (lines 22-26), bounded-open branches (lines 28-32), preserve-only seams (lines 34-38), reversal-sensitive boundaries (lines 40-44), and inquiry debt (lines 46-50). None are collapsed into generic `open` or `deferred`.

5. **The broad-vs-narrow analysis is genuine value-add.** Lines 68-83 provide cross-stack analysis that goes beyond what either upstream map produces individually. The "broad but not load-bearing" section correctly identifies skill count, output-style surfaces, peripheral workflows, and raw file volume as non-primary. The "narrow but load-bearing" section correctly elevates config-file top matter, hooks, compaction prompts, preserve-only field seams, completion markers, and the `.md`/`.toml` agent-authority split. This analysis satisfies the launch spec's closure standard (lines 112-113) and will serve as useful audit-onboarding material.

6. **Claim markers and source basis are consistent and mostly correct.** The artifact uses the repo's claim-type scheme throughout. I spot-checked the following citations against their targets and found them correctly placed:
   - Line 22 citing PLAN.md:378-386 for the integrated envelope decision
   - Line 54 citing the Codex map and GSD synthesis for the recommended unit of analysis
   - Lines 63-66 citing the readiness plan, launch spec, and synthesis spec for defensibility
   - Line 96 citing the launch spec and plan for the GSD split obligation
   The one exception is F1 above.

7. **Clean scoping discipline throughout.** The artifact does not reach conclusions about whether harness surfaces are good enough — it consistently says "later audit should test," "Checkpoint 4 should inspect," and similar future-directed language. No excellence judgment is smuggled into the scoping pass.

## What Must Change Before Closure

1. **Fix the mispointed citation at line 44** (F1). Replace the `checkpoint-3-codex-surface-map.md:68, lines 68-70` citation with the correct Codex-map line range, or narrow the Codex support claim to reflect that the Codex side contributes general seam context rather than direct completion semantics.

2. **Add an explicit routing note for branch/worktree boundary materialization** (F2). One sentence in or near the mandatory seam checks (line 59) or the Checkpoint 5 section (line 91) that explicitly addresses the STATUS.md:50-55 blocker by stating that worktree-boundary materialization is traced through the execution-completion seam check in Checkpoint 4 and the conditional Checkpoint 5 combined item, closing the apparent gap.

Additionally, alongside or immediately after scope-audit closure:

3. **Update STATUS.md and TASKS.md** to reflect that R3.3, R3.4, and R3.5 are complete (F3). This is a readiness-package obligation, not a scope-audit revision, but it should not be deferred past the Checkpoint 3 closure commit.

## What Can Wait Until Later

1. **Seam-check lane-concentration guidance** (F4). Checkpoint 4 should resolve how to distribute seam-checking effort across lanes when it designs its own audit passes. The scope audit's "across all four lanes" phrasing is correct in intent.

2. **Independently substantive defensibility argument** (F5). Fair scoping choice for now. If a later reviewer questions the readiness plan itself, this section would need to be supplemented, but that is not a Checkpoint 3 obligation.

3. **Sublane direct citations** (F6). The two-hop citation chain is authorized by the synthesis spec and the GSD synthesis has strong traceability to the sublanes. No action needed.

4. **GSD-split-resolution section overlap** (Opus R1 F3). The repetition serves onboarding and is not harmful. Could be trimmed later for length discipline.

5. **Explicit value-add statement** (Opus R1 F6). A reader can reconstruct what the scope audit adds beyond combining the maps, but the artifact does not call this out. Low priority.
