# Checkpoint 3 Workflow / Harness Scope Audit Bundle

This bundle defines how Checkpoint 3 should be executed.

## Purpose

Map the real workflow / harness landscape before Checkpoint 4 fixes the deeper excellence-audit envelope.

The output of this checkpoint must be reusable later as:

- a harness-orientation / audit-onboarding surface
- the justified audit envelope for Checkpoint 4
- a filter that distinguishes doc-local governance issues already handled in Checkpoint 2 from deeper machinery-owned follow-through

## Bundle Shape

Run these lanes:

1. `checkpoint-3-codex-surface-map`
2. `checkpoint-3-gsd-surface-map`
3. `checkpoint-3-gsd-workflow-chain-and-artifact-contracts`
4. `checkpoint-3-gsd-agent-doctrine-and-role-contracts`
5. `checkpoint-3-gsd-runtime-config-overlay-truth`
6. `checkpoint-3-gsd-scope-synthesis`
7. `checkpoint-3-scope-synthesis`

The Codex lane must not rely only on repo-local `.codex/` inspection.

It should combine:

- repo-local Codex surfaces
- official Codex documentation for capabilities, controls, and documented limitations
- recent unofficial or user-reported behavior when that behavior affects real operating constraints

and keep the source-basis of those claims explicit.

For unofficial sources:

- prefer still-open or recently active issues, discussions, or reports when current applicability matters
- older, closed, or likely superseded sources may still be included when they teach something real, but their current applicability must be qualified explicitly
- do not treat stale anecdote as if it were a current harness limitation

## Launch Order

- Launch the Codex and GSD mapping lanes in parallel.
- Do not launch the overall synthesis lane until the Codex map exists and the GSD-only synthesis exists.
- If the initial GSD mapping lane fires the split trigger, stay inside Checkpoint 3:
  - launch the required GSD deeper-mapping sublanes
  - run the GSD-only synthesis
  - only then run the overall workflow / harness scope synthesis

## Global Non-Goals

- do not redesign the harness in Checkpoint 3
- do not patch GSD or Codex machinery in Checkpoint 3
- do not confuse skill count with harness importance
- do not optimize for the smallest possible audit envelope if that would hide a load-bearing surface

## Split Trigger

The GSD lane must not bluff completeness.

If the GSD mapper concludes that the repo-local GSD surface is too broad to map honestly in one pass, it must:

- say so explicitly
- identify the sublanes it thinks are required
- explain why the split is load-bearing rather than merely convenient
- stop short of pretending to have completed the full GSD map

## Split Outcome

That trigger has now fired.

The accepted GSD mapping concluded that the repo-local GSD surface is too broad for a single honest mapping pass.

That means the split itself belongs to Checkpoint 3 as deeper mapping work, not to Checkpoint 4.

Checkpoint 3 must therefore complete:

- deeper GSD mapping sublanes
- a GSD-only synthesis
- then the overall Codex+GSD scope synthesis

The deeper GSD mapping must, at minimum, honor the already-earned distinction between:

- phase-critical workflow chain plus artifact contracts
- active agent-role contracts plus shared doctrine
- runtime/config/overlay truth

## Expected Primary Outputs

- [checkpoint-3-codex-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-codex-surface-map.md)
- [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
- [checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md)
- [checkpoint-3-gsd-agent-doctrine-and-role-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md)
- [checkpoint-3-gsd-runtime-config-overlay-truth.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md)
- [checkpoint-3-gsd-scope-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-scope-synthesis.md)
- [checkpoint-3-workflow-harness-scope-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md)

## Model / Reasoning

- mapping lanes: `gpt-5.4 xhigh`
- synthesis lane: `gpt-5.4 xhigh`

## Closure Standard

Checkpoint 3 is not complete when we merely have "some notes about the harness."

It is complete only when:

- the later Checkpoint 4 audit has a defensible unit of analysis
- later auditors can onboard into the harness landscape without relying on session memory
- broad-but-shallow surfaces have been separated from narrow-but-load-bearing ones
- if the split trigger fired, the deeper GSD mapping and GSD-only synthesis were completed before the overall synthesis
