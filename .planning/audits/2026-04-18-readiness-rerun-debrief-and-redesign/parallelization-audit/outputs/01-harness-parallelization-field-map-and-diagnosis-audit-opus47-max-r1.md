Date: 2026-04-22
Status: frozen external-lane return

# Harness Parallelization Field Map And Diagnosis

## Domain Split

- [g:r:i] Three fields, not one. Keep these separate:
  - [d:r:i] `vanilla GSD in action`
    - parallelization baked into upstream workflow grammar (wave execution, parallel mappers, classifier fan-outs, background Task agents, cross-phase workstreams)
    - governed mainly by `config.json.parallelization`, wave frontmatter, and per-workflow fan-out rules
  - [d:r:i] `modified harness in action`
    - the same vanilla surface as it travels under `.codex/`, overlay skills, harness-modifier carriers, AGENTS/CLAUDE wrappers, and the launch-truth / timing-estimate / propagation-review / runtime-visibility toolkit
    - governed additionally by root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md) `Delegation And Orchestration`, planning-local [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md), and the repo-local contract-propagation doctrine
  - [d:r:i] `harness-improvement program overlap`
    - how the improvement program itself overlaps audit lanes, external reviewer work, sub-agent delegation, change-triggered refreshes, governance-carry tranches, and implementation on frozen adjacent families
    - governed by [AUDIT-LANE-PATTERN-LIBRARY.md](../../governance/AUDIT-LANE-PATTERN-LIBRARY.md) `Bounded Parallelization And Overlap`, [HARNESS-IMPROVEMENT-REGISTER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/HARNESS-IMPROVEMENT-REGISTER.md) `Horizon Routing`, and the active `intervention-proposals/162-165` semantic split
- [g:r:i] The three fields share vocabulary but not behavior. A `parallelize more` rule in one degrades another. The governing task is classification, boundary naming, and prerequisite disclosure, not one scalar.
- [d:r:i] The strongest representation here is a map of classes, boundaries, and prerequisites rather than one universal rule. The three fields diverge under pressure and later doctrine should preserve the split.

## Vanilla GSD Posture

- [e:c+r:i] Explicit governed parallelization (plan-side, wave-level):
  - [e:c:i] `execute-phase` wave-based parallel execution with intra-wave `files_modified` overlap detection, post-wave hook validation, post-merge test gate, and worktree isolation (`.codex/get-shit-done/workflows/execute-phase.md:334-785`; SDK `phase-runner.ts:579-720`).
  - [e:c:i] Config-surface parallelization knobs: `parallelization.enabled / plan_level / task_level / skip_checkpoints / max_concurrent_agents / min_plans_for_parallel` (`.codex/get-shit-done/templates/config.json:21-28`).
  - [e:c:i] `USE_WORKTREES=false` fallback forces sequential within the main working tree; submodule repos fall back to sequential automatically (`execute-phase.md:85-94`).
- [e:c+r:i] Explicit governed parallelization (lateral / fan-out agents):
  - [e:c:i] `map-codebase` spawns four `gsd-codebase-mapper` agents in parallel with `run_in_background=true`, using a direct-write-to-disk pattern so the orchestrator only collects line counts (`.codex/get-shit-done/workflows/map-codebase.md:101-219`).
  - [e:c:i] `new-project` runs four parallel researcher sessions (`sdk/src/init-runner.ts:4`, `parallelization: true`).
  - [e:c:i] `ingest-docs` spawns one `gsd-doc-classifier` per discovered doc in a single multi-Task message, with sequential fallback for Copilot (`ingest-docs.md:188-207`).
  - [e:c:i] `verify-work -> diagnose-issues` spawns one `gsd-debugger` per UAT gap in parallel on a frozen symptom set (`.codex/get-shit-done/workflows/diagnose-issues.md:86-118`).
  - [e:c:i] `manager` dispatches plan/execute as background `Task(run_in_background=true)` agents while running discuss inline, with a compound "Continue" option enumerating multiple actions at once (`.codex/get-shit-done/workflows/manager.md:56-282`).
  - [e:c:i] `workstreams` provides explicit cross-phase parallel streams with a session-scoped active pointer (`docs/INVENTORY.md:111`, workstream-flag reference).
- [e:r:i] Implied but undernamed / operator-memory-governed parallelization:
  - [d:r:i] The revision loop inside `plan-phase` (planner → plan-checker → revise → plan-checker, up to 3 iterations) is strictly serial, but plan-checker's verification dimensions have disjoint subjects and are bundled into one agent call rather than split.
  - [d:r:i] The post-implementation review family (`code-review`, `secure-phase`, `validate-phase` / `nyquist-auditor`, `ui-review`, `eval-review`, `audit-uat`, `docs-update` verifier) runs one command at a time; each has its own subject and output carrier, and no wave grouping exists across them.
  - [d:r:i] `ai-integration-phase` runs framework-selector → ai-researcher → domain-researcher → eval-planner strictly sequentially (`commands/gsd/ai-integration-phase.md:16-21`); ai-researcher and domain-researcher have disjoint inputs once the framework is chosen.
  - [d:r:i] `autonomous` drives discuss → plan → execute per phase sequentially across a milestone; no cross-phase overlap even when later-phase preparatory research would be safe on a frozen upstream basis.
- [e:r:i] Principled serial (not accidental):
  - [d:r:i] The discuss → research → plan → execute → verify backbone. Each step consumes the prior step's durable output (`CONTEXT.md`, `RESEARCH.md`, `PLAN.md`, `SUMMARY.md`, `VERIFICATION.md`). The SDK `phase-runner.ts` encodes this as one state machine.
  - [d:r:i] Atomic per-task git commits inside `execute-plan.md`: serial within a plan is a deliberate auditability guarantee, not throughput timidity.
  - [d:r:i] Cross-AI review in `review.md` invokes external CLIs sequentially and flags this explicitly as "avoid rate limits"; principled given per-provider keyed quota plus the synthesis step wanting a stable run-home per reviewer (`review.md:172-297`).
- [d:r:i] Accidental / historically inherited serial:
  - [d:r:i] Single `gsd-phase-researcher` per phase. The researcher output is one `RESEARCH.md`, but research questions often partition (domain, integrations, pitfalls, validation strategy); the split-and-synthesize pattern already used in `new-project` and `map-codebase` is not reused here.
  - [d:r:i] Cross-AI review serialization: rate-limits are a real constraint, but per-CLI run-homes and independent stdin-fed prompts are already in place; the "sequential" framing conflates rate-limit pacing with composition ownership.
  - [d:r:i] `audit-uat` reads each phase's UAT.md to build a prioritized list, but reading is done by one agent rather than fan-out plus parent synthesis.
- [d:r:i] Asymmetry vs the modified harness: vanilla GSD treats parallelization as a config-flag plus wave-grammar problem. Overlap discipline beyond the plan wave is implicit; there is no vanilla doctrine corresponding to `Bounded Parallelization And Overlap`.

## Modified Harness Posture

- [e:c+r:i] New opportunities the modifier has opened:
  - [d:r:i] Baseline/delta propagation pair (`intervention-proposals/95`, `96`) partitions review reads: upstream-pristine baseline in one lane, repo-local delta in another, without racing on the same propagation canon.
  - [d:r:i] Detect-only specialist workflows (`uplift-project`, `seed-migration-inventory`, `propagation-review`) default to read-only inspection (`.codex/get-shit-done/workflows/propagation-review.md:1-141`; `workflows/uplift-project.md`; `workflows/seed-migration-inventory.md`). These are safe to run as companion lanes alongside an active main slice.
  - [d:r:i] Frozen durable artifacts (propagation registry v2 pack at `propagation-audit/artifacts/02-06`, runtime-visibility snapshots, `harness_canary.py` reports, `manifest_install_coherence.py` reports) give concurrent readers a stable object without touching live runtime.
  - [d:r:i] Top-level reasoning uplift (`gpt-5.4` `xhigh` for orchestration) plus the research-methodology tier (Codex 5.4 high gathering → xhigh synthesis) give parallel researcher fan-outs more carry per spawn than vanilla profile assumptions.
  - [d:r:i] Launch-truth capture (`capture_launch_truth.py --since`) plus the audit lane scaffolding (opening note / packet / spec / prompt / launch-truth / output / inheritance / comparative disposition / frozen artifacts in [AUDIT-LANE-PATTERN-LIBRARY.md](../../governance/AUDIT-LANE-PATTERN-LIBRARY.md)) make N concurrent external reviewer lanes individually auditable rather than collapsing into folklore.
  - [d:r:i] Change-triggered refresh cadence (`propagation-audit/17-50`) lets mechanical propagation notes land alongside unrelated lanes instead of waiting for a giant catch-up.
- [e:c+r:i] New frictions the modifier introduces:
  - [d:r:i] Top-level orchestration rule forbids recursive GSD call graphs (`AGENTS.md:148-150`). Some naive parallel fan-outs that require nested workflow spawn paths are now illegal; parent thread has to own composition.
  - [d:r:i] Pre-spawn ceremony per agent call: re-read `AGENTS.md`, classify task class, state `agent -> model -> reasoning` mapping, state bounded duration, verify effective launch settings against `~/.codex/state_5.sqlite`, preserve durable launch-truth for doctrine-sensitive work (`AGENTS.md:156-184`). Fan-outs pay this cost per spawn, which thins the "just launch five classifiers in one message" pattern that vanilla `ingest-docs` assumes.
  - [d:r:i] Review-then-disposition gate before committing delegated output (`AGENTS.md:168-178`). Parallel fan-out and parallel disposition are not equivalent; disposition bottlenecks back into the parent thread.
  - [d:r:i] Checkpoint-commit prerequisite before delegating substantial bounded edits (`AGENTS.md:164-167`). Two lanes that want different baselines cannot overlap on the same worktree.
  - [d:r:i] Cross-vendor wrapper translation: `.codex` vs `.claude` ask-question/spawn-agent grammar differs (Claude `Task` + `AskUserQuestion` vs Codex `spawn_agent` + `request_user_input` vs Copilot `vscode_askquestions`; see overlay skill adapters at `harness_modifier/overlay/skills/*/SKILL.md`). An interactive lane that parallels cleanly in Claude Code degrades in Codex.
  - [d:r:i] `.codex/` is the observed basis and `.claude/` is held-annotation (`intervention-proposals/116`, `134`, `135`). Running live parity-driven materialization lanes in parallel across both runtimes is not yet governed.
- [e:c+r:i] New protocol demands:
  - [d:r:i] Launch-truth per doctrine-sensitive spawn, captured to an owning review/disposition carrier before inheriting the return (`AGENTS.md:175-180`; `.planning/AGENTS.md` `Launch-Truth Discipline`).
  - [d:r:i] Timing-estimate ledger per substantial external lane, with post-run calibration note (`../../governance/AUDIT-LANE-PATTERN-LIBRARY.md` `Timing estimate`).
  - [d:r:i] Explicit disposition verb per return: `accept` / `revise` / `park` / `reject`.
  - [d:r:i] Propagation-review route when a slice crosses producer/consumer families (`.planning/AGENTS.md` `Contract-Propagation Hygiene`; `workflows/propagation-review.md`).
  - [d:r:i] Anti-threshold doctrine: do not let parallel reviewer fan-outs collapse into threshold agreement; keep lone high-signal criticism, merely-adequate areas, and later-audit risks visible even without consensus (`tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:344-375`).
- [e:c+r:i] New risks to continuity and quality:
  - [d:r:i] Single-writer governance surfaces (`CURRENT-STATE.md`, `STATUS.md`, `INDEX.md`, `../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md`, `.planning/HARNESS-IMPROVEMENT-REGISTER.md`, `.planning/STATE.md`) can be silently double-updated when multiple background lanes return. Vanilla GSD assumes one orchestrator writer; the harness-improvement program has more independent lanes touching these surfaces.
  - [d:r:i] Background `manager` Task agents running while an operator hand-edits `.planning/` doctrine can miss doctrine updates the reviewer should have read.
  - [d:r:i] Parallel reviewer lanes that merge into consensus synthesis lose adversarial review power. The `Review Consumer Contract` layer guards against this for plan review, not for general audit reviews.
  - [d:r:i] Refmap/topology rewrites (`tooling/codex/audit_refmap.py move` / `retire`) while any lane reads a frozen basis invalidate that lane's paths. Listed as a forbidden overlap in `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md`, but enforcement is by operator memory.
  - [d:r:i] Installer runs (`scripts/setup-portable-gsd.sh`) while any lane treats `.codex/` as frozen truth corrupt that lane's basis. Same enforcement gap.
- [d:r:i] Asymmetry summary vs vanilla GSD:
  - [d:r:i] The modifier broadens overlap governance (companion-carry checklist, timing-estimate recheck, horizon routing) in ways vanilla GSD does not express, which intensifies safe companion-carry overlap.
  - [d:r:i] The modifier sharpens propagation review into a first-class route (`propagation-review.md`, baseline/delta pair, registry v2), which intensifies safe multi-family contract movement.
  - [d:r:i] The modifier pays a per-spawn ceremony cost (launch-truth, model mapping statement, disposition, bounded duration) that thins purely throughput-driven fan-out forms.
  - [d:r:i] The modifier inherits cross-vendor UI asymmetry it has not resolved: interactive parallel lanes degrade more sharply in Codex than in Claude Code because `request_user_input` has no `multiSelect` and Execute-mode strips the prompt entirely.

## Harness-Improvement Program Overlap

- [e:c+r:i] Already governed:
  - [d:r:i] `Bounded Parallelization And Overlap` in [AUDIT-LANE-PATTERN-LIBRARY.md](../../governance/AUDIT-LANE-PATTERN-LIBRARY.md) (lines 77-104) names earned overlap patterns (external-lane overlap with unrelated governance carry; narrower delegated work with parent-thread composition; change-triggered refresh cadence; bounded reread on a frozen slice), forbidden overlaps (editing packet/spec/prompt/basis a live lane is reading; changing governance role surfaces during a live lane; refmap/topology rewrites that invalidate the basis; crossing the Phase 01 rerun boundary while a lane is returning), and the recheck rule tied to timing estimates.
  - [d:r:i] Horizon routing in [HARNESS-IMPROVEMENT-REGISTER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/HARNESS-IMPROVEMENT-REGISTER.md) (lines 48-76) lists five carrier classes (`active bounded slice` / `held later` / `seed` / `deferred` / `doctrine / protected seam` / `audit-family memory`) so concurrent findings flow into different carriers instead of colliding on one surface.
  - [d:r:i] Audit lane scaffolding makes parallel audit lanes reproducible without rebuilding packet/spec/prompt logic. Frozen artifacts (propagation registry, canary reports, runtime-visibility snapshots) give lanes a stable readable object.
  - [d:r:i] Audit-canon absorption and subtree-aging vocabulary (`../../governance/AUDIT-CANON-ABSORPTION-PROTOCOL.md`, `../../governance/AUDIT-SUBTREE-AGING-AND-GRADUATION.md`) route completed lane output into durable doctrine without letting the lane subtree silently grow into canon.
- [e:c+r:i] Still depends too much on operator memory:
  - [d:r:i] Which governance surfaces are single-writer is not enumerated. The companion-carry checklist implies it but does not name the set.
  - [d:r:i] Which bounded sub-agent patterns are safely delegable is emerging through the uplift-assist packet family (`entry-uplift-audit/packets/06-12`), but no cross-family reference yet consolidates "composition-keeping delegation" versus "composition-leaking delegation".
  - [d:r:i] Cross-vendor lane launches (`.codex` vs `.claude`) have a parity classifier (`intervention-proposals/134`, `135`) but no rule for what it means to run two wrappers in parallel on the same basis.
  - [d:r:i] What counts as "frozen basis frozen enough" for a secondary lane (tag? commit? no governance-surface edits? no refmap move?) is implicit in the forbidden-overlap list.
  - [d:r:i] Recheck cadence relies on operator discipline to inspect the lane rather than manufacture filler work.
  - [d:r:i] `Ownerless Concerns` in the register names `how the harness in action... should map and govern parallelization opportunities beyond execution-wave splitting`, explicitly flagging that the in-action map is not yet carried.

## Safe Earned Parallelization

- [d:r:i] Wave-based plan execution when the intra-wave `files_modified` overlap detector returns no intersection and the post-merge test gate is active.
- [d:r:i] Four-way codebase mapping with direct-write-to-disk and confirmation-only return (disjoint focus areas: tech / architecture / quality / concerns).
- [d:r:i] New-project parallel researcher sessions with synthesizer-owned composition.
- [d:r:i] One `gsd-doc-classifier` per ingested planning doc in a single multi-Task message, with sequential fallback for runtimes where subagent completion is unreliable.
- [d:r:i] One `gsd-debugger` per UAT gap on a frozen symptom set and frozen implementation basis.
- [d:r:i] Long-running external reviewer lane plus bounded governance carry on an unrelated audit family (change-triggered refreshes, subtree-status updates, launch-ledger housekeeping, register updates).
- [d:r:i] Bounded reread lane on a frozen landed slice while adjacent unrelated families continue.
- [d:r:i] Detect-only specialist carry (`propagation-review` read-only, `uplift-project` detect-only, `seed-migration-inventory` detect-only) during another active lane, provided none of them writes to the governance surfaces the other lane is reading.
- [d:r:i] `manager`-backed background plan/execute Task agents with inline discuss on the operator terminal, provided each background lane stays inside its phase's files and the operator does not hand-edit `.planning/` doctrine mid-run.

## Promising But Not-Yet-Governed Parallelization

- [d:r:i] Pre-execution research split: decompose `gsd-phase-researcher` into parallel disjoint sub-questions (domain / integrations / pitfalls / validation) on a frozen CONTEXT.md, with parent synthesis into `RESEARCH.md`. Earned only when top-level framing is coherent and sub-questions are genuinely separable. Needs a small packet template equivalent to the one `map-codebase` already uses.
- [d:r:i] Post-implementation review family wave: `code-review`, `secure-phase`, `validate-phase`, `ui-review`, `eval-review`, docs-verifier can fan out on a frozen implementation basis. Each already has its own subject and output carrier. Today they run one command at a time; a bounded "review wave" surface would name the disjoint-output invariant and collect returns through one disposition pass.
- [d:r:i] Cross-AI plan review concurrency: today `review.md` forces sequential because of rate limits, but per-CLI run-homes already exist (`$RUN_HOME/raw/{gemini,claude,codex,coderabbit,opencode}.*`) and rate limits are per-key. A guarded async-parallel variant with per-CLI back-off and the existing synthesis step would preserve adversarial rigor while cutting wall-clock without changing the sequential default.
- [d:r:i] Harness-improvement sub-agent delegation patterns (`packet_assembly`, `classification`, `carrier_gap_identification`, `docs_governance_classification`, `cross_runtime_comparison`): the first three patterns are now exercised (`entry-uplift-audit/packets/06-12`). Running two or more of them in the same tranche on disjoint packet inputs is still operator-memory-governed; a compact reference consolidating "what keeps composition" would remove that dependence.
- [d:r:i] Change-triggered refresh fan-out: when one slice triggers refreshes across several propagation-family rows, the registry v2 layered carriers (`propagation-audit/artifacts/02-06`) can be updated in parallel because the layered shape partitions writes. Not yet named as an earned pattern.
- [d:r:i] Cross-vendor parity audits: run `.codex` and `.claude` parity-classifier passes on the same basis from different lanes. Safe today because `.codex` is observed basis and `.claude` is held annotation; governance for when that holds and when it breaks is not yet explicit.
- [d:r:i] Audit-subtree aging sweeps: several subtrees can be aged / graduated in one tranche on the same repo state because each has its own README status line. Currently done one-at-a-time on operator initiative.

## Likely Coherence And Quality Risks

- [d:r:i] Two `gsd-planner` lanes on the same phase basis without a compaction rule: outputs diverge, one has to be re-read or thrown out. Degrades continuity.
- [d:r:i] `discuss-phase` running while the phase's `CONTEXT.md` is being human-edited: interactive prompt adoption races and the steering brief silently drifts.
- [d:r:i] Parallel writes to single-writer governance surfaces (`CURRENT-STATE.md`, `STATUS.md`, `INDEX.md`, `../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md`, `HARNESS-IMPROVEMENT-REGISTER.md`, `.planning/STATE.md`). Vanilla GSD assumes one orchestrator writer; concurrent audit lanes can both update these and lose the later write.
- [d:r:i] `map-codebase` refresh while `execute-phase` is modifying code: the map is stale the moment it commits.
- [d:r:i] Parallel reviewer fan-out that collapses into consensus synthesis without the `Review Consumer Contract` layer: loses lone high-signal criticism and merely-adequate detection that the repo's anti-threshold doctrine specifically protects.
- [d:r:i] Refmap/topology rewrites (`audit_refmap.py move` / `retire`) while any lane reads a frozen basis: invalidates the lane's paths.
- [d:r:i] Installer runs (`setup-portable-gsd.sh`) while any lane treats `.codex/` as frozen truth: the basis moves under the lane.
- [d:r:i] Crossing the Phase 01 rerun boundary while a lane is still returning on the prior governed baseline: an explicit forbidden overlap in the pattern library and a repeated anti-misread in the governing docs.
- [d:r:i] Background `manager` agents plus concurrent hand-edits of `AGENTS.md`, wrappers, or `.planning/AGENTS.md`: the background agent reads the prior instruction set and acts on stale doctrine.
- [d:r:i] Audit-subtree aging and canon-absorption running in the same tranche that touches the subtrees they classify: the classification output and the subtree state drift.

## Governance And Operator Surface Changes

- [d:r:i] Name single-writer surfaces explicitly. The right carrier is [AUDIT-LANE-PATTERN-LIBRARY.md](../../governance/AUDIT-LANE-PATTERN-LIBRARY.md) `Bounded Parallelization And Overlap`, extended with a `Single-Writer Governance Surfaces` subsection enumerating: `CURRENT-STATE.md`, `STATUS.md`, `INDEX.md`, `../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md`, `HARNESS-IMPROVEMENT-REGISTER.md`, `.planning/STATE.md`, `.planning/ROADMAP.md`, and `.planning/REQUIREMENTS.md`. Later concurrent lanes must route writes through the active-bounded-slice owner rather than the secondary lane.
- [d:r:i] Promote `Ownerless Concerns -> how the harness in action... should map and govern parallelization opportunities` in [HARNESS-IMPROVEMENT-REGISTER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/HARNESS-IMPROVEMENT-REGISTER.md) into a named Active Improvement Family (`Parallelization field map and overlap governance`) carrying this output as its first slice. The family should point at `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md` as the current doctrine carrier and at `parallelization-audit/` as the audit-family memory.
- [d:r:i] Add a compact `Fan-Out Packet` template in a later bounded slice (under `intervention-proposals/`) that preserves the top-level-orchestration rule: one packet, N spawns on disjoint inputs, parent-thread composition disposition. Keep it as a reusable carrier, not inline `AGENTS.md` text.
- [d:r:i] Extend [.codex/get-shit-done/workflows/propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/propagation-review.md) output shape with an optional `Parallelization Impact` section when the triggering slice changes a parallelization-adjacent surface (`execute-phase.md`, `review.md`, `map-codebase.md`, `ingest-docs.md`, `diagnose-issues.md`, `manager.md`, agent-skills matrix, `config.json.parallelization`). This keeps later changes routing through the same propagation family rather than drive-by edits.
- [d:r:i] Add one doctrine line in [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md) naming what makes a frozen basis frozen enough for a secondary lane: explicit commit or tag; no pending governance-surface edits; no refmap move in flight; no installer reinstall in flight; no active Phase 01 rerun touching. Keep it as one layer, not a new master frame.
- [d:r:i] Do not rewrite live workflows in this slice. `execute-phase.md`, `review.md`, `map-codebase.md`, `ingest-docs.md`, `diagnose-issues.md`, `manager.md` stay out of scope; change them only when a later bounded proposal explicitly earns the move.
- [d:r:i] Do not promote horizon routing into `.planning/AGENTS.md` in this slice. Per [workspace-state-audit/dispositions/01](../../workspace-state-audit/dispositions/01-where-are-we-now-horizon-inheritance-and-parallelization-audit-inheritance.md) that promotion is explicitly held later until the register-local shape has proven useful on more real findings.

## Short Horizon

- [d:r:i] Land this field map as `parallelization-audit/outputs/01-*`, route inheritance through `parallelization-audit/dispositions/01-*`, and update the governance spine minimally (`../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md`, `CURRENT-STATE.md`, `STATUS.md`, `INDEX.md`).
- [d:r:i] Carry the three-class taxonomy (`safe earned` / `promising but not-yet-governed` / `likely coherence risk`) into the next adjacent audit lane that asks an overlap question. Do not pre-promote the taxonomy into doctrine before it has been exercised on a second real lane.
- [d:r:i] Keep the cross-vendor wrapper translation asymmetry visible in the register as a held-later parallelization concern; do not try to fix Codex `request_user_input` ergonomics inside this slice.

## Medium Horizon

- [d:r:i] When a bounded proposal under `intervention-proposals/` next touches a parallelization-adjacent surface, route it through `propagation-review` with a `Parallelization Impact` note. This turns the three-class map into a travelling review filter rather than one frozen doctrine statement.
- [d:r:i] Split `Post-Implementation Review Family Wave` and `Pre-Execution Research Split` into bounded follow-through proposals when the rerun boundary has moved and a concrete host-project slice actually wants either. Neither is earned before that trigger.
- [d:r:i] Build out the `single-writer governance surfaces` enumeration through `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md` companion carry; verify it against one real multi-lane tranche before treating it as binding.
- [d:r:i] Exercise at least one more uplift-assist delegation pattern in parallel with a main audit lane to test the `composition-keeping delegation` doctrine under real overlap pressure before consolidating it into a reference surface.
- [d:r:i] Keep cross-AI review sequential-by-default while an async-parallel variant matures in a bounded proposal; do not flip the default without rate-limit backoff tested first.

## Long Horizon

- [d:r:i] Protected futures for parallelization remain open but unforced: stronger harness-in-action parallelization frameworks (review-family wave, research-split packet, cross-vendor parity lane), stronger harness-improvement-program overlap governance (named single-writer set, fan-out packet, delegation-composition reference), stronger propagation-review parallelization-impact carrier. None of these should be pre-committed into doctrine now.
- [d:r:i] Do not let a local throughput win on `execute-phase` silently foreclose the right shape for the broader field. Throughput is one axis; continuity, cross-vendor carry, adversarial review rigor, and single-writer governance are the other axes the repo has already earned.
- [d:r:i] Keep cross-repo extraction (`intervention-proposals/115`, `136`, `137`) and distributability as separate protected futures. Parallelization governance should travel with extraction when it happens, not block it now.
- [d:r:i] Do not collapse the three-field split in `162-165` into one flattened `parallelization doctrine`. The three fields share vocabulary but diverge under pressure; later doctrine should preserve the split.

## Exact Next Moves

1. [d:r:i] Freeze this output at `parallelization-audit/outputs/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1.md`.
2. [d:r:i] Write `parallelization-audit/dispositions/01-*-inheritance.md` with:
   - the three-class taxonomy carried forward
   - the single-writer governance surfaces list as a held-later carry slated for `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md`
   - the `Parallelization Impact` extension to `propagation-review.md` as a held-later carry
   - the fan-out packet template as a held-later carry
   - the `Ownerless Concerns -> Active Improvement Family` promotion in `HARNESS-IMPROVEMENT-REGISTER.md` as the one landed governance move
3. [d:r:i] Update [HARNESS-IMPROVEMENT-REGISTER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/HARNESS-IMPROVEMENT-REGISTER.md) `Active Improvement Families` to carry `Parallelization field map and overlap governance` as a named family, with this lane as its first evidence.
4. [d:r:i] Update [CURRENT-STATE.md](../../CURRENT-STATE.md), [STATUS.md](../../STATUS.md), [INDEX.md](../../INDEX.md), and [AUDIT-SUBTREE-STATUS-REGISTER.md](../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md) so `parallelization-audit/` reads as an active companion subtree with one completed lane rather than a still-open widening lane.
5. [d:r:i] Do not rewrite `execute-phase.md`, `review.md`, `map-codebase.md`, `ingest-docs.md`, `diagnose-issues.md`, `manager.md`, or `config.json.parallelization` in this slice. Those changes belong to later bounded proposals that cite this map as basis.
6. [d:r:i] Do not reopen the Phase 01 rerun boundary. Do not widen into GSD Reflect, telemetry, deployment-feedback, or multi-provider portability beyond `.codex` and `.claude`.
7. [d:r:i] When the next adjacent audit or intervention lane actually encounters a parallelization question, route its judgment through the three-class taxonomy and the single-writer surface list rather than reconstructing the field from chat memory.
