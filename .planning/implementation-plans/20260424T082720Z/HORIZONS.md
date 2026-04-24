# Horizon Plan

Date: 2026-04-24
Status: draft strategic frame

## Trace Links

- Package index: [README.md](README.md)
- Short-horizon program plan: [SHORT-HORIZON.md](SHORT-HORIZON.md)
- Current immediate concrete plan: [concrete-plans/002-runtime-intervention-surface-inventory/PLAN.md](concrete-plans/002-runtime-intervention-surface-inventory/PLAN.md)

## Context

`gsd-modifier` is intended to become a deployable, robust modified GSD/GSDR harness for near-term use. It should help early `prix-guesser` development without pretending to be the final product-building harness.

The longer-term operating-model question now lives in `../harness-studio`.

The practical sequencing problem is:

1. stabilize `gsd-modifier`
2. ship a short-term bridge harness
3. use it conservatively for early `prix-guesser`
4. design the richer future harness in `harness-studio`
5. avoid foreclosing migration from GSD-based artifacts into the future harness

## Immediate Horizon

Goal: restore `gsd-modifier` to a clean, auditable, releasable development state.

Primary work:

- stabilize the imported audit folder in `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`
- remove or avoid unwanted imported clutter such as the already-deleted top-level `.planning/topology-map`
- fix `tooling/codex/audit_refmap.py` so batch moves handle both moved targets and moved source files
- regenerate reference-map reports through the script, not ad hoc repair
- verify reference-count regression against the known baseline
- bucket commits by semantic boundary
- avoid touching unrelated dirty model-benchmark/config files unless explicitly brought into scope

Exit criteria:

- audit import is in the intended location
- reference rewrites are script-backed
- missing-link count is explained and not silently worsened
- audit import, script/tooling fixes, and docs/handoff updates are separated into reviewable commit buckets
- deterministic local verification passes for touched tooling

Current concrete plan:

- [001 Audit Import Refmap Stabilization](concrete-plans/001-audit-import-refmap-stabilization/PLAN.md) - completed
- [002 Runtime Intervention Surface Inventory](concrete-plans/002-runtime-intervention-surface-inventory/PLAN.md) - current executable draft

## Short-Term Horizon

Goal: make `gsd-modifier` deployable as a bridge harness.

Primary work:

- maintain Codex/Claude core parity as shared outcomes, not identical wrapper files
- explicitly inventory runtime-exposed intervention surfaces:
  - `AGENTS.md`
  - `.planning/AGENTS.md`
  - `CLAUDE.md`
  - `.planning/CLAUDE.md`
  - Codex compact prompt config
  - `.codex/config.toml`
  - `.codex/agents/*.toml`
  - Claude runtime equivalents
  - generated onboarding/governance docs
  - uplift carrier catalog
- audit current `new-project` and uplift behavior around `AGENTS.md` and `CLAUDE.md`
- decide whether `CLAUDE.md` generation needs parity extension or a separate runtime-specific companion
- define the bridge-harness contract for early `prix-guesser`
- define project-level governance artifact seeding posture, including whether `LONG-ARC.md` remains sufficient or should be joined by artifacts such as `OPERATING-MODEL.md`, `PRODUCT-THESIS.md`, `WORKFLOW-LANES.md`, `FEEDBACK-LOOPS.md`, `RELEASE-PLAN.md`, and `RISK-REGISTER.md`
- rerun full repo-self dual-runtime verification

Exit criteria:

- deployable bridge-harness release boundary is documented
- runtime intervention surfaces are inventoried and their parity posture is explicit
- project-governance artifact seeding is specified at least at contract level
- repo-self Codex/Claude materialization proof is green
- CI gates pass

## Medium-Term Horizon

Goal: use the bridge harness conservatively for early `prix-guesser` milestones.

Primary work:

- apply the deployable `gsd-modifier` harness to `prix-guesser`
- declare active workflow lanes per phase/milestone instead of treating all work as homogeneous phase execution
- use GSD for execution logistics: plans, handoffs, delegation, verification, review, audit, commits
- preserve product/game strategy as portable artifacts outside GSD-only state
- run UI/design, architecture, product, feedback, security, and devops workflows only when the project stage calls for them
- record migration-relevant outputs so `harness-studio` can later ingest or reinterpret them

Exit criteria:

- early `prix-guesser` work is better governed without making GSD the permanent product brain
- product artifacts remain portable and inspectable
- bridge constraints are respected:
  - no hidden product strategy only in `.planning/STATE.md`
  - no release cadence as accidental phase-completion byproduct
  - no buried feedback loops in chat-only summaries

## Long-Term Horizon

Goal: let `harness-studio` define the future product-building operating model.

Primary work:

- complete a portfolio audit across current and plausible future projects
- classify projects by ambition, risk, lifecycle, monetization possibility, domain complexity, and workflow needs
- design an operating-model selector
- define workflow playbooks independent of GSD
- define expert-role or capability modules
- decide whether GSD remains a useful execution kernel, becomes one adapter, or is replaced
- define migration/import paths from GSD artifacts into the future harness

Exit criteria:

- `harness-studio` can explain which harness shape fits which project class
- GSD's future role is explicitly decided rather than assumed
- early `prix-guesser` bridge artifacts can be imported or interpreted by the future harness
