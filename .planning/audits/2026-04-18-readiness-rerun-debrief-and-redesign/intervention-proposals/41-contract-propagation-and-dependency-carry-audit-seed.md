Date: 2026-04-21
Status: active seed artifact

# Contract Propagation And Dependency-Carry Audit Seed

## Purpose

- [g:r:i] This artifact records a later audit family that the workspace has now clearly earned: one explicit audit should ask whether contract changes propagate strongly enough across the GSD network rather than assuming local edits plus a few partial tools are enough.
- [g:r:i] The target is broader than reference rewrites and broader than runtime/install coherence. The target is the whole producer/consumer network around workflows, skills, scripts, registries, outputs, manifests, wrappers, and governing-doc carriers.

## Why This Family Is Opened

- [e:c+i] The repo now has several partial propagation and visibility tools:
  - `audit_refmap.py`
  - `runtime_visibility.py`
  - `manifest_install_coherence.py`
  - the uplift report / state / manifest chain
  Sources: [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:38), [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:52), [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:63), [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:84).
- [d:r:i] Those surfaces are useful, but they do not yet add up to one explicit network-carry audit. They show pieces of the system:
  - reference rewrites
  - live-vs-overlay classification
  - selected manifest/install coherence
  - project-uplift posture
- [d:r:i] What is still not explicit enough is the broader question:
  - when a contract changes, which producers, consumers, intermediates, and outputs should move with it?
  - which surfaces are supposed to inherit directly?
  - which surfaces should only consume a result?
  - which surfaces have drifted because no one owns the propagation path strongly enough?

## Existing Stronger Inputs

- [e:c+i] Checkpoint-3 already aimed at a related concern by mapping the GSD surface family and workflow/artifact contracts rather than only isolated files. Sources: [.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts-spec.md:5), [.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts-spec.md:13).
- [d:r:i] The docs/harness intervention layer also already pushed toward stronger surface mapping and Codex-harness interaction carry through:
  - `../harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md`
  - `../governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md`
  - `../indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md`
  - `../indexes/SURFACE-STATUS-AND-DELTA.md`
- [d:r:i] The uplift family now adds a more concrete composition-layer example. The landed slice plus its reread make the current missing family easier to see: once one contract changes, what else should have changed with it across the wider network?

## The Current Stronger Reading

- [d:r:i] The workspace has done meaningful propagation work, but not yet to the strongest available form.
- [d:r:i] Stronger current gains:
  - reference-heavy planning/audit topology changes now have a managed refmap tool
  - live-vs-overlay and manifest/install surfaces now have real classification tooling
  - uplift now has a thin producer/consumer chain with durable outputs and a `progress` consumer
  - several contract families have been widened and then challenged through explicit audit lanes
- [d:r:i] What still thins:
  - no explicit producer/consumer map for many workflow->artifact->consumer chains
  - no compact impact map for `if this contract changes, these adjacent surfaces should be re-read`
  - no one audit that checks whether changed contract families actually propagated into scripts, skills, wrappers, and outputs
  - no one enhanced docs layer that fully unifies upstream GSD docs, repo-local doctrine, and Codex-harness interaction structure into one stronger dependency view

## Candidate Audit Questions

- [d:r:i] Which workflow, skill, script, manifest, wrapper, and output surfaces are direct producers of contract changes?
- [d:r:i] Which surfaces are direct consumers, indirect consumers, or only narrative mirrors?
- [d:r:i] Where does the current repo already expose dependency relations strongly, and where do those relations remain ambient or memory-carried?
- [d:r:i] Which recent contract changes in this workspace propagated strongly, and which ones still leave likely un-updated neighbors?
- [d:r:i] Which enhanced docs or inventories would most improve operator control over relevance, downstream consequence, and re-read obligations?
- [d:r:i] Which contract families need machine-helped dependency disclosure, and which are better carried by stronger docs and audit protocols alone?

## Likely Scope Of The Later Audit

- [d:r:i] workflow -> artifact contracts
- [d:r:i] skill/workflow consumer routing
- [d:r:i] runtime registry and wrapper posture
- [d:r:i] manifest/report/state consumer chains
- [d:r:i] governance-doc and required-reading propagation
- [d:r:i] repo-local tooling inventory and its doctrine-carrying role
- [d:r:i] Codex-harness interaction surfaces that upstream docs alone do not explain strongly enough

## Sequencing

- [d:r:i] Do not open this audit family before the uplift signal-layer harden slice lands.
- [d:r:i] The harden slice makes the current uplift family a cleaner example of producer/consumer carry.
- [d:r:i] After that, this audit can ask the wider network question on stronger basis instead of mixing live signal noise with propagation judgment.

## Current Consequence

- [d:r:i] This concern is now recorded as an explicit later audit family rather than only as chat memory.
- [d:r:i] The immediate next move remains the uplift signal-layer harden slice.
- [d:r:i] The next broader audit after that should use this seed together with the older Checkpoint-3 mapping lineage and the enhanced harness-intervention docs layer.
