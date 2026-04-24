# Harness Intervention Update Lane

Date: 2026-04-20
Status: probe findings landed

## Purpose

- [d:r:i] This artifact corrects the frame that had begun to over-center `R5.18`.
- [d:r:i] The governing question is broader: can the strengthened docs, mappings, and newer upstream/runtime deltas be turned into better onboarding for planning repo-local harness interventions that improve both near-term work quality and longer-horizon management across complex design landscapes?

## Frame Correction

- [e:c+i] The earlier bridge audit did not conclude `docs are enough` or `R5.18 is the whole point`. It concluded `revise + guarded hybrid reseed`: no docs-only restart, no no-change preserve, and no silent substitution of upstream docs for local intervention doctrine. Sources: [SYNTHESIS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:5), [SYNTHESIS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:7), [SYNTHESIS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:11).
- [e:c+i] The Wave-1 mapping lane later sharpened the question further: the real target is `intervention-ready mapping`, not just whether readiness mapping roughly matched docs. It explicitly asked what still separates current mapping from intervention-ready mapping and rejected any `docs quality = runtime adequacy` shortcut. Sources: [03-mapping-adequacy-and-comparative-mapping-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/wave-1/specs/03-mapping-adequacy-and-comparative-mapping-spec.md:14), [03-mapping-adequacy-and-comparative-mapping-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/wave-1/specs/03-mapping-adequacy-and-comparative-mapping-spec.md:27).
- [e:c+i] That lane's actual result was a map that stayed directionally useful but still left important surfaces under-mapped, including the runtime-authoritative `.toml` worker plane, the router / side-entry plane, and the installer / overlay / runtime materialization chain. Sources: [03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/wave-1/outputs/03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md:12), [03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/wave-1/outputs/03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md:49), [03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/wave-1/outputs/03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md:67).
- [d:r:i] So `R5.18` remains one bounded obstruction and proof surface, but not the sovereign target. The larger target is harness intervention planning across the ecosystem.

## Three Baselines

### 1. Current Repo-Local Pinned Runtime

- [e:c+i] The active repo-local install path still materializes regular local GSD via `npx get-shit-done-cc --codex --local`, then reapplies the tracked repo overlay from `tooling/portable-gsd/overlay/` into `.codex/`. Sources: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:18), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:20), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:24).
- [e:c+i] The active readiness/audit work has been operating against a pinned `v1.36.0` upstream baseline for the docs crosswalk and early comparison work. Source: [lane-02-docs-vs-readiness-crosswalk.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-02-docs-vs-readiness-crosswalk.md:15).

### 2. Updated Docs Branch

- [e:c+i] The local upstream working clone still carries the cumulative docs-refresh branch at `docs/pr4-consistency-drift-guards` (`84c5e1b`), while the fork remote has the newer `docs/pr4-consistency-drift-guards-r2` at `4f3de80`. These are docs/testing branches, not the repo's live release branch. Source: local git refs refreshed on 2026-04-20.
- [e:r:i] The docs-refresh family still matters because it introduced the strongest inventory / drift-guard posture we have seen: authoritative surface inventory, explicit broad-doc drift tests, and stronger docs parity discipline.

### 3. Current Upstream Main / Release

- [e:r:i] Ref refresh on 2026-04-20 shows the upstream repo has moved materially past the pinned baseline: `origin/main` is now `ebbe74d`, `origin/hotfix/1.38.1` exists, and `origin/release/1.39.0` exists.
- [e:r:i] This means the decision is no longer just whether to inherit a docs PR. It is whether and how to reconcile the pinned local runtime, the forked docs-refresh branch, and materially newer upstream code/install/runtime surfaces.

## Isolated Latest-Install Probe

- [e:c+i] At the 2026-04-20 probe boundary, the active repo-local `.codex/` was already on `v1.38.1`, not still on the earlier `v1.36.0` docs-crosswalk baseline. Sources: [.codex/get-shit-done/VERSION](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/VERSION:1), [.codex/gsd-file-manifest.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-file-manifest.json:2).
- [e:r:i] A detached probe worktree was created at `/tmp/prix-guesser-gsd-update-probe`, and the real local installer path `./scripts/setup-portable-gsd.sh` was run there on 2026-04-20. The install materialized `Get Shit Done v1.38.1`, not a newer published runtime.
- [e:r:i] After path normalization, the active repo `.codex/` and the fresh probe `.codex/` differ semantically in only two files: `config.toml` and `gsd-file-manifest.json`.
- [e:r:i] The substantive `config.toml` delta is repo-local and deliberate: the active repo keeps `model_reasoning_effort = "xhigh"` while the fresh install default is `high`.
- [e:r:i] The `gsd-file-manifest.json` delta is not a live-surface drift signal. Both manifests report `version: 1.38.1`, but the active manifest carries many hashes that do not match the current on-disk files even though those files match the fresh probe after path normalization.
- [o:r:i] This strongly suggests a tooling/manifest coherence issue in the install-plus-overlay flow: the manifest is not yet a trustworthy summary of the final materialized local state once repo-local overlay/patched carry is reapplied.

## What The Docs Branch Still Adds

- [e:r:i] Relative to the current upstream `1.38.1` line, the docs-refresh branch is not a proxy for current shipped truth. It is missing many surfaces now present in `1.38.1`, including `ingest-docs`, `sketch`, `spike`, `ultraplan-phase`, `mandatory-initial-read`, and several newer references/workflows.
- [e:r:i] The same comparison shows the docs-refresh branch still carries one especially valuable thing that current shipped docs do not: the stronger `docs/INVENTORY.md` + parity/consistency-guard posture as a first-class docs-governance model.
- [e:r:i] The live upstream delta beyond `1.38.1` is currently small at the branch level we can inspect locally: `origin/release/1.39.0` differs from `origin/hotfix/1.38.1` only in `get-shit-done/bin/gsd-tools.cjs`.
- [d:r:i] So the current opportunity is not `install a dramatically newer runtime immediately`. The stronger opportunity is to convert the docs-refresh branch's inventory/parity discipline into intervention onboarding for the actual current harness surfaces.

## Why The Earlier Comparison Is Not Enough

- [e:c+i] The bridge crosswalk explicitly left docs-vs-runtime drift unresolved. Source: [lane-02-docs-vs-readiness-crosswalk.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-02-docs-vs-readiness-crosswalk.md:142).
- [e:c+i] The Wave-1 mapping output later found that the strongest live counter-pressure came from runtime-authority drift and the materialization chain, not from broad-doc prose quality alone. Sources: [03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/wave-1/outputs/03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md:15), [03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/wave-1/outputs/03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md:109).
- [d:r:i] Therefore the missing object is not `another docs-vs-docs comparison`. It is a purpose-built intervention-onboarding layer that uses docs, runtime, overlay, installer, helpers, commands, skills, and agent contracts as distinct but related intervention surfaces.

## Intervention-Relevant New Surfaces

- [e:r:i] The updated docs/workflow world introduces or reinforces several surfaces that matter directly for long-horizon intervention planning:
  - authoritative shipped-surface inventory and docs drift guards
  - stronger inventory-backed architecture counts
  - newer installer/runtime behavior
  - newer command/workflow surfaces for spec-first work, ingest/import, and help/routing
  - newer SDK/runtime checks and hook/read-guard machinery
- [d:r:i] These are not automatically all `adopt now`. But they are all now candidates for the intervention map because they affect how the harness can be understood, updated, and governed over time.

## Governing Next Move

- [d:r:i] Do not treat the updated docs branch as equivalent to the latest upstream runtime.
- [d:r:i] Do not spend another cycle pretending the repo still needs a blind `latest install` just to know where it stands; the isolated probe already answered that question for the then-current `v1.38.1` boundary, and later live-version claims should defer to current runtime carriers.
- [g:r:i] The correct next sequence is:
  1. write the intervention-onboarding map from the now-completed three-way comparison: the then-active local `v1.38.1` probe boundary, the docs-refresh branch, and current upstream branch state
  2. include an explicit `declared vs effective authority` split for docs, installer, overlay, runtime, helpers, commands, skills, and agent contracts
  3. separate `adopt into repo-local harness`, `use only as onboarding/governance`, and `hold as future pressure`
  4. record the manifest-coherence issue as tooling debt rather than silently trusting manifest hashes as runtime truth
  5. only then decide whether any additional repo-local harness mutation or upgrade is warranted

## Open Questions

- [o:r:i] Which additions on the then-current upstream `1.38.1` surfaces were direct candidates for repo-local harness intervention, and which were only docs/public-facing improvements?
- [o:r:i] Which of the docs-refresh branch's parity/consistency mechanisms should be copied into the repo-local intervention process even if the literal docs files are not?
- [o:r:i] Which local overlay patches or repo-local operating assumptions would silently flatten if the harness were later republished against a runtime newer than the `1.38.1` probe boundary without a fresh isolated probe first?
