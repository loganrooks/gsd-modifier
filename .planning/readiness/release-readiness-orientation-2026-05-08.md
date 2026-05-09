# Release Readiness Orientation — 2026-05-08

Date: 2026-05-08
Repo: `/home/rookslog/workspace/projects/gsd-modifier`
Branch: `main` (in sync with `origin/main`)
Head: `135ea14`
Status: snapshot orientation artifact, dated, archive on close
Authority: not a re-entry doc; `docs/handoff/current.md` retains that role

## Role

Snapshot synthesis written to enable downstream proposals after the 2026-04-24 temp handoff (`docs/handoff/DELETE-AFTER-INGESTION-2026-04-24-release-readiness-and-plan-004.md`) was found to rest on a premise that has shifted. Read once, drive proposals, then archive.

This file is **not** a competing `current.md`. It does not declare new accepted direction. Its job is to lay out evidence and recommend specific approval-gated next moves.

## Sections

1. Active state verified
2. Upstream gap snapshot (2026-04-24 → 2026-05-08)
3. Plan 004 disposition with corrected premise
4. Drift inventory (overlay carriers vs current upstream)
5. Posture recommendation (uplift mode shape)
6. Long-horizon framing revised against shipped upstream
7. Proposed next moves (numbered, separately approvable)
8. Disposition for this artifact

---

## 1. Active state verified

| Claim | Source | Verified |
|---|---|---|
| Branch is `main` | `git branch --show-current` | yes |
| In sync with `origin/main` | `git status --short --branch` shows `## main...origin/main` | yes |
| Head: `135ea14 fix(workflow): clarify approval process for architectural changes` | `git log --oneline -1` | yes |
| `AGENTS.md` governance edit landed | head commit message + AGENTS.md present at root | yes — the temp handoff's "uncommitted AGENTS.md" claim is now stale; the edit landed as `135ea14` |
| Only untracked file is the temp handoff itself | `git status --short` | yes |
| Repo-self proof gates last passed | asserted by handoff; **not re-run in this read-only pass** | not re-verified |
| Synthetic host matrix `status: ok` | `.planning/measurement/host-exercise-matrix/matrix-summary.json`, asserted by handoff | not re-verified |

**Gates not re-run in this pass.** Per the orientation pass scope (read-only), I did not run `check-deterministic.sh`, `check-bootstrap.sh`, or the host matrix. They write to `.planning/measurement/` and are state-mutating. They should be re-run as part of any downstream proposal that touches their inputs.

**Stale claim from the temp handoff to discard.** The handoff says "branch is ahead of `origin/main`" and "uncommitted change in `AGENTS.md`". Neither is true now. The governance edit landed two weeks ago.

## 2. Upstream gap snapshot

Upstream reference: `~/workspace/projects/get-shit-done-upstream` (`gsd-build/get-shit-done`), refs refreshed via `git fetch --all --tags --prune` in this pass. Comparing the period from the handoff date (2026-04-24) to today (2026-05-08).

### 2.1 Tags shipped in the gap

```
v1.38.4   2026-04-25
v1.38.5   2026-04-25
v1.39.0   2026-05-01 (rc cycle)
v1.39.1   2026-05-01 (hotfix)
v1.39.2   ...
v1.40.0   ...
v1.41.0   2026-05-07 (latest stable)
```

Plus rc and `v1.50.0-canary.{1,2}` on the canary channel.

`origin/main` advanced `1e6737cd..96806003` (10+ commits).

### 2.2 PR #2341 (`c5b14455`) status

`git tag --contains c5b14455` confirms the commit ships in **v1.38.4 onward**, including every stable release since the handoff was written. The handoff's "release-bound shim" framing is therefore obsolete on its own terms — there is no remaining release window to shim across.

### 2.3 Material upstream changes that touch modifier overlay surface

Drawn from `CHANGELOG.md` on `origin/main` for the v1.41.0 / v1.39.x / v1.38.x sections. Listed by overlay-impact severity, not chronologically.

| Upstream change | Source PR | Overlay impact |
|---|---|---|
| Skill consolidation 86 → 59 (#2790, #2824); 31 micro-skills deleted incl. `do`, `from-gsd2`, `plant-seed`, `note`, `add-todo`, `add-backlog`, `check-todos`, `next`, `intel`, `code-review-fix`, `research-phase`, `list-phase-assumptions`, `plan-milestone-gaps`, `analyze-dependencies`, `from-gsd2`, `session-report`, `join-discord`, `scan`, `set-profile`, `settings-advanced`, `settings-integrations`, `add-phase`, `insert-phase`, `remove-phase`, `edit-phase`, `new-workspace`, `list-workspaces`, `remove-workspace`, `sync-skills`, `reapply-patches`, `sketch-wrap-up`, `spike-wrap-up` | #2790, #2824 | **Overlay declares stale skills** — see §4.2 |
| Six namespace meta-skills (`gsd:workflow`, `gsd:project`, `gsd:review`, `gsd:context`, `gsd:manage`, `gsd:ideate`) replace flat 86-skill listing with two-stage routing | #2792 | **Architectural** — modifier hasn't adopted; defer decision |
| `--minimal` install flag writes only main-loop core skills (~700 tokens vs ~12k); install manifest records `mode: "minimal" | "full"` | #2762 | **New install dimension** — modifier's `codex-core`/`claude-core`/`dual-runtime-core` profiles predate this; intersection is open |
| `/gsd-edit-phase` command | #2617 | New surface; not in overlay |
| Slash-command namespace standardized: `/gsd-<cmd>` (hyphen) is canonical user-typed form, `gsd:<cmd>` (colon) reserved for internal `Skill(skill="...")` invocation | #2855, #2768/#2783, #2697 | **Modifier overlay needs to be checked for stale `/gsd:<cmd>` slash references** — see §4.4 |
| SDK ships prebuilt in tarball; `--sdk` flag semantics changed | #2441/#2453 | **Install behavior changed** — affects bootstrap proof; modifier already calls `gsd-sdk query` |
| `gsd-tools.cjs` formally deprecated; `gsd-sdk` is canonical surface; `gsd-tools` bin alias added | #2791 | **Plan 004 decision intersects** — modifier overlay's wrapper still relevant; see §3 |
| Codex installer + hooks hardening: legacy `[agents]`/`[[agents]]` strip, `[[hooks]]` migration, atomic write with TOML validation | #2760, #2727, #2637, #2809, #2866 | **Directly bears on `codex-core` / `dual-runtime-core` proof**; rerun host matrix recommended |
| `gsd-read-injection-scanner` PostToolUse hook actually ships now (was missing from `HOOKS_TO_COPY` allowlist for two minor versions) | #2406 | New hook; not yet in overlay |
| Hotfix release flow auto-cherry-picks fixes from main; bundles SDK; cumulative-fix anchor model | #2955 | **Direct analog to "release-bound patch representation" guardrail question** |
| Canary release workflow on `dev` branch with `canary` dist-tag | #2828, #2868 | Release infra; modifier may want a simpler analog |
| Shipped-paths classifier (`scripts/diff-touches-shipped-paths.cjs`) for hotfix cherry-pick filtering with explicit exit-code semantics | #2980, #2983 | **Direct analog to "what should fail CI when upstream changes break overlay assumptions"** |
| Phase-lifecycle status-line read-side: `parseStateMd` reads `active_phase`, `next_action`, `next_phases`, `progress` | #2833 | New STATE.md frontmatter fields; modifier consumes STATE.md |
| `buildStateFrontmatter` counts nested `plans/<N>-PLAN-<NN>-<slug>.md` files | #3261 | Affects nested plan layout, which `gsd-modifier` uses |
| `gap-analysis` parses non-`REQ-` requirement IDs (e.g. `TST-`, `BACK-`, `INSP-`) and ignores traceability table headers | #2897 | Modifier overlay does not declare `gap-analysis` carriers; minor |
| `audit-uat` reads `human_verification:` from frontmatter array | #2788 | Affects UAT parsing if modifier uses it |
| Workstream config inheritance: deep-merge of root + workstream config | #2714 | Modifier may benefit |
| `extractCurrentMilestone` no longer truncates at heading-like lines inside fenced code blocks | #2787 | Bug-class fix; if modifier ROADMAP has fenced code, was potentially affected |

### 2.4 Latent risk indicator

The CHANGELOG records that on **2026-04-25** (one day after the handoff was written) v1.38.4 shipped with major SDK behavior changes — full installed agent/workflow prompts loaded at runtime, plan content actually passed to executor, verification reads VERIFICATION.md. These are SDK runner behavior changes that may affect anyone routing through `gsd-sdk query` — modifier included. If the bootstrap gate hasn't been re-run against latest upstream surface, claims about runtime behavior in the handoff are dated.

---

## 3. Plan 004 disposition with corrected premise

### 3.1 Premise correction

The temp handoff frames `4a32421 fix(instructions): preserve runtime instruction targets` as **suspect** and recommends review for whether to revert / shim / supersede. The framing rests on the claim that the modifier's local generator wrapper is a workaround for the v1.38.3 `--output` bug, which upstream `main` has fixed.

This premise is wrong on its own terms. Reading the actual artifacts:

**Plan 004 PLAN.md (`.planning/implementation-plans/20260424T082720Z/concrete-plans/004-generator-owner-and-command-contract/PLAN.md`)** explicitly enumerates four options (A: repo-owned wrapper, B: upstream defect, C: CJS direct, D: companion contract). It states implementation is allowed only after the decision artifact names an option.

**The decision artifact (`evidence/decision.md`)** was written and the implementation tail proceeded under **Option A: Repo-Owned Runtime-Neutral Wrapper**. Commit `4a32421` is that authorized implementation tail. Its boundary statement reads: "keeps the repo-owned wrapper as a file-write repair only. It does not switch back to upstream CJS template generation, add companion instruction files, or change broader uplift/catalog behavior."

**The wrapper has independent modifier-specific value beyond the v1.38.3 bug**, visible in the actual code at `tooling/portable-gsd/overlay/get-shit-done/bin/generate-instruction.cjs`:

| Wrapper feature | Evidence (file:line) | Why upstream's writer cannot supply it |
|---|---|---|
| `--runtime` flag for runtime-targeted output path | `generate-instruction.cjs:56` | Upstream's `generateClaudeMd` writes a Claude-specific file; modifier needs neutral target driven by `$RUNTIME` env |
| Multi-runtime skill discovery across `.codex/skills/`, `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/` | `generate-instruction.cjs:47` | Upstream's writer is Claude-context only |
| `## GSD Workflow Enforcement` section with modifier-specific entry-point guidance | `generate-instruction.cjs:29-38` | Modifier-owned content; upstream does not write equivalent |
| `<!-- GSD:profile-start -->` placeholder for `$gsd-profile-user` | `generate-instruction.cjs:39-46` | Modifier-specific carrier |
| Marker-section update model (`<!-- GSD:project-start source:... -->`) preserving user content outside markers | `generate-instruction.cjs:212-228` | Modifier-specific update policy |

**Workflow-side evidence.** `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md:1273-1274` explicitly invokes the modifier wrapper:

```bash
GSD_INSTRUCTION_GENERATOR="$GSD_RUNTIME_ROOT/get-shit-done/bin/generate-instruction.cjs"
node "$GSD_INSTRUCTION_GENERATOR" --output "$INSTRUCTION_FILE" --runtime "$RUNTIME"
```

Upstream's `new-project.md` at the same line range still calls `gsd-sdk query generate-claude-md --output "$INSTRUCTION_FILE"` — upstream did not migrate to a runtime-neutral generator. The modifier's wrapper provides a feature upstream does not.

**Manifest-side evidence.** `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` declares `get-shit-done/bin/generate-instruction.cjs` with `parity_tier: core_required`, `mode: add` for both codex and claude. Marked as repo-owned, not an overwrite of an upstream file.

### 3.2 Recommended disposition

**Keep `4a32421` and the wrapper.** Update Plan 004's disposition record to capture the corrected upstream evidence (#2341 has shipped since the decision was made; this does not change the decision).

The handoff's three options collapse to one defensible choice:

| Handoff option | Verdict | Reason |
|---|---|---|
| Revert all of `4a32421` | reject | Removes modifier-specific multi-runtime skill discovery, GSD enforcement section, and runtime-targeted output. Loses real capability for a non-existent gain. |
| Mark wrapper as release-bound shim | reject | Premise is wrong — wrapper is not a shim, it owns content upstream does not produce. |
| Restore overlay closer to upstream intent while keeping modifier-specific behavior | already done | The wrapper *is* that posture: file-write repair only, no broader uplift/catalog behavior. |
| Keep wrapper permanently and document why | recommended | Matches Plan 004 Option A's explicit decision; matches the boundary statement in `4a32421`. |

### 3.3 What remains to do for Plan 004

A small disposition update — not a behavior change. Specifically:

1. Append to `.planning/implementation-plans/20260424T082720Z/concrete-plans/004-generator-owner-and-command-contract/evidence/implementation-disposition.md` (or write if absent) a "Premise Update 2026-05-08" section noting:
   - PR #2341 / commit `c5b14455` shipped in v1.38.4 (2026-04-25) and is in v1.41.0 (latest)
   - This does not invalidate Option A; the wrapper has modifier-specific value beyond the v1.38.3 bug
   - The handoff's "release-bound shim" framing is rejected; the wrapper is repo-owned content, not a release-window patch
2. No source/contract/manifest edits needed.

**This is an evidence-only commit. Conventional Commit subject suggestion: `docs(planning): update plan 004 disposition with shipped upstream evidence`.**

---

## 4. Drift inventory — overlay carriers vs current upstream

Method: enumerate overlay carriers declared in `OVERLAY-MANIFEST.json`, compare each against `origin/main` of `~/workspace/projects/get-shit-done-upstream`. Classification:

- **aligned** — carrier still has an upstream analog at the expected path
- **stale-deleted** — upstream removed the entry in the gap; overlay still declares it
- **stale-renamed** — upstream renamed/absorbed; overlay carrier name no longer canonical
- **modifier-owned-net-new** — overlay declares as `mode: add` from `harness_modifier/overlay/...`; not a copy of upstream
- **needs-content-resync** — both still exist, but upstream content has materially changed since modifier's copy was taken
- **not-checked** — out of scope for this pass

### 4.1 Overlay agent files

`agents/gsd-code-fixer.{md,toml}`, `agents/gsd-code-reviewer.{md,toml}`, `agents/gsd-executor.toml`, `agents/gsd-intel-updater.{md,toml}`, `agents/gsd-pattern-mapper.{md,toml}`, `agents/gsd-phase-researcher.toml`, `agents/gsd-plan-checker.toml`, `agents/gsd-planner.toml`, `agents/gsd-verifier.toml` → **status: not-checked-for-content-drift**

These are upstream agents the overlay materializes. The CHANGELOG cites #2363, #2361, #2368 as content edits to `gsd-debugger`, `gsd-planner`, `gsd-executor`, `gsd-phase-researcher`, `gsd-verifier`, `gsd-doc-writer`, `gsd-debugger`. Overlay copies of these may be drifted from current upstream content.

**Action**: a content-drift sweep of overlay agent .md files vs upstream is recommended but not required for the immediate disposition slice. Defer to short-horizon item (§7).

### 4.2 Overlay skills — confirmed stale

| Overlay carrier | Upstream status (`origin/main`) | Classification |
|---|---|---|
| `skills/gsd-do/SKILL.md` (`mode: overwrite`) | upstream `commands/gsd/do.md` **deleted** in #2790 (absorbed into `progress --do`) | **stale-deleted** |
| `skills/gsd-from-gsd2/SKILL.md` (`mode: overwrite`) | upstream `commands/gsd/from-gsd2.md` **deleted** in #2790 | **stale-deleted** |
| `skills/gsd-plant-seed/SKILL.md` (`mode: overwrite`) | upstream `commands/gsd/plant-seed.md` **deleted** in #2790 (absorbed into `capture --seed`) | **stale-deleted** |

Verified by:
```bash
cd ~/workspace/projects/get-shit-done-upstream && git ls-tree origin/main commands/gsd/{do,from-gsd2,plant-seed}.md
```
returns empty for all three.

**Implication**: when `dual-runtime-core` materializes for a runtime where these skills come from upstream, the overlay's `overwrite` mode is overwriting nothing. For codex (where these are routed through `skills/`), the overlay still works because codex doesn't read `commands/gsd/` — but the modifier carriers are unmaintained against an upstream that no longer ships these.

**Question for downstream proposal**: keep modifier-owned versions of these skills (and reclassify as `mode: add` from `harness_modifier/overlay/`), or delete from overlay because users on current upstream don't need them?

### 4.3 Overlay skills — likely modifier-owned-net-new

| Overlay carrier | Upstream status | Classification |
|---|---|---|
| `skills/gsd-rigorous-research/SKILL.md` + 3 references (`mode: add`, codex only) | `commands/gsd/rigorous-research.md` **does not exist** upstream | **modifier-owned-net-new** |

Likely intentional. Confirms the manifest's `mode: add` (not `overwrite`) is the right pattern for net-new content. No drift concern; this is overlay extending upstream, not mirroring it.

### 4.4 Overlay workflows — likely stale rename

| Overlay carrier | Upstream status | Classification |
|---|---|---|
| `get-shit-done/workflows/do.md` (`mode: overwrite`) | upstream did not delete the workflow file, but the *skill that invoked it* was absorbed into `progress`. The workflow's body may still exist or have been refactored. | **needs-check** |
| `get-shit-done/workflows/plant-seed.md` (`mode: overwrite`) | same shape as `do.md` | **needs-check** |
| `get-shit-done/workflows/research-phase.md` (`mode: overwrite`) | upstream deleted the corresponding skill; workflow file status open | **needs-check** |

Not blocking; these workflows still execute when invoked. Deferred to short-horizon sweep.

### 4.5 Overlay net-new modifier-owned features

The manifest declares three modifier-owned entrypoints with cross-runtime materialization:

| Capability | Codex target | Claude target | Source |
|---|---|---|---|
| `entrypoint.gsd-propagation-review` | `skills/gsd-propagation-review/SKILL.md` | `commands/gsd/propagation-review.md` | `harness_modifier/overlay/...` |
| `entrypoint.gsd-seed-migration-inventory` | `skills/gsd-seed-migration-inventory/SKILL.md` | `commands/gsd/seed-migration-inventory.md` | same |
| `entrypoint.gsd-uplift-project` | `skills/gsd-uplift-project/SKILL.md` | `commands/gsd/uplift-project.md` | same |

`parity_tier: core_adapted`. These are net-new modifier capabilities and are correctly modeled. No drift.

### 4.6 Overlay generator wrapper

| Overlay carrier | Upstream status | Classification |
|---|---|---|
| `get-shit-done/bin/generate-instruction.cjs` (`mode: add`, both runtimes) | upstream has `bin/lib/profile-output.cjs` writing a Claude-only file; functionally distinct | **modifier-owned-net-new** (not a shim) |

See §3 for full disposition.

### 4.7 Overlay lib/*.cjs files

`get-shit-done/bin/lib/{config,roadmap,phase,state,audit}.cjs` (5 files, all `mode: overwrite`)

Upstream's `bin/lib/` now contains 40+ files (per `git ls-tree origin/main get-shit-done/bin/lib/`). Modifier overlays only 5. This means the modifier's overwrite covers 5 specific lib modules; upstream additions like `config-schema.cjs`, `state-command-router.cjs`, `model-catalog.cjs`, `model-profiles.cjs`, `init-command-router.cjs`, `planning-workspace.cjs`, etc. flow through unmodified.

**status: aligned** — overlay's narrow overwrite footprint is intentional and continues to work as upstream adds neighboring modules.

**Risk**: if upstream changes the *interface* of the 5 overlaid files in a backwards-incompatible way (e.g., extracts `planning-workspace.cjs` from `core.cjs` per #2900 — already shipped), modifier's overwrite may not match the new contract. Worth a content-resync check on the 5 overlaid files.

### 4.8 Overlay templates

7 template files, all `mode: overwrite`, both runtimes. **status: not-checked-for-content-drift**. Lower priority than agents/lib/workflows — templates are slower-moving.

### 4.9 Slash-command namespace check

Per #2855, upstream standardized: `/gsd-<cmd>` is canonical user-typed form, `gsd:<cmd>` (colon) reserved for internal `Skill(skill="...")` invocation. Modifier overlay needs a check for whether it carries any stale `/gsd:<cmd>` (slash + colon) references in workflow body text.

**Not run in this pass.** Cheap to spot-check via `grep -r "/gsd:" tooling/portable-gsd/overlay/`. Deferred to a downstream proposal.

### 4.10 Drift inventory summary

| Class | Count | Action class |
|---|---|---|
| aligned (or out of scope) | majority | none |
| stale-deleted (overlay declares, upstream removed) | 3 confirmed (`gsd-do`, `gsd-from-gsd2`, `gsd-plant-seed`) | reclassify or delete |
| stale-renamed | 0 confirmed (workflows in §4.4 need check) | TBD |
| modifier-owned-net-new (correctly modeled) | wrapper + 3 entrypoints + 1 skill | none |
| needs-content-resync | overlay agents (12 files), overlay templates (7), 5 lib/*.cjs | sweep recommended, not required for §3 disposition |

**Bottom line**: drift is real but bounded. Three confirmed stale-deleted skills are the primary surfaced finding. Plan 004 disposition is independently resolvable without tackling drift first.

---

## 5. Posture recommendation — uplift mode shape

### 5.1 Concrete examples from the inventory

The orientation pass surfaces examples that pressure-test the three archetypes from the prior conversation (A: config toggle, B: always-on, C: tiered-by-surface).

**Example 1** — Plan 004 disposition: this conversation followed the *propose-evidence-approve* discipline and surfaced that the temp handoff's premise was wrong. The discipline caught the error before any edit. **The discipline already works.** It is not theoretical; it is the operative posture as of `135ea14`.

**Example 2** — Stale-deleted skills (§4.2): three skill carriers reference upstream files that no longer exist. The current discipline did not catch this — there was no automated trigger. A manual `gsd-modifier`-vs-upstream-roster check (or analog of upstream's #2980 shipped-paths classifier) would have surfaced it on the next manifest validation. **Argues for an explicit guardrail surface, not a process change.**

**Example 3** — `4a32421` itself: the commit's boundary statement explicitly disclaims broader uplift/catalog scope. This is exactly the kind of explicit boundary AGENTS.md asks for. **The current commit-message discipline is sufficient when followed.**

**Example 4** — The handoff's existence: a temporary file that explicitly carries durable decisions and a delete-after-ingestion marker is a working pattern. It just needs to be picked up rather than persisting unread. **Argues for a read-and-disposition cadence, not a new mechanism.**

### 5.2 Recommendation: archetype-B with explicit change-class triggers, no toggle

The evidence does not justify a config-toggle posture. The risk that "uplift mode" becomes hidden architecture (something workflows quietly read and adapt to) is exactly the failure mode AGENTS.md was written to prevent. A toggle invites the kind of silent flattening between "work happening under uplift" and "work happening normally" that AGENTS.md §63 forbids.

The current AGENTS.md governance is already archetype-B-shaped. What's missing is *operational triggers* — concrete categories of change that always require the full propose-evidence-approve cycle, made explicit so neither operator nor agent has to infer from context.

Proposed trigger taxonomy (to be drafted into AGENTS.md or a referenced doc, not into a config setting):

1. **Overlay carrier add/remove** — any change to `OVERLAY-MANIFEST.json` entries or files under `tooling/portable-gsd/overlay/` (and `harness_modifier/overlay/`)
2. **Contract surface change** — anything under `harness_modifier/contract/`, `tooling/codex/audit_refmap.py`, `tooling/codex/scan_threshold_language.py`
3. **Install/bootstrap script change** — `scripts/setup-portable-gsd*.sh`, `scripts/ci/check-*.sh`
4. **Governance carrier change** — `AGENTS.md`, `CLAUDE.md`, `WORKFLOW.md`, `docs/handoff/current.md`, `.planning/STATUS.md`, `.planning/CURRENT-STATE.md`
5. **Plan disposition or premise change** — `evidence/decision.md`, `evidence/implementation-disposition.md`, any decision artifact

Out of scope (small mechanical fixes per AGENTS.md §58 still proceed):
- Documentation typos with no semantic change
- Test additions that confirm existing behavior
- Comment-only changes
- Whitespace/formatting confined to a single file

### 5.3 Guardrail surfaces — content for what the posture actually checks

Several handoff guardrail items already exist in code. The orientation surfaces what's there and what's missing:

| Guardrail | Existing carrier | Missing piece |
|---|---|---|
| upstream drift check | none built-in | **net-new** — proposed in §7 |
| overlay/source/materialized parity check | `harness_modifier/contract/portable_gsd_contract.py` (validate-manifest, verify-materialized) | trigger discipline — when does it run? |
| release-bound patch inventory | none | **net-new**; could mirror upstream's #2980 shipped-paths classifier model |
| contract propagation check | `tooling/codex/audit_refmap.py` | trigger discipline |
| source vs materialized verification distinction | `--source-only` flag on validate-manifest; `verify-materialized` separate | already operational |
| regression tests around bootstrap/new-project/instruction-file | `tooling/codex/tests/test_initialization_read_packet_contract.py` (added by `4a32421`) | broaden coverage |
| explicit plan disposition when upstream evidence changes | this orientation pass | could become a recurring discipline (e.g., "if upstream major version changes during a plan's execution, reopen its decision artifact") |

### 5.4 What the posture proposal looks like at write time

Single PR with two parts (or two commits):
1. AGENTS.md addendum: change-class triggers + the rule that any change in those classes requires the full propose-evidence-approve cycle. CLAUDE.md added as runtime-neutral governance (see §7 #2).
2. `.planning/readiness/posture-triggers.md` (or similar) with the operational checklist + linkage to existing contract tools.

No config field. No mode toggle. No two parallel codepaths. The posture is the discipline.

---

## 6. Long-horizon framing revised against shipped upstream

The temp handoff's "explicitly later" list and "potential guardrail surfaces" list, revisited with current upstream evidence.

### 6.1 Short term (active slice — proposable now)

Items the orientation directly enables. Each is approval-gated separately.

1. Plan 004 disposition update (§3.3) — evidence-only commit
2. Three stale-deleted skill carriers (§4.2) — reclassify as modifier-owned or remove
3. CLAUDE.md drafted (§7 #2) — runtime parity at the governance carrier
4. AGENTS.md change-class triggers + posture discipline (§5.4)
5. Temp handoff deletion (after the above lands and durable parts are absorbed)

### 6.2 Medium term (months, dependency-chained)

Items that depend on short-term landing or on additional evidence.

1. **Overlay content-resync sweep** — agent .md files (12), template .md files (7), 5 overlaid lib/*.cjs files. Goal: identify which need refresh, which are intentionally pinned, and record the boundary explicitly per §4 classification.
2. **Slash-command namespace audit** — grep overlay for stale `/gsd:<cmd>` slash references; correct to `/gsd-<cmd>` per #2855.
3. **Workflow stale-rename check** — verify `do.md`, `plant-seed.md`, `research-phase.md` workflow bodies on `origin/main`; reclassify or remove from overlay as appropriate.
4. **Upstream drift check tool** — small CI gate that, given the upstream reference clone path, reports overlay carriers whose upstream analog has been deleted/renamed since last sync. Modeled on but simpler than upstream's #2980 shipped-paths classifier.
5. **Re-run host matrix and bootstrap gate against current upstream** — once #1 is partially landed, re-establish the runtime baseline. Codex installer + hooks hardening (#2760, #2727, #2637, #2809, #2866) is the most likely site of change.
6. **Release-bound patch inventory** — durable home for the rare cases where a modifier patch genuinely is release-window-bound. Open question: needed at all if the wrapper-as-modifier-owned-content interpretation generalizes? May be a smaller artifact than the handoff anticipated.

### 6.3 Long term (defer or revisit when triggered)

Items the handoff classified as "explicitly later"; current evidence does not promote them.

1. Semantic merge tolerance for changed runtime-specific wrappers — still real. Upstream velocity (4 minor releases in 13 days) makes this more pressing in concept, but no concrete trigger fires yet.
2. Upstream-template drift compatibility beyond exact declared carriers — still real; defer until medium-term sweep #1 produces evidence.
3. Richer optional install profiles beyond core contract — partially intersected by upstream's `--minimal` (#2762). Open whether modifier should adopt that frame or extend its own.
4. Internal path collapse / overlay rehome cleanup — still later. The overlay split between `tooling/portable-gsd/overlay/` and `harness_modifier/overlay/` (visible in §4.5) is the kind of thing this would address. No urgency.
5. Modifier route vs own harness strategy revisit — upstream's namespace meta-skills (#2792) and `--minimal` (#2762) reshape this question. Worth revisiting only after medium-term tooling is in place.

### 6.4 Promoted items (handoff "later" → now active)

- "Explicit plan disposition when upstream evidence changes" (handoff guardrail item) — promoted to short-term as the §3 disposition update. Should become a recurring discipline triggered by upstream major-version change during plan execution.
- "Regression tests around bootstrap/new-project/instruction-file behavior" (handoff guardrail) — partially landed in `test_initialization_read_packet_contract.py` via `4a32421`. Medium-term: broaden to cover wrapper edge cases the upstream SDK now also handles, so divergence is testable.

---

## 7. Proposed next moves (numbered, separately approvable)

Each item below is a separate proposal. No edits proceed until each is individually approved, per AGENTS.md §49.

### 7.1 Plan 004 disposition update

- **Class**: governance / planning artifact
- **Write set**: `.planning/implementation-plans/20260424T082720Z/concrete-plans/004-generator-owner-and-command-contract/evidence/implementation-disposition.md` (append, or create if missing)
- **Verification**: `python3 tooling/codex/audit_refmap.py verify .planning/implementation-plans/20260424T082720Z`; `git diff --check`
- **Commit**: `docs(planning): update plan 004 disposition with shipped upstream evidence`
- **Boundary**: evidence-only; no source/contract/manifest changes
- **Why now**: closes the suspect-commit framing; locks in the corrected premise so future readers don't re-litigate

### 7.2 Draft CLAUDE.md as runtime-neutral pointer with thin claude-specific addendum

- **Class**: governance carrier / runtime parity
- **Recommendation**: short CLAUDE.md that points at AGENTS.md as the runtime-neutral source of truth, plus any genuinely Claude-specific addenda. Both files share the runtime-neutral body; CLAUDE.md notes Claude-specific surface (e.g., `commands/gsd/` routing path, Claude-specific MCP context if any). AGENTS.md notes Codex-specific surface (e.g., `[[hooks.<Event>]]` config path).
- **Alternative considered**: full mirror — rejected because two duplicates drift.
- **Alternative considered**: empty CLAUDE.md or symlink — rejected because Claude Code auto-load conventions expect substantive content.
- **Write set**: `CLAUDE.md` (new); minor cross-reference edits in `AGENTS.md` to acknowledge `CLAUDE.md` as the Claude-side governance carrier; `docs/handoff/current.md` "Governing Surfaces" list updated to include `CLAUDE.md`
- **Verification**: `python3 tooling/codex/audit_refmap.py verify .` (governance docs change); `git diff --check`
- **Commit**: `docs(governance): add CLAUDE.md as runtime-parity governance carrier`
- **Why now**: completes runtime parity at the governance layer; without it, the dual-runtime story has a Claude-side gap

### 7.3 Reclassify the three stale-deleted skill carriers

- **Class**: overlay carrier change (triggers full discipline)
- **Three options to evaluate in the proposal**:
  - **3a**: Reclassify all three as `mode: add` from `harness_modifier/overlay/skills/` (modifier-owned versions); copy current SKILL.md contents from the overlay into the new modifier-owned location. Implication: modifier ships its own `gsd-do`, `gsd-from-gsd2`, `gsd-plant-seed` indefinitely.
  - **3b**: Remove all three from `OVERLAY-MANIFEST.json` and delete the overlay SKILL.md files. Implication: users on current upstream do not get these skills; modifier follows upstream's consolidation.
  - **3c**: Mixed — keep ones that have modifier value (likely `gsd-from-gsd2` if modifier still needs gsd2 import for any flow); drop the rest.
- **Decision reserved to operator** — orientation does not pick one
- **Write set varies by option**
- **Verification**: full bootstrap stack
- **Commit**: separate commit per option chosen

### 7.4 Add change-class trigger taxonomy to AGENTS.md (and CLAUDE.md)

- **Class**: governance carrier change
- **Write set**: AGENTS.md addendum after existing §49 (Workflow Rules); CLAUDE.md addendum if §7.2 has landed; `.planning/readiness/posture-triggers.md` (operational checklist)
- **Verification**: `python3 tooling/codex/audit_refmap.py verify .`; `python3 tooling/codex/scan_threshold_language.py --ignore-meta-instruction-lines ...`; `git diff --check`
- **Commit**: `docs(governance): explicit change-class triggers for propose-evidence-approve`
- **Boundary**: governance text only; no contract or runtime change

### 7.5 Delete the temp handoff after §7.1 + §7.4 land

- **Class**: governance carrier deletion
- **Write set**: delete `docs/handoff/DELETE-AFTER-INGESTION-2026-04-24-release-readiness-and-plan-004.md`
- **Precondition**: §7.1 has captured the durable disposition; §7.4 has captured the durable governance discipline; this orientation has captured the durable evidence
- **Commit**: `chore(handoff): delete ingested temp handoff for plan 004`
- **Why**: per the handoff's own delete-after-ingestion instruction; removes the second-current.md risk

### 7.6 Run bootstrap gate against current state (verify the §1 unverified claims)

- **Class**: verification, no source change
- **Action**: run `bash scripts/ci/check-deterministic.sh` and `bash scripts/ci/check-bootstrap.sh`
- **Why**: confirm the gates still pass under current code before any §7.1–§7.5 edit. This is the moment to catch any latent drift caught by the existing tooling but not surfaced because gates haven't been re-run.
- **State-mutating**: yes — writes `.planning/measurement/...`. Therefore not part of the read-only orientation pass; requires explicit approval.

### 7.7 Medium-term sweep proposals (placeholder — propose once short-term lands)

§6.2 items will be proposed individually after the short-term slice closes. Listed there for completeness, not for current approval.

---

## 8. Disposition for this artifact

This file is a snapshot. After §7.1, §7.2, §7.4, §7.5 land:

1. The durable disposition lives in `evidence/implementation-disposition.md` (§7.1)
2. The durable posture lives in AGENTS.md / CLAUDE.md / `posture-triggers.md` (§7.4)
3. The durable horizon lives in any new long-form roadmap or in updates to `.planning/STATUS.md` / `CURRENT-STATE.md`
4. This orientation file is **archived** to `.planning/readiness/archive/release-readiness-orientation-2026-05-08.md` (or kept in place if the readiness directory pattern supports dated snapshots — TBD by §7.4 conventions).

It does not become a re-entry doc. It does not become governance. It does not persist as a competing authority. Its job is to enable the §7 proposals; once they land, its content is absorbed.

---

## Read trail (cite for §7 proposals)

Files read during this pass (read-only):
- `AGENTS.md`
- `WORKFLOW.md` (header check, content not deeply read)
- `.planning/STATUS.md`
- `.planning/CURRENT-STATE.md`
- `docs/handoff/current.md`
- `docs/handoff/DELETE-AFTER-INGESTION-2026-04-24-release-readiness-and-plan-004.md`
- `.planning/implementation-plans/20260424T082720Z/concrete-plans/004-generator-owner-and-command-contract/PLAN.md`
- `tooling/portable-gsd/overlay/get-shit-done/bin/generate-instruction.cjs`
- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md` (lines 1–50, plus targeted greps)
- `scripts/ci/check-deterministic.sh`
- `scripts/ci/check-bootstrap.sh`

Upstream reference reads (read-only via `git show origin/main:<path>` / `git ls-tree origin/main`):
- `CHANGELOG.md` lines 1–340 (covers Unreleased, 1.41.0, 1.39.1)
- `CHANGELOG.md` lines 340–470 (covers 1.38.5, 1.38.4, 1.38.2, 1.37.1, 1.37.0)
- `get-shit-done/workflows/new-project.md` (targeted grep)
- `commands/gsd/{do,from-gsd2,plant-seed,progress,explore,discuss-phase,plan-phase,update,review,resume-work,rigorous-research,health}.md` (existence checks)
- tag inspection: `git tag --contains c5b14455`
- ref refresh: `git fetch --all --tags --prune`

Commits referenced:
- `4a32421` `fix(instructions): preserve runtime instruction targets` (modifier — Plan 004 implementation tail)
- `135ea14` `fix(workflow): clarify approval process for architectural changes` (modifier — landed governance edit)
- `c5b14455` upstream — `feat(sdk): golden parity harness and query handler CJS alignment (#2302 Track A) (#2341)`
- `1e6737cd..96806003` upstream `origin/main` advance during gap

Upstream PR numbers cited from CHANGELOG: #2302/#2341, #2406, #2441, #2453, #2500, #2606, #2612, #2617, #2637, #2641, #2673, #2697, #2714, #2727, #2729, #2733, #2735, #2742, #2757/#2734, #2760, #2762, #2767, #2768/#2783, #2769, #2770, #2772, #2774, #2775/#2777, #2787, #2788, #2789, #2790, #2791, #2792, #2796, #2798, #2801, #2803, #2805, #2808, #2809, #2824, #2828, #2829, #2831, #2832, #2833, #2835, #2836, #2838, #2839, #2851, #2855, #2866, #2868, #2872, #2876, #2897, #2900, #2917, #2943, #2948, #2949, #2950, #2954, #2955, #2962, #2969, #2980, #2983, #2986, #2987, #2998, #3162, #3164, #3166, #3170, #3181, #3215, #3227, #3231, #3236, #3238, #3242, #3245, #3252, #3254, #3257, #3260, #3261.
