# Checkpoint 4 Codex Load-Bearing Surfaces And Seams Spec

## Purpose

Audit the active Codex-side control surfaces and Codex-to-repo seams against the repo's excellence standard.

This is not a generic Codex product review.

It is a repo-specific judgment about whether Codex, as actually used here, helps produce excellent work or leaves critical quality discipline to docs and human vigilance alone.

## Why This Lane Exists Now

Checkpoint 3 already established that Codex deserves its own lane rather than being flattened into the GSD side.

This lane owns:

- instruction/config precedence
- launch-setting truth
- authoritative agent path
- hook coverage
- compaction/resume continuity
- Codex-to-repo and Codex-to-GSD seams

It should also use official and recent unofficial Codex sources where capability, control, or limitation claims materially affect the audit, with explicit source-basis and qualification.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
4. [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
5. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
6. [GATES/checkpoint-4.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md)
7. [AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md)
8. [AUDITS/checkpoint-3-codex-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-codex-surface-map.md)
9. [02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md)

Then inspect, at minimum:

- `.codex/config.toml`
- `.codex/hooks/`
- `.codex/tooling/compact-prompts/`
- `.codex/agents/`
- relevant official Codex documentation for instruction loading, config, subagents, hooks, and compaction

Required external evidence:

- relevant official Codex documentation for instruction loading, config, subagents, hooks, and compaction

Conditional supporting inputs, when present and still current:

- [03-compaction-context-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/03-compaction-context-response.md)
- [SESSION-REENTRY-CHECKLIST.md](/home/rookslog/workspace/projects/prix-guesser/.planning/SESSION-REENTRY-CHECKLIST.md)
- recent still-relevant unofficial issue/discussion evidence where current limitations or operating advice materially affect this repo

## Core Questions

- does the repo's Codex-side harness preserve the right doctrine and continuity under pressure, or does it mostly rely on fragile operator memory?
- are launch settings, instruction authority, and model policy reliably real, or merely declared?
- is the compaction/resume posture strong enough for long-running planning/audit work?
- do hooks and session re-entry discipline catch enough to materially improve quality, or only provide thin reminders?
- are there Codex-side limitations or gaps that the repo should treat as stable operating constraints?
- where is the strongest justified criticism of the current Codex-side posture?

## Output

Write:

- [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Current Strengths`
- `Load-Bearing Codex Surfaces`
- `Pass/Fail-Thin Or Opportunity-Suppressing Surfaces`
- `Compaction, Resume, And Continuity Assessment`
- `Authority / Launch / Model-Truth Assessment`
- `Strongest Justified Criticisms`
- `Strategic Opportunities`
- `Ownership Assessment`
- `Conditional Follow-Through Candidates`

`Ownership Assessment` must classify each material finding as:

- `doc-level doctrine`
- `workflow-protocol`
- `machinery-owned`
- or `split/ambiguous`

## Constraints

- keep unofficial-source applicability qualified
- for unofficial evidence, say why it is still relevant to the current Codex version or operating posture, or qualify it as suggestive rather than settled
- prefer still-open or recently active issues when present-state behavior matters; if using older or closed reports, explain why their lessons still apply
- do not treat stale user reports as present truth without qualification
- do not confuse product limitation with repo misconfiguration
- do not patch files
- do not jump straight to Checkpoint 5 ownership claims without explaining why docs or protocol are insufficient

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
