Date: 2026-04-21
Status: completed launch-truth record

# Propagation Chain Reread Launch Truth

## Lane Identity

- [g:r:i] Lane: `propagation-audit/01-propagation-chain-reread`
- [g:r:i] Purpose: bounded external reread of the current propagation family after the landed two-consumer uplift baseline
- [g:r:i] Frozen launch basis commit: `b0e48c4`
- [g:r:i] Launch timestamp (America/Toronto): `2026-04-21T05:58:47-04:00`

## Request Surfaces

- [e:c+i] Packet: [../packets/01-propagation-chain-reread-packet.md](../packets/01-propagation-chain-reread-packet.md)
- [e:c+i] Spec: [../specs/01-propagation-chain-reread-spec.md](../specs/01-propagation-chain-reread-spec.md)
- [e:c+i] Prompt: [../prompts/01-propagation-chain-reread-opus47-max-r1-launch-prompt.md](../prompts/01-propagation-chain-reread-opus47-max-r1-launch-prompt.md)
- [e:c+i] Request-surface threshold scan returned `No threshold-language residue found` before launch.

## Requested Model Settings

- [d:r:i] Requested model string: `opus[1m]`
- [d:r:i] Requested effort: `max`
- [d:r:i] Invocation path: `python3 tooling/codex/run_claude_probe.py --label propagation-chain-reread-opus47-max-r1 --model 'opus[1m]' --effort max --prompt-file ... --dangerously-skip-permissions`

## Probe Result

- [e:c+i] Label: `propagation-chain-reread-opus47-max-r1`
- [e:c+i] Exit code: `0`
- [e:c+i] Elapsed seconds: `423.587`
- [e:c+i] Result session id: `d585e844-a299-4482-9b39-376f98438dab`
- [e:c+i] Total cost usd: `3.7735877499999986`
- [e:c+i] Output artifact: [../outputs/01-propagation-chain-reread-opus47-max-r1.md](../outputs/01-propagation-chain-reread-opus47-max-r1.md)

## Probe Artifacts

- [e:c+i] Stream jsonl: `/tmp/propagation-chain-reread-opus47-max-r1-20260421-055847.vxtnjart.stream.jsonl`
- [e:c+i] Stderr log: `/tmp/propagation-chain-reread-opus47-max-r1-20260421-055847.9umc0x8w.stderr.log`
- [e:c+i] Debug log: `/tmp/propagation-chain-reread-opus47-max-r1-20260421-055847.ozj5iguo.debug.log`

## Consequence

- [d:r:i] This lane now has durable requested-vs-executed launch truth for the bounded Opus reread of the propagation family.
- [d:r:i] The next step is local inheritance of the returned routes into the propagation family state and next sequence.
