Date: 2026-04-22
Status: landed reusable packet template

# Uplift Docs Governance Classification Packet Template

## Purpose

- [g:r:i] Provide one reusable packet shape for the bounded `docs_governance_classification` assist pattern.
- [g:r:i] This template is for packet assembly and later delegated or parent-thread packet review.
- [g:r:i] It is not itself an accepted uplift judgment and it is not a live route hook.

## Runtime And Ownership

- [d:r:i] Default runtime: Codex subagent or parent-thread packet exercise.
- [d:r:i] Parent thread owns:
  - packet assembly
  - final disposition
  - any later governance-doc edits
  - any durable uplift writes
- [d:r:i] The assist lane or packet consumer owns only:
  - rereading the assembled packet
  - producing the bounded classification note

## Input Bundle Layout

Create one packet directory or one grouped packet note with these components:

1. `PACKET.md`
   - name the concrete uplift result or question
   - name the governance/doc carriers under consideration
   - state whether the lane is Codex-local or parent-thread only
2. `inputs/detect.json`
   - current `project_uplift.py detect ... --json` output
3. `inputs/UPLIFT-REPORT.md`
   - current durable uplift report when present
4. `inputs/UPLIFT-MANIFEST.json`
   - current durable uplift manifest when present
5. `inputs/STATE-uplift-section.md`
   - current uplift section extracted from `STATE.md`
6. `inputs/governance-docs/`
   - only the named governance carriers under current review
   - do not dump the whole governance tree when the question is narrower

## Packet Header Shape

Use this compact header in `PACKET.md`:

```md
# Uplift Docs Governance Classification Packet

- Trigger:
- Current uplift result:
- Governance carriers under consideration:
- Runtime for packet consumption:
- Explicit write boundary:
- Expected disposition home:
```

## Expected Output Shape

The packet consumer should write one bounded markdown note with these exact sections:

1. `Carriers To Refresh Now`
2. `Carriers To Hold Explicitly`
3. `Reasons`
4. `Later Route Ownership`

Inside those sections:
- name concrete carriers, not umbrella families only
- distinguish refresh now from hold explicitly
- name who should own each later route when the packet says "later"

## Disposition Endpoint

- [d:r:i] Default durable disposition home:
  - `entry-uplift-audit/dispositions/`
- [d:r:i] The disposition note should state one of:
  - `accept`
  - `revise`
  - `park`
  - `reject`
- [d:r:i] The disposition note should point back to:
  - the packet
  - the packet output
  - any later route or hold family named by the result

## Write Boundary

- [d:r:i] The packet consumer may write:
  - one bounded output note
- [d:r:i] The packet consumer may not write:
  - `UPLIFT-REPORT.md`
  - `UPLIFT-MANIFEST.json`
  - `STATE.md`
  - `uplift-project.md`
  - `gsd-uplift-project/SKILL.md`
  - any governance doc under review

## What This Template Does Not Claim

- [d:r:i] It does not define packet templates for the other three assist patterns.
- [d:r:i] It does not authorize a live uplift-route hook.
- [d:r:i] It does not replace `$gsd-propagation-review`.
- [d:r:i] It does not turn packet assembly into automatic helper behavior.
