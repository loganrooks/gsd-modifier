# Self-Overcoming Audit Launch Truth: Companion-Layer Proposal

Status: completed and dispositioned  
Date: 2026-04-21

## Frozen Basis

- frozen launch basis commit: `e466bea`
- packet: [../packets/01-companion-layer-proposal-packet.md](../packets/01-companion-layer-proposal-packet.md)
- spec: [../specs/01-companion-layer-proposal-cross-vendor-spec.md](../specs/01-companion-layer-proposal-cross-vendor-spec.md)
- Opus prompt: [../prompts/01-companion-layer-proposal-opus47-max-r1-launch-prompt.md](../prompts/01-companion-layer-proposal-opus47-max-r1-launch-prompt.md)
- GPT brief: [../prompts/01-companion-layer-proposal-gpt54-xhigh-r1-brief.md](../prompts/01-companion-layer-proposal-gpt54-xhigh-r1-brief.md)

## Requested Outputs

- Opus output:
  - [../outputs/01-companion-layer-proposal-opus47-max-r1.md](../outputs/01-companion-layer-proposal-opus47-max-r1.md)
- GPT output:
  - [../outputs/01-companion-layer-proposal-gpt54-xhigh-r1.md](../outputs/01-companion-layer-proposal-gpt54-xhigh-r1.md)
- comparative disposition:
  - [../dispositions/01-companion-layer-proposal-comparative-disposition.md](../dispositions/01-companion-layer-proposal-comparative-disposition.md)

## Request-Surface Language Check

- `python3 tooling/codex/scan_threshold_language.py` was run against:
  - [../README.md](../README.md)
  - [../packets/01-companion-layer-proposal-packet.md](../packets/01-companion-layer-proposal-packet.md)
  - [../specs/01-companion-layer-proposal-cross-vendor-spec.md](../specs/01-companion-layer-proposal-cross-vendor-spec.md)
  - [../prompts/01-companion-layer-proposal-opus47-max-r1-launch-prompt.md](../prompts/01-companion-layer-proposal-opus47-max-r1-launch-prompt.md)
  - [../prompts/01-companion-layer-proposal-gpt54-xhigh-r1-brief.md](../prompts/01-companion-layer-proposal-gpt54-xhigh-r1-brief.md)
- scanner result: `No threshold-language residue found.`

## Requested Launch Modes

- Opus:
  - operator-facing model / reasoning: `Opus 4.7 Max` / `max`
  - effective Claude model string: `opus[1m]`
  - mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`
  - live command / process evidence:
    - `python3 tooling/codex/run_claude_probe.py --label companion-layer-proposal-opus47-max-r1 --model opus[1m] --effort max --prompt-file ... --dangerously-skip-permissions`
    - child process observed as `claude -p --dangerously-skip-permissions --model opus[1m] --effort max ...`
- GPT:
  - model / reasoning: `gpt-5.4` / `xhigh`
  - mode: `spawn_agent`
  - agent id: `019dae40-516b-7ff2-a973-4831bdae1376`
  - requested-vs-effective launch truth preserved at `/tmp/self_overcoming_local_launch_truth.md`
  - effective row capture:
    - `thread_id`: `019dae40-516b-7ff2-a973-4831bdae1376`
    - `created_at`: `2026-04-21T00:15:44-04:00`
    - `model`: `gpt-5.4`
    - `reasoning_effort`: `xhigh`
    - `approval_mode`: `never`
    - `sandbox_policy`: `danger-full-access`

## Return Summary

- Opus:
  - exit code: `0`
  - elapsed seconds: `483.379`
  - session id: `1de565fd-35ec-4cf0-866f-3a722b1dd3d5`
  - total cost usd: `3.34107775`
  - stdout/stderr/debug artifacts:
    - `/tmp/companion-layer-proposal-opus47-max-r1-20260421-001602.riyq_k8y.stream.jsonl`
    - `/tmp/companion-layer-proposal-opus47-max-r1-20260421-001602.1fnatjs_.stderr.log`
    - `/tmp/companion-layer-proposal-opus47-max-r1-20260421-001602.ol59m29m.debug.log`
- GPT:
  - agent completed and wrote the requested output artifact
  - requested-vs-effective capture at `/tmp/self_overcoming_local_launch_truth.md` shows exact `gpt-5.4 / xhigh` carry on the recorded thread row

## Current Consequence

- [g:r:i] This lane pair is complete. The current move is to inherit the pair through [../dispositions/01-companion-layer-proposal-comparative-disposition.md](../dispositions/01-companion-layer-proposal-comparative-disposition.md), not to reopen the request/spec/prompt set.
