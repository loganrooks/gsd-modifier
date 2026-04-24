Date: 2026-04-22
Status: frozen lane return

# Overlay Carrier Rehome Audit

## Extraction Pressure At This Boundary

- [e:c+i] Two extraction slices have already landed: the generic helper rehome under `harness_modifier/contract/` and `harness_modifier/capture/` ([139](../../intervention-proposals/139-harness-modifier-in-place-rehome-step-1-implementation.md)), and the portable compatibility declaration carrier under `harness_modifier/compatibility/` ([141](../../intervention-proposals/141-harness-modifier-compatibility-declaration-carrier-implementation.md)). A standalone harness-modifier project would still inherit only code-side contract/probe helpers plus one declaration from that footing — the operator-visible harness behavior still lives in overlay workflows, skills, references, templates, and compact-prompts.
- [e:c+i] The current overlay is materially larger than one-off glue. `OVERLAY-MANIFEST.json` already typifies ~80 entries split between `add` (modifier-owned) and `overwrite` (upstream-derived) ownership, and it spans workflows (`uplift-project`, `propagation-review`, `seed-migration-inventory`), skills (`gsd-uplift-project`, `gsd-propagation-review`, `gsd-seed-migration-inventory`, plus re-entry/health/update/progress/resume/from-gsd2 wrappers), references (`mandatory-initial-read`, `entry-runtime-uplift-continuity`, `milestone-boundary-uplift-continuity`), and two `tooling/compact-prompts/` entries.
- [e:c+i] The pressure is not `can we move some of this`; it is that the next slice has to keep three ownerships explicit at once — generic harness carry, shared-boundary carry, and host-repo-local content — while not widening into repo split, npm/`npx` packaging, or a bulk overlay gesture. Sources: [136](../../intervention-proposals/136-harness-extraction-escalation-and-scope-boundary-note.md), [137](../../intervention-proposals/137-harness-extraction-field-map.md), [142](../../intervention-proposals/142-harness-modifier-overlay-carrier-rehome-next-proposal.md).
- [d:r:i] The live pressure that sharpens this boundary now is scope leak: co-located host planning doctrine gets read as harness doctrine when both live under the same repo tree (136). Every overlay carrier that embeds a concrete audit-workspace path inside its `required_reading` / `supporting_reading` / route block is already a carrier with leak risk, independent of any filesystem move.

## Harness-Horizon Versus Host-Horizon Split

- [d:r:i] Harness-uplift horizons for this lane are:
  - near-term: one more bounded in-repo slice under `harness_modifier/overlay/` that carries generic workflow/skill/reference carriers while keeping installer/materialization contract stable
  - medium-term: standalone-project preparation — boundary design, second-host dry run, installer shape
  - later: repo split and later distribution channel
- [d:r:i] Host-horizon surfaces stay `prix-guesser` product-planning: `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/LONG-ARC.md`, `.planning/STATE.md`, and readiness/rerun canon. Those remain contextual inputs unless a slice deliberately crosses into product planning, rerun coupling, or entry/re-entry integration per [WORKSPACE-AUTHORITY-AND-ORGANIZATION.md](../../governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md) and [GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md](../../governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md).
- [d:r:i] This lane is not a product-planning lane. It is a harness-carry lane. Product canon enters only when a shared-boundary carrier explicitly routes through it — for example, the compact-prompts body that today names Phase 01 readiness paths.
- [d:r:i] Keep `.codex` and `.claude` as the primary runtime horizon for this lane, anchored to the declared `compatibility_posture = observed_basis_only` with `.claude` as held annotation ([declaration.json](../../../../../harness_modifier/compatibility/declaration.json)). Multi-provider widening stays later-lane.

## Carrier Classification

### Generic harness carriers (can travel largely as-is, subject to text cleanup)

- [d:r:i] Skill adapters whose semantics are not tied to host product:
  - `skills/gsd-uplift-project/SKILL.md`
  - `skills/gsd-propagation-review/SKILL.md`
  - `skills/gsd-seed-migration-inventory/SKILL.md`
  - `skills/gsd-progress/SKILL.md`
  - `skills/gsd-resume-work/SKILL.md`
  - `skills/gsd-health/SKILL.md`
  - `skills/gsd-update/SKILL.md`
  - `skills/gsd-from-gsd2/SKILL.md`
  - `skills/gsd-rigorous-research/SKILL.md` and its three `references/*` children
- [d:r:i] Workflow mechanism shells whose instructions read as generic uplift/propagation/migration flow:
  - `workflows/uplift-project.md` (mechanism: helper-backed detect/write, routed layering)
  - `workflows/propagation-review.md` (mechanism: baseline/delta/typed-registry triage against a trigger surface)
  - `workflows/seed-migration-inventory.md` (mechanism: detect/write migration packet)
- [d:r:i] Harness-side reference carriers whose text is not host-product doctrine:
  - `references/entry-runtime-uplift-continuity.md` (pending text audit)
  - `references/milestone-boundary-uplift-continuity.md` (pending text audit)
  - `references/mandatory-initial-read.md` (overwrite-mode; must stay compatible with upstream baseline)
- [d:r:i] Declaration already staged generic: `harness_modifier/compatibility/declaration.json` travels unchanged.

### Shared-boundary carriers (move with care; explicit contract)

- [d:r:i] `OVERLAY-MANIFEST.json` itself. It typifies `add` vs `overwrite` ownership — that schema is generic and must travel with a standalone project, but the exact roster reflects what this repo currently tracks. Treat the schema/mechanism as generic and the roster entries as follow-through bookkeeping per move.
- [d:r:i] The installer spine `scripts/setup-portable-gsd.sh` and its `PRIX_COMPACT_PROMPT_FILE` + `.codex.local/compact-prompt.txt` override levers. The materialization mechanism (helper-backed `ensure_gsd_sdk_runtime` → `capture-pristine-overwrites` → `apply-overlay` → `apply-reasoning-defaults` → `verify-materialized`) is generic. The `prix-`-prefixed env var and repo-specific paths are host-local surface on a generic contract.
- [d:r:i] Any overlay file whose mechanism is generic but whose `required_reading` / `supporting_reading` / route text currently embeds concrete audit-workspace paths:
  - `workflows/propagation-review.md` embeds `@__PROJECT_ROOT__/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/95-...` and `96-...` plus four audit-workspace `propagation-audit/artifacts/*.json` references in supporting reading
  - `workflows/uplift-project.md` route step names `103-uplift-agent-assist-patterns.md`, `06-uplift-docs-governance-classification-packet-template.md`, and `08-uplift-carrier-gap-identification-packet-template.md` under `entry-uplift-audit/`
  - `workflows/propagation-review.md` step `choose_tools` names `python3 tooling/codex/audit_refmap.py` and `python3 tooling/codex/project_uplift.py` — the helper rehome in 139 has already moved some of these behind shims, but the workflow text still refers to the old `tooling/codex/*` home for the non-rehomed shared-boundary helpers (`audit_refmap.py`, `project_uplift.py`, `seed_migration_inventory.py`)
- [d:r:i] Compact-prompt entries `tooling/compact-prompts/project.md` and `tooling/compact-prompts/readiness.md`. The *mechanism* (a named compact prompt selected via env/selector) is generic. The *body* of `readiness.md` names `.planning/readiness/phase-01-rerun/*` and a Phase 01 rerun packet — that is host-product doctrine, not harness doctrine. The body of `project.md` also explicitly preserves `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md` and similar planning canon. Mechanism-vs-content must split before this tranche moves.
- [d:r:i] Parity scan baseline rules inside `declaration.json` that anchor on `gsd-local-patches/`, `agents/gsd-debugger.toml`, and `get-shit-done/workflows/update.md`. The schema and classification grammar are generic; the specific rule set reflects what this host has observed so far.

### Host-repo-local carriers (do not travel)

- [d:r:i] `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/` content — all intervention proposals, audit subtrees, dispositions, launch-truth, and registry artifacts referenced from overlay text should not travel as overlay; a standalone harness-modifier project would carry its own equivalent registries keyed to its own history.
- [d:r:i] `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/LONG-ARC.md`, `.planning/STATE.md`, readiness/rerun canon, `rooms/`/product-side doctrine — pure host.
- [d:r:i] The specific text of `tooling/compact-prompts/readiness.md` referencing Phase 01 rerun is host-local; any generic compact-prompt *template* must replace repo-specific anchors with placeholders.
- [d:r:i] Governance anchors the modifier does not own: `AGENTS.md`, `CLAUDE.md`, `AI-GUARDRAILS.md`, `WORKFLOW.md`, `ARTIFACT-GOVERNANCE.md`, `.planning/AGENTS.md`, `.planning/CLAUDE.md` — these carry host-repo wrappers, not harness doctrine, even where they reference `harness_modifier/`. They stay host in a later split and update their pointers into the modifier package rather than moving with it.

## What Should Move In The Next Slice

- [d:r:i] Do not bulk-move the overlay tree. The next move is a bounded classification-plus-narrow-slice pair, not a filesystem sweep.
- [d:r:i] Move (filesystem rehome into `harness_modifier/overlay/`) only the carriers whose text is already generic or can be rendered generic inside the same slice:
  - the three specialist skill adapters that do not embed audit-workspace paths: `gsd-uplift-project/SKILL.md`, `gsd-propagation-review/SKILL.md`, `gsd-seed-migration-inventory/SKILL.md`
  - the matching workflow shells `uplift-project.md`, `propagation-review.md`, `seed-migration-inventory.md` — but only after their embedded audit-workspace paths are either abstracted behind the modifier package or held explicitly as host-side appendix text
  - `references/mandatory-initial-read.md` (after confirming it is not silently carrying host planning doctrine; it is overwrite-mode and must stay upstream-compatible)
- [d:r:i] Hold the rest of the overlay (re-entry wrappers, compact-prompts, templates, reference continuity docs) for their own narrower slices after the carrier roster is written and audited.
- [d:r:i] Pair the filesystem move with a typed carrier roster at `harness_modifier/overlay/ROSTER.md` (or similar) that states per-entry classification and reason, so later slices read from a declared roster rather than inferring from filesystem position.

## What Should Remain Shared Boundary

- [d:r:i] `OVERLAY-MANIFEST.json` as a schema and ownership contract. Its `add` vs `overwrite` grammar travels with the modifier; its roster stays a shared-boundary file because each host repo's observed overlay roster is not automatically the harness's roster.
- [d:r:i] The installer spine `scripts/setup-portable-gsd.sh`. Decompose into:
  - a modifier-owned generic installer library (overlay apply, reasoning defaults, verify-materialized, capture-pristine-overwrites) — travels
  - a host-owned wrapper that sets `PRIX_COMPACT_PROMPT_FILE`, `DEFAULT_COMPACT_PROMPT_FILE`, and sources the modifier library — stays host
- [d:r:i] Compatibility declaration `declaration.json` stays a shared-boundary artifact too: the schema travels unchanged, but `runtime_held_annotations`, `parity_scan_baseline.rules`, and `upstream_compatibility_window.state` reflect what the current host observes and should remain refreshable per-host.
- [d:r:i] Workflows whose mechanism is generic but whose current text embeds audit-workspace paths stay shared-boundary *until* their text is split into generic shell plus host-local appendix — at which point the shell moves and the appendix stays host. Specifically:
  - `propagation-review.md` — embedded `95`/`96` and four `propagation-audit/artifacts/*.json` paths
  - `uplift-project.md` — embedded `103`, `06`, `08` audit-workspace packet paths in the route block
  - both files still reference `tooling/codex/project_uplift.py`, `tooling/codex/audit_refmap.py`, `tooling/codex/seed_migration_inventory.py` — these remain shared-boundary helpers per [139](../../intervention-proposals/139-harness-modifier-in-place-rehome-step-1-implementation.md) and the overlay text must not drift from helper-home truth

## What Should Stay Host-Repo Local

- [d:r:i] All `.planning/audits/…`, `.planning/readiness/…`, `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/LONG-ARC.md`, `.planning/STATE.md`, `.planning/REQUIREMENTS.md` content — these remain host and do not travel under `harness_modifier/overlay/`.
- [d:r:i] The host-side pointers into the modifier from `AGENTS.md`, `CLAUDE.md`, `AI-GUARDRAILS.md`, `WORKFLOW.md`, `ARTIFACT-GOVERNANCE.md`, `.planning/CLAUDE.md`, `.planning/AGENTS.md` — these stay host-owned governance and are updated as consumers rather than moved.
- [d:r:i] The specific *body* of `compact-prompts/readiness.md` and `compact-prompts/project.md` referencing Phase 01 rerun, `PROJECT.md`/`ROADMAP.md`/`REQUIREMENTS.md` canon, and rerun-floor anchors. Only a generic template skeleton may become modifier-owned later.
- [d:r:i] `.codex.local/compact-prompt.txt` selector and the `PRIX_COMPACT_PROMPT_FILE` env var — these are the host's local override levers on the generic mechanism.
- [d:r:i] The `prix-guesser/.planning/HARNESS-IMPROVEMENT-REGISTER.md` as a host register. The standalone project would carry its own improvement register keyed to its own history.

## Materialization And Override Control

- [d:r:i] Ownership layering for materialization must stay explicit across three layers (consistent with the inheritance in [dispositions/01](../dispositions/01-harness-extraction-field-map-audit-inheritance.md)):
  - upstream GSD runtime owns its own install; modifier does not claim upstream control
  - modifier owns overlay apply, reasoning defaults, verify-materialized, pristine-overwrite capture, compatibility declaration reading
  - host owns selector env vars, default compact-prompt choice, `.codex.local/` overrides, and any repo-specific post-materialization verification hooks
- [d:r:i] Local-override control in this lane means three levers must survive any rehome:
  - `PRIX_COMPACT_PROMPT_FILE` (or a renamed generic equivalent like `HARNESS_MODIFIER_COMPACT_PROMPT_FILE` in a later slice, with the host-specific name kept as a deprecated alias)
  - `.codex.local/compact-prompt.txt` selector file
  - `DEFAULT_COMPACT_PROMPT_FILE` at the host-wrapper level, so the modifier default does not silently displace host choice
- [d:r:i] The `OVERLAY-MANIFEST.json` `add` vs `overwrite` distinction is itself an override-control surface: `overwrite` entries must stay revisable by the host when upstream baseline movement forces it, and the modifier cannot silently convert `add` into `overwrite`.
- [d:r:i] The compatibility carrier stays the declaration-of-record; the installer echoes it inside `verify-materialized` rather than forking its own compatibility constants ([141](../../intervention-proposals/141-harness-modifier-compatibility-declaration-carrier-implementation.md)).

## Propagation Obligations

- [d:r:i] Before any overlay rehome slice lands, audit every overlay workflow and skill text for embedded host paths and record findings under `extraction-audit/` (outputs or a dedicated roster doc). This is the contract-change discipline from [GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md](../../governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md) applied to overlay carriers.
- [d:r:i] Move-coupled updates required with any rehome slice that changes overlay source paths:
  - `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` roster entries (path changes flow through here)
  - `scripts/setup-portable-gsd.sh` if it resolves any moved path literally
  - `harness_modifier/contract/portable_gsd_contract.py` overlay-apply and verify-materialized paths
  - `harness_modifier/contract/manifest_install_coherence.py` snapshot expectations
  - `python3 tooling/codex/audit_refmap.py` reference-map fixups for any moved markdown pointer (per `.planning/CLAUDE.md`)
- [d:r:i] Governance-surface updates required:
  - `tooling/portable-gsd/README.md`
  - `AGENTS.md`, `AI-GUARDRAILS.md`, `WORKFLOW.md`, `CLAUDE.md`, `.planning/CLAUDE.md`, `.planning/AGENTS.md` if they name overlay paths
  - `.planning/HARNESS-IMPROVEMENT-REGISTER.md` family status for the overlay-rehome slice
- [d:r:i] Propagation registry refresh required:
  - `propagation-audit/artifacts/03-propagation-registry-v2-declared-contracts.json`
  - `propagation-audit/artifacts/04-propagation-registry-v2-semantic-map.json`
  - `propagation-audit/artifacts/05-propagation-registry-v2-evidence-index.json`
  - `propagation-audit/artifacts/06-propagation-registry-v2-coverage-and-refresh.json`
  - a new `propagation-audit/NN-harness-modifier-overlay-rehome-change-triggered-refresh.md` matching the pattern used for `51`/`52`
- [d:r:i] Compatibility declaration refresh if the rehome moves any path currently named in `parity_scan_baseline.rules` (e.g., if `get-shit-done/workflows/update.md` becomes resolved from a rehomed overlay source). The declaration schema stays; the rule rows move in lockstep.
- [d:r:i] Installer verification required after any rehome slice: `./scripts/setup-portable-gsd.sh` + `python3 harness_modifier/contract/harness_canary.py report . --strict`, producing a clean canary report frozen into the slice's implementation proposal.
- [d:r:i] `$gsd-propagation-review` (the workflow and the skill) itself must be rerun against the slice; the route's own required_reading is part of what a rehome slice would change and must not drift silently.

## Recommended Sequence

1. [d:r:i] Write `harness_modifier/overlay/ROSTER.md` (or equivalent) with per-entry classification (`generic` / `shared-boundary` / `host-local`), the reason, and any propagation obligation the entry carries. Pair this with a scan of embedded host paths across every overlay workflow and skill text. No filesystem moves yet.
2. [d:r:i] Abstraction pass on workflow text: convert embedded audit-workspace path references in `propagation-review.md`, `uplift-project.md`, and `seed-migration-inventory.md` from hard `@__PROJECT_ROOT__/.planning/audits/...` anchors into (a) generic references that live inside the modifier package or (b) a host-side appendix referenced by a named role (e.g., `LOCAL_PROPAGATION_BASELINE_DOC`). Keep the change non-functional: semantics stay, anchors indirect.
3. [d:r:i] First bounded filesystem rehome under `harness_modifier/overlay/`: the three specialist skills (`gsd-uplift-project`, `gsd-propagation-review`, `gsd-seed-migration-inventory`) plus their matching workflow shells, after step 2 has cleaned their text. Manifest/installer/governance/registry propagation in the same slice. Post-slice `harness_canary` clean.
4. [d:r:i] Second bounded slice: references (`mandatory-initial-read.md`, `entry-runtime-uplift-continuity.md`, `milestone-boundary-uplift-continuity.md`) after confirming their text is host-neutral.
5. [d:r:i] Third bounded slice: compact-prompts split. Extract a mechanism template into `harness_modifier/overlay/tooling/compact-prompts/` (with host anchors replaced by named placeholders) and keep `tooling/compact-prompts/project.md` and `readiness.md` host-local as the concrete bodies this repo carries. Update the installer so the generic template falls back to the host body via the existing `PRIX_COMPACT_PROMPT_FILE` / `.codex.local/compact-prompt.txt` levers.
6. [d:r:i] Fourth bounded slice: re-entry / update / resume / progress / health / from-gsd2 skill wrappers, once the specialist tranche has exercised the rehome path cleanly.
7. [d:r:i] Only then reopen standalone-repo boundary design, second-host dry run, and later distribution route.

## Held Later

- [d:r:i] Standalone repo split
- [d:r:i] npm / `npx` packaging
- [d:r:i] Second-host dry run
- [d:r:i] Full `.claude` materialization widening beyond the current held-annotation posture
- [d:r:i] Widening into all-provider portability
- [d:r:i] Any bulk `move the overlay` sweep
- [d:r:i] Renaming `PRIX_COMPACT_PROMPT_FILE` to a provider-neutral env — keep the current host name while a deprecated-alias path is still carried; do not flip naming mid-rehome

## Exact Next Move

- [d:r:i] Open one bounded proposal (a `143-` or next-available intervention number) whose scope is strictly:
  1. author the carrier roster at `harness_modifier/overlay/ROSTER.md` with generic / shared-boundary / host-local classification per current overlay entry
  2. produce an embedded-host-path scan across `tooling/portable-gsd/overlay/get-shit-done/workflows/*.md` and `tooling/portable-gsd/overlay/skills/*/SKILL.md`, capturing every `required_reading` / `supporting_reading` / route-block reference to `.planning/audits/...` or other host-owned paths
  3. name the explicit set of overlay entries eligible for the first filesystem rehome slice (the specialist-skill-plus-workflow pair per step 3 of the sequence) and the explicit propagation obligations that slice carries
- [d:r:i] Do not include any filesystem rehome in that proposal's land-now scope. The first rehome slice is the next-after-143 proposal, authored only once the roster and scan are frozen.
- [d:r:i] Keep this boundary referenced from [.planning/HARNESS-IMPROVEMENT-REGISTER.md](../../../../HARNESS-IMPROVEMENT-REGISTER.md) `Current Bounded Next Slices` so it does not become ambient between subtrees.
