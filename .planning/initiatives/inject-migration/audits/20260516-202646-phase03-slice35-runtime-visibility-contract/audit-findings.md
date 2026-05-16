---
reviewer: adversarial-auditor-xhigh (Claude, fresh session)
artifact: Phase 3 Slice 3.5 follow-up diff — harness_modifier/contract/runtime_visibility.py + tooling/codex/tests/test_runtime_visibility.py
base_head: 0c0e0c17343c5dac728bc95dc0b046b3c60e61ce
review_type: contract-surface (GUARDRAILS.md "Reviewer-Mediated Continuation" → `harness_modifier/contract/`)
---

# Verdict block (REVIEWERS.md format)

VERDICT: PASS
REASONING: The diff is the smallest correct fix for the documented blocker. `runtime_visibility.py` previously assumed every manifest-backed surface had a readable `source_path`, but `portable_gsd_contract.normalize_overlay_inject_materializer_entry` normalizes inject specs to `source_path: ""` (line 319), which resolved to `Path(".")` and crashed the canary report. The patch gates `source_path` reads behind `not is_inject and overlay_path is not None` while treating inject entries as overlay-covered (so `overlay_exists` is True from the manifest declaration alone), then reuses the same `inject_operations.verify_inject_state` engine that `portable_gsd_contract.build_materialization_report_for_roots` already calls for `verify-materialized` (lines 898–937) — this structurally precludes divergence between the canary's view and verify-materialized's view of "did the inject land". Verified-inject is mapped to `INTENTIONAL`/`SUB_INJECT_VERIFIED` (counts as `intentional_materialized_carry`); failed-inject is mapped to `UNKNOWN`/`SUB_INJECT_UNVERIFIED`, which `build_parity_assessment` (lines 506–514) already promotes into `dual-runtime-conflict`, which in turn flips `check_dual_runtime_core_alignment` in `harness_canary.py` (lines 297–307) to `issue` — so `--strict` would exit 1 on a failed inject. New per-entry fields (`mode`, `inject_verification`) are purely additive; `harness_canary.py` only consumes the top-level `summary` and `parity_details` (lines 351–353), so no canary edit is needed. The existing pre-flight verification (canary exit 0; verify-materialized exit 0 with `inject_failure_count: 0`; 8/8 runtime-visibility tests OK) corroborates the surface change.
RECOMMENDATION: proceed
EVIDENCE:
- runtime_visibility.py:374–385 — `is_inject` gate + `overlay_exists` short-circuit; non-inject path preserves prior semantics byte-for-byte (compare to pre-diff `overlay_spec is not None and overlay_path.exists()`).
- runtime_visibility.py:397 — overlay-text read gated by `overlay_exists and not is_inject and overlay_path is not None`; the new `and not is_inject` is the only behavior change for the existing path and it is logically necessary.
- runtime_visibility.py:412–429 — inject branch reuses `inject_operations.verify_inject_state` (same engine used by `portable_gsd_contract.build_materialization_report_for_roots` at portable_gsd_contract.py:904), so canary and verify-materialized cannot drift on inject semantics.
- runtime_visibility.py:419–429 — verified inject → `INTENTIONAL`/`SUB_INJECT_VERIFIED`; failed → `UNKNOWN`/`SUB_INJECT_UNVERIFIED`. UNKNOWN reaches canary's strict failure path via build_parity_assessment lines 506–514 → check_dual_runtime_core_alignment at harness_canary.py:297–307.
- runtime_visibility.py:445–467 — entry shape adds `mode` and `inject_verification` keys; existing keys unchanged. harness_canary.py:351–353 reads only top-level summary/parity_details, so the additive shape is safe for the only in-tree consumer.
- portable_gsd_contract.py:295–321 — confirms `mode: inject` materializers normalize `source_path: ""`, which is the root cause being addressed.
- inject_operations.py:1188–1258 — `verify_inject_state` is the existing, reviewer-approved Phase 2 Slice 4 engine; reusing it is the right choice for parity with verify-materialized.
- test_runtime_visibility.py:163–202 — two focused tests cover (a) verified inject without source-path read → INTENTIONAL/SUB_INJECT_VERIFIED, no unknown_live_drift, and (b) missing-marker inject → UNKNOWN/SUB_INJECT_UNVERIFIED with `"missing_marker"` in the note, no crash. Pre-existing 6 tests in the file are unchanged.
- STATE.md:53–54 — blocker #1 names exactly this `runtime_visibility.py` crash and the slice's intent; GUARDRAILS.md:75–82 mandates `adversarial-auditor-xhigh` for `harness_modifier/contract/`, satisfied by this review.
- phases/03-pilot.md:115–125 — phase-boundary verification step explicitly lists `harness_canary.py report . --all-supported --strict` as required; the fix is necessary to clear that gate.

---

# Per-question disposition

## Q1 — Preserves contract for overwrite/add/live-only?

**Yes.** The non-inject path is structurally identical:

- `overlay_spec is None` (live-only): `is_inject = False` → `overlay_path = overlay_root / rel_path` → `overlay_exists` evaluated by `.exists()`. Same as pre-diff.
- `overlay_spec` with `mode in {overwrite, add}`: `is_inject = False` → `overlay_path = Path(spec["source_path"])` → `overlay_exists` evaluated by `.exists()`. Same as pre-diff.
- The new `and not is_inject` guard on line 397 fires only for inject entries, where the previous code would have crashed reading `Path("")`. For all other entries, the predicate evaluates identically to the prior `overlay_exists` alone.

Confidence: high. No behavioral change observed in the four pre-existing tests that exercise overwrite/add/live-only paths (test_build_report_records_scope_and_subclassification_counts, test_build_report_marks_dual_runtime_read_side_when_both_runtimes_exist_without_markers, test_build_report_for_runtime_roots_reads_modifier_and_host_separately, plus the classify-direct unit tests).

## Q2 — Correct to classify verified inject as `intentional materialized carry` via `verify_inject_state`?

**Yes.** For overwrite/add, "intentional carry" means "the overlay's declared content reached live (raw or normalized equal)". For inject, the overlay does not own the full file — it only owns marker-bracketed regions and operation post-states. The morally equivalent "declared post-state reached live" is exactly what `verify_inject_state` asserts under ADR-001 §8 Option V1. Reusing that engine (rather than re-implementing a parallel check or comparing arbitrary overlay source text) keeps the canary and `verify-materialized` symmetric — a verified-inject from one is a verified-inject from the other by construction.

Confidence: high. The alternative (comparing overlay source text to a slice of live) is the wrong shape for inject: there is no whole-file overlay text to compare.

## Q3 — Does failed inject reach `unknown_live_drift` strongly enough for canary/parity?

**Yes.** Path:

1. Failed `verify_inject_state` → `classification = UNKNOWN` (runtime_visibility.py:424).
2. UNKNOWN counts toward `summary["unknown_live_drift"]` (line 347).
3. `build_parity_assessment` adds the runtime to `conflicting_runtimes` when `unknown_live_drift > 0` (lines 506–514).
4. `parity_state` becomes `dual-runtime-conflict` (line 541).
5. `check_dual_runtime_core_alignment` in harness_canary.py sees `parity_state != "dual-runtime-aligned"` and returns `issue` (lines 308–317).
6. `harness_canary.py report . --strict` exits non-zero (per the `--strict` path that already gates on `issue`-status checks).

The failed-verification note also surfaces the per-op `marker_key`, `kind`, and `status` (e.g., `"missing_marker"`, `"anchor_missing"`, `"wrong_position"`) via `failed_inject_verification_summary`, which is the right granularity for a triage-level signal in a JSON report.

Confidence: high.

## Q4 — Acceptably additive entry shape (`mode`, `inject_verification`)?

**Yes.** Two new optional keys per entry:

- `mode`: `"inject" | "overwrite" | "add" | None` (None for non-manifest live-only entries). Pure addition.
- `inject_verification`: structured payload from `inject_verification_payload`, or `None` for non-inject entries and for inject entries with absent live target. Pure addition.

The only in-tree consumer (`harness_canary.py`) reads `parity_state`, `summary`, and `parity_details` from the top of the report, not per-entry fields. Downstream tooling that walks `entries` will see the new keys but will not break unless it strictly schema-validates the entries (no such consumer exists in the codebase). No external consumer is known to exist (this is a repo-local introspection tool).

Confidence: high.

## Q5 — Reason to edit `harness_canary.py` itself?

**No.** Three independent lines of evidence:

1. `harness_canary.py` reads only `parity_state`, `summary`, and `parity_details` from the runtime_visibility report (lines 296, 304–305, 314–315, 323–324, 343, 350–353). All three are computed identically; the new inject branch flows through the same `summary`/`parity_details` plumbing.
2. The pre-flight rerun of `harness_canary.py report . --all-supported --strict` already exits 0 with `parity_state: dual-runtime-aligned` and `unknown_live_drift: 0`, confirming end-to-end correctness without a canary edit.
3. The slice's plan-reviewer-approved write set deliberately excludes canary.py; adding it would be scope-creep without a demonstrated need.

Confidence: high.

---

# What works well

- **Engine reuse, not re-implementation.** Pulling `verify_inject_state` into runtime_visibility — rather than implementing an ad-hoc "is the marker there" check — means the canary view of inject state and the verify-materialized view of inject state cannot drift. This is the right structural choice for a contract-surface change.
- **Symmetry between intentional and unknown.** Verified-inject → `INTENTIONAL`; failed-inject → `UNKNOWN`. Both already flow through the existing summary/parity plumbing; no new aggregation logic is needed, and the failed case correctly propagates to `--strict` exit 1.
- **Two new constants, well-named.** `SUB_INJECT_VERIFIED` / `SUB_INJECT_UNVERIFIED` follow the existing `SUB_*` taxonomy and document the new analytical category honestly.
- **Tests are focused and load-bearing.** The two new tests directly target (a) "no source_path read happens" (the original crash) and (b) "missing marker becomes drift, not a crash". They are the right two test cases for this fix; they would have caught the original `IsADirectoryError`.
- **Typing fix is correct.** `entry_specs_for_family` return type widened from `dict[str, dict[str, str]]` to `dict[str, dict[str, Any]]` because `operations` is `list[dict]`, not a string. Quiet correctness.
- **Slice discipline.** The diff stays within the reviewer-approved write set (runtime_visibility.py + test + STATE + checkpoint), no scope creep into harness_canary.py despite the gate ostensibly being its problem.

# Convergent risks

None observed. The change is structurally narrow and the verification stack converges on a single engine (`verify_inject_state`).

# Steelman residue

- I considered flagging the implicit "inject without live target falls through to `classify()` and lands on `SUB_UNKNOWN_MISSING_LIVE`" as an ambiguity worth a third subclassification (e.g., `SUB_INJECT_TARGET_MISSING`). On reflection that critique does less work than it looked like: `SUB_UNKNOWN_MISSING_LIVE` is exactly the right semantics ("manifest-declared surface absent from live"), the inject-specificity is recoverable from the entry's `mode` field, and adding a third constant for this case would be schema growth without analytical payoff. Dropped.
- I considered flagging that `inject_verification` is `None` for both "non-inject entries" and "inject entries with absent live target" — the same null sentinel for two different reasons. Two-state nulls are a known smell. But the disambiguation is trivial via the new `mode` field (`mode == "inject" and inject_verification is None` → "inject target absent"), and forcing a structured "skipped" payload would add ceremony for a downstream consumer that does not yet exist. Quality-tier observation at best, not blocking.
- I considered whether the failed-verification `note` string ("mode: inject live target failed operation-state verification: ...") might collide with consumers that grep for legacy classify() note prefixes. It does not — those prefixes are stable, and the new prefix is distinct.

# What this audit cannot tell you

- Whether the schema v4 + inject contract is *substantively* correct (that was Phase 1 ADR-001's job, already passed reviewer-mediated review at 2026-05-16T00:39Z and 2026-05-16T00:55Z; and Phase 2 Slice 4 verify engine review at 2026-05-16T03:47Z).
- Whether the larger composite-bootstrap gate's non-pilot baseline failures are the agent's problem (operator triangulation triangulated these as out-of-scope per STATE.md OOS #3, #4 and the 2026-05-16 conditional-PASS).
- Whether the audit_refmap.py exit-1 baseline (6 unclassified items in `.codex/.claude`) is acceptable for commit — that is a guardrails-compliance question already addressed by Required Discipline #8 + the "no new items" check the agent reports satisfying.
- Whether `harness_canary.py` should be split / refactored — out of scope.
