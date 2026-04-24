# Wave-2 Lane-05 Launch Truth

Status: recorded launch-state artifact  
Date: 2026-04-19

## Frozen Basis

- frozen launch basis commit: `f7cea83`
- frozen launch basis description: Wave-2 lane-05 packet, spec, and Opus prompt drafted; lane-06 had not yet inherited an accepted lane-05 return

## Requested External Lane

- lane: `suppressed-opportunity-and-non-intervention`
- requested model / reasoning: `opus[1m]` / `max`
- launch mode: `python3 tooling/codex/run_claude_probe.py --dangerously-skip-permissions`
- prompt artifact: [../prompts/05-suppressed-opportunity-and-non-intervention-opus47-max-r1-launch-prompt.md](../prompts/05-suppressed-opportunity-and-non-intervention-opus47-max-r1-launch-prompt.md)
- governing spec: [../specs/05-suppressed-opportunity-and-non-intervention-spec.md](../specs/05-suppressed-opportunity-and-non-intervention-spec.md)
- governing packet: [../packets/05-suppressed-opportunity-and-non-intervention-packet.md](../packets/05-suppressed-opportunity-and-non-intervention-packet.md)

## External Return

- output artifact: [../outputs/05-suppressed-opportunity-and-non-intervention-opus47-max-r1.md](../outputs/05-suppressed-opportunity-and-non-intervention-opus47-max-r1.md)
- exit code: `0`
- elapsed seconds: `723.535`
- session id: `6878dc51-d924-4a93-b6f6-f93080b09716`
- total cost usd: `7.09883875`

## Parallel Local Reviewer

- launch mode: `spawn_agent`
- agent id: `019da841-2642-7751-93b6-4456c4ba74c1`
- agent nickname: `Turing`
- effective settings verified against `~/.codex/state_5.sqlite`: `worker / gpt-5.4 / xhigh`
- output artifact: [../outputs/05-suppressed-opportunity-and-non-intervention-gpt54-xhigh-r1.md](../outputs/05-suppressed-opportunity-and-non-intervention-gpt54-xhigh-r1.md)

## Ingest Note

- [d:r:i] The Opus output initially landed with malformed local markdown links using invalid line-range targets and wrong relative depth. Those links were repaired locally before acceptance. After repair, `python3 tooling/codex/verify_touched_audit_refs.py` returned `0` missing local targets for the active audit root.
- [d:r:i] This artifact records launch and ingest truth only. Comparative inheritance lives in [../dispositions/05-wave-2-lane05-comparative-disposition.md](../dispositions/05-wave-2-lane05-comparative-disposition.md).
