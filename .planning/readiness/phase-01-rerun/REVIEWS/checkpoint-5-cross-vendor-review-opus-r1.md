# Checkpoint 5 Cross-Vendor Review — Claude Opus R1

**Reviewer:** Claude Opus 4.6 (claude-opus-4-6)  
**Date:** 2026-04-15  
**Subject:** Checkpoint 5 bounded follow-through candidate  
**Governing prompt:** checkpoint-5-bounded-follow-through-cross-vendor-review-prompt.md

---

## Historical Status

- [d:c:i] This review applies only to the pre-reactivation partial Checkpoint 5 bundle. It remains valid as audit evidence, but it is not closure authority for the reactivated Checkpoint 5 scope now governed by [checkpoint-5-reactivated-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-reactivated-launch-spec.md:1).

---

## Verdict

**Closure-ready with one required fix and two recorded caveats.**

The candidate materially solves the three rerun-blocking seams that Checkpoint 4 assigned to Checkpoint 5. The work stayed genuinely bounded — no deferred hardening was smuggled in. The strongest criticism I can make is architectural, not a coverage gap: the overlay materialization design creates a dual-truth maintenance surface that is honest and necessary now but will become a real engineering liability if the overlay file set grows. That liability is tolerable for the current bounded scope but should be recorded explicitly as a known cost rather than silently accepted.

One concrete issue must be fixed before closure: the `capture_launch_truth.py` helper lacks any automated test or smoke-check, which is inconsistent with the repo's own verification honesty rule.

---

## Findings

### Finding 1 — No automated test or smoke-check for capture_launch_truth.py

**Severity: Must fix before closure**

The Track C helper at `tooling/codex/capture_launch_truth.py` is 432 lines of Python that parses CLI arguments, queries sqlite, normalizes sandbox policies, compares requested-vs-effective settings, and renders markdown. It has no test file, no smoke script, and no `--dry-run` or self-test mode. The implementation note at `AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md:21` cites this helper as the durable capture surface, and `WORKFLOW.md:75` tells operators to run it. `AI-GUARDRAILS.md:90` tells agents to use it.

The repo's own verification honesty rule (`AI-GUARDRAILS.md:93-95`) says: "If a command/test/verification step was not run, say so." A helper that is now doctrine-facing and protocol-facing should have at minimum a basic smoke test that proves it can produce correct output against a known input — or an explicit statement that no test exists and why.

This is not asking for full test coverage. It is asking for: can the helper actually run, parse arguments, and produce the expected markdown structure? A single `--help` invocation is not enough because the logic under test is the sqlite → markdown path.

**Required fix:** Either add a minimal smoke test (e.g., a script or pytest file that creates a temp sqlite, inserts a known row, runs the helper, and checks the output contains expected sections), or add an explicit `## Untested Surfaces` note to the implementation note documenting that this helper has no automated validation and explaining why that is acceptable for the current bounded scope. The first option is materially stronger.

### Finding 2 — Overlay/live dual-truth maintenance liability is real but acceptable

**Severity: Record as known cost, not a blocker**

The auditability materialization decision (`AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md:24-26`) is correct: the `.codex/` directory is gitignored, so changes there alone are not auditable or reinstallable. Materializing the touched files into `tooling/portable-gsd/overlay/` so they can be tracked and reinstalled via `scripts/setup-portable-gsd.sh` is the minimum credible response.

I verified that all seven overlay files currently match their live `.codex/` counterparts after `__PROJECT_ROOT__` → repo-path normalization. The `setup-portable-gsd.sh` script (`scripts/setup-portable-gsd.sh:15-31`) does perform the reverse substitution on install. This is currently sound.

The cost: any future edit to these agent or workflow files must be made in both places (or in overlay and then reinstalled), and drift between the two will be silent. The five agent `.toml` files are each 500–1200 lines. The current overlay set is seven files. If this grows to 15–20 files, the maintenance burden becomes a real source of quiet drift.

This is not a closure blocker — the implementation note is honest about it and the checkpoint explicitly deferred broader install pinning. But the cost should be recorded explicitly in the checkpoint closure or STATUS.md as a known carrying cost for later harness work, not just implied by the deferred-items list.

### Finding 3 — Launch-truth fallback capture is honestly weak but adequate

**Severity: Acceptable as-is**

The fallback capture at `AUDITS/checkpoint-5-launch-truth-capture-fallback.md` uses `--latest 3` because the stronger `--since` boundary was not recorded before the worker wave launched. The implementation note (`AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md:30`) labels this as "explicitly fallback-grade evidence." The helper output itself (`checkpoint-5-launch-truth-capture-fallback.md:27`) includes the selection caveat. The `WORKFLOW.md:78` doctrine explicitly marks `--latest N` as weaker evidence.

All three captured rows show consistent settings (`gpt-5.4`, `high`, `never`, `danger-full-access`), and `agent_path` is honestly left unresolved. This is adequate. The protocol documentation in WORKFLOW.md ensures future launches can use the stronger `--since` boundary.

### Finding 4 — Review/closure-pressure changes are substantive, not cosmetic

**Severity: Already strong**

The review prompt changes at `tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:122-126` now ask for "Strongest Justified Criticism," "What Is Merely Adequate," and "Later Audit Failures" — three new first-class review dimensions beyond the previous generic concerns/suggestions structure. The synthesis template at lines 237-253 now has dedicated sections for "Lone High-Signal Concerns," "Merely Adequate Areas," and "Later Audit Risks," preventing those signals from being absorbed into the consensus overlap.

The planner-reviews reference at `tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:10-14` now makes the "must address" category include "any lone high-signal criticism that is well-justified and would create likely later-audit failure if ignored," and line 29 explicitly says "Consensus raises confidence, but lack of consensus does not automatically downgrade a criticism." Lines 33 add: "If you reject a lone high-signal criticism, explain why the criticism is not persuasive; do not dismiss it solely because only one reviewer raised it."

These are real structural changes to review semantics, not wording tweaks. A lone strong criticism can now travel from review through synthesis through planner reread without being diluted by consensus absence at any stage.

### Finding 5 — Worker prompt alignment is complete and consistent

**Severity: Already strong**

All five phase-critical `.toml` worker prompts now contain a consistent `<project_context>` block that:
1. Routes workers to repo-root `AGENTS.md` and `.planning/AGENTS.md` as governing instruction surfaces
2. Routes skill/runtime discovery through `.codex/skills/` and `.codex/get-shit-done/`
3. Explicitly rejects `.claude/skills/`, `.agents/skills/`, `./CLAUDE.md`, and home-level Reflect directories
4. Includes an AGENTS.md enforcement step appropriate to each worker role (research → constraints section, executor → hard constraints during execution, verifier → anti-pattern scanning)

The specific blocks:
- `gsd-phase-researcher.toml:32-43` — instruction surface + AGENTS enforcement for research constraints
- `gsd-planner.toml:40-49` — instruction surface + skill pattern accounting for plans
- `gsd-plan-checker.toml:36-46` — instruction surface + verification of plan compliance
- `gsd-executor.toml:27-39` — instruction surface + AGENTS enforcement as execution hard constraints
- `gsd-verifier.toml:27-37` — instruction surface + skill rules for anti-pattern scanning

This directly addresses the Checkpoint 4 finding that the runtime-authoritative `.toml` prompts were still telling workers to read `./CLAUDE.md` and legacy skill paths.

### Finding 6 — WORKFLOW.md doctrine-sensitive launch section is well-scoped

**Severity: Already strong**

The new `### Doctrine-sensitive worker launches` section at `WORKFLOW.md:69-83` is cleanly bounded to the protocol: record boundary, launch, capture, preserve. It explicitly marks the helper as a "capture aid, not a proof machine" and keeps the epistemic honesty rules (effective from sqlite, requested from operator, missing fields unresolved). The AI-GUARDRAILS.md additions at lines 89-91 are the minimal corresponding agent-facing rules. Neither doc overreaches.

### Finding 7 — Boundedness is genuine

**Severity: Already strong**

The implementation note (`AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md:35-36`) explicitly records that the pass did not reopen broad install pinning, archival provenance replacement, full path-portability hardening, broader branch/worktree redesign, or broad claim-discipline propagation. The one adjacent move — materializing touched runtime files into tracked overlay — is explained as "the smallest credible way to keep the accepted follow-through auditable and reinstallable" and is well-justified given the `.codex/` gitignore reality.

The TASKS.md conditional items R5.4 through R5.7 remain untouched and conditional. No scope creep is visible.

---

## What Is Already Strong

- **Worker prompt alignment** is thorough and consistent across all five phase-critical agents. The reject-list for legacy paths is explicit and the AGENTS.md enforcement step is tailored per worker role rather than copy-pasted generically.
- **Review pressure changes** are structurally meaningful. The three new review dimensions (strongest criticism, merely adequate, later audit failure) and the synthesis preservation of lone high-signal concerns create a genuine path from minority criticism to planner action that did not exist before.
- **Launch-truth helper** is honest about what it can and cannot prove. The distinction between `--since` and `--latest`, the operator-declared vs. effective framing, and the unresolved-field handling are all epistemically clean.
- **Boundedness discipline** is genuinely tight. The implementation note, the deferred-items record, and the TASKS.md conditional structure all work together to make the checkpoint's scope auditable.
- **Overlay materialization** is the right call given the gitignore reality, and the `__PROJECT_ROOT__` placeholder + install script design is mechanically sound.

---

## What Must Change Before Closure

1. **Add a smoke test for `capture_launch_truth.py`** or explicitly document its untested status with a justification for why that is acceptable within the bounded scope. (Finding 1)

---

## What Can Wait Until Later

1. **Overlay/live dual-truth maintenance cost** should be recorded as a known carrying cost in STATUS.md or checkpoint closure notes, but does not need to be solved now. If the overlay file count grows significantly, a dedicated maintenance or reconciliation mechanism becomes warranted. (Finding 2)
2. **Broader `.toml` alignment** beyond the five phase-critical agents is not needed before rerun and was correctly scoped out. (Launch spec non-goal)
3. **Install pinning, provenance hardening, and path-portability** remain correctly deferred. (Implementation note deferred-items record)
4. **A reconciliation or drift-detection script** for overlay ↔ live `.codex/` coherence would be valuable eventually but is not blocking. (Related to Finding 2)
