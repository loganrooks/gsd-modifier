# PR Docs Intervention Audit Next Steps

Date: 2026-04-20
Status: partially completed next-step note

## Purpose

- [g:r:i] This note records the immediate sequence after the local [PR-DOCS-INTERVENTION-CARRY-AUDIT.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/pr-docs-intervention/PR-DOCS-INTERVENTION-CARRY-AUDIT.md:1), so the plan for challenging, inheriting, and operationalizing that audit does not remain chat-only.

## Sequence

1. **Run the audit as a challenged lane pair**
   - [d:r:i] Launch a narrow external/cross-model audit of the submitted docs PR for intervention carry.
   - [d:r:i] Primary lane: `Opus 4.7 Max`.
   - [d:r:i] Parallel comparison lane: `gpt-5.4 xhigh`.
   - [d:r:i] Keep the packet tight:
     - [PR-DOCS-INTERVENTION-CARRY-AUDIT.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/pr-docs-intervention/PR-DOCS-INTERVENTION-CARRY-AUDIT.md:1)
     - [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:1)
     - [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:1)
     - [upstream-docs-pr-r2/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/README.md:1)
     - [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:1)
   - [d:c+i] Completed:
     - [docs-audit/outputs/01-pr-docs-intervention-carry-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/docs-audit/outputs/01-pr-docs-intervention-carry-opus47-max-r1.md:1)
     - [docs-audit/outputs/01-pr-docs-intervention-carry-gpt54-xhigh-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/docs-audit/outputs/01-pr-docs-intervention-carry-gpt54-xhigh-r1.md:1)

2. **Keep the frame narrow and anti-threshold**
   - [g:r:i] The launch spec and prompt should explicitly forbid `adequate`, `good enough`, `passes`, `ready`, or equivalent threshold framing as the governing question.
   - [d:r:i] The lanes should instead judge:
     - what the PR docs newly expose
     - what they still flatten, hide, or mis-rank
     - where they carry contributor orientation but not intervention planning
     - what should remain stable reference docs
     - what needs a paired intervention layer

3. **Write a comparative inheritance note after the returns**
   - [d:r:i] Record what the two audit lanes converge on, where they differ, and what this workspace accepts from each.
   - [d:r:i] Separate `what the external lanes said` from `what this workspace now inherits`.
   - [d:c+i] Completed:
     - [docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md:1)

4. **Only after that, write the transformation plan**
   - [d:r:i] Decide how the submitted docs should be transformed, extended, or paired so they carry stronger intervention planning.
   - [d:r:i] Keep stable contributor/reference docs distinct from any heavier intervention-oriented layer.
   - [d:c+i] Completed:
     - [PR-DOCS-INTERVENTION-TRANSFORMATION-PLAN.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/pr-docs-intervention/PR-DOCS-INTERVENTION-TRANSFORMATION-PLAN.md:1)

5. **Then route into bounded intervention proposals**
  - [d:r:i] Turn the four highest-rank harness surfaces into bounded proposal artifacts:
    - agent `.toml` authority alignment
    - launch-truth capture
    - manifest/install coherence
    - live-vs-overlay drift visibility
  - [d:c+i] Completed:
    - [intervention-proposals/01-agent-toml-authority-alignment-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/01-agent-toml-authority-alignment-proposal.md:1)
    - [intervention-proposals/02-launch-truth-capture-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/02-launch-truth-capture-proposal.md:1)
    - [intervention-proposals/03-manifest-install-coherence-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/03-manifest-install-coherence-proposal.md:1)
    - [intervention-proposals/04-live-vs-overlay-drift-visibility-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/04-live-vs-overlay-drift-visibility-proposal.md:1)
    - [intervention-proposals/05-batch-routing-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/05-batch-routing-note.md:1)
    - [intervention-proposals/06-first-tranche-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/06-first-tranche-disposition.md:1)

## Things To Keep Explicitly In View

- [d:r:i] The submitted docs PR is not current runtime truth.
- [d:r:i] At the 2026-04-20 docs-audit boundary, the local runtime already sat at published `v1.38.1`; the live runtime has since moved, but that does not reopen the old blind-reinstall question.
- [d:r:i] The frozen PR-docs snapshot is partial by design and is stored as `.md.txt` evidence so it does not pollute markdown-reference verification inside this audit workspace.
- [d:r:i] The goal is not to decide whether the docs `work`. The goal is to decide how they should be inherited and transformed so they carry stronger intervention planning across the harness ecosystem.

## Bottom Line

- [g:r:i] The first bounded companion artifact is now landed:
  - [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:1)
- [g:r:i] The bounded companion layer is now complete:
  - [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:1)
  - [SURFACE-STATUS-AND-DELTA.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/SURFACE-STATUS-AND-DELTA.md:1)
- [g:r:i] The bounded intervention proposal batch now exists under:
  - [intervention-proposals/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/README.md:1)
- [g:r:i] The first-tranche disposition now exists and the first accepted pair is partially landed:
  - [intervention-proposals/06-first-tranche-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/06-first-tranche-disposition.md:1)
- [g:r:i] Immediate next move: checkpoint the landed first pair and then decide whether to start the second tranche with bounded drift visibility.
