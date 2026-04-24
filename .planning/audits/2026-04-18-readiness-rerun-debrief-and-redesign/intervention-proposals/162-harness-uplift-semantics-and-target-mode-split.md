Date: 2026-04-22
Status: active doctrine note

# Harness Uplift Semantics And Target-Mode Split

## Role

- [d:r:i] This note fixes a recurring semantic blur around the word `uplift`.
- [d:r:i] Its job is to distinguish what is being uplifted, in what sense, and by what mode, so later extraction, deployability, host-artifact, and harness-agential work do not get misread as one flattened family.

## Why This Note Exists

- [d:r:i] The workspace currently contains three overlapping projects:
  - the `prix-guesser` host product
  - the repo-local harness-modifier development program
  - the later standalone/distributable harness-modifier project
- [d:r:i] When those are not kept distinct, host-product horizon carriers can be over-read as harness-program horizon carriers, and host-artifact uplift can be misread as harness-agential improvement.

## Uplift Targets

### 1. Harness-Contract Uplift

- [d:r:i] The target is the harness as a contract-bearing system:
  - workflows
  - skills
  - registries
  - helper boundaries
  - installer/materialization logic
  - propagation routes
  - review routes
  - extraction seams

### 2. Host-Artifact Uplift

- [d:r:i] The target is the host repo's existing operational corpus:
  - `.planning/STATE.md`
  - `.planning/phases/*`
  - uplift memory
  - runtime directories
  - seed corpora
  - migration packets
- [d:r:i] This is the family that keeps a host repo runnable or more readable under the modified harness.

### 3. Harness-Agential Uplift

- [d:r:i] The target is the harness as a software-development / project / planning machine.
- [d:r:i] This includes:
  - handling multiple horizons without blur
  - adapting to new evidence without drift
  - preserving promising futures without premature closure
  - routing deferred/open findings more cleanly
  - carrying long-horizon orientation while remaining revisable

### 4. Harness-Operational Uplift

- [d:r:i] The target is the improvement program's own execution posture:
  - launch truth
  - inheritance/disposition
  - timing calibration
  - overlap discipline
  - sub-agent onboarding and continuity
  - governance/admin carry while lanes run

### 5. Harness-Adaptive Uplift

- [d:r:i] The target is post-deploy learning and correction:
  - discrepancy capture
  - semantic signal capture
  - expectation-versus-observation comparison
  - doctrine sedimentation
  - adaptive correction loops

### 6. Distribution / Deployability Uplift

- [d:r:i] The target is travel across host repos and runtimes:
  - extraction into its own repo
  - installability
  - compatibility declaration
  - host-context testing breadth
  - deployment and upgrade surfaces

## Uplift Modes

- [d:r:i] `neutralize`
  - remove host-local or helper-local literals so a cleaner carrier can own them
- [d:r:i] `externalize`
  - move a contract, policy, or grammar into a named carrier
- [d:r:i] `propagate`
  - carry a changed contract through its neighboring producer / consumer / registry / governance surfaces
- [d:r:i] `classify`
  - distinguish cases that should not yet be collapsed into one branch
- [d:r:i] `translate`
  - carry a contract across runtime or host-shape differences
- [d:r:i] `observe`
  - disclose posture, divergence, or current carry state without forcing write-side action
- [d:r:i] `adapt`
  - change the harness or host behavior in response to stronger evidence
- [d:r:i] `sediment`
  - stabilize a result into doctrine, carrier, or governance form
- [d:r:i] `deploy`
  - make the modifier/install path travel into real host contexts

## Interpretation Rules

- [d:r:i] Do not use `uplift` as a singular umbrella when the target or mode matters materially.
- [d:r:i] If a slice changes how the modifier governs host planning artifacts, that is usually:
  - harness-contract uplift
  - by neutralization or externalization
  - in service of host-artifact uplift
- [d:r:i] If a slice changes how the improvement program handles horizons, open questions, overlap, or later revision, that is harness-agential and/or harness-operational uplift, not host-artifact uplift.
- [d:r:i] If a slice changes deployability, compatibility, or later standalone travel, that belongs to distribution/deployability uplift even when it reuses host-artifact evidence.

## Current Concrete Example

- [d:r:i] [../../../../harness_modifier/uplift/state_section.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/state_section.json) and [../../../../harness_modifier/uplift/phase_layout.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/uplift/phase_layout.json) are not primarily host-product horizon doctrine.
- [d:r:i] They are modifier-owned carriers created during harness development.
- [d:r:i] Their target is deployed host-artifact uplift:
  - how the modifier reads and writes host planning artifacts
  - not how `prix-guesser` chooses its own long-horizon product direction

## Anti-Misread Rules

- [d:r:i] Host-product planning docs are not the default horizon carriers for the harness-improvement program.
- [d:r:i] A development-time extraction of a deployed contract is not category confusion by itself; it becomes confusing only when the target/mode split is left unnamed.
- [d:r:i] Later extraction into its own repo is partly a packaging move and partly a semantic-sovereignty move.

## Immediate Consequence

- [d:r:i] Use this note when reading or writing later extraction, deployability, responsible-closure, and host-uplift proposals.
- [d:r:i] If a later note says `uplift` without the target or mode being inferable from context, sharpen it rather than letting the ambiguity ride.
