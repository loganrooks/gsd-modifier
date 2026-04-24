Date: 2026-04-21
Status: completed launch-truth record

# Revised Entry Surface / Project Uplift Bundle Reread Launch Truth

## Lane Identity

- [g:r:i] Lane: `entry-uplift-audit/03-revised-entry-surface-project-uplift-bundle-reread`
- [g:r:i] Purpose: bounded reread of the revised `37 + 38 + 39` bundle after the Opus-led local revision pass
- [g:r:i] Frozen launch basis commit: `ad26b7c`
- [g:r:i] Launch timestamp (UTC): `2026-04-21T08:08:06Z`

## Request Surfaces

- [e:c+i] Packet: [../packets/03-revised-entry-surface-project-uplift-bundle-reread-packet.md](../packets/03-revised-entry-surface-project-uplift-bundle-reread-packet.md)
- [e:c+i] Spec: [../specs/03-revised-entry-surface-project-uplift-bundle-reread-spec.md](../specs/03-revised-entry-surface-project-uplift-bundle-reread-spec.md)
- [e:c+i] Prompt: [../prompts/03-revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1-launch-prompt.md](../prompts/03-revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1-launch-prompt.md)
- [e:c+i] Request-surface threshold scan returned `No threshold-language residue found` before launch.

## Requested Model Settings

- [d:r:i] Requested model string: `opus[1m]`
- [d:r:i] Requested effort: `max`
- [d:r:i] Invocation path: `python3 tooling/codex/run_claude_probe.py --label revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1 --model 'opus[1m]' --effort max --prompt-file ... --dangerously-skip-permissions`

## Probe Result

- [e:c+i] Label: `revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1`
- [e:c+i] Exit code: `0`
- [e:c+i] Elapsed seconds: `530.465`
- [e:c+i] Result session id: `f41b20b1-df48-4181-be62-b77f0b66d217`
- [e:c+i] Total cost usd: `2.12706125`
- [e:c+i] Output artifact: [../outputs/03-revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1.md](../outputs/03-revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1.md)

## Probe Artifacts

- [e:c+i] Stream jsonl: `/tmp/revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1-20260421-040807.qvrmxewq.stream.jsonl`
- [e:c+i] Stderr log: `/tmp/revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1-20260421-040807.7x6ru6ng.stderr.log`
- [e:c+i] Debug log: `/tmp/revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1-20260421-040807.p8dr6mut.debug.log`

## Consequence

- [d:r:i] This lane now has durable requested-vs-executed launch truth for the single-model Opus reread.
- [d:r:i] The next step is local inheritance of the returned review into the entry-uplift family state and next sequence.
