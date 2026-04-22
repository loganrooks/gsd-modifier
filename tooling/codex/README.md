# Codex Tooling Notes

This directory holds small local utilities for debugging and operating Codex / Claude CLI behavior in this repo.

## Headless Claude Probe Rule

When using `run_claude_probe.py` or any direct `claude -p` headless run:

- if the prompt is fully inline, normal permissions may be fine
- if the prompt tells Claude to read a repo-local spec, wrapper, or instruction file, prefer:
  - a repo-local path, not a `/tmp` path
  - `--dangerously-skip-permissions`

Why this is written down:

- we hit a failure mode where headless Opus runs looked like mysterious post-request crashes
- startup completed
- auth completed
- `/v1/messages` was dispatched
- but no `assistant` or `result` event ever appeared

That turned out to be a bad test shape for file-mediated prompts, because the run had permission ambiguity around reading the referenced spec.

## Avoid Repeating

- do not treat wrapper-to-file probes as valid controls unless permissions are explicit
- do not use `/tmp` spec files when a repo-local spec file is available
- do not infer "model is broken" before checking whether the model was actually allowed to read the referenced file set

## Preferred Patterns

Inline prompt:

```bash
python3 tooling/codex/run_claude_probe.py \
  --label canary \
  --model sonnet \
  --effort high \
  --prompt 'Reply with exactly OK.'
```

Repo-local wrapper/spec:

```bash
python3 tooling/codex/run_claude_probe.py \
  --label repo-spec \
  --model 'opus[1m]' \
  --effort xhigh \
  --dangerously-skip-permissions \
  --prompt-file .planning/.../wrapper-spec.md
```

## Utilities

- `audit_refmap.py`
  - manages markdown-heavy audit/planning topology work with `map`, `snapshot`, `verify`, `rewrite`, `move`, and `retire`
  - use it instead of hand-editing large reference rewrites across `.planning/`
- `verify_touched_audit_refs.py`
  - runs `audit_refmap.py verify` against touched audit roots by default
  - use `--staged` for staged-only checks and `--all` for a broader audit sweep
- `run_claude_probe.py`
  - runs a headless Claude probe and prints a compact summary: exit code, runtime, event counts, final text, stderr/debug tail
- `extract_stream_text.py`
  - extracts just text-bearing content from `stream-json` logs with `--head`, `--tail`, `--range`, and `--last-message`
- `capture_launch_truth.py`
  - captures requested-vs-effective Codex launch settings from `~/.codex/state_5.sqlite`
  - see also the propagation-family lane records under `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/` when launch-truth becomes part of a wider contract-carry question
- `runtime_visibility.py`
  - reports final repo-local GSD runtime truth for selected high-leverage families without rewriting updater/custom-file manifest semantics
  - use it when live-vs-overlay differences need classification (`intentional materialized carry`, `repo-local config carry`, `selective overlay boundary`, `obsolete live residue`, `unknown live drift`) rather than a blunt mismatch list
  - report output now records whether normalized overlay hashes are checkout-local, distinguishes live-only residue from live-only surfaces that are still explained by manifest, backup-meta, or install-mutation carry, and exposes stable per-entry `subclassification` / top-level `subclassification_summary` fields so selective boundaries do not collapse into one undifferentiated bucket
- `capture_runtime_visibility_snapshot.py`
  - captures a durable selected-lane snapshot around `runtime_visibility.py` with label, timestamp, branch, basis commit, dirty-worktree flag, and the full classified report payload
  - use it when an audit or intervention lane needs a frozen runtime-truth record instead of only ephemeral terminal output
- `manifest_install_coherence.py`
  - compares updater/custom-file boundary truth (`gsd-file-manifest.json`), tracked carried-subset truth (`backup-meta.json`), and a frozen selected-lane runtime snapshot
  - use it for manifest/install coherence passes when the question is whether any real contradiction remains after semantic separation, not whether one file can be forced to stand in for all three surfaces
  - `--strict` is the preferred mode for audit checkpoints because it fails on dirty current state, dirty snapshot boundaries, unknown live drift, or currently evidenced obsolete residue inside the selected runtime scope
  - see also `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/` for the broader producer/consumer/carrier map that decides when coherence belongs in a wider propagation slice
- `scan_threshold_language.py`
  - heuristically scans docs/specs/prompts/reviews for threshold framing, deficit-oriented pseudo-positive residue, and selected static-positive `enough` phrasing
  - use it only when the task is explicitly a framing-residue audit or a doctrine-sensitive reread already warrants it
  - do not use it as a routine `clean batch` gate for ordinary work
  - treat it as intake, not adjudication: findings still need contextual reread and disposition
  - do not rewrite explicit prohibitions, quoted examples, or historical evidence solely to quiet a scanner hit
  - a clean result only means no heuristic hits were found; it does not certify the surface as contextually clean
  - `--ignore-meta-instruction-lines` is useful when scanning doctrine or instruction files that deliberately quote forbidden phrasing
  - exit code `1` means findings were detected, not that the scanner crashed
- `project_uplift.py`
  - detects repo-local project uplift posture and can write first-slice uplift memory
  - detect mode writes `.planning/UPLIFT-REPORT.md`, `.planning/UPLIFT-MANIFEST.json`, and a `STATE.md` uplift section when `--write` is used
  - progress-note mode is the thin read-only hook for the live routed consumers `gsd-progress` and `gsd-resume-work`; it reads structured uplift memory and current doctrine fingerprints rather than prose
  - the current harden slice now carries multi-axis posture (`project_class` plus `secondary_signals`), marker-local section hashes for strengthening carriers, normalized TOML hashes for runtime registry carriers, structured doctrine-sensitive proposal states (`absent` vs `drifted`), phase-boundary signal capture from active `CONTEXT.md`, an explicit observed-basis compatibility block, and bounded seed-corpus posture scanning
  - the compatibility block records the currently observed GSD runtime basis from the canonical repo-local runtime path (`.codex/get-shit-done/VERSION`) plus `.codex/gsd-file-manifest.json` when present, alongside the overlay schema anchor, uplift schema anchor, and the check protocol for later runtime movement without overclaiming a broad version window
  - the seed-corpus block records whether `.planning/seeds/` is absent, current-contract-only, legacy-unversioned, or mixed, and keeps later migration explicit rather than silently absorbing it into detect-only
  - when that observed runtime basis moves after the last durable uplift write, progress-note now routes the live consumers toward `$gsd-uplift-project --write` so compatibility drift reaches the active consumer chain instead of remaining only in stored uplift memory
  - the same write route now activates after seed-corpus posture movement too, so legacy seed shape does not stay buried only in the last stored uplift manifest
  - progress-note now also carries operator-facing seed posture fields for `progress` and `resume-project`, so ordinary re-entry can see active seed corpus posture without reopening milestone-open logic or widening into audit routes
  - the current network-carry chain now includes:
    - workflow consumers: `uplift-project`, `progress`, `resume-project`
    - durable outputs: `.planning/UPLIFT-REPORT.md`, `.planning/UPLIFT-MANIFEST.json`, and the `Project Uplift` section in `.planning/STATE.md`
    - audit lineage: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/`
- `seed_migration_inventory.py`
  - inventories legacy or drifted seed-corpus posture without rewriting seed files
  - detect mode can write `.planning/SEED-MIGRATION-REPORT.md` and `.planning/SEED-MIGRATION-MANIFEST.json` when `--write` is used
  - keeps seed-corpus posture, per-seed vintage, contract-shape gaps, and migration moves explicit as a separate planning packet instead of crowding those semantics into uplift memory alone
  - treat it as the specialist detect-only route once uplift or milestone-open surfaces point at older seed corpora
- `harness_canary.py`
  - emits a bounded machine-checkable report for current runtime/install invariants
  - the first slice checks:
    - canonical runtime version anchor presence
    - overlay manifest validation
    - post-materialization coherence
    - runtime config reasoning default
    - selected high-stakes agent reasoning defaults
    - uplift compatibility-anchor freshness when uplift memory exists
  - use `--strict` when the caller wants a real gate on those bounded invariants rather than a read-only report
- `portable_gsd_contract.py`
  - owns the tracked overlay install contract for repo-local GSD materialization
  - validates [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json), captures fresh-install pristine overwrite copies when upstream no longer leaves them behind, applies overlay files, applies repo-local reasoning defaults, and verifies post-materialization coherence
  - use it when the question is whether overlay ownership, backup-carried overwrite truth, and additive repo-local owners are still aligned
- `ensure_gsd_sdk_runtime.py`
  - verifies the repo-local `gsd-sdk` runtime under `/bin/sh` after upstream local install and repairs the known executable-bit failure when the installed launcher target has a shebang but lost execute bits
  - use it as a narrow recovery surface after `get-shit-done-cc --codex --local` exits through the misleading `gsd-sdk` PATH banner
  - it does not hide real off-PATH cases or broader upstream install failures; it only recovers the bounded local executability case and then proves `gsd-sdk --version` under `/bin/sh`
- `UPLIFT-HELD-LATER.md`
  - named reference for the uplift families the current detect-only slice keeps explicit rather than absorbing
