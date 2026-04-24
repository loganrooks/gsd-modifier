Date: 2026-04-22
Status: reference, route pointer, and docs-governance runtime-proof landed

# Uplift Agent-Assist First Slice Proposal

## Purpose

- [g:r:i] Define the first bounded uplift-agent-assist route without turning project uplift into an agent-owned black box.
- [g:r:i] Keep the composition layer and operator-facing judgment in the parent thread while identifying the narrower subproblems that later delegation can sharpen.

## Why This Route Now

- [e:c+i] The repo-local uplift route is already a real composition-layer workflow with helper-driven detect/write posture and explicit held-later routes. Sources:
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md:24)
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md:104)
- [e:c+i] The propagation family now also has a cleaner operator-facing review route with the route-hardening follow-through landed, so later delegation no longer needs to answer to a thinner propagation surface. Sources:
  - [97-propagation-review-route-first-slice-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/97-propagation-review-route-first-slice-proposal.md:8)
  - [100-propagation-review-route-harden-follow-through-implementation.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/100-propagation-review-route-harden-follow-through-implementation.md:5)
- [d:c+i] The remaining live question is no longer whether uplift exists. The live question is which narrower uplift subproblems deserve delegation while the main thread keeps composition-layer control. Source: [93-uplift-agent-assist-and-propagation-baseline-split-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/93-uplift-agent-assist-and-propagation-baseline-split-note.md:39).

## Proposed First Slice

- [d:r:i] Do not add a monolithic `uplift agent` that owns project uplift end-to-end.
- [d:r:i] Add one explicit bounded assist pattern family for later use at the uplift boundary:
  - docs/governance uplift classification
  - carrier-gap identification across workflow/skill/output/governance surfaces
  - additive-install packet drafting
  - cross-runtime comparison packet drafting
- [d:r:i] Keep those assist lanes read-only or packet-writing-first.
- [d:r:i] Keep final uplift judgment, durable uplift writes, and composition across neighboring routes in the parent thread.

## Proposed Carriers

- [d:r:i] One bounded reference surface:
  - `103-uplift-agent-assist-patterns.md`
  - role:
    - define the allowed assist-lane shapes
    - define input packet expectations
    - define write-boundary and disposition rules
- [d:r:i] One bounded route note in the uplift family:
  - later update `uplift-project.md` and `gsd-uplift-project/SKILL.md` so they can point at those assist patterns when the operator explicitly wants delegation
  - do not make delegation the default posture

## Assist Patterns That Look Most Promising

- [d:r:i] `docs_governance_classification`
  - input:
    - current uplift detect output
    - current uplift report/manifest/state section
    - named governance docs that may need alignment
  - output:
    - one compact candidate disposition note
- [d:r:i] `carrier_gap_identification`
  - input:
    - uplift detect output
    - baseline/delta pair
    - current propagation review route
  - output:
    - one compact list of neighboring carriers that deserve follow-through or explicit hold
- [d:r:i] `additive_install_packet`
  - input:
    - absent additive carriers
    - runtime/materialization evidence
    - current uplift posture
  - output:
    - one bounded install-route packet
- [d:r:i] `cross_runtime_comparison_packet`
  - input:
    - runtime dirs
    - observed runtime basis
    - compatibility anchor
  - output:
    - one bounded comparison packet for later review

## Boundaries

- [d:r:i] No automatic agent spawn from `uplift-project` in this first slice.
- [d:r:i] No new CLI command in this first slice.
- [d:r:i] No durable uplift write delegated away from the parent thread in this first slice.
- [d:r:i] No broader propagation-map redesign in this first slice.

## Verification Gates

- [d:r:i] The assist-pattern reference should make write ownership and disposition boundaries explicit enough that later delegated packets cannot be mistaken for accepted uplift judgment.
- [d:r:i] The reference should fit the current propagation-review and uplift-route doctrine rather than creating a second competing propagation path.
- [d:r:i] The first implementation slice, if later accepted, should widen route-local tests or route docs so delegation remains explicit and opt-in.

## Current Consequence

- [d:r:i] The assist-pattern reference named in this proposal has now landed in `103`.
- [d:r:i] This proposal now remains active as the family boundary and sequencing carrier for what still stays outside that landed reference:
  - route-hook carry into `uplift-project.md` and `gsd-uplift-project/SKILL.md`
  - automatic-spawn refusal
  - durable-write parent-thread ownership
  - broader propagation-map hold
- [d:r:i] The first bounded packet/disposition layer and the first two parent-thread exercises now exist:
  - `docs_governance_classification`
  - `carrier_gap_identification`
- [d:r:i] The narrow operator-initiated route pointer is now landed in the live uplift route.
- [d:r:i] The `docs_governance_classification` pattern now also has one live-trigger runtime-proof and the resulting parent-thread durable refresh.
- [d:r:i] The `cross_runtime_comparison_packet` family now also has its first exercised packet round trip in `112`.
- [d:r:i] That Opus widening lane is now completed and inherited through lane `07`.
- [d:r:i] The concern-family split note and its follow-on Opus lane are now also completed and inherited through lane `08`.
- [d:r:i] The next bounded move is now the compatibility-family widening-shape proposal in `114`, not direct cross-runtime translation.
