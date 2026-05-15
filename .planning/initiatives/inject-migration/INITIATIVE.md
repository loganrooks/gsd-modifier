# Inject Migration — Master Plan

Date: 2026-05-08 (created); 2026-05-15 (rebuilt around `/goal` + reviewer-mediated checkpoints)
Status: not started (Phase 0 Slice 0)
Authority: governed by [AGENTS.md](../../../AGENTS.md) and [CLAUDE.md](../../../CLAUDE.md); operationalized by [PROTOCOL.md](PROTOCOL.md); bounded by [GUARDRAILS.md](GUARDRAILS.md); reviewer architecture in [REVIEWERS.md](REVIEWERS.md); state tracked in [STATE.md](STATE.md); invocation in [LOOP-PROMPT.md](LOOP-PROMPT.md)

## Mission

Migrate `gsd-modifier`'s overlay model from overwrite-heavy to surgical injection. Make modifier-specific changes by *operations* against well-known anchors in upstream files instead of carrying whole-file post-conversion snapshots. Reduce the overlay's drift surface, eliminate the silent-staleness failure mode, and document the resulting model as a stable extension posture for `gsd-build/get-shit-done`.

## Why This Initiative Exists

Three findings from the 2026-05-08 readiness pass made the case unambiguous:

1. **Modifier carries post-conversion content.** Upstream `bin/install.js:2199-2224` runs `convertClaudeToCodexMarkdown()` at install time, plus 14 other runtime-specific converter families. Modifier overlays live *after* that conversion. Every modifier overwrite goes silently stale on two axes: upstream content changes AND upstream converter rule changes. Concrete evidence: `bin/lib/state.cjs` has a 779-line diff against upstream and is missing upstream's new `computeProgressPercent` from #3242; `agents/gsd-code-fixer.md` has a 269-line diff; `new-project.md` has a 283-line diff.

2. **Three stale-deleted carriers and one stale-deleted workflow** are empirically attested by the bootstrap gate's `hard_failures` output: `skills/gsd-do/SKILL.md`, `skills/gsd-from-gsd2/SKILL.md`, `skills/gsd-plant-seed/SKILL.md`, `workflows/research-phase.md`. The gate currently *tolerates* these (exit 0 despite hard_failures). That tolerance is itself a smell.

3. **The overlay's overwrite pressure decomposes orthogonally.** Of the 22 overwrite-mode workflow files, ~70% are dominated by additive modifier content (`<supporting_reading>` and `<deeper_reading>` blocks plus `@`-include rewrites). ~20% need targeted line patches. ~10% need step-level operations. Only the third truly demands body-level intervention; the other two could be patch-style. The overlay overwrites the additive cases anyway because no patch-style mechanism exists.

The fix is not to refresh the overlay snapshots faster. The fix is to stop carrying snapshots where the change is anchor-targetable.

Read [.planning/readiness/intervention-strategies-2026-05-08.md](../../readiness/intervention-strategies-2026-05-08.md) for the full evidence base. That document underpins every phase below.

## The Model

Three modes, used as follows:

### `mode: inject` (NEW)

For carriers where modifier change is additive or anchor-targetable. The modifier ships a list of *operations* in the manifest entry. At install time, each operation is applied to the upstream file in place, with idempotency markers so re-applying produces the same result.

Operation kinds (initial set; extend as needed in Phase 1):

- `section_insert_after` — insert a content block after a named XML tag (e.g., after `<supporting_reading>`)
- `section_replace` — replace content between matched `<!-- GSD_MODIFIER:start key:KEY -->` and `<!-- GSD_MODIFIER:end -->` markers (idempotent)
- `step_remove` — remove a `<step name="X">...</step>` block from a workflow's `<process>` section
- `step_insert_after` — insert a `<step>` block after a named-step anchor
- `include_add` — add a single `@`-include line inside a named XML tag if not already present
- `include_remove` — remove a single `@`-include line if present
- `block_replace` — replace a block matched by a precise text anchor (start string + end string)

Each operation declares the *anchor* it targets. If the anchor isn't found at apply time, the operation fails and the install reports the failure as a contract violation.

### `mode: overwrite` (existing; kept for genuine replacements)

For carriers where injection cannot apply. Concretely:

- `bin/lib/*.cjs` (5 files) — JavaScript code; no markdown injection model
- Heavy-restructure carriers — workflows where modifier replaces upstream's prose wholesale rather than augmenting it
- Templates with full re-authored content (some, not all)

Each `mode: overwrite` carrier must document its reason in the phase plan that processed it. "Inherited from earlier overlay" is not a sufficient reason.

### `mode: add` (existing; for net-new modifier content)

For modifier-owned content with no upstream analog. This includes:

- Modifier-net-new workflows (`propagation-review`, `seed-migration-inventory`, `uplift-project`)
- The runtime-neutral generator wrapper (`bin/generate-instruction.cjs`)
- Modifier-owned references (`entry-runtime-uplift-continuity.md`, `milestone-boundary-uplift-continuity.md`)
- Reclassified-as-modifier carriers from Phase 0 (the four stale-deleted)

No change required for these; they are already correctly modeled.

## Phase Catalog

11 phases. Each phase is bounded; each phase produces a coherent deliverable; phases land sequentially.

Reviewer-mediated gates replace the formerly operator-gated approval points. See [REVIEWERS.md](REVIEWERS.md) for which reviewer at which gate. Per-phase verification at phase boundary is always `trajectory-verifier` (mandatory).

| # | Phase | Slug | Key deliverable | Reviewer gate | Dependencies |
|---|---|---|---|---|---|
| 0 | Surface cleanup | `00-surface-cleanup` | 4 stale carriers reclassified; change-class triggers in governance; temp handoff deleted | none beyond per-phase | none |
| 1 | Schema foundation | `01-schema-foundation` | ADR for manifest schema v4; operation kind catalog; marker conventions documented | `adversarial-auditor-xhigh` review of ADR-001 (pre-execute + post-execute) | Phase 0 |
| 2 | Contract tools | `02-contract-tools` | `validate_inject_operations`, `apply_inject_operations`, `extract_inject_markers`, `verify_inject_state` implemented in `portable_gsd_contract.py`; unit tests | `adversarial-auditor-xhigh` review of contract diff (pre-commit) | Phase 1 |
| 3 | Pilot | `03-pilot` | One reference (`mandatory-initial-read.md`) migrated to `mode: inject`; bootstrap gate green; both runtimes verify | `adversarial-auditor-xhigh` review of pilot result (post-commit) | Phase 2 |
| 4 | First wave | `04-first-wave-references` | 4 small references migrated (`verification-overrides`, `agent-contracts`, `planner-reviews`, `planning-config`) | none beyond per-phase | Phase 3 |
| 5 | Second wave | `05-second-wave-additive-workflows` | 5 additive-pattern workflows migrated (`spec-phase`, `verify-phase`, `complete-milestone`, `new-milestone`, `ingest-docs`) | none beyond per-phase | Phase 4 |
| 6 | Third wave | `06-third-wave-step-level` | 3 step-level workflows migrated (`health`, `update`, `progress`) — first uses of `step_remove` / `step_insert_after` | `adversarial-auditor-xhigh` review of first new-operation-kind use | Phase 5 |
| 7 | Fourth wave | `07-fourth-wave-large-workflows` | 3 large workflows migrated (`new-project`, `discuss-phase`, `plan-phase`) — DEFERRABLE; cost-benefit may not justify entry | `adversarial-auditor-xhigh` cost-benefit review (enter or skip; VERDICT determines) | Phase 6 |
| 8 | Templates and agents | `08-templates-and-agents` | Evaluate 7 templates + 4 agent .md files; migrate viable; document non-migrated | `adversarial-auditor-xhigh` per-file (migrate or skip; VERDICT determines) | Phase 6 (independent of 7) |
| 9 | Codex skill mirrors | `09-codex-skill-mirrors` | Decide between pre-conversion overlay vs accept-as-is for `skills/gsd-*/SKILL.md` | `adversarial-auditor-xhigh` review of ADR-002 (outcome A vs B) | Phase 8 |
| 10 | Closeout | `10-closeout` | Retrospective; ROADMAP/STATUS updated; AGENTS.md/CLAUDE.md document inject as stable; archive | `trajectory-verifier` initiative-level + `adversarial-auditor-xhigh` retrospective review | all prior |

Each phase has its own plan in `phases/<NN>-<slug>.md` with concrete slice-level detail.

## Verification Strategy

Three tiers of verification.

### Per-slice (every iteration)

Run by the agent in PROTOCOL.md per-iteration flow. Includes:

- `git diff --check` (clean)
- `python3 tooling/codex/audit_refmap.py verify .` (exit 0)
- Slice-specific tests (declared in slice spec — typically 1–3 unit tests or smoke probes)

Slice gates are designed to be fast (under 30s typical) so they can run on every commit without disrupting the loop's rhythm.

### Per-phase (at phase boundary)

Run when the last slice of a phase completes, before marking the phase complete in STATE.md. Includes:

- All per-slice gates re-run on the cumulative diff
- Phase-specific exit criteria from the phase plan
- One of the bigger gates (`check-deterministic.sh` typically; `check-bootstrap.sh` for phases that touch runtime-affecting carriers)

The phase-boundary verification is **state-mutating** in some cases (bootstrap gate writes to `.planning/measurement/`). The phase plan must explicitly authorize the gate run.

### Initiative-level (closeout only)

Run only at Phase 10 closeout, or on operator request:

- Full `check-deterministic.sh` + `check-bootstrap.sh` against the cumulative initiative branch
- Full host matrix (`harness_modifier/closure/host_exercise_matrix.py`) — most expensive; explicitly state-mutating
- All initiative carriers verified under both runtimes
- Contract documentation cross-references checked

## Completion Criteria

The initiative is complete when ALL of the following are true:

1. **`STATE.md → Sentinel` is `INITIATIVE-COMPLETE`**
2. **`STATE.md → Counters → Bootstrap gate hard_failures` is 0**
3. **All 11 phases marked `[x]` in `STATE.md → Phase Progress`** (Phase 7 may be `[~]` for "deliberately deferred" if the operator decides; the closeout phase records the deferral)
4. **All migrated `mode: inject` carriers verify** under both runtimes via `verify-materialized --strict --all-supported`
5. **Manifest schema v4 documented** in `harness_modifier/contract/` plus an ADR
6. **AGENTS.md and CLAUDE.md document `mode: inject`** as a recognized carrier class with a change-class trigger entry
7. **Closeout retrospective written** at `.planning/initiatives/inject-migration/RETROSPECTIVE.md` (created by Phase 10)
8. **Contract code is back-compat** — all pre-existing `mode: overwrite` and `mode: add` entries still validate and verify under v4
9. **Operator final review marks the initiative closed** (a final commit by the operator setting the sentinel and writing a closing checkpoint)

## What Is Out Of Scope

Items deliberately not pursued in this initiative. They may be later initiatives.

- **Forking upstream** — the modifier remains an overlay against upstream `gsd-build/get-shit-done`, not a fork
- **Upstreaming the inject mechanism to `gsd-build`** — that's a separate effort; this initiative produces a modifier-internal mechanism that could later be proposed upstream
- **Migrating non-overlay tooling** — `harness_modifier/` modifier-net-new code is not part of this initiative except where its contract surface needs `mode: inject` support
- **Adding support for new runtimes** beyond the existing `codex` and `claude` profiles
- **Touching `prix-guesser` or other adjacent repos**
- **Building a richer install profile system** (`--minimal`, etc., per upstream #2762) — that's tracked as a long-horizon item in the orientation
- **Integrating with a hypothetical upstream `EXTENDING.md`** — upstream has no such doc; modifier reasons from code inspection
- **Resolving the `gsd-progress` declaration anomaly** (manifest declares `mode: add` but upstream synthesizes the same path) — Phase 0 may surface this; the resolution is part of Phase 0 only if state-mutating verification confirms the bug; otherwise deferred

## How This Initiative Interacts With Existing Surfaces

- **`AGENTS.md` and `CLAUDE.md`**: Phase 0 adds a change-class trigger entry for overlay/contract changes. Phase 10 adds `mode: inject` as a documented stable surface. No other governance edits.
- **`docs/handoff/current.md`**: Phase 0 deletes the temp handoff (delete-after-ingestion has been honored by the orientation + this initiative). Other phases do not edit `current.md` until Phase 10's closeout.
- **`OVERLAY-MANIFEST.json`**: heavily modified across phases. Each modification is in a single slice; backward compat asserted at each step.
- **`harness_modifier/contract/portable_gsd_contract.py`**: extended in Phase 2; touched in later phases only via additive operation kinds. Existing functions preserved.
- **`tooling/codex/tests/`**: extended with inject-mechanism tests in Phase 2; per-carrier smoke tests in later phases.
- **ROADMAP.md / STATUS.md** (project-level GSD): updated by Phase 10 only. The initiative runs as its own track parallel to milestone-level GSD work.
- **`.planning/measurement/`**: may receive new entries from state-mutating gate runs at phase boundaries; no schema change.

## How This Initiative Is Driven

The initiative is **`/goal`-driven** with reviewer-mediated checkpoints. The operator invokes `/goal` once; the runtime fires turns automatically until the goal condition is met. Within turns, the agent advances autonomously through slices; at gates, the agent spawns reviewer agents per [REVIEWERS.md](REVIEWERS.md) and acts on their verdicts.

Operator presence is required only for:

1. Initial `/goal` invocation (the GO signal — see [LOOP-PROMPT.md](LOOP-PROMPT.md))
2. Manual interrupt (`/goal clear` or Ctrl+C) if intervention is wanted
3. Hard-stop responses (5 conditions in [GUARDRAILS.md](GUARDRAILS.md); the goal terminates and the operator addresses the recorded `## Question for operator` in the checkpoint)
4. Final retrospective review after `Sentinel: INITIATIVE-COMPLETE`

Every other former-approval-point is now mediated by `adversarial-auditor-xhigh`, `trajectory-verifier`, `gsd-debugger`, `Explore`, or `Plan` agents. Reviewer verdicts are **advisory + logged** — the operator audits decisions post-hoc via `STATE.md → Reviewer Decisions Log` and the per-slice checkpoints.

Between operator-required events, the agent loops autonomously per [PROTOCOL.md](PROTOCOL.md). The expected operator-presence frequency is roughly: GO signal once, then nothing until a hard-stop or completion.

## How To Start

Open a Claude Code session at `/home/rookslog/workspace/projects/gsd-modifier` (v2.1.139 or later) and paste the `/goal` invocation from [LOOP-PROMPT.md](LOOP-PROMPT.md) (section "Primary: `/goal` Invocation").

The first turn starts at Phase 0 Slice 0 (`00-surface-cleanup`). See [phases/00-surface-cleanup.md](phases/00-surface-cleanup.md) for the slice catalog.

## Cross-References

| Doc | Purpose |
|---|---|
| [.planning/readiness/release-readiness-orientation-2026-05-08.md](../../readiness/release-readiness-orientation-2026-05-08.md) | Initiative-spawning evidence base |
| [.planning/readiness/intervention-strategies-2026-05-08.md](../../readiness/intervention-strategies-2026-05-08.md) | Underlying strategy analysis |
| [.planning/implementation-plans/20260424T082720Z/concrete-plans/004-generator-owner-and-command-contract/](../../implementation-plans/20260424T082720Z/concrete-plans/004-generator-owner-and-command-contract/) | Plan 004 — set Option A precedent for `mode: add` modifier-owned generator wrapper |
| [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](../../../tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json) | The manifest under migration |
| [harness_modifier/contract/portable_gsd_contract.py](../../../harness_modifier/contract/portable_gsd_contract.py) | The contract code under extension |
| [scripts/ci/check-bootstrap.sh](../../../scripts/ci/check-bootstrap.sh) | The bootstrap gate (state-mutating; phase-boundary use) |
| [scripts/ci/check-deterministic.sh](../../../scripts/ci/check-deterministic.sh) | The deterministic gate (faster; per-phase use) |

## Glossary

- **Anchor** — a stable textual marker in an upstream file that an inject operation targets. Examples: `<supporting_reading>` opening tag, `<!-- GSD_MODIFIER:start key:foo -->` comment marker, named-step `<step name="X">`.
- **Carrier** — a single entry in `OVERLAY-MANIFEST.json`. Each carrier has a path, a `parity_tier`, a mode, and per-runtime materializers.
- **Marker** — an HTML-comment idempotency wrapper. `<!-- GSD_MODIFIER:start key:KEY -->` opens; `<!-- GSD_MODIFIER:end -->` closes. Re-applying an operation between markers replaces only the marker-bounded region.
- **Operation** — a single transformation applied during `mode: inject` materialization. Operations have a `kind`, an `anchor`, and a `payload`.
- **`parity_tier`** — describes a carrier's role in dual-runtime parity (`core_required` / `core_adapted` / `runtime_specific`). Orthogonal to mode.
- **`parity_intent`** (proposed; Phase 1) — describes whether per-runtime operations should produce identical effective additions (`outcome_aligned`) or are intentionally divergent (`runtime_independent`).
- **Phase** — a top-level unit of work in this initiative. Each has its own plan and ends with a phase-boundary verification.
- **Slice** — one bounded iteration. Each slice produces one commit with passing verification.
- **Sentinel** — the loop's terminator field in STATE.md (`NOT-STARTED` / `IN-PROGRESS` / `INITIATIVE-COMPLETE` / `ABORTED`).
- **Surface cleanup** (Phase 0) — preparing the worktree for migration: clearing the bootstrap gate's hard_failures, locking governance, removing the temp handoff.

## Risk Inventory (initiative-level)

These are risks the initiative as a whole faces. Per-phase risks live in phase plans.

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Upstream renames an XML tag (e.g., `<supporting_reading>` → `<context_reading>`) breaking inject anchors | medium (upstream is active) | high (operations fail) | apply_inject_operations fails loud on missing anchor; phase plans recommend periodic anchor-presence checks (cheap CI gate, future) |
| Upstream changes converter rules (e.g., `convertClaudeToCodexMarkdown`) such that injected content gets converted unexpectedly | medium | medium | phase 3 pilot tests both runtimes; ongoing waves verify per-runtime |
| Manifest schema v4 design proves insufficient for a real carrier's needs | medium | medium-high | phase 1 ADR is reviewable; phase 2 includes a backward-incompatibility test; phase 3 pilot exercises the model end-to-end before scale |
| Modifier-net-new workflows (propagation-review, etc.) become drift surfaces of their own | low (small set) | low | initiative does not migrate them; their carriers stay `mode: add` |
| Operator interruption or context loss leaves worktree in inconsistent state | high (long initiative) | low if PROTOCOL is followed | PROTOCOL Cold Start step 4 reconciles STATE.md against `git log`; checkpoint files preserve per-iteration history |
| Reviewer agent gives wrong verdict (false PASS); agent proceeds with bad action | low-medium | medium-high | reviewer verdicts are advisory + logged; operator post-hoc audit via STATE.md → Reviewer Decisions Log and per-slice checkpoints; any reviewer-influenced commit carries `Reviewer:` trailer for grep-ability; per-slice commits are atomic rollback units |
| `/goal` evaluator misjudges turn-end status (false completion) | low | high (premature termination) | `[GOAL-EVAL]` line format is exact and parseable; condition string is precise about terminal markers; 300-turn cap is safety floor, not target |
| Reviewer triangulation deadlocks (1 PASS, 1 FAIL) on every gate | very low | high (initiative stalls) | hard-stop with `reviewer-deadlock` reason; operator addresses by revising slice spec or reviewer prompt template |
| A new upstream feature (e.g., #2792 namespace meta-skills) lands during the initiative and changes the architectural assumptions | medium | medium | phase plans keep waves small; closeout phase reviews assumption drift; initiative may pause for re-orientation if a structural change lands |
| `mode: inject` operations produce subtly different content than today's `mode: overwrite` carriers, breaking downstream LLM behavior | low (operations are explicit) | high (silent regression) | per-slice smoke tests; phase 3 pilot's exit criteria includes content-equivalence check |
| Initiative drags on for many sessions, accumulating unobservable drift in this directory | medium | low | every iteration writes a checkpoint; phase boundaries write a phase-summary; STATE.md counters surface progress |

## Sign-Off

This INITIATIVE.md is a contract: the agent operates under it, the operator reviews it. Once Phase 0 begins, edits to this file should be rare and surface-only (typo, link fix). Substantive direction changes mid-initiative require:

1. The operator updating this file
2. The agent re-reading on next iteration
3. STATE.md noting the change in `Notes For The Agent`

The initiative may be ABORTED at any time per the LOOP-PROMPT operator halt signal.
