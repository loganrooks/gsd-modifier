Date: 2026-04-22
Status: completed launch-truth record

# Seed Migration Operator-Facing Pointer Bridge Reread Launch Truth

## Lane Identity

- [g:r:i] Lane: `propagation-audit/05-seed-migration-operator-facing-pointer-bridge-reread`
- [g:r:i] Purpose: bounded reread of the landed operator-facing seed-migration bridge after `89/90`
- [g:r:i] Frozen launch basis commit: `846b6b0`
- [g:r:i] Launch timestamp (UTC): `2026-04-22T02:14:53Z`

## Request Surfaces

- [e:c+i] Packet: [../packets/05-seed-migration-operator-facing-pointer-bridge-reread-packet.md](../packets/05-seed-migration-operator-facing-pointer-bridge-reread-packet.md)
- [e:c+i] Spec: [../specs/05-seed-migration-operator-facing-pointer-bridge-reread-spec.md](../specs/05-seed-migration-operator-facing-pointer-bridge-reread-spec.md)
- [e:c+i] Prompt: [../prompts/05-seed-migration-operator-facing-pointer-bridge-reread-opus47-max-r1-launch-prompt.md](../prompts/05-seed-migration-operator-facing-pointer-bridge-reread-opus47-max-r1-launch-prompt.md)
- [d:r:i] Request surfaces received contextual reread before launch; no heuristic scanner result is treated as a wording gate for this lane.

## Requested Model Settings

- [d:r:i] Requested model string: `opus[1m]`
- [d:r:i] Requested effort: `max`
- [d:r:i] Invocation path:
  - `python3 tooling/codex/run_claude_probe.py --label seed-migration-operator-facing-pointer-bridge-reread-opus47-max-r1 --model 'opus[1m]' --effort max --dangerously-skip-permissions --prompt-file ...`

## Probe Result

- [e:c+i] Label: `seed-migration-operator-facing-pointer-bridge-reread-opus47-max-r1`
- [e:c+i] Exit code: `0`
- [e:c+i] Elapsed seconds: `561.719`
- [e:c+i] Result session id: `1c63179e-fb42-4dda-9e84-509c885a29f0`
- [e:c+i] Total cost usd: `3.1109447500000003`
- [e:c+i] Output artifact: [../outputs/05-seed-migration-operator-facing-pointer-bridge-reread-opus47-max-r1.md](../outputs/05-seed-migration-operator-facing-pointer-bridge-reread-opus47-max-r1.md)

## Probe Artifacts

- [e:c+i] Stream jsonl: `/tmp/seed-migration-operator-facing-pointer-bridge-reread-opus47-max-r1-20260421-221453.58vzxb01.stream.jsonl`
- [e:c+i] Stderr log: `/tmp/seed-migration-operator-facing-pointer-bridge-reread-opus47-max-r1-20260421-221453.vnzh3az1.stderr.log`
- [e:c+i] Debug log: `/tmp/seed-migration-operator-facing-pointer-bridge-reread-opus47-max-r1-20260421-221453.f5m8qb8c.debug.log`

## Consequence

- [d:r:i] This lane now has durable requested-vs-executed launch truth for the Opus reread over the landed operator-facing bridge.
- [d:r:i] The next step is local inheritance into a bridge-hardening batch that raises exercised evidence, command-split clarity, and consumer contract coverage before any wider seed-family inheritance opens.
