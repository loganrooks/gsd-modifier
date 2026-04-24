Date: 2026-04-21
Status: completed Opus 4.7 Max widening output (r1)
Reviewer: `opus[1m]` `max` via Claude Code CLI

# Harness Maximal Improvement Field Map (Opus 4.7 Max r1)

## Role Of This Map

- [g:r:i] This output is a bounded full-field widening. It is not a scorecard, a maturity tier, a top-few ranking, or a pass/fail review. It does not decide whether the harness is adequate. It maps where the current harness already carries force, where current carry thins or fragments, which improvement families are still undernamed, and which bounded future interventions become visible once the field is read as one terrain.
- [d:r:i] The spec and packet explicitly require distinguishing:
  - governance/docs improvements
  - workflow/skill/reference improvements
  - helper/tooling/test improvements
  - compatibility/update improvements
  - lifecycle carry improvements
  - self-improvement and ideal-oriented iteration surfaces
- [d:r:i] This map keeps those kept separate, then adds two further layers the packet asked for: cross-family clusters and tensions, and bounded future intervention families surfaced only once the full field is read at once.

## Method

- [d:r:i] Read the packeted baselines before naming families. Do not treat the currently active families as the whole field. Do not compress full-field mapping into early ranking.
- [d:r:i] For each family: name what it currently carries, what it does not yet carry, and which neighbor families it is already entangled with.
- [d:r:i] For each currently absent or undernamed family: explain why it becomes visible only against the backdrop of the active families, not as a private gap claim.
- [d:r:i] For clusters and tensions: name the carrier edges that tie multiple families together, and the live tensions that will otherwise resolve silently through whichever family edits next.
- [d:r:i] For future intervention families: stay bounded to what the current terrain actually exposes. Do not import relaunch planning, product-scope debates, or domain ideology.

## Part 1 — Current Strengthening Families And Where They Already Carry Force

The harness currently carries several active strengthening families. Each has already intensified specific surfaces rather than living only as proposal prose.

### 1.1 Governance Progressive Disclosure

- [e:c+i] The governance set separates roles explicitly: `INDEX.md` is the controlled entry path, `ARTIFACT-INVENTORY.md` is denser discovery, `CURRENT-STATE.md` is the short governing synthesis, `CURRENT-STATE-TRACE.md` is the longer cumulative trace, `STATUS.md` is the mutable queue, and `../../governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md` routes update discipline. Sources: [GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md](../../governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md:15), [CURRENT-STATE.md](../../CURRENT-STATE.md:7), [ARTIFACT-INVENTORY.md](../../ARTIFACT-INVENTORY.md:7).
- [e:c+i] `../../plain-language/PLAIN-LANGUAGE-STATE.md` and `../../plain-language/PLAIN-LANGUAGE-GLOSSARY.md` sit at the front of the reading path for a lost reader. Source: [CURRENT-STATE.md](../../CURRENT-STATE.md:26).
- [d:r:i] Where this family currently carries force: reread paths can be chosen by task rather than by accident; role disputes have a named home; the short governing synthesis does not silently become a warehouse because the protocol routes expansion into the trace or STATUS instead.
- [d:r:i] The disclosure discipline also now reaches the repo-local root through `.planning/AGENTS.md:42-80`, which carries the progressive-disclosure rule back into repo doctrine rather than leaving it only as an audit-local convention.

### 1.2 Docs / Harness Intervention Carry

- [e:c+i] The intervention-onboarding layer includes `../../harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md`, `../../harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md`, `../../governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md`, `../../indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md`, and `../../indexes/SURFACE-STATUS-AND-DELTA.md`. Sources: [HARNESS-INTERVENTION-ONBOARDING.md](../../harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:1), [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](../../indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:1), [SURFACE-STATUS-AND-DELTA.md](../../indexes/SURFACE-STATUS-AND-DELTA.md:1).
- [e:c+i] The goal-to-surface index routes common intervention goals to the actual carrier surface rather than letting wrapper prose absorb intervention work. Source: [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](../../indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:18).
- [e:c+i] `../../indexes/SURFACE-STATUS-AND-DELTA.md` keeps four truth states visibly distinct: frozen PR-doc snapshot, current upstream line, tracked overlay canon, and live repo-local effective runtime. Source: [SURFACE-STATUS-AND-DELTA.md](../../indexes/SURFACE-STATUS-AND-DELTA.md:9).
- [d:r:i] Where this family carries force: intervention planning starts from the declared-vs-effective authority split rather than from wrapper-level docs, so common mis-starts are avoided.

### 1.3 Entry-Surface And Project-Uplift

- [e:c+i] The entry-surface terrain is now mapped across creation, milestone opening, docs bootstrap/merge, re-entry, repair, update, migration, workspace/worktree entry, phase-injection entry, installer rerun, governing-posture install, four-way uplift split, mid-phase uplift, forensics entry, archived-milestone re-entry, and audit-subtree aging. Source: [intervention-proposals/37-entry-surface-and-project-uplift-map.md](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md:13).
- [e:c+i] The uplift helper has landed in executable form: `tooling/codex/project_uplift.py` carries multi-axis posture (`project_class` + `secondary_signals`), phase-boundary signal from active `CONTEXT.md`, per-carrier `fingerprint_shape`, normalized TOML hashes for runtime-registry carriers, marker-local hashes for strengthening carriers, typed doctrine-sensitive proposal states (`absent` / `drifted`), and an observed-basis compatibility block. Sources: [intervention-proposals/42-project-uplift-signal-layer-harden-slice.md](../../intervention-proposals/42-project-uplift-signal-layer-harden-slice.md:13), [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:1).
- [e:c+i] The uplift compatibility anchor now steers the live routed consumer chain: `progress-note` compares stored versus observed runtime basis and routes movement toward `$gsd-uplift-project --write`. Source: [intervention-proposals/44-project-uplift-compatibility-consumer-follow-through.md](../../intervention-proposals/44-project-uplift-compatibility-consumer-follow-through.md:12).
- [e:c+i] Durable uplift outputs exist as first-class state carriers: `.planning/UPLIFT-REPORT.md`, `.planning/UPLIFT-MANIFEST.json`, and the `Project Uplift` section of `.planning/STATE.md`. Source: [ARTIFACT-INVENTORY.md](../../ARTIFACT-INVENTORY.md:86).
- [d:r:i] Where this family carries force: uplift is now both a worked producer/consumer example and a concrete helper that ran on this repo itself, with one real drift case already caught and repaired.

### 1.4 Propagation / Typed Registry

- [e:c+i] The propagation family has an explicit subtree with 18 prose artifacts plus a layered `v2` registry across `artifacts/02-06`, three external reread lanes, and a change-triggered slice refresh discipline. Sources: [propagation-audit/README.md](../../propagation-audit/README.md:1), [propagation-audit/14-propagation-registry-generation-and-seeding-policy.md](../../propagation-audit/14-propagation-registry-generation-and-seeding-policy.md:1).
- [e:c+i] The overlay contract is explicit and verified: `OVERLAY-MANIFEST.json` carries add-vs-overwrite typing, `portable_gsd_contract.py` validates the contract and rejects drift with named failure modes (`backup_overlay_not_overwrite`, `overwrite_missing_backup`, `add_path_in_backup`). Sources: [tooling/codex/portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:70), [propagation-audit/07-overlay-add-vs-overwrite-contract-and-post-materialization-gate.md](../../propagation-audit/07-overlay-add-vs-overwrite-contract-and-post-materialization-gate.md:1).
- [e:c+i] The registry layers (`L0` roster, `L1` declared contracts, `L2` AI-authored semantic map, `L3` generated evidence, `L4` operator control) are named and split across separate JSON artifacts rather than blended. Source: [propagation-audit/14-propagation-registry-generation-and-seeding-policy.md](../../propagation-audit/14-propagation-registry-generation-and-seeding-policy.md:17).
- [e:c+i] Three change-triggered slice refreshes have run against real contract movement: compatibility-anchor (`16`), compatibility-consumer (`17`), and threshold-scanner helper/lane carry (`18`). Source: [propagation-audit/README.md](../../propagation-audit/README.md:85).
- [d:r:i] Where this family carries force: the propagation registry is already surviving repeated real contract moves without collapsing into either whole-registry rebuilds or hand-memory.

### 1.5 Helper / Tooling Cohort

- [e:c+i] The helper cohort now includes `audit_refmap.py`, `verify_touched_audit_refs.py`, `run_claude_probe.py`, `extract_stream_text.py`, `capture_launch_truth.py`, `runtime_visibility.py`, `capture_runtime_visibility_snapshot.py`, `manifest_install_coherence.py`, `scan_threshold_language.py`, `project_uplift.py`, and `portable_gsd_contract.py`. Source: [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:53).
- [e:c+i] Several helpers have unit coverage: `test_capture_runtime_visibility_snapshot.py`, `test_manifest_install_coherence.py`, `test_portable_gsd_contract.py`, `test_project_uplift.py`, `test_runtime_visibility.py`, `test_scan_threshold_language.py`. Source: [tooling/codex/tests](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests).
- [e:c+i] The helpers are named directly in root and planning doctrine rather than hidden behind prose. Sources: [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:54), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:85).
- [d:r:i] Where this family carries force: doctrine-carrying tools now exist in code with tests and are named in instruction surfaces, which raises the floor on how quickly an operator can probe runtime/overlay/coherence/propagation state.

### 1.6 Launch-Truth / Orchestration Capture

- [e:c+i] `capture_launch_truth.py` reads `~/.codex/state_5.sqlite`, preserves requested-vs-effective launch rows, and is routed through per-lane `launch-truth/` subtrees plus `../../root-support/LAUNCH-LEDGER.md`. Sources: [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:65), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:167).
- [d:r:i] Where this family carries force: cross-vendor audit lanes inherit a durable launch-truth row rather than relying on chat memory; the current workspace has lane-scoped launch-truth captures as a standing discipline.

### 1.7 Long-Horizon And Threshold Carry

- [e:c+i] `29-long-horizon-carry-gap-register.md` now holds the full field of lifecycle, cross-horizon, positive-self-overcoming, and best-possible-harness pressure. Source: [intervention-proposals/29-long-horizon-carry-gap-register.md](../../intervention-proposals/29-long-horizon-carry-gap-register.md:1).
- [e:c+i] The threshold family has completed five dispositions including a historical scanner-influenced reread, narrowed a still-live false-control edge in `scan_threshold_language.py`, and added direct unit coverage. Source: [threshold-audit/dispositions/05-historical-scanner-influenced-reread-inheritance.md](../../threshold-audit/dispositions/05-historical-scanner-influenced-reread-inheritance.md:1).
- [e:c+i] Anti-threshold doctrine is now repeated across root/planning `AGENTS.md` and both `CLAUDE.md` wrappers, covers classic threshold phrasing, pseudo-positive deficit phrasing, and static-positive `enough` phrasing. Source: [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:70).
- [d:r:i] Where this family carries force: the language-level discipline now has both doctrine carriers and a demoted heuristic aid, which stops the scanner from silently governing wording.

### 1.8 Self-Overcoming / Strengthening Opportunity

- [e:c+i] The strengthening family now reaches live planning surfaces: `discuss-phase` carries a new strengthening bucket, `plan-phase` plus planner/checker carry `strengthening_routes`, `plant-seed` preserves out-of-phase strengthening moves, `gsd-rigorous-research` has explicit strengthening handoff carry, and a reference surface exists at `35`. Sources: [STATUS.md](../../STATUS.md:147), [intervention-proposals/32-strengthening-opportunity-first-slice-implementation.md](../../intervention-proposals/32-strengthening-opportunity-first-slice-implementation.md:1), [intervention-proposals/33-research-and-planner-strengthening-carry-follow-through.md](../../intervention-proposals/33-research-and-planner-strengthening-carry-follow-through.md:1).
- [d:r:i] Where this family carries force: strengthening language has both a benchmark packet (`34`) and a compact reference (`35`), so it can be inherited by later lanes without reconstructing the family from memory.

### 1.9 Runtime-Authority / Agent `.toml` Alignment

- [e:c+i] Four `.toml` agents (`gsd-code-reviewer`, `gsd-code-fixer`, `gsd-intel-updater`, `gsd-pattern-mapper`) now carry as paired overlay/live surfaces with AGENTS-governed discovery, captured-state rollback where relevant, and post-carry runtime visibility reports. Source: [STATUS.md](../../STATUS.md:130).
- [e:c+i] The three-surface model-policy invariant (`10`) ties doctrine, installer-applied reasoning defaults, and live agent registry truth together. Source: [propagation-audit/10-model-policy-three-surface-invariant.md](../../propagation-audit/10-model-policy-three-surface-invariant.md:1).
- [d:r:i] Where this family carries force: spawned-worker behavior now has a declared-vs-effective invariant rather than living as ambient model-pick memory.

### 1.10 Rerun Floor And Honesty Rules

- [e:c+i] `25` through `28` now carry the recomputed rerun floor, brake-exit rule, preserve-only activation-trigger doctrine, and execution-capacity reopen rule as bounded proposal artifacts rather than ambient lane-06 chat memory. Source: [STATUS.md](../../STATUS.md:137).
- [d:r:i] Where this family carries force: rerun-pressure questions now have a named honesty layer, which keeps pre-rerun floor items separable from ordinary phase execution.

## Part 2 — Where Current Carry Still Thins Or Fragments

The active families above already intensify specific surfaces. Even so, several carry modes still thin, fragment, or remain weakly consumed.

### 2.1 Lifecycle-Carry Thinning Beyond Discuss/Plan

- [e:c+i] `verify-phase` verifies goal/truth/artifact/wiring/behavior but does not load `future_awareness`, `future_preservation`, `Protected Seams`, or `Explicit Non-Decisions` as verification inputs. Source: [intervention-proposals/29-long-horizon-carry-gap-register.md](../../intervention-proposals/29-long-horizon-carry-gap-register.md:37).
- [e:c+i] `transition` does not load `LONG-ARC.md` or seam registers at phase close; `new-milestone` and `complete-milestone` also omit `LONG-ARC.md` from required reading. Source: [intervention-proposals/29-long-horizon-carry-gap-register.md](../../intervention-proposals/29-long-horizon-carry-gap-register.md:42).
- [e:c+i] `templates/spec.md` locks goal/boundaries/constraints/acceptance but has no future-aware section, so early WHAT is narrower than later CONTEXT. Source: [intervention-proposals/29-long-horizon-carry-gap-register.md](../../intervention-proposals/29-long-horizon-carry-gap-register.md:54).
- [d:r:i] Consequence: long-horizon carry enters strongly at discuss/plan, thins through verification/transition/milestone, and re-surfaces only because a later audit catches what earlier lifecycle surfaces dropped. Even the live strengthening routes (1.8) stop at planning entry and do not yet cross into post-execution carry.

### 2.2 Seed System Shape

- [e:c+i] `plant-seed` now preserves out-of-phase strengthening moves, but the seed format itself is still idea-shaped: there is no seam-shaped, activation-trigger-shaped, or preserve-only-seam-shaped seed typing. Sources: [intervention-proposals/29-long-horizon-carry-gap-register.md](../../intervention-proposals/29-long-horizon-carry-gap-register.md:33), [.codex/get-shit-done/workflows/plant-seed.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plant-seed.md:1).
- [d:r:i] Consequence: long-horizon pressure that is not really an idea (e.g. a seam to protect, an activation trigger to watch) still has to borrow the idea slot, so it can be under-prioritized during seed scan.

### 2.3 STATE / Progress Horizon Bias

- [e:c+i] `progress` carries routing, verification debt detection, and uplift-compatibility awareness, but does not carry an explicit long-horizon watchlist, preserve-only seam register, or activation-trigger summary. Source: [intervention-proposals/29-long-horizon-carry-gap-register.md](../../intervention-proposals/29-long-horizon-carry-gap-register.md:58).
- [d:r:i] Consequence: first-read surfaces carry short-horizon state strongly and long-horizon state thinly, so operator attention defaults toward the current phase even when later-family pressure is live.

### 2.4 Entry-Surface Ownership Gaps

- [e:c+i] `37` names multiple scenarios where no primary workflow owner exists yet: mid-phase uplift, required-reading posture install on an existing project, claim-type/long-horizon/anti-threshold install on an existing project, lightly aged uplift, aged-bespoke uplift, cross-runtime uplift, upstream-template-drift uplift, audit-subtree aging, and governing-posture install. Source: [intervention-proposals/37-entry-surface-and-project-uplift-map.md](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md:49).
- [d:r:i] Consequence: the uplift helper has landed, but the composition-layer workflow (`gsd-uplift-project`) is still in proposal form for these scenario classes, so the helper output has to be operator-interpreted for several posture types. This is a live fragmentation, not a historical gap.

### 2.5 Propagation-Registry Consumption Is Still Manual

- [e:c+i] The typed `v2` registry exists, and change-triggered slice refreshes are already running (compatibility anchor, compatibility consumer, threshold scanner). But there is no diff/verifier tooling that compares successive registry slices, detects stale entries, or warns when a contract-changing commit lands without an accompanying registry refresh. Source: [propagation-audit/README.md](../../propagation-audit/README.md:85).
- [d:r:i] Consequence: the registry is a durable artifact but its freshness still depends on operator discipline. The `L4` operator-control layer records refresh kinds, but no tool treats missing refreshes as a signal.

### 2.6 Upstream-Pristine Frontier Is Doctrine-Only

- [e:c+i] `11` names the upstream-pristine frontier propagation obligation but explicitly does not yet automate pristine-diff detection. Source: [propagation-audit/11-upstream-pristine-frontier-propagation-obligation.md](../../propagation-audit/11-upstream-pristine-frontier-propagation-obligation.md:32).
- [d:r:i] Consequence: upstream shifts depend on manual probe runs. A pristine change that collides with tracked overlay entries would be caught by `portable_gsd_contract.py`, but a pristine change that silently extends shipped behavior without collision would not surface as a propagation signal.

### 2.7 Test Coverage Thins At The Chain Level

- [e:c+i] Per-helper unit tests exist for six helpers, but there is no end-to-end integration test that exercises install → materialization → `runtime_visibility` → `manifest_install_coherence` → `project_uplift` → durable output as one pipeline. Source: [tooling/codex/tests](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests).
- [e:c+i] `test_scan_threshold_language.py` is 726 bytes, narrower than the other test files. Source: [tooling/codex/tests/test_scan_threshold_language.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_scan_threshold_language.py).
- [d:r:i] Consequence: per-helper regressions would be caught; cross-helper integration regressions (e.g. an install-stage change that invalidates a later `project_uplift.py` assumption) would surface only through ad hoc operator reruns.

### 2.8 Launch-Truth Is Capture-Only

- [e:c+i] `capture_launch_truth.py` preserves requested-vs-effective rows, and the repo-local `../../root-support/LAUNCH-LEDGER.md` now tracks lane launches. But there is no durable cross-lane analysis surface that compares reviewer variance, model-pick drift, sandbox posture, or reasoning-level drift across lanes. Source: [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:167).
- [d:r:i] Consequence: launch-truth is strong as a per-lane discipline and weaker as a durable cross-lane pattern library.

### 2.9 Compact-Prompt Carry

- [e:c+i] `09` names `compact-prompt carry` as a propagation row, but it is not yet routed through a change-triggered refresh or mapped into a helper/contract. Source: [propagation-audit/09-sharpened-propagation-field-split.md](../../propagation-audit/09-sharpened-propagation-field-split.md:44).
- [d:r:i] Consequence: compact-prompt overrides are a durable runtime carrier and still carry only through ambient installer wiring rather than through a named propagation slice.

### 2.10 STATE Multi-Ownership

- [e:c+i] `.planning/STATE.md` now carries a Project Uplift section in addition to session continuity, phase state, and progress/resume carry. State-continuity surface is a named propagation row in `09`. Source: [propagation-audit/09-sharpened-propagation-field-split.md](../../propagation-audit/09-sharpened-propagation-field-split.md:43).
- [d:r:i] Consequence: STATE has several writers (uplift helper, progress/resume workflows, transition/new-milestone closures) and no single contract for how those sections relate. The multi-writer surface is durable and useful, and it is also the most likely place for silent content loss if two workflows rewrite the same section with different assumptions.

### 2.11 Audit-Subtree Aging

- [e:c+i] `37` explicitly names `audit-subtree aging and companion-carrier refresh` as a scenario without a primary owner. Source: [intervention-proposals/37-entry-surface-and-project-uplift-map.md](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md:82).
- [d:r:i] Consequence: a subtree like this one (`harness-improvement-audit/`) has no standing protocol for deciding when its intervention proposals should graduate to canon, be retired as tombstones, be archived, or be refreshed against newer doctrine. `gsd-cleanup` covers phase archival; audit subtrees have less owned lifecycle.

### 2.12 Operator Navigation Across Multiple Live Families

- [e:c+i] `progress` routes the operator through current project state; `../../indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md` routes common intervention goals. But no single surface carries "here are the currently active intervention families in flight, their active baselines, and their next adjacent decision surfaces" for the reader opening the workspace cold. Sources: [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](../../indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:1), [CURRENT-STATE.md](../../CURRENT-STATE.md:24).
- [d:r:i] Consequence: `CURRENT-STATE.md` is doing part of this work, but it is single-workspace-scoped and assumes the reader already knows which intervention families exist as candidate top-level objects. This is why the bounded reread set (`INDEX` → `CURRENT-STATE` → family-specific artifacts) still requires operator interpretation to choose which family to enter.

## Part 3 — Omitted Or Undernamed Improvement Families

These families do not yet live as durable surfaces in the workspace, and several only become visible once the active families are read as one terrain.

### 3.1 Failure-Mode Taxonomy / Canonical Drift Fingerprints

- [d:r:i] The workspace has already surfaced several distinct drift classes one at a time: scanner-as-gate residue, scanner-demotion, silent installer-reasoning regression (fixed during the reviewer tranche), overlay-ownership drift on `skills/gsd-resume-work/SKILL.md` (caught by `portable_gsd_contract.py`), stale manifest hashes, compatibility-anchor carry gap, progress-consumer stale-manifest read, and post-write transient drift in uplift memory.
- [d:r:i] What is currently absent: a named catalog of these canonical drift fingerprints with expected detection surface. The overlay contract has named rejection codes; the propagation registry does not yet carry a sibling catalog of what a drift looks like when it arrives.
- [d:r:i] Why this becomes visible now: once the propagation registry is layered and the helper cohort produces structured reports, the absent object is a shared vocabulary of drift signatures across those carriers. That vocabulary would let later reviewers classify a finding by type instead of reinventing it.

### 3.2 Harness Regression / Canary Surface

- [d:r:i] The installer-reasoning default regression was caught because a reviewer happened to look at `.codex/config.toml` during the tranche. Other silent regressions (e.g. a future tracked overlay update that inadvertently reintroduces `high` where `xhigh` is required) would currently depend on the next `project_uplift.py` run or the next reviewer lane.
- [d:r:i] What is currently absent: a standing canary that asserts invariant runtime-registry rows (top-level `model_reasoning_effort`, agent-level reasoning, required tracked overlay entries, compatibility-anchor roster) and fails loudly when those change silently. `manifest_install_coherence.py --strict` comes closest but is selected-lane only.
- [d:r:i] Why this becomes visible now: the three-surface model-policy invariant (`10`) is a durable invariant; the absence of a live canary is therefore the undernamed carry, not the invariant itself.

### 3.3 Audit-Lane Pattern Library

- [d:r:i] Every challenge lane carries the same shape: packet, spec, prompt, launch-truth, output, disposition, inheritance note. The audit-improvement family has eight subtrees so far (`docs-audit`, `tranche-audit`, `long-horizon-audit`, `threshold-audit`, `self-overcoming-audit`, `entry-uplift-audit`, `propagation-audit`, and now `harness-improvement-audit`).
- [d:r:i] What is currently absent: a named pattern library or shared template set that carries recurring packet/spec/prompt conventions, anti-misread rules, launch-truth capture protocol, and inheritance-note shape as reusable primitives.
- [d:r:i] Why this becomes visible now: each audit lane builds the same scaffold by copy-reread from a prior lane. That pattern works; it also silently re-spends authoring budget on scaffolding that could be inherited directly.

### 3.4 Harness Self-Improvement Standing Register

- [e:c+i] `29` names the weak ideal-oriented iteration surface: there is no dedicated recurring artifact asking what bounded moves would make the harness a materially stronger version of itself. Source: [intervention-proposals/29-long-horizon-carry-gap-register.md](../../intervention-proposals/29-long-horizon-carry-gap-register.md:149).
- [d:r:i] What is currently absent: a repo-local surface that maintains a compact roster of known harness weaknesses, tensions, strength opportunities, and live intervention slices as one durable object. The current workspace is doing this work, but only as a time-bounded audit subtree.
- [d:r:i] Why this becomes visible now: this subtree will eventually archive. Without a graduation path, the improvement register dies with it.

### 3.5 Cross-Dimensional Quality Basket

- [e:c+i] `29` also names the absent cross-dimensional evaluation basket (maintainability, runtime-authority clarity, update resilience, long-horizon carry, operator legibility, auditability, cross-vendor reproducibility, intervention yield). Source: [intervention-proposals/29-long-horizon-carry-gap-register.md](../../intervention-proposals/29-long-horizon-carry-gap-register.md:137).
- [d:r:i] What is currently absent: no active carrier uses these dimensions as a shared evaluative lens across multiple intervention proposals. Individual proposals reach one or two dimensions each.
- [d:r:i] Why this becomes visible now: several proposals that thin one dimension (e.g. rising governance-doc density) carry gains on others (operator routing, progressive disclosure). Without a shared lens, those tradeoffs stay implicit.

### 3.6 Rollback / Rollforward Discipline For Landed Slices

- [d:r:i] The harness has `gsd-undo` for phase and plan commits, and the audit trail carries bounded checkpoint commits. But there is no explicit rollback plan for a landed propagation-audit slice, a landed uplift consumer follow-through, or a landed instruction-layer hardening note.
- [d:r:i] What is currently absent: a protocol for "if this landed slice later proves wrong, here is how the propagation registry, the overlay manifest, the durable outputs, and the governance docs back out together."
- [d:r:i] Why this becomes visible now: the change-triggered slice refresh discipline is landing real contract movements. Each landing increases the number of places a future correction would have to touch, and none of those touches are currently sequenced.

### 3.7 Capability-Gap / "Harness Should Have X" Register

- [d:r:i] The workspace currently surfaces tooling needs through proposal artifacts (`11`'s upstream-pristine-diff helper, `08`'s cross-carrier coherence tooling, `29`'s cross-dimensional basket, the implicit registry-diff helper from Section 2.5). Each lives in the proposal that noticed it.
- [d:r:i] What is currently absent: a standing register of "the harness should have X, we keep working around its absence" across active families.
- [d:r:i] Why this becomes visible now: several proposals have independently observed capability gaps. Naming them together would make their cumulative weight legible, and would also expose where one helper would close several proposal-specific workarounds at once.

### 3.8 Canon Absorption Protocol For Landed Intervention Families

- [d:r:i] The strengthening family has reached live workflow surfaces (discuss, plan, research, plant-seed). The entry-uplift family has reached a live helper. The propagation family has reached multiple artifacts, a layered registry, and a verified overlay contract.
- [d:r:i] What is currently absent: a protocol for when canon (root/planning `AGENTS.md`, `CLAIM-TYPES.md`, `LONG-ARC.md`, reference files) should re-absorb a landed intervention family rather than leave it living only in the audit subtree. `.planning/AGENTS.md` does absorb propagation doctrine in `Contract-Propagation Hygiene`; this is one precedent but not a generalized canon-absorption rule.
- [d:r:i] Why this becomes visible now: as intervention proposals land, some of their doctrine properly belongs in durable canon surfaces rather than in the audit trail. Without a protocol, canon uplift depends on whether someone happens to move the wording.

### 3.9 Machine-Checkable Governance Gates

- [d:r:i] The workspace has prose governance rules (root `AGENTS.md`, `.planning/AGENTS.md`, the progressive-disclosure protocol, the propagation hygiene rule) and mechanical tools (`audit_refmap.py verify`, `git diff --check`, `portable_gsd_contract.py verify`, `manifest_install_coherence.py --strict`). These are largely separate.
- [d:r:i] What is currently absent: a checkpoint-level gate that asserts "this commit touches a contract-carrying surface; did you name its direct producers/consumers/mirrors in a proposal, disposition, or audit note?" — in the spirit of the contract-propagation hygiene rule but mechanically enforced.
- [d:r:i] Why this becomes visible now: propagation obligations are written as doctrine, and the helper layer can reason about which surfaces are contract-carrying. The missing link is a pre-checkpoint hook that converts doctrine into a soft gate.

### 3.10 Cross-Repo Uplift Carry

- [d:r:i] All current uplift/propagation/governance work assumes one repo. `project_uplift.py` runs on this repo and records its posture.
- [d:r:i] What is currently absent: a path for carrying posture to a second project, either by deriving a portable uplift packet from this repo's durable uplift outputs or by defining a cross-repo doctrine export.
- [d:r:i] Why this becomes visible now: the helper cohort plus tracked overlay is reaching the point where its gains could travel. Without a cross-repo path, they stay single-repo gains.

### 3.11 Time / Decay / Vintage Semantics

- [d:r:i] Audit artifacts carry `Date:` stamps; the propagation registry carries refresh kinds; `UPLIFT-MANIFEST.json` carries a compatibility basis. None of these surfaces carries a live decay signal (e.g. "this registry refresh was last taken 30 days ago and has seen 12 intervening contract changes").
- [d:r:i] What is currently absent: a compact vintage layer that exposes staleness as a signal to the operator or to routed consumers.
- [d:r:i] Why this becomes visible now: the compatibility-anchor mechanism already treats "observed basis moved" as a signal. Generalizing that to "durable artifact age vs. contract movement since last refresh" is a visible next layer.

### 3.12 Observability / Usage Telemetry

- [d:r:i] The harness runs many workflows, skills, and helpers. No durable surface records which ones actually ran over time, which intervention proposals produced a landed slice, which helpers are called by which workflows in practice.
- [d:r:i] What is currently absent: a lightweight usage record that lets a later reader tell whether a proposed workflow is used, whether an intervention proposal actually drove work, or which helpers are load-bearing under live conditions.
- [d:r:i] Why this becomes visible now: the proposal sequence is long (44 bounded proposals, 18 propagation notes, 6 registry artifacts, 8 audit subtrees). Without usage telemetry, it is hard to tell whether any given proposal carries weight at intervention time.

### 3.13 Security / Privacy / Secret Carrier Row

- [d:r:i] `AGENTS.md` addresses non-affiliation with F1 marks, and `tooling/codex/run_claude_probe.py` notes permission boundaries. No propagation row names secrets, credentials, tokens, state-bearing URLs, or privacy surfaces as a distinct carrier.
- [d:r:i] What is currently absent: a secret/privacy row in the propagation family with its own producer/consumer split (e.g., `.env`, launch-truth captures that could include session ids, headless probe outputs).
- [d:r:i] Why this becomes visible now: `capture_launch_truth.py` reads `state_5.sqlite`; launch-truth artifacts persist requested-vs-effective rows. As this pattern widens, the implicit privacy boundary becomes load-bearing and deserves named carry.

### 3.14 Token-Budget / Cost Carrier Row

- [d:r:i] The model-policy three-surface invariant (`10`) names reasoning effort but not cost/budget. Each reasoning-level change affects token cost and response latency; no surface carries those as named tradeoffs.
- [d:r:i] What is currently absent: a thin budget/cost row in the propagation family or a compact cost note in governance doctrine.
- [d:r:i] Why this becomes visible now: the workspace has explicit preferences for `xhigh` on orchestration and `high` elsewhere; that preference carries cost implications across the lane fleet. The tradeoff lives in prose; it does not live as a carrier.

### 3.15 Cross-Vendor Reviewer Inheritance

- [d:r:i] The workspace has launched multiple Opus and GPT reviewer lanes. Inheritance notes record what was accepted; launch-truth captures record the lane's requested-vs-effective settings. Reviewer-specific recurring patterns (Opus tends to widen field, GPT tends to sharpen contract; Opus picks up ideal-form pressure, GPT picks up operational under-reach) surface in dispositions but not as a durable review-pattern record.
- [d:r:i] What is currently absent: a compact cross-vendor review-pattern artifact that records reviewer-specific strengths and biases across lanes, so future packet/spec/prompt design can bias lane selection to the right reviewer.
- [d:r:i] Why this becomes visible now: several comparative dispositions already say something like "Opus adds the broader frame, GPT adds the tighter landing." That observation is recurring rather than incidental.

### 3.16 Structured / Prose Coherence

- [d:r:i] The workspace now has layered JSON (`artifacts/02-06`), prose propagation family, and intervention proposals. Cross-references between JSON and prose are hand-maintained.
- [d:r:i] What is currently absent: a mechanical check that the JSON roster / contracts / semantic map / evidence / coverage stays in sync with the prose family, or vice versa.
- [d:r:i] Why this becomes visible now: the `v2` split is already producing real change-triggered refreshes. As refreshes accumulate, hand-maintained cross-references become the most likely drift point.

### 3.17 Activation-Trigger / Seam-Lifecycle Consumer

- [e:c+i] Activation-trigger doctrine now exists in `27`. `plant-seed` preserves out-of-phase moves. But no workflow actively reads activation triggers, checks seam closure, or surfaces a live "this preserved seam is now pressured" signal. Sources: [intervention-proposals/27-preserve-only-activation-trigger-doctrine.md](../../intervention-proposals/27-preserve-only-activation-trigger-doctrine.md:1), [intervention-proposals/29-long-horizon-carry-gap-register.md](../../intervention-proposals/29-long-horizon-carry-gap-register.md:80).
- [d:r:i] What is currently absent: a lifecycle consumer that treats preserved seams and activation triggers as live inputs to the next adjacent routing decision, not as one-shot planning residue.

### 3.18 Sovereignty / Ownerless-Concern Map

- [d:r:i] `../../governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md` carries authority classes. `37` records scenario ownership. Between them, several concerns still have no stable owner: mid-phase uplift, audit-subtree aging, cross-runtime posture, token-budget carry, secret-handling, cross-vendor pattern inheritance, canon absorption.
- [d:r:i] What is currently absent: a compact map of concerns that have no current owner, so those concerns do not silently leak into whichever workflow happens to touch them next.

## Part 4 — Cross-Family Clusters And Tensions

Mapping the field as one terrain exposes several clusters where pressure crosses family boundaries, and several tensions where two families pull in different directions.

### 4.1 Clusters

- [d:r:i] **Cluster L (Layered Truth).** Install frontier, overlay canon, live runtime, durable outputs, and registry evidence form one cluster where no single surface can stand in for the others and where each already has a classification or coherence tool. Members: `../../indexes/SURFACE-STATUS-AND-DELTA.md`, `portable_gsd_contract.py`, `runtime_visibility.py`, `manifest_install_coherence.py`, `UPLIFT-MANIFEST.json`, `artifacts/02-06`. Pressure: the absent canary (3.2), cross-helper integration test (2.7), and registry-refresh verification (2.5) would sit inside this cluster.
- [d:r:i] **Cluster R (Relevance Routing).** `INDEX`, `CURRENT-STATE`, `ARTIFACT-INVENTORY`, `STATUS`, `PLAIN-LANGUAGE-*`, `GOAL-TO-SURFACE-INTERVENTION-INDEX`, `GOVERNANCE-READING-AND-UPDATE-PROTOCOL` all serve progressive disclosure through different entry points. Pressure: the absent active-family routing (2.12) and capability-gap register (3.7) would extend this cluster.
- [d:r:i] **Cluster F (Fingerprint / Integrity Carriers).** `OVERLAY-MANIFEST.json`, `UPLIFT-MANIFEST.json`, `.codex/gsd-local-patches/backup-meta.json`, `.codex/gsd-file-manifest.json`, launch-truth captures, runtime-visibility snapshots, registry `v2` evidence index. Pressure: harness-wide schema versioning and canonical drift fingerprints (3.1) would live here.
- [d:r:i] **Cluster A (Anti-Threshold Posture).** Doctrine in root/planning `AGENTS.md` and `CLAUDE.md` wrappers, `scan_threshold_language.py` as demoted heuristic intake, threshold-audit dispositions `01-05`, self-overcoming family proposals `30-35`. Pressure: the lifecycle surfaces (2.1) that do not yet consume anti-threshold framing; the missing cross-dimensional basket (3.5).
- [d:r:i] **Cluster U (Uplift / Propagation / Entry-Surface).** `36-44` and `propagation-audit/01-18` sit together as one pressure family. Pressure: the ownerless posture scenarios (2.4), the absent `gsd-uplift-project` workflow consumer, and the cross-repo carry (3.10).
- [d:r:i] **Cluster H (Helper Cohort).** `tooling/codex/*.py` with per-helper tests and cross-carrier consumption relations named in `12`. Pressure: chain-level integration test (2.7), registry-refresh verifier (2.5), and pristine-diff helper (2.6).
- [d:r:i] **Cluster G (Governance Progressive Disclosure).** `GOVERNANCE-READING-AND-UPDATE-PROTOCOL`, `INDEX`, `CURRENT-STATE`, `STATUS`, `ARTIFACT-INVENTORY`, `WORKSPACE-AUTHORITY-AND-ORGANIZATION`, `.planning/AGENTS.md:42-80`. Pressure: canon-absorption protocol (3.8) and audit-subtree aging (2.11).
- [d:r:i] **Cluster X (Cross-Vendor Review Infrastructure).** Packet/spec/prompt discipline, launch-truth capture, inheritance notes, comparative dispositions, `../../root-support/LAUNCH-LEDGER.md`. Pressure: pattern library (3.3), reviewer-inheritance surface (3.15).

### 4.2 Tensions

- [d:r:i] **T1. Bounded scope vs. network-wide propagation.** Each intervention proposal is deliberately bounded. The propagation family keeps widening the network of surfaces that each bounded slice touches. Holding both at once depends on discipline (the "what was held for later" discipline in almost every recent disposition). This tension is currently managed well; it is also the most load-bearing single discipline in the workspace.
- [d:r:i] **T2. AI-authored vs. machine-derived.** Registry `v2` policy is explicit: `L0` rosters can be mechanical, `L1` declared contracts need authored intent, `L2` semantic mapping stays AI-authored, `L3` evidence is generated, `L4` operator control is authored. Many carriers still blur these edges in practice (e.g., `UPLIFT-MANIFEST.json` is both authored schema and observed evidence).
- [d:r:i] **T3. Inline governance vs. progressive disclosure.** Root `AGENTS.md` now carries propagation hygiene, claim-type doctrine, anti-threshold doctrine, delegation/orchestration, quality bar, pushback discipline, and maintenance rules. The progressive-disclosure protocol applies inside the audit subtree; root canon has absorbed a lot of the doctrine that progressive disclosure was designed to defer.
- [d:r:i] **T4. Intervention-first vs. canon-first.** Strengthening started in audit-subtree proposals and landed in canon via `AGENTS.md` doctrine plus live workflow inserts. Uplift landed in `tooling/codex/` helpers plus `.planning/UPLIFT-*` outputs. Propagation landed in `AGENTS.md:49-63` plus registry artifacts. Each family chose its own canon-absorption path; no shared protocol decides when to absorb and when to keep in subtree (this is where 3.8 would sit).
- [d:r:i] **T5. Refresh cadence vs. change-triggered refresh.** The registry policy names three refresh kinds: scheduled whole-registry, change-triggered slice, lane-scoped. The workspace currently runs only change-triggered and lane-scoped refreshes. Scheduled whole-registry refresh is named but not cadenced; without a cadence, stale layers will only surface when the next change-triggered refresh happens to notice them.
- [d:r:i] **T6. Helper as intake vs. helper as adjudicator.** `scan_threshold_language.py` is demoted to intake, with `--ignore-meta-instruction-lines` and clear doctrine that it does not govern wording. Other helpers have not needed this distinction yet. The general shape of the tension — any helper that produces structured output risks becoming a silent adjudicator — is a recurring pattern.
- [d:r:i] **T7. Doctrine density vs. operator legibility.** Every doctrine addition to root/planning `AGENTS.md` or `CLAUDE.md` wrappers raises load on the reader. The wrappers are already dense. Without a standing canon-absorption criterion, doctrine density grows monotonically.
- [d:r:i] **T8. Audit-subtree durability vs. cumulative intervention register.** This audit subtree is bounded. The improvement-register concern (3.4) is durable. The absence of a graduation path creates a live tension between keeping the subtree focused and not losing the register when the subtree archives.

## Part 5 — Bounded Future Intervention Families Surfaced By The Full Map

These are bounded future intervention families that become visible once the active families, thinning edges, and omitted families are read together. They are candidates, not recommendations; packet and spec say the narrowing step comes only after this map is written.

### 5.1 Lifecycle-Carry Family

- [d:r:i] Bounded interventions that close the post-planning horizon gap:
  - verify-phase future-preservation lane (29 §1)
  - transition seam-carry block (29 §2)
  - new-milestone and complete-milestone `LONG-ARC.md` reread (29 §3)
  - SPEC template future-aware section (29 §4)
  - STATE and progress horizon-watch row (29 §5)
  - seed-system seam typing (29 §6)
  - activation-trigger/seam-lifecycle consumer workflow (3.17)
- [d:r:i] This family is mostly named in `29` but has not yet become a worked intervention chain. It would extend the currently strong discuss/plan entry carry through later lifecycle surfaces.

### 5.2 Harness-Quality Canary / Invariant Assertion Family

- [d:r:i] Bounded interventions around silent-regression protection:
  - live invariant assertions for runtime-registry rows (e.g. top-level reasoning, agent-level reasoning, required overlay entries)
  - harness-wide pre-commit or pre-checkpoint gate that checks a minimum runtime-invariant set (3.2, 3.9)
  - scheduled whole-registry refresh with stale-detection (2.5, T5)
  - cross-helper chain-level integration test (2.7)
  - structured/prose coherence check between `artifacts/02-06` and the prose family (3.16)
- [d:r:i] This family would convert current doctrine invariants into mechanical gates, raising the cost of silent regression.

### 5.3 Audit-Program Infrastructure Family

- [d:r:i] Bounded interventions around cross-audit reuse:
  - audit-lane pattern library / shared scaffolding (3.3)
  - audit-subtree aging / graduation / archival protocol (2.11)
  - canon-absorption protocol for landed intervention families (3.8)
  - reviewer-inheritance / cross-vendor pattern surface (3.15)
  - compact drift-fingerprint catalog with expected detection surface (3.1)
- [d:r:i] This family would let the next audit subtree carry more from this one without repeating scaffolding work.

### 5.4 Self-Improvement Standing-Register Family

- [d:r:i] Bounded interventions around the weak ideal-oriented iteration surface (29 §6.3):
  - repo-local standing harness-self-improvement register (3.4, 29 §6.1)
  - cross-dimensional quality basket as a shared evaluative lens (3.5, 29 §6.2)
  - capability-gap register ("harness should have X") (3.7)
  - ownerless-concern sovereignty map (3.18)
- [d:r:i] This family would make the improvement field visible as a durable object rather than one that dies with each audit subtree.

### 5.5 Uplift / Propagation Consumer Family

- [d:r:i] Bounded interventions that complete the current uplift and propagation loops:
  - land `gsd-uplift-project` as a live workflow/skill beyond the helper, with detect-only default and per-carrier install flags (`39` proposal, 2.4)
  - typed owner(s) for mid-phase uplift, aged-bespoke uplift, cross-runtime uplift, upstream-template-drift uplift (2.4)
  - pristine-diff helper for the upstream-pristine frontier obligation (2.6, 3.7)
  - registry-refresh diff helper / freshness signal (2.5)
  - compact-prompt propagation slice (2.9)
- [d:r:i] This family would harden the current uplift and propagation gains into more routable carriers rather than keeping them operator-interpreted.

### 5.6 Durable Memory And Decay Family

- [d:r:i] Bounded interventions around vintage and cross-run memory:
  - vintage / decay signal for audit subtrees, intervention proposals, registry layers (3.11)
  - harness-wide schema versioning across durable outputs (overlay-manifest, uplift-manifest, registry v2) (Cluster F)
  - usage telemetry / observability record for workflows, skills, helpers (3.12)
  - session-continuity carry beyond one operator (extension of STATE multi-ownership, 2.10)
- [d:r:i] This family would give later readers a signal for how much to trust a durable artifact they find.

### 5.7 Safety / Cost / Privacy Carrier Family

- [d:r:i] Bounded interventions around currently implicit carriers:
  - secret / privacy row in the propagation family, with producer/consumer typing (3.13)
  - token-budget / cost row or compact cost note in doctrine (3.14)
  - rollback / rollforward discipline for landed slices (3.6)
- [d:r:i] This family would make currently ambient carriers visible without expanding scope into general product-level safety work.

### 5.8 Cross-Repo / Distribution Family

- [d:r:i] Bounded interventions around carrying posture beyond this repo:
  - cross-repo uplift packet derivation path from durable uplift outputs (3.10)
  - portable doctrine export pattern for root/planning `AGENTS.md` and `CLAUDE.md` wrappers
  - bounded "apply this harness posture to another project" skill or workflow
- [d:r:i] This family is later-stage work by nature and should not be opened ahead of 5.5, but naming it here prevents it from disappearing into "maybe someday."

## Part 6 — Anti-Misread Layer

- [g:r:i] This map does not claim that the harness lacks long-horizon carry, propagation carry, uplift carry, governance discipline, or helper tooling. The harness carries all of those actively.
- [g:r:i] This map does not rank the families above, does not collapse them into one score, and does not identify a top-three.
- [g:r:i] This map does not import relaunch-planning pressure, product-scope debates, or Phase 01 execution pressure. The rerun stays paused.
- [g:r:i] This map does not promote any proposed future intervention to an approved next slice. The spec is a widening lane; narrowing is later work.
- [g:r:i] This map does not treat the scanner as authority, does not treat the propagation registry as exhaustive, does not treat uplift memory as final compatibility truth, and does not treat durable outputs as runtime truth. Each of those distinctions is preserved throughout.
- [g:r:i] This map does not use threshold framing (`adequate`, `sufficient`, `good enough`, `ready`), static-positive framing (`already strong`, `clear enough`), or deficit-pseudo-positive framing (`not lacking`, `no longer missing`) as structural claims. Where it says a family carries force, it names which surface carries what.

## Part 7 — Current Consequence

- [d:r:i] The harness currently intensifies maintainability, robustness, propagation visibility, update resilience, governance legibility, and long-horizon carry across at least ten active families. Those families have produced durable artifacts, executable helpers, verified contracts, challenge-lane inheritance, and governance discipline.
- [d:r:i] The full field still carries visible intensification opportunity across:
  - post-discuss/plan lifecycle surfaces (verify, transition, milestone boundaries, SPEC, STATE, seeds)
  - canary-level invariant assertion
  - cross-audit pattern reuse
  - standing self-improvement register and cross-dimensional quality basket
  - uplift/propagation consumer completion (workflow, pristine-diff, registry-refresh helper, compact-prompt slice)
  - durable-memory decay / vintage / observability
  - safety / cost / privacy carriers
  - cross-repo distribution
- [d:r:i] Several tensions (T1-T8) will resolve silently through whichever family edits next unless a standing register holds them.
- [d:r:i] Several concerns still have no owner (mid-phase uplift, audit-subtree aging, token-budget carry, secret handling, canon absorption, cross-vendor pattern inheritance); naming them here preserves them as ownerless rather than letting them disappear into whichever workflow touches them next.
- [d:r:i] Per the spec, this output does not choose the next narrower sequence. It leaves the field mapped so that a later disposition, narrower packet, or bounded intervention slice can be chosen without discarding paths that only surface once the whole terrain is visible at once.
