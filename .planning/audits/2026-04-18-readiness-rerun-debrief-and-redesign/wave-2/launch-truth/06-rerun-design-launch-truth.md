# Wave-2 Lane-06 Launch Truth

Status: recorded launch-state artifact  
Date: 2026-04-19

## Frozen Basis

- frozen launch basis commit: `24b54d3`
- frozen launch basis description: lane-06 prompt frozen; accepted Wave-2 lane-05 comparative disposition already inserted into the lane-06 packet; bounded runtime-authority drift probe brief added as a parallel follow-up

## Requested External Lane

- lane: `rerun-design`
- requested model / reasoning: `opus[1m]` / `max`
- launch mode: `python3 tooling/codex/run_claude_probe.py --dangerously-skip-permissions`
- prompt artifact: [../prompts/06-rerun-design-opus47-max-r1-launch-prompt.md](../prompts/06-rerun-design-opus47-max-r1-launch-prompt.md)
- governing spec: [../specs/06-rerun-design-spec.md](../specs/06-rerun-design-spec.md)
- governing packet: [../packets/06-rerun-design-packet.md](../packets/06-rerun-design-packet.md)

## External Return

- output artifact: [../outputs/06-rerun-design-opus47-max-r1.md](../outputs/06-rerun-design-opus47-max-r1.md)
- exit code: `0`
- elapsed seconds: `1073.232`
- session id: `077a1333-dd5c-41fb-98d0-86b70a3e163b`
- total cost usd: `8.137341`
- stream artifact: `/tmp/wave2-lane06-rerun-design-opus47-max-r1-20260419-214409.fenirdup.stream.jsonl`
- stderr artifact: `/tmp/wave2-lane06-rerun-design-opus47-max-r1-20260419-214409.q0m21om2.stderr.log`
- debug artifact: `/tmp/wave2-lane06-rerun-design-opus47-max-r1-20260419-214409.q3lifo6o.debug.log`

## Parallel Local Reviewers

- rerun-design counterpart:
  - launch mode: `spawn_agent`
  - agent id: `019da88f-35d7-77b0-b32e-8e1c1bae1d29`
  - agent nickname: `Lovelace`
  - effective settings verified against `~/.codex/state_5.sqlite`: `worker / gpt-5.4 / xhigh`
  - output artifact: [../outputs/06-rerun-design-gpt54-xhigh-r1.md](../outputs/06-rerun-design-gpt54-xhigh-r1.md)
- bounded parallel follow-up:
  - launch mode: `spawn_agent`
  - agent id: `019da88f-3646-7040-bc45-b46de25dd060`
  - agent nickname: `Meitner`
  - effective settings verified against `~/.codex/state_5.sqlite`: `worker / gpt-5.4 / xhigh`
  - brief artifact: [../prompts/05a-runtime-authority-materialization-drift-probe-gpt54-xhigh-brief.md](../prompts/05a-runtime-authority-materialization-drift-probe-gpt54-xhigh-brief.md)
  - output artifact: [../outputs/05a-runtime-authority-materialization-drift-probe-gpt54-xhigh-r1.md](../outputs/05a-runtime-authority-materialization-drift-probe-gpt54-xhigh-r1.md)

## Ingest Note

- [d:r:i] After all three returned artifacts landed, `python3 tooling/codex/verify_touched_audit_refs.py` passed with `0` missing local targets for the active audit root.
- [d:r:i] This artifact records launch and ingest truth only. Comparative inheritance lives in [../dispositions/06-wave-2-lane06-comparative-disposition.md](../dispositions/06-wave-2-lane06-comparative-disposition.md).
