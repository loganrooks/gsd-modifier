Date: 2026-04-22
Status: landed bounded reference

# Uplift Agent-Assist Patterns

## Purpose

- [g:r:i] Define the bounded uplift-assist shapes that later delegation may use without dissolving project uplift into an agent-owned black box.
- [g:r:i] This reference is for narrower uplift subproblems, not for handing away the composition layer.

## Governing Rule

- [e:c+i] The uplift workflow remains detect-only by default, keeps broader uplift refresh/install routes held for later slices, and keeps composition separate from current execution/verification routing when the helper classifies the repo as `mid-phase uplift`. Sources:
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md:24)
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md:31)
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md:120)
- [d:c+i] Later uplift delegation should therefore sharpen narrower subproblems while leaving final uplift judgment, durable uplift writes, and multi-route composition in the parent thread. Sources:
  - [93-uplift-agent-assist-and-propagation-baseline-split-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/93-uplift-agent-assist-and-propagation-baseline-split-note.md:41)
  - [102-uplift-agent-assist-first-slice-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/102-uplift-agent-assist-first-slice-proposal.md:20)

## Allowed Assist Patterns

### 1. `docs_governance_classification`

- [d:r:i] Goal:
  - classify which governance and durable-memory carriers deserve refresh after a concrete uplift result
- [d:r:i] Input packet:
  - current uplift detect JSON
  - current `UPLIFT-REPORT.md` / `UPLIFT-MANIFEST.json` / `STATE.md` uplift section when they already exist
  - the named governance docs under consideration
- [d:r:i] Output:
  - one compact note listing:
    - carriers to refresh now
    - carriers to hold explicitly
    - reasons and later route ownership
- [d:r:i] Write boundary:
  - packet or note only
  - no direct edit of governance docs by the assist lane

### 2. `carrier_gap_identification`

- [d:r:i] Goal:
  - surface neighboring workflow/skill/output/governance carriers that the current uplift slice still leaves thinner
- [d:r:i] Input packet:
  - current uplift detect JSON
  - [95-upstream-pristine-propagation-baseline-first-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/95-upstream-pristine-propagation-baseline-first-slice.md)
  - [96-repo-local-propagation-delta-first-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/96-repo-local-propagation-delta-first-slice.md)
  - the current `propagation-review` route when propagation widening matters
- [d:r:i] Output:
  - one bounded gap list grouped by:
    - direct consumers
    - narrative mirrors
    - runtime/registry carriers
    - held-later neighbors
- [d:r:i] Relation to `$gsd-propagation-review`:
  - treat this pattern as the uplift-context narrowing that can precede a wider propagation review when the question starts from an uplift result
  - do not treat it as a competing replacement for `$gsd-propagation-review` when the question is already a concrete multi-family contract change
- [d:r:i] Write boundary:
  - read-only analysis or one bounded review note

### 3. `additive_install_packet`

- [d:r:i] Goal:
  - draft a bounded packet for absent additive carriers without silently turning detect-only uplift into install work
- [d:r:i] Input packet:
  - `absent_additive_carriers`
  - current runtime/materialization evidence
  - compatibility anchor
- [d:r:i] Output:
  - one install-route packet or proposal note
- [d:r:i] Write boundary:
  - packet/proposal only
  - no direct installation or carrier mutation by the assist lane

### 4. `cross_runtime_comparison_packet`

- [d:r:i] Goal:
  - build a sharper comparison packet when uplift needs to reason across more than one runtime/materialized state
- [d:r:i] Input packet:
  - `runtime_dirs`
  - observed runtime basis
  - compatibility posture
  - relevant runtime snapshots or coherence artifacts
- [d:r:i] Output:
  - one bounded comparison packet for later review
- [d:r:i] Write boundary:
  - packet only
  - no direct runtime mutation by the assist lane

## Packet Assembly

- [d:r:i] Packet assembly stays parent-thread-owned unless a later helper or wrapper earns that job explicitly.
- [d:r:i] For `docs_governance_classification`, use the packet template at:
  - [entry-uplift-audit/packets/06-uplift-docs-governance-classification-packet-template.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/entry-uplift-audit/packets/06-uplift-docs-governance-classification-packet-template.md)
- [d:r:i] For `carrier_gap_identification`, use the packet template at:
  - [entry-uplift-audit/packets/08-uplift-carrier-gap-identification-packet-template.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/entry-uplift-audit/packets/08-uplift-carrier-gap-identification-packet-template.md)
- [d:r:i] Do not infer that the other three patterns have the same packet shape.
- [d:r:i] Each later pattern should earn its own assembly carrier when its concrete subproblem becomes live.

## Output Discipline

- [e:c+i] The propagation-review route now already requires durable notes to prefer existing lane homes and to preserve local claim-type grammar when they land inside this audit workspace. Source: [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:123).
- [d:r:i] Later uplift assist lanes should follow the same discipline:
  - `outputs/` for preserved external/composite returns
  - `dispositions/` for local inheritance or judgment
  - `*-change-triggered-refresh.md` when the note itself becomes a propagation carrier
- [d:r:i] Until a live route hook exists, the default durable disposition home for this family is:
  - [entry-uplift-audit/dispositions/](../entry-uplift-audit/dispositions/)
- [d:r:i] Assist output is never self-accepting.
- [d:r:i] The parent thread must still disposition it as:
  - `accept`
  - `revise`
  - `park`
  - `reject`

## Delegation Shape

- [d:r:i] Use a Codex subagent only when the subproblem is concrete, bounded, and has an auditable read/write boundary.
- [d:r:i] Use an external Opus lane when the task is widening, field-mapping, or comparative challenge rather than repo-local packet work.
- [d:r:i] Keep one assist lane per subproblem. Do not launch a generic “uplift helper” agent with mixed ownership.
- [d:r:i] Default runtime mapping for the current four patterns:
  - `docs_governance_classification` -> Codex subagent or parent-thread packet exercise
  - `carrier_gap_identification` -> Opus widening when the gap question is still field-mapping; Codex only when the carrier set is already concrete and bounded
  - `additive_install_packet` -> Codex subagent or parent-thread packet drafting
  - `cross_runtime_comparison_packet` -> external Opus lane unless the comparison has already been narrowed to one auditable repo-local packet

## What This Reference Does Not Authorize

- [d:r:i] No monolithic uplift agent that owns project uplift end-to-end.
- [d:r:i] No automatic agent spawn from `uplift-project` by default.
- [d:r:i] No delegation of final uplift classification, durable uplift writes, or cross-route composition.
- [d:r:i] No silent upgrade from detect-only posture into additive install or rewrite work.

## Current Consequence

- [d:r:i] The uplift-agent question now has a bounded reference surface rather than only an open note and a proposal.
- [d:r:i] The family now carries two exercised patterns with explicit packet templates:
  - `docs_governance_classification`
  - `carrier_gap_identification`
- [d:r:i] The narrow live route pointer is now landed in `uplift-project.md`.
- [d:r:i] The `docs_governance_classification` pattern now also has one live-trigger runtime-proof plus the resulting parent-thread durable refresh.
- [d:r:i] The `cross_runtime_comparison_packet` family now also has one reusable packet carrier.
- [d:r:i] The `cross_runtime_comparison_packet` family now also has its first exercised packet round trip in `112`.
- [d:r:i] That Opus widening lane is now completed and inherited through lane `07`.
- [d:r:i] The concern-family split note and its follow-on Opus lane are now also completed and inherited through lane `08`.
- [d:r:i] The next adjacent move is now the bounded compatibility-family widening-shape proposal in `114` before any live `.claude` translation or composition judgment.
