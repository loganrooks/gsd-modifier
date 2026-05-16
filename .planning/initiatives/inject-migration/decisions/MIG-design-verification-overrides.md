# Migration Design: verification-overrides.md

Date: 2026-05-16
Phase: 4 (`04-first-wave-references`)
Slice: 1 (`design migration of references/verification-overrides.md`)
Status: design-only; no manifest, overlay, runtime, bootstrap, or contract behavior changed

## Decision

Do not treat `get-shit-done/references/verification-overrides.md` as a routine Phase 4 apply candidate yet.

Most of the modifier delta can be expressed with marker-clean `block_replace` operations over existing tagged sections. One current modifier delta, however, edits the final fenced `Example VERIFICATION.md` block at end-of-file. With the v4 operation catalog, that edit cannot be full-fidelity and marker-clean at the same time: a precise `block_replace` needs an end anchor after the replaced region, but the final code fence has no following anchor. The mechanically valid fallback would put `<!-- GSD_MODIFIER:* -->` markers inside the example code block, which risks teaching agents to copy marker lines into generated `VERIFICATION.md` examples.

Recommendation: before Slice 2 applies this carrier, run a reviewer-mediated decision on whether to:

1. Accept marker lines inside the final fenced example as a bounded tradeoff.
2. Drop the final example-field delta as redundant because the first YAML example and verifier-behavior prose already carry the debt-bearing contract.
3. Add or amend an operation kind for clean end-of-file block replacement, then migrate this carrier.

## Current State

Upstream source read from:

```text
/home/rookslog/workspace/projects/get-shit-done-upstream/get-shit-done/references/verification-overrides.md
```

Upstream checkout: `a7f0af2c`.

Upstream relevant ranges:

- `:1-39` — `Override Format` tagged block and first YAML example.
- `:89-133` — `Verifier Behavior with Overrides` tagged block.
- `:135-171` — `Creating Overrides` tagged block.
- `:173-202` — `Override Lifecycle` tagged block.
- `:204-227` — final `Example VERIFICATION.md` fenced block.

Current modifier overwrite source:

```text
tooling/portable-gsd/overlay/get-shit-done/references/verification-overrides.md
```

Modifier relevant ranges:

- `:1-41` — first YAML example adds `completion_mode: debt_carrying_completion` and `debt_bearing: true`.
- `:91-136` — verifier behavior adds the rule that overrides imply debt-bearing completion metadata.
- `:138-174` — command examples use `$gsd-verify-work` instead of `/gsd:verify-work`.
- `:176-205` — milestone audit example uses `$gsd-audit-milestone` instead of `/gsd:audit-milestone`.
- `:207-232` — final example adds `completion_mode` and `debt_bearing` fields.

Current manifest entry:

```json
{
  "capability_id": "get-shit-done/references/verification-overrides.md",
  "parity_tier": "core_required",
  "materializers": {
    "codex": {
      "mode": "overwrite",
      "target": "get-shit-done/references/verification-overrides.md",
      "source": "tooling/portable-gsd/overlay/get-shit-done/references/verification-overrides.md"
    },
    "claude": {
      "mode": "overwrite",
      "target": "get-shit-done/references/verification-overrides.md",
      "source": "tooling/portable-gsd/overlay/get-shit-done/references/verification-overrides.md"
    }
  }
}
```

Precise diff from upstream to current modifier source:

```diff
@@ -13,6 +13,8 @@
 phase: 03-authentication
 verified: 2026-04-05T12:00:00Z
 status: passed
+completion_mode: debt_carrying_completion
+debt_bearing: true
 score: 5/5
 overrides_applied: 2
 overrides:
@@ -120,6 +122,7 @@
 - `PASSED (override)` items count toward the passing score, not the failing score
 - A phase with all items either VERIFIED or PASSED (override) can have status `passed`
 - Overrides do NOT suppress `human_needed` items — those still require human testing
+- Overrides do NOT imply clean completion. If any override is applied, VERIFICATION.md must set `completion_mode: debt_carrying_completion` and `debt_bearing: true` even when `status: passed`.

 ### Frontmatter Score

@@ -163,10 +166,10 @@

 Overrides can also be managed through the verification workflow:

-1. Run `/gsd:verify-work` — verification finds gaps
+1. Run `$gsd-verify-work` — verification finds gaps
 2. Review gaps — determine which are intentional deviations
 3. Add override entries to VERIFICATION.md frontmatter
-4. Re-run `/gsd:verify-work` — overrides are applied, remaining gaps shown
+4. Re-run `$gsd-verify-work` — overrides are applied, remaining gaps shown

 </creating_overrides>

@@ -183,7 +186,7 @@

 ### At Milestone Completion

-During `/gsd:audit-milestone`, overrides are surfaced in the audit report:
+During `$gsd-audit-milestone`, overrides are surfaced in the audit report:

 ```
 ### Verification Overrides ({count} across {phase_count} phases)
@@ -208,6 +211,8 @@
 phase: 03-api-layer
 verified: 2026-04-05T12:00:00Z
 status: passed
+completion_mode: debt_carrying_completion
+debt_bearing: true
 score: 3/3
 overrides_applied: 1
 overrides:
```

## Proposed Manifest Entry (Candidate, Not Apply-Ready)

The marker-clean portion of the migration can be expressed with four section-sized `block_replace` operations. The final example delta is intentionally omitted from this candidate because preserving it with today's v4 catalog would place marker lines inside the fenced example.

```json
"get-shit-done/references/verification-overrides.md": {
  "capability_id": "get-shit-done/references/verification-overrides.md",
  "parity_tier": "core_required",
  "parity_intent": "outcome_aligned",
  "materializers": {
    "codex": {
      "mode": "inject",
      "target": "get-shit-done/references/verification-overrides.md",
      "operations": [
        {
          "kind": "block_replace",
          "start_anchor": "<override_format>\n",
          "end_anchor": "</override_format>\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/override-format-body.md",
          "marker_key": "GSD_MODIFIER:references-verification-overrides:override-format-body"
        },
        {
          "kind": "block_replace",
          "start_anchor": "<verifier_behavior>\n",
          "end_anchor": "</verifier_behavior>\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/verifier-behavior-body.md",
          "marker_key": "GSD_MODIFIER:references-verification-overrides:verifier-behavior-body"
        },
        {
          "kind": "block_replace",
          "start_anchor": "<creating_overrides>\n",
          "end_anchor": "</creating_overrides>\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/creating-overrides-body.md",
          "marker_key": "GSD_MODIFIER:references-verification-overrides:creating-overrides-body"
        },
        {
          "kind": "block_replace",
          "start_anchor": "<override_lifecycle>\n",
          "end_anchor": "</override_lifecycle>\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/override-lifecycle-body.md",
          "marker_key": "GSD_MODIFIER:references-verification-overrides:override-lifecycle-body"
        }
      ]
    },
    "claude": {
      "mode": "inject",
      "target": "get-shit-done/references/verification-overrides.md",
      "operations": [
        {
          "kind": "block_replace",
          "start_anchor": "<override_format>\n",
          "end_anchor": "</override_format>\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/override-format-body.md",
          "marker_key": "GSD_MODIFIER:references-verification-overrides:override-format-body"
        },
        {
          "kind": "block_replace",
          "start_anchor": "<verifier_behavior>\n",
          "end_anchor": "</verifier_behavior>\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/verifier-behavior-body.md",
          "marker_key": "GSD_MODIFIER:references-verification-overrides:verifier-behavior-body"
        },
        {
          "kind": "block_replace",
          "start_anchor": "<creating_overrides>\n",
          "end_anchor": "</creating_overrides>\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/creating-overrides-body.md",
          "marker_key": "GSD_MODIFIER:references-verification-overrides:creating-overrides-body"
        },
        {
          "kind": "block_replace",
          "start_anchor": "<override_lifecycle>\n",
          "end_anchor": "</override_lifecycle>\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/override-lifecycle-body.md",
          "marker_key": "GSD_MODIFIER:references-verification-overrides:override-lifecycle-body"
        }
      ]
    }
  }
}
```

## Modifier Source Files

Candidate files:

- `harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/override-format-body.md`
  - Body between `<override_format>` and `</override_format>`, matching current modifier lines `6-40`.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/verifier-behavior-body.md`
  - Body between `<verifier_behavior>` and `</verifier_behavior>`, matching current modifier lines `92-135`.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/creating-overrides-body.md`
  - Body between `<creating_overrides>` and `</creating_overrides>`, matching current modifier lines `139-173`.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/override-lifecycle-body.md`
  - Body between `<override_lifecycle>` and `</override_lifecycle>`, matching current modifier lines `177-204`.

No candidate source file is listed for the final `Example VERIFICATION.md` block because the file ends immediately after the fenced example. A full-fidelity edit there needs a new clean EOF-capable operation or an explicit decision to tolerate marker lines inside the fenced example.

## Expected Materialized Content Sketch

With the four-operation candidate, the materialized file would:

- Preserve upstream heading and introductory prose outside marker regions.
- Keep `<override_format>`, `<verifier_behavior>`, `<creating_overrides>`, and `<override_lifecycle>` tags as upstream anchors.
- Wrap each replaced tagged body in its own `GSD_MODIFIER` marker region.
- Produce the same debt-bearing frontmatter example, verifier-behavior bullet, `$gsd-verify-work` command examples, and `$gsd-audit-milestone` reference as the current overwrite for those four tagged sections.
- Leave the final `## Example VERIFICATION.md` block in upstream form, missing the two debt-bearing frontmatter lines that current modifier overlay adds.

Therefore the four-operation candidate is marker-clean but not full-fidelity.

The full-fidelity fallback would add a fifth operation that inserts `completion_mode` and `debt_bearing` between `status: passed` and `score: 3/3` inside the final fenced example. That would pass the current v4 verifier but would place marker comments inside the code example; this design does not recommend that without reviewer approval.

## Verification Approach

Slice 2 should not apply this carrier until the open question below is resolved.

If a reviewer approves the four-operation marker-clean-but-not-full-fidelity candidate, Slice 2 should run:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify .
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --source-only --strict
python3 -m unittest discover -s tooling/codex/tests
python3 -m unittest discover -s tooling/codex/tests -p 'test_inject*.py'
```

If a reviewer instead approves a full-fidelity marker-in-fence operation, Slice 2 should also visually inspect the materialized final example before treating the migration as acceptable.

## Rollback Plan

If Slice 2 proceeds and fails before commit:

1. Restore `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`.
2. Restore `tooling/portable-gsd/overlay/get-shit-done/references/verification-overrides.md`.
3. Remove the newly created `harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/` directory.
4. Rerun the failed Slice 2 gates.

If Slice 2 fails after commit, revert the single Slice 2 commit. No later Phase 4 carrier should depend on this migration until it has materialized cleanly under both runtimes.

## Open Questions

Blocking for Slice 2:

1. Should the final EOF fenced example be allowed to contain GSD marker comments inside the code block?
2. If not, should the final example debt-field delta be dropped as redundant, or should Phase 4 pause for an ADR amendment adding a clean EOF block-replacement operation?

Recommended next action: before applying this carrier, invoke a Plan/slice-ambiguity reviewer or stop for an ADR amendment decision. This is exactly the kind of not-pilot-evident issue Phase 4 was meant to surface.
