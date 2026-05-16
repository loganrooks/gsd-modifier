# ADR-001 — Manifest Schema v4 (`mode: inject`)

Status: Draft (post-pre-execute-review; pending post-execute reviewer + operator approval per phase plan exit gate)
Date: 2026-05-16
Phase: inject-migration phase 01-schema-foundation slice 1
Supersedes: none (first ADR in this initiative)
Superseded by: none

## 1. Context

This ADR responds to drift pressure documented in three load-bearing sources:

1. **`intervention-strategies-2026-05-08.md` §1.4** (overwrite-pressure decomposition): of 75 manifest entries pre-Phase-0, 49 were `mode: overwrite` and 26 were `mode: add`. The 49 overwrites carried meaningful drift risk because every upstream change to those files invalidated modifier-owned content silently.
2. **`intervention-strategies-2026-05-08.md` §5** (manifest schema sketch): proposes a `mode: inject` extension defining operations against well-known anchors, with marker-bounded idempotency, so the modifier owns *additions* rather than *whole files*.
3. **`intervention-strategies-2026-05-08.md` §7** (strategy recommendation): patch-style materialization is the path of lowest long-term drift cost; the alternative (continued bulk overwrite) accumulates silent staleness as upstream evolves.

Supporting context:

- **`release-readiness-orientation-2026-05-08.md` §3** corrected the Plan 004 premise: the modifier carries post-conversion content (not pre-conversion). Injection at materialization time is therefore the correct architectural layer.
- **`release-readiness-orientation-2026-05-08.md` §4** documents the upstream gap evidence: many overwritten files have only small modifier-owned regions (often a single XML block), so injection-shaped additions are a natural fit.
- **Phase 0 closed 2026-05-16** with 4 stale-overwrite entries reclassified to `mode: add` (gsd-do, gsd-from-gsd2, gsd-plant-seed, research-phase). Roughly 45 modifier-owned overwrites remain that may benefit from injection in Phases 3–7.
- **`INITIATIVE.md` "The Model" §29-41** authoritatively narrows §5.2's 9-operation candidate set down to 7 operations as the v4 core catalog.

## 2. Decision

Adopt **manifest schema v4** with the following additions to schema v3:

1. **`mode: "inject"`** is a new materializer mode alongside `mode: "overwrite"` and `mode: "add"`.
2. **`operations` array** per `mode: inject` materializer, replacing the v3 single-`source` field. Each operation is an object with a `kind` discriminator and kind-specific arguments.
3. **`parity_intent` field** per entry, with values:
   - `outcome_aligned` — both runtimes produce equivalent visible modifier content after injection. Operations may differ between materializers; verification asserts outcome equivalence (the named markers are present).
   - `runtime_independent` — each runtime carries different modifier content (e.g., a Codex-only `<codex_skill_adapter>` block has no Claude analog). No equivalence assertion.
   The field is OPTIONAL for v3 entries (defaults to `outcome_aligned` for `core_required` and `core_adapted`; `runtime_independent` for `runtime_specific`). It is REQUIRED for v4 `mode: inject` entries.
4. **HTML-comment markers** as the idempotency primitive:
   ```
   <!-- GSD_MODIFIER:start key:KEY -->
   <content>
   <!-- GSD_MODIFIER:end key:KEY -->
   ```
   where `KEY` follows the convention `GSD_MODIFIER:<carrier-slug>:<op-slug>` (kebab-case ASCII; alphanumeric plus `-` and `:`).
5. **Backward compatibility**: `schema_version: 3` entries continue to validate and apply unchanged. v4 entries are recognized only when the manifest header declares `schema_version: 4`. Mixed-mode manifests (some v3 entries, some v4 entries) are allowed during the migration; each entry independently declares its own `mode`.

The `parity_intent` field name is used (not §5.5's proposed `parity_outcome`) because `INITIATIVE.md:198` glossary already names the field `parity_intent`. The rename is purely lexical; semantics are identical to §5.5.

## 3. Operation kind catalog

The v4 catalog defines **7 operation kinds**, narrowed from `intervention-strategies-2026-05-08.md` §5.2's 9-operation candidate list. The narrowing was made authoritatively at `INITIATIVE.md:33-41` ("The Model"), not invented at slice-spec time. The dropped kinds (`step_replace`, `line_replace`, `text_substitute`) are deferred:

- `step_replace` is implementable as `step_remove` + `step_insert_after` (2 operations); v4's catalog covers the kinds surfaced in the carrier survey via composition.
- `line_replace` and `text_substitute` cover narrow use cases not surfaced in the carrier survey; a future ADR (v4.1 or v5) may extend the catalog if Phase 3+ migrations surface a real need.

The §5.2 example manifest at `intervention-strategies-2026-05-08.md:538` uses `step_replace`, which means that particular illustrative carrier (`new-project.md`'s `generate_instruction_file` step) cannot be expressed in v4-as-defined without two operations. This is a deliberate trade-off: a smaller catalog with a small composition tax, vs a larger catalog with more validation surface and more semantic overlap. Slice 2's worked-example appendix will demonstrate the composition pattern.

The 7 kinds:

**Common to all kinds**: every operation accepts a `marker_key` (string) field declaring the unique KEY (per §4 convention) that labels the marker region the operation creates (for `section_insert_after`, `step_remove`, `step_insert_after`, `include_add`, `block_replace`) or the existing region it acts on (for `section_replace`, `include_remove`). The per-kind signatures below omit `marker_key` for brevity; the contract validator (Phase 2) enforces the field's presence and global uniqueness across the manifest. Worked examples in Appendix A show the field on every operation.

### `section_insert_after { tag, source }`

Insert content from a source file immediately after the named XML close tag in the target.

- `tag` (string): the XML tag name to anchor on (e.g., `"required_reading"`); the operation finds `</tag>` in the target and inserts after it.
- `source` (path): modifier file containing the content to insert.

The inserted content is wrapped in `<!-- GSD_MODIFIER:start key:KEY -->` / `<!-- GSD_MODIFIER:end key:KEY -->` markers.

### `section_replace { marker_key, source }`

Replace the content between matched start/end markers with content from a source file. Used for in-place updates of an already-injected section.

- `marker_key` (string): the `KEY` whose `start`/`end` markers bracket the region to replace.
- `source` (path): modifier file containing the new content.

This operation requires the markers to already be present in the target (i.e., a prior `section_insert_after` with the same key has run).

### `step_remove { name }`

Remove a `<step name="X">...</step>` block from the workflow's `<process>` section. Leaves a marker recording the removal:

```
<!-- GSD_MODIFIER:start key:KEY -->
<!-- GSD_MODIFIER:step_removed name:NAME -->
<!-- GSD_MODIFIER:end key:KEY -->
```

- `name` (string): the value of the step's `name` attribute.

### `step_insert_after { after_name, source }`

Insert a new `<step name="X">...</step>` block immediately after the step named `after_name`.

- `after_name` (string): the anchor step's `name` attribute value.
- `source` (path): modifier file containing the full `<step name="X">...</step>` element.

The inserted step is wrapped in markers.

### `include_add { tag, line }`

Add a single `@`-include line inside the named XML tag if the line is not already present. Used for adding `@__PROJECT_ROOT__/...` references inside `<required_reading>`, `<supporting_reading>`, etc.

- `tag` (string): the XML tag whose body receives the line.
- `line` (string): the literal line content to add (typically begins with `@`).

The line is wrapped in markers; if a prior `include_add` for the same `KEY` already exists, the operation is a no-op.

### `include_remove { tag, line }`

Remove a previously-added `@`-include line. Inverse of `include_add`.

- `tag` (string): the XML tag to search.
- `line` (string): the literal line to remove.

The marker block bracketing the line is also removed.

### `block_replace { start_anchor, end_anchor, source }`

Replace the content between two precise text anchors (no markers required). Used for cases where neither XML tags nor markers are available — e.g., bulk replacement of a fenced code block bounded by exact text.

- `start_anchor` (string): the literal text marking the start of the replaced region (the anchor itself is preserved).
- `end_anchor` (string): the literal text marking the end (preserved).
- `source` (path): modifier file containing the replacement content.

The replacement content is wrapped in markers; the anchors are NOT modified.

## 4. Marker conventions

### Format

```
<!-- GSD_MODIFIER:start key:KEY -->
<one or more lines of injected content>
<!-- GSD_MODIFIER:end key:KEY -->
```

The `<!-- ... -->` HTML-comment form was chosen because:

1. It survives in markdown without rendering visibly to readers.
2. JSON-stripping comment scrubbers in the manifest itself do not affect target files (the markers live in materialized targets, not in `OVERLAY-MANIFEST.json`).
3. It survives in HTML-rendered docs (the comments are stripped by browsers).
4. It survives in code files where `#`/`//` comments would conflict with the language.

### Key naming

```
KEY := "GSD_MODIFIER" ":" CARRIER_SLUG ":" OPERATION_SLUG
CARRIER_SLUG := lowercase-kebab-case, slashes replaced with dashes
                e.g., "workflows-new-project" for "workflows/new-project.md"
OPERATION_SLUG := lowercase-kebab-case description of the operation's intent
                  e.g., "supporting-reading", "include-mandatory-initial-read"
```

Examples:

- `GSD_MODIFIER:workflows-new-project:supporting-reading`
- `GSD_MODIFIER:workflows-health:remove-context-check`
- `GSD_MODIFIER:references-mandatory-initial-read:add-content`

### Idempotency guarantee

The presence of the `<!-- GSD_MODIFIER:start key:KEY -->` marker in a target file means the operation with that `KEY` has been applied. The apply-time logic checks for marker presence before applying; if present, the operation is skipped (idempotent happy path).

Marker keys MUST be globally unique across the manifest (across all entries and all operations). The contract validation tool (Phase 2) will enforce uniqueness.

## 5. Parity_intent semantics

`parity_intent` describes what equivalence (if any) is asserted between per-runtime materializer outputs.

### `outcome_aligned`

Both runtimes are expected to produce the same modifier-owned content visible in their respective materialized files. The operations themselves may differ between materializers (e.g., one may use `section_insert_after`, the other `block_replace`) as long as the modifier-owned content arrives in both.

Verify-time check: both runtimes' materialized targets contain the markers for all operations declared in their respective materializer blocks, AND the marker-bounded content matches across runtimes (when the operation's source file is the same — which is the common case).

Use this for shared workflows where the modifier wants the same effective behavior regardless of which runtime is reading the file.

### `runtime_independent`

Each runtime carries different modifier content. No cross-runtime equivalence is asserted.

Verify-time check: each runtime's materialized target independently contains its declared markers; no cross-runtime comparison.

Use this for runtime-specific extensions (Codex-only `<codex_skill_adapter>` blocks, Claude-only YAML frontmatter additions, etc.).

### Relation to `parity_tier`

`parity_tier` (existing field; values: `core_required`, `core_adapted`, `runtime_specific`) is a **design-time** declaration of which carriers must be installed for which install profiles.

`parity_intent` (new field) is a **materialization-time** declaration of what equivalence is asserted at the verify gate.

The typical case for shared workflows is `parity_tier: core_required` PLUS `parity_intent: outcome_aligned`. The two fields are orthogonal: `parity_tier` says "this carrier must be present in all profiles", while `parity_intent` says "if it's present, both runtimes produce equivalent modifier-owned content".

## 6. Backward compatibility

### Schema version semantics

- Manifests with `schema_version: 3` continue to validate identically to today.
- Manifests with `schema_version: 4` accept all v3 modes (`overwrite`, `add`) PLUS the new `inject` mode.
- The `parity_intent` field is OPTIONAL for v3 entries (with the defaults specified in §2).
- Validation code branches on `schema_version` (the existing branch in `portable_gsd_contract.py:295-312` per `intervention-strategies §5.6`).

### Mixed-mode manifests

A v4 manifest may contain a mix of `mode: overwrite`, `mode: add`, and `mode: inject` entries. Each entry independently declares its own mode. There is no requirement that all entries migrate at the same time.

### Migration trigger

The `schema_version` bumps from 3 to 4 the first time a `mode: inject` entry is added to the manifest. After the bump, all existing entries continue to apply unchanged.

### Rollback

If a `mode: inject` entry needs to be reverted to `mode: overwrite` (e.g., the inject-mechanism turns out unsuitable for a particular carrier), the procedure is:

1. Edit the manifest entry to change `mode: inject` → `mode: overwrite`, restore the `source` field, remove the `operations` array.
2. The next materializer run will overwrite the target file with the source, removing all inject markers.
3. Backup-meta tracking handles the cleanup automatically.

## 7. Apply-time semantics

For each `mode: inject` entry, the apply procedure is:

1. **Read** the upstream-installed target file content into memory.
2. **For each operation** in the order declared in the `operations` array:
   - Compute the marker `KEY` (per §4 convention).
   - Check whether the `<!-- GSD_MODIFIER:start key:KEY -->` marker is already present in the in-memory content.
     - If present AND the marker-bounded content matches the source file content (or, for marker-only operations like `step_remove`, the marker bracket contains the expected `<!-- GSD_MODIFIER:step_removed -->` sentinel): **skip** (idempotent happy path).
     - If present AND the marker-bounded content differs from expected: **fatal — marker key conflict** (the same `KEY` is in use with different content; this is a configuration error, not a recoverable state).
     - If absent: **apply** the operation in-memory (mutate the working content).
3. **Atomic write** the resulting file content to the target path.

### Pre-flight atomicity

All operations are computed in-memory before any file write. If any operation fails mid-sequence (anchor not found, source file missing, marker conflict), the original target file on disk is preserved untouched. The partial in-memory state is discarded; no half-migrated file is ever written.

### Failure modes (all fatal)

- **Anchor not found**: an operation's anchor (XML tag for `section_insert_after`, step name for `step_*`, text anchor for `block_replace`) is not present in the target. Likely cause: upstream renamed or removed the anchor.
- **Source file missing**: the operation's `source` path does not resolve. Likely cause: typo in manifest or modifier source not committed.
- **Marker key conflict**: marker present with content that differs from expected. Likely cause: two operations were given the same `KEY` (configuration error) OR a manual edit modified the marker-bounded content (operator intervention required).

Fail-loud is the default per `INITIATIVE.md:210`; the inject mechanism does not attempt automatic recovery from these failures. The operator triages and either fixes the manifest, updates the operation's anchor, or accepts the failure as a signal that the carrier should move back to `mode: overwrite`.

## 8. Verify-time semantics

For each `mode: inject` entry, the verify procedure is:

1. Read the materialized target file content.
2. **For each operation** in the entry's `operations` array:
   - Check that the `<!-- GSD_MODIFIER:start key:KEY -->` marker is present in the materialized content (Option V1 from `intervention-strategies-2026-05-08.md:632-638`).
   - Verify the marker is positioned correctly (e.g., for `section_insert_after`, the start marker appears after the anchor `</tag>`).
3. Pass if all operations' markers are present in the expected positions; fail if any is absent or misplaced.

### V1 default vs V2 trade-off

The verify procedure uses **Option V1** (marker presence + position check) as the default, NOT Option V2 (marker presence + content-hash verification of the marker-bounded region). This is a deliberate trade-off:

- **V1 advantage**: cheap, fast, tolerant of in-marker drift (e.g., upstream renames a sub-anchor that the modifier's source file references).
- **V1 risk**: an operator who manually edits inside the markers will not be caught at verify time. The marker is present, the position is correct, but the content has drifted from the modifier's intent.

`INITIATIVE.md:219` flags "subtly different content than `mode: overwrite`" as a high-impact risk. The mitigation chain accepted by this ADR is:

1. **Per-slice smoke tests** during migration (Phase 3+) that read the materialized file and assert key content strings are present.
2. **Phase 3's pilot content-equivalence check** that compares the materialized content to a golden snapshot.
3. **Operator vigilance**: the markers are visible in any file diff; operators reviewing materialized state can spot in-marker drift.

V2 is **deferred** to a future ADR if Phase 3 surfaces real in-marker drift incidents. Re-introducing V2 is a backward-compatible extension: add an optional `content_hash` field to operation entries; the verifier checks it when present, ignores it when absent.

V3 (whole-file hash) is **rejected** because it is incompatible with the goal "non-marker regions can drift" (per `intervention-strategies-2026-05-08.md:649`).

## 9. Migration guidance

A decision tree for evaluating whether an existing `mode: overwrite` carrier should move to `mode: inject`:

**Step 0 — Is this carrier modifier-net-new (no upstream analog)?**

If yes (e.g., a skill the modifier ships that upstream does not have at all): keep as `mode: add`. **The carrier should not move to `mode: inject`.** This is the boundary Phase 0 traversed for the 4 stale-deleted carriers (gsd-do, gsd-from-gsd2, gsd-plant-seed, research-phase) — they remain `mode: add` because there is no upstream file to inject into.

If no (the carrier shadows an upstream file), proceed to Step 1.

**Step 1 — How much of the file's content does the modifier own?**

- `>70%` modifier-owned: keep as `mode: overwrite`. The injection model adds operation-validation overhead without proportional benefit when the modifier rewrites most of the file.
- `<30%` modifier-owned: strong candidate for `mode: inject`.
- `30%–70%`: judgment call; weigh anchor stability and operation count.

**Step 2 — Is the modifier's contribution shaped as anchor-targeted additions?**

- "Add a section after `<required_reading>`" → `section_insert_after`.
- "Add an include inside `<supporting_reading>`" → `include_add`.
- "Replace the body of an existing section, leaving the section tag" → `section_replace` (after a prior `section_insert_after` lands).
- "Modify upstream's `<process>` steps" → `step_remove` / `step_insert_after`.
- "Replace a precisely-bounded text block with no convenient anchor" → `block_replace` (use sparingly; brittle to upstream text changes).

**Step 3 — Are the upstream anchors stable?**

If upstream has renamed or restructured the anchor more than once in the past year: prefer `mode: overwrite` (the inject mechanism's robustness depends on anchor stability). If anchors are stable: `mode: inject` is robust.

**Step 4 — Is the modifier-owned content runtime-specific?**

If the content has no equivalent in the other runtime (e.g., a Codex `<codex_skill_adapter>` block): set `parity_intent: runtime_independent`. Otherwise (the typical case): `parity_intent: outcome_aligned`.

## 10. Out of scope (this ADR does NOT cover)

### Mechanism extensions deferred to future ADRs

- **Conditional operations** (e.g., "apply only if upstream version >= X"): operation execution is unconditional in v4. A future ADR may add `condition` field if needed.
- **Runtime-time operation evaluation**: operations are static at apply-time; nothing is evaluated at runtime read time. The materialized file is the artifact.
- **Dynamic regex-matched anchors**: anchors are literal text or named XML tags. Regex matching is not supported.
- **Operation rollback beyond "restore captured pristine then re-apply"**: there is no per-operation undo. To roll back an operation, restore the pristine baseline and re-apply the operation set without the unwanted operation.
- **In-marker content-hash verification (Option V2)**: deferred; see §8.

### Boundaries with adjacent surfaces

- **What `mode: inject` is NOT for**: modifier-net-new carriers with no upstream file (these stay `mode: add` per §9 Step 0). Phase 0's reclassified carriers (gsd-do, gsd-from-gsd2, gsd-plant-seed, research-phase) demonstrate the boundary — they are modifier-owned, but they are NOT injection candidates because there is no upstream file to inject into.
- **Phase 2 contract code implementation**: this ADR specifies WHAT the apply/verify procedures do. It does NOT specify HOW they are implemented (function signatures, module structure, error message format). Those decisions belong to Phase 2's slice specs and will be made within the constraints of this ADR.
- **Phase 3 pilot specifics**: the pilot will migrate `references/mandatory-initial-read.md` (per `INITIATIVE.md` and Slice 2's worked example A.1). The exact operation sequence, source file structure, and marker keys are NOT pre-committed by this ADR; they are decided in Phase 3's slice specs.

### Interaction with the upstream installer's migrations prompt

`STATE.md → Out-Of-Scope Surfaces #3` documents that the upstream installer (called by `setup-portable-gsd-runtime.sh`) currently blocks on 12 pre-existing untracked `.codex/hooks/` files, preventing the bootstrap chain from running end-to-end.

The inject mechanism's relationship to this block is **layered**, not uniform:

- **At the installer-block layer**: if the installer cannot run, the materializer cannot run, and ALL modes (`overwrite`, `add`, `inject`) are equally blocked. The installer-block is upstream-driven and orthogonal to mode choice.
- **At the partial-failure layer (after installer runs)**: `mode: inject` has more failure surface than `mode: overwrite` because injection involves multiple sequential operations. A failure mid-sequence COULD leave a half-migrated file in principle. §7's "pre-flight atomicity" requirement closes this risk: all operations are computed in-memory before the atomic write, so a mid-sequence failure preserves the original target untouched. The failure surface is therefore equivalent to `mode: overwrite` (atomic write succeeds or doesn't), modulo the additional failure modes (anchor not found, source missing, marker conflict) that `mode: overwrite` does not have.

### Phase coupling

This ADR does not pre-authorize Phase 1 Slice 3's edit to AGENTS.md/CLAUDE.md change-class triggers (that's Slice 3's pre-spec'd write set). It does not pre-authorize Phase 2's contract code (Phase 2 gets its own slice plans).

## 11. Risks (initiative-level; mitigation responsibility)

| Risk | Likelihood | Impact | Mitigation owner |
|---|---|---|---|
| Phase 3 pilot reveals an operation kind the v4 catalog cannot express | medium | low (catalog is extensible via future ADR) | Slice 2 worked examples surface this early; Phase 3 reviewer-mediated |
| In-marker drift after manual edits goes undetected at verify time (V1 weakness) | medium | medium | Per-slice smoke tests; Phase 3 content-equivalence check; operator vigilance on materialized diffs |
| Upstream anchor rename breaks an inject operation | medium | low (fail-loud surfaces it; fix is operation update or revert to overwrite) | Operator triage on apply failure |
| Marker key collision across entries | low (validation will enforce uniqueness) | high (silent operation skip if the validator misses) | Phase 2 contract code MUST enforce global key uniqueness in `validate-manifest` |
| Schema v4 entries land before Phase 2 contract code can read v4 | low (this ADR explicitly defers v4 entries until Phase 2 ships) | medium (validation breaks; bootstrap fails) | Phase 2 ships before any v4 entry is added; the schema_version bump to 4 happens in Phase 3 pilot, not Phase 2 |
| Installer-block on hooks (Out-Of-Scope Surfaces #3) blocks Phase 1+ verification | medium | high | Phase 1 produces design only; Phase 2+ test code can mock the installer surface; full bootstrap-chain verification is a separate operational track |

## Appendix A: Worked Examples

This appendix demonstrates the schema (§3 catalog, §4 markers, §7 apply, §8 verify) against five representative carriers. Per `phases/01-schema-foundation.md:84`, the appendix is illustrative and does NOT pre-commit to the exact migration approach for these carriers; each migration phase reviews the example and commits to a final approach.

The five examples are NOT chosen to flatter the schema — A.1, A.2, and A.5 are deliberately included to surface boundary cases. A "Patterns surfaced" subsection at the end names the design observations the worked examples produced (including the schema gaps they identify) for operator review at the Phase 1 exit gate (`phases/01-schema-foundation.md:120`).

### A.1 — `references/mandatory-initial-read.md` (Phase 3 pilot target)

**Current state**

- Upstream installed at `.codex/get-shit-done/references/mandatory-initial-read.md`: 2 lines (only the "**CRITICAL: Mandatory Initial Read**" header and a single directive sentence ending "...This is your primary context.")
- Modifier overlay at `tooling/portable-gsd/overlay/get-shit-done/references/mandatory-initial-read.md`: 23 lines (lines 1-2 mirror upstream; lines 3-23 are modifier-added content describing the `<required_reading>` / `<supporting_reading>` / `<deeper_reading>` reading-tier semantics and contextual-reread rules)
- Mode today: `overwrite` (per OVERLAY-MANIFEST.json:322-337); both codex and claude materializers
- File format: markdown; NO XML tags

**Schema gap surfaced**

The slice spec line 70 suggested "pure `section_insert_after` after `<required_reading>`". The file does NOT contain a `<required_reading>` block — it is a reference document ABOUT that block, which lives in workflow files. The v4 catalog's `section_insert_after` requires an XML close tag (`</tag>`) as the anchor, which this file lacks. Modifier-added content goes at end-of-file (after the last upstream line), not after a tagged block.

`block_replace` is the catalog's nearest fit, but it is also not a clean match: the modifier's content goes AFTER the last upstream line, not BETWEEN two anchors. The semantics work via a degenerate same-anchor case (start_anchor == end_anchor; "between" is empty; replacement effectively inserts at that position), but the appendix flags this as a real schema gap surfaced by the pilot example. See "Patterns surfaced" below for the recommended future amendment.

**Proposed `mode: inject` manifest entry**

```json
{
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
            "start_anchor": "If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.",
            "end_anchor": "If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.",
            "source": "harness_modifier/overlay/get-shit-done/references/mandatory-initial-read/extended-content.md",
            "marker_key": "GSD_MODIFIER:references-mandatory-initial-read:extended-content"
          }
        ]
      },
      "claude": "<<same operations as codex; outcome_aligned>>"
    }
  }
}
```

**Proposed modifier source files**

- `harness_modifier/overlay/get-shit-done/references/mandatory-initial-read/extended-content.md`: lines 3-23 of today's overwrite source, no front-matter or XML wrapping (the markers are added at apply-time per §4)

**Expected materialized output sketch**

```markdown
**CRITICAL: Mandatory Initial Read**
If the prompt contains a `<required_reading>` block, you MUST use the `Read` tool to load every file listed there before performing any other actions. This is your primary context.

<!-- GSD_MODIFIER:start key:GSD_MODIFIER:references-mandatory-initial-read:extended-content -->

**Reading packet tiers**

- `<required_reading>`
  - load all listed files before doing anything else
[... 17 more modifier-owned lines per today's overwrite source ...]

<!-- GSD_MODIFIER:end key:GSD_MODIFIER:references-mandatory-initial-read:extended-content -->
```

**Edge cases**

- Same start_anchor == end_anchor: per §7 marker-conflict semantics, the operation finds the anchor once, treats "between" as empty (zero characters), wraps modifier content in markers, inserts at that position. Apply-time logic must handle the degenerate-block-replace case explicitly (this is a Phase 2 implementation note, not a v4 schema requirement).
- Upstream changes the directive sentence: anchor mismatch; fail-loud; operator either updates the anchor to match new upstream text or accepts that this carrier should remain `mode: overwrite` until upstream stabilizes.
- File becomes empty upstream (e.g., upstream deletes the file): operation fails (anchor not found); fail-loud surfaces the upstream change.

### A.2 — `references/agent-contracts.md` (medium additive)

**Current state**

- Upstream at `.codex/get-shit-done/references/agent-contracts.md`: 79 lines; markdown with `##` headings (`# Agent Contracts`, `## Agent Registry`, `## Marker Rules`, `## Key Handoff Contracts` with 4 `###` subsections, `## Workflow Regex Patterns`)
- Modifier overlay at `tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md`: 109 lines (~30 modifier-added lines)
- Mode today: `overwrite` (per OVERLAY-MANIFEST.json:274-289)
- File format: markdown with `##` heading anchors; NO XML tags

**Schema gap surfaced (same family as A.1)**

Same as A.1: this is a markdown reference file with no XML tags. The `section_insert_after { tag }` operation does not apply. The workaround uses `block_replace` with markdown-heading text as anchors. The "Patterns surfaced" section names this collectively.

**Proposed `mode: inject` manifest entry (sketch)**

```json
{
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
            "start_anchor": "## Workflow Regex Patterns",
            "end_anchor": "<<the next-stable-anchor or EOF; see Patterns surfaced gap>>",
            "source": "harness_modifier/overlay/get-shit-done/references/agent-contracts/modifier-extensions.md",
            "marker_key": "GSD_MODIFIER:references-agent-contracts:modifier-extensions"
          }
        ]
      },
      "claude": "<<same operations as codex; outcome_aligned>>"
    }
  }
}
```

**Proposed modifier source files**

- `harness_modifier/overlay/get-shit-done/references/agent-contracts/modifier-extensions.md`: the ~30 modifier-added lines, isolated from the upstream content; specific section depends on Phase 4's actual diff between upstream and overlay versions

**Edge cases**

- Same EOF schema gap as A.1: if modifier content goes after the last upstream heading, end_anchor needs to be either the last line of upstream or a sentinel for end-of-file; current schema has no clean expression
- Upstream adds a new section after `## Workflow Regex Patterns`: anchor still resolves but the inserted modifier content lands BEFORE the new upstream section (which may or may not be the desired position); operator triages on apply

### A.3 — `workflows/spec-phase.md` (additive workflow)

**Current state**

- Upstream at `.codex/get-shit-done/workflows/spec-phase.md`: ~286 lines (modifier overwrite has same line count; difference is internal); XML tags `<purpose>`, `<ambiguity_model>`, `<interview_perspectives>`, `<process>`, `<critical_rules>`, `<success_criteria>` (verified via grep)
- Notably ABSENT from upstream: `<required_reading>`, `<supporting_reading>`, `<deeper_reading>` — the modifier wants to ADD a `<supporting_reading>` block
- Mode today: `overwrite` (per OVERLAY-MANIFEST.json:818-833)
- File format: XML-tagged; clean candidate for v4

**Operation choice: single `section_insert_after` with self-contained source**

Per the pre-execute reviewer's recommendation (option b), the modifier's source file already contains both the `<supporting_reading>` block opening tag AND the `@`-include line(s) inside it. This avoids the cross-operation dependency that the original plan (`section_insert_after` + `include_add` chain) would have required. Single operation; clean v4 expression.

**Proposed `mode: inject` manifest entry**

```json
{
  "get-shit-done/workflows/spec-phase.md": {
    "capability_id": "get-shit-done/workflows/spec-phase.md",
    "parity_tier": "core_required",
    "parity_intent": "outcome_aligned",
    "materializers": {
      "codex": {
        "mode": "inject",
        "target": "get-shit-done/workflows/spec-phase.md",
        "operations": [
          {
            "kind": "section_insert_after",
            "tag": "purpose",
            "source": "harness_modifier/overlay/get-shit-done/workflows/spec-phase/supporting_reading_block.md",
            "marker_key": "GSD_MODIFIER:workflows-spec-phase:supporting-reading"
          }
        ]
      },
      "claude": "<<same; outcome_aligned>>"
    }
  }
}
```

**Proposed modifier source files**

- `harness_modifier/overlay/get-shit-done/workflows/spec-phase/supporting_reading_block.md`:
  ```xml
  <supporting_reading>
  @__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md
  @__PROJECT_ROOT__/.codex/get-shit-done/references/spec-quality-rubric.md
  </supporting_reading>
  ```
  (Self-contained block; no chained `include_add` needed)

**Expected materialized output sketch**

```xml
<purpose>
[... upstream purpose content ...]
</purpose>

<!-- GSD_MODIFIER:start key:GSD_MODIFIER:workflows-spec-phase:supporting-reading -->
<supporting_reading>
@__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md
@__PROJECT_ROOT__/.codex/get-shit-done/references/spec-quality-rubric.md
</supporting_reading>
<!-- GSD_MODIFIER:end key:GSD_MODIFIER:workflows-spec-phase:supporting-reading -->

<ambiguity_model>
[... continues ...]
```

**Edge cases**

- Upstream renames `<purpose>` to `<intent>`: anchor not found; fail-loud; operator updates the manifest's `tag` field
- Modifier later wants to add another `@`-include to the inserted `<supporting_reading>` block: today's options are (a) edit the modifier source file and re-run materializer (the markers are re-emitted with new content; idempotency-key match means skip-if-content-same OR fatal-if-content-different per §7), (b) use `section_replace` to swap the marker-bounded region, (c) use a future `include_add` operation that targets text inside an existing marker region (NOT supported by v4 — see "Patterns surfaced")

### A.4 — `workflows/health.md` (step-level)

**Current state**

- Upstream at `.codex/get-shit-done/workflows/health.md`: line 36 contains `<step name="context_check">` (verified)
- Modifier overlay at `tooling/portable-gsd/overlay/get-shit-done/workflows/health.md`: 300 lines; line 52 contains `<step name="keep_route_boundaries_explicit">` (modifier-added; verified)
- Mode today: `overwrite` (per OVERLAY-MANIFEST.json:594-609)
- File format: XML-tagged with `<process>` and multiple `<step>` blocks; clean candidate for v4

**Operation choice: `step_remove` + `step_insert_after`**

The modifier wants to (1) remove upstream's `context_check` step (per intervention-strategies §5.1 example) and (2) insert its own `keep_route_boundaries_explicit` step after the `validate` step. Two independent operations targeting the same `<process>` block.

**Proposed `mode: inject` manifest entry**

```json
{
  "get-shit-done/workflows/health.md": {
    "capability_id": "get-shit-done/workflows/health.md",
    "parity_tier": "core_required",
    "parity_intent": "outcome_aligned",
    "materializers": {
      "codex": {
        "mode": "inject",
        "target": "get-shit-done/workflows/health.md",
        "operations": [
          {
            "kind": "step_remove",
            "name": "context_check",
            "marker_key": "GSD_MODIFIER:workflows-health:remove-context-check"
          },
          {
            "kind": "step_insert_after",
            "after_name": "validate",
            "source": "harness_modifier/overlay/get-shit-done/workflows/health/keep_route_boundaries_explicit.md",
            "marker_key": "GSD_MODIFIER:workflows-health:keep-route-boundaries-explicit"
          }
        ]
      },
      "claude": "<<same; outcome_aligned>>"
    }
  }
}
```

**Proposed modifier source files**

- `harness_modifier/overlay/get-shit-done/workflows/health/keep_route_boundaries_explicit.md`: the full `<step name="keep_route_boundaries_explicit">...</step>` element (today at lines 52-61 of the overwrite source)

**Expected materialized output sketch (around the step_remove and step_insert_after operations)**

```xml
<process>
[... earlier upstream steps ...]

<step name="parse_args">
[... upstream content ...]
</step>

<!-- GSD_MODIFIER:start key:GSD_MODIFIER:workflows-health:remove-context-check -->
<!-- GSD_MODIFIER:step_removed name:context_check -->
<!-- GSD_MODIFIER:end key:GSD_MODIFIER:workflows-health:remove-context-check -->

<step name="run_health_check">
[... upstream content ...]
</step>

<step name="validate">
[... upstream content ...]
</step>

<!-- GSD_MODIFIER:start key:GSD_MODIFIER:workflows-health:keep-route-boundaries-explicit -->
<step name="keep_route_boundaries_explicit">
[... modifier-owned step content ...]
</step>
<!-- GSD_MODIFIER:end key:GSD_MODIFIER:workflows-health:keep-route-boundaries-explicit -->

<step name="offer_repair">
[... upstream content ...]
</step>
[... continues ...]
</process>
```

**Edge cases**

- Upstream renames `context_check` step: `step_remove` operation fails (anchor not found); fail-loud; operator either updates the manifest or accepts that the upstream rename means the step should no longer be removed
- Upstream renames `validate` step: `step_insert_after` fails; operator triages
- Upstream re-adds a `context_check` step in a future version: the marker comment from `step_remove` is still present; operator must decide whether to re-remove (re-apply the operation) or re-incorporate the upstream step (delete the manifest operation)

### A.5 — `bin/lib/state.cjs` (explicit non-example: must stay `mode: overwrite`)

**Why this is NOT an inject candidate**

Per §9 Step 1 (the >70% modifier-owned heuristic) and §9 Step 2 (the operation-choice mapping):

1. **`bin/lib/state.cjs` is 1687 lines** (per `wc -l`). The modifier owns substantially all of this file; it is a runtime library shipped exclusively by the modifier (no upstream analog with similar shape).
2. **JavaScript is not in §9 Step 2's mapping**. The mapping covers XML-tagged additions (`section_insert_after`, `include_add`), step-level workflow modifications (`step_remove`, `step_insert_after`), and text-anchor block replacement (`block_replace`). Code files are not addressed.
3. **The schema deliberately scopes to XML/markdown carriers**. §3's operation catalog uses XML tag close (`</tag>`) and named XML elements (`<step name="X">`) as anchors. JavaScript has no stable analog: function boundaries are not standardized text patterns; module exports change shape across upstream versions; comment-bounded regions are language-specific and conflict with HTML-comment markers (which are not valid JavaScript syntax).

**Conclusion**

`bin/lib/state.cjs` and similar code carriers (`*.cjs`, `*.js`, `*.py`) stay `mode: overwrite` per §9 Step 1's >70% rule AND the schema's XML/markdown scope. v4 does not attempt to express code-file modifications; that is an explicit out-of-scope per §10's "Boundaries with adjacent surfaces" subsection.

A future ADR could extend the schema with code-file-aware operations (e.g., `function_replace { name }` for JavaScript, `class_method_insert { class, method, source }`), but that is a non-trivial design effort with cross-language complications and is deferred indefinitely. Code carriers stay `mode: overwrite` for the foreseeable future.

### Patterns surfaced (operator review at Phase 1 exit gate)

The five worked examples surfaced the following design observations. Each is a candidate for operator review at the Phase 1 exit gate per `phases/01-schema-foundation.md:120`. None blocks Slice 3; all are appendix-author judgment calls the operator should ratify or revise.

**1. Schema gap: append-after-text shape (A.1, A.2)**

Both A.1 and A.2 surfaced that the v4 catalog has no first-class operation for "insert content after a specific text anchor with no end anchor (i.e., end-of-file or end-of-section)." The current workaround uses `block_replace` with degenerate same-anchor (start_anchor == end_anchor; "between" is empty). This works but is awkward to express and depends on Phase 2 contract code handling the degenerate case explicitly.

**Recommended future amendment** (deferred to a future ADR if Phase 4+ migrations need it repeatedly): add an `append_after_text { anchor, source }` operation kind, OR extend `block_replace` to allow `end_anchor: null` (or a sentinel value) meaning "to end-of-file/section". The amendment is backward-compatible (purely additive). Slice 3 of Phase 1 (governance triggers) is not the right place for a schema amendment; surface to operator at Phase 1 exit gate.

**2. Schema gap: non-XML markdown anchors (A.1, A.2)**

The v4 catalog's `section_insert_after { tag }` requires an XML close tag. Markdown files with `##` headings (like A.1, A.2) cannot use this operation. The workaround is `block_replace` with text anchors at heading text. This works but loses the semantic clarity of "insert after this section."

**Recommended future amendment** (deferred): add `section_insert_after_heading { heading_text, level, source }` operation kind for markdown carriers. Same backward-compatibility properties as #1 above.

**3. Cross-operation dependency considered and avoided (A.3)**

The pre-execute reviewer flagged that `include_add` targeting a tag introduced by a prior `section_insert_after` in the same `operations` array depends on §7's sequential in-memory application semantics, which §3's `include_add` spec does not explicitly mention. A.3 was redesigned (per pre-execute recommendation) to use a single self-contained `section_insert_after` whose source file already contains the `@`-include lines, avoiding the cross-operation dependency. This is a clean composition for v4.

**Future carriers may legitimately need the chain** (`section_insert_after` then `include_add` into the just-inserted block). When that case arises, the recommendation is to either (a) bundle the chain into the source file as A.3 does, OR (b) amend §3's `include_add` spec to explicitly allow targeting tags inside prior-operation marker regions. The amendment is not blocking for v4 release.

**4. Code carriers explicitly out-of-scope by design (A.5)**

The §9 Step 2 mapping table does not cover code files. A.5 makes this boundary explicit. Future operators evaluating whether to migrate a `.cjs`/`.js`/`.py` carrier to `mode: inject` should default to "no — keep as `mode: overwrite`" until a future ADR introduces code-file-aware operations.

**5. Idiom catalog (for Phase 3+ migrations)**

The five examples surface 3 reusable idioms:

- **Add-a-tagged-block** (A.3): single `section_insert_after`; source file contains the entire new XML block including the open and close tags
- **Remove-and-replace-step** (A.4): `step_remove` + `step_insert_after`; two operations on the same `<process>` parent
- **Append-modifier-content-to-non-XML-file** (A.1, A.2): `block_replace` with degenerate same-anchor; workaround pending append-after-text amendment

Phase 3+ migration phases should cite these idiom names rather than re-deriving the operation choices from scratch.
