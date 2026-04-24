Date: 2026-04-22
Status: completed audit output
Basis: phase-01-guardrails-rerun-boundary @ 0ab6040

# Workspace State And Operating-Model Audit

## Current Machine Reading

- [e:c+i] The workspace is no longer operating as a pile of landed slices. It is operating as a governed self-improvement machine with four visible moving parts running at different tempos:
  - an **intervention-proposal chain** (`intervention-proposals/001` through `intervention-proposals/135`) where each contract-moving move lands as a proposal/implementation pair, often paired with a `propagation-audit/NN-change-triggered-refresh` entry on the same commit.
  - a set of **audit subtrees** (`long-horizon-audit/`, `threshold-audit/`, `self-overcoming-audit/`, `harness-improvement-audit/`, `entry-uplift-audit/`, `propagation-audit/`, `review-route-audit/`, `docs-audit/`, `tranche-audit/`, and now `workspace-state-audit/`) that each own one widening lane, one bounded reread, or one change-triggered refresh chain.
  - a **governance spine** under this audit directory (`INDEX.md` -> `ARTIFACT-INVENTORY.md` -> `CURRENT-STATE.md` -> `CURRENT-STATE-TRACE.md` -> `STATUS.md`) with a sharpened role separation documented in [GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md](../../governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md) and [WORKSPACE-AUTHORITY-AND-ORGANIZATION.md](../../governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md).
  - a **durable cross-family register** at [.planning/HARNESS-IMPROVEMENT-REGISTER.md](../../../../HARNESS-IMPROVEMENT-REGISTER.md) that carries improvement families, ownerless concerns, and current bounded next slices outside any one audit subtree.
- [d:r:i] These four parts have distinct lifecycles:
  - proposals move in days
  - audit subtrees move in widening/reread cycles of hours-to-weeks
  - the governance spine moves at the speed of genuine role/responsibility change
  - the register moves when a concern becomes durable past one audit
- [d:r:i] New surfaces have been arriving relatively automatically through three recurring mechanisms:
  - **change-triggered refresh:** a landed slice forces one `propagation-audit/NN-change-triggered-refresh.md`, which names the typed registry rows that moved — the refresh cadence is mechanical, not discretionary
  - **bounded reread:** a landed slice is rechallenged by an external Opus lane, which produces a `launch-truth/`, `output/`, and `disposition/` triple that locks inheritance before further widening
  - **classification carrier landings:** when parity concerns arrive (for example `.codex` vs `.claude`), the first bounded move lands a classification surface rather than a materialization branch, keeping the horizon explicit without consuming later optionality
- [e:c+i] The rerun boundary itself is preserved: `.planning/STATE.md` still reads `stopped_at: Phase 01 pre-rerun boundary prepared`, and the rerun-floor is recomputed as `25` through `28` without being discharged. Source: [.planning/STATE.md:7](../../../../STATE.md:7).

## Horizon Handling Now

- [d:r:i] The workspace already runs on at least four differentiated horizons rather than one flattened future. Forcing them into one model would thin the machine.
- [d:r:i] **Short horizon — immediate bounded slice.** Owned by:
  - the numbered `intervention-proposals/NNN-*-proposal.md` + `intervention-proposals/NNN-*-implementation.md` pair
  - the matching `propagation-audit/NN-change-triggered-refresh.md`
  - the `Immediate Decision Surfaces` and `Next Bounded Move` sections of [CURRENT-STATE.md](../../CURRENT-STATE.md) and the relevant disposition
  - the `Current Bounded Next Slices` block of [HARNESS-IMPROVEMENT-REGISTER.md](../../../../HARNESS-IMPROVEMENT-REGISTER.md)
- [d:r:i] **Medium horizon — near-term family queue.** Owned by:
  - the durable `Active Improvement Families` block of the harness register
  - subtree `README.md` + `../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md` role lines (active lane / active companion / aging companion)
  - the recurring `Keep Explicitly Later` block inside disposition notes (for example the review-route lane-`01` inheritance carries four explicit later families)
- [d:r:i] **Long horizon — doctrine and protected seams.** Owned by:
  - [.planning/LONG-ARC.md](../../../../LONG-ARC.md) for milestone arc, visibility/hosting/support doctrine, and `Protected Bets`
  - root [AGENTS.md](../../../../../AGENTS.md) and [.planning/AGENTS.md](../../../../AGENTS.md) for quality bar, propagation hygiene, claim-type grammar, and launch-truth discipline
  - the provider wrappers [CLAUDE.md](../../../../../CLAUDE.md) and [.planning/CLAUDE.md](../../../../CLAUDE.md) for Claude-side translation of that doctrine
- [d:r:i] **Deferred / held / seed horizon.** Owned by several surfaces that are currently distinct:
  - `.planning/seeds/SEED-NNN-slug.md` with `seed_contract_version: 2` (producer: `plant-seed`, consumer: `new-milestone`, uplift-surfacer: `project_uplift.py`). Currently `no_seed_corpus` per [STATE.md:91](../../../../STATE.md:91)
  - explicit per-proposal deferred notes, e.g. [intervention-proposals/132-codex-claude-installation-parity-audit-deferred-note.md](../../intervention-proposals/132-codex-claude-installation-parity-audit-deferred-note.md)
  - per-disposition `Keep Explicitly Later` blocks (review-route inheritance, entry-uplift parity inheritance)
  - STATE.md `Deferred Items` table (milestone-close residue, currently empty)
  - register `Held Later` and `Ownerless Concerns` sections (register-level durable holds)
- [d:r:i] These horizon types are not interchangeable. A seed is a forward-looking idea with trigger conditions that auto-surfaces at milestone-open. A held-later note is a bounded intra-family hold that a later slice in that same family will resume. A deferred item is a milestone-close residue that crosses milestone boundaries. Doctrine is protected seam material that later planning should preserve rather than reopen.
- [d:r:i] What the machine does well across horizons:
  - change-triggered refresh keeps the typed `v2` registry in tune with landed contract movement without operator memory
  - layered read-packet discipline (`required_reading` / `supporting_reading` / `deeper_reading`) now lands uniformly across `new-project`, `new-milestone`, `ingest-docs`, `health`, `from-gsd2`, `update`, `progress`, `resume-project`, and `uplift-project`
  - the progress/resume-project route now carries uplift posture, held runtime annotation, seed corpus posture, and seed-migration pointer as a live consumer chain rather than as paper contract
- [d:r:i] Where horizon handling is still more implicit than the machine's own pace:
  - there is no single surface that names the four horizon types above and tells a later reader which carrier owns each
  - the "explicit horizon-inheritance policy" concern is still listed as ownerless in [HARNESS-IMPROVEMENT-REGISTER.md:97](../../../../HARNESS-IMPROVEMENT-REGISTER.md:97)
  - the register keeps a `Held Later` list, intervention-proposals hold per-proposal `Keep Explicitly Later`, seeds hold trigger conditions, and STATE.md keeps a `Deferred Items` table — the four carriers are individually sharp but not yet mutually mapped in one place

## Deferred, Held, Seed, And Doctrine Routing

- [d:r:i] A finding currently routes through roughly this sequence, in order of decreasing immediacy:
  1. **Into active state / next-slice routing** when the slice is already the adjacent next move. Carriers: CURRENT-STATE.md `Immediate Decision Surfaces`, STATUS.md `current *` status lines, the proposal/implementation pair, and the matching propagation change-triggered refresh.
  2. **Into audit-family memory** when the finding belongs to one widening lane or bounded reread. Carriers: the relevant subtree `packets/`, `specs/`, `prompts/`, `launch-truth/`, `outputs/`, and `dispositions/` files. Subtree-status register plus canon-absorption protocol govern when that family should graduate into doctrine.
  3. **Into a bounded held-later line** when the finding belongs to a live family but should not be executed in the current slice. Carriers: `Keep Explicitly Later` in dispositions, `Held Later` in the register, explicit `132-*-deferred-note.md` style proposals.
  4. **Into a seed** when the finding is forward-looking, bounded by a trigger condition, and should auto-surface at the next milestone-open rather than now. Carrier: `.planning/seeds/SEED-NNN-slug.md` with vintage `seed_contract_version: 2`. Currently no live seed corpus; the producer/consumer chain is wired but empty.
  5. **Into doctrine** when the finding is durable enough to preserve across multiple intervention families. Carriers: `.planning/LONG-ARC.md`, root/planning `AGENTS.md`, provider wrappers.
- [d:r:i] The workspace already does the first three routes mechanically. Routes 4 and 5 are earned less often but are both present:
  - route 4 is exercised through the seed-family hardening chain (`75`-`92`), even though the live corpus is empty today
  - route 5 is exercised through the quality-bar and propagation-hygiene hardening inside root and planning `AGENTS.md` plus the matching `CLAUDE.md` translations
- [d:r:i] Where routing is still too implicit:
  - a finding arriving from an external lane can land in two or three of these routes at once (for example "later route-translation appetite" is both a held-later inside the review-route disposition and a cross-family concern that could reach doctrine), and the cross-carrier routing is resolved by operator judgment rather than by a named protocol
  - the register's `Held Later` and a disposition's `Keep Explicitly Later` use different vocabulary even though they carry the same type of carry — a later reader needs to know that
  - STATE.md `Deferred Items` is currently empty but semantically overlaps with `Future Carry Forward`, and both now coexist with uplift-memory posture fields. The live re-entry works; the typing does not

## Parallelization And Overlap

- [d:r:i] Parallelization is already earned in four concrete patterns and still ambient in at least one more:
  - **external-lane (Opus) timing overlap:** a long-running external Opus lane creates a usable local-work window. During that window, the machine already runs: propagation change-triggered refreshes, lane-pattern / canon-absorption doctrine edits, subtree-status updates, and launch-ledger entries. The `review-route-audit/` lane-`01` disposition names this pattern explicitly: "external-lane timing created a usable local work window".
  - **sub-agent delegation for narrower uplift packets:** the uplift-assist family (`103`, `104`-`106`) now has two exercised patterns, a narrow route-pointer slice, one runtime-proof, and a classification-packet template. Parent-thread ownership stays on composition-layer judgment; delegation sharpens classification or gap-identification.
  - **change-triggered refresh cadence:** refresh chains `16` through `50` fire off landed slices without blocking the parent thread and without needing an external lane. This is a repeat-parallel pattern, not a one-shot.
  - **bounded reread of the immediately prior landed slice:** `04` (seed-migration detect-only) and `06` (pointer-bridge harden) are reread lanes that run while other families advance. The reread lands durable inheritance notes instead of informal chat memory.
- [d:r:i] Where bounded parallelization is **not** earned:
  - spawning a new widening Opus lane on a still-moving baseline (the launch-truth discipline in both AGENTS files explicitly preserves basis-commit freezing)
  - running substantive edits to the doctrine spine while an external lane reads that same spine as its packet
  - crossing the Phase 01 rerun boundary as a parallelization move — the rerun remains paused, and no audit lane should silently relaunch it
  - delegating composition-layer judgment that should remain parent-thread (uplift-assist family `103` is explicit about this)
- [d:r:i] What still lives as implicit operator skill rather than as named pattern:
  - which administrative/governance/propagation slices belong with a long external lane versus which should wait for the lane return
  - timing-calibrated wait windows: the `Timing estimate` block in [AUDIT-LANE-PATTERN-LIBRARY.md:60-76](../../governance/AUDIT-LANE-PATTERN-LIBRARY.md:60) names the protocol but does not yet pair it with a "while-the-lane-runs companion carry" checklist
  - the rule that a propagation change-triggered refresh and a subtree-status update can travel with a live lane, but a governance-spine role change should not

## Administrative And Governance Carry

- [d:r:i] The current administrative/governance carry that keeps the machine coherent while substantive work lands includes:
  - `python3 tooling/codex/audit_refmap.py verify` after any link-touching edit
  - `python3 tooling/codex/verify_touched_audit_refs.py --staged` before checkpoints
  - `python3 tooling/codex/harness_canary.py report . --strict` after runtime/install-touching slices
  - `propagation-audit/NN-change-triggered-refresh.md` after any contract-carrying slice
  - `../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md` update when a subtree changes force
  - `../../root-support/LAUNCH-LEDGER.md` entry when a material external lane lands
  - `$gsd-propagation-review` for operator-facing multi-family propagation reviews
- [d:r:i] Carry that currently travels well with a long-running external lane:
  - propagation change-triggered refreshes on unrelated landed families
  - subtree-status edits for families not being reread
  - launch-ledger housekeeping on earlier lanes
  - intervention-proposals housekeeping (cross-linking adjacent families)
  - HARNESS-IMPROVEMENT-REGISTER update when a durable improvement family shifts state
- [d:r:i] Carry that should not travel with an external lane:
  - edits to the packet/spec that lane is reading
  - edits to `CURRENT-STATE.md` sections that the lane's inheritance will need to inherit
  - rebase or refmap moves that could invalidate the lane's basis commit
  - governance-role changes to `../../governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md` or `../../governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md`

## What The Current Machine Already Enables

- [d:r:i] Progressive-disclosure governance: INDEX/ARTIFACT-INVENTORY/CURRENT-STATE/CURRENT-STATE-TRACE/STATUS/WORKSPACE-AUTHORITY now carry distinct jobs, and the update rules are codified in [GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md](../../governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md).
- [d:r:i] Durable cross-family carry outside any audit subtree: [HARNESS-IMPROVEMENT-REGISTER.md](../../../../HARNESS-IMPROVEMENT-REGISTER.md) carries active families, ownerless concerns, and next slices without the content needing to live inside one workspace.
- [d:r:i] Machine-checkable invariants: `harness_canary.py report --strict`, `manifest_install_coherence.py --strict`, and `runtime_visibility.py` now carry classified final-runtime truth rather than prose summary.
- [d:r:i] Mechanical propagation: the typed `v2` layered registry plus `propagation-audit/16`-`50` refresh chain keeps compatibility, threshold-helper, verifier-lifecycle, setup, transition, milestone-boundary, first-read, spec, read-packet, initialization, health, update, seed, migration, pointer-bridge, uplift-continuity, and parity-classifier movement visible.
- [d:r:i] Lifecycle carry across entry, execution, closure, and re-entry: verifier (`53`/`54`), transition (`57`/`58`), milestone-boundary (`59`/`60`), first-read consumer (`61`/`62`), spec boundary (`63`/`64`), read-packet (`65`/`66`), initialization/ingest (`67`/`68`), health/migration (`69`/`70`), update (`71`/`72`), and seed consumer (`73`/`74`).
- [d:r:i] Operator-facing pointer bridges with compact disclosure: `progress` and `resume-project` now surface uplift posture, held runtime annotation, seed corpus posture, and seed-migration candidate pointer without flattening them into one notification.
- [d:r:i] Classification carriers for cross-runtime parity: the first `.codex` / `.claude` parity classification carrier (`134`/`135`) keeps Claude-held-annotation explicit without opening a materialization branch.
- [d:r:i] Audit-program infrastructure: [AUDIT-LANE-PATTERN-LIBRARY.md](../../governance/AUDIT-LANE-PATTERN-LIBRARY.md), [AUDIT-CANON-ABSORPTION-PROTOCOL.md](../../governance/AUDIT-CANON-ABSORPTION-PROTOCOL.md), [AUDIT-SUBTREE-AGING-AND-GRADUATION.md](../../governance/AUDIT-SUBTREE-AGING-AND-GRADUATION.md), [AUDIT-SUBTREE-STATUS-REGISTER.md](../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md). These now govern lane shape, canon absorption, aging, and current subtree force.
- [d:r:i] External-lane timing calibration: the launch-truth + timing estimate + post-run calibration triple is codified in [AUDIT-LANE-PATTERN-LIBRARY.md:46-77](../../governance/AUDIT-LANE-PATTERN-LIBRARY.md:46).

## Where The Machine Thins

- [d:r:i] **Horizon-routing policy is not yet one surface.** A finding can land in active state, held-later, seed, deferred, or doctrine. Today a careful operator picks the right carrier by lane memory. Later readers would benefit from one named surface listing the carriers and telling them which type of finding belongs where. The gap is already named as ownerless in [HARNESS-IMPROVEMENT-REGISTER.md:97](../../../../HARNESS-IMPROVEMENT-REGISTER.md:97).
- [d:r:i] **Parallelization is named as pattern but not yet codified as discipline.** The audit-lane library names timing calibration, but does not name what companion work should travel with a live external lane and what should not. The review-route inheritance observed this ambient pattern but did not promote it into lane-pattern-library text.
- [d:r:i] **`CURRENT-STATE.md` is drifting toward warehouse shape again.** Its `Active Baselines` bullet has grown into a long inline chain of intervention-proposal references. The protocol in [GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md:69](../../governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md:69) explicitly warns against this pattern; the surface is close to needing its next split.
- [d:r:i] **Launch-ledger carries `/tmp` paths for earlier probes.** The later CLAUDE.md translation asks for repo-local paths over `/tmp` artifacts when the repo can carry them. Older ledger entries are historical trail, but the habit should not leak into new ones.
- [d:r:i] **Seed corpus is currently empty while the producer/consumer chain has hardened considerably.** Until a real seed lands, the vintage-anchor, operator-facing pointer bridge, and migration-detect-only chain remain exercised on synthetic and held-later evidence rather than on live corpus drift.
- [d:r:i] **Operator norms live in the register, not in compaction/continuation prompts.** The `Current Operator Directive` block in [HARNESS-IMPROVEMENT-REGISTER.md:122-130](../../../../HARNESS-IMPROVEMENT-REGISTER.md:122) has concrete anti-shortcut language; that language is not mirrored in compaction, continuation, or resume-project prompts, so operator directive depends on memory rather than on re-entry carry.

## Governance And Operator Surface Changes

- [d:r:i] One bounded governance change is earned by this audit and should land as a first slice once the return is inherited. Two adjacent changes are ready to be held as queued follow-throughs rather than done in the same slice.
- [d:r:i] **Earned now — add an explicit horizon-routing surface.** Preferred carrier, in order of least new doctrine added:
  - (a) add a new top-level section `Horizon Routing` to [.planning/HARNESS-IMPROVEMENT-REGISTER.md](../../../../HARNESS-IMPROVEMENT-REGISTER.md) naming the four horizon types (active / held-later / seed / deferred / doctrine) and their concrete carriers with one example each
  - (b) alternatively, add `Horizon Routing` to [.planning/AGENTS.md](../../../../AGENTS.md) under `Research And Audit Quality` or `Future-Flexibility Statusing`. This is the more doctrine-weighted route and would make horizon-routing reachable outside this audit workspace
  - (a) carries less doctrine weight and stays register-local. (b) carries more weight and is slower to land
  - **Recommended:** (a) first, and only promote into `.planning/AGENTS.md` once the register-local shape has been exercised on a real finding
- [d:r:i] **Earned now — add a bounded-parallelization section to [AUDIT-LANE-PATTERN-LIBRARY.md](../../governance/AUDIT-LANE-PATTERN-LIBRARY.md).** Shape:
  - name the four already-earned patterns (external-lane overlap; narrower sub-agent delegation with parent composition-ownership; change-triggered refresh cadence; bounded reread)
  - name the four currently-forbidden overlaps (moving packet/spec for a live lane, governance-spine role change during a live lane, refmap move during a live lane, crossing the rerun boundary)
  - name the companion-carry checklist that should travel with a long external lane (propagation refreshes on unrelated families, subtree-status edits on other families, launch-ledger housekeeping, register update for durable shifts)
  - link to the timing-calibration block in the same file so the two are read together
- [d:r:i] **Adjacent — later slice.** If the first two land, revisit:
  - splitting `Active Baselines` in `CURRENT-STATE.md` into a family-keyed block that points into `ARTIFACT-INVENTORY.md` instead of inline chaining references, so the short synthesis stops accreting
  - mirroring the `Current Operator Directive` language from `HARNESS-IMPROVEMENT-REGISTER.md` into the compaction/continuation prompts so the directive survives re-entry without relying on memory
- [d:r:i] **Not earned yet.** Do not mint a new top-level governance file. The current six-file spine plus the audit-program quartet plus the register already carries the jobs; adding a seventh file would dilute role separation rather than deepen it.

## Short Horizon

- [d:r:i] Finish this audit's inheritance:
  - write the lane disposition (`dispositions/01-where-are-we-now-horizon-inheritance-and-parallelization-audit-inheritance.md`)
  - update `CURRENT-STATE.md` `Immediate Decision Surfaces` only with the accepted next moves
  - update `STATUS.md` with the one-line lane-close entry
  - do **not** expand `CURRENT-STATE.md` into a cumulative warehouse during that pass
- [d:r:i] Immediately adjacent bounded slices that were already queued before this audit opened and should still run next, in whichever order the operator chooses:
  - land the review-route helper-backed first slice (helper: `tooling/codex/run_review_reviewer.py`; matching tests; workflow and wrapper follow-through; propagation refresh; one timing-calibrated real acceptance run) per [review-route-audit/dispositions/01-*.md](../../review-route-audit/dispositions/01-gsd-review-route-hardening-audit-inheritance.md)
  - continue the uplift-continuity consumer chain: the next adjacent consumer is `from-gsd2` per [entry-uplift-audit/dispositions/23-*.md:65](../../entry-uplift-audit/dispositions/23-codex-claude-installation-parity-audit-inheritance.md:65)
  - exercise the `134`/`135` classification carrier on a real materialization boundary before any larger `.claude` install widening is reopened

## Medium Horizon

- [d:r:i] Lifecycle-carry follow-through beyond the current bridges (verifier, transition, milestone-boundary, first-read, spec, read-packet, initialization/ingest, health/migration, update, seed). Candidates still open: deeper setup/materialization robustness, cross-family discovery boundaries, token-budget/cost carrier, secret/privacy carrier. Carrier: intervention-proposals chain plus HARNESS-IMPROVEMENT-REGISTER active-family update.
- [d:r:i] Uplift-assist widening after the narrow route-pointer slice, the first docs-governance runtime-proof, the first cross-runtime packet exercise, and the now-landed classified parity carrier. Shape: one more bounded delegation pattern before the composition layer is widened. Parent-thread ownership stays on composition.
- [d:r:i] Propagation family: continue upstream-pristine / repo-local delta split and keep the propagation-review route maturing. Next real work is exercising the route on a multi-family slice rather than further proposal packing.
- [d:r:i] Seed-migration and operator-facing pointer bridge: when real legacy seeds appear, run the specialist detect-only + inspect/write + harden chain on them. Until then, the chain stays exercised on synthetic fixtures.
- [d:r:i] Setup robustness beyond the first harden slice: reinstall durability, updater/frontier movement, standalone compatibility carrier separate from uplift memory.
- [d:r:i] Docs PR transformation and companion-layer landings continue as background medium-horizon work.

## Long Horizon

- [d:r:i] [.planning/LONG-ARC.md](../../../../LONG-ARC.md) remains the doctrine layer for milestone arc, visibility/hosting/support ladder, wrapper plurality, memory-layer distinctions, and protected bets. It is neither frozen roadmap nor ambient aspiration; it is preserve-only seam material. Do not re-litigate it phase by phase.
- [d:r:i] Root [AGENTS.md](../../../../../AGENTS.md) and [.planning/AGENTS.md](../../../../AGENTS.md) carry the long-horizon quality bar: anti-threshold posture, propagation hygiene, launch-truth discipline, claim-type grammar, future-flexibility statusing. [CLAUDE.md](../../../../../CLAUDE.md) and [.planning/CLAUDE.md](../../../../CLAUDE.md) carry the Claude-side translation.
- [d:r:i] Held long-horizon routes that should not be promoted early:
  - cross-repo / npm / `npx` extraction of the harness-modifier layer (`115`) — hold until uplift/cross-runtime/propagation contracts sharpen further
  - `.claude` install/materialization widening — hold until the classified parity carrier is exercised across real materialization boundaries
  - broader multi-provider parity beyond the `.codex` / `.claude` horizon — out of scope here
  - full peer-to-peer room authority as main branch — preserve-only per LONG-ARC
  - public live participation, paid guaranteed access, open creator marketplace — explicit deferrals per LONG-ARC
- [d:r:i] The answer to "one vague orientation vs one concrete doctrine layer vs differentiated horizon types" is explicitly the third. The long horizon already carries a concrete doctrine layer (LONG-ARC plus AGENTS quality bar) **and** a held-route layer (register, deferred notes, per-disposition held-later) **and** a seed layer (empty corpus today). Flattening these into one ambient future would thin the machine.

## Exact Next Moves

- [d:r:i] 1. Write the lane `01` disposition and inherit it into `CURRENT-STATE.md` `Immediate Decision Surfaces`, `STATUS.md`, and the subtree-status register. Timing: same operator sitting as the output landing.
- [d:r:i] 2. Land the earned governance change: add `Horizon Routing` as a new section to [HARNESS-IMPROVEMENT-REGISTER.md](../../../../HARNESS-IMPROVEMENT-REGISTER.md) naming the four horizon types (active / held-later / seed / deferred / doctrine), their carriers, and one routing example each. Pair with an `Ownerless Concerns` cleanup removing the "explicit horizon-inheritance policy" bullet now that it has an owner. Do not promote into `.planning/AGENTS.md` on this slice.
- [d:r:i] 3. Land the earned parallelization change: add `Bounded Parallelization And Overlap` as a new section to [AUDIT-LANE-PATTERN-LIBRARY.md](../../governance/AUDIT-LANE-PATTERN-LIBRARY.md) naming the four earned patterns, the four forbidden overlaps, and a `Companion Carry During A Live External Lane` checklist. Link the new section to the existing `Timing estimate` block.
- [d:r:i] 4. Pair `2` and `3` with one matching `propagation-audit/NN-change-triggered-refresh.md` if either slice moves a contract surface that the typed `v2` registry tracks; otherwise leave the propagation family untouched.
- [d:r:i] 5. Hold explicitly later, inside the disposition `Keep Explicitly Later`:
  - splitting `CURRENT-STATE.md` `Active Baselines` into a family-keyed block pointing into `ARTIFACT-INVENTORY.md`
  - mirroring the `Current Operator Directive` into compaction/continuation prompts
  - promoting horizon-routing into `.planning/AGENTS.md` after one real finding has used the register-local shape
  - cross-repo extraction, broader parity widening, and reopening the rerun
- [d:r:i] 6. Do not spawn another widening external lane on this workspace until `2` and `3` land, so the next widening runs against a cleaner governed baseline.
- [d:r:i] 7. Outside this audit's scope but worth naming here: the already-queued `gsd-review` helper-backed first slice and the next uplift-continuity consumer (`from-gsd2`) remain the adjacent substantive moves.
