Date: 2026-04-20
Launch scaffold basis: `3856c9b`
Packet content basis: `3856c9b`
Status: completed pair; locally inherited

# Long-Horizon Field Mapping Launch Truth

## Scope

- [g:r:i] This note captures requested versus effective launch truth for the first bounded cross-vendor lane focused on long-horizon carry, horizon-tension management, optionality preservation, and harness self-overcoming pressure.
- [d:r:i] The target is the field mapped by [intervention-proposals/29-long-horizon-carry-gap-register.md](../../intervention-proposals/29-long-horizon-carry-gap-register.md), not the full readiness-rerun workspace in undifferentiated form.

## Requested Launches

### External lane

- model: `Opus 4.7 Max`
- effective Claude model string: `opus[1m]`
- launcher: `python3 tooling/codex/run_claude_probe.py`
- label: `long-horizon-field-mapping-opus47-max-r1`
- prompt:
  - [01-long-horizon-field-mapping-opus47-max-r1-launch-prompt.md](../prompts/01-long-horizon-field-mapping-opus47-max-r1-launch-prompt.md)
- target output:
  - [01-long-horizon-field-mapping-opus47-max-r1.md](../outputs/01-long-horizon-field-mapping-opus47-max-r1.md)
- requested status: `launched`
- effective completion status: `completed`
- completion summary:
  - exit code: `0`
  - elapsed seconds: `908.288`
  - Claude session id: `cc3be3b3-11bd-41be-ac84-e681e25e7ec6`
  - total cost usd: `6.0682`
  - output artifact:
    - [01-long-horizon-field-mapping-opus47-max-r1.md](../outputs/01-long-horizon-field-mapping-opus47-max-r1.md)

### Local parallel lane

- task classification: `replanning/revision/gap-filling`
- requested mapping: `worker -> gpt-5.4 -> xhigh`
- reviewer agent id: `019dadec-9b5e-7bc3-8d95-f24f3e45ac2b`
- reviewer nickname: `Hypatia`
- brief:
  - [01-long-horizon-field-mapping-gpt54-xhigh-r1-brief.md](../prompts/01-long-horizon-field-mapping-gpt54-xhigh-r1-brief.md)
- target output:
  - [01-long-horizon-field-mapping-gpt54-xhigh-r1.md](../outputs/01-long-horizon-field-mapping-gpt54-xhigh-r1.md)
- effective completion status: `completed`
- output artifact:
  - [01-long-horizon-field-mapping-gpt54-xhigh-r1.md](../outputs/01-long-horizon-field-mapping-gpt54-xhigh-r1.md)

## Effective Local Verification

- [e:c+i] `~/.codex/state_5.sqlite` records the launched reviewer thread as:
  - id: `019dadec-9b5e-7bc3-8d95-f24f3e45ac2b`
  - role: `worker`
  - model: `gpt-5.4`
  - reasoning: `xhigh`
  - cwd: `/home/rookslog/workspace/projects/prix-guesser`
- [d:r:i] Current consequence: the local parallel lane launched with the requested effective settings and did not need restart.

## External Model Confirmation

- [e:c+i] The live process table during execution showed:
  - `python3 tooling/codex/run_claude_probe.py --label long-horizon-field-mapping-opus47-max-r1 --model opus[1m] --effort max ...`
  - child process:
    - `claude -p --dangerously-skip-permissions --model opus[1m] --effort max ...`
- [d:r:i] Current consequence: the external lane was not merely intended for `Opus 4.7 Max`; it was actually launched under the `opus[1m]` model string as requested.

## Pending Completion Capture

- [d:r:i] No launch mismatch or restart event occurred.
- [d:r:i] The lane scaffold and packet content share the same checkpoint basis `3856c9b`, so no later packet-drift distinction needs to be carried for this lane.
