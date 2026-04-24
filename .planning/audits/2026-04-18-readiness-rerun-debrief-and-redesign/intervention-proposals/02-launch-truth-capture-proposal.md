Date: 2026-04-20
Status: draft bounded proposal

# Launch-Truth Capture Proposal

## Purpose

- [g:r:i] This proposal defines a bounded follow-through candidate for the other major Codex-side gap named by Checkpoint 4: launch truth exists, but it is still carried too much by operator vigilance and chat memory instead of durable, reviewable artifacts.

## Why This Proposal Exists

- [e:c+i] Checkpoint 4 found that effective launch settings already have a real truth surface in `state_5.sqlite`, but the repo currently reaches that truth through a vigilance-heavy protocol rather than through durable capture at spawn/review boundaries. Sources: [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:62), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:65), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:72), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:80), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:100).
- [e:c+i] The intervention onboarding map and the new goal-routing index both treat launch-truth capture as a first-rank intervention surface rather than a minor operator hygiene issue. Sources: [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:50), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:52), [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:26), [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:60).

## Bounded Scope

- [d:r:i] Limit the first capture protocol to high-stakes spawned work:
  - planning
  - execution
  - verification
  - external audit/review lanes whose outputs may steer doctrine or harness intervention
- [d:r:i] Do not try to capture every trivial spawned helper or every casual local experiment in the first pass.

## Proposed Move

### 1. Require A Launch-Truth Record At Spawn Boundary

- [d:r:i] For each in-scope launch, create or update a durable launch-truth note at the moment the worker is started.
- [d:r:i] The note should record:
  - requested agent / label
  - requested model and requested reasoning level
  - requested sandbox / approval posture if materially relevant
  - when the launch happened
  - where the operator intends to verify effective settings

### 2. Require An Effective-Settings Check At Review Boundary

- [d:r:i] Before accepting the returned work, add the effective-settings check result to the same note.
- [d:r:i] The check should state:
  - what was actually observed from the runtime truth surface
  - whether requested and effective settings matched
  - what disposition was taken if they diverged

### 3. Keep The Artifact Lightweight

- [d:r:i] Use one compact markdown note per lane / launch family, not a heavy database or daemon.
- [d:r:i] The proposal is for durable reviewability, not for replacing judgment with invisible automation.

## Candidate Minimal Schema

```md
Status: launched | verified | mismatch | superseded

- requested agent:
- requested model:
- requested reasoning:
- requested sandbox/approval:
- launch timestamp:
- effective check source:
- effective model:
- effective reasoning:
- effective sandbox/approval:
- mismatch:
- disposition:
```

## Explicit Non-Goals

- [d:r:i] Do not attempt a heavy auto-capture system first.
- [d:r:i] Do not pretend that launch-truth capture removes the need for human review.
- [d:r:i] Do not widen this to every low-stakes spawned action before the high-stakes protocol proves useful.

## Why This Bounded Shape Is Stronger

- [d:r:i] It turns an existing truth surface into a durable review boundary without claiming to solve every runtime-observability problem.
- [d:r:i] It preserves human judgment while reducing dependence on memory and chat archaeology.
- [d:r:i] It directly supports later scrutiny when a strong reviewer asks not just “what was requested?” but “what actually launched?”

## Success Signals

- [d:r:i] Later reviewers can inspect high-stakes launch records without reconstructing settings from conversation fragments.
- [d:r:i] Mismatch handling becomes visible and auditable instead of implicit.
- [d:r:i] The protocol is light enough that people actually keep using it rather than bypassing it.

## Ceremony Risk Check

- [d:r:i] This proposal fails if it produces one more formal note that no one consults at review time.
- [d:r:i] It also fails if it grows into a heavy pseudo-automation layer before the lightweight capture protocol proves it changes treatment or scrutiny quality.

## Next Disposition Question

- [g:r:i] The next decision on this proposal should be whether to accept a lightweight launch-truth note protocol now, revise the schema/scope, or hold it behind some narrower precondition.
