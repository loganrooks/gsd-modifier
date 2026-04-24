Date: 2026-04-22
Status: first external widening return, lane 01

# Harness Extraction Audit

## Current Extraction Pressure

- [d:r:i] The pressure is no longer only later packaging appetite. Three distinct forces now press on the same field at once, and they would keep pressing even if npm packaging were deferred indefinitely:
  - `scope-leak pressure` — host-project long-horizon carriers (`.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, readiness/rerun canon) get read as if they were harness-uplift horizon carriers merely because both live in `prix-guesser/`. Sources: [136-harness-extraction-escalation-and-scope-boundary-note.md](../../intervention-proposals/136-harness-extraction-escalation-and-scope-boundary-note.md), [workspace-state-audit/dispositions/01-where-are-we-now-horizon-inheritance-and-parallelization-audit-inheritance.md](../../workspace-state-audit/dispositions/01-where-are-we-now-horizon-inheritance-and-parallelization-audit-inheritance.md).
  - `carrier-mass pressure` — the modifier layer now owns 24 overlay workflows, 15 overlay skills, a dozen+ `tooling/codex/` helpers, a typed overlay manifest, a layered propagation registry (`v2` with four JSON artifacts), and a standing self-improvement register. This is materially larger than one-off repo glue. Sources: [101-repo-local-workflow-additions-and-propagation-map-orientation.md](../../intervention-proposals/101-repo-local-workflow-additions-and-propagation-map-orientation.md), [96-repo-local-propagation-delta-first-slice.md](../../intervention-proposals/96-repo-local-propagation-delta-first-slice.md).
  - `governance-doctrine pressure` — the audit subtree now produces durable doctrine (`../../governance/AUDIT-LANE-PATTERN-LIBRARY.md`, `../../governance/AUDIT-CANON-ABSORPTION-PROTOCOL.md`, `../../governance/AUDIT-SUBTREE-AGING-AND-GRADUATION.md`, `HARNESS-IMPROVEMENT-REGISTER.md`) that already speaks to other projects in general, not only to `prix-guesser`.
- [d:r:i] These forces are not uniform. `scope-leak` is the sharpest and most concrete now; `carrier-mass` is substantial but still actively moving; `governance-doctrine` is the most portable in principle but the least urgent to relocate.
- [d:r:i] The pressure does not yet collapse into a single decision. The cross-runtime parity family is still traveling (`134/135` landed one classified carrier, later real materialization exercises still owed), the baseline/delta split only just landed through `95/96`, and the entry-runtime continuity chain is still walking its next consumer (`from-gsd2`). Extracting while these seams are actively moving would harden moving seams into a cross-repo contract.

## Carrier Split

- [d:r:i] `generic harness carriers` — portable to any host repo with only `.codex` / `.claude` / `get-shit-done` runtime assumptions:
  - runtime/install/update/materialization helpers:
    - [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)
    - [tooling/codex/portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py)
    - [tooling/codex/ensure_gsd_sdk_runtime.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/ensure_gsd_sdk_runtime.py)
    - [tooling/codex/manifest_install_coherence.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/manifest_install_coherence.py)
    - [tooling/codex/runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py)
    - [tooling/codex/harness_canary.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/harness_canary.py)
  - overlay content with non-host semantics:
    - overlay workflows whose meaning is harness-composition, not product-flow: `uplift-project.md`, `propagation-review.md`, `seed-migration-inventory.md`, and the reading-control widenings across `progress.md`, `resume-project.md`, `new-project.md`, `new-milestone.md`, `ingest-docs.md`, `health.md`, `update.md`
    - matching skills under [tooling/portable-gsd/overlay/skills/](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/): `gsd-uplift-project`, `gsd-propagation-review`, `gsd-seed-migration-inventory`, `gsd-resume-work`, `gsd-progress`, `gsd-update`, `gsd-from-gsd2`, `gsd-plant-seed`, `gsd-health`, `gsd-explore`, `gsd-review`, `gsd-rigorous-research`, `gsd-do`
    - overlay manifest and reasoning defaults: [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json), `QUALITY_REASONING` in `portable_gsd_contract.py`
  - audit-program infrastructure (doctrine whose semantics are not product-scoped):
    - `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md`, `../../governance/AUDIT-CANON-ABSORPTION-PROTOCOL.md`, `../../governance/AUDIT-SUBTREE-AGING-AND-GRADUATION.md`, `../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md`
    - the anti-threshold posture and `[g|d|o|e:r|c+i:i]` claim-typing vocabulary carried in wrapper files
  - parity and propagation disclosure helpers:
    - `runtime_specific_reference_scan` inside `portable_gsd_contract.verify-materialized`
    - typed propagation registry shape (`v2` artifacts `02–06` under `propagation-audit/artifacts/`)
- [d:r:i] `host-project-specific carriers` — meaningful only because this repo is `prix-guesser`:
  - product-planning canon: `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/STATE.md`
  - readiness/rerun canon and Phase 01 doctrine: `.planning/readiness/`
  - room/game product concepts, Phase 01 pre-rerun boundary narrative
  - audit subtrees whose existence is product-rerun-driven even if their *form* is generic: readiness post-mortems, rerun debrief framing prose
  - host product compact prompt content (currently `tooling/compact-prompts/project.md`) — the *mechanism* is generic, the *content* is host-specific
  - [CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/CLAUDE.md), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md), `.planning/CLAUDE.md`, `.planning/AGENTS.md` — the *wrapper pattern* is generic; the *routing to this repo's canon* is host-specific
- [d:r:i] `shared boundary carriers` — belong in the modifier layer but must read host-project surfaces to function:
  - `project_uplift.py` — inspects `.planning/STATE.md`, `.planning/seeds/`, runtime dirs, writes `.planning/UPLIFT-REPORT.md` and `UPLIFT-MANIFEST.json` into a host-project path. The helper is generic; the *paths* it reads and writes are host-project contract.
  - `audit_refmap.py` — structurally rewrites `.planning/audits/` references; generic machinery, host-governed subtree shape.
  - `seed_migration_inventory.py` — generic specialist, host-project seed corpus.
  - `capture_launch_truth.py`, `capture_runtime_visibility_snapshot.py`, `run_claude_probe.py` — generic capture helpers that write into host-project audit subtrees.
  - the wrapper-read-order pattern carried by `CLAUDE.md` / `AGENTS.md` / `.planning/CLAUDE.md` / `.planning/AGENTS.md`
  - `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md` plus subtree-aging doctrine *as applied to* a host-project's live subtree set
- [d:r:i] The split still blurs in three places and a clean extraction would need to settle each one:
  - `audit-subtree doctrine` blurs generic-vs-shared because the doctrine is universal but its live register (`../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md`) is a host-repo ledger.
  - `propagation-review` blurs because the workflow is generic but `95/96` baseline and delta artifacts reference host-specific overlay paths inside their prose examples.
  - `uplift-project` blurs because the helper is generic but its `.planning/STATE.md` consumer expectations are host-governed.

## What The Standalone Project Should Own

- [d:r:i] `runtime and materialization contract` — one canonical name, one repo, one versioned semantics:
  - the `portable_gsd_contract.py` surface (`validate-manifest`, `capture-pristine-overwrites`, `apply-overlay`, `apply-reasoning-defaults`, `verify-materialized`, `runtime_specific_reference_scan`)
  - the overlay manifest schema and `add`/`overwrite` ownership contract
  - the SDK runtime detection in `ensure_gsd_sdk_runtime.py`
  - the compact-prompt selector mechanism (not its host-specific content)
  - the runtime-visibility helper and the canary helper as live invariants on any host
- [d:r:i] `overlay content whose semantics are composition, not product flow`:
  - uplift composition: `uplift-project.md`, `gsd-uplift-project/`, the reasoning-default map
  - propagation review: `propagation-review.md`, `gsd-propagation-review/`
  - seed specialist: `seed-migration-inventory.md`, `gsd-seed-migration-inventory/`
  - reading-control and read-packet widenings across the re-entry and initialization surfaces listed in `65–72`, held as *overlay deltas* whose content is generic phrasing + typed slots, not host-specific example text
  - `gsd-from-gsd2` migration path
- [d:r:i] `harness doctrine and audit-program infrastructure as a separable doctrine library`:
  - anti-threshold posture and claim-typing vocabulary
  - `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md`, `../../governance/AUDIT-CANON-ABSORPTION-PROTOCOL.md`, `../../governance/AUDIT-SUBTREE-AGING-AND-GRADUATION.md` as templates/rules, not as prix-guesser's live applied ledger
  - `HARNESS-IMPROVEMENT-REGISTER.md` as a template with a host-planted instance, not as a single shared register across repos
- [d:r:i] `compatibility declaration and parity disclosure`:
  - the classified parity carrier (`134/135`) lifted from an `.codex`-only baseline list into a data shape the standalone project owns, so hosts inherit an updated baseline on install
  - the observed-basis posture (`COMPATIBILITY_POSTURE = observed_basis_only`) as an explicit contract rather than a string constant buried in a helper
- [d:r:i] `installer/materialization bridge` — thin by construction (see Installer And Materialization Ownership below):
  - a wrapper that runs upstream `npx get-shit-done-cc` first, then applies the overlay and runs the contract helpers, then emits the materialization report
  - not a replacement for upstream install; not a full `.codex`/`.claude` dual installer
- [d:r:i] `provider wrapper translation` for `.codex` and `.claude`:
  - the `CLAUDE.md` / `AGENTS.md` read-order translation pattern, carried as a template the installer materializes with host-specific routing slots
  - the parity-classifier scan so a `.claude` install emits the same warnings the current `.codex` install does, not a wider claim

## What Should Stay Host-Repo Local

- [d:r:i] All `prix-guesser` product planning and readiness/rerun canon. The standalone project must not adopt `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, `.planning/STATE.md`, `.planning/REQUIREMENTS.md`, or any readiness artifact as doctrine. These are host inputs, not harness inheritance. The `CURRENT-STATE.md` scope correction already names this, and the standalone project must preserve that scope-correction explicitly rather than silently re-import it.
- [d:r:i] The *live applied* audit-subtree register for this repo. The standalone project can ship the *template* and the *rules*, but the `../../governance/AUDIT-SUBTREE-STATUS-REGISTER.md` instance with its current subtree names (`threshold-audit`, `workspace-state-audit`, `entry-uplift-audit`, etc.) stays here because those subtrees exist because of this repo's history.
- [d:r:i] The live `HARNESS-IMPROVEMENT-REGISTER.md` content. Template shape extracts; local pressure rows, ownerless concerns, and current bounded next slices stay with the host.
- [d:r:i] The live `.planning/UPLIFT-REPORT.md`, `.planning/UPLIFT-MANIFEST.json`, and `.planning/seeds/` corpus. These are host-generated artifacts the helpers produce — never harness-owned.
- [d:r:i] The host compact prompt content (`tooling/compact-prompts/project.md` body). The *selector mechanism* moves; the *product-facing phrasing* stays.
- [d:r:i] Audit subtree prose that is specifically about this repo's rerun history, Phase 01 pre-rerun boundary, room/game product questions, or commercialization direction.
- [d:r:i] Host-side wrapper files. The pattern (`CLAUDE.md` points to `AGENTS.md`, `.planning/CLAUDE.md` points to `.planning/AGENTS.md`, reading-order lists) extracts as a template; the actual files stay host-owned because they translate the harness into *this specific host*.

## Installer And Materialization Ownership

- [d:r:i] Ownership is three-layered and the standalone project should make each layer explicit rather than hiding them behind one installer command:
  - `layer 1: upstream GSD runtime` — owned by `get-shit-done-cc` upstream. Installs `.codex/get-shit-done/` (and the `.claude` sibling when that runtime is targeted), ships `docs/INVENTORY.md`, provides the upstream workflow/skill baseline documented in `95-upstream-pristine-propagation-baseline-first-slice.md`. The standalone project does not absorb this and does not pretend to re-implement it.
  - `layer 2: modifier overlay and contract` — owned by the standalone harness project. Owns `portable_gsd_contract.py`, the overlay manifest, the `add`/`overwrite` ownership semantics, `apply-overlay`, `apply-reasoning-defaults`, `verify-materialized` (including `runtime_specific_reference_scan`). Runs *after* layer 1 completes. Does not rewrite upstream files; overlays them with typed ownership.
  - `layer 3: host-project materialization` — owned by the host repo. The host picks the compact-prompt selector, provides the `.planning/` canon the uplift helper reads, owns the wrapper files, owns the host's audit subtree instances. The standalone project hands the host a thin bootstrap (one script, one config file) and does not own host `.planning/` layout.
- [d:r:i] The current `scripts/setup-portable-gsd.sh` already enacts this three-layer flow but calls it one thing. The extracted project should name the layers in the script itself and in the materialization report so hosts can tell where a failure originated.
- [d:r:i] `.codex` versus `.claude` differences live at layer 1, not in the standalone project's installer. The standalone project should:
  - declare which runtimes its overlay currently materializes cleanly (right now: `.codex`)
  - keep `.claude` materialization as a classified held-annotation posture (`HELD_RUNTIME_ANNOTATION_POSTURE = held_annotation` in `project_uplift.py` already carries this shape) rather than claim dual parity
  - emit the parity scan on whichever runtime is targeted, not only the current one
- [d:r:i] Upstream still owns: runtime version, SDK shape, `.codex` vs `.claude` install mechanics, core workflow/skill base set. The standalone project must not reach into those.

## Compatibility Declaration Shape

- [d:r:i] The declaration should be *observed-basis-only* as a first-class contract, not an internal constant. The current `COMPATIBILITY_POSTURE = "observed_basis_only"` and `COMPATIBILITY_HELD_LATER` list in `project_uplift.py` already carry the shape; extraction should promote them into a typed compatibility declaration file that the installer reads and the materialization report echoes.
- [d:r:i] Minimum fields for a credible declaration:
  - `runtime_basis` — the runtime(s) the overlay has been observed to materialize cleanly on, with `.codex` version range captured from the live `.codex/get-shit-done/VERSION` at capture time
  - `runtime_held_annotations` — runtimes recognized but not actively materialized (currently `.claude`), with the held-later note carried explicitly
  - `overlay_schema_version` — the `OVERLAY-MANIFEST.json` schema version (currently `UPLIFT_MANIFEST_SCHEMA_VERSION = 6`)
  - `parity_scan_baseline` — the classified runtime-specific reference baseline from `runtime_specific_reference_scan`
  - `upstream_compatibility_window` — the upstream `get-shit-done-cc` versions the overlay has been verified against, including an explicit `unknown` state rather than a default-accept
- [d:r:i] Declaration semantics should be:
  - `refuse` when upstream runtime is outside the observed basis and no held-annotation applies
  - `warn` when upstream runtime is inside the basis but overlay schema has moved forward
  - `annotate-and-proceed` when a held-annotation runtime is detected
  - `proceed` only when `runtime_basis` matches cleanly
- [d:r:i] The declaration should not claim a support window it has not exercised. `observed_basis_only` is the right floor and should stay visible in the extracted project rather than being quietly replaced with a broader-looking matrix to make the README read better.

## Repo Shape And Distribution Sequence

- [d:r:i] The strongest near-term shape is `separate repo first, no package yet`:
  - extract to its own git repo that imports into a host via a thin bootstrap script committed to the host
  - no npm package, no `npx` installer, no distribution channel beyond `git clone` plus bootstrap
  - lets the carrier split harden against one concrete non-`prix-guesser` host before freezing a package contract
- [d:r:i] `package plus installer` stays explicitly later. npm/`npx` reads as attractive ergonomics but requires the compatibility declaration, the layer boundaries, and the held-annotation posture to be stable enough that a versioned package does not lock the host into stale semantics. None of those are stable yet.
- [d:r:i] `dual-layer shape` (standalone repo as source of truth, package as distribution channel) is the right long shape but only after the second-host exercise. The package should be a thin bootstrap that `git clone`s or vendors the contract helpers, not a full inlined overlay.
- [d:r:i] The repo structure inside the extracted project should preserve the three-layer ownership rather than collapse it:
  - `overlay/` — the current `tooling/portable-gsd/overlay/` contents, minus host-specific compact-prompt content
  - `contract/` — `portable_gsd_contract.py`, `ensure_gsd_sdk_runtime.py`, `manifest_install_coherence.py`, `runtime_visibility.py`, `harness_canary.py`
  - `uplift/` — `project_uplift.py`, `seed_migration_inventory.py`, `audit_refmap.py`
  - `capture/` — `capture_launch_truth.py`, `capture_runtime_visibility_snapshot.py`, `run_claude_probe.py`, `scan_threshold_language.py`
  - `doctrine/` — audit-program infrastructure files as templates, claim-typing reference, anti-threshold posture note
  - `bootstrap/` — the host-facing entry script derived from current `setup-portable-gsd.sh` plus a wrapper-template directory
  - `compatibility/` — the typed compatibility declaration file, parity baseline, held-annotation note
- [d:r:i] Naming: do not reuse `portable-gsd` as the extracted project name if it overlaps with upstream surfaces in unpredictable ways. Pick a name that does not signal ownership of the upstream runtime.

## Migration Sequence

- [d:r:i] `step 0 — hold current packaging appetite.` Do not extract until the parity classifier has been exercised on at least one non-`.codex` materialization boundary, the `from-gsd2` continuity consumer has landed, and the `95/96` baseline/delta pair has absorbed at least one host-independent reread.
- [d:r:i] `step 1 — sharpen the in-place boundary first.` Inside this repo, move the files that already belong in `generic harness carriers` into a single top-level directory with a name that signals extraction intent (e.g. `harness-modifier/`), while leaving them git-tracked here. No new repo yet. This surfaces leaks that today hide behind the `tooling/codex/` + `tooling/portable-gsd/overlay/` split.
- [d:r:i] `step 2 — compatibility-declaration carrier.` Promote `COMPATIBILITY_POSTURE`, `COMPATIBILITY_HELD_LATER`, parity-scan baseline, and the overlay schema version into a single typed file inside `harness-modifier/compatibility/`. Wire the installer to read it. Treat this as the first artifact that will travel unchanged into the standalone repo.
- [d:r:i] `step 3 — second-host dry run inside this repo.` Point `scripts/setup-portable-gsd.sh` at a throwaway sibling directory with no `.planning/` canon and no host wrapper files, and confirm the installer either proceeds with empty host slots or refuses with a legible message. Any blur the dry run exposes goes back into the carrier split before extraction.
- [d:r:i] `step 4 — extract to its own repo.` Copy `harness-modifier/` into a new repo. Replace the in-repo references in `scripts/setup-portable-gsd.sh` with a bootstrap that pins the extracted repo at a tag. Keep `prix-guesser` as the first real host.
- [d:r:i] `step 5 — second real host.` Install into one other repo before considering npm packaging. This is where the carrier split either earns its separation or exposes missed shared-boundary carriers. Do not skip.
- [d:r:i] `step 6 — later.` Reopen the `package plus installer` question only after step 5 has returned clean on at least one non-`prix-guesser` host.

## Held Later

- [d:r:i] npm/`npx` packaging. The `115` route stays explicit but unblessed.
- [d:r:i] A `.claude` full-materialization branch. Current posture stays `held_annotation`; widening is contingent on extraction reaching step 5.
- [d:r:i] A cross-repo shared `HARNESS-IMPROVEMENT-REGISTER.md`. The template extracts; a shared live register does not yet earn a carrier.
- [d:r:i] A cross-repo shared audit-subtree register. Same shape.
- [d:r:i] A support-window claim broader than `observed_basis_only`.
- [d:r:i] Host-project doctrine travel. `LONG-ARC.md`, `ROADMAP.md`, `STATE.md`, readiness/rerun canon, room/game product doctrine — none of these travel with the extracted project at any step.
- [d:r:i] Dual-layer distribution (repo + package). Held until step 5 returns clean.
- [d:r:i] Upstream-runtime absorption. The standalone project never owns `.codex` or `.claude` install mechanics.
- [d:r:i] Provider widening beyond `.codex` and `.claude`. Out of scope for this field map; gemini/opencode/kilo etc. remain outside the extracted project's horizon.

## Exact Next Move

- [d:r:i] Do not extract now. Do not open an npm proposal. Do not split the repo.
- [d:r:i] Land `step 1` only: create a `harness-modifier/` top-level directory inside this repo, move the generic-carrier files into it (leaving shared-boundary helpers with explicit notes about their host-contract reads), and update `scripts/setup-portable-gsd.sh` plus the `tooling/codex/*.py` imports to use the new paths. No semantic changes; path changes only. One commit, matching propagation refresh, governance-trace note.
- [d:r:i] The `step 1` move is the highest-yield local intervention this field map earns because it forces the carrier split to be enacted in the filesystem rather than described in prose, and it surfaces any remaining host-project doctrine leakage into what we currently call modifier code before extraction becomes a cross-repo coordination problem. It also keeps the current in-flight contracts (`134/135` exercise, `from-gsd2`, baseline/delta reread) parallelizable because no extraction has yet hardened their moving seams.
- [d:r:i] After `step 1` lands and its propagation refresh is clean, reopen this lane's `Migration Sequence` at `step 2` (compatibility-declaration carrier). Do not pre-commit to `step 3` through `step 6` from this lane's authority alone.
