# Pilot Design: mandatory-initial-read.md

Date: 2026-05-16
Phase: 3 (`03-pilot`)
Slice: 1 (`design the migration`)
Status: design-only; no manifest, overlay, runtime, bootstrap, or contract behavior changed

## Decision

Migrate `get-shit-done/references/mandatory-initial-read.md` from `mode: overwrite` to `mode: inject` in Phase 3 Slice 2 using one `block_replace` operation in the degenerate same-anchor form.

The operation inserts the modifier-owned reading-tier section immediately after the upstream file's final directive sentence. Both Codex and Claude materializers use the same operation and marker key under `parity_intent: outcome_aligned`.

## Current State

Upstream source read from `/home/rookslog/workspace/projects/get-shit-done-upstream/get-shit-done/references/mandatory-initial-read.md` at upstream checkout `a7f0af2c`:

```markdown
**CRITICAL: Mandatory Initial Read**
If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.
```

Current modifier overwrite source:

```text
tooling/portable-gsd/overlay/get-shit-done/references/mandatory-initial-read.md
```

It preserves the two upstream lines and appends 20 modifier-owned lines defining reading packet tiers and contextual reread rules.

Current manifest entry:

```json
"get-shit-done/references/mandatory-initial-read.md": {
  "capability_id": "get-shit-done/references/mandatory-initial-read.md",
  "parity_tier": "core_required",
  "materializers": {
    "codex": {
      "mode": "overwrite",
      "target": "get-shit-done/references/mandatory-initial-read.md",
      "source": "tooling/portable-gsd/overlay/get-shit-done/references/mandatory-initial-read.md"
    },
    "claude": {
      "mode": "overwrite",
      "target": "get-shit-done/references/mandatory-initial-read.md",
      "source": "tooling/portable-gsd/overlay/get-shit-done/references/mandatory-initial-read.md"
    }
  }
}
```

Precise diff from upstream to current modifier source:

```diff
@@ -1,2 +1,22 @@
 **CRITICAL: Mandatory Initial Read**
 If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.
+
+**Reading packet tiers**
+
+- `<required_reading>`
+  - load all listed files before doing anything else
+  - this block carries the minimum context the task cannot proceed without
+- `<supporting_reading>`
+  - load only after the required block
+  - use it when the active route, anomaly, or user request points at one of those files
+  - do not widen into the whole supporting list by reflex
+- `<deeper_reading>`
+  - load only when the task is blocked, the current route explicitly depends on it, or you are intentionally widening the read set for a bounded reason
+  - do not treat deeper reading as default startup context
+
+**Contextual reread rules**
+
+- The blocks widen attention; they do not replace judgment about what the current task actually needs next.
+- When a workflow or prompt provides structured helpers, summaries, manifests, or snapshots, prefer those as the first route into the task before widening into broader prose files.
+- If a later route points into one specific family, reread that family deliberately rather than flattening the whole workspace into startup context.
+- If a prompt or workflow explicitly says a quoted anti-pattern, prohibition, or historical example must stay visible, do not rewrite or omit it merely to keep the packet narrow.
```

## Operation Choice

Do not use `include_add` or `section_insert_after` for this pilot.

This file is Markdown reference prose, not an XML-like workflow file. It does not contain a `<required_reading>` block; it describes that block. The viable v4 operation is `block_replace` with `start_anchor` equal to `end_anchor`, which ADR-001 explicitly treats as the degenerate insertion-after-anchor case.

The chosen anchor includes the upstream line ending:

```text
If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.\n
```

Reason: the no-newline anchor applies and verifies, but collapses the blank line before the injected Markdown section. Including the line ending preserves the current overwrite's visible spacing. If upstream removes the trailing newline, the operation should fail loud rather than silently produce a subtly different reference file.

## Proposed Manifest Entry

Slice 2 should bump the manifest `schema_version` from `3` to `4` and replace the existing entry with:

```json
"get-shit-done/references/mandatory-initial-read.md": {
  "capability_id": "get-shit-done/references/mandatory-initial-read.md",
  "parity_tier": "core_required",
  "parity_intent": "outcome_aligned",
  "materializers": {
    "codex": {
      "mode": "inject",
      "target": "get-shit-done/references/mandatory-initial-read.md",
      "operations": [
        {
          "kind": "block_replace",
          "start_anchor": "If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.\n",
          "end_anchor": "If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/mandatory-initial-read/extended-content.md",
          "marker_key": "GSD_MODIFIER:references-mandatory-initial-read:extended-content"
        }
      ]
    },
    "claude": {
      "mode": "inject",
      "target": "get-shit-done/references/mandatory-initial-read.md",
      "operations": [
        {
          "kind": "block_replace",
          "start_anchor": "If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.\n",
          "end_anchor": "If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/mandatory-initial-read/extended-content.md",
          "marker_key": "GSD_MODIFIER:references-mandatory-initial-read:extended-content"
        }
      ]
    }
  }
}
```

## Modifier Source File

Slice 2 should create:

```text
harness_modifier/overlay/inject-sources/get-shit-done/references/mandatory-initial-read/extended-content.md
```

Content:

```markdown
**Reading packet tiers**

- `<required_reading>`
  - load all listed files before doing anything else
  - this block carries the minimum context the task cannot proceed without
- `<supporting_reading>`
  - load only after the required block
  - use it when the active route, anomaly, or user request points at one of those files
  - do not widen into the whole supporting list by reflex
- `<deeper_reading>`
  - load only when the task is blocked, the current route explicitly depends on it, or you are intentionally widening the read set for a bounded reason
  - do not treat deeper reading as default startup context

**Contextual reread rules**

- The blocks widen attention; they do not replace judgment about what the current task actually needs next.
- When a workflow or prompt provides structured helpers, summaries, manifests, or snapshots, prefer those as the first route into the task before widening into broader prose files.
- If a later route points into one specific family, reread that family deliberately rather than flattening the whole workspace into startup context.
- If a prompt or workflow explicitly says a quoted anti-pattern, prohibition, or historical example must stay visible, do not rewrite or omit it merely to keep the packet narrow.
```

## Materialization Preview

Expected materialized output after applying the operation to upstream:

```markdown
**CRITICAL: Mandatory Initial Read**
If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.

<!-- GSD_MODIFIER:start key:GSD_MODIFIER:references-mandatory-initial-read:extended-content -->
**Reading packet tiers**

- `<required_reading>`
  - load all listed files before doing anything else
  - this block carries the minimum context the task cannot proceed without
- `<supporting_reading>`
  - load only after the required block
  - use it when the active route, anomaly, or user request points at one of those files
  - do not widen into the whole supporting list by reflex
- `<deeper_reading>`
  - load only when the task is blocked, the current route explicitly depends on it, or you are intentionally widening the read set for a bounded reason
  - do not treat deeper reading as default startup context

**Contextual reread rules**

- The blocks widen attention; they do not replace judgment about what the current task actually needs next.
- When a workflow or prompt provides structured helpers, summaries, manifests, or snapshots, prefer those as the first route into the task before widening into broader prose files.
- If a later route points into one specific family, reread that family deliberately rather than flattening the whole workspace into startup context.
- If a prompt or workflow explicitly says a quoted anti-pattern, prohibition, or historical example must stay visible, do not rewrite or omit it merely to keep the packet narrow.
<!-- GSD_MODIFIER:end key:GSD_MODIFIER:references-mandatory-initial-read:extended-content -->
```

## Source-Only Preflight

Ran an in-memory preflight using the current upstream file, current modifier overwrite source, and Phase 2 pure functions:

```text
apply_inject_operations(...)
verify_inject_state(...)
```

Result:

```text
upstream_lines 2
overlay_lines 22
source_body_lines 20
records [('block_replace', 'applied', 'GSD_MODIFIER:references-mandatory-initial-read:extended-content')]
verify_passed True
verify_details [('block_replace', 'verified', 'marker present between anchors')]
```

The generated content matches the current overwrite modulo marker lines and the final trailing newline after marker removal. The materialized file itself remains newline-terminated because the end marker is written as the final line.

## Verification Approach

Slice 2 should run:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify .
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --source-only --strict
python3 -m unittest discover -s tooling/codex/tests
python3 -m unittest discover -s tooling/codex/tests -p 'test_inject*.py'
```

Those gates confirm whitespace hygiene, no new unclassified reference-map issues, schema v4 source-only manifest validity, broad test continuity, and focused inject continuity.

Slice 3 should then run the state-mutating materialization gates required by the phase plan. The known installer/bootstrap blocker remains a Phase 3 completion risk; it is not a Slice 2 design blocker.

## Rollback Plan

If Slice 2 fails before commit:

1. Restore `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`.
2. Restore `tooling/portable-gsd/overlay/get-shit-done/references/mandatory-initial-read.md`.
3. Remove the newly created inject source directory for this carrier.
4. Rerun the Slice 2 verification gates that failed.

If Slice 2 fails after commit, revert the single Slice 2 commit. The pilot is one carrier only, so no later carrier migrations depend on it.

## Open Questions

No open questions block Slice 2.

Known Phase 3 completion risk: `check-bootstrap.sh` has a pre-existing installer/hooks-classification blocker recorded in `STATE.md` Out-Of-Scope Surface #3. Slice 2 can proceed source-only; Slice 3 cannot claim full end-to-end success until that blocker is resolved or explicitly routed by the phase-boundary review.
