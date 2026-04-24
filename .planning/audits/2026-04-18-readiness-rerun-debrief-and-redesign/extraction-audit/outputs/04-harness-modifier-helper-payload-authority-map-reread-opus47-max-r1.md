Date: 2026-04-22
Status: frozen lane output

# Helper Payload Authority Map Reread

## What The Current Split Already Clarified

- The landed 148 + 150 pair separated three authority surfaces and made them nameable without collapsing them:
  - **source authority** for workflow shells and skill adapters now lives under `harness_modifier/overlay/...`
  - **install-target authority** remains declared in `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`, now carrying inline `{mode, source}` indirection for the specialist tranche
  - **materialization / validation authority** remains in `harness_modifier/contract/portable_gsd_contract.py`
  - **compatibility declaration authority** is typed and package-owned at `harness_modifier/compatibility/declaration.json`
- Against that sharper grammar, the helper layer is visibly the next unresolved object. The three files under `harness_modifier/overlay/helpers/` are identical three-line shims: add repo_root to `sys.path`, `from tooling.codex.<name> import *, main`, then `raise SystemExit(main())`. Package-level authority is currently only over invocation, not over the substantive helper body.
- The three candidate payloads are visibly non-symmetric. `project_uplift.py` has already grown one reverse edge into `harness_modifier.compatibility`, so its payload now reaches up into the modifier package for typed input. `seed_migration_inventory.py` imports `from tooling.codex import project_uplift as pu` and is a narrow specialist consumer of that module. `audit_refmap.py` hard-codes `r"/home/rookslog/workspace/projects/prix-guesser/..."` and `r"(?:\.planning|tooling|scripts)/..."` into its link-grammar regex and runs `git` with `cwd=REPO_ROOT` — repo-local path grammar sits inside the payload itself.
- The first residue-classification pass had already declined to let the presence of shims stand in as a verdict on payload authority; this reread now deepens that classification with per-helper evidence instead of leaving them as a single "later" row.
- The runtime horizon the map is planning against stays `.codex` observed basis plus `.claude` held annotation, via the compatibility declaration. The map does not widen into cross-runtime composition or standalone packaging.

## Per-Helper Authority Classification

- `project_uplift.py`: **modifier-facing payload candidate, not yet earned relocation**.
  - Evidence for modifier-facing: imports `harness_modifier.compatibility.declaration`; consumes `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`; writes `.planning/UPLIFT-REPORT.md` and `.planning/UPLIFT-MANIFEST.json`; reads `.planning/STATE.md`; carries a generic `RUNTIME_DIRS = [".codex", ".claude", ".gemini", ".config/opencode", ".opencode", ".config/kilo", ".kilo"]` surface. None of that is host-specific to `prix-guesser`.
  - Evidence against relocation-readiness now: the module is 1547 lines and frames several carriers (`.planning/UPLIFT-*`, `tooling/codex/UPLIFT-HELD-LATER.md`, `RUNTIME_BASIS_DECLARATION` routing, skill/workflow pointer constants) as durable paths embedded in code rather than data. Any movement into `harness_modifier/` as payload owner would want at least the runtime-dir set and the planning-output policy made data-driven before the move rather than after it.
  - Classification outcome: this is the one helper whose later payload movement is a live object, not the helper whose payload movement should happen first. It earns a neutralization slice before any relocation slice.

- `seed_migration_inventory.py`: **derived consumer; cannot lead a payload relocation**.
  - Evidence: the entire module reaches `project_uplift` as `pu` and depends on `pu.read_text`, `pu.parse_frontmatter_map`, `pu.frontmatter_text`, `pu.extract_h2_headings`, `pu.parse_seed_contract_version`, `pu.CURRENT_SEED_CONTRACT_VERSION`, `pu.REQUIRED_SEED_FRONTMATTER_KEYS`, `pu.REQUIRED_SEED_SECTION_HEADINGS`. Its own path grammar is neutral; it writes `.planning/SEED-MIGRATION-REPORT.md` and `.planning/SEED-MIGRATION-MANIFEST.json` through the same planning-output policy.
  - Weight: narrower than `project_uplift.py`. Its posture is "moves with or after `project_uplift.py`, never before." Treating it as a same-weight sibling in this family would mis-frame the family shape.
  - Classification outcome: derived-consumer, modifier-facing in principle but strictly downstream of the `project_uplift` authority move.

- `audit_refmap.py`: **not a member of the later modifier-payload family**. Sharper shared-boundary.
  - Evidence: the payload encodes the literal host-absolute path `/home/rookslog/workspace/projects/prix-guesser/...` as a regex alternative; it further hard-codes the `.planning|tooling|scripts` subtree grammar inside `LOCAL_PATH_RE`; it resolves relative paths through `REPO_ROOT = Path(__file__).resolve().parents[2]`; it runs `git` with `cwd=REPO_ROOT`; its docstring describes it as tooling for "audit-workspace migrations," which is a repo-local concern.
  - Family judgment: this is repo-local audit / migration tooling. Its workplace is `.planning/audits/` trees, not modifier installation. Its portability is bounded by the host repo's subtree names and absolute-path grammar, not by the `.codex` / `.claude` runtime boundary.
  - Classification outcome: move this helper out of the later-payload-movement candidate set. Keep the shim as the stable overlay-facing invocation surface and let the payload stay in `tooling/codex/`. Any later work is neutralization-or-not for repo-local path grammar, not relocation.

## Shim Boundary Judgment

- The shim layer is not one answer. It is a mixed answer and the mixture is informative.
  - For `project_uplift.py` the shim is a **temporary bridge**. Once the payload has earned relocation (after the neutralization slice named below), the shim's role changes from invocation bridge to compatibility redirect, and it becomes a deletion candidate rather than a long-lived feature.
  - For `seed_migration_inventory.py` the shim is a **bridge whose lifetime tracks `project_uplift`'s**. It should not be decided separately; its role moves when the upstream helper's does.
  - For `audit_refmap.py` the shim is a **stable, long-lived source/install boundary**. The payload does not travel; the shim is the legitimate place where the overlay/helper invocation surface is typed inside the modifier package even though the substantive body stays repo-local.
- The unifying rule is not "shims are temporary" or "shims are permanent." It is that a shim's lifetime derives from the payload authority it bridges, which means the shim layer itself cannot be classified as one thing — the helper-by-helper authority classification has to govern the shim classification.
- One consequence is that the current uniform three-line shim style is workable today but understates durability differences. A later slice can make the `audit_refmap` shim a typed long-lived surface (for example, with a package-local docstring and a focused test over the invocation contract), while leaving the `project_uplift` / `seed_migration_inventory` shims as transparent forwarders whose fate is tied to a future relocation.

## What Still Stays Shared-Boundary

- The `audit_refmap.py` payload body itself, because its repo-local path grammar and absolute-path regex preserve the current host's audit-workspace shape.
- The overwrite-family workflow and wrapper carriers named in `harness_modifier/overlay/ROSTER.md` that still reference helper homes (`progress.md`, `resume-project.md`, `transition.md`, and the skill wrappers listed under `later`). Helper-home references in those bodies remain coupled to host planning/runtime consumers until those carriers earn their own source split.
- The default source root anchored at `tooling/portable-gsd/overlay/` inside the overlay manifest. Explicit `{mode, source}` indirection stays the typed, sparse widening mechanism; the default root stays stable until more carriers have earned separate source homes.
- Overwrite-mode source-indirection readiness, which the 150 pass explicitly held open and which this reread does not earn forward.
- The planning-output policy inside `project_uplift.py` (`.planning/UPLIFT-*` paths, `.planning/STATE.md` read, `tooling/codex/UPLIFT-HELD-LATER.md` pointer). Until that policy is made data-driven, the payload is a modifier-facing candidate but not a modifier-relocatable one.
- Observed-basis versus held-annotation posture for `.codex` and `.claude` inside `harness_modifier/compatibility/declaration.json` and all consumers of `RUNTIME_BASIS_DECLARATION` / `RUNTIME_HELD_ANNOTATIONS_DECLARATION`. Helper-payload movement must inherit that posture, not re-invent it.

## What No Longer Needs To Be Re-Litigated

- Whether source authority and install target can separate inside one manifest. 148 already proved that for the specialist workflow/skill tranche; this reread does not reopen it.
- Whether the specialist trio was the right first filesystem-rehome set. That classification is settled.
- Whether the existence of helper shims already earns payload relocation. 150 declined that inference, and this reread sharpens the decline with per-helper evidence instead of overturning it.
- Whether `audit_refmap.py` should be read as a "slightly host-coupled but otherwise modifier-facing" helper. It should not. Its repo-local path grammar is load-bearing, not cosmetic, and the helper belongs to a different family than `project_uplift` / `seed_migration_inventory`.
- Whether `seed_migration_inventory.py` could move independently of `project_uplift.py`. It cannot, because its imports are structural.
- Whether the shim layer is uniformly temporary or uniformly permanent. It is neither; it is a mixed answer whose split is now named rather than ambient.

## Recommended Next Slice

- Write one bounded artifact only: a helper-payload authority map under `harness_modifier/overlay/helpers/` (for example a `AUTHORITY-MAP.md`) that records the per-helper classification above as the governing local basis. Shape:
  - per-helper rows for `project_uplift.py`, `seed_migration_inventory.py`, `audit_refmap.py` with columns for **source-of-payload**, **shim-lifetime class**, **modifier-facing posture**, **blockers to relocation**, **family**.
  - an explicit line declaring `audit_refmap.py` out of the later-payload-movement candidate set and into a separate repo-local audit-tooling family whose shim is the long-lived interface.
  - an explicit line declaring `seed_migration_inventory.py` downstream of `project_uplift.py` so any future movement is not re-opened as an independent slice.
  - a named neutralization precondition list for `project_uplift.py` (runtime-dir set as data, planning-output paths as data, compatibility-anchor routing via declaration rather than constants). No relocation in this slice.
- Refresh `harness_modifier/overlay/ROSTER.md` only where the authority map changes a current carrier's declared posture; do not widen the roster into a second filesystem tranche.
- Add one row to `.planning/HARNESS-IMPROVEMENT-REGISTER.md` under the extraction / uplift family line noting the authority-map landing, so the distinction between payload-candidate helpers and shared-boundary helpers does not dissolve back into one umbrella bucket.
- Keep the slice anti-threshold in formulation. The artifact is not a gate that helpers "pass" or "fail"; it is a directional map of what broadened at the shim layer, where payload authority still thins, and what would have to be made data-driven before payload movement earns its next slice.

## Held Later

- Actual helper-payload relocation for any of the three files. `project_uplift.py` movement depends on the neutralization precondition list being landed first; `seed_migration_inventory.py` movement depends on `project_uplift.py`; `audit_refmap.py` movement is not queued at all inside this family.
- Default-source-root migration inside the overlay manifest.
- Overwrite-mode source-indirection readiness slice.
- A second overlay filesystem tranche, whether generic or shared-boundary.
- Overwrite-family source split for workflow / template / reference carriers still listed `later` in `ROSTER.md`.
- Compact-prompt body split, runtime / agent / config tranche, host-local compact-prompt reclassification.
- Standalone repo boundary design, npm / `npx` packaging route, and any second-host exercise. These remain outside this lane's horizon.
- Any broader `.claude` install / materialization widening beyond the held-annotation posture already in the compatibility declaration. The runtime horizon for this family stays `.codex` observed basis plus `.claude` held annotation.

## Exact Next Move

1. Draft the bounded helper-payload authority-map artifact described in **Recommended Next Slice**, with per-helper classification rows, the explicit reclassification line for `audit_refmap.py`, the explicit downstream line for `seed_migration_inventory.py`, and the named `project_uplift.py` neutralization precondition list.
2. Update `harness_modifier/overlay/ROSTER.md` where the authority map changes a current carrier's declared posture, and add one row to `.planning/HARNESS-IMPROVEMENT-REGISTER.md` under the extraction / uplift family so the per-helper split is durable outside this audit subtree.
3. Refresh governed state (this extraction-audit's `README.md`, `CURRENT-STATE.md` Active Baselines for this family, and `STATUS.md`) so the next queued object reads as the `project_uplift.py` neutralization slice — not a relocation, not a second filesystem tranche, not an overwrite-family exercise, not a standalone or distribution move.
4. Only after that authority map is inherited, open a separate bounded proposal for the `project_uplift.py` neutralization precondition slice. Do not roll the neutralization work into this lane.
