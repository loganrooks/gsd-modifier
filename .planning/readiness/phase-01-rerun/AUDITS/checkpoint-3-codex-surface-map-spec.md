# Checkpoint 3 Codex Surface Map Spec

## Purpose

Map the current Codex-side harness surfaces that materially affect planning quality, delegation quality, verification quality, continuity, and auditability in this repo.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
4. [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
5. [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)
6. [SESSION-REENTRY-CHECKLIST.md](/home/rookslog/workspace/projects/prix-guesser/.planning/SESSION-REENTRY-CHECKLIST.md)
7. [checkpoint-3.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-3.md)
8. [checkpoint-3-workflow-harness-scope-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-launch-spec.md)

Then inspect the current Codex-side repo surfaces:

- `.codex/config.toml`
- `.codex/hooks.json`
- `.codex/hooks/`
- `.codex/tooling/compact-prompts/`
- `.codex/agents/`
- any repo-local instruction / runtime surfaces that materially constrain Codex behavior in this repo

Also inspect external Codex-side sources where they materially affect the harness map:

- official OpenAI Codex docs for capabilities, controls, and documented limitations
- recent unofficial or user-reported sources when they expose practical behavior not obvious from repo-local files alone

Keep the source-basis explicit:

- distinguish repo-local state from official documented capability
- distinguish official documented capability from unofficial or user-reported behavior
- do not let unofficial reports silently masquerade as stable official guarantees
- prefer still-open or recently active unofficial reports when current applicability matters
- if a relevant unofficial source is closed, old, or plausibly superseded, say so explicitly and explain whether it is still instructive, partly applicable, or mostly historical

## Scope Questions

- what are the real load-bearing Codex-side control surfaces?
- which ones are durable doctrine versus current harness-state?
- where do continuity, compaction, delegation, and runtime constraints actually live?
- what workflows and controls does Codex actually make possible in practice, beyond what this repo happens to be using?
- what limitations or sharp edges matter for this repo even if they are not obvious from `.codex/` alone?
- what navigation or mitigation patterns are externally supported, merely repo-local, or still only anecdotal?
- which unofficial claims still look current versus historical or superseded?
- what looks broad but is mostly descriptive, and what looks narrow but actually steers a lot of downstream behavior?
- what later Checkpoint 4 questions should definitely include Codex-side surfaces?

## Output

Write:

- [checkpoint-3-codex-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-codex-surface-map.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Codex Surface Inventory`
- `Load-Bearing Codex Layers`
- `Broad but Low-Leverage Surfaces`
- `Narrow but High-Leverage Surfaces`
- `Cross-Layer Seams into GSD or governance docs`
- `What Checkpoint 4 must inspect`
- `What can stay lighter`

## Constraints

- do not patch files
- do not assess repo-local GSD internals in depth here except where a real Codex↔GSD seam requires it
- cite concrete files and lines
- cite external sources explicitly when they are carrying real capability, limitation, or workaround claims

## Lane

- classification: `replanning/revision/gap-filling`
- model / reasoning: `gpt-5.4 xhigh`
