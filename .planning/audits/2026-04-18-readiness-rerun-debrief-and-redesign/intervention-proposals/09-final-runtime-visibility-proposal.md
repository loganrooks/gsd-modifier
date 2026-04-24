Date: 2026-04-20
Status: draft bounded proposal

# Final Runtime Visibility Proposal

## Purpose

- [g:r:i] This proposal defines the missing second-tranche object named by [08-manifest-semantic-contract-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/08-manifest-semantic-contract-disposition.md:1): a separate visibility surface for the final repo-local runtime that does not overwrite updater/custom-file boundary truth.
- [d:r:i] The goal is stronger intervention carry, not a prettier diff. Future harness work should be able to see what the live runtime actually carries after install, overlay materialization, and repo-local mutation without confusing that question with update-protection semantics.

## Why This Proposal Exists

- [e:c+i] The drift-register pilot already shows that sampled high-leverage differences are mostly intelligible as materialized carry, repo-local config carry, or selective overlay boundary rather than as mystery drift. Sources: [07-live-vs-overlay-drift-register-pilot.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/07-live-vs-overlay-drift-register-pilot.md:19), [07-live-vs-overlay-drift-register-pilot.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/07-live-vs-overlay-drift-register-pilot.md:36).
- [e:c+i] The new semantic contract then clarifies why the existing manifest cannot simply be repurposed to express that truth: it is already serving updater/custom-file boundary logic, while `backup-meta.json` serves tracked carried-subset metadata. Sources: [08-manifest-semantic-contract-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/08-manifest-semantic-contract-disposition.md:12), [08-manifest-semantic-contract-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/08-manifest-semantic-contract-disposition.md:23).
- [e:c+i] The runtime/materialization companion already identified the missing operational seam: final live truth is currently reconstructed across install script, overlay canon, post-copy mutation, live `.codex/` inspection, and proof notes. Sources: [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:21), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:61).

## Bounded Scope

- [d:r:i] Start with the same high-leverage families already used by the drift pilot:
  - `.codex/config.toml`
  - `.codex/agents/*.toml`
  - selected `.codex/get-shit-done/workflows/*`
  - selected `.codex/get-shit-done/references/*`
  - selected `.codex/get-shit-done/bin/lib/*`
- [d:r:i] Do not widen the first pass into a total `.codex/` inventory, a package manager, or a full updater replacement.

## Proposed Move

### 1. Add A Separate Runtime-Truth Command Or Artifact

- [d:r:i] Create a repo-local visibility surface that reports final runtime truth **after**:
  - upstream install
  - overlay materialization
  - repo-local post-copy mutation
- [d:r:i] This can take one of two bounded forms:
  - an on-demand verifier/snapshot command
  - a generated local artifact in ignored `.codex/`
- [d:r:i] The critical requirement is semantic separation, not one storage format over another.

### 2. Carry Classification, Not Bare Mismatch

- [d:r:i] Reuse the drift-register classes as first-class output:
  - `intentional materialized carry`
  - `repo-local config carry`
  - `selective overlay boundary`
  - `unknown live drift`
  - `obsolete live residue`
- [d:r:i] A stronger surface must say what kind of difference the runtime carries, not merely that two files differ.

### 3. Keep Updater-Boundary Truth Separate

- [d:r:i] The new visibility surface must not replace `gsd-file-manifest.json`.
- [d:r:i] It should coexist with:
  - upstream/update-boundary manifest truth
  - tracked carried-subset backup metadata
  - final runtime truth

### 4. Make It Useful For Intervention Planning

- [d:r:i] The first version should answer questions like:
  - which high-stakes runtime surfaces differ from tracked overlay canon for intelligible reasons
  - which differences are repo-local carry versus unexplained drift
  - which surfaces would need to move into tracked overlay canon if we want stronger persistence
  - which surfaces should remain explicitly local

## Explicit Non-Goals

- [d:r:i] Do not rewrite `gsd-file-manifest.json`.
- [d:r:i] Do not pretend this new surface can replace semantic review of live behavior.
- [d:r:i] Do not attempt full `.codex/` exhaustiveness before the high-leverage families become easier to carry and reason about.

## Why This Shape Is Stronger

- [d:r:i] It preserves the update workflow’s custom-file boundary instead of accidentally erasing it.
- [d:r:i] It gives later intervention lanes a more direct handle on final runtime truth than the current combination of manual inspection and scattered proof notes.
- [d:r:i] It lets manifest/install coherence become a discriminating multi-surface problem rather than a one-file fetish.

## Success Signals

- [d:r:i] A later reviewer can tell, from one bounded surface, what the final runtime is carrying in the high-leverage families and why.
- [d:r:i] Future updater/install work no longer has to overload `gsd-file-manifest.json` to answer runtime-truth questions it was not designed to answer.
- [d:r:i] Proposal decisions about overlay expansion, local carry, and drift cleanup become faster and less error-prone.

## Ceremony Risk Check

- [d:r:i] This proposal fails if it becomes another static report no later intervention uses.
- [d:r:i] It also fails if it quietly becomes a second opaque manifest with no classification, rationale, or clear relation to overlay canon.

## Next Disposition Question

- [g:r:i] The next decision on this proposal should be whether to implement the first version as an on-demand verifier/snapshot command, an ignored generated artifact, or a small paired command-plus-artifact pattern.
