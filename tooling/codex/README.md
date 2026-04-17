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

- `run_claude_probe.py`
  - runs a headless Claude probe and prints a compact summary: exit code, runtime, event counts, final text, stderr/debug tail
- `extract_stream_text.py`
  - extracts just text-bearing content from `stream-json` logs with `--head`, `--tail`, `--range`, and `--last-message`
- `capture_launch_truth.py`
  - captures requested-vs-effective Codex launch settings from `~/.codex/state_5.sqlite`
