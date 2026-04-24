Date: 2026-04-22
Status: completed launch-truth record

# Seed Migration Pointer Bridge Harden Reread Launch Truth

## Lane Identity

- [g:r:i] Lane: `propagation-audit/06-seed-migration-pointer-bridge-harden-reread`
- [g:r:i] Purpose: bounded reread of the hardened operator-facing seed-migration bridge after `91/92/38`
- [g:r:i] Frozen launch basis commit: `61fd707`

## Request Surfaces

- [e:c+i] Packet: [../packets/06-seed-migration-pointer-bridge-harden-reread-packet.md](../packets/06-seed-migration-pointer-bridge-harden-reread-packet.md)
- [e:c+i] Spec: [../specs/06-seed-migration-pointer-bridge-harden-reread-spec.md](../specs/06-seed-migration-pointer-bridge-harden-reread-spec.md)
- [e:c+i] Prompt: [../prompts/06-seed-migration-pointer-bridge-harden-reread-opus47-max-r1-launch-prompt.md](../prompts/06-seed-migration-pointer-bridge-harden-reread-opus47-max-r1-launch-prompt.md)
- [d:r:i] Request surfaces received contextual reread before launch; no heuristic scanner result was used as a wording gate for this lane.

## Requested Model Settings

- [d:r:i] Requested model string: `opus[1m]`
- [d:r:i] Requested effort: `max`
- [d:r:i] Invocation path:
  - `python3 tooling/codex/run_claude_probe.py --label seed-migration-pointer-bridge-harden-reread-opus47-max-r1 --model 'opus[1m]' --effort max --dangerously-skip-permissions --prompt-file ...`

## Attempt History

- [e:c+i] Attempt `1` stalled mid tool-input stream and was cut rather than left hanging:
  - session id: `f04ad45b-cc78-424a-b824-237cb2344050`
  - stream artifact: `/tmp/seed-migration-pointer-bridge-harden-reread-opus47-max-r1-20260421-224415.7v9foalh.stream.jsonl`
  - stderr artifact: `/tmp/seed-migration-pointer-bridge-harden-reread-opus47-max-r1-20260421-224415.jdve7pnq.stderr.log`
  - debug artifact: `/tmp/seed-migration-pointer-bridge-harden-reread-opus47-max-r1-20260421-224415.fa6s1h6a.debug.log`
  - local consequence: relaunch from the same clean basis and same request surfaces rather than inherit a hung write path
- [e:c+i] Attempt `2` completed successfully and is the effective lane return:
  - session id: `092ba18f-ae3b-4ec1-83fa-873ffa8eebe8`
  - elapsed seconds: `389.084`
  - total cost usd: `2.53485525`
  - stop reason: `end_turn`
  - stream artifact: `/tmp/seed-migration-pointer-bridge-harden-reread-opus47-max-r1-20260421-225353.e6vmlhgx.stream.jsonl`
  - stderr artifact: `/tmp/seed-migration-pointer-bridge-harden-reread-opus47-max-r1-20260421-225353.neb8a3br.stderr.log`
  - debug artifact: `/tmp/seed-migration-pointer-bridge-harden-reread-opus47-max-r1-20260421-225353.kfsoo4l4.debug.log`

## Output Artifact

- [e:c+i] Opus output: [../outputs/06-seed-migration-pointer-bridge-harden-reread-opus47-max-r1.md](../outputs/06-seed-migration-pointer-bridge-harden-reread-opus47-max-r1.md)

## Current Consequence

- [d:r:i] This bounded Opus reread is now complete.
- [d:r:i] The next move is local inheritance of the return: preserve the hardened bridge where it already carries more clearly, keep narrower bridge-footprint sharpenings explicit, and shift the adjacent family route toward the `93` note rather than forcing another seed-family harden pass without live corpus.
