Date: 2026-04-21
Status: completed reread output (opus47-max-r1)

# Landed Project Uplift First-Slice Reread — Opus 4.7 Max R1

## Framing

- [g:r:i] This reread reads the landed first slice of the `37 + 38 + 39` project-uplift family against the live helper, the authoritative workflow and wrapper sources, the `progress` consumer, and the durable repo outputs. The target is not the bundle shape in the abstract; it is the live carry in `tooling/codex/project_uplift.py`, `harness_modifier/overlay/get-shit-done/workflows/uplift-project.md`, `harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md`, the materialized `.codex/get-shit-done/workflows/progress.md`, and the written `.planning/UPLIFT-REPORT.md`, `.planning/UPLIFT-MANIFEST.json`, and `.planning/STATE.md` uplift section.
- [g:r:i] Claim notation follows [AGENTS.md:93-106](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:93). Evidenced positive claims carry `[e:c+i]` with direct file:line; downstream design moves carry `[d:r:i]`; framing lines carry `[g:r:i]`.
- [g:r:i] Where this reread judges live mechanics against the bundle's own prior reread, it cites the landed code first and the bundle pressure second, so the judgment stays on the live surface rather than on memory of `03-revised-*-reread-opus47-max-r1.md`.

## What The Landed First Slice Now Carries More Strongly

### 1. The helper is one Python module with typed carrier specs rather than scattered shell plus ad hoc filesystem reads

- [e:c+i] `tooling/codex/project_uplift.py` consolidates carrier definitions, fingerprinting, classification, report rendering, manifest writing, `STATE.md` section update, and the read-only `progress-note` consumer into one module with two dataclasses — `FileCarrierSpec` and `MarkerCarrierSpec`. Sources: [project_uplift.py:39-98](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:39).
- [d:r:i] The bundle's `39:183` said `fingerprints or version stamps` interchangeably, and the prior reread named that as a seam. In the live code the shape is still uniform (see §Thins/Compresses), but the typed carrier specs are the surface where a per-carrier shape can now be installed cleanly. The dataclass split makes the `marker-present` state orthogonal to the file's own presence (line 199 `present` vs line 180 `file_present`), which was the first structural distinction the bundle needed and the first distinction the live helper carries.

### 2. Mid-phase uplift is now a reachable class in the helper's classifier

- [e:c+i] `classify_project` now carries `mid-phase uplift` as its own branch at [project_uplift.py:254-255](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:254). The prior reread's revision §1 pressure for mid-phase-as-class is present in code rather than only in proposal prose.
- [d:r:i] The class is not yet orthogonal to cross-runtime (§Thins/Compresses names that), but it exists as a reachable classification outcome. That is the carry the prior reread asked for on paper; what the live code still compresses is the axis, not the class.

### 3. Marker-vs-file carrier distinction is now a live type, not a comment

- [e:c+i] The strengthening-route carriers are typed as `MarkerCarrierSpec` at [project_uplift.py:69-98](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:69) with `marker="Strengthening Opportunities"`, and their status is computed through `build_marker_carrier` at [project_uplift.py:180-203](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:180) with three discrete states: `marker_present`, `marker_absent`, `absent`.
- [d:r:i] Before the slice landed, the bundle framed strengthening-route carry as "not yet present on surfaces where the repo now expects it" (39:76) without specifying how presence would be detected. The live type turns that into a three-state answer that the manifest, report table, and `progress` consumer all read identically. That is stronger form than a presence boolean for a substring test embedded in ad hoc code.

### 4. The `progress` consumer is actually wired and conditionally rendered

- [e:c+i] `.codex/get-shit-done/workflows/progress.md` at [progress.md:131-147](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:131) invokes `python3 tooling/codex/project_uplift.py progress-note` and conditionally renders the `## Uplift Posture` section only when `UPLIFT_NOTE.show` is `true`.
- [d:r:i] The bundle's §6 in `39` named "one read-only `progress` hook" as the first live consumer. In the live surface, the hook is not only named but also conditional on real manifest state: no manifest, no section — so `progress` output stays thin when uplift memory is absent. That is the consumer-side posture the bundle's "first live routed consumer" pressure was asking for, and it now meets the operator through the same path progress was already running.

### 5. The read-only `progress-note` consumer reads the manifest as authoritative fingerprint source

- [e:c+i] `build_progress_note` at [project_uplift.py:518-563](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:518) loads the stored manifest, runs a fresh `analyze_repo` to get the current doctrine fingerprint, compares the stored `doctrine_reference_hash` against the live one, and builds its recommendation from that delta plus any `pending_doctrine_sensitive_proposals` in the stored manifest.
- [d:r:i] The prior reread's revision §6 asked the hook to read the manifest as structural signal and `STATE.md` as narrative companion. The live implementation does that — the manifest is the fingerprint source; `STATE.md` is prose that `progress` does not parse. There is still a subtlety about re-running the full analyze on every call (see §Thins/Compresses §8), but the separation between structural and narrative carry is clean in code.

### 6. The transient pre-write recommendation bug is fixed in `post_write_analysis`

- [e:c+i] `post_write_analysis` at [project_uplift.py:433-443](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:433) strips the exact reason string `"no uplift manifest recorded yet"` from `recommendation_reasons` before the report, manifest, and `STATE.md` section are written, then recomputes `recommend_detect_only` against the remaining reasons.
- [d:r:i] The bundle's `40:40-44` recorded this as the first real integration bug the live slice surfaced on itself. The fix is not a one-line special case buried in the writer; it is a named function that makes the before/after distinction legible to any future reader. Operator-facing durable outputs now reflect post-write posture rather than the transient pre-write moment the detector saw.

### 7. The `.planning/STATE.md` uplift section is landed with correct routing to `## Session Continuity`

- [e:c+i] `.planning/STATE.md` at [STATE.md:81-89](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:81) carries a real `## Project Uplift` section with last-pass date, class, doctrine-change flag, pending count, recommendation, and pointers to report and manifest. `update_state_section` at [project_uplift.py:469-484](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:469) matches an existing `## Project Uplift` heading with a `(?=\n## |\Z)` lookahead so later sections do not get swallowed, and when no prior section exists it inserts before `## Session Continuity` rather than appending past the end.
- [d:r:i] That placement choice — above `## Session Continuity` — keeps the uplift memory visible at the top of the state surface rather than behind resume prose. A future `resume-project` hook (held for later) reading `STATE.md` prose will encounter the uplift posture before session context. The bundle named "dedicated uplift section inside `STATE.md`" as primary carrier at `39:169`; the live insertion rule makes the location choice concrete.

### 8. Dogfood carry is real and non-fake

- [e:c+i] The current `.planning/UPLIFT-REPORT.md` at [UPLIFT-REPORT.md:5](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:5) records `Project class: cross-runtime uplift` and the manifest at [UPLIFT-MANIFEST.json:9-12](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:9) shows `runtime_dirs: [".codex", ".claude"]`.
- [d:r:i] The dogfood run surfaced a real classification for the prix-guesser repo itself rather than a convenient `already current` that would have hidden the live cross-runtime surface. That class carries truthful pressure for later cross-runtime uplift work (the actual refresh action stays held), and it validates that the helper's detection does not simply prefer `current-aligned posture` on the repo that built it.

### 9. Durable outputs are written through one atomic writer rather than three separate routines

- [e:c+i] `write_outputs` at [project_uplift.py:487-515](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:487) creates `.planning/` if missing, runs `post_write_analysis` once, renders the report, writes the manifest, and updates the state section in sequence using the same `written_analysis` payload.
- [d:r:i] Three durable outputs share one analysis payload, which means the class, fingerprints, reasons, and recommendation cannot disagree across the three artifacts within a single pass. A partial-write crash (e.g., disk full mid-state-update) could leave the report and manifest newer than the state section, but no path in normal operation lets the three drift apart within one run.

### 10. The overlay workflow and skill carry through materialization rather than live-only patch

- [e:c+i] `tooling/portable-gsd/overlay/get-shit-done/workflows/uplift-project.md` and `tooling/portable-gsd/overlay/skills/gsd-uplift-project/SKILL.md` exist as tracked overlay artifacts; `40:23-24` records that `.codex/` was re-materialized through `./scripts/setup-portable-gsd.sh`; `ls` confirms `.codex/get-shit-done/workflows/uplift-project.md` and `.codex/skills/gsd-uplift-project/SKILL.md` both exist.
- [d:r:i] The tracked overlay is the durable authority; the `.codex/` tree is its materialization. This preserves the materialization chain named in [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:33-42](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:33) rather than creating a live-only fork where `.codex/` has content that tracked overlay cannot reproduce.

### 11. The synthetic test set exercises write-then-doctrine-change end-to-end

- [e:c+i] `tooling/codex/tests/test_project_uplift.py` at [test_project_uplift.py:74-117](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_project_uplift.py:74) writes outputs for a lightly aged fixture, asserts that the immediate `progress-note` reports `recommend_detect_only: false`, then mutates `AGENTS.md` and asserts that the next `progress-note` picks up `doctrine_reference_changed: true`.
- [d:r:i] That test is the one that validates the consumer-side routing contract: the manifest's stored doctrine hash vs the live doctrine hash drives the `progress` recommendation. Writing the test against the mutation rather than against a pre-baked manifest is what makes it a round-trip contract rather than a fixture-parity check.

## Where The Live Implementation Boundary Still Thins Or Compresses Distinct Jobs

### 1. Classification is exclusive-branch, so mid-phase and cross-runtime cannot both carry on the same repo

- [e:c+i] `classify_project` at [project_uplift.py:250-260](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:250) tests cross-runtime (line 252) before mid-phase (line 254) and returns the first matching branch. For prix-guesser, `runtime_dirs = [".codex", ".claude"]` ([UPLIFT-MANIFEST.json:9-12](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:9)) makes `any(runtime_dir != ".codex" ...)` true, so cross-runtime wins and mid-phase is unreachable.
- [e:c+i] The repo is also at a pre-rerun Phase 01 boundary per [AGENTS.md:43](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:43) and [STATE.md:4-6](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:4). `STATE.md`'s `status: planning` means `active_phase` is true per [project_uplift.py:309](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:309). The mid-phase signal exists for the dogfood repo, but the classifier does not surface it.
- [d:r:i] That shadow matters because the dogfood case is the single live example the slice has. The mid-phase class is reachable on repos without a second runtime dir, but prix-guesser's own uplift memory does not record mid-phase posture at all. The bundle's prior reread introduced mid-phase as a class without specifying orthogonality; the live code took the simpler single-axis path. The compression thins the signal most on the repo whose dogfood behavior the team actually rereads.

### 2. Fingerprint shape is uniform content-hash across every carrier

- [e:c+i] Every file carrier's fingerprint is `sha256_text(text)` at [project_uplift.py:175](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:175). Every marker carrier's fingerprint is also `sha256_text(text)` where `text` is the full file contents, at [project_uplift.py:201](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:201).
- [e:c+i] The prior reread revision §2 specifically asked for per-carrier shape: `version-stamp for CLAIM-TYPES.md/LONG-ARC.md/AGENTS.md when those carry a doctrine-vintage marker; content hash for CLAUDE.md wrappers; section-list hash for tooling inventory; registry-file hash for .codex/config.toml` (see [03-revised-*-reread-opus47-max-r1.md:167](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/entry-uplift-audit/outputs/03-revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1.md:167)).
- [d:r:i] Uniform content-hash is the simplest first-slice choice, but it carries two costs. First, a whitespace-level edit anywhere in a carrier changes the fingerprint, so `progress` will recommend `$gsd-uplift-project --detect-only` after a typo fix in `AGENTS.md`. Second, for marker carriers the whole file is hashed even though the doctrine carry is the marker, so unrelated edits to `.codex/get-shit-done/workflows/discuss-phase.md` produce noise against strengthening-route stability. The per-carrier shape pressure the prior reread named as a concrete contract has not yet landed; the uniform shape is the implicit contract.

### 3. Mid-phase detection is coarse relative to the prior reread's specific signal

- [e:c+i] The mid-phase branch at [project_uplift.py:254](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:254) fires on `active_phase and (not has_manifest or doctrine_changed or pending_doctrine_sensitive or absent_additive)`.
- [e:c+i] The prior reread's revision §1 named the detection signal as: "the active phase's `CONTEXT.md` lacks a rerun-boundary stamp while governing doctrine has moved since the `CONTEXT.md` was authored" ([03-revised-*.md:163](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/entry-uplift-audit/outputs/03-revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1.md:163)).
- [d:r:i] The live check reads nothing from per-phase `CONTEXT.md` and nothing about rerun-boundary stamps. Any active-phase drift triggers mid-phase; a repo with a clean active phase and a stale `CONTEXT.md` that has not been rerun under current doctrine would not be detected. `38` §6 put `per-phase CONTEXT.md` first among rerun-boundary carriers; the helper's mid-phase branch does not touch that carrier.

### 4. Runtime registry carriers are hardcoded to a three-file subset

- [e:c+i] `FILE_CARRIERS` at [project_uplift.py:64-66](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:64) names exactly three runtime registry files: `.codex/config.toml`, `.codex/agents/gsd-planner.toml`, `.codex/agents/gsd-plan-checker.toml`.
- [e:c+i] The bundle's `38:147-153` named `.codex/config.toml` and `.codex/agents/*.toml` as primary runtime-side registry carriers.
- [d:r:i] A glob was compressed into two named agent TOMLs. Any additional agent TOML added later — `gsd-executor.toml`, `gsd-verifier.toml`, etc. — is invisible to the detector. The manifest's runtime_registry slice will report present/absent for the two named agents while silently missing the rest. That is a bounded compression (two agents are the most load-bearing), but it ages out of correctness as the agent set grows.

### 5. Doctrine-sensitive proposal routes are named in concept but generate nothing yet

- [e:c+i] `analyze_repo` computes `pending_doctrine_sensitive_proposals` only from absent doctrine-sensitive carriers at [project_uplift.py:304-308](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:304).
- [e:c+i] The bundle's `39:156-159` named four doctrine-sensitive proposal routes: diffs/proposals for root/planning `AGENTS.md`, root/planning `CLAUDE.md`, required-reading practice, and strengthening-route carry.
- [d:r:i] The live helper does not generate any proposal artifact. It lists absent doctrine-sensitive carriers and names those as "pending proposals." For prix-guesser the list is empty because all doctrine-sensitive carriers are present — so the field reads as `[]` in the manifest, which conflates "no proposals needed" with "no proposal pipeline exists." A reader cannot tell from the durable outputs whether the proposal lane is quiet because there is nothing to propose or because the lane is not yet implemented. The prior reread kept the proposal-generation lane explicit by splitting the routes; the live slice implicitly folded the proposal-generation lane into the absent-carrier detector.

### 6. Cross-runtime detection is presence-only rather than fingerprint-comparing

- [e:c+i] The cross-runtime branch at [project_uplift.py:252-253](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:252) fires on `any(runtime_dir != ".codex" for runtime_dir in runtime_dirs)`. The runtime registry carriers are fingerprinted, but the cross-runtime signal itself does not compare `.codex` and `.claude` registry fingerprints or wrapper alignment between them.
- [d:r:i] For the dogfood case the signal fires correctly, but it fires because `.claude/` exists, not because the two runtimes carry different posture. A repo with `.codex/config.toml` pointing at GPT-5.4 and `.claude/` pointing at Claude Opus 4.7 and a repo with both runtimes in perfect posture alignment would classify identically. `38` §8's placement pressure was registry-as-primary for cross-runtime posture; the live detection treats cross-runtime as a directory-presence boolean and leaves the registry-comparison work for later.

### 7. Marker carrier fingerprint scope is file-wide rather than marker-local

- [e:c+i] For marker carriers, the fingerprint is `sha256_text(text) if marker_present and text is not None else None` at [project_uplift.py:201](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:201), where `text` is the whole file contents read at line 182.
- [d:r:i] Two carry questions sit on one hash: "is the marker present" (already recorded in `status`) and "has the marker's surrounding content stayed stable." An edit to `.codex/get-shit-done/workflows/discuss-phase.md` that leaves the strengthening-route section untouched changes the fingerprint, so the doctrine hash moves and `progress` recommends detect-only. The marker-scoped hash the bundle implied (because the strengthening-route carry is a section, not the whole workflow) is not yet carried.

### 8. `build_progress_note` re-runs a full `analyze_repo` on every invocation

- [e:c+i] `build_progress_note` at [project_uplift.py:537](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:537) calls `analyze_repo(repo_root)`, which rebuilds every carrier entry from disk and recomputes every fingerprint.
- [d:r:i] The name "progress-note" suggests reading the manifest; the implementation reads the repo. That is defensively correct — it catches doctrine drift the manifest has not yet seen — but it means `progress` is doing a 14-carrier SHA scan per invocation. For a repo of this size the cost is small; at larger repos or with richer carrier sets, the consumer-side cost rises. A "structured signal" hook that re-does the full producer-side work is not as read-only as the name implies. The same fingerprint rule could be enforced by caching the live doctrine hash in a tiny extra artifact or by accepting staleness between explicit `detect` calls; neither path is required for first slice, but the current choice is the heavier one.

### 9. `HELD_LATER_FAMILIES` is a five-item Python constant rather than a spec or doc carrier

- [e:c+i] `HELD_LATER_FAMILIES` at [project_uplift.py:30-36](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:30) lists five items: `required-reading installation practice`, `cross-runtime uplift composition`, `upstream-template drift machinery`, `aged-bespoke deep merge`, `audit-subtree aging carry`.
- [e:c+i] The bundle's `39:91-99` first-slice hold-out list carries more than five items (no full reinstall, no full migration, no cross-project batching, no workstream reconciliation, no aged-bespoke deep merge, no full audit-tree restructuring, no doctrine-carrying audit-subtree vintage stamping, no full upstream-template expression pass, no broad doctrine-sensitive wrapper rewrites by default). The prior reread's "Later Families To Keep Explicit" list named roughly eleven items.
- [d:r:i] The constant compresses the full hold-out list into the five most load-bearing names. That is a legitimate first-slice choice for report surface, but it puts the held-family set in Python rather than in `39` or in a reference doc. Extending the list requires a code change; the list cannot be read by any tool other than the helper itself; `progress.md` does not reference the held-family set at all. The carrier for "what the first slice intentionally holds" is embedded where it is least visible to a doctrine reader.

### 10. `pending_doctrine_sensitive_proposals` has two silently conflated states

- [e:c+i] The field is populated at [project_uplift.py:304-308](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:304) with labels of doctrine-sensitive carriers whose `present` is false.
- [d:r:i] Semantically this carries two things under one name: "carrier absent, proposal needed to install" (for a truly missing `.planning/CLAUDE.md` on a vanilla repo) and "carrier present but fingerprint moved, proposal needed to refresh" (which the live code does not currently detect — a fingerprint delta on an already-present doctrine-sensitive carrier does not add the carrier to the pending list). The field name promises proposal routing; the implementation only fires on absence. The `progress` hook's `pending` check at [project_uplift.py:544](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:544) inherits the same conflation.

## What The Landed Mechanics Improve In Live Use

### Posture Classification

- [d:r:i] Posture classification now runs as a six-branch decision tree with one concrete classification outcome per repo state. `pre-uplift structural initialization` catches projects without `.planning/` scaffolding; `cross-runtime uplift` catches multi-runtime repos; `mid-phase uplift` catches active-phase drift; `vanilla uplift` catches wide absence with high additive/doctrine-sensitive pressure; `lightly aged uplift` catches narrower drift; `current-aligned posture` is the no-op. The six classes cover the family shape the bundle named, even though the mid-phase vs cross-runtime axis compression in §Thins/Compresses §1 shadows one live signal. Replacing the sequence with primary+secondary fields would preserve orthogonality without reopening the six-class design.

### Durable Uplift Memory

- [d:r:i] The three durable outputs (report, manifest, state section) are now written in one pass from one analysis payload, which means operator-visible prose, machine-readable fingerprints, and routing prose cannot disagree within a single run. The manifest's `schema_version: 1` at [UPLIFT-MANIFEST.json:2](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:2) is a first concession to later evolution; reports written by newer helpers can be recognized as schema-incompatible rather than silently read with wrong assumptions. The durable memory is now real rather than proposed, and the update semantics for `STATE.md` (pattern-replace-or-insert-before-session-continuity) keep the state carrier stable under repeated writes.

### Thin Manifest Carry

- [d:r:i] The thin manifest carries exactly what downstream consumers need without prose parsing: the class, both hashes, the current status, the runtime dir list, the recommendation, the reasons, the absent-additive list, the pending-doctrine-sensitive list, the held-later list, and the full carrier array with per-carrier `key`, `group`, `status`, `fingerprint`, `note`. The consumer reads the manifest through JSON deserialization, not through markdown parsing. That is the load-bearing gain the prior reread named as first-slice pressure; it has landed cleanly.

### Read-Only `progress` Consumption

- [d:r:i] `progress` now consumes uplift memory with one bash invocation and one JSON parse at [progress.md:131-147](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:131), and renders a section conditionally on `UPLIFT_NOTE.show`. The carry is real: progress output for a repo with no uplift memory stays unchanged; progress output for a repo with current uplift memory gains a five-line block naming last class, recommendation, reasons, and report/manifest paths. The consumer hook is the concrete surface where the producer's work reaches the operator.

### Detect-Only Routing

- [d:r:i] The helper's default mode is detect-only; `--write` must be explicit at [project_uplift.py:121](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:121). The overlay workflow at [uplift-project.md:12-14](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md:12) reinforces the default as a step discipline; the overlay skill at [SKILL.md:56-60](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md:56) repeats it. Three surfaces agree on the default posture, so an operator invoking the skill cannot accidentally start with a write. That triple-carry is load-bearing because the first slice does not widen install routes — detection is all it is expected to do without explicit consent.

### Post-Write Recommendation Hygiene

- [d:r:i] `post_write_analysis` is the named surface that prevents the durable artifacts from quoting a reason that was only true pre-write. The fix is one function, readable by any future reviewer, and the surface means a later contributor adding another transient reason has a known place to strip it rather than re-discovering the bug class. The regression resistance is higher than an inline filter would have given.

## What Still Deserves Revision Before Wider Follow-Through

These revisions are narrow, each bounded to the live helper or the manifest shape, and each closes a specific compression named in §Thins/Compresses. They should ship together as one harden-the-slice pass before any additive install routes or cross-runtime widening.

### 1. Make classification multi-axis so mid-phase survives cross-runtime on the dogfood repo

- [d:r:i] Replace the exclusive-branch `classify_project` at [project_uplift.py:250-260](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:250) with a primary class plus a secondary-flags field: primary stays the first matching class (or a new explicit precedence), but secondary flags accumulate orthogonal signals (`mid_phase`, `cross_runtime`, `doctrine_changed`, `has_pending_proposals`). Persist both in the manifest and mirror them in the `STATE.md` section so the dogfood repo records `primary: cross-runtime uplift; secondary: [mid-phase, doctrine-current]`. The report surface can still feature the primary class prominently; the secondary field keeps the shadowed signal alive for later passes.

### 2. Install per-carrier fingerprint shape rather than one uniform content hash

- [d:r:i] Carry the prior reread revision §2 into code. For `.planning/CLAIM-TYPES.md` and `.planning/LONG-ARC.md`, prefer an explicit version-stamp or doctrine-vintage line in the file's own header when the carrier exposes one, and fall back to content hash when it does not. For marker carriers, hash marker-scoped content (the bounded section the marker introduces plus its direct siblings) rather than the whole file. For `.codex/config.toml` and `.codex/agents/*.toml`, hash normalized TOML (key-sorted, whitespace-stripped) so formatting edits do not trigger drift. The carrier dataclasses already carry a `group` field; adding a `fingerprint_shape` discriminator keeps the change narrow.

### 3. Make mid-phase detection read per-phase `CONTEXT.md` rerun-boundary carry directly

- [d:r:i] The bundle's prior reread §1 detection signal names `CONTEXT.md` specifically. Extend the helper to scan `.planning/phases/<current-phase>/<n>-CONTEXT.md` for a rerun-boundary marker (or its absence plus a `doctrine_reference_changed` signal) and set the mid-phase branch condition on that carrier rather than on the coarser `active_phase and drift` heuristic. This makes the mid-phase class mean what `37:49-51` says it means, rather than firing whenever an active-phase repo has any uplift pressure.

### 4. Replace hardcoded agent TOMLs with `.codex/agents/*.toml` enumeration

- [d:r:i] Turn the runtime registry carrier portion of `FILE_CARRIERS` into a generated list: read `.codex/agents/*.toml` at classification time and produce one carrier entry per file with a derived `key`. Keep the dataclass contract; add a factory that expands `MarkerCarrierSpec`/`FileCarrierSpec` instances from a glob pattern. The inventory stays live as the agent set grows, and the manifest's runtime_registry slice matches what actually exists in `.codex/agents/`.

### 5. Scope the marker carrier fingerprint to marker-local content

- [d:r:i] Where `MarkerCarrierSpec` describes a section-level carry, hash only the matched section (marker line plus bounded block until the next heading of equal or higher level) rather than the whole file. The change is inside `build_marker_carrier` at [project_uplift.py:180-203](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:180). This cuts the noise floor on doctrine-changed recommendations when unrelated content around the marker drifts.

### 6. Distinguish `carrier absent` from `carrier present but fingerprint drifted` in `pending_doctrine_sensitive_proposals`

- [d:r:i] Extend the manifest field to carry one of two structured states per entry: `absent` (first-time install proposal) or `drifted` (refresh proposal, with the delta summarized). The `progress` consumer then renders the distinction operator-facing instead of showing a single "pending doctrine-sensitive proposals" count that collides two different states. This keeps the proposal-route lane explicit and forecloses the "everything empty looks like everything current" reading.

### 7. Move `HELD_LATER_FAMILIES` out of Python constants into a named reference

- [d:r:i] Carry the hold list in `.planning/audits/.../intervention-proposals/39-project-uplift-workflow-proposal.md` or a dedicated `tooling/codex/UPLIFT-HELD-LATER.md`, and load the file at runtime. That makes the hold list readable by operators and by other tools without importing the helper, and keeps extension of the list a documentation change rather than a code change.

### 8. Widen the synthetic verification set to cover orthogonality and whitespace noise

- [d:r:i] The current test set at [test_project_uplift.py:45-117](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_project_uplift.py:45) covers vanilla, lightly aged, and a write-then-mutate round trip. Add three cases: (a) a repo that is both active-phase and multi-runtime to assert that the manifest records both signals after revision §1 lands, (b) a whitespace-only edit to a doctrine-sensitive carrier to assert the fingerprint does not change after revision §2 lands, (c) a repo where a doctrine-sensitive carrier is present but its fingerprint differs from a prior manifest, to assert `drifted` appears in the pending list after revision §6 lands. These three cases turn the revision contracts into round-trip gates rather than design intent.

## Later Families To Keep Explicit

### Mid-Phase Routing Mechanics Inside `discuss-phase`

- [d:r:i] The first slice classifies and records mid-phase (once revision §1 above restores the shadowed signal). Defining what `discuss-phase` does when uplift memory shows mid-phase — how the steering brief gets reopened, what `CONTEXT.md` carries forward, how the rerun-boundary stamp is refreshed — stays with later family work. The detection/classification carry is what makes the later family implementable without retrofitting.

### Aged-Bespoke Uplift

- [d:r:i] A project whose governing docs carry bespoke local content needs section-level diff with bespoke carve-outs before any refresh. The first slice does not attempt this; the prior reread `03:200-202` held it explicitly; the live slice's hold (via `HELD_LATER_FAMILIES`) names `aged-bespoke deep merge`. The hold stays correct.

### Cross-Runtime Reconciliation Beyond Detection

- [d:r:i] The live slice detects the cross-runtime class via directory presence. The later family handles the actual reconciliation: registry-vs-wrapper alignment, cross-runtime agent-contract parity, instruction-file harmonization, and any refresh action that touches both `.codex/` and `.claude/`. That work carries its own blast radius and belongs in its own slice.

### Upstream-Template-Drift Detection And Diff

- [d:r:i] A project current on package version and local posture can still lag shipped upstream templates. The detection requires a carrier recording the upstream-template version the project was last aligned with; that carrier's design belongs in the upstream-drift slice itself. The live slice names `upstream-template drift machinery` in the hold list.

### Audit-Subtree Aging Machinery

- [d:r:i] Doctrine-carrying audit subtrees (this workspace being a live example) need per-audit doctrine-vintage stamps. The prior reread's revision §7 asked `39` to name this in the hold list; the live slice's `HELD_LATER_FAMILIES` names `audit-subtree aging carry`. The hold stays explicit; the machinery stays with audit-subtree aging work.

### Required-Reading Template Seeding Upstream

- [d:r:i] The first slice treats required-reading installation practice as a held later family. Propagating the practice upstream (into shipped templates that other repos inherit) is a different slice with different blast radius and different review path. The hold list names it explicitly.

### Workstream Parent↔Child Posture Reconciliation

- [d:r:i] Uplift memory can note workspace drift in reports when detected; actual parent-driven reconciliation stays with workstream-family work. The uplift workflow should not merge across workstreams.

### Forensics And Archived-Milestone Re-Entry

- [d:r:i] These stay specialist-owned. The uplift workflow can consume forensic output as one input where relevant, but forensics and archived-milestone re-entry each carry their own discipline and should not be absorbed.

### Routed-Entry Hooks In `resume-project`, `health`, `update`, `ingest-docs`, `new-milestone`

- [d:r:i] The first slice carries only the `progress` hook. Widening to the other five specialist surfaces can wait until live examples show which routing the operator actually wants. The `39:62-68` deferral remains correct; the live slice respects it.

### Aged-Bespoke Claim-Type Activation Across Load-Bearing Artifacts

- [d:r:i] The first slice treats `CLAIM-TYPES.md` reference install as write-if-absent. Activating claim notation across existing load-bearing artifacts rewrites content and requires explicit operator consent per `39:160-162`. That activation belongs with aged-bespoke slice work.

### Rich Doctrine-Manifest Content Diffs Beyond Thin Version-Marker Form

- [d:r:i] The first slice carries carrier-name → fingerprint pairs plus five-line metadata. Rich section-level content diffs, bespoke carve-out logic, and cross-carrier correlation land in later slices. Revision §2 above installs per-carrier fingerprint shape, which is narrower than rich diffs and reachable as a harden-the-slice move.

## Strongest Adjacent Strengthening Route

- [d:r:i] The strongest adjacent route is to harden the landed slice's signal quality before any widening. The concrete surface is the helper's fingerprint and classification layer; the concrete work is revisions §1, §2, §4, §5, and §6 from §What Still Deserves Revision above, shipped together as one bounded pass with the widened verification set in §8. Carry this as a named "harden-slice" sub-slice rather than as unnamed cleanup.
- [d:r:i] The reason to prefer this over widening into additive install routes (install `CLAIM-TYPES.md`/`LONG-ARC.md` on projects where they are absent) or into cross-runtime uplift follow-through: the additive install routes reach other repos, and cross-runtime follow-through reaches other runtimes, but both paths consume the same fingerprint and classification signals that the harden pass makes more honest. Installing `CLAIM-TYPES.md` on a lightly aged project is a write-if-absent action whose correctness is already clear; the install does not need the signal improvements. But a future additive install that triggers on `drifted` rather than `absent` does need them, and a cross-runtime reconciliation that depends on registry-fingerprint deltas needs normalized TOML hashing, not whitespace-sensitive content hashing. Hardening the signal layer is the leverage move because later routes inherit it.
- [d:r:i] The reason to prefer this over implementing the doctrine-sensitive proposal generation lane (diffs/proposals for `AGENTS.md`, `CLAUDE.md`, required-reading practice): proposal generation has its own design pressure (what does a proposal artifact look like; where does it live; what is the review workflow; how does acceptance feed back into the manifest) that deserves its own slice. The signal-hardening work is narrower and does not preempt proposal-lane design; in fact, once proposal generation lands, it can fire on both `absent` and `drifted` states, which revision §6 puts in place.
- [d:r:i] Verification route for the harden-slice: three new synthetic tests per revision §8 above, plus one dogfood rerun of `$gsd-uplift-project --detect-only --write` on prix-guesser itself. That rerun should produce a `primary: cross-runtime uplift; secondary: [mid-phase]` classification (after revision §1), and the marker carriers' fingerprints should be stable after whitespace-only touches to the surrounding workflow files (after revision §5). `scan_threshold_language.py` should continue to find no residue on the report surface; `audit_refmap.py verify` should stay clean against the audit root; `manifest_install_coherence.py` can be a later-gate addition once the runtime registry uses a glob. That verification set is narrower than a full two-case pilot and targets exactly the compressions this reread names.
- [d:r:i] If the next user preference is to widen rather than harden, the narrowest widening move is to expose the doctrine-sensitive proposal-generation lane as an explicit no-op stub (revision §6 above plus a placeholder writer that emits a `PROPOSAL-TODO.md` in the relevant location rather than nothing) — so the absence of proposal artifacts is visible rather than silently folded into carrier absence. That is smaller than implementing real proposals and smaller than additive install routes, and it keeps the proposal lane legible without committing to its internal design yet.

## How This Landed Slice Should Be Inherited

### Carry Forward

- [d:r:i] `tooling/codex/project_uplift.py` as the single-module helper with dataclass-typed carrier specs and a two-subcommand CLI (`detect`, `progress-note`).
- [d:r:i] Detect-only as the default mode with explicit `--write` required for durable output, enforced across helper (argparse), overlay workflow, and overlay skill.
- [d:r:i] The six-class classifier with `pre-uplift structural initialization`, `cross-runtime uplift`, `mid-phase uplift`, `vanilla uplift`, `lightly aged uplift`, and `current-aligned posture` as live outcomes.
- [d:r:i] `FileCarrierSpec` vs `MarkerCarrierSpec` as orthogonal carrier types with three-state status for marker carriers (`marker_present`, `marker_absent`, `absent`).
- [d:r:i] `build_progress_note` as the read-only consumer entry that reads the manifest as authoritative fingerprint source and `STATE.md` as narrative companion.
- [d:r:i] `.codex/get-shit-done/workflows/progress.md:131-147` as the first live routed consumer with conditional section rendering on `UPLIFT_NOTE.show`.
- [d:r:i] `post_write_analysis` as the named transient-reason stripper, separating pre-write detection from post-write durable record.
- [d:r:i] `update_state_section` with pattern-replace-or-insert-before-session-continuity as the `STATE.md` uplift section contract.
- [d:r:i] `.planning/UPLIFT-REPORT.md`, `.planning/UPLIFT-MANIFEST.json`, and the `## Project Uplift` section in `.planning/STATE.md` as the three durable outputs from one write pass.
- [d:r:i] The manifest's `schema_version: 1` field as the first concession to later schema evolution.
- [d:r:i] `tooling/codex/README.md` as the concrete tooling inventory carrier (bundle named the role; live slice pointed it at a real file).
- [d:r:i] The tracked-overlay + setup-portable-gsd.sh materialization chain as the live runtime posture for the workflow and skill, preserving materialization authority per `RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:33-42`.
- [d:r:i] The dogfood classification as `cross-runtime uplift` (rather than a convenient `current-aligned posture`) on prix-guesser itself.
- [d:r:i] `test_project_uplift.py` covering vanilla, lightly aged, and write-then-doctrine-change round trip as the baseline synthetic verification set.

### Revise Before Widening

- [d:r:i] Replace exclusive-branch classification with primary + secondary axis so mid-phase survives cross-runtime on the dogfood repo (revision §1).
- [d:r:i] Install per-carrier fingerprint shape rather than uniform content hash — version-stamp where available, normalized TOML for registry files, section-list for inventory, marker-local for marker carriers (revision §2).
- [d:r:i] Make mid-phase detection read per-phase `CONTEXT.md` rerun-boundary carry directly rather than inferring from `active_phase and drift` (revision §3).
- [d:r:i] Replace hardcoded agent TOML list with `.codex/agents/*.toml` glob expansion (revision §4).
- [d:r:i] Scope marker carrier fingerprints to marker-local content rather than whole-file (revision §5).
- [d:r:i] Distinguish `absent` from `drifted` in `pending_doctrine_sensitive_proposals` so the field stops silently conflating two states (revision §6).
- [d:r:i] Move `HELD_LATER_FAMILIES` out of Python constants into a named reference doc loadable at runtime (revision §7).
- [d:r:i] Widen the synthetic verification set with orthogonality, whitespace-noise, and drifted-but-present cases (revision §8).

### Hold For Later

- [d:r:i] Mid-phase routing mechanics inside `discuss-phase` — first slice classifies and records; later family defines what the route does.
- [d:r:i] Aged-bespoke refresh with section-level diff and bespoke carve-out detection.
- [d:r:i] Cross-runtime reconciliation action beyond directory-presence detection — registry parity, wrapper alignment, instruction-file harmonization.
- [d:r:i] Upstream-template-drift detection and diff, with a dedicated upstream-version carrier.
- [d:r:i] Audit-subtree aging machinery for doctrine-carrying subtrees, including per-audit doctrine-vintage stamps.
- [d:r:i] Required-reading template seeding upstream into shipped templates.
- [d:r:i] Workstream parent↔child posture reconciliation across workspaces.
- [d:r:i] Forensics and archived-milestone re-entry integration — uplift can consume outputs; these stay specialist-owned.
- [d:r:i] Routed-entry hooks in `resume-project`, `health`, `update`, `ingest-docs`, `new-milestone` beyond the first `progress` hook.
- [d:r:i] Aged-bespoke claim-type activation across existing load-bearing artifacts (reference install may sit in first slice via a later additive route; activation is explicit-consent rewrite work).
- [d:r:i] Rich doctrine-manifest content diffs with bespoke carve-out logic and cross-carrier correlation.
- [d:r:i] Doctrine-sensitive proposal-generation lane (beyond revision §6's explicit-state distinction) — actual proposal artifact shape, review workflow, and acceptance-feedback wiring belong in the proposal-generation slice itself.

## Internal Coherence Notes

- [d:r:i] This reread challenges the landed slice from `tooling/codex/project_uplift.py`, `tooling/codex/tests/test_project_uplift.py`, the tracked overlay workflow and skill, the materialized `.codex/get-shit-done/workflows/progress.md`, and the three durable outputs under `.planning/` — not from memory of the bundle's own prior reread. Each `[e:c+i]` claim cites a file and line in the live surface.
- [d:r:i] The revisions named in §What Still Deserves Revision are narrower than the prior reread's eight-item pre-implementation list; they are post-implementation harden-slice moves rather than pre-implementation harmonization. That shift reflects the live slice's actual carry: the eight prior revisions closed the bundle's open seams; the eight here close the live helper's implementation compressions.
- [d:r:i] Threshold-language and deficit-pseudo-positive bans from [AGENTS.md:53-56](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:53) and [.planning/AGENTS.md:156-163](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:156) shape this review's phrasing. Where the live helper's own report surface could regress into threshold shape (e.g., "Recommendation: Continue with current routing" at [UPLIFT-REPORT.md:6](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:6)), that phrasing already avoids adequacy/threshold language, so the scan gate at `39:227` continues to have a clean target.
- [d:r:i] The strongest adjacent route recommended here is a harden-slice pass, not another bundle-level review. The carry logic is: the first-slice producer now exists; the consumer now exists; the three durable outputs now exist; what sharpens next-slice leverage most is fingerprint and classification signal quality, because every later slice inherits those signals.
