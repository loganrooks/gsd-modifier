# Checkpoint 5 R5.19b4 Bin / Agent / Overlay / Runtime-Control Exclusion-Justification Audit Internal R1

## Summary

- [d:c+r:i] The current bin/overlay boundary is only partly defensible. `phase.cjs`, `roadmap.cjs`, `tooling/portable-gsd/overlay/agents/gsd-executor.toml`, and `tooling/portable-gsd/overlay/agents/gsd-verifier.toml` remain correctly inside active Checkpoint 5 consideration because their own file lines still encode cheap-closure or no-debt-carrier behavior, and `R5.18` already promotes them into Bucket 1. Sources: `.codex/get-shit-done/bin/lib/phase.cjs:771-824`; `.codex/get-shit-done/bin/lib/roadmap.cjs:176-195`; `tooling/portable-gsd/overlay/agents/gsd-executor.toml:361-399`; `tooling/portable-gsd/overlay/agents/gsd-verifier.toml:486-500`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:92-100`.
- [d:c+r:i] The current live-agent boundary is under-justified. Any frontier that promotes overlay `gsd-executor.toml` / `gsd-verifier.toml` while leaving the runtime-authoritative `.codex/agents/gsd-executor.toml` / `.codex/agents/gsd-verifier.toml` copies ambient is not scrutiny-resistant, because `.codex/config.toml` points Codex at the live `.codex/agents/*.toml` files and the implementation spec itself requires `.codex`/overlay pairing for touched runtime surfaces. Sources: `.codex/config.toml:52-55,112-114`; `.codex/agents/gsd-executor.toml:361-399`; `.codex/agents/gsd-verifier.toml:486-500`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:29-37`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:92-100`.
- [d:c+r:i] The only clean surviving preserved exclusion in this lane is `tooling/codex/capture_launch_truth.py` rendering cleanup. It still has bounded quality upside, but its own file semantics are launch-truth capture and disclosure, not completion/debt routing; leaving it out of the current debt/completion corrective wave does not preserve the core cheap-closure contradiction. Sources: `tooling/codex/capture_launch_truth.py:248-371`; `WORKFLOW.md:71-82`; `AI-GUARDRAILS.md:89-91`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:218-228`.
- [d:c+r:i] `commands.cjs`, `uat.cjs`, and `audit.cjs` can stay out of first-wave patch-now treatment only as explicit-disposition surfaces already inside active consideration. They are not clean exclusions: `commands.cjs` already owns adjacent status vocabulary, while `uat.cjs` and `audit.cjs` consume non-passing verification/UAT states downstream. Sources: `.codex/get-shit-done/bin/lib/commands.cjs:12-35`; `.codex/get-shit-done/bin/lib/uat.cjs:53-70,211-251`; `.codex/get-shit-done/bin/lib/audit.cjs:347-476`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:132-145,162-178`.

## Exclusions That Survive

### `tooling/codex/capture_launch_truth.py`

- [d:c+r:i] Judgment: preserved exclusion survives for the current debt/completion wave.
- Propagation-level case: the file captures requested-versus-effective worker-launch truth and renders caveated markdown; it does not emit verifier status, mutate phase completion, or route milestone progression. Its output can influence review quality, but not the producer/routing contradiction that defines the current chain-tail repair set.
- Independent-file case: there is still real quality upside in making the `--latest` weakness more prominent at point of use, but that gain is local to launch-truth review honesty rather than the active completion-mode repair.
- Sphere-of-influence proof: `render_markdown()` summarizes requested/effective rows, appends a `--latest` caveat only when applicable, and explicitly says missing runtime fields must stay unresolved. The file never touches ROADMAP, VERIFICATION, SUMMARY, or phase-status routing. Sources: `tooling/codex/capture_launch_truth.py:235-371`.
- Direct file-line evidence from the excluded file: `tooling/codex/capture_launch_truth.py:248-271` (requested/effective assessment); `tooling/codex/capture_launch_truth.py:358-369` (weaker `--latest` caveat plus unresolved-field reminder).
- Direct file-line evidence from the exclusion source: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:218-228` preserves `launch-truth rendering cleanup`; `WORKFLOW.md:71-82` and `AI-GUARDRAILS.md:89-91` already encode the honest-use rule around the helper.

### `.codex/get-shit-done/bin/lib/commands.cjs`

- [d:c+r:i] Judgment: keeping `commands.cjs` out of Bucket 1 survives, but only as explicit-disposition, not as preserved exclusion.
- Propagation-level case: `determinePhaseStatus()` derives status labels from plan/summary/verification state, but the currently contested cheap-closure routing happens in `phase.cjs`, `roadmap.cjs`, `progress.md`, and `transition.md`, which do not currently defer to this helper for the completion/debt boundary.
- Independent-file case: the file is still too load-bearing to disappear by omission because it already owns adjacent `Complete` / `Needs Review` / `Executed` vocabulary. That is why Bucket 2 plus the Bucket 3 representation-mechanism choice is the defensible posture.
- Sphere-of-influence proof: the function returns strings only; it does not flip ROADMAP checkboxes, write progress rows, or authorize next-step routing. Sources: `.codex/get-shit-done/bin/lib/commands.cjs:12-35`.
- Direct file-line evidence from the excluded file: `.codex/get-shit-done/bin/lib/commands.cjs:15-35`.
- Direct file-line evidence from the exclusion source: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:135-145` places `commands.cjs` in Bucket 2 and explicitly says it has stronger standing than `uat.cjs` / `audit.cjs`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:162-178` keeps the debt-carrier mechanism as an open scope-gating choice.

### `.codex/get-shit-done/bin/lib/uat.cjs` and `.codex/get-shit-done/bin/lib/audit.cjs`

- [d:c+r:i] Judgment: keeping these files out of Bucket 1 survives, but only as explicit-disposition surfaces already inside active consideration.
- Propagation-level case: both files consume non-passing states after the fact. `uat.cjs` extracts `human_needed` / `gaps_found` items for workflow consumption; `audit.cjs` scans phases for incomplete UAT or verification gaps. Neither file is currently the first authority that marks a phase complete or routes the user onward.
- Independent-file case: because they consume the same debt-bearing states the repair set is trying to formalize, they remain independently load-bearing for later audit truthfulness and cannot be silently dropped.
- Sphere-of-influence proof: the current functions aggregate or report gap state; they do not define the terminal state vocabulary or completion-routing contract. Sources: `.codex/get-shit-done/bin/lib/uat.cjs:53-70,211-251`; `.codex/get-shit-done/bin/lib/audit.cjs:347-476`.
- Direct file-line evidence from the excluded files: `.codex/get-shit-done/bin/lib/uat.cjs:53-70,211-251`; `.codex/get-shit-done/bin/lib/audit.cjs:347-398,418-476`.
- Direct file-line evidence from the exclusion source: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:137-145` keeps both in Bucket 2 with weaker standing than `commands.cjs`.

### Non-phase-critical `.codex/agents/*.toml` remainder outside the five Track A roles

- [d:c+r:i] Judgment: this narrower exclusion survives; blanket `.codex/agents/` exclusion does not.
- Propagation-level case: the rerun path directly invokes `gsd-phase-researcher`, `gsd-planner`, `gsd-plan-checker`, `gsd-executor`, and `gsd-verifier`. The launch spec's Track A write scope names only those five runtime-authoritative `.toml` files and explicitly says not to patch every `.toml` in the repo.
- Independent-file case: the broader agent family may matter for later workflows, but no current Checkpoint 5 file in this lane shows that `gsd-code-reviewer`, `gsd-ui-*`, `gsd-doc-*`, or similar roles are on the rerun-critical discuss/plan/execute/verify path.
- Sphere-of-influence proof: the rerun workflows enumerate the five phase-critical roles, while the launch spec treats broader `.toml` sweeping as a non-goal. Sources: `.codex/get-shit-done/workflows/discuss-phase.md:18-25`; `.codex/get-shit-done/workflows/plan-phase.md:16-19`; `.codex/get-shit-done/workflows/execute-phase.md:38-42`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-launch-spec.md:52-71`.
- Direct file-line evidence from the excluded surface: `.codex/config.toml:28-50,92-110` shows multiple non-phase-critical agent registrations with code-review, UI, doc, and profiling purposes outside the rerun-critical chain.
- Direct file-line evidence from the exclusion source: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-launch-spec.md:54-70`.

## Exclusions That Fail

### Blanket `.codex/agents/` omission once overlay counterparts are active

- [d:c+r:i] Judgment: fails.
- Propagation-level case: `.codex/config.toml` points Codex at the live `.codex/agents/*.toml` files, not at the overlay copies. Once a Checkpoint 5 track changes the operative agent contract in overlay, leaving the live `.codex/agents` counterpart ambient would keep the currently launched worker on the old contract until re-materialization or reinstall.
- Independent-file case: the live `.codex/agents/*.toml` files are runtime-authoritative regardless of overlay tracking. Their own lines are load-bearing even if the tracked source-of-truth lives under `tooling/portable-gsd/overlay/`.
- Sphere-of-influence proof: the config registry maps `gsd-executor` and `gsd-verifier` to live `.codex/agents` paths; the implementation spec states that every touched runtime surface under `.codex/` must be paired with a tracked overlay counterpart, not replaced by it. Sources: `.codex/config.toml:52-55,112-114`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:29-37`.
- Direct file-line evidence from the excluded files: `.codex/agents/gsd-executor.toml:361-399` still defines the live SUMMARY carrier; `.codex/agents/gsd-verifier.toml:486-500` still defines the live three-terminal-state tree.
- Direct file-line evidence from the exclusion source: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:94-99` names only the overlay `gsd-executor.toml` / `gsd-verifier.toml` files in Bucket 1, with no paired live `.codex/agents` entries.

### Live `.codex/agents/gsd-executor.toml` and `.codex/agents/gsd-verifier.toml`

- [d:c+r:i] Judgment: current non-modification is invalid.
- Propagation-level case: the live files carry exactly the same completion/debt contract that made the overlay copies Bucket 1 files. Excluding the live copies would create a split where the tracked overlay is "fixed" while the active runtime still launches the old contract.
- Independent-file case: these files remain first-order operative surfaces even after Track A alignment; they are not documentation or install metadata.
- Sphere-of-influence proof: `.codex/config.toml` loads them directly, and the live files themselves still lack a debt-bearing completion slot. Sources: `.codex/config.toml:52-55,112-114`; `.codex/agents/gsd-executor.toml:365-367,427-430`; `.codex/agents/gsd-verifier.toml:488-500,582-585`.
- Direct file-line evidence from the excluded files: `.codex/agents/gsd-executor.toml:365-367,427-430`; `.codex/agents/gsd-verifier.toml:488-500,582-585`.
- Direct file-line evidence from the exclusion source: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:94-99`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:29-37`.

### Overlay-only treatment of the active research / steering agent tracks

- [o:c+r:i] Judgment: under current evidence, overlay-only treatment is under-justified and should be treated as a conditional failure if those tracks stay active.
- Propagation-level case: `discuss-phase.md` and `plan-phase.md` route through `gsd-phase-researcher`, `gsd-planner`, and `gsd-plan-checker`; the implementation spec keeps their overlay counterparts inside the active research-disposition and steering-consumer ownership sets. If those overlay files are edited without paired live `.codex/agents` treatment, the same overlay/live drift problem reappears one layer earlier in the chain.
- Independent-file case: after Track A the direct doctrine contradiction on these live files is reduced, so this is weaker than the executor/verifier case; but it is still not a clean exclusion if the corresponding overlay files remain in active scope.
- Sphere-of-influence proof: the rerun workflows invoke these roles, the live files are the registered runtime targets, and the implementation spec names their overlay counterparts inside active scope. Sources: `.codex/get-shit-done/workflows/discuss-phase.md:18-25`; `.codex/get-shit-done/workflows/plan-phase.md:16-19`; `.codex/config.toml:68-78`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:41-71`.
- Direct file-line evidence from the excluded files: `.codex/agents/gsd-phase-researcher.toml:32-43`; `.codex/agents/gsd-planner.toml:40-47`; `.codex/agents/gsd-plan-checker.toml:36-43`.
- Direct file-line evidence from the exclusion source: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:41-71` names only the overlay agent counterparts inside these two active ownership sets.

## Runtime / Chain-Tail Surfaces That Must Move Into Active Consideration

### Immediate

- [d:c+r:i] `.codex/agents/gsd-executor.toml` must move into explicit `R5.18` consideration as the live pair of promoted overlay `gsd-executor.toml`. Current omission is not defensible on runtime-authority grounds. Sources: `.codex/config.toml:52-55`; `.codex/agents/gsd-executor.toml:361-399`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:29-37`.
- [d:c+r:i] `.codex/agents/gsd-verifier.toml` must move into explicit `R5.18` consideration as the live pair of promoted overlay `gsd-verifier.toml`. Current omission is not defensible on runtime-authority grounds. Sources: `.codex/config.toml:112-114`; `.codex/agents/gsd-verifier.toml:486-500`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:29-37`.

### Conditional On Active Steering / Research Contract Work Staying Open

- [o:c+r:i] `.codex/agents/gsd-phase-researcher.toml` must move into explicit paired consideration if `R5.18` keeps the research-disposition contract active, because the implementation spec still treats the overlay researcher file as an active ownership surface. Sources: `.codex/config.toml:68-70`; `.codex/agents/gsd-phase-researcher.toml:32-43`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:41-54`.
- [o:c+r:i] `.codex/agents/gsd-planner.toml` must move into explicit paired consideration if `R5.18` keeps the steering-consumer branch active, because the implementation spec still treats the overlay planner file as an active ownership surface. Sources: `.codex/config.toml:76-78`; `.codex/agents/gsd-planner.toml:40-47`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:58-71`.
- [o:c+r:i] `.codex/agents/gsd-plan-checker.toml` must move into explicit paired consideration under the same condition, because the implementation spec still treats the overlay checker file as an active ownership surface. Sources: `.codex/config.toml:72-74`; `.codex/agents/gsd-plan-checker.toml:36-43`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:41-54,58-71`.

### No Additional Move Required

- [d:c+r:i] No additional move is required for `.codex/get-shit-done/bin/lib/phase.cjs`, `.codex/get-shit-done/bin/lib/roadmap.cjs`, `tooling/portable-gsd/overlay/agents/gsd-executor.toml`, or `tooling/portable-gsd/overlay/agents/gsd-verifier.toml`; their exclusion already failed, and `R5.18` correctly holds them in Bucket 1. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:92-100`.

## Potential Quality Gains Left On The Table

- [p:r:i] Pairing the live `.codex/agents` executor/verifier files with their overlay counterparts would eliminate the current "overlay fixed, runtime still stale until rematerialized" risk and would make `R5.18`'s active frontier match the files Codex actually launches.
- [p:r:i] If the steering/research tracks remain active, pairing the live researcher/planner/checker files would prevent a second round of overlay/live doctrine drift on the earlier planning chain.
- [p:r:i] Promoting `commands.cjs` from explicit disposition into a later targeted patch could give the harness one authoritative status-vocabulary helper instead of leaving completion-mode semantics duplicated in routing surfaces.
- [p:r:i] Promoting `uat.cjs` and `audit.cjs` later could make debt-bearing completion more visible in cross-phase audit and UAT scans, reducing later reread ambiguity even if those files stay out of first-wave.
- [p:r:i] Reopening `capture_launch_truth.py` in a later Track C cleanup could make `--latest` weakness harder to miss in downstream review artifacts, but that is bounded launch-truth polish rather than current chain-tail repair.

## Read-Set Adequacy

- [d:c+r:i] The read set is adequate to judge the active bin / overlay / runtime-control boundary and the live-agent pairing problem. This pass directly read the governing specs, `STATUS.md`, `TASKS.md`, `GATES/checkpoint-5.md`, `PROTOCOL.md`, `R5.18`, the relevant `R5.17d2` / `R5.17e` adjudication stack, `.codex/config.toml`, the candidate bin files, the overlay executor/verifier files, the live `.codex/agents` executor/verifier/researcher/planner/checker files, the rerun-path workflow invocation lists, and `capture_launch_truth.py`.
- [d:c+r:i] The read set is also strong enough to defend the narrow surviving exclusion for `capture_launch_truth.py` and the non-first-wave treatment of `commands.cjs`, `uat.cjs`, and `audit.cjs`, because those judgments turn on each file's own semantics plus explicit `R5.18` bucket placement rather than on inherited category heuristics.
- [o:r:i] The read set is not a directory-wide reread of every non-phase-critical agent file under `.codex/agents/`. The surviving exclusion for the non-phase-critical remainder is therefore a family-level bounded judgment grounded in the rerun-path invocation list and the Track A non-goal, not a per-file certification of the entire directory. If a later lane wants to challenge `gsd-code-reviewer`, `gsd-ui-*`, `gsd-doc-*`, or other off-path agents for Checkpoint 5 relevance, it should widen the read set explicitly rather than inherit this narrower family judgment.
