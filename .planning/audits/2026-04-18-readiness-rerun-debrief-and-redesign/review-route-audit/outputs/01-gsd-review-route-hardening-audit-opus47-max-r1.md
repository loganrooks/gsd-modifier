Date: 2026-04-22
Status: first-pass bounded audit output

# GSD Review Route Audit

## Current Route Reading

- [d:r:i] The route as it stands is a single sequential-dispatch shell loop sitting on top of whatever stdout each CLI happens to produce. Every reviewer is treated as a plain-stdout runner; `claude`, `codex`, `gemini`, `coderabbit`, and `opencode` all funnel through the same `2>/dev/null > /tmp/...` shape in [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:156).
- [d:r:i] Prompt, per-reviewer output, and any transient debug artifacts all land in `/tmp`. The same workflow then commits a synthesis artifact at `{phase_dir}/{padded_phase}-REVIEWS.md`, and the workflow's final step deletes the temp files ([review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:278)). Nothing durable survives the run other than the synthesis file, which collapses five reviewer runs into one consumer artifact with no trail back to the raw material or how each invocation was actually configured.
- [d:r:i] The `/tmp` choice directly contradicts the repo-local probe rule already written in [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:26). That rule is not incidental. It exists because a Claude headless run that looks like a silent post-dispatch crash often turns out to be a permission-ambiguity failure on file-mediated prompts, and `/tmp` prompts make that failure mode harder to see.
- [d:r:i] Launch-truth is absent. The workflow sends a model-bearing CLI invocation and records nothing about what model, reasoning, or permission posture the reviewer actually ran under, which is the exact gap the pattern library and [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py) were written to close for external lanes ([AUDIT-LANE-PATTERN-LIBRARY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/AUDIT-LANE-PATTERN-LIBRARY.md:47)).
- [d:r:i] Timing discipline is also absent. No pre-launch estimate, no post-run elapsed measurement, no calibration note, while the broader repo already carries wall-clock records across wave launches in [LAUNCH-LEDGER.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/root-support/LAUNCH-LEDGER.md:28) and has an explicit calibration rule at the top of that file.
- [d:r:i] The failure contract is binary and destructive. `claude -p "..." 2>/dev/null > file` hides every error signal, and the workflow only adds a size check on OpenCode ([review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:180)). A reviewer whose process emits three paragraphs of assistant text and then dies before a final `result` event produces a zero-byte output, and the route drops the content silently.
- [d:r:i] The planner-consumer contract is the strongest surviving part. [planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:7) and [plan-phase.md step 9](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:786) actively read the `Review Consumer Contract` block, refuse to finish `--reviews` replanning without `Review Feedback Addressed`, and categorize Must/Should/Consider/Rebut from it. That contract is repo-load-bearing, which is why the hardening question lives at the run surface rather than at the synthesis artifact.

## Keep Versus Replace

- [d:r:i] Keep the route. Harden it in place. Do not replace `$gsd-review` and do not fork a parallel review-route family as the first slice.
- [d:r:i] Reasons to keep: the `{padded_phase}-REVIEWS.md` artifact, its Review Consumer Contract sections, and the `--reviews` re-plan mode already form a producer/consumer pair that planner, plan-checker, and revision loop all treat as source-of-truth. Replacing the route churns three consumers and a doctrine file without widening what the route carries.
- [d:r:i] Reasons not to add a sibling route yet: the real pressure is that the single existing route flattens reviewer shapes and loses salvage. A second route family would inherit both gaps unless the hardening is done first, so the hardening is the prerequisite for any later subject-keyed split rather than a branch of it.
- [d:r:i] What the hardening is not: it is not a telemetry system, it is not a reviewer orchestrator, and it is not a cross-provider portability layer. It is a bounded widening of what each review run preserves, classifies, and hands off.

## Reviewer Shapes

Three runner shapes belong in the route, and the first slice should refuse to flatten them.

- [d:r:i] **Claude (`claude -p`, primary horizon).** Stream-JSON capable through `--output-format stream-json --include-partial-messages`. Last-assistant-message is recoverable after exit via [tooling/codex/extract_stream_text.py --last-message](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/extract_stream_text.py:173). Reads repo-local prompt files under `--dangerously-skip-permissions` as documented in [tooling/codex/run_claude_probe.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/run_claude_probe.py:156). Launch-truth (session id, model, cost, elapsed) is emitted inline as `system`/`result` events in the stream itself, so requested-vs-effective can be captured from the stream rather than from an external database.
- [d:r:i] **Codex (`codex exec`, primary horizon).** Produces text output, but the load-bearing requested-vs-effective evidence lives in `~/.codex/state_5.sqlite` and is already formalized by [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py). Salvage for a partially-returned run is the same last-message pattern as Claude when `codex exec` is run with a JSON-lines compatible transcript, and falls back to file-tail extraction on plain-stdout runs.
- [d:r:i] **Plain-stdout reviewers (`gemini -p`, `opencode run -`, `coderabbit review --prompt-only`).** No stream format, no sqlite launch-truth source. Best available evidence for these is: requested invocation string, exit code, byte count, stdout file, stderr tail, wall-clock elapsed. These keep their current shape but stop writing to `/tmp` and stop being the silent case that defines the whole route's floor.

The first-slice helper work pays off most on Claude and Codex. The plain-stdout shape widens by inheriting run-home and launch-truth-lite (the invocation line plus exit code and elapsed), not by inventing a fake stream where none exists.

## First-Slice Hardening Shape

This is the bounded first live slice. Each item names the surface and holds its scope.

- [d:r:i] **Run-home per review run.** Write all prompt, per-reviewer raw output, stderr, stream-json (when available), and metadata under `.planning/phases/{padded_phase}/reviews/{run_id}/` where `run_id` is `{ISO-timestamp}-{short-git-sha}`. The `{padded_phase}-REVIEWS.md` synthesis stays in the phase directory unchanged so the planner consumer contract does not move. The `/tmp` paths come out of the workflow entirely for prompt and output; debug/stderr may still land in `/tmp` if a runner demands it, but the canonical per-reviewer artifacts belong in the run-home.
- [d:r:i] **Per-reviewer launch-truth.** Produce `launch-truth/{reviewer}.md` inside the run-home. For `claude`, parse the stream-json `system.init` and `result` events for model, session id, cost, and elapsed. For `codex`, call the existing `capture_launch_truth.py` with a pre-spawn `--since` boundary and write the artifact directly into the run-home. For plain-stdout reviewers, record the exact invocation, exit code, byte count, and elapsed. Requested settings go in the same file as declared intent, independent of whether the reviewer exposes effective settings.
- [d:r:i] **Per-run timing record.** `timing.md` in the run-home carries one pre-launch estimate (single value or bounded range) per reviewer and one post-run actual, plus the one-line calibration note prescribed by [LAUNCH-LEDGER.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/root-support/LAUNCH-LEDGER.md:4). The estimate is allowed to be naive on the first run; the point is to widen the repo's runtime model as runs accumulate.
- [d:r:i] **Claude runner uses stream-json.** Replace `claude -p "$(cat prompt)" 2>/dev/null > output.md` with an invocation that matches the repo's own probe shape: `--output-format stream-json --include-partial-messages --verbose`, repo-local prompt path, `--dangerously-skip-permissions` when the prompt is file-referenced. The `output.md` for the synthesis block is then reconstructed from the stream instead of being the only surviving artifact.
- [d:r:i] **Codex runner keeps `codex exec` but adds launch-truth.** Record `--since` just before spawn, call `capture_launch_truth.py` immediately after, write the artifact into run-home. Leave codex's transcript format as-is for the first slice; do not force a stream-json migration where codex's own shape is already covered by the sqlite capture.
- [d:r:i] **Plain-stdout reviewers inherit run-home and the byte-size sanity check.** The `[ ! -s ... ]` check that currently only wraps OpenCode applies to all plain-stdout reviewers. If the output is empty, that is an `absent` reviewer state, not an empty synthesis block.
- [d:r:i] **Three reviewer states in REVIEWS.md.** `complete`, `partial`, `absent` (details in the next section). Each reviewer section in the synthesis artifact carries one of the three states and a pointer into the run-home, so the planner consumer can still read the contract without chasing the raw material, and the operator can still chase it when needed.

These widenings are additive. Each one survives standalone; the slice is sharpened when all of them land together but the route does not break if, for example, the timing record is ahead of the stream-json migration.

## Helper Versus Workflow Split

- [d:r:i] **Helper owns** (narrow, testable):
  - stream-json invocation for Claude with the repo-local probe defaults,
  - `codex exec` invocation plus the `capture_launch_truth.py` wrap,
  - last-assistant-message extraction from stream-json or transcript,
  - partial-vs-complete-vs-absent classification,
  - launch-truth-lite for plain-stdout reviewers (invocation, exit, byte count, elapsed),
  - run-home path construction and writing the per-reviewer artifact set.
  The natural location is an additive module beside the existing codex tooling family, for example `tooling/codex/run_review_reviewer.py`, reusing `extract_stream_text.py` and `capture_launch_truth.py` rather than duplicating their logic.
- [d:r:i] **Workflow keeps owning** (contract-carrying):
  - reviewer selection, the `SELF_CLI` skip rule, and flag parsing,
  - prompt assembly from PROJECT.md / ROADMAP / PLAN / CONTEXT / RESEARCH / REQUIREMENTS,
  - the REVIEWS.md synthesis block and its Review Consumer Contract sections,
  - commit and display,
  - the planner-consumer surface exposed to [planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md) and [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md).
- [d:r:i] **Helper does not own**: synthesis composition, Must/Should/Consider categorization, the `SELF_CLI` decision, prompt content choices, or the adversarial-review framing. Pushing those into the helper would collapse the line between a runner primitive and the planner-consumer contract, and the consumer contract is the part of the route that is already durable enough to deserve protection.

## Failure Salvage And Last-Message Recovery

- [d:r:i] **Three reviewer states, never a silent empty.** For each reviewer the helper returns:
  - `complete` when the run produced a terminal `result` event or a non-empty stdout and exited zero.
  - `partial` when at least one assistant text block is recoverable but either the exit was nonzero, no terminal `result` appeared, or the output was truncated. REVIEWS.md carries a `## {Reviewer} Review (partial)` section with the salvaged text and a machine-readable footer pointing at the stream-json, stderr tail, exit code, and last error-like line.
  - `absent` when nothing is recoverable. The synthesis section for that reviewer reads as absent with the reason (timeout, nonzero exit with empty stream, permission failure) rather than as an empty heading.
- [d:r:i] **Last-message recovery route.** For `claude` and `codex`, use `extract_stream_text.py --last-message` on the stream-json / transcript file. That module already exists and already handles the case where no terminal `result` appeared. For plain-stdout reviewers, the "last message" is the file content itself, so the partial state reduces to nonzero exit plus non-empty stdout.
- [d:r:i] **Salvage affects the planner contract explicitly.** The synthesis reviewer for each `partial` section must note the partial state inside the Review Consumer Contract when deciding whether a criticism is Must / Should / Consider, rather than silently weighting a partial reviewer down. A partial reviewer with one strong criticism is still a lone high-signal source; the partial tag is metadata, not a downweight.
- [d:r:i] **What this is not.** It is not a retry framework, it is not a reviewer-resume system, and it is not an automatic salvage heuristic that tries to guess what the reviewer meant. It is the narrow rule that no reviewer run disappears into a blank heading when its last assistant message was still on disk.

## Other Review Workflow Uplift Routes

Named now so they do not get reinvented later. None of these land in the first slice.

- [d:r:i] **Subject-keyed route split.** `$gsd-review` currently assumes the subject is a phase plan. The same shell of reviewer dispatch + launch-truth + salvage + synthesis could serve `audit-proposal-reread`, `lane-output-comparative-read`, or `implementation-reread` routes. Each wants a different prompt template and a different consumer artifact. First slice should not split the route; the hardening is the precondition because a route family that still carries `/tmp`-bound outputs and silent failure would multiply the same debt across subjects.
- [d:r:i] **Stronger tie to repo-local audit-lane discipline.** The pattern library in [AUDIT-LANE-PATTERN-LIBRARY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/AUDIT-LANE-PATTERN-LIBRARY.md) names packet / spec / prompt / launch-truth / output / inheritance as recurring objects. The first slice adopts run-home and launch-truth. A later adjacent slice could expose a packet artifact inside the run-home (for example `prompt.md` accompanied by `packet.md` with the read-set and anti-misread notes) so review runs feel less like an external thing stapled onto the phase directory.
- [d:r:i] **Governance refresh at the propagation layer.** The review route is a contract-carrying surface with downstream consumers (planner, plan-checker, revision loop, `--reviews` mode in plan-phase). When the route changes, a propagation-audit `change-triggered-refresh` entry belongs with the slice, consistent with the register in [.planning/HARNESS-IMPROVEMENT-REGISTER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/HARNESS-IMPROVEMENT-REGISTER.md:40).
- [d:r:i] **Later provider-specific salvage.** Once run-home exists, a second-tier salvage could use `claude --resume` for dropped Claude runs or `codex` retry-from-transcript for dropped Codex runs. These are durable improvements but they depend on the run-home and state classification that the first slice lands, so they remain later.
- [d:r:i] **Reviewer-parity carry across `.codex` and `.claude`.** The parity audit landed a typed classification carrier in `portable_gsd_contract.py` ([23-codex-claude-installation-parity-audit-inheritance.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/entry-uplift-audit/dispositions/23-codex-claude-installation-parity-audit-inheritance.md), [134-...-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/134-codex-claude-parity-classification-carrier-proposal.md), [135-...-implementation.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/135-codex-claude-parity-classification-carrier-implementation.md)). The review-route helper should not drag the parity question forward by widening into `.claude` materialization. The first slice's Claude runner only invokes the `claude` CLI, same as the current workflow, and only inside the already established primary horizon.

## Verification And Review Gates

- [d:r:i] **Focused helper coverage.** Tests for `run_review_reviewer.py` cover: last-message extraction on a truncated stream fixture, classification of `complete` vs `partial` vs `absent` for each reviewer shape, run-home path construction, and the requested-vs-effective fields in launch-truth for both Claude (parsed from stream-json) and Codex (parsed from `capture_launch_truth.py` output).
- [d:r:i] **Assembly smoke without external CLIs.** A dry-run mode assembles a REVIEWS.md from fixture per-reviewer artifacts without invoking any external CLI. This keeps the synthesis logic provable in CI and separates "synthesis broke" from "external CLI failed" in later debugging.
- [d:r:i] **One real acceptance run.** At least one `--claude` + `--codex` review against a real small phase, verifying: run-home populated, launch-truth matches requested settings where observable, partial-reviewer footer appears when a run is deliberately truncated, and the planner consumer contract remains readable by `plan-phase.md` step 9 `--reviews` handling without modification.
- [d:r:i] **Propagation check.** `change-triggered-refresh` entry in `propagation-audit/` names the consumer chain (planner, plan-checker, revision loop, `--reviews` mode) and records what moved vs what was explicitly held.
- [d:r:i] **Repo governance gates that apply.** `audit_refmap.py verify` for the audit subtree when outputs/dispositions move. `harness_canary.py` is not load-bearing for this slice; the slice does not change runtime version anchors, overlay manifest, or materialization. Do not invoke it as a false gate.

## Held Later

- [d:r:i] `.claude` materialization parity and runtime-aware dispatch in `setup-portable-gsd.sh`.
- [d:r:i] Subject-keyed `$gsd-review` family split (phase-plan / audit-reread / implementation-reread / comparative-read).
- [d:r:i] Reviewer-resume and retry logic beyond last-message salvage.
- [d:r:i] Automated telemetry, review-run aggregation dashboards, or freshness-scored reviewer-choice routing.
- [d:r:i] Helper ownership of the Review Consumer Contract or the Must/Should/Consider categorization.
- [d:r:i] Multi-provider portability beyond the `.codex` / `.claude` primary horizon. `gemini`, `opencode`, `coderabbit` stay within the route as plain-stdout reviewers; they do not become the shape the first helper slice is designed around.
- [d:r:i] A packet artifact inside the run-home that mirrors the full audit-lane pattern-library scaffolding.
- [d:r:i] Cross-repo distribution of the helper layer.

## Exact Next Move

1. [d:r:i] Land `tooling/codex/run_review_reviewer.py` with three classifications (`complete` / `partial` / `absent`), last-message extraction for stream-json and transcript inputs, launch-truth-lite for plain-stdout reviewers, and a run-home writer that produces `prompt.md`, `{reviewer}.stream.jsonl` (when available), `{reviewer}.stdout.md`, `{reviewer}.stderr.log`, `launch-truth/{reviewer}.md`, and `timing.md` under `.planning/phases/{padded_phase}/reviews/{run_id}/`.
2. [d:r:i] Add focused tests covering the three classifications for each reviewer shape and the two launch-truth sources (stream-json for Claude, `capture_launch_truth.py` for Codex).
3. [d:r:i] Update [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md) so that the `invoke_reviewers` step calls the helper for `claude` and `codex`, calls plain-stdout reviewers with run-home paths instead of `/tmp`, removes the temp-file cleanup step, and adds the per-reviewer state to each synthesis section. Do not touch the Review Consumer Contract structure or the `--reviews` downstream reads.
4. [d:r:i] Record a pre-launch timing estimate and a post-run calibration note on the first real run, matching the rule at [LAUNCH-LEDGER.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/root-support/LAUNCH-LEDGER.md:4).
5. [d:r:i] Pair the slice with a `change-triggered-refresh` entry under `.planning/audits/.../propagation-audit/` naming the consumer chain (planner, plan-checker, revision loop, `--reviews` mode) and the carry delta: run-home + launch-truth + timing + three-state reviewer classification.
6. [d:r:i] Keep the held-later list as a named tail. Do not let the first slice absorb subject-keyed route splitting, retry frameworks, or `.claude` parity widening simply because the helper now exists.
