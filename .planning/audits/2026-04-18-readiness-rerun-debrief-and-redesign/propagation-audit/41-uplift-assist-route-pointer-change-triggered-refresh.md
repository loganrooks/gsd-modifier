Date: 2026-04-22
Status: landed change-triggered refresh

# Uplift Assist Route Pointer Change-Triggered Refresh

## Purpose

- [g:r:i] Record the narrow uplift-assist route-pointer landing as a real propagation carrier instead of leaving it as a local workflow-only change.

## What Moved

- [e:c+i] The live uplift workflow now carries one operator-facing assist-family pointer in its route block:
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
- [e:c+i] The wrapper now inherits that route without duplicating the packet-template details:
  - [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)
- [e:c+i] The route now points at the assist-family reference plus both exercised packet templates:
  - [../intervention-proposals/103-uplift-agent-assist-patterns.md](../intervention-proposals/103-uplift-agent-assist-patterns.md)
  - [../entry-uplift-audit/packets/06-uplift-docs-governance-classification-packet-template.md](../entry-uplift-audit/packets/06-uplift-docs-governance-classification-packet-template.md)
  - [../entry-uplift-audit/packets/08-uplift-carrier-gap-identification-packet-template.md](../entry-uplift-audit/packets/08-uplift-carrier-gap-identification-packet-template.md)
- [e:c+i] The focused contract test now covers the pointer’s operator-initiated and helper-neutral posture:
  - [test_uplift_assist_route_pointer_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_uplift_assist_route_pointer_contract.py)
- [e:c+i] The implementation note is now explicit:
  - [../intervention-proposals/108-uplift-assist-route-pointer-first-slice-implementation.md](../intervention-proposals/108-uplift-assist-route-pointer-first-slice-implementation.md)

## Registry Consequence

- [d:r:i] The repo-local delta layer should now keep the uplift-assist family visible as:
  - a live operator-facing route inside the uplift composition layer
  - a route that still preserves detect-only posture
  - a route that points at packet/disposition carriers rather than widening helper or CLI semantics
- [d:r:i] This refresh keeps the route movement explicit without treating it as a whole propagation-registry redesign.

## Current Consequence

- [d:r:i] The uplift-assist family no longer sits only in proposal/reference/audit carriers.
- [d:r:i] It now has one real operator-facing pointer in the live uplift route, with the propagation family explicitly carrying that movement.
