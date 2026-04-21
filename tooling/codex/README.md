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
- `scan_threshold_language.py`
  - scans docs/specs/prompts/reviews for threshold framing and deficit-oriented pseudo-positive residue
  - use it when auditing older artifacts for `adequate` / `sufficient` / `good enough` / `not lacking` / `no longer missing` style regressions
  - exit code `1` means findings were detected, not that the scanner crashed
- `project_uplift.py`
  - detects repo-local project uplift posture and can write first-slice uplift memory
  - detect mode writes `.planning/UPLIFT-REPORT.md`, `.planning/UPLIFT-MANIFEST.json`, and a `STATE.md` uplift section when `--write` is used
  - progress-note mode is the thin read-only hook for `gsd-progress`; it reads structured uplift memory and current doctrine fingerprints rather than prose
