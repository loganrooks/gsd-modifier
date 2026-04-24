Date: 2026-04-20
Status: local second-tranche disposition

# Manifest Semantic Contract Disposition

## Purpose

- [g:r:i] This note settles what the existing manifest-like surfaces are and are not allowed to mean before any install-path mutation is attempted.
- [d:r:i] The pressure here is not merely `hash mismatch`. It is semantic collapse: if we make one artifact stand in for both updater custom-file protection and final repo-local runtime truth, we will lose discriminating power exactly where this harness needs it most.

## What The Probe Changed

- [e:c+i] The earlier coherence proposal assumed the main unresolved choice was whether `gsd-file-manifest.json` should mean `base+overlay snapshot` or `final materialized runtime snapshot`. Sources: [03-manifest-install-coherence-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/03-manifest-install-coherence-proposal.md:22), [03-manifest-install-coherence-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/03-manifest-install-coherence-proposal.md:24).
- [e:c+i] The install path itself shows a three-stage sequence: upstream local install, tracked overlay materialization with placeholder substitution, then repo-local post-copy reasoning mutation. Sources: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:20), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:23), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:46).
- [e:c+i] The runtime tool surface then adds a stronger constraint: `detect-custom-files` uses `gsd-file-manifest.json` to decide which files inside GSD-managed directories count as user-added carry that must be protected before update wipes those directories. Sources: [.codex/get-shit-done/bin/gsd-tools.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/gsd-tools.cjs:1150), [.codex/get-shit-done/bin/gsd-tools.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/gsd-tools.cjs:1152), [.codex/get-shit-done/bin/gsd-tools.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/gsd-tools.cjs:1190), [.codex/get-shit-done/bin/gsd-tools.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/gsd-tools.cjs:1222), [.codex/get-shit-done/bin/gsd-tools.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/gsd-tools.cjs:1226).
- [e:c+i] The current manifest inventories upstream-style managed files such as `agents/gsd-planner.md`, while the live runtime also carries `.toml` agent contracts that are not present in the manifest keys. Sources: [.codex/gsd-file-manifest.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-file-manifest.json:312), [.codex/agents/gsd-planner.md](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-planner.md:1), [.codex/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-planner.toml:1).
- [e:c+i] The tracked backup metadata is narrower again: it explicitly records a selected carried subset anchored to an upstream baseline, not a full live-runtime roster. Sources: [.codex/gsd-local-patches/backup-meta.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:2), [.codex/gsd-local-patches/backup-meta.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:4), [.codex/gsd-local-patches/backup-meta.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:21), [.codex/gsd-local-patches/backup-meta.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:30).
- [e:r:i] A direct local probe of `node .codex/get-shit-done/bin/gsd-tools.cjs detect-custom-files --config-dir .codex` currently returns fifty custom files, including all agent `.toml` files, repo-local hooks, and `gsd-rigorous-research` skill files. That result only makes sense if the manifest is preserving an upstream/custom boundary rather than claiming to be a complete final-runtime inventory.

## Disposition

### 1. Preserve `gsd-file-manifest.json` As An Upstream-Inventory / Update-Boundary Artifact

- [d:r:i] `gsd-file-manifest.json` should **not** be redefined as the final repo-local runtime snapshot.
- [d:r:i] Its active operational role is narrower and more important:
  - it inventories the installer-managed upstream payload
  - it gives update tooling a boundary for what counts as user-added/custom carry inside wiped directories
- [d:r:i] If we rewrite that file after overlay carry and repo-local post-copy mutation, we will blur or erase the updater’s ability to distinguish upstream inventory from repo-local additions.

### 2. Preserve `backup-meta.json` As A Tracked Carried-Subset Metadata Surface

- [d:r:i] `backup-meta.json` is not the full runtime truth surface either.
- [d:r:i] Its job is to remember which selected files the repo intentionally carries against an upstream baseline, together with the pristine hashes that make later reapplication and comparison possible.
- [d:r:i] That narrower role remains useful and should stay explicit.

### 3. Admit That Final Materialized Runtime Truth Still Lacks Its Own Durable Artifact

- [d:r:i] The final live runtime is currently legible through a combination of:
  - the install script
  - tracked overlay canon
  - repo-local post-copy mutations
  - live `.codex/` inspection
  - proof/disposition notes
- [d:r:i] That is enough to reason from, but it is not yet the strongest available visibility surface.
- [d:r:i] So the real missing object is not `regenerate the existing manifest after install`. The real missing object is a **separate** repo-local materialized-runtime visibility surface that does not sabotage update-boundary semantics.

## What This Revises

- [d:r:i] This note revises the earlier either/or framing in [03-manifest-install-coherence-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/03-manifest-install-coherence-proposal.md:22) and [03-manifest-install-coherence-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/03-manifest-install-coherence-proposal.md:24).
- [d:r:i] The earlier either/or framing was too coarse.
- [d:r:i] The corrected contract is:
  - preserve the existing manifest as upstream/update-boundary truth
  - preserve backup metadata as tracked carried-subset truth
  - add a separate final-runtime visibility artifact later if stronger materialization truth is needed

## Consequences For The Second Tranche

- [d:r:i] Do **not** patch `scripts/setup-portable-gsd.sh` to rewrite `gsd-file-manifest.json` after overlay application or repo-local reasoning defaults.
- [d:r:i] Do **not** treat overlay/live templating and post-copy mutation as a manifest-staleness bug by default.
- [d:r:i] Reframe manifest/install coherence as a two-surface problem:
  - update-boundary truth
  - final materialized runtime truth
- [d:r:i] The drift-register pilot now becomes more valuable, not less, because it is already helping classify which live differences belong to materialization carry, repo-local config carry, or selective overlay scope.

## Ceremony Risk Check

- [d:r:i] This disposition fails if it gets paraphrased into `leave the manifest alone` without also carrying the second half of the pressure: a stronger final-runtime visibility artifact is still missing.
- [d:r:i] It also fails if a later implementation quietly reintroduces the semantic collapse by using one file to stand in for both updater boundary and materialized runtime truth.

## Immediate Next Move

- [g:r:i] Draft the bounded follow-through that this note now authorizes: a separate repo-local materialized-runtime visibility proposal or verifier surface that can coexist with the current updater/custom-file manifest rather than replacing it.
