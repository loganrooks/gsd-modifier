# Checkpoint 4 GSD Runtime Config Overlay Truth Excellence Spec

## Purpose

Audit the repo-local GSD runtime, config, overlay, and launch-truth surface against the repo's excellence bar.

This lane should determine whether the underlying machinery reliably realizes the intended workflow and doctrine, or whether config drift, overlay ambiguity, or launch-truth gaps silently degrade quality.

## Why This Lane Exists Now

Checkpoint 3 established that runtime/config/overlay truth is a separate load-bearing surface.

If this layer is weak, the repo can write strong doctrine and still fail to get that doctrine into live behavior.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
4. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
5. [GATES/checkpoint-4.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md)
6. [AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md)
7. [AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md)
8. [AUDITS/checkpoint-3-codex-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-codex-surface-map.md)

Then inspect, at minimum:

- `.planning/config.json`
- `.codex/config.toml`
- `.codex/get-shit-done/`
- `.codex/gsd-local-patches/`
- `scripts/setup-portable-gsd.sh`
- any repo-local install, overlay, launcher, or config-normalization surfaces that materially determine runtime behavior

## Core Questions

- are install source, overlay provenance, supported config, and launch behavior aligned tightly enough to support excellent work?
- where can drift or ambiguity silently degrade reasoning, review, or execution quality?
- is agent launch authority and model/reasoning truth stable enough to trust?
- are config keys and workflow probes cleanly owned, or does the repo still rely on behaviorally real but weakly governed seams?
- what is the strongest justified criticism of the current runtime/config/overlay posture?

## Output

Write:

- [checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Current Strengths`
- `Where Runtime Truth Reliably Supports Quality`
- `Where Runtime Truth Leaves Quality Exposed`
- `Authority / Config / Overlay Risk Assessment`
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

- do not assume documented config or overlay intent equals runtime truth
- do not patch files
- do not treat every drift or mismatch as automatically machinery-owned; explain why protocol or doctrine would be insufficient if that is the conclusion

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
