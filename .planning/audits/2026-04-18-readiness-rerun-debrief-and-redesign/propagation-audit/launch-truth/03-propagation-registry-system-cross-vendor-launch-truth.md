Date: 2026-04-21
Status: completed launch-truth record

# Propagation Registry System Cross-Vendor Launch Truth

## Frozen Basis

- [g:r:i] Frozen launch basis commit: `3ee6d58`
- [e:c+i] Packet: [../packets/03-propagation-registry-system-cross-vendor-packet.md](../packets/03-propagation-registry-system-cross-vendor-packet.md)
- [e:c+i] Spec: [../specs/03-propagation-registry-system-cross-vendor-spec.md](../specs/03-propagation-registry-system-cross-vendor-spec.md)
- [e:c+i] Opus prompt: [../prompts/03-propagation-registry-system-opus47-max-r1-launch-prompt.md](../prompts/03-propagation-registry-system-opus47-max-r1-launch-prompt.md)
- [e:c+i] GPT brief: [../prompts/03-propagation-registry-system-gpt54-xhigh-r1-brief.md](../prompts/03-propagation-registry-system-gpt54-xhigh-r1-brief.md)

## Requested Outputs

- [e:c+i] Opus output:
  - [../outputs/03-propagation-registry-system-opus47-max-r1.md](../outputs/03-propagation-registry-system-opus47-max-r1.md)
- [e:c+i] GPT output:
  - [../outputs/03-propagation-registry-system-gpt54-xhigh-r1.md](../outputs/03-propagation-registry-system-gpt54-xhigh-r1.md)
- [e:c+i] Local inheritance:
  - [../dispositions/03-propagation-registry-system-cross-vendor-inheritance.md](../dispositions/03-propagation-registry-system-cross-vendor-inheritance.md)

## Request-Surface Language Check

- [e:c+i] `python3 tooling/codex/scan_threshold_language.py --ignore-meta-instruction-lines ...` was run against:
  - [../README.md](../README.md)
  - [../packets/03-propagation-registry-system-cross-vendor-packet.md](../packets/03-propagation-registry-system-cross-vendor-packet.md)
  - [../specs/03-propagation-registry-system-cross-vendor-spec.md](../specs/03-propagation-registry-system-cross-vendor-spec.md)
  - [../prompts/03-propagation-registry-system-opus47-max-r1-launch-prompt.md](../prompts/03-propagation-registry-system-opus47-max-r1-launch-prompt.md)
  - [../prompts/03-propagation-registry-system-gpt54-xhigh-r1-brief.md](../prompts/03-propagation-registry-system-gpt54-xhigh-r1-brief.md)
- [e:c+i] Scanner result: `No scanner findings. Contextual reread still required.`

## Requested Launch Modes

- [d:r:i] Opus:
  - operator-facing model / reasoning: `Opus 4.7 Max` / `max`
  - effective Claude model string: `opus[1m]`
  - mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`
  - live command / process evidence:
    - `python3 tooling/codex/run_claude_probe.py --label propagation-registry-system-opus47-max-r1 --model 'opus[1m]' --effort max --dangerously-skip-permissions --prompt-file ...`
- [d:r:i] GPT:
  - requested model / reasoning: `gpt-5.4` / `xhigh`
  - mode: `spawn_agent`
  - agent id: `019db161-e0d2-7282-9a7f-a91e144d211f`
  - agent nickname: `Boyle`
  - requested-vs-effective launch truth preserved at `/tmp/propagation_registry_system_local_launch_truth.md`
  - effective row capture:
    - `thread_id`: `019db161-e0d2-7282-9a7f-a91e144d211f`
    - `created_at`: `2026-04-21T14:51:15-04:00`
    - `model`: `gpt-5.4`
    - `reasoning_effort`: `xhigh`
    - `approval_mode`: `never`
    - `sandbox_policy`: `danger-full-access`
    - `agent_role`: `default`

## Return Summary

- [e:c+i] Opus:
  - exit code: `0`
  - elapsed seconds: `462.964`
  - session id: `922519cc-c1df-4144-8496-5f894e6704eb`
  - total cost usd: `2.275288`
  - stdout/stderr/debug artifacts:
    - `/tmp/propagation-registry-system-opus47-max-r1-20260421-145113.v4ufepvq.stream.jsonl`
    - `/tmp/propagation-registry-system-opus47-max-r1-20260421-145113.0mzrph5t.stderr.log`
    - `/tmp/propagation-registry-system-opus47-max-r1-20260421-145113.sxnrdl49.debug.log`
- [e:c+i] GPT:
  - local reviewer completed and wrote the requested output artifact
  - requested-vs-effective capture at `/tmp/propagation_registry_system_local_launch_truth.md` preserves the exact `gpt-5.4 / xhigh / never / danger-full-access` row
  - the sqlite row stores `agent_role: default`, so the earlier `worker` phrasing remains operator intent rather than effective proof

## Current Consequence

- [d:r:i] This lane pair is complete.
- [d:r:i] The next move is local inheritance of the layered/federated registry direction with Opus carrying the widening lead and GPT serving as a narrower corroborating split on seed ownership, evidence typing, and explicit operator-control layers.
