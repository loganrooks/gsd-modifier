Composite note:
- Sections `1-2` are preserved from the completed portion of the first `opus[1m]` reply-only reread attempt.
- Sections `3-6` are a bounded local completion against the same frozen basis `306f1d8` after two Opus continuation attempts stalled before returning final text.
- Failed continuation attempts are preserved in lane evidence and launch truth rather than hidden.

# What The New Route Now Makes More Explicit

Previously the baseline (`95-...baseline-first-slice.md`), the delta (`96-...delta-first-slice.md`), and the typed `v2` registry (`artifacts/03-06`) existed beside each other, but concrete multi-family review had to rebuild the packet from chat memory, local-diff intuition, or one audit subtree's lane record. The landed workflow/wrapper/refresh/contract-test set now carries several things more explicitly:

- **One orchestrated read-walk.** `tooling/portable-gsd/overlay/get-shit-done/workflows/propagation-review.md` binds baseline → delta → registry 03-06 → partial tooling → contextual reread into a single named process (`parse_args → map_the_slice → choose_tools → update_or_hold → output_shape → verification`). The earlier state had each layer but no contract carrying the order.
- **A consistent output contract.** The output template names ten sections (`Trigger`, `Baseline Versus Delta`, `Producers`, `Consumers`, `Narrative Mirrors`, `Runtime And Durable Carriers`, `Updated In This Slice`, `Held With Explicit Boundary`, `Verification`, `Next Route`), so later multi-family reviews inherit a shape rather than reconstructing one.
- **The baseline-versus-delta axis as a live review question.** The workflow requires each important carrier to be classified as `upstream-pristine baseline` / `repo-local delta` / `mixed baseline-plus-delta widening`. That moves the 95/96 split out of orientation prose and into the review's own vocabulary.
- **Tooling partial by contract, not only by habit.** The sovereignty line *"Do not let a clean tool result replace contextual reread."* is now a tested invariant (`test_workflow_reads_baseline_delta_and_names_runtime_gate_tools`). `audit_refmap.py`, `project_uplift.py`, `runtime_visibility.py`, `manifest_install_coherence.py --strict`, and `harness_canary.py report . --strict` are named in the step header as partial-visibility aids with per-tool when-to-use hints rather than as whole-network proof.
- **Read-only default plus explicit write-through handoff.** The skill `gsd-propagation-review/SKILL.md` makes `Default posture is read-only.` load-bearing, keeps `--write-note PATH` as the explicit durable-note flag, keeps `--strict-runtime` as the gate flag for slices that touch live materialization/registry carriers, and explicitly routes uplift-posture movement to `$gsd-uplift-project --write` and seed-posture movement to `$gsd-seed-migration-inventory [--write]` rather than absorbing those specialist responsibilities.
- **Layered reading packet rather than flat startup burden.** `required_reading` (mandatory-read + 95 + 96 + `execution_context` files), `supporting_reading` (registry 03-06 + changed surfaces + current lane artifact), `deeper_reading` (older propagation lanes / long-horizon docs / broader governance docs only when the slice cannot be judged from the first two tiers). That preserves the `.planning/AGENTS.md` §Governance-Doc Progressive Disclosure posture at the workflow level.
- **Registry and governance carry updated in the same motion.** `propagation-audit/39-propagation-review-route-change-triggered-refresh.md` records the route inside the typed family. `artifacts/03` adds the `propagation_review_route_contract` row (families_touched `install_overlay / workflow_output / wrapper / governance_lane / helper`). `artifacts/05` adds three evidence entries (`_impl_98`, `_tests`, `_refresh_39`). `artifacts/06` extends the `change_triggered_slice_refresh` chain through the new route. `AGENTS.md` §Contract Propagation, `.planning/AGENTS.md` §Contract-Propagation Hygiene, `tooling/codex/README.md` §Operator Routes, `CURRENT-STATE.md` §Stable Ground, and `HARNESS-IMPROVEMENT-REGISTER.md` §Active Improvement Families / Uplift / propagation consumer completion all name `$gsd-propagation-review` as the operator-facing route.
- **Overlay ownership typed as `add`.** `OVERLAY-MANIFEST.json` records both `get-shit-done/workflows/propagation-review.md` and `skills/gsd-propagation-review/SKILL.md` as `add`, keeping the `overlay_ownership_contract` add-vs-overwrite typing consistent and the repo-local add surface distinguishable from an upstream override.
- **A focused contract test as the tested frontier.** `tooling/codex/tests/test_propagation_review_route_contract.py` asserts overlay ownership of the two surfaces, the workflow's baseline/delta references, the runtime/install tool names, the sovereignty line, and the skill-side read-only plus handoff language — turning the earlier implicit expectations into five tested invariants.

# Where The Live Route Still Compresses Distinct Jobs

- **Workflow doctrine versus skill doctrine.** The workflow carries process, tool-choice discipline, output shape, and verification obligations. The skill carries invocation, the codex cross-vendor adapter, handoff routing, and the `--write-note` / `--strict-runtime` guidance. The "keep the route hybrid" sentence now lives on both surfaces, the `--strict-runtime` gate is named in both with slightly different framing, and the specialist-handoff rules (uplift, seed-migration) appear only in the skill although they are directly relevant to the workflow's `update_or_hold` step. A reader of either surface alone will build a partial mental model of the route.
- **Baseline/delta prose role versus typed registry row role.** The workflow treats `95` and `96` as `required_reading` and `artifacts/03-06` as `supporting_reading`, which matches their current jobs — baseline/delta are operator-facing family inventories; registry 03-06 are typed declared-contract layers. The live route does not say which surface is load-bearing for a given slice, so there is a live risk of baseline/delta being read as narrative mirrors of the registry rather than as a distinct prose answer to a different question. The `propagation_review_route_contract` row in `03` restates the claim boundary but does not name which baseline/delta family a concrete slice would sit in.
- **Tool output versus update-or-hold partition.** `choose_tools` lists five tools and `update_or_hold` drives the actual neighbor-update partition, but the workflow does not spell out how tool output modifies the `Updated In This Slice` versus `Held With Explicit Boundary` split. The sovereignty line carries the principle; the step interaction carries no explicit doctrine for how a strict-run coherence report or a clean canary report should change the disposition.
- **Route-local note writing versus audit-lane inheritance.** `--write-note PATH` accepts an arbitrary repo path. The workflow does not route durable notes into the existing audit-lane naming (dispositions, change-triggered refreshes, launch-truth, outputs) or into the `.planning/` governance surfaces that already host baseline/delta, so a series of route runs would produce review notes scattered across locations rather than accumulating into one inheritance discipline.
- **Claim-type grammar carry.** Baseline `95`, delta `96`, refresh `39`, `AGENTS.md`, `.planning/AGENTS.md`, `CURRENT-STATE.md`, and `HARNESS-IMPROVEMENT-REGISTER.md` use `[g:r:i]` / `[d:r:i]` / `[e:c+i]` markers. The workflow body and the output-shape template carry none. Durable notes produced through `--write-note PATH` would drop out of the repo's claim-type grammar unless the operator imports it manually.
- **Overlay-ownership class carry.** The tracked overlay manifest pins both surfaces as `add`. The workflow does not surface that its own ownership class is part of the route's contract — a later flip between `add` and `overwrite` is caught only by the focused contract test, not by reading the workflow or the skill.
- **Governance-carry framing.** `$gsd-propagation-review` is named in `AGENTS.md` §Contract Propagation (operator-facing review route for concrete multi-family slices), `.planning/AGENTS.md` §Contract-Propagation Hygiene (operator-facing review route rather than another ad hoc reread packet), `tooling/codex/README.md` §Operator Routes (operator-facing route for contract-changing slices that cross several producer/consumer families), `CURRENT-STATE.md` §Stable Ground (bounded route for later multi-family contract movement), and `HARNESS-IMPROVEMENT-REGISTER.md` §Active Improvement Families (use-then-reread posture). Those five framings remain mutually consistent, but they carry a distinct job compression: governance doctrine carry, operator-facing introduction, and register posture each reach the reader as a slightly different shape of the same route.
- **Contract-test frontier versus governance frontier.** The focused test covers five invariants. It leaves outside its frontier: the output-shape template presence, `--write-note PATH` / `--strict-runtime` support, the refresh `39` back-pointer, the registry-row `families_touched` set, and the `AGENTS.md` / `tooling/codex/README.md` mentions. That reflects a deliberate scoping choice, but several governance-carry surfaces now sit outside the tested frontier.

# How The Route's Progressive Disclosure Should Be Inherited

- **Keep the three-tier packet structure as route doctrine, not one route-local convenience.** `required_reading` should stay reserved for the irreducible startup packet: mandatory initial read, the baseline/delta pair, and the execution-context files that define the live route. `supporting_reading` should remain the normal widening layer for typed registry carriers, changed surfaces, and the active slice artifact. `deeper_reading` should stay genuinely conditional. That structure is one of the clearest advances of this route and should be reused whenever later operator-facing routes risk turning every context surface into startup burden.
- **Keep the workflow as the main doctrine carrier and the skill wrapper thin.** The workflow is the place where route-local process, output shape, tool partiality, and verification belong. The skill should remain the invocation adapter plus explicit handoffs. Where the same doctrine currently appears on both surfaces, later sharpening should move toward one authoritative workflow statement with the wrapper pointing to it rather than duplicating route logic in two places.
- **Keep contextual reread sovereign, but make its escalation path more legible.** The current route says not to let clean tool results replace reread, and it separates supporting from deeper reading. The next inherited form should make escalation more visible too: what kind of ambiguity, conflict, or cross-family movement is enough to justify widening from supporting to deeper reading. That would preserve operator control without reopening the flat all-context startup burden this route just improved.
- **Keep durable notes compact, but stop leaving their placement ambient.** Progressive disclosure applies to outputs too. The note should remain short and route-local rather than turning into another warehouse. But later inheritance should give `--write-note PATH` a cleaner default home and clearer relationship to change-triggered refreshes, dispositions, and governance state so operators do not have to invent storage discipline each time.
- **Preserve the baseline/delta pair as the first interpretive lens.** The route gets more control from reading `95` and `96` first than from treating the typed registry as the only map. That should be inherited beyond this route: begin with the human-readable baseline-versus-delta distinction, then widen into typed registry and tools when the slice needs more precision.

# Neighboring Carriers That Still Deserve Sharpening

- **Primary sharpen candidate: the route-local durable note contract.** The route now has `--write-note PATH`, a strong output shape, and a clear audit family, but it still leaves note destination, naming discipline, and claim-type carry too open. The narrowest high-yield sharpening is to bind those together:
  - say where propagation-review notes normally belong when the caller does not already own a better path
  - say whether route notes should inherit the claim-type grammar directly
  - say how route notes answer back to change-triggered refreshes versus dispositions
- **Second sharpen candidate: the tool-result-to-disposition bridge.** The workflow should say more explicitly how partial tool findings sharpen `Updated In This Slice` versus `Held With Explicit Boundary`. Right now the principle is present, but the disposition bridge is still operator-inferred.
- **Third sharpen candidate: test frontier widening around governance carry.** The current focused test is useful, but one bounded follow-through could widen it just enough to cover the output-shape contract, the note/write flags, and one registry/governance back-pointer without turning the route test into a whole-family test.

# Adjacent Route To Inherit Next

- **Next adjacent route: a bounded harden slice on `propagation-review` itself, not uplift agent-assist yet.** This reread still points first to sharpening the newly landed route before moving into the later `93` family. The best next object is a narrow follow-through that:
  - hardens durable note placement and claim-type carry
  - makes the tool-result-to-disposition bridge more explicit
  - slightly widens the focused contract-test frontier
- **Why this route first.** It raises maintainability and propagation control at the exact surface now meant to prevent missed downstream carriers. If later agent-assist or broader family widening inherits on top of a route whose output placement and disposition bridge are still thinner than they should be, the repo will widen capability faster than it widens control.
- **Held second:** bounded uplift agent-assist remains visible and promising through `93`, but it still belongs after this route-local harden pass rather than in place of it.

# How This Route Should Be Inherited

## Carry Forward

- Keep the baseline/delta pair as required startup context for the route.
- Keep the three-tier packet structure and contextual-reread sovereignty.
- Keep the read-only default and specialist-owner handoffs in the wrapper.
- Keep tool usage explicitly partial and route-local rather than letting clean helper output impersonate whole-network proof.
- Keep the typed registry and governance surfaces moving in the same batch when the route changes.

## Revise Before Widening

- Revise the route so durable note placement is less ambient.
- Revise the route so claim-type carry for durable notes is explicit instead of operator-invented.
- Revise the workflow so tool results connect more clearly to the `Updated In This Slice` versus `Held With Explicit Boundary` partition.
- Revise the focused contract test just enough to cover note/write-path and output-shape carry, not only the current five invariants.
- Revise duplicated doctrine between workflow and wrapper toward one clearer authoritative home.

## Hold For Later

- Hold bounded uplift agent-assist as the later adjacent family rather than folding it into this reread.
- Hold broader pristine-diff, freshness-signal, or compact-prompt propagation work until the operator-facing route itself carries its outputs and dispositions more cleanly.
- Hold any attempt to turn this route into a whole propagation engine. Its value comes from being a bounded operator-facing review path, not from absorbing the rest of the family.
