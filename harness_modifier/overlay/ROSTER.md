# Harness Modifier Overlay Roster

This roster freezes the current tracked overlay frontier declared in
`tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`.

Current split:
- total tracked overlay entries: `78`
- `generic`: `7`
- `shared-boundary`: `69`
- `host-local`: `2`

Context rule:
- ordinary references to generic GSD planning canon such as `.planning/PROJECT.md`
  or `.planning/STATE.md` are not treated here as extraction defects by
  themselves
- the live blockers for the first filesystem rehome are narrower:
  - embedded host audit-workspace paths
  - helper-home references that still point at `tooling/codex/*.py`
  - compact-prompt bodies that intentionally preserve this host repo's doctrine

## Generic Carriers

These carriers can travel as modifier-owned overlay content without first
splitting host doctrine out of their current text.

| Path | Mode | Current extraction posture | Why it can travel |
| --- | --- | --- | --- |
| `skills/gsd-propagation-review/SKILL.md` | `add` | `first-filesystem-rehome` | Additive specialist skill adapter; wrapper text is generic and points to the workflow shell. |
| `skills/gsd-uplift-project/SKILL.md` | `add` | `first-filesystem-rehome` | Additive specialist skill adapter; wrapper text is generic and points to the workflow shell. |
| `skills/gsd-seed-migration-inventory/SKILL.md` | `add` | `first-filesystem-rehome` | Additive specialist skill adapter; wrapper text is generic and points to the workflow shell. |
| `skills/gsd-rigorous-research/SKILL.md` | `add` | `later-generic-slice` | Additive specialist research adapter with generic route semantics. |
| `skills/gsd-rigorous-research/references/method.md` | `add` | `later-generic-slice` | Generic research method reference. |
| `skills/gsd-rigorous-research/references/output-template.md` | `add` | `later-generic-slice` | Generic research output template. |
| `skills/gsd-rigorous-research/references/repo-canon.md` | `add` | `later-generic-slice` | Generic repo-canon reference that names planning canon without embedding host audit-workspace paths. |

## Shared-Boundary Carriers

These carriers belong to the standalone modifier story, but they still depend on
upstream overwrite behavior, host planning/runtime consumers, helper-home
references, or later text-neutrality work.

### Runtime / Agent / Installer Layer

| Path | Mode | Current extraction posture | Why it remains shared-boundary |
| --- | --- | --- | --- |
| `agents/gsd-code-fixer.md` | `overwrite` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-code-fixer.toml` | `add` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-code-reviewer.md` | `overwrite` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-code-reviewer.toml` | `add` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-executor.toml` | `add` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-intel-updater.md` | `overwrite` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-intel-updater.toml` | `add` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-pattern-mapper.md` | `overwrite` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-pattern-mapper.toml` | `add` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-phase-researcher.toml` | `add` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-plan-checker.toml` | `add` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-planner.toml` | `add` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `agents/gsd-verifier.toml` | `add` | `later` | Runtime-specific agent carrier tied to overlay materialization and later extraction routing. |
| `config.toml` | `add` | `later` | Runtime config carrier tied to the current install/materialization contract. |
| `get-shit-done/bin/lib/audit.cjs` | `overwrite` | `later` | Patched upstream CLI library; generic contract but still tied to host materialization and overlay apply. |
| `get-shit-done/bin/lib/config.cjs` | `overwrite` | `later` | Patched upstream CLI library; generic contract but still tied to host materialization and overlay apply. |
| `get-shit-done/bin/lib/phase.cjs` | `overwrite` | `later` | Patched upstream CLI library; generic contract but still tied to host materialization and overlay apply. |
| `get-shit-done/bin/lib/roadmap.cjs` | `overwrite` | `later` | Patched upstream CLI library; generic contract but still tied to host materialization and overlay apply. |
| `get-shit-done/bin/lib/state.cjs` | `overwrite` | `later` | Patched upstream CLI library; generic contract but still tied to host materialization and overlay apply. |

### References And Templates

| Path | Mode | Current extraction posture | Why it remains shared-boundary |
| --- | --- | --- | --- |
| `get-shit-done/references/agent-contracts.md` | `overwrite` | `later` | Reference carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/references/entry-runtime-uplift-continuity.md` | `add` | `later-text-neutrality-slice` | Continuity reference is plausibly generic but still tied to host planning-state carriers. |
| `get-shit-done/references/mandatory-initial-read.md` | `overwrite` | `later` | Upstream-overwrite reference that must stay aligned with baseline and host reading doctrine. |
| `get-shit-done/references/milestone-boundary-uplift-continuity.md` | `add` | `later-text-neutrality-slice` | Continuity reference is plausibly generic but still tied to host planning-state carriers. |
| `get-shit-done/references/planner-reviews.md` | `overwrite` | `later` | Reference carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/references/planning-config.md` | `overwrite` | `later` | Reference carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/references/verification-overrides.md` | `overwrite` | `later` | Reference carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/templates/config.json` | `overwrite` | `later` | Template carrier shapes host planning canon and remains coupled to upstream/runtime materialization. |
| `get-shit-done/templates/context.md` | `overwrite` | `later` | Template carrier shapes host planning canon and remains coupled to upstream/runtime materialization. |
| `get-shit-done/templates/phase-prompt.md` | `overwrite` | `later` | Template carrier shapes host planning canon and remains coupled to upstream/runtime materialization. |
| `get-shit-done/templates/research.md` | `overwrite` | `later` | Template carrier shapes host planning canon and remains coupled to upstream/runtime materialization. |
| `get-shit-done/templates/spec.md` | `overwrite` | `later` | Template carrier shapes host planning canon and remains coupled to upstream/runtime materialization. |
| `get-shit-done/templates/state.md` | `overwrite` | `later` | Template carrier shapes host planning canon and remains coupled to upstream/runtime materialization. |
| `get-shit-done/templates/verification-report.md` | `overwrite` | `later` | Template carrier shapes host planning canon and remains coupled to upstream/runtime materialization. |

### Workflows

| Path | Mode | Current extraction posture | Why it remains shared-boundary |
| --- | --- | --- | --- |
| `get-shit-done/workflows/complete-milestone.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/discuss-phase-assumptions.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/discuss-phase-power.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/discuss-phase.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/do.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/explore.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/health.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/ingest-docs.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/new-milestone.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/new-project.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/plan-phase.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/plant-seed.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/progress.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers; it still references helper-home uplift routing. |
| `get-shit-done/workflows/propagation-review.md` | `add` | `first-filesystem-rehome-after-text-split` | Generic mechanism shell still embeds host audit-workspace paths and helper-home refs. |
| `get-shit-done/workflows/quick.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/research-phase.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/resume-project.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers; it still references helper-home uplift routing. |
| `get-shit-done/workflows/review.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/seed-migration-inventory.md` | `add` | `first-filesystem-rehome-after-text-split` | Generic mechanism shell still points at the helper-home detect script. |
| `get-shit-done/workflows/settings.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/spec-phase.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/transition.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers; it still references helper-home uplift routing. |
| `get-shit-done/workflows/update.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |
| `get-shit-done/workflows/uplift-project.md` | `add` | `first-filesystem-rehome-after-text-split` | Generic mechanism shell still embeds host audit packet links and helper-home refs. |
| `get-shit-done/workflows/verify-phase.md` | `overwrite` | `later` | Workflow carrier remains coupled to upstream baseline or host planning/runtime consumers. |

### Skill Wrappers

| Path | Mode | Current extraction posture | Why it remains shared-boundary |
| --- | --- | --- | --- |
| `skills/gsd-discuss-phase/SKILL.md` | `overwrite` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |
| `skills/gsd-do/SKILL.md` | `overwrite` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |
| `skills/gsd-explore/SKILL.md` | `overwrite` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |
| `skills/gsd-from-gsd2/SKILL.md` | `overwrite` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |
| `skills/gsd-health/SKILL.md` | `overwrite` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |
| `skills/gsd-plan-phase/SKILL.md` | `overwrite` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |
| `skills/gsd-plant-seed/SKILL.md` | `overwrite` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |
| `skills/gsd-progress/SKILL.md` | `add` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |
| `skills/gsd-resume-work/SKILL.md` | `overwrite` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |
| `skills/gsd-review/SKILL.md` | `overwrite` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |
| `skills/gsd-update/SKILL.md` | `overwrite` | `later` | Skill wrapper remains coupled to host planning/runtime consumers or upstream overwrite behavior. |

## Host-Local Carriers

These entries should not travel into a generic modifier-owned overlay because
their current body preserves this host repo's concrete doctrine and control
surfaces.

| Path | Mode | Current extraction posture | Why it stays host-local |
| --- | --- | --- | --- |
| `tooling/compact-prompts/project.md` | `add` | `hold-host-local` | Compact-prompt body preserves this host repo canon and should remain host-owned. |
| `tooling/compact-prompts/readiness.md` | `add` | `hold-host-local` | Compact-prompt body preserves host readiness/rerun doctrine and should remain host-owned. |

## First Filesystem-Rehome Eligible Set

The frozen first eligible set is:
- `skills/gsd-uplift-project/SKILL.md`
- `skills/gsd-propagation-review/SKILL.md`
- `skills/gsd-seed-migration-inventory/SKILL.md`
- `get-shit-done/workflows/uplift-project.md`
- `get-shit-done/workflows/propagation-review.md`
- `get-shit-done/workflows/seed-migration-inventory.md`

Current blocker state:
- the three skill adapters are already generic enough to travel
- the three workflow shells still need one text-abstraction pass first:
  - replace hard host audit-workspace links with generic package-owned or
    named-host-appendix references
  - replace helper-home refs that still point at `tooling/codex/*.py`
    with the post-rehome authoritative helper home or a stable shim contract

Later slices after that first rehome:
- continuity references
- `gsd-rigorous-research` generic tranche
- overwrite workflow/template/reference families
- runtime/agent/config carriers
- compact-prompt mechanism/body split
