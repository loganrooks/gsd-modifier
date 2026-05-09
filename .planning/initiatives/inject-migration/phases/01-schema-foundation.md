# Phase 1 — Schema Foundation

ID: `01-schema-foundation`
Status: `pending`
Dependencies: Phase 0 complete (clean baseline)
Approval gates: operator review of ADR before phase exit

## Objective

Produce a reviewed, durable Architecture Decision Record (ADR) defining the manifest schema v4 (`mode: inject`), the operation kind catalog, marker conventions, parity_intent semantics, and backward compatibility with v3. No code changes; design documentation only.

## Rationale

Phase 2 implements the contract code. That implementation needs a stable spec to follow. Phase 1 produces that spec as a reviewable artifact, exercises it on paper against representative carriers, and locks the design before code is written. This is the cheapest moment to discover spec gaps.

The operator review gate at phase exit catches design issues before they're encoded in implementation.

## Approach

Three slices. Slice 1 drafts the ADR. Slice 2 walks five representative carriers through the schema as a worked example (still in the ADR; appendix-style). Slice 3 adds the `mode: inject` change-class trigger entry to AGENTS.md and CLAUDE.md (extending Phase 0 Slice 5).

The ADR lives at `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md`. The decisions/ directory is created if needed.

## Slice Catalog

### Slice 1 — Draft the ADR (schema, operation kinds, markers, parity_intent)

- **Status**: `[ ]`
- **Type**: planning artifact (not contract-carrying yet)
- **Write set**:
  - `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md` → CREATE
- **Required ADR sections**:
  1. **Context** — citing intervention-strategies §5 and orientation artifacts as source
  2. **Decision** — adopt manifest schema v4 with `mode: "inject"` plus operation array; introduce `parity_intent` field (`outcome_aligned` | `runtime_independent`); `<!-- GSD_MODIFIER:start key:KEY -->` markers as the idempotency primitive
  3. **Operation kind catalog**:
     - `section_insert_after { tag, source }` — insert content from source file after the named XML tag
     - `section_replace { marker_key, source }` — replace content between matched start/end markers with content from source
     - `step_remove { name }` — remove `<step name="X">...</step>` from the workflow's `<process>`
     - `step_insert_after { after_name, source }` — insert step after named anchor
     - `include_add { tag, line }` — add an `@`-include line inside the named tag if absent
     - `include_remove { tag, line }` — remove the matching `@`-include line
     - `block_replace { start_anchor, end_anchor, source }` — replace a block matched by precise text anchors (no markers)
  4. **Marker conventions** — exact format for `GSD_MODIFIER` markers; key naming rules; idempotency guarantees
  5. **Parity_intent semantics** — when each value applies; relation to `parity_tier`
  6. **Backward compatibility** — schema v3 entries (with `mode: overwrite` or `mode: add`) continue to validate and apply; v4 entries are recognized only when `schema_version: 4` is set in the manifest header
  7. **Apply-time semantics** — how `apply_inject_operations` proceeds: read upstream file, apply operations in declared order, write result; failure mode (missing anchor) is fatal
  8. **Verify-time semantics** — how `verify_inject_state` confirms operations landed: re-read materialized file, confirm each operation's expected effect is present (markers exist, expected lines exist)
  9. **Migration guidance** — how to evaluate whether an existing `mode: overwrite` carrier should move to `mode: inject` (decision tree)
  10. **Out of scope** — what schema v4 deliberately does NOT cover (e.g., conditional operations, runtime-time operation evaluation, dynamic anchors)
- **Approach**:
  1. Read intervention-strategies §5 (manifest schema sketch) for the source design
  2. Draft each ADR section; cite line numbers from intervention-strategies for every design choice
  3. Cross-reference Phase 0's reclassified carriers (which stay `mode: add`, not `mode: inject`) to demonstrate the model boundary
- **Verification**:
  - `git diff --check` clean
  - `python3 tooling/codex/audit_refmap.py verify .` exit 0
  - `python3 tooling/codex/scan_threshold_language.py --ignore-meta-instruction-lines .planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md` exit 0
- **Commit**: `docs(initiative): draft ADR-001 for manifest schema v4 (mode: inject)`
- **Boundary**: ADR is design-only. No code, no manifest changes, no carrier migrations.

### Slice 2 — Worked examples in the ADR

The ADR's design is verified against five representative carriers in an appendix. This slice extends Slice 1's ADR rather than creating a new file.

- **Status**: `[ ]`
- **Type**: planning artifact extension
- **Write set**:
  - `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md` → EDIT (append "Appendix A: Worked Examples" section)
- **Worked examples to include** (one subsection each, fully spec'd):
  - **A.1**: `references/mandatory-initial-read.md` — small additive; pure `section_insert_after` after `<required_reading>`. Show the manifest entry, the modifier's source content, the expected materialized output. (This is Phase 3's pilot target.)
  - **A.2**: `references/agent-contracts.md` — medium additive (36 lines per intervention-strategies §4.3). Show whether one operation suffices or if multiple are needed.
  - **A.3**: `workflows/spec-phase.md` — additive workflow (Phase 5 first wave). Show `include_add` for a modifier reference + `section_insert_after` for `<supporting_reading>` block.
  - **A.4**: `workflows/health.md` — step-level (Phase 6). Show `step_remove` for upstream's removed step + `step_insert_after` for modifier's added step.
  - **A.5**: `bin/lib/state.cjs` — explicit non-example. Show why this carrier must stay `mode: overwrite`. (Demonstrates the boundary the schema does NOT cross.)
- **For each example**, the ADR appendix must include:
  - Current upstream content (cite path; do NOT inline more than ~30 lines)
  - Current modifier overwrite content (cite path; same)
  - Proposed `mode: inject` manifest entry (full JSON, inline)
  - Proposed modifier source files for each operation (cite paths or sketch content)
  - Expected materialized output (sketch the resulting file structure)
  - Edge cases (what happens if upstream renames the anchor? if modifier source is empty? etc.)
- **Verification**: same as Slice 1
- **Commit**: `docs(initiative): add worked-example appendix to ADR-001`
- **Boundary**: The worked examples are illustrative; they do NOT pre-commit to the exact migration approach for those carriers. Phase 3+ will revisit the spec when actually migrating.

### Slice 3 — Add `mode: inject` to AGENTS.md and CLAUDE.md change-class triggers

Phase 0 Slice 5 added the change-class trigger taxonomy. This slice extends it now that `mode: inject` is defined.

- **Status**: `[ ]`
- **Type**: governance carrier change (per AGENTS.md change-class triggers; pre-authorized by this slice spec)
- **Write set**:
  - `AGENTS.md` → EDIT (extend "Change-Class Triggers" subsection added in Phase 0 with a sixth class)
  - `CLAUDE.md` → EDIT (parallel update)
  - `.planning/initiatives/inject-migration/posture-triggers.md` → EDIT (add the sixth class to the operational checklist)
- **Content for AGENTS.md** (append to Change-Class Triggers list):

```markdown
6. **Inject mechanism change** — modifications to `mode: inject` operation kinds, marker conventions, parity_intent semantics, or backward-compat shims. New operation kinds count as inject mechanism changes; new uses of existing operation kinds do not.
```

- **Content for CLAUDE.md** (extend the parallel paragraph): trivial — add a sentence noting the new sixth class is runtime-neutral.
- **Content for `posture-triggers.md`**: append the sixth class with examples
- **Verification**:
  - `git diff --check` clean
  - `audit_refmap verify .` exit 0
  - `scan_threshold_language --ignore-meta-instruction-lines AGENTS.md CLAUDE.md` exit 0
- **Commit**: `docs(governance): add inject mechanism as change-class trigger`
- **Boundary**: governance text only; no contract or operational change

## Exit Criteria (phase boundary)

After Slice 3 commits:

1. All three slices marked `[x]` in this file
2. ADR-001 exists at `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md` with all 10 required sections plus 5-example appendix
3. AGENTS.md and CLAUDE.md include `mode: inject` as a change-class trigger
4. STATE.md → Phase 1 marked `[x]`; advanced to Phase 2

**Operator review gate**: the operator must explicitly approve the ADR before Phase 2 begins. The agent stops here with `paused-for-approval` after Slice 3 commits and surfaces the ADR for review. The operator's approval signal is to invoke the next iteration prompt explicitly (rather than letting the loop auto-advance).

## Phase Boundary Verification

```bash
# Per-slice gates already run; phase-boundary additionally:
git log --oneline --grep "Initiative: inject-migration phase 01" | wc -l   # expect 3
ls .planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md  # exists
grep -c "Inject mechanism change" AGENTS.md CLAUDE.md                       # expect 1+ each
```

State-mutating gates are NOT required at this phase boundary (no contract code; no carrier changes; only docs). Run them only if the operator requests.

## Boundary

- This phase produces NO code. The contract code lives in Phase 2.
- This phase does NOT migrate any carrier. Migration starts in Phase 3 (pilot).
- This phase does NOT modify `OVERLAY-MANIFEST.json` (the schema_version field stays at 3 until Phase 2's contract code can read v4).
- This phase does NOT pre-authorize the worked-example carriers' actual migration. Each migration phase reviews the example and commits to a final approach.

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| ADR worked examples reveal a missing operation kind | medium (we may underestimate) | low (the ADR can be amended in Phase 2 or 3 with operator approval) | Slice 2 explicitly walks 5 carriers; the appendix is the design-stress test |
| ADR design is over-engineered (too many operation kinds; unused complexity) | medium | low | Slice 2 worked examples should each use only 1-2 kinds; if the appendix shows 3+ kinds per carrier, suspect over-design |
| Operator review surfaces a fundamental disagreement with the design | low (the design follows intervention-strategies §5 closely) | high (Phase 2 cannot start) | the ADR cites every design choice; review can be section-by-section; revisions land as ADR-002 (not edits to ADR-001) |
| The worked examples cite content that has changed in upstream since intervention-strategies was written | low (4 days) | low | re-read upstream files at slice-start time; cite by `git show origin/main:<path>` |

## Notes For Future Iterations

- The ADR is a precedent. Future schema changes (v5+) follow the same shape: numbered ADR with worked examples and operator review.
- Slice 2's worked examples become the first targets in Phase 3+. Avoid changing them after the ADR lands; revisit in their own phase.
