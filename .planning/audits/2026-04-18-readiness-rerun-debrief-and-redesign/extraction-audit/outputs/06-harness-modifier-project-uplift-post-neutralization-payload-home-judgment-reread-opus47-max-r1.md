Date: 2026-04-22
Status: lane return

# Project Uplift Post-Neutralization Payload-Home Judgment

## What The Neutralization Slice Changed

- Runtime-discovery policy now routes through `harness_modifier/compatibility/observation.json`; `project_uplift.runtime_dirs_present` reads the typed observed plus candidate sets rather than carrying a helper-local directory list.
- Uplift output topology now routes through `harness_modifier/uplift/output_policy.json`; `state_heading`, `report_rel_path`, `manifest_rel_path`, and `held_later_rel_path` all resolve through that carrier, so the state-heading, report path, manifest path, and held-later pointer are no longer helper-local ambient memory.
- Seed-contract shape now routes through `harness_modifier/compatibility/seed_contract.json`; seed-root relative path, current contract version, required frontmatter keys, and required section headings are typed rather than re-declared in helper code.
- Compatibility posture stays declaration-driven through `harness_modifier/compatibility/declaration.json`, preserving `.codex` observed basis plus `.claude` held annotation as the compatibility surface rather than implicit helper wiring.
- Downstream consumers moved with the split: `seed_migration_inventory.py` now loads the seed-contract carrier directly, and `harness_canary.py` reads the output-policy carrier directly instead of importing path constants out of `project_uplift`.
- The shim at `harness_modifier/overlay/helpers/project_uplift.py` is now just a path/import bridge to `tooling/codex/project_uplift.py`, not a second authority surface.

## Remaining Host Or Shared-Boundary Coupling

- Embedded host-doctrine carrier catalog. `STATIC_FILE_CARRIERS` and `MARKER_CARRIERS` inside `project_uplift.py` hard-code:
  - host governance carriers (`AGENTS.md`, `.planning/AGENTS.md`, `CLAUDE.md`, `.planning/CLAUDE.md`);
  - runtime-specific doctrine carriers (`.codex/get-shit-done/workflows/verify-phase.md`, `.codex/get-shit-done/templates/verification-report.md`, `.codex/get-shit-done/workflows/discuss-phase.md`, `.codex/get-shit-done/templates/context.md`, `.codex/get-shit-done/workflows/plan-phase.md`, `.codex/skills/gsd-rigorous-research/references/output-template.md`);
  - planning-canon additive carriers (`.planning/CLAIM-TYPES.md`, `.planning/LONG-ARC.md`, `tooling/codex/README.md`);
  - runtime-registry anchor (`.codex/config.toml`).
  This catalog still lives as helper-local classification (`doctrine_sensitive` / `additive_install` / `runtime_registry`) plus per-carrier fingerprint shape, which is structurally the same helper-local doctrine the neutralization slice just lifted on the observation / seed-contract / output-policy seams.
- Runtime-agent glob. `build_runtime_agent_specs` walks `.codex/agents/*.toml` directly, encoding the `.codex` runtime directory plus agent-contract suffix pattern in helper code rather than in a typed host carrier.
- Rerun-boundary pattern set. `RERUN_BOUNDARY_PATTERNS` encodes host-specific boundary phrases (`pre-rerun`, `fresh discuss + plan required`, `rerun-boundary`, `input to the next discuss pass`) as a helper-local constant.
- Install-contract pointer constant. `OVERLAY_MANIFEST_REL_PATH = "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json"` couples the helper to the current install-target wiring rather than to a declared portable path.
- Skill-command tokens. `SEED_MIGRATION_SKILL_COMMAND` and the `$gsd-uplift-project` strings inside recommendation and state-section text tie helper output to the current skill-namespace shape.
- Planning-state writer. `state_status`, `latest_phase_context_path`, and `update_state_section` reach directly into `.planning/STATE.md` and `.planning/phases/*/*-CONTEXT.md`, so the helper still doubles as a host planning-surface writer, not just a reader of typed policy carriers.
- `held_later_rel_path` still resolves through `output_policy.json` into `tooling/codex/UPLIFT-HELD-LATER.md`, which keeps one uplift artifact home inside the helper's own source tree rather than under `.planning/`.

## What Would Travel If Later Movement Were Still Earned

- `tooling/codex/project_uplift.py` itself as the payload module.
- The already-typed carriers it consumes: `harness_modifier/compatibility/declaration.json`, `harness_modifier/compatibility/observation.json`, `harness_modifier/compatibility/seed_contract.json`, `harness_modifier/uplift/output_policy.json`, and their loader modules.
- The overlay-owned shim `harness_modifier/overlay/helpers/project_uplift.py` as the stable import entry.
- The direct test surface `tooling/codex/tests/test_project_uplift.py`, which is the in-repo parity guard for this helper's analysis behavior.
- Downstream consumers that already adopted the typed carriers (`seed_migration_inventory.py` on the seed-contract surface, `harness_canary.py` on the output-policy surface) travel only once their own host-coupling tails are themselves neutralized; they do not lead the movement.
- `.codex` plus `.claude` observed-basis wiring stays as the travel-compatibility anchor rather than expanding into multi-runtime support.

## What Should Stay Helper-Local

- The analysis algorithm itself: carrier fingerprinting, doctrine-reference hashing, primary-class classification, secondary-signal derivation, recommendation-reason composition, and seed-corpus posture analysis.
- The mechanism-level dataclasses `FileCarrierSpec` and `MarkerCarrierSpec` and the fingerprint-shape dispatch (`content_sha256`, `frontmatter_hash`, `inventory_item_hash`, `normalized_toml_hash`, `marker_block_hash`).
- Manifest drift comparison (`compatibility_drift_reasons`, `seed_corpus_drift_reasons`), progress-note assembly, and report/manifest/state-section rendering.
- CLI wiring, argument parsing, and JSON-emit behavior.

The pattern line is: typed catalogs of what carriers and boundary phrases the helper observes belong in typed carriers; the logic that turns those observations into a classification and a recommendation belongs in the helper.

## Judgment On The Payload-Home Question

- The neutralization slice sharpened the helper at its policy-data seams, so `project_uplift.py` now reads rather than re-declares the observation, output-policy, and seed-contract surfaces.
- The helper remains materially coupled to this host through three still-embedded surfaces: the host-doctrine carrier catalog, the rerun-boundary and skill-command vocabulary, and the direct `.planning/STATE.md` plus `.planning/phases/` reach. Each of those is structurally the same kind of helper-local doctrine the neutralization slice just externalized elsewhere.
- Relocating the payload now would carry that remaining helper-local doctrine with it, which would re-host the same kind of blur in a new home instead of dissolving it.
- The sharper next move is therefore not relocation and not a pivot to a different adjacent extraction family. It is one further neutralization tranche on `project_uplift.py` itself — the host-doctrine carrier catalog plus its boundary-vocabulary constants — before the payload-home question is reopened.
- `seed_migration_inventory.py` stays downstream and must not lead; `harness_canary.py` stays a neighboring consumer and must not inherit payload-home authority; `audit_refmap.py` stays out of the payload-movement candidate set.

## Recommended Next Slice

Open a bounded second neutralization intervention on `project_uplift.py` that moves its embedded host-doctrine catalog out of helper-local constants into typed carriers under `harness_modifier/`, keeping `.codex` plus `.claude` as the observed-basis horizon. Specifically:

- Split the host-doctrine catalog into a typed carrier sibling to the existing uplift and compatibility carriers — for example `harness_modifier/uplift/carrier_catalog.json` — encoding per-carrier `key`, `group`, `rel_path`, `label`, and `fingerprint_shape`, plus the marker string for marker-kind carriers. `project_uplift.py` consumes the catalog and keeps the fingerprint-shape dispatch helper-local.
- Externalize the runtime-agent registry shape (directory plus glob plus fingerprint-shape) into the same catalog carrier or a narrow sibling, so `build_runtime_agent_specs` reads a typed registry description rather than a hard-coded `.codex/agents/*.toml` walk.
- Externalize rerun-boundary phrases and the `$gsd-uplift-project` / `$gsd-seed-migration-inventory` skill-command tokens into a typed uplift-vocabulary carrier (for example `harness_modifier/uplift/vocabulary.json`), so recommendation text, state-section text, and progress-note text do not embed host skill-namespace strings in helper code.
- Keep the `.planning/STATE.md` write reach and `.planning/phases/` scan reach explicitly out of this tranche; split them into a separate host-planning-shape neutralization slice after this one so the declared-catalog surface stays bounded.
- Preserve the current analysis behavior with focused parity tests (carrier fingerprint stability, absent-additive list, drift-reason text) so the neutralization does not move classification behavior under the cover of data externalization.
- Refresh `harness_modifier/overlay/helpers/AUTHORITY-MAP.md`, `harness_modifier/overlay/ROSTER.md`, and `.planning/HARNESS-IMPROVEMENT-REGISTER.md` around the landed slice, the same way 154's propagation refresh landed.

## Held Later

- `project_uplift.py` relocation itself.
- `seed_migration_inventory.py` relocation.
- `audit_refmap.py` movement or reopening as a payload candidate.
- Second overlay filesystem tranche.
- Overwrite-family source-indirection widening.
- Standalone repo boundary design.
- npm or `npx` packaging.
- Broader `.codex` / `.claude` parity redesign beyond the observed-basis plus held-annotation anchor.
- Speculative widening of the observation carrier's candidate runtimes (`.gemini`, `.config/opencode`, `.opencode`, `.config/kilo`, `.kilo`) beyond the current `.codex` observed basis.
- `.planning/STATE.md` writer and `.planning/phases/` scanner neutralization, as its own host-planning-shape slice after the catalog tranche lands.

## Exact Next Move

1. Draft a bounded intervention proposal — `156-harness-modifier-project-uplift-host-doctrine-catalog-neutralization-proposal` — scoping the typed carrier catalog plus vocabulary carrier above, with `.codex` observed basis and `.claude` held annotation preserved.
2. Inherit that proposal through the normal reread-and-dispose lane rather than widening it into a relocation slice.
3. Only after that second neutralization tranche lands and its propagation refresh is recorded, reopen the `project_uplift.py` payload-home question on top of the further-thinned helper; do not reopen overwrite-family source split, second overlay tranche, standalone repo boundary, or packaging from this lane.
