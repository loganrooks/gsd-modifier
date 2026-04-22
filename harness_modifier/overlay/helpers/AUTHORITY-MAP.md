Date: 2026-04-22
Status: active helper authority map

# Helper Authority Map

## Purpose

- [g:r:i] This file records the current per-helper authority split for the modifier-owned helper bridge under `harness_modifier/overlay/helpers/`.
- [g:r:i] It exists so the shim layer does not blur together helpers whose payload authority differs materially.

## Current Split

| Helper | Shim Role | Payload Home | Authority Posture | Blockers Before Any Later Movement | Family |
| --- | --- | --- | --- | --- | --- |
| `project_uplift.py` | temporary bridge | `tooling/codex/project_uplift.py` | modifier-facing payload candidate | neutralize runtime-dir set, planning-output paths, and compatibility-anchor routing into data before any relocation slice | extraction / uplift |
| `seed_migration_inventory.py` | derivative bridge | `tooling/codex/seed_migration_inventory.py` | downstream specialist consumer; cannot lead movement | inherits `project_uplift.py` neutralization first | extraction / uplift |
| `audit_refmap.py` | stable long-lived source/install boundary | `tooling/codex/audit_refmap.py` | sharper shared-boundary helper; out of the later payload-movement candidate set | not a relocation candidate in this family; any later work is repo-local audit-tooling neutralization, not payload movement | repo-local audit tooling |

## Carry Rules

- [d:r:i] Do not treat the existence of a shim as evidence that the payload behind it should travel.
- [d:r:i] Do not treat all helper shims as having one lifetime class.
- [d:r:i] Do not reopen `audit_refmap.py` as a modifier-facing payload candidate unless its repo-local path grammar is first neutralized deliberately in a separate family.
- [d:r:i] Do not open `seed_migration_inventory.py` relocation ahead of `project_uplift.py`; its payload authority remains downstream.

## Project Uplift Neutralization Preconditions

- [d:r:i] move runtime-dir policy out of hard-coded module constants and into typed data
- [d:r:i] move uplift planning-output policy out of embedded path constants and into typed data
- [d:r:i] keep compatibility-anchor routing declaration-driven rather than helper-constant-driven
- [d:r:i] preserve `.codex` observed basis plus `.claude` held annotation while doing the neutralization

## Exact Next Move

- [d:r:i] Open a bounded `project_uplift.py` neutralization proposal.
- [d:r:i] Do not relocate any helper payload in the same slice as this authority map.
