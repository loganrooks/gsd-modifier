Date: 2026-04-22
Status: lane return

# Project Uplift Host-Doctrine Catalog Neutralization Judgment

## What The Payload-Home Lane Clarified

- Lane `06` widened the helper's remaining coupling map past "relocate or not" into three distinct still-embedded surfaces inside `project_uplift.py`: the host-doctrine carrier catalog (`STATIC_FILE_CARRIERS` / `MARKER_CARRIERS` plus the `build_runtime_agent_specs` `.codex/agents/*.toml` walk), the host-facing rerun-boundary and skill-command vocabulary (`RERUN_BOUNDARY_PATTERNS`, `$gsd-uplift-project`, `$gsd-seed-migration-inventory`, and the state-section / recommendation strings around them), and the direct `.planning/STATE.md` plus `.planning/phases/*/*-CONTEXT.md` writer/scanner reach (`state_status`, `latest_phase_context_path`, `update_state_section`, `count_phase_files`).
- Lane `06` fixed the sequencing so these three surfaces do not collapse into one tranche: the catalog plus vocabulary belong to the current neutralization tranche, while the `.planning/STATE.md` writer and `.planning/phases/` scanner split out into a later host-planning-shape slice so the typed carrier surface this tranche opens stays bounded rather than inheriting planning-state write semantics.
- Lane `06` kept `project_uplift.py` relocation, `seed_migration_inventory.py` relocation, `audit_refmap.py` movement, overwrite-family source split, second overlay filesystem tranche, standalone repo boundary, and packaging all explicitly outside this tranche, with `.codex` as observed basis and `.claude` as held annotation rather than expanding into a multi-runtime parity move.
- Lane `06` also framed the move as externalizing observed typed doctrine surfaces, not flattening the analysis algorithm into data — fingerprinting dispatch, classification, drift-reason composition, recommendation-reason composition, and report/manifest/state-section rendering continue to be the helper's job.

## What The Proposal Gets Right

- Proposal `156` mirrors the three-surface map from lane `06` one-for-one: catalog is the first bounded target, vocabulary is the second bounded target, and the `.planning/STATE.md` plus `.planning/phases/` reach is explicitly held as a later host-planning-shape slice rather than smuggled into the same tranche.
- The per-item catalog schema the proposal names (`stable key`, `group or class`, `relative path`, `label`, `fingerprint shape`, `marker string where marker-based`) directly matches the `FileCarrierSpec` / `MarkerCarrierSpec` shape `project_uplift.py` already carries, so the catalog can externalize observed doctrine without inventing a new classification vocabulary.
- The proposal routes runtime-agent registry shape through the same catalog or a narrow sibling rather than leaving `build_runtime_agent_specs` as a separately hard-coded walk, which aligns with lane `06`'s observation that the `.codex/agents/*.toml` glob is structurally the same kind of host-doctrine as the static list rather than a separate class.
- The explicit hold list stays narrowed to the current lane's bounded concern: no relocation, no second overlay tranche, no overwrite-family source split, no standalone repo, no npm/`npx` packaging, no broader `.codex` / `.claude` parity redesign, and no `.planning/STATE.md` writer work in the same slice.
- Keeping fingerprint logic, classification, drift-reason composition, report/manifest rendering, dataclasses, and CLI wiring helper-local preserves the pattern line lane `06` settled on: typed catalogs of what the helper observes belong in typed carriers, and the logic that turns those observations into classifications and recommendations stays in the helper.
- The vocabulary carrier scope is drawn at the right coupling boundary — it captures both rerun-boundary phrases and operator-facing skill-command tokens rather than pulling one and leaving the other embedded, which would otherwise keep the helper's recommendation/state-section text acting as an unmanaged vocabulary surface.

## What Still Needs Sharpening

- The "same catalog or a very narrow sibling" clause for runtime-agent registry shape leaves the open-vs-closed split undetermined. The registry entry is dynamically expanded by directory glob, while `STATIC_FILE_CARRIERS` entries are enumerated statically, so collapsing them under one JSON list forces a discriminant field (`spec_kind: "file" | "marker" | "directory_glob"`) and changes the catalog loader shape. A narrow sibling (for example a `runtime_agent_registry` subsection inside the same catalog file, or a distinct `registry` object) keeps the loader mechanically simple; this choice should be settled in the proposal rather than deferred to implementation.
- `OVERLAY_MANIFEST_REL_PATH = "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json"` is named in lane `06` as a remaining install-contract pointer constant, but proposal `156` does not say where it lives in the new split. It is neither host-doctrine carrier shape nor operator-facing vocabulary; it is install-contract wiring. The tranche should either include it in the catalog under an install-contract entry (with its own group, for example `install_contract`) or explicitly keep it helper-local for this tranche and defer install-contract neutralization to a later bounded slice. Leaving it unclassified risks silently widening later.
- The proposal names "rerun-boundary phrases" and "`$gsd-uplift-project` / `$gsd-seed-migration-inventory`" but does not draw the line between those and the surrounding label constants (`PROGRESS_NOTE_RENDER_FIELDS`, `SEED_MIGRATION_CANDIDATE_LABEL`, etc.). Label constants that only shape internal rendering are helper-local; tokens that encode host skill-namespace strings or host-specific doctrinal boundary phrases are vocabulary. The tranche needs an explicit inclusion/exclusion rule, otherwise vocabulary creep pulls rendering literals in too.
- The state-heading string (`"## Project Uplift"`) already lives in `uplift/output_policy.json`, but the inline recommendation strings (for example `"Run \`$gsd-uplift-project --detect-only\` before treating ordinary routing as settled."`) still embed skill-command vocabulary through f-string composition. The proposal implicitly covers these through the vocabulary carrier, but should say so directly — otherwise one natural reading is that the vocabulary carrier exposes only the raw tokens while the composed sentences stay helper-local, which would leave the host-facing operator vocabulary half-externalized.
- The parity-test frontier the proposal gestures at ("carrier fingerprint stability, absent-additive list, drift-reason text") should be tied to concrete test entry points before implementation — at minimum `tooling/codex/tests/test_project_uplift.py` assertions over `analyze_repo` output for a representative fixture, so catalog externalization cannot silently change classification or carrier fingerprint shape under cover of data movement.
- The proposal does not say how the catalog carrier declares ordering. `STATIC_FILE_CARRIERS + build_runtime_agent_specs(...) + MARKER_CARRIERS` ordering currently feeds `doctrine_reference_hash` indirectly through sort-and-join, but any externalized list needs a stable ordering rule so catalog reordering does not churn the doctrine reference hash across reruns. This is either an explicit order-by-key rule at the loader, or an explicit list ordering inside the JSON.

## Recommended Catalog And Vocabulary Boundary

- `harness_modifier/uplift/carrier_catalog.json` carries the typed host-doctrine surface. Suggested shape:
  - `schema_version`: `1`
  - `file_carriers`: list of `{ key, group, rel_path, label, fingerprint_shape }` objects, mirroring the current `STATIC_FILE_CARRIERS` entries one-to-one, including `runtime_config` (the `.codex/config.toml` anchor).
  - `marker_carriers`: list of `{ key, group, rel_path, label, marker, fingerprint_shape }` objects, mirroring the current `MARKER_CARRIERS` entries one-to-one.
  - `runtime_agent_registry`: single object (not a list) of `{ group, dir_rel_path, glob, key_prefix, label_template, fingerprint_shape }` covering the `.codex/agents/*.toml` walk. Keeping it as a named sibling object rather than a hidden entry inside `file_carriers` preserves the enumerate-vs-expand distinction and keeps the catalog loader shape simple.
  - Ordering rule: `file_carriers` and `marker_carriers` preserve list-order as authored; the loader does not resort them. `doctrine_reference_hash` keeps its current sort-and-join over fingerprint rows rather than depending on catalog order.
- `harness_modifier/uplift/vocabulary.json` carries the typed host-facing vocabulary surface. Suggested shape:
  - `schema_version`: `1`
  - `rerun_boundary_patterns`: list of regex strings (`pre-rerun`, `fresh discuss \+ plan required`, `rerun-boundary`, `input to the next discuss pass`), compiled helper-side; compilation flags stay in the loader or helper, not the data.
  - `skill_commands`: object with named keys (`uplift_project` → `$gsd-uplift-project`, `seed_migration_inventory` → `$gsd-seed-migration-inventory`); the `--write` variant stays composed helper-side from the base token so the carrier does not duplicate composition.
  - `recommendation_sentences`: named sentence templates for the four operator-facing strings (first-pass write, detect-only, write-after-movement, routing-settled) so the vocabulary carrier owns both the tokens and the full operator-facing sentences, not only the tokens.
- `harness_modifier/uplift/carrier_catalog.py` and `harness_modifier/uplift/vocabulary.py` loaders sit next to the existing `harness_modifier/uplift/output_policy.py` and `harness_modifier/compatibility/{declaration,observation,seed_contract}.py` loaders, keeping the pattern set consistent.
- `project_uplift.py` calls the two loaders once at analysis entry, retains the `FileCarrierSpec` / `MarkerCarrierSpec` dataclasses as in-memory shapes constructed from catalog data, and keeps `build_runtime_agent_specs` in place but parameterized by the registry entry (directory, glob, key prefix, label template, fingerprint shape) rather than hard-coded literals.
- `OVERLAY_MANIFEST_REL_PATH` stays helper-local for this tranche rather than riding into the catalog. It is install-contract wiring, not host-doctrine catalog content. A later bounded slice can neutralize install-contract wiring as its own typed carrier; pulling it in here widens this tranche's declared surface.
- Internal rendering labels (`PROGRESS_NOTE_RENDER_FIELDS` tuple, `PROGRESS_NOTE_REASON_LABEL`, `SEED_POSTURE_REASON_LABEL`, `SEED_MIGRATION_CANDIDATE_LABEL`, `SEED_MIGRATION_BREAKDOWN_LABEL`, `SEED_MIGRATION_INSPECT_POINTER_LABEL`, `SEED_MIGRATION_WRITE_POINTER_LABEL`) stay helper-local — they shape the helper's own report/progress-note layout rather than carrying host-facing operator vocabulary.

## What Should Stay Helper-Local

- Fingerprint dispatch and primitives: `compute_fingerprint`, `normalized_toml_fingerprint`, `frontmatter_text`, `marker_block_text`, `extract_h2_headings`, `inventory_items`, `parse_frontmatter_map`, `parse_seed_contract_version`, `sha256_text`, `heading_level`.
- Dataclasses `FileCarrierSpec` and `MarkerCarrierSpec` as in-memory classification shapes constructed from catalog data, not moved into the JSON carrier itself.
- Classification logic: `classify_project`, `secondary_signals`, `doctrine_sensitive_proposals`, `doctrine_reference_hash`, `project_fingerprint_hash`, `seed_corpus_needs_attention`.
- Analysis composition: `analyze_repo`, `build_file_carrier`, `build_marker_carrier`, `build_runtime_agent_specs` (now parameterized by the registry entry), `build_seed_corpus_posture`, `build_compatibility_basis`, `phase_boundary_signal`, `post_write_analysis`.
- Drift-reason composition: `compatibility_drift_reasons`, `seed_corpus_drift_reasons`, `recommendation_reasons`, `seed_corpus_reasons`, `seed_corpus_summary`, `seed_migration_candidate_breakdown_text`, `summarize_proposal_route`.
- Rendering and emit: `render_report`, `state_section_text`, `build_progress_note`, `progress_note_seed_fields`, `emit_json`, `load_held_later_families`, `parse_held_later_family_line`, `format_held_later_family`.
- CLI and IO plumbing: `parse_args`, `main`, `read_text`, `read_json`, `now_iso`, `rel_path`, `write_outputs`.
- The `state_status` reader, `latest_phase_context_path` scanner, `count_phase_files` counter, and `update_state_section` writer — these belong to the later host-planning-shape slice and stay untouched in this tranche rather than acting as hidden scope creep.
- `OVERLAY_MANIFEST_REL_PATH` — install-contract wiring held as helper-local for this tranche.
- `PROGRESS_NOTE_RENDER_FIELDS` and sibling label constants — internal rendering labels, not host-facing vocabulary.

## Held Later

- `project_uplift.py` relocation itself — reopen only after this second tranche plus its propagation refresh lands.
- `seed_migration_inventory.py` relocation — downstream of `project_uplift.py`, does not lead.
- `audit_refmap.py` movement or any reopening as a payload candidate — remains repo-local audit tooling.
- Second overlay filesystem tranche.
- Overwrite-family source-indirection widening.
- Standalone repo boundary design and npm/`npx` packaging.
- Broader `.codex` / `.claude` parity redesign beyond the current observed basis plus held annotation anchor.
- Candidate runtime widening (`.gemini`, `.config/opencode`, `.opencode`, `.config/kilo`, `.kilo`) beyond the current `.codex` observed basis.
- `.planning/STATE.md` writer plus `.planning/phases/*/*-CONTEXT.md` scanner neutralization — its own host-planning-shape slice after this catalog + vocabulary tranche lands.
- Install-contract pointer neutralization (`OVERLAY_MANIFEST_REL_PATH` and any neighboring install-contract wiring) — its own later bounded slice rather than a hidden fold into this catalog.

## Exact Next Move

1. Land the sharpened proposal as the working spec for the tranche: settle runtime-agent registry as a named sibling object inside `carrier_catalog.json` (not a hidden entry in `file_carriers`); settle `OVERLAY_MANIFEST_REL_PATH` as helper-local held-later rather than catalog-resident; settle that the vocabulary carrier owns both raw tokens and the four operator-facing sentence templates, not only the tokens; settle that internal rendering labels stay helper-local.
2. Open `harness_modifier/uplift/carrier_catalog.json` with the `file_carriers` / `marker_carriers` / `runtime_agent_registry` shape above, plus `harness_modifier/uplift/carrier_catalog.py` as its loader, mirroring the existing `output_policy.py` loader pattern.
3. Open `harness_modifier/uplift/vocabulary.json` with the `rerun_boundary_patterns` / `skill_commands` / `recommendation_sentences` shape above, plus `harness_modifier/uplift/vocabulary.py` as its loader.
4. Rewire `project_uplift.py` to consume both loaders at analysis entry, parameterize `build_runtime_agent_specs` through the registry entry, and replace the inline f-string recommendation sentences with vocabulary-carrier templates while leaving classification, fingerprinting, drift-reason composition, and rendering unchanged.
5. Add focused parity tests in `tooling/codex/tests/test_project_uplift.py` covering carrier fingerprint stability on a representative fixture, absent-additive list equality, `doctrine_reference_hash` stability across a catalog-order no-op, drift-reason text equivalence, and recommendation-sentence equivalence — so catalog plus vocabulary externalization cannot silently change analysis output.
6. Refresh `harness_modifier/overlay/helpers/AUTHORITY-MAP.md`, `harness_modifier/overlay/ROSTER.md`, and `.planning/HARNESS-IMPROVEMENT-REGISTER.md` around the landed tranche, and open the matching propagation-audit entry in the `propagation-audit/` family the same way `57` landed for tranche one.
7. Only after this tranche plus its propagation refresh lands, reopen the `project_uplift.py` payload-home question on top of the further-thinned helper. Do not reopen overwrite-family source split, second overlay filesystem tranche, standalone repo boundary, `.planning/STATE.md` writer neutralization, or install-contract pointer neutralization from this lane.
