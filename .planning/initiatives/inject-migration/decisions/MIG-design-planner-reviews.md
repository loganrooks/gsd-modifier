# Migration Design: planner-reviews.md

Date: 2026-05-16
Phase: 4 (`04-first-wave-references`)
Slice: 5 (`design migration of references/planner-reviews.md`)
Status: design-only; no manifest, overlay, runtime, bootstrap, or contract behavior changed

## Decision

Do not treat `get-shit-done/references/planner-reviews.md` as a routine apply-ready Phase 4 candidate yet.

The modifier delta has two parts:

1. Steps 1-3 can be represented cleanly with three existing `block_replace` operations.
2. Step 4 changes the final fenced return-format example at end-of-file. With the current v4 operation catalog, that edit cannot be both full-fidelity and marker-clean: replacing the final fenced block needs an end anchor after the region, but the file ends immediately after the closing fence. The mechanically valid fallback would put `<!-- GSD_MODIFIER:* -->` markers inside the copyable return-format example.

Recommendation: before Slice 6 applies this carrier, run a reviewer-mediated decision on whether to:

1. Accept marker lines inside the final fenced return-format example as a bounded tradeoff.
2. Drop the Step 4 return-format delta as covered by the strengthened Steps 1-3 prose.
3. Pause for an ADR amendment adding a clean EOF-capable operation kind.

## Current State

Upstream source read from:

```text
/home/rookslog/workspace/projects/get-shit-done-upstream/get-shit-done/references/planner-reviews.md
```

Upstream checkout: `a7f0af2c`.

Upstream relevant ranges:

- `:7-12` - Step 1 review parsing guidance.
- `:13-18` - Step 2 feedback categorization.
- `:19-23` - Step 3 planning-with-review-context guidance.
- `:25-39` - Step 4 fenced return-format example at end-of-file.

Current modifier overwrite source:

```text
tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md
```

Modifier relevant ranges:

- `:7-21` - Step 1 adds Review Consumer Contract and Review Synthesis parsing.
- `:23-39` - Step 2 adds must/should/consider/rebuttal buckets and consensus caution.
- `:41-48` - Step 3 adds rebuttal, lone high-signal, unchanged-plan, and already-covered traceability rules.
- `:50-69` - Step 4 return-format example adds Source columns and a Rejected table.

Current manifest entry:

```json
{
  "capability_id": "get-shit-done/references/planner-reviews.md",
  "parity_tier": "core_required",
  "materializers": {
    "codex": {
      "mode": "overwrite",
      "target": "get-shit-done/references/planner-reviews.md",
      "source": "tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md"
    },
    "claude": {
      "mode": "overwrite",
      "target": "get-shit-done/references/planner-reviews.md",
      "source": "tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md"
    }
  }
}
```

Precise diff from upstream to current modifier source:

```diff
@@ -7,20 +7,45 @@
 ### Step 1: Load REVIEWS.md
 Read the reviews file from `<files_to_read>`. Parse:
 - Per-reviewer feedback (strengths, concerns, suggestions)
-- Consensus Summary (agreed concerns = highest priority to address)
-- Divergent Views (investigate, make a judgment call)
+- Review Consumer Contract:
+  - Must Address In Replan
+  - Explicit Rebuttal Required If Not Accepted
+  - Safe To Defer
+- Review Synthesis:
+  - Agreed Concerns
+  - Lone High-Signal Concerns
+  - Merely Adequate Areas
+  - Later Audit Risks
+  - Divergent Views
+- Treat synthesis as guidance, not as permission to ignore a strong individual criticism.
+- If the consumer-contract section is missing or incomplete, derive the same buckets from the individual reviews and synthesis instead of downgrading the review pass.
 
 ### Step 2: Categorize Feedback
 Group review feedback into:
-- **Must address**: HIGH severity consensus concerns
-- **Should address**: MEDIUM severity concerns from 2+ reviewers
-- **Consider**: Individual reviewer suggestions, LOW severity items
+- **Must address**:
+  - Every item in `Must Address In Replan`
+  - HIGH severity agreed concerns
+  - Any lone high-signal criticism that is well-justified and would create likely later-audit failure if ignored
+  - Later audit risks or merely-adequate areas that would leave the plan weak, misleadingly closure-ready, or brittle against the repo quality bar if left untouched
+- **Should address**:
+  - MEDIUM severity agreed concerns
+  - Merely adequate areas that leave the plan technically passable but weak for the repo's quality bar, when they are not already in Must address
+- **Consider**:
+  - Items listed in `Safe To Defer`
+  - Individual reviewer suggestions that are useful but not load-bearing
+  - LOW severity items
+- **Explicit rebuttal required**:
+  - Every item in `Explicit Rebuttal Required If Not Accepted`
+- Consensus raises confidence, but lack of consensus does not automatically downgrade a criticism.
 
 ### Step 3: Plan Fresh with Review Context
 Create new plans following the standard planning process, but with review feedback as additional constraints:
-- Each HIGH severity consensus concern MUST have a task that addresses it
-- MEDIUM concerns should be addressed where feasible without over-engineering
+- Each must-address concern MUST have a task that addresses it or an explicit written rebuttal for why the criticism is not accepted
+- MEDIUM concerns and merely-adequate areas should be addressed where feasible without over-engineering
 - Note in task actions: "Addresses review concern: {concern}" for traceability
+- If you reject a lone high-signal criticism, explain why the criticism is not persuasive; do not dismiss it solely because only one reviewer raised it
+- Do not leave the existing plans materially unchanged unless you can point to the exact existing plan/task that already satisfies each must-address concern
+- If a concern is already covered, say exactly which plan/task covers it instead of silently assuming coverage
 
 ### Step 4: Return
 Use standard PLANNING COMPLETE return format, adding a reviews section:
@@ -28,12 +53,17 @@
 ```markdown
 ### Review Feedback Addressed
 
-| Concern | Severity | How Addressed |
-|---------|----------|---------------|
-| {concern} | HIGH | Plan {N}, Task {M}: {how} |
+| Concern | Source | Severity | How Addressed |
+|---------|--------|----------|---------------|
+| {concern} | {reviewer or synthesis section} | HIGH | Plan {N}, Task {M}: {how} |
 
 ### Review Feedback Deferred
-| Concern | Reason |
-|---------|--------|
-| {concern} | {why — out of scope, disagree, etc.} |
+| Concern | Source | Reason |
+|---------|--------|--------|
+| {concern} | {reviewer or synthesis section} | {why — safe to defer or intentionally sequenced out} |
+
+### Review Feedback Rejected
+| Concern | Source | Reason |
+|---------|--------|--------|
+| {concern} | {reviewer or synthesis section} | {why the criticism was not accepted on the merits} |
 ```
```

## Proposed Manifest Entry (Candidate, Not Apply-Ready)

The marker-clean portion of the migration can be expressed with three `block_replace` operations. The final Step 4 fenced return-format delta is intentionally omitted from this candidate because preserving it with today's v4 catalog would place marker lines inside the fenced example.

```json
"get-shit-done/references/planner-reviews.md": {
  "capability_id": "get-shit-done/references/planner-reviews.md",
  "parity_tier": "core_required",
  "parity_intent": "outcome_aligned",
  "materializers": {
    "codex": {
      "mode": "inject",
      "target": "get-shit-done/references/planner-reviews.md",
      "operations": [
        {
          "kind": "block_replace",
          "start_anchor": "### Step 1: Load REVIEWS.md\n",
          "end_anchor": "### Step 2: Categorize Feedback\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planner-reviews/step-1-load-reviews-body.md",
          "marker_key": "GSD_MODIFIER:references-planner-reviews:load-reviews"
        },
        {
          "kind": "block_replace",
          "start_anchor": "### Step 2: Categorize Feedback\n",
          "end_anchor": "### Step 3: Plan Fresh with Review Context\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planner-reviews/step-2-categorize-feedback-body.md",
          "marker_key": "GSD_MODIFIER:references-planner-reviews:categorize-feedback"
        },
        {
          "kind": "block_replace",
          "start_anchor": "### Step 3: Plan Fresh with Review Context\n",
          "end_anchor": "### Step 4: Return\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planner-reviews/step-3-plan-fresh-body.md",
          "marker_key": "GSD_MODIFIER:references-planner-reviews:plan-fresh"
        }
      ]
    },
    "claude": {
      "mode": "inject",
      "target": "get-shit-done/references/planner-reviews.md",
      "operations": [
        {
          "kind": "block_replace",
          "start_anchor": "### Step 1: Load REVIEWS.md\n",
          "end_anchor": "### Step 2: Categorize Feedback\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planner-reviews/step-1-load-reviews-body.md",
          "marker_key": "GSD_MODIFIER:references-planner-reviews:load-reviews"
        },
        {
          "kind": "block_replace",
          "start_anchor": "### Step 2: Categorize Feedback\n",
          "end_anchor": "### Step 3: Plan Fresh with Review Context\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planner-reviews/step-2-categorize-feedback-body.md",
          "marker_key": "GSD_MODIFIER:references-planner-reviews:categorize-feedback"
        },
        {
          "kind": "block_replace",
          "start_anchor": "### Step 3: Plan Fresh with Review Context\n",
          "end_anchor": "### Step 4: Return\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planner-reviews/step-3-plan-fresh-body.md",
          "marker_key": "GSD_MODIFIER:references-planner-reviews:plan-fresh"
        }
      ]
    }
  }
}
```

## Modifier Source Files

Candidate files:

- `harness_modifier/overlay/inject-sources/get-shit-done/references/planner-reviews/step-1-load-reviews-body.md`
  - Body between `### Step 1: Load REVIEWS.md` and `### Step 2: Categorize Feedback`, matching current modifier lines `8-21`.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/planner-reviews/step-2-categorize-feedback-body.md`
  - Body between `### Step 2: Categorize Feedback` and `### Step 3: Plan Fresh with Review Context`, matching current modifier lines `24-39`.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/planner-reviews/step-3-plan-fresh-body.md`
  - Body between `### Step 3: Plan Fresh with Review Context` and `### Step 4: Return`, matching current modifier lines `42-48`.

No candidate source file is listed for Step 4 because the file ends immediately after the fenced return-format example. A full-fidelity edit there needs a clean EOF-capable operation or an explicit decision to tolerate marker lines inside the fenced example.

## Expected Materialized Content Sketch

With the three-operation candidate, the materialized file would:

- Preserve upstream heading, introduction, and Step 4 return-format example outside marker regions.
- Replace Step 1's review parsing body with the modifier version carrying Review Consumer Contract and Review Synthesis parsing.
- Replace Step 2's categorization body with the modifier version carrying must/should/consider/explicit-rebuttal buckets.
- Replace Step 3's planning guidance body with the modifier version carrying rebuttal, lone-high-signal, unchanged-plan, and already-covered traceability rules.
- Wrap each replaced Step 1-3 body in its own `GSD_MODIFIER` marker region.
- Leave the final Step 4 fenced return-format example in upstream form, missing the Source columns and Rejected table that the current modifier overlay adds.

Therefore the three-operation candidate is marker-clean but not full-fidelity.

The full-fidelity fallback would replace the final fenced example, but the only mechanically valid form with today's catalog would put marker comments inside the code block. This design does not recommend that without reviewer approval.

## Preflight

Pure-function preflight against the real upstream content and the three candidate operation bodies:

```text
records=3 statuses=['applied', 'applied', 'applied']
verify_passed=True statuses=['verified', 'verified', 'verified'] extraction_error=None
step4_delta_remaining=True
```

## Verification Approach

Slice 6 should not apply this carrier until the open question below is resolved.

If a reviewer approves the three-operation marker-clean-but-not-full-fidelity candidate, Slice 6 should run:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify .
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --source-only --strict
python3 -m unittest discover -s tooling/codex/tests -p 'test_inject*.py'
python3 -m unittest discover -s tooling/codex/tests
```

If a reviewer instead approves a full-fidelity marker-in-fence operation, Slice 6 should also inspect the materialized fenced return-format example before treating the migration as acceptable.

## Rollback Plan

If Slice 6 proceeds and fails before commit:

1. Restore `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`.
2. Restore `tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md`.
3. Remove the newly created `harness_modifier/overlay/inject-sources/get-shit-done/references/planner-reviews/` directory.
4. Rerun the failed Slice 6 gates.

If Slice 6 fails after commit, revert the single Slice 6 commit. No later Phase 4 carrier should depend on this migration until it has materialized cleanly under both runtimes.

## Open Questions

Blocking for Slice 6:

1. Should the final EOF fenced return-format example be allowed to contain GSD marker comments inside the code block?
2. If not, should the Step 4 return-format delta be dropped despite losing Source-column and Rejected-table output guidance, or should Phase 4 pause for an ADR amendment adding a clean EOF block-replacement operation?

Recommended next action: before applying this carrier, invoke a Plan/slice-ambiguity reviewer. This is the second Phase 4 reference to surface the same EOF fenced-block limitation, so the reviewer should evaluate whether the pattern now warrants an ADR amendment rather than another per-carrier omission.
