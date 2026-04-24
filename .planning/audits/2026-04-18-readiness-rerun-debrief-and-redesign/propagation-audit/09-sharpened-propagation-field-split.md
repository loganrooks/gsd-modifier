Date: 2026-04-21
Status: active sharpened disclosure batch

# Sharpened Propagation Field Split

## Purpose

- [g:r:i] This note lands the first disclosure batch earned by the lane-02 widening reread.
- [g:r:i] `08` widened the field into seven carrier families. This note keeps that widening, but sharpens the places where one family was still carrying too many distinct propagation modes at once.
- [g:r:i] The target is stronger routing, not a flatter bigger list.

## What This Note Sharpens

- [d:c+i] This note lands the disclosure routes the lane-02 inheritance put first:
  - `H` helper-cohort disclosure
  - `I` install-frontier split
  - `J` workflow-family carrier-mode split
  - `K` skill-family mode split
  - `R` governance-scope split
  - `L` launch-truth row
  - `N` compact-prompt carrier row
  - `Q` state-continuity row
  Source: [dispositions/02-broader-network-propagation-field-mapping-inheritance.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/dispositions/02-broader-network-propagation-field-mapping-inheritance.md:16).
- [d:r:i] The larger seven-family split from `08` remains the right top-level field map.
- [d:r:i] This note is the sharper sub-family layer that later operators should use when the seven-row view is too coarse.

## Sharpened Carrier Rows

| Sharpened carrier | Main producers | Main consumers | Distinct carry |
| --- | --- | --- | --- |
| Governing doctrine | root/planning `AGENTS.md`, `CLAUDE.md`, `LONG-ARC.md`, `CLAIM-TYPES.md` | agents, workflows, skills, audit specs, research lanes | repo-wide doctrine and request-shaping carry |
| Upstream-pristine install frontier | upstream installer, `gsd-file-manifest.json`, `.codex/gsd-local-patches/backup-meta.json` | pristine live `.codex/` files, local overlay contract | upstream-shipped truth before repo-local overlay carry |
| Local-overlay frontier | tracked overlay, `OVERLAY-MANIFEST.json`, `portable_gsd_contract.py`, installer overlay apply step | live `.codex/` overlay-owned files | repo-local overlay ownership and post-materialization verification |
| Runtime registry / launch authority | `.codex/config.toml`, `.codex/agents/*.toml`, root model doctrine | spawned workers, runtime role selection | declared active runtime authority |
| Launch-truth / orchestration capture | `capture_launch_truth.py`, per-lane `launch-truth/`, `../root-support/LAUNCH-LEDGER.md`, `~/.codex/state_5.sqlite` | reviewers, audit inheritance, spawn verification | requested-vs-effective launch history |
| Workflow -> durable output | `workflows/*.md` that write `.planning/` artifacts | operators, later phases, helper readers | live workflow semantics and output production |
| Template -> output shape | `templates/*.md` | workflows, planning artifacts, later readers | schema/shape pressure on produced artifacts |
| Reference -> agent behavior | `references/*.md` | workflows, agents, skills | behavioral and doctrine-sensitive guidance |
| Lib -> runtime implementation | `bin/lib/*.cjs` | workflow runtime, CLI behavior | executable runtime logic |
| Invocation-binding wrapper | most `skills/*/SKILL.md` | user invocation, workflow binding | entry routing into deeper contracts |
| Reference-owner skill | skills carrying embedded reference sets, especially `gsd-rigorous-research` | users, helper sampling, doctrine-sensitive marker carry | skill-owned reference logic and sampleable doctrine markers |
| Named helper cohorts | `project_uplift.py`, `audit_refmap.py`, `runtime_visibility.py`, `capture_runtime_visibility_snapshot.py`, `manifest_install_coherence.py`, `portable_gsd_contract.py`, `scan_threshold_language.py`, `capture_launch_truth.py` | direct consumers, reports, governance/audit users | producer-specific helper/output chains |
| State-continuity surface | `.planning/STATE.md` and its writers | re-entry workflows, operators, audit/state readers | multi-owner durable project memory |
| Compact-prompt carry | `tooling/compact-prompts/*`, `.codex.local/compact-prompt.txt`, installer prompt-override wiring | compacted sessions, operator reset path | repo-local compaction override carry |
| Repo-root doctrine scope | repo-root governance docs | all workspaces and runtime families | repo-wide contract pressure |
| Workspace governance scope | `CURRENT-STATE`, `STATUS`, `INDEX`, `ARTIFACT-INVENTORY`, protocol docs | this audit workspace | workspace-level routing and relevance control |
| Audit-lane artifact scope | packet/spec/prompt/output/disposition sets | one challenge lane and its inheritance | lane-scoped audit memory |

## Sharpening Rationale

### Install Frontiers

- [e:c+i] The installer contract already distinguishes tracked overlay truth from backup-carried overwrite truth in code. Sources: [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:70), [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:137).
- [d:r:i] Treating both as one row in `08` was useful for widening, but too blended for later contract-change routing.

### Workflow Family Modes

- [e:c+i] `workflow`, `template`, `reference`, and `bin/lib` carriers all appear inside the installer-backed runtime subset, but they impose different propagation duties. Source: [.codex/gsd-local-patches/backup-meta.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:5).
- [d:r:i] The sharper split stops later readers from treating all touched workflow-adjacent files as one kind of move.

### Skill Modes

- [e:c+i] `project_uplift.py` samples `gsd-rigorous-research` reference carriers as doctrine-sensitive markers, which is a different propagation shape than plain wrapper invocation. Source: [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:118).
- [d:r:i] The sharper split keeps wrapper-routing logic distinct from skill-owned reference logic.

### Governance Scopes

- [e:c+i] The governance protocol already separates fast re-entry, synthesis, mutable queue, and deeper trace surfaces. Source: [GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md:16).
- [d:r:i] The sharper scope split makes explicit that repo doctrine, workspace governance, and lane artifacts do not carry the same propagation burden.

## Active Use

- [d:r:i] Use `08` for the top-level field view.
- [d:r:i] Use this note when a change touches one of the formerly blended rows and the next question is `which specific carrier mode moved?`
- [d:r:i] Keep the next invariant / relation batch explicit rather than absorbing it here:
  - `O` model-policy three-surface invariant
  - `P` upstream-pristine frontier propagation obligation
  - `S` cross-family-edge supplement

## Current Consequence

- [d:r:i] The propagation family now carries a stronger two-level map:
  - `08` for top-level family disclosure
  - `09` for the first sharpened sub-family layer
- [d:r:i] The next move is to land the named invariant / relation companions that sit between these sharpened rows.
