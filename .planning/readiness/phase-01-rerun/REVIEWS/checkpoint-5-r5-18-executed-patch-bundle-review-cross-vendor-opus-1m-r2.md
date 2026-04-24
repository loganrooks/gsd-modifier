# Checkpoint 5 R5.18 Executed Patch Bundle Review — Cross-Vendor Opus-1M R2

## Header

- checkpoint: `5`
- artifact(s) under review: executed `R5.18` patch bundle (`R5.18a1`/`a2` boundary decisions, `R5.18b` review/planning surfaces, `R5.18c` completion/routing surfaces, `R5.18d` integration/ledger), as represented by the live on-disk files under `.codex/*` and `tooling/portable-gsd/overlay/*` plus the package-truth docs under `.planning/readiness/phase-01-rerun/*`.
- review mode: `cross-vendor-reread`
- authoring lane: internal Codex (GPT-5.4 high for `R5.18a1/a2/b/c/d`); cross-vendor Claude Opus for prior checkpoint rereads
- reviewer: Anthropic Claude, current CLI, large-context lane
- model / reasoning or vendor: `claude-opus-4-7[1m]` (Opus 4.7, 1M-context variant), extended thinking posture
- baseline commit / artifact snapshot: workspace as of 2026-04-16; last committed readiness commit `32d01c8 docs(signal): cross-vendor-duplicate-dispatch-and-causal-overreach`; `R5.18` bundle remains uncommitted local-runtime state plus uncommitted readiness-package updates (see `git status`)
- independence relationship: `cross-vendor` (Claude reviewing Codex-authored bundle); note that this reviewer is reading the same working tree the authors landed, not a separate snapshot, so independence is vendor-level, not environment-level

## Review Questions

- What closure claim is this review challenging? That the executed `R5.18` bundle is honest Checkpoint 5 follow-through, bounded, review-clean, and free of silent closure of parked or later-lane concerns.
- Which gate exit criteria are being tested? `GATES/checkpoint-5.md:107-112` — specifically that the bundle passes fresh internal and cross-vendor review against the accepted spec, that the `R5.18a1` contradiction ledger governed `R5.18b/c` scope, that `R8.1` through `R8.4` remain explicit later-lane ownership rather than implied closure, that router-pair asymmetry is either paired or explicitly defended, and that the exclusion heuristics did not re-enter as standing doctrine.
- Which quality questions are being tested? The seven spec questions (ledger governance, later-lane explicitness, router asymmetry, authority shelter, exclusion heuristics, package truth, runtime-tracking risk).
- Which regressions are most relevant? Silent widening of `Bucket 1`; quiet promotion of parked router/audit-uat items; authority-shelter masking of downstream semantic obligations; exclusion-heuristic re-entry; divergence between tracked overlay canon and live runtime that invisibly unwinds doctrine next time the portable-GSD installer runs.
- What meaningful quality opportunity is being left unused? Landing the R5.18 doctrine into the *tracked* `tooling/portable-gsd/overlay/*` surfaces so the patch survives `scripts/setup-portable-gsd.sh` reinstallation, and making that traceable in the commit graph rather than only as local-runtime state.

## Findings

Ordered by severity. Severity classifications: `HIGH` blocks honest closure of Checkpoint 5 on the executed-bundle review; `MEDIUM` is a meaningful quality gap that should be answered before closure; `LOW` is a note for the record.

### Finding 1 — `HIGH` — Tracked portable-GSD overlay canon silently diverges from the live R5.18-patched runtime

Severity: `HIGH`. Classification: `revise-current`.

The R5.18b/c patch set edited files under `.codex/*` that are `.gitignore`'d (confirmed: `.gitignore:1` whitelists `.codex/` via a single `.codex/` line; every spot-check path except the two `tooling/portable-gsd/overlay/agents/*.toml` paths returned a match against `.gitignore:1` under `git check-ignore -v`). The repo's documented reinstall path is `scripts/setup-portable-gsd.sh`, which runs `npx get-shit-done-cc --codex --local` to lay down a base `.codex/*` and then overlays every file under `tooling/portable-gsd/overlay/*` onto `.codex/*`, replacing `__PROJECT_ROOT__` with the repo path (`scripts/setup-portable-gsd.sh:10-31`). That makes the tracked overlay directory the canonical source of any repo-local GSD divergence from the npm base.

The executed bundle did *not* propagate R5.18b/c doctrine into the tracked overlay. Concretely:

- `tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md` is tracked and clean (`git status` shows no modification; diff against `.codex/get-shit-done/references/agent-contracts.md` shows the overlay still lacks the R5.18c `## PLAN COMPLETE` routing clarification on line 45 of the live file, the `completion_mode` / `completion_debt` rows for the Executor→Verifier contract at lines 76-77, the entire new Verifier→Routing section at lines 82-90, and the closing NOTE at line 108). A fresh reinstall therefore restores an `agent-contracts.md` that omits the R5.18c contract the live runtime now depends on.
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md` is tracked and clean; diff against the live `.codex/get-shit-done/workflows/plan-phase.md` shows the overlay is missing the required-reading line for `planner-reviews.md` and (by token-search spot check) the R5.18b reviews-mode planner rules, checker rules, and revision-loop rules on live-side lines 706-709, 855-857, and 956. Reinstall therefore erases the R5.18b review-consumer contract from the live plan-phase workflow.
- `tooling/portable-gsd/overlay/agents/gsd-executor.toml` and `.../gsd-verifier.toml` are *untracked* (`git ls-files tooling/portable-gsd/overlay/agents/` returns only `gsd-phase-researcher.toml`, `gsd-plan-checker.toml`, `gsd-planner.toml`; the executor/verifier tomls appear only under `git status --porcelain` as `??`). The R5.18c internal review explicitly promoted this pair as the tracked overlay counterpart of the live runtime (`REVIEWS/checkpoint-5-r5-18c-completion-routing-chain-launch-internal-r1.md:6,11-14`), but no one committed them, so the tracked overlay contains *no* R5.18c executor/verifier at all. A fresh `setup-portable-gsd.sh` run therefore leaves the base npm executor/verifier pair in place — i.e., the pre-R5.18 versions without the `completion_mode` / `debt_carrying_execution` / `completion_debt` contract and without the debt-aware override coupling.
- `tooling/portable-gsd/overlay/get-shit-done/workflows/review.md` and `.../references/planner-reviews.md` are *untracked* new files (`git status` shows both as `??`). The R5.18b "review consumer chain" therefore also has no tracked canon.
- Multiple R5.18b/c patched live surfaces have no overlay counterpart at all and are only repo-ignored live files: `.codex/skills/gsd-review/SKILL.md`, `.codex/skills/gsd-plan-phase/SKILL.md`, `.codex/skills/gsd-do/SKILL.md`, `.codex/get-shit-done/workflows/do.md`, `.codex/get-shit-done/workflows/progress.md`, `.codex/get-shit-done/workflows/transition.md`, `.codex/get-shit-done/references/verification-overrides.md`, `.codex/get-shit-done/bin/lib/phase.cjs`, `.codex/get-shit-done/bin/lib/roadmap.cjs`. None of those paths appear under `tooling/portable-gsd/overlay/` at all (`ls tooling/portable-gsd/overlay/get-shit-done/{workflows,references,bin/lib,skills}/` and `ls tooling/portable-gsd/overlay/skills/` both confirm these live-only files have no overlay twins). That means on any fresh install, the live runtime reverts to whatever the npm base ships — almost certainly pre-R5.18 — for every one of them.

Why this is a `HIGH` closure finding rather than documentary noise:

- The executed bundle's own STATUS claim is that "R5.18c landed … the promoted live `.codex/agents` executor/verifier pair" (`STATUS.md:105`) and that "direct verification now exists alongside the implementation artifacts" via the live repo (`STATUS.md:107-110`). Both claims are true *on this worktree right now* and false for any other materialization — including this same workstation after the next `setup-portable-gsd.sh` run, and any fresh clone or CI environment.
- `R5.18d` makes `package truth is updated to match the implemented frontier` an explicit required check (`AUDITS/checkpoint-5-r5-18d-integration-and-review-prep-launch-spec.md:13`). The implemented frontier is not one surface; it is a live-only surface and a tracked overlay surface that has silently diverged. Calling that "partially git-tracked" (`REVIEWS/checkpoint-5-r5-18d-integration-and-review-prep-launch-internal-r1.md:40`) is soft language for "the reinstallable canon does not match the executed bundle".
- The `R5.19d4` operational-consequences frame treated overlay-vs-live alignment as part of the Track C surface that `R5.18c` must own (`AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:16-29` by reference). Letting the executor/verifier overlay sit untracked is exactly the kind of silent closure-by-authority the `R5.19` frame was commissioned to flag: "the overlay side contract already matches" is true of one worktree, not of the canon.
- The checkpoint charter treats `R5.8` branch/worktree materialization as accepted bounded risk with a sharp reopen trigger (`REVIEWS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md:175-185`). Untracked overlay files at precisely the materialization seam are, by the trigger's own terms ("if later verification exposes a concrete branch/worktree mismatch"), *a concrete branch/worktree-mismatch*: the tracked tree and the live runtime materially disagree about what the executor/verifier/review/planner/completion chain says. The accepted-bounded-risk posture for `R5.8` is therefore no longer honest on the current evidence.

What would close it cleanly:

1. Land R5.18b/c overlay parity: add tracked overlay counterparts under `tooling/portable-gsd/overlay/` for every R5.18-patched live surface, using `__PROJECT_ROOT__` placeholders and matching content, and commit them in one bundle.
2. Commit the currently untracked `tooling/portable-gsd/overlay/agents/gsd-executor.toml`, `.../gsd-verifier.toml`, `.../get-shit-done/references/planner-reviews.md`, and `.../get-shit-done/workflows/review.md`.
3. Update `STATUS.md`, `STATE.yaml`, `GATES/checkpoint-5.md`, and the `R5.18d` integration artifact to state bluntly that the executed bundle is reproducible from the tracked tree rather than "local-runtime state".
4. Explicitly re-disposition `R5.8` since the bounded-risk trigger has fired.

Until this lands, Checkpoint 5 closure on the executed bundle cannot honestly rest on the current artifacts — the review surface and the runtime surface will silently disagree the next time anyone reinstalls.

### Finding 2 — `MEDIUM` — Integration artifact and package truth understate the tracking gap from Finding 1

Severity: `MEDIUM`. Classification: `revise-current`.

The `R5.18d` integration artifact acknowledges that "much of `.codex/*` is repo-ignored or otherwise not available as a conventional tracked diff here" and tells reviewers to "rely on direct file-content inspection and the verification commands below rather than tracked-path expectations alone" (`REVIEWS/checkpoint-5-r5-18d-integration-and-review-prep-launch-internal-r1.md:40`). The `R5.18b` and `R5.18c` internal reviews use equivalent language (`REVIEWS/checkpoint-5-r5-18b-review-planning-chain-launch-internal-r1.md:28`; `REVIEWS/checkpoint-5-r5-18c-completion-routing-chain-launch-internal-r1.md:26`). `STATE.yaml:20` encodes the same framing as `executed_r5_18_patch_bundle_is_local_runtime_state_and_only_partially_git_tracked`.

Two problems with that framing under the readiness quality bar:

- It treats the ignored-vs-tracked split as a reviewer ergonomics problem, when Finding 1 shows it is an actual divergence of canon from runtime. The honest statement is not "review can't use diffs" but "the canon the tracked tree will reinstall from does not match the bundle under review".
- It effectively shelters the executed bundle behind the `.gitignore` instead of making the missed overlay work visible as an executed-bundle obligation. That is exactly the "authority-shelter" failure mode the spec's Q4 tries to test: governing files (here, the decision to gitignore `.codex/*`) being used as a shield against the downstream obligation to carry the patch into tracked canon.

What would close it cleanly: rewrite the "partially git-tracked" language in `R5.18d`, `STATUS.md:107-110`, `STATE.yaml:20`, and `GATES/checkpoint-5.md:138` to name the overlay-vs-live divergence directly, and make it an explicit live contradiction on the active frontier until Finding 1 is addressed.

### Finding 3 — `MEDIUM` — `R5.8` bounded-risk disposition is logically inconsistent with the executed bundle

Severity: `MEDIUM`. Classification: `revise-current` (or `reactivate-earlier` if the owner prefers a formal reopen).

`R5.8` is reaffirmed as `accepted bounded risk` on the explicit condition "reactivate immediately if Checkpoint 5 changes worktree/config behavior or later verification exposes a concrete branch/worktree mismatch" (`REVIEWS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md:183-184`; `TASKS.md:39`). The executed bundle is itself a concrete branch/worktree mismatch because the repo-local installer overlay and the live runtime no longer agree about the R5.18 patched content (Finding 1). The trigger has fired in the same wave it was re-accepted. Leaving `R5.8` as `accepted bounded risk` while a materialization divergence exists on the executed surfaces rereads as self-insulating.

What would close it cleanly: reclassify `R5.8` to reactivated in the same patch that closes Finding 1, or document explicitly why the overlay divergence is *not* the kind of branch/worktree mismatch that fires the trigger.

### Finding 4 — `LOW` — STATUS.md and GATES/checkpoint-5.md list the seven-question review obligation as five rather than the full spec set

Severity: `LOW`. Classification: `revise-current`.

`GATES/checkpoint-5.md:107-110` and the `R5.18d` integration artifact's "Review Surface" list five review questions (`REVIEWS/checkpoint-5-r5-18d-integration-and-review-prep-launch-internal-r1.md:33-38`). The spec for this review requires seven (`REVIEWS/checkpoint-5-r5-18-executed-patch-bundle-review-spec.md:50-57`), adding (Q6) package-truth adequacy and (Q7) the partially-tracked runtime closure risk. The integration artifact folds Q6 implicitly into its own output and Q7 into the "partially git-tracked" caveat; neither survives as an explicit review-test obligation in the gate. For a readiness gate that is about to request closure, collapsing the seven-question frame into five is exactly the kind of quiet scope compression the `R5.19` exclusion work was commissioned to prevent. Minor because the reviewer still has the spec, but it compounds Finding 2 by making it easier for later readers to miss the tracking-risk question.

What would close it cleanly: restore the seven-question frame verbatim in `GATES/checkpoint-5.md` and in `R5.18d`, and treat Q7 as a first-class review test rather than a caveat.

### Finding 5 — `LOW` — `live review/planning markers are present in the .codex/* surfaces` is loose for a verification line

Severity: `LOW`. Classification: `defer-nonblocking`.

`STATUS.md:108-110` describes verification as "live review/planning markers are present in the `.codex/*` surfaces" and records the two node commands. The marker-presence check is accurate (the `rg` evidence holds), but the line undersells its own evidence grade: it is consistent with both "the live files contain the intended content" and "the markers are present but shallow". The `R5.18b` review's own verification is stronger (`REVIEWS/checkpoint-5-r5-18b-review-planning-chain-launch-internal-r1.md:30-33`). Not a blocker; future status prose should mirror the stronger internal-review verification language.

## What Is Already Strong

Listed so a later fix pass does not regress them.

- The `R5.18a1` contradiction ledger is genuinely load-bearing. Every non-first-wave live item has a decision, contradiction statement, owner, reopen trigger, and split-comparison traceability row, and the `R5.18b/c` internal reviews demonstrate that neither patch wave touched those kept-out items. Grep for the exclusion-heuristic phrases (`thin wrapper`, `only a mapper`, `not runtime-authoritative`, `secondary surface`, `intersection-not-union`, `authority vs must-edit`, `mandatory conditional disposition`) over every spot-check file returned zero hits, so none of the prohibited heuristics re-entered as standing doctrine. This is honest follow-through on Q1 and Q5.
- `R5.18a2`'s `R8.1`–`R8.4` later-lane naming is explicit and non-collapsed: `TASKS.md:46-55` carries a dedicated `Later / Post-Rerun Ownership` section with named owners, triggers, and guardrails; `STATE.yaml:13` encodes "broader_r8_later_lane_ownership_not_yet_review_ratified" as an explicit open blocker; `STATUS.md:150-165` numbers the broader-ownership concern as a distinct blocking finding rather than flattening it into ambient "later work". This answers Q2 well.
- Router-pair asymmetry is handled honestly at the routing surface. The `gsd-do` / `workflows/do.md` pair distinguish `$gsd-review`, `$gsd-plan-phase --reviews`, and `$gsd-verify-work` as three separate routes (`do.md:47-53`; `gsd-do/SKILL.md:54`); the `$gsd-audit-uat` router does not appear in the routing table and the skill/workflow pair remains at pre-patch `mtime` (both 2026-04-15, prior to the R5.18b/c landings at 2026-04-16), consistent with the `park-with-trigger as paired non-promotion` disposition. This answers Q3.
- Downstream semantic-uptake obligations actually land where the review consumer contract requires them. `planner-reviews.md:7-48` forces planners to build a must-address set from both the consumer contract and strong individual criticisms; `plan-phase.md:705-709` and `:855-857` force the checker to fail plans that dismiss lone high-signal criticism or omit must-address review items; `plan-phase.md:780` explicitly downgrades `## PLANNING COMPLETE` to `## PLANNING INCONCLUSIVE` when the `Review Feedback Addressed` section is missing. That is real semantic enforcement, not authority talk. This answers Q4 at the live-runtime layer (the overlay-canon layer is where Finding 1 bites, not here).
- The chain-tail CLI in `.codex/get-shit-done/bin/lib/phase.cjs:11-109,875-1129` and `.../roadmap.cjs:184-222,293-381` materializes the `completion_mode` / `clean_completion` / `debt_bearing` / `verification_pending` / `checkbox_conflicts_with_disk` distinctions as first-class fields in `roadmap analyze --raw`, which I verified by running the command and seeing all five new fields on every phase record. The executor/verifier toml pair and the overlay pair are content-identical modulo `__PROJECT_ROOT__` placeholder expansion (diff against each other returns only path differences). This part of R5.18c actually clears the "debt-aware completion routing" promise on the live runtime, and the overlay tomls would clear it on the tracked tree too — if they were committed (Finding 1).

## Question Statuses

Per the spec, one row per required question.

1. **Did the `R5.18a1` contradiction ledger actually govern `R5.18b/c` scope?** — Yes, at the live-runtime layer. No parked item leaked back in; the grepped exclusion-heuristic phrases are absent; router parking discipline held. Strong `accept`.
2. **Did the `R5.18a2` later-lane assignments remain explicit?** — Yes. `R8.1`–`R8.4` remain named owners in `TASKS.md`, `STATE.yaml`, `STATUS.md`, and `GATES/checkpoint-5.md`, and the executed patches do not imply closure by adjacency. `accept`.
3. **Is router asymmetry handled honestly?** — Yes at the routing surface. `gsd-do` promoted-pair is symmetric; `gsd-audit-uat` is parked paired non-promotion with unchanged `mtimes`. `accept`.
4. **Did authority shelter stay narrow, or did the executed bundle use governing files as a shield against downstream semantic-uptake obligations?** — Narrow for the review/planning doctrine uptake (planner-reviews.md and plan-phase.md actually enforce must-address), but *broad* for the tracking/authority posture: the "partially git-tracked" framing (Finding 2) uses the gitignore convention as a shield against the overlay-canon obligation (Finding 1). `revise-current`.
5. **Did any standing-doctrine use of the blocked exclusion heuristics slip back in?** — No. Direct grep across all R5.18-patched files returned zero hits. `accept`.
6. **Does package truth now accurately describe the implemented frontier and the remaining live contradictions?** — Partially. The internal-frontier story, contradiction ledger, and later-lane ownership are honest. The overlay-vs-live divergence is called "partially git-tracked" and `R5.8`'s bounded-risk disposition is inconsistent with the actual materialization mismatch. `revise-current`.
7. **Does the partially git-tracked local-runtime surface create any material review or closure risk that the package is undercalling?** — Yes, materially. Findings 1–3. `revise-current` at minimum, possibly `reactivate-earlier` for `R5.8`.

## Residual Risks

- If Finding 1 is addressed but Findings 2–4 are not, the review surface will claim closure but future readers will continue to misread the bundle as "tracking-caveat only" rather than as a completed-and-reproducible Checkpoint 5 follow-through. Keep the fix bundle tight so the tracking-divergence statement and the `R5.8` re-disposition travel with the overlay commit, not in a later docs pass.
- If Finding 1 is addressed by adding overlay parity without retesting, there is a secondary risk that the newly-tracked overlay versions drift from the live files during the fix-commit process itself. Recommend driving the overlay versions from the live files (with explicit `/home/rookslog/workspace/projects/prix-guesser/` → `__PROJECT_ROOT__` substitution), then re-running the two verification `node` commands after setup-script reinstall to confirm overlay-materialized content matches the content reviewed here.
- `R5.19` exclusion-heuristic prohibition remains governance-only doctrine; the first adversarial test of whether the heuristics survive scrutiny is still `open` and is not advanced by this bundle. That is honest per the `R5.18a1` ledger row, but a reader who closes this checkpoint should not inherit the prohibition as if it were adversarially validated.
- The `R5.19d4` "operational consequences" pressure on milestone-boundary consumers, `commands.cjs`, `init.cjs`, and `summary.md` template hardening genuinely stays outside this wave (`STATUS.md:164-165`). A later reader should treat Checkpoint 5 as closing the rerun-blocking subset only, not as closing the broader lifecycle debt that `R8.2` now owns.
- The signal file currently present in the working tree at `.planning/knowledge/signals/prix-guesser/2026-04-16-explicit-opus-1m-needed-for-large-claude-reread.md` documents that large-context Opus reruns are sometimes required for this kind of review; this `opus-4-7[1m]` review was run under that lane. If any later review uses a non-`[1m]` Claude CLI, its output should be treated as preserved partial evidence, not as the clean cross-vendor reread.

## What Would Need Revision Before Closure

Treat Checkpoint 5 closure as `blocked` until all of the following are answered in one coherent patch pass.

1. Land R5.18b/c parity into the *tracked* portable-GSD overlay:
   - Add tracked overlay files under `tooling/portable-gsd/overlay/` for every R5.18-patched live path that is currently overlay-only in untracked form or overlay-missing (see Finding 1 for the concrete list), using `__PROJECT_ROOT__` placeholders that match `setup-portable-gsd.sh`'s substitution.
   - Patch the already-tracked overlay `agent-contracts.md` and `plan-phase.md` to match the R5.18c/b content currently only present in the live copies.
   - Commit the overlay additions and patches in a single change so the tracked tree, when reinstalled, reproduces the R5.18 runtime.
2. Reframe the "partially git-tracked" language everywhere it appears (`REVIEWS/checkpoint-5-r5-18d-integration-and-review-prep-launch-internal-r1.md:40`; `REVIEWS/checkpoint-5-r5-18b-…-r1.md:28`; `REVIEWS/checkpoint-5-r5-18c-…-r1.md:26`; `STATUS.md:107-110`; `STATE.yaml:20`; `GATES/checkpoint-5.md:138`) so that, post-fix, it states plainly that R5.18 is reproducible from the tracked tree, and so that prior to the fix the language names the divergence rather than calling it a tracking caveat.
3. Reclassify `R5.8` (`TASKS.md:39`, `REVIEWS/checkpoint-5-r5-18a1-…-r1.md:175-185`) against the fired trigger. Either reactivate and bound the reactivation explicitly, or articulate why the overlay/live divergence does not constitute the branch/worktree materialization mismatch that the trigger names.
4. Restore the full seven-question review frame in `GATES/checkpoint-5.md:107-110` and in the `R5.18d` integration artifact's "Review Surface" list so package truth and the review spec do not disagree on how many questions Checkpoint 5 closure must answer.
5. Re-run the two `node` verification commands after the setup-script reinstall to confirm that the tracked overlay, materialized back into `.codex/*`, still returns `module-load-ok` and a `roadmap analyze --raw` with the full `completion_mode` / `clean_completion` / `debt_bearing` / `completion_warnings` / `checkbox_conflicts_with_disk` field set. Record that check in `R5.18d` (or an `R5.18e` reread spec) so the verification is traceable to the tracked canon rather than only to the local worktree.

Only after 1–5 is it honest to route this bundle into checkpoint close. Internal follow-up review plus a brief cross-vendor reread of the overlay-parity commit is a proportionate closing step under the `disposition_ladder` value `revise-current` in `REVIEW-POLICY.yaml:38`.

## Disposition

- `revise-current` on the overall bundle.
- `escalate-cross-vendor` is not additionally required — this review already *is* the cross-vendor lane the policy calls for at Checkpoint 5 (`REVIEW-POLICY.yaml:106-115`; `cross_vendor_default: strongly_preferred`, `preferred_cross_vendor_model: opus`). A brief same-vendor reread after the fix is sufficient unless the fix itself reopens doctrine.
- Individual-finding classifications: Finding 1 `revise-current` / high stakes; Finding 2 `revise-current`; Finding 3 `revise-current` (or `reactivate-earlier` if the fix owner prefers); Findings 4 and 5 `revise-current` and `defer-nonblocking` respectively.

## Verdict

- status: `blocked`
- explanation: The executed bundle's internal-frontier story is genuinely strong on the doctrine surface — contradiction ledger, later-lane naming, router-pair discipline, exclusion-heuristic prohibition, and downstream semantic-uptake enforcement are all honest and load-bearing. But the patched runtime is not reproducible from the tracked tree. That is not a tracking-tool caveat; it is an overlay/live canon divergence at exactly the materialization seam `R5.8` is supposed to guard, and the integration artifact, STATUS, STATE, and gate language all soften it into "partially git-tracked" rather than name it. Closure on evidence that only lives in one worktree is below the readiness quality bar this checkpoint earned; closure requires the overlay parity commit, the re-disposition of `R5.8`, and the language rewrite.

## Required Next Action

- exact next step: owner opens a bounded fix lane (suggested name `R5.18f` or `R5.18e2`, keeping `R5.18e` available for the external-reread artifact family) that lands overlay parity, the STATUS/STATE/GATES/R5.18d language rewrite, the `R5.8` re-disposition, and the re-verification described in "What Would Need Revision Before Closure" items 1–5. After commit, a short same-vendor reread of the overlay-parity diff is sufficient for closure; a second cross-vendor pass is only needed if the rewrite itself reopens doctrine.
- owner / lane: `R5.18` boundary owner for overlay materialization + Checkpoint 5 package-truth owner.
- commit implication: `fix then commit` (the fix is the closing commit; the current working tree should not be checkpointed as-is because `STATUS.md`/`STATE.yaml` still claim a frontier the tracked tree cannot reproduce).

## Independence Note

- Does this review satisfy the checkpoint's independent-review requirement? Yes for the cross-vendor lane. `REVIEW-POLICY.yaml:106-115` names cross-vendor as `strongly_preferred` at Checkpoint 5 and prefers Opus. This review was run by Anthropic Opus 4.7 (`claude-opus-4-7[1m]`) against a working tree authored by Codex, so vendor independence holds.
- Was a cross-vendor lane available? Yes; it is the one being run now.
- If cross-vendor was available, which Claude lane was appropriate here and why? The large-context Opus lane, because the bundle requires reading the full executed runtime plus the full upstream `R5.18a1/a2/b/c/d` artifacts plus the packaging-truth set in one pass; the earlier `R5.17e` cross-vendor work already recorded a signal that non-`[1m]` Opus overflows on this kind of full-bundle reread.
- If used, what did independence add? Independence surfaced Finding 1. Internal review ran against a Codex-authored bundle on the same machine that authored it, and its own language ("partially git-tracked") treated the overlay-vs-live divergence as a reviewer-tooling caveat. A cross-vendor reader with no authoring context read that same caveat as authority-shelter hiding a concrete materialization mismatch. That reframing is the independence value — the facts were visible, but the frame flipped only under an external lane.
