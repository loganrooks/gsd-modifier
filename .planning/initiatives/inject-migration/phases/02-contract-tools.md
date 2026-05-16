# Phase 2 — Contract Tools

ID: `02-contract-tools`
Status: `pending`
Dependencies: Phase 1 ADR landed and operator-approved
Approval gates: operator approval before merging contract code (phase exit)

## Objective

Implement the four core inject-handling functions in `harness_modifier/contract/portable_gsd_contract.py` (or sibling modules as the existing structure dictates), add unit tests for each operation kind, ensure backward compatibility with `mode: overwrite` and `mode: add`, and update the manifest's `schema_version` field to support v4 entries (without yet introducing any).

## Rationale

The contract code is the engine that applies and verifies inject operations. Until it exists, no carrier can be migrated to `mode: inject`. Phase 2 is the gating implementation phase.

The implementation must be unit-tested per operation kind because debugging mismatched apply-time vs verify-time behavior in a real carrier migration would be expensive and would conflate the operation's bug with the carrier's content. Unit tests on synthetic content isolate the operation correctness.

## Approach

Six slices, plus an integration verification at phase boundary.

- Slice 1: extend manifest schema reader to recognize `schema_version: 4` and `mode: inject` (no apply-time logic yet; just parse and validate)
- Slice 2: implement `apply_inject_operations` (the apply-time engine)
- Slice 3: implement `extract_inject_markers` (utility for finding GSD_MODIFIER marker regions)
- Slice 4: implement `verify_inject_state` (the verify-time check)
- Slice 5: add unit tests for all 7 operation kinds
- Slice 6: add a backward-compatibility regression test (v3 entries continue to work)

After Slice 6, a phase-boundary state-mutating verification confirms the existing test suite still passes plus the new tests.

## Slice Catalog

### Slice 1 — Schema reader for `schema_version: 4` and `mode: inject`

- **Status**: `[ ]`
- **Type**: contract surface change (per AGENTS.md change-class triggers; pre-authorized by this slice spec)
- **Write set**:
  - `harness_modifier/contract/portable_gsd_contract.py` → EDIT (extend the manifest parser to recognize `schema_version: 4`; add validation for `mode: inject` entries — they must declare `operations: [...]` and each operation must have a recognized `kind`)
  - Possibly `harness_modifier/contract/__init__.py` → EDIT if new module is exposed
  - `harness_modifier/contract/inject_operations.py` → CREATE (new module that defines the operation-kind enum and validation per kind)
  - `tooling/codex/tests/test_inject_schema.py` → CREATE (initial smoke test that a manifest with `schema_version: 4` and a single sample inject entry parses without error)
- **Approach**:
  1. Read existing parser code in `portable_gsd_contract.py` to find where `schema_version` is checked and where mode is dispatched
  2. Add v4 path that delegates to inject-aware validation
  3. Define operation kinds in `inject_operations.py` (matches ADR-001 §3)
  4. Each kind has a JSON-Schema-style validator function `validate_<kind>(op_dict)` that checks required fields exist and have correct types
  5. Add the smoke test
- **Verification**:
  - `git diff --check` clean
  - `python3 -m py_compile harness_modifier/contract/portable_gsd_contract.py harness_modifier/contract/inject_operations.py harness_modifier/contract/__init__.py`
  - `python3 -m unittest tooling.codex.tests.test_inject_schema` exit 0
  - `python3 tooling/codex/audit_refmap.py verify .` exit 0
- **Commit**: `feat(contract): recognize schema v4 and mode: inject (parser only)`
- **Boundary**: parsing only. No apply-time or verify-time logic. The validate-manifest tool reads v4 entries successfully but does NOT yet apply them.

### Slice 2 — Implement `apply_inject_operations`

- **Status**: `[ ]`
- **Type**: contract surface change
- **Write set**:
  - `harness_modifier/contract/inject_operations.py` → EDIT (add `apply_inject_operations(content: str, operations: list[dict], source_resolver: callable) -> tuple[str, list[OperationRecord]]`)
  - `harness_modifier/contract/portable_gsd_contract.py` → EDIT (call `apply_inject_operations` from the materialization codepath when mode == 'inject')
  - `tooling/codex/tests/test_inject_apply.py` → CREATE (one test per operation kind, with synthetic content)
- **Required behavior**:
  - For each operation kind, define and document the apply-time semantics
  - Operations apply in declared order
  - Each operation either succeeds (returns updated content + a record of what was changed) or fails fatally (raises a typed exception with the anchor and the reason)
  - The function is **pure** (does not write files); the caller (in `portable_gsd_contract.py`) is responsible for writing the result
  - Idempotency: re-applying the same operations to the already-applied content produces identical content (markers are recognized; replacement regions are preserved)
- **Verification**: as Slice 1, plus the new test
- **Commit**: `feat(contract): implement apply_inject_operations for 7 operation kinds`
- **Boundary**: the materialization codepath now applies inject operations, but verification doesn't yet check them. Verify-materialized still uses the old (file-existence) check for inject carriers.

### Slice 3 — Implement `extract_inject_markers`

- **Status**: `[ ]`
- **Type**: contract surface change
- **Write set**:
  - `harness_modifier/contract/inject_operations.py` → EDIT (add `extract_inject_markers(content: str) -> dict[str, MarkerRegion]` that finds all `<!-- GSD_MODIFIER:start key:KEY -->` ... `<!-- GSD_MODIFIER:end -->` regions and returns their key + line ranges)
  - `tooling/codex/tests/test_inject_markers.py` → CREATE (tests for: no markers, one marker, multiple markers, nested markers (should fail), unbalanced markers (should fail))
- **Verification**: per slice
- **Commit**: `feat(contract): implement extract_inject_markers utility`
- **Boundary**: utility only. Used by `apply_inject_operations` (already in Slice 2; refactor to use this) and `verify_inject_state` (next slice).

### Slice 4 — Implement `verify_inject_state`

- **Status**: `[ ]`
- **Type**: contract surface change
- **Write set**:
  - `harness_modifier/contract/inject_operations.py` → EDIT (add `verify_inject_state(materialized_content: str, expected_operations: list[dict]) -> VerifyResult`)
  - `harness_modifier/contract/portable_gsd_contract.py` → EDIT (verify-materialized codepath calls verify_inject_state for inject entries)
  - `tooling/codex/tests/test_inject_verify.py` → CREATE (tests for: all operations landed, missing marker, partial application, content drifted in non-marker region (should pass; modifier doesn't own that region))
- **Required behavior**:
  - For `section_replace` ops: marker exists with expected key
  - For `include_add` ops: expected line exists in expected tag region
  - For `step_remove` ops: named step is absent
  - For `step_insert_after` ops: anchor step is followed by inserted step
  - For `block_replace` ops: anchors exist with expected content between
  - For `section_insert_after` ops: marker exists (insertion uses a marker for idempotency)
  - The function does NOT verify content equality (that's the materialization step's job); it verifies operation effects landed
- **Verification**: per slice
- **Commit**: `feat(contract): implement verify_inject_state`
- **Boundary**: verify-materialized for inject entries is now functional. Pilot phase (Phase 3) can use it.

### Slice 5 — Comprehensive operation-kind unit tests

- **Status**: `[ ]`
- **Type**: test addition (lower-discipline; small mechanical fix per AGENTS.md)
- **Write set**:
  - `tooling/codex/tests/test_inject_operations_thorough.py` → CREATE (one suite per operation kind with comprehensive cases: happy path, missing anchor, malformed anchor, ambiguous anchor, idempotency, ordering)
- **Approach**: a thorough exercise of each operation kind to surface edge cases the per-slice tests in Slices 1–4 may have missed
- **Verification**: per-slice gates plus `python3 -m unittest discover -s tooling/codex/tests` (the full test suite) — must pass
- **Commit**: `test(contract): comprehensive unit tests for inject operation kinds`
- **Boundary**: tests only; no behavior change

### Slice 6 — Backward-compat regression test

- **Status**: `[ ]`
- **Type**: test addition
- **Write set**:
  - `tooling/codex/tests/test_inject_back_compat.py` → CREATE (a test that builds a manifest with mixed `mode: overwrite`, `mode: add`, and `mode: inject` entries; runs validate-manifest and verify-materialized; confirms all three modes coexist)
- **Verification**: per-slice gates; `python3 -m unittest discover -s tooling/codex/tests` exit 0
- **Commit**: `test(contract): backward compatibility for mixed-mode manifests`
- **Boundary**: tests only

## Exit Criteria (phase boundary)

After Slice 6:

1. All slices marked `[x]`
2. New module `harness_modifier/contract/inject_operations.py` exists with all four core functions
3. `portable_gsd_contract.py` integrates inject operations into apply and verify codepaths
4. New tests under `tooling/codex/tests/test_inject_*.py` exist and pass
5. Existing tests (full unittest discover) still pass
6. `bash scripts/ci/check-deterministic.sh` exit 0 (state-mutating; phase-boundary authorized; the existing manifest schema is unchanged so the gate's manifest reading still works)
7. Manifest schema_version stays at 3 (no production v4 entries yet; Phase 3's pilot is the first)

**Operator review gate**: the operator reviews the contract code via diff after Slice 6 lands. The agent surfaces the diff for review. Operator approval signal is to invoke the next iteration prompt; without approval, Phase 3 cannot start.

## Phase Boundary Verification

```bash
# State-mutating; authorized at phase boundary only
bash scripts/ci/check-deterministic.sh

# Full unittest run (most thorough check)
python3 -m unittest discover -s tooling/codex/tests

# Confirm new functions are importable
python3 -c "
from harness_modifier.contract.inject_operations import (
    apply_inject_operations, extract_inject_markers, verify_inject_state
)
print('inject_operations module imports correctly')
"
```

## Boundary

- This phase does NOT migrate any carrier to `mode: inject`. The pilot is Phase 3.
- This phase does NOT change `OVERLAY-MANIFEST.json`'s `schema_version` to 4. The bump happens in Phase 3 when the first inject entry lands.
- This phase does NOT modify upstream conversion logic. Upstream's `bin/install.js` is untouched.
- This phase does NOT add any host-matrix scenarios for inject. That's a Phase 6+ concern when richer operations are exercised.

## Note on OOS #3 (installer-block) — Operator Direction 2026-05-16T01:53Z

Per `STATE.md` → Out-Of-Scope Surfaces #3, the upstream installer is currently blocking `bash scripts/ci/check-bootstrap.sh` because of a hooks-classification prompt for 12 pre-existing untracked `.codex/hooks/` files. Operator direction for Phase 2:

- **In scope for Phase 2 verification**: per-slice unit tests on synthetic content (already specified per slice); `bash scripts/ci/check-deterministic.sh` at the phase boundary (manifest reading only; not affected by installer hooks).
- **Out of scope for Phase 2 verification**: `bash scripts/ci/check-bootstrap.sh` (its first step is the blocked installer); full materializer-runtime exercise.
- **Phase 2 contract code does NOT depend on the installer being unblocked**. `apply_inject_operations` and `verify_inject_state` operate on string content; tests inject synthetic strings and assert string outputs. No filesystem materialization in test paths.
- **Resolution of OOS #3 itself is a separate workstream**, to be addressed before Phase 3 (pilot) attempts end-to-end materialization. Options under consideration: (a) mock the installer surface for test purposes; (b) investigate the upstream installer change to unblock the bootstrap chain; (c) accept and document long-term divergence.

This direction supersedes any implicit assumption that Phase 2 boundary verification would re-establish the bootstrap-chain green-state.

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Apply-time and verify-time semantics drift (an operation applies one way, verifies as if it applied another) | medium | high | each operation has both apply and verify tests in Slices 2–4; the smoke test in Slice 6 exercises both end-to-end |
| Idempotency bugs (re-apply changes content) | medium | medium | each operation kind explicitly tested for idempotency in Slice 5 |
| Performance — applying many operations to a large file is O(N²) in the naive implementation | medium | low (workflow files are <2000 lines; even N²=4M is fast) | benchmark in Slice 5 if a real concern emerges |
| Type confusion between operation dicts (parsed JSON) and pythonic structures | medium | low | use `TypedDict` definitions in `inject_operations.py`; tests catch shape mismatches |
| The contract code surface grows large enough that AGENTS.md's contract-change discipline becomes a bottleneck | low (small phase; few changes per slice) | low | adhere to slice boundaries; one operation kind = one slice if needed |

## Notes For Future Iterations

- The 4 core functions are the "API" for the inject mechanism. Future operation kinds added in later phases extend these without changing their signatures.
- Tests in Phase 2 are FOUNDATIONAL: every later phase relies on these functions being correct. Do not skip the comprehensive Slice 5 tests for time pressure.
