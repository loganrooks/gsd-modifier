Date: 2026-04-21
Status: completed launch-truth record

# Broader Network Propagation Field Mapping Launch Truth

## Lane Identity

- [g:r:i] Lane: `propagation-audit/02-broader-network-propagation-field-mapping`
- [g:r:i] Purpose: bounded external widening reread of the broader propagation carrier split after local `08` landed
- [g:r:i] Frozen launch basis commit: `93251d1`
- [g:r:i] Launch timestamp (America/Toronto): `2026-04-21T06:28:56-04:00`

## Request Surfaces

- [e:c+i] Packet: [../packets/02-broader-network-propagation-field-mapping-packet.md](../packets/02-broader-network-propagation-field-mapping-packet.md)
- [e:c+i] Spec: [../specs/02-broader-network-propagation-field-mapping-spec.md](../specs/02-broader-network-propagation-field-mapping-spec.md)
- [e:c+i] Prompt: [../prompts/02-broader-network-propagation-field-mapping-opus47-max-r1-launch-prompt.md](../prompts/02-broader-network-propagation-field-mapping-opus47-max-r1-launch-prompt.md)
- [e:c+i] Request-surface threshold scan returned `No threshold-language residue found` before launch.

## Requested Model Settings

- [d:r:i] Requested model string: `opus[1m]`
- [d:r:i] Requested effort: `max`
- [d:r:i] Invocation path: `python3 tooling/codex/run_claude_probe.py --label broader-network-propagation-field-mapping-opus47-max-r1 --model 'opus[1m]' --effort max --dangerously-skip-permissions --prompt-file ...`

## Probe Result

- [e:c+i] Label: `broader-network-propagation-field-mapping-opus47-max-r1`
- [e:c+i] Exit code: `0`
- [e:c+i] Elapsed seconds: `593.295`
- [e:c+i] Result session id: `aff2e5fa-7d40-4ee7-bc6f-57e1cfe782a1`
- [e:c+i] Total cost usd: `4.87804875`
- [e:c+i] Output artifact: [../outputs/02-broader-network-propagation-field-mapping-opus47-max-r1.md](../outputs/02-broader-network-propagation-field-mapping-opus47-max-r1.md)

## Probe Artifacts

- [e:c+i] Stream jsonl: `/tmp/broader-network-propagation-field-mapping-opus47-max-r1-20260421-062856.3thrs0f4.stream.jsonl`
- [e:c+i] Stderr log: `/tmp/broader-network-propagation-field-mapping-opus47-max-r1-20260421-062856.jcuj3ela.stderr.log`
- [e:c+i] Debug log: `/tmp/broader-network-propagation-field-mapping-opus47-max-r1-20260421-062856.9_dvbpju.debug.log`

## Consequence

- [d:r:i] This lane now has durable requested-vs-executed launch truth for the bounded Opus widening reread over the broader propagation field.
- [d:r:i] The next step is local inheritance of the widened splits, added carrier rows, and bounded strengthening routes into the propagation family state and next sequence.
