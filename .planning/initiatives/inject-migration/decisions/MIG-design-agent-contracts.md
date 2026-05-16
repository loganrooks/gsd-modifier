# Migration Design: agent-contracts.md

Date: 2026-05-16
Phase: 4 (`04-first-wave-references`)
Slice: 3 (`design migration of references/agent-contracts.md`)
Status: design-only; no manifest, overlay, runtime, bootstrap, or contract behavior changed

## Decision

`get-shit-done/references/agent-contracts.md` is an apply-ready Phase 4 candidate.

The current modifier delta can be represented with three existing `block_replace` operations:

1. Replace the body between `## Marker Rules` and `## Key Handoff Contracts`.
2. Replace the body between `## Key Handoff Contracts` and `## Workflow Regex Patterns`.
3. Insert the clean/debt completion note after the existing `## PLAN COMPLETE` note using the degenerate `block_replace` pattern where `start_anchor == end_anchor`.

No new operation kind is needed, and there is no EOF fenced-code-block ambiguity like the one surfaced by `verification-overrides.md`.

## Current State

Upstream source read from:

```text
/home/rookslog/workspace/projects/get-shit-done-upstream/get-shit-done/references/agent-contracts.md
```

Upstream checkout: `a7f0af2c`.

Upstream relevant ranges:

- `:36-43` - `Marker Rules` body.
- `:44-64` - `Key Handoff Contracts` body.
- `:65-79` - `Workflow Regex Patterns` body and final `## PLAN COMPLETE` note.

Current modifier overwrite source:

```text
tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md
```

Modifier relevant ranges:

- `:36-45` - marker rules add research completion/blocking and debt-aware plan completion semantics.
- `:47-91` - handoff contracts add Researcher -> Planner, future preservation, execution debt, and verifier routing metadata.
- `:93-109` - workflow regex note adds clean/debt completion caveat.

Current manifest entry:

```json
{
  "capability_id": "get-shit-done/references/agent-contracts.md",
  "parity_tier": "core_required",
  "materializers": {
    "codex": {
      "mode": "overwrite",
      "target": "get-shit-done/references/agent-contracts.md",
      "source": "tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md"
    },
    "claude": {
      "mode": "overwrite",
      "target": "get-shit-done/references/agent-contracts.md",
      "source": "tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md"
    }
  }
}
```

Precise diff from upstream to current modifier source:

```diff
@@ -40,14 +40,29 @@
 3. **Non-standard markers** (e.g., `## PARTIAL`, `## ESCALATE`) in audit agents indicate partial results requiring orchestrator judgment
 4. **Agents without markers** either write artifacts directly to disk or return structured data (JSON/sections) that the caller parses
 5. Markers must appear as H2 headings (`## `) at the start of a line in the agent's final output
+6. `## RESEARCH COMPLETE` is compatible with unresolved uncertainty only when the agent also provides explicit disposition accounting for what was resolved, what planning must carry forward, what remains intentionally open, and what is still inconclusive
+7. `## RESEARCH BLOCKED` is reserved for cases where no reviewable research artifact can yet guide planning
+8. `## PLAN COMPLETE` means execution finished and a SUMMARY exists; it does **not** mean the phase reached clean completion. Routing must read `completion_mode` / debt metadata from SUMMARY and VERIFICATION artifacts rather than inferring clean closure from the marker alone.

 ## Key Handoff Contracts

+### Researcher -> Planner (via RESEARCH.md)
+
+| Field / Section | Required | Description |
+|-----------------|----------|-------------|
+| `## User Constraints` | Yes when CONTEXT.md exists | Locked decisions, discretion areas, and deferred ideas copied from CONTEXT.md |
+| `## Research Disposition` | Yes when anything remains open, escalated, intentionally preserved, or inconclusive | Names what planning may treat as settled versus what it must still carry forward |
+| `## Standard Stack` | Yes | Libraries/tools planning should prefer |
+| `## Architecture Patterns` | Yes | Structural guidance and anti-patterns |
+| `## Common Pitfalls` | Yes | Things verification and task design should guard against |
+| `## Sources` | Yes | Confidence-bearing provenance for research claims |
+
 ### Planner -> Executor (via PLAN.md)

 | Field | Required | Description |
 |-------|----------|-------------|
 | Frontmatter | Yes | phase, plan, type, wave, depends_on, files_modified, autonomous, requirements |
+| `future_preservation` | Yes when CONTEXT future-awareness is non-empty | Preserved seams, explicit non-decisions, posture assumptions, and strengthening routes |
 | `<objective>` | Yes | What the plan achieves |
 | `<tasks>` | Yes | Ordered task list with type, files, action, verify, acceptance_criteria |
 | `<verification>` | Yes | Overall verification steps |
@@ -58,10 +73,23 @@
 | Field | Required | Description |
 |-------|----------|-------------|
 | Frontmatter | Yes | phase, plan, subsystem, tags, key-files, metrics |
+| `completion_mode` | Yes | `clean_execution` or `debt_carrying_execution` so downstream consumers know whether execution itself carried known debt before verification |
+| `completion_debt` | Yes when `completion_mode=debt_carrying_execution` | Structured reasons carried out of execution (auth gates, intentional stubs, failed self-check, other known debt) |
 | Commits table | Yes | Per-task commit hashes and descriptions |
 | Deviations section | Yes | Auto-fixed issues or "None" |
 | Self-Check | Yes | PASSED or FAILED with details |

+### Verifier -> Routing (via VERIFICATION.md)
+
+| Field | Required | Description |
+|-------|----------|-------------|
+| `status` | Yes | `passed`, `gaps_found`, or `human_needed` |
+| `completion_mode` | Yes | `clean_completion` or `debt_carrying_completion`; distinguishes clean closure from accepted or unresolved carried debt |
+| `debt_bearing` | Yes | Boolean mirror of `completion_mode` for consumers that only need a quick debt flag |
+| `overrides_applied` | Yes | Count of accepted verification overrides contributing to the final result |
+| `future_preservation_review` | Yes when any source PLAN carries `future_preservation` | Structured verifier review of whether preserved seams, explicit non-decisions, posture assumptions, and strengthening routes were carried, thinned, or still need human judgment |
+| `gaps` / `human_verification` | Yes when applicable | Structured downstream debt details for routing and planning |
+
 ## Workflow Regex Patterns

 Workflows match these markers to detect agent completion:
@@ -77,3 +105,5 @@
 - `## Self-Check: FAILED` (summary self-check)

 > **NOTE:** `## PLAN COMPLETE` is the gsd-executor's completion marker but execute-phase.md does not regex-match it. Instead, it detects executor completion via spot-checks (SUMMARY.md existence, git commit state). This is intentional behavior, not a mismatch.
+>
+> **NOTE:** Clean-versus-debt-carrying completion must be read from `completion_mode` and verification artifacts, not from the presence of `## PLAN COMPLETE` or a SUMMARY file alone.
```

## Proposed Manifest Entry

```json
"get-shit-done/references/agent-contracts.md": {
  "capability_id": "get-shit-done/references/agent-contracts.md",
  "parity_tier": "core_required",
  "parity_intent": "outcome_aligned",
  "materializers": {
    "codex": {
      "mode": "inject",
      "target": "get-shit-done/references/agent-contracts.md",
      "operations": [
        {
          "kind": "block_replace",
          "start_anchor": "## Marker Rules\n",
          "end_anchor": "## Key Handoff Contracts\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/agent-contracts/marker-rules-body.md",
          "marker_key": "GSD_MODIFIER:references-agent-contracts:marker-rules"
        },
        {
          "kind": "block_replace",
          "start_anchor": "## Key Handoff Contracts\n",
          "end_anchor": "## Workflow Regex Patterns\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/agent-contracts/handoff-contracts-body.md",
          "marker_key": "GSD_MODIFIER:references-agent-contracts:handoff-contracts"
        },
        {
          "kind": "block_replace",
          "start_anchor": "> **NOTE:** `## PLAN COMPLETE` is the gsd-executor's completion marker but execute-phase.md does not regex-match it. Instead, it detects executor completion via spot-checks (SUMMARY.md existence, git commit state). This is intentional behavior, not a mismatch.\n",
          "end_anchor": "> **NOTE:** `## PLAN COMPLETE` is the gsd-executor's completion marker but execute-phase.md does not regex-match it. Instead, it detects executor completion via spot-checks (SUMMARY.md existence, git commit state). This is intentional behavior, not a mismatch.\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/agent-contracts/clean-completion-note.md",
          "marker_key": "GSD_MODIFIER:references-agent-contracts:clean-completion-note"
        }
      ]
    },
    "claude": {
      "mode": "inject",
      "target": "get-shit-done/references/agent-contracts.md",
      "operations": [
        {
          "kind": "block_replace",
          "start_anchor": "## Marker Rules\n",
          "end_anchor": "## Key Handoff Contracts\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/agent-contracts/marker-rules-body.md",
          "marker_key": "GSD_MODIFIER:references-agent-contracts:marker-rules"
        },
        {
          "kind": "block_replace",
          "start_anchor": "## Key Handoff Contracts\n",
          "end_anchor": "## Workflow Regex Patterns\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/agent-contracts/handoff-contracts-body.md",
          "marker_key": "GSD_MODIFIER:references-agent-contracts:handoff-contracts"
        },
        {
          "kind": "block_replace",
          "start_anchor": "> **NOTE:** `## PLAN COMPLETE` is the gsd-executor's completion marker but execute-phase.md does not regex-match it. Instead, it detects executor completion via spot-checks (SUMMARY.md existence, git commit state). This is intentional behavior, not a mismatch.\n",
          "end_anchor": "> **NOTE:** `## PLAN COMPLETE` is the gsd-executor's completion marker but execute-phase.md does not regex-match it. Instead, it detects executor completion via spot-checks (SUMMARY.md existence, git commit state). This is intentional behavior, not a mismatch.\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/agent-contracts/clean-completion-note.md",
          "marker_key": "GSD_MODIFIER:references-agent-contracts:clean-completion-note"
        }
      ]
    }
  }
}
```

## Modifier Source Files

Candidate files:

- `harness_modifier/overlay/inject-sources/get-shit-done/references/agent-contracts/marker-rules-body.md`
  - Body between `## Marker Rules` and `## Key Handoff Contracts`, matching current modifier lines `38-45`.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/agent-contracts/handoff-contracts-body.md`
  - Body between `## Key Handoff Contracts` and `## Workflow Regex Patterns`, matching current modifier lines `49-91`.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/agent-contracts/clean-completion-note.md`
  - Added clean/debt completion blockquote continuation, matching current modifier lines `108-109`.

## Expected Materialized Content Sketch

The materialized file should:

- Preserve upstream agent registry and workflow regex bullets.
- Replace the marker-rules section body with the modifier version carrying research disposition and debt-aware `PLAN COMPLETE` semantics.
- Replace the key handoff contracts body with the modifier version carrying Researcher -> Planner, future preservation, execution-debt, and verifier-routing metadata.
- Insert the clean/debt completion note after the existing `## PLAN COMPLETE` workflow-regex note.
- Add three marker regions around the replaced/inserted modifier-owned content.

Because the third operation uses `start_anchor == end_anchor`, it inserts after a real line near EOF without requiring a new EOF operation and without putting markers inside a fenced code block.

## Preflight

A local pure-function preflight applied the three proposed operations against the upstream file with `apply_inject_operations` and then ran `verify_inject_state` against the generated content:

```text
records [('block_replace', 'GSD_MODIFIER:references-agent-contracts:marker-rules', 'applied'), ('block_replace', 'GSD_MODIFIER:references-agent-contracts:handoff-contracts', 'applied'), ('block_replace', 'GSD_MODIFIER:references-agent-contracts:clean-completion-note', 'applied')]
verify_passed True extraction_error None
verification_statuses [('GSD_MODIFIER:references-agent-contracts:marker-rules', 'verified'), ('GSD_MODIFIER:references-agent-contracts:handoff-contracts', 'verified'), ('GSD_MODIFIER:references-agent-contracts:clean-completion-note', 'verified')]
```

## Verification Approach

Slice 4 should run:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify .
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --source-only --strict
python3 -m unittest discover -s tooling/codex/tests -p 'test_inject*.py'
python3 -m unittest discover -s tooling/codex/tests
```

The full discover gate is expected to continue hitting the known non-carrier baseline until OOS #5 is addressed; if its failure shape changes or names `agent-contracts.md`, route through `gsd-debugger`.

## Rollback Plan

If Slice 4 proceeds and fails before commit:

1. Restore `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`.
2. Restore `tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md`.
3. Remove the newly created `harness_modifier/overlay/inject-sources/get-shit-done/references/agent-contracts/` directory.
4. Rerun the failed Slice 4 gates.

If Slice 4 fails after commit, revert the single Slice 4 commit before migrating later Phase 4 carriers.

## Open Questions

None blocking.

One implementation detail to watch in Slice 4: the final-note operation's anchor is a long blockquote line. If upstream changes that sentence before apply, the operation should fail loudly under source-only validation/materialization rather than falling back to an approximate anchor.
