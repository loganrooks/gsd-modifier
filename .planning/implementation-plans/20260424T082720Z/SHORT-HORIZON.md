# Short-Horizon Plan

Date: 2026-04-24
Status: detailed short-horizon draft

## Goal

Produce a deployable `gsd-modifier` bridge harness that can support early `prix-guesser` development without foreclosing later migration to a richer `harness-studio` operating model.

## Design Principles

- Treat GSD as execution logistics, not the sovereign product ontology.
- Preserve product strategy, long-horizon intent, workflow lanes, feedback loops, release posture, and risk decisions as portable artifacts.
- Treat Codex/Claude parity as shared outcomes with runtime-specific carriers, not identical files.
- Prefer explicit inventories and contracts over hidden convention.
- Keep verification materialized-runtime-aware, not source-only.
- Keep commits semantically bucketed so later auditors can reconstruct why each change happened.

## Workstream 1: Runtime Intervention Surface Inventory

Purpose: make every load-bearing runtime intervention seam visible before changing behavior.

Surfaces to inventory:

- `AGENTS.md`
- `.planning/AGENTS.md`
- `CLAUDE.md`
- `.planning/CLAUDE.md`
- Codex compact prompt file and `experimental_compact_prompt_file`
- `.codex/config.toml`
- `.codex/agents/*.toml`
- `.codex/skills/*`
- `.codex/get-shit-done/workflows/*`
- `.codex/get-shit-done/references/*`
- `.claude` runtime equivalents
- `harness_modifier/uplift/carrier_catalog.json`
- generated project onboarding docs
- installer/materialization scripts

Deliverables:

- `docs/runtime-intervention-surfaces.md`
- parity posture table:
  - shared core outcome
  - Codex-specific carrier
  - Claude-specific carrier
  - generated or hand-maintained
  - materialization check
  - known gap or deferred question

Audit questions:

- Which surfaces directly affect runtime behavior?
- Which surfaces only provide human/operator guidance?
- Which surfaces are generated?
- Which surfaces are preserved across reinstall/update?
- Which surfaces must diverge by runtime?
- Which divergences are currently untested?

## Workstream 2: Instruction-Surface Generation And Parity

Purpose: understand and improve how project-level instructions are generated and maintained.

Known starting evidence:

- current local scan found `new-project.md` using `AGENTS.md` in the instruction-generation path
- uplift carrier catalog already knows about `AGENTS.md`, `.planning/AGENTS.md`, `CLAUDE.md`, and `.planning/CLAUDE.md`
- Codex agents currently privilege `AGENTS.md` and explicitly do not treat `CLAUDE.md` as governing truth for Codex

Deliverables:

- audit note on current `new-project` instruction generation
- decision record for instruction-surface parity:
  - keep `AGENTS.md` as shared or Codex primary
  - generate `CLAUDE.md` as Claude-facing mirror or companion
  - decide `.planning/AGENTS.md` / `.planning/CLAUDE.md` relationship
  - define conflict handling when both exist

Pitfalls:

- false parity by copying text into both files even when runtime semantics differ
- hidden divergence where generated docs differ but no verifier catches it
- treating `CLAUDE.md` as Codex authority or `AGENTS.md` as Claude authority without explicit runtime behavior

## Workstream 3: Compact Prompt And Runtime-Specific Capability Surfaces

Purpose: support runtime-native advantages without breaking parity.

Codex-specific known surface:

- `experimental_compact_prompt_file` in `.codex/config.toml`

Potential Claude-specific surfaces:

- `CLAUDE.md`
- Claude project memory/instructions behavior
- hooks or tool restrictions if available in the relevant Claude runtime

Deliverables:

- runtime capability comparison note
- explicit contract for compact-prompt behavior:
  - what Codex gets
  - what Claude gets instead, if anything
  - how absence is documented
  - how materialization verification detects the configured path

Pitfalls:

- blocking shared bridge-harness release on perfect runtime symmetry
- silently treating a Codex-only enhancement as cross-runtime behavior
- letting runtime-specific features leak into runtime-neutral `.planning/` artifacts

## Workstream 4: Bridge-Harness Governance Artifact Seeding

Purpose: define which project-level artifacts a serious project should receive at onboarding/uplift time.

Candidate artifacts:

- `PROJECT.md`
- `LONG-ARC.md`
- `OPERATING-MODEL.md`
- `PRODUCT-THESIS.md`
- `WORKFLOW-LANES.md`
- `DECISION-LOG.md`
- `FEEDBACK-LOOPS.md`
- `RELEASE-PLAN.md`
- `RISK-REGISTER.md`
- `QUALITY-BAR.md`

Deliverables:

- governance artifact proposal
- seed/update policy:
  - create when absent
  - detect when stale
  - never overwrite without explicit consent
  - generate proposals for doctrine-sensitive changes
- `LONG-ARC.md` disposition note:
  - keep
  - split
  - generalize
  - replace

Pitfalls:

- too many artifacts for small utility projects
- heavyweight process before project classification exists
- overwriting bespoke project docs
- assuming `prix-guesser` needs define all projects' defaults

## Workstream 5: Prix Bridge Contract

Purpose: define how early `prix-guesser` should use the bridge harness.

Deliverables:

- `docs/prix-bridge-harness-contract.md` or equivalent
- lane declaration format for early phases/milestones
- minimum portable artifacts for product/game work:
  - product thesis
  - game-loop spec
  - design brief
  - feedback loop plan
  - release/readiness notes
  - risk register

Pitfalls:

- turning `prix-guesser` into the universal case
- letting phase completion stand in for product learning
- making future `harness-studio` migration depend on GSD internals

## Workstream 6: Verification And Release Readiness

Purpose: close the bridge-harness release boundary with material evidence.

Required verification:

- `python3 -m py_compile ...` for touched Python files
- focused unit tests for touched tooling
- `python3 tooling/codex/audit_refmap.py map ...` for audit reference health
- `./scripts/setup-portable-gsd-runtime.sh --runtime both`
- `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --strict`
- `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict`
- `bash scripts/ci/check-deterministic.sh`
- `bash scripts/ci/check-bootstrap.sh`
- `git diff --check`

Optional but release-relevant:

- host exercise matrix after shipped/runtime-facing changes
- `runtime_visibility.py`
- `manifest_install_coherence.py`
- `harness_canary.py`

## Recommended Sequence

1. Stabilize the current audit import and `audit_refmap.py`.
2. Commit the stabilized import/tooling/docs buckets.
3. Create runtime intervention surface inventory.
4. Audit instruction-generation and compact-prompt parity.
5. Draft governance artifact seeding proposal.
6. Draft `prix-guesser` bridge contract.
7. Run repo-self dual-runtime proof.
8. Decide whether to cut a short-term deployable release or do one more hardening slice.

