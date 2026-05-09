# Phase 9 — Codex Skill Mirrors

ID: `09-codex-skill-mirrors`
Status: `pending`
Dependencies: Phase 8 complete
Approval gates: operator decides architectural direction (entry decision)

## Objective

Resolve the "codex skill mirrors" architectural question: should the modifier overlay continue to overwrite the codex `skills/gsd-*/SKILL.md` files (which are post-conversion synthesis from upstream's `commands/gsd/*.md`), or should the overlay reach pre-conversion (`commands/gsd/*.md`) and let upstream's installer synthesize the codex skill output?

## Rationale

This is the deepest structural question in the migration. Per intervention-strategies §4.7 and §7.7:

- Today: modifier overlays `skills/gsd-X/SKILL.md` directly, **after** upstream's installer has synthesized that file from `commands/gsd/X.md` via `convertClaudeCommandToCodexSkill()` in `bin/install.js`.
- Alternative: modifier overlays `commands/gsd/X.md` (pre-conversion), and upstream's installer synthesizes the codex form. This is more architecturally honest (modifier owns the source; upstream owns the conversion) but requires injecting modifier content **before** upstream's installer runs.

The current install flow runs modifier's overlay AFTER upstream's installer. Reversing or interleaving requires nontrivial infrastructure work. The alternative may not be worth the cost.

The phase decides. Two outcomes are pre-authorized:

- **Outcome A**: keep skill mirrors as `mode: overwrite` of `skills/gsd-X/SKILL.md`. Document the architectural boundary. Note that for these carriers, modifier accepts content-drift risk.
- **Outcome B**: migrate to overlay of `commands/gsd/X.md` (pre-conversion). Requires install-flow restructuring; substantially more work.

## Approach

Three slices. Slice 1 produces the architectural-direction artifact (a structured decision doc). Slice 2 records the outcome. Slice 3 is the phase debrief.

If the operator chooses Outcome A, this phase is short (just documentation). If Outcome B, this phase opens a sub-initiative for install-flow restructuring — but the restructuring itself is a Phase 9 child, not a separate initiative.

The phase plan only commits to Outcome A as a default. Outcome B requires explicit operator authorization with scope acknowledgment.

## Slice Catalog

### Slice 1 — Architectural-direction analysis

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/ADR-002-codex-skill-mirror-direction.md`
- **Required content**:
  - **Context**: cite intervention-strategies §4.7 and §7.7
  - **Outcome A** (keep mirroring): pros, cons, effort, risks
  - **Outcome B** (pre-conversion overlay): pros, cons, effort, risks
  - **Cost analysis**: A = ~½ day documentation; B = several weeks (install-flow change is substantial)
  - **Risk analysis**:
    - Outcome A's risk: skill mirror content drifts as upstream changes converters or commands/gsd/ files
    - Outcome B's risk: install-flow restructuring touches `scripts/setup-portable-gsd-runtime.sh` which is install-bootstrap critical
  - **Recommendation**: typically Outcome A unless concrete operator-stated need for Outcome B exists
  - **Reversibility**: Outcome A is reversible (could move to B later); Outcome B is reversible but expensive
  - **Affected carriers**: which skill mirrors are at issue (the 7 codex-only `skills/gsd-*/SKILL.md` overwrites that aren't `gsd-do`/`gsd-from-gsd2`/`gsd-plant-seed` — those were reclassified in Phase 0; this phase covers `gsd-discuss-phase`, `gsd-explore`, `gsd-health`, `gsd-plan-phase`, `gsd-resume-work`, `gsd-review`, `gsd-update`)
- **Verification**: per-slice gates
- **Commit**: `docs(initiative): ADR-002 codex skill mirror direction analysis`

### Slice 2 — Operator decision and outcome record

This slice is paused-for-approval until operator picks Outcome A or B.

- **Status**: `[ ]`
- **Write set varies**:
  - Outcome A: `.planning/initiatives/inject-migration/decisions/ADR-002-decision-A.md` → CREATE (records the operator's choice; cites architectural reasoning)
  - Outcome B: `.planning/initiatives/inject-migration/decisions/ADR-002-decision-B.md` → CREATE (records choice plus opens sub-initiative; the sub-initiative work is then planned as Phase 9 children — additional slices)
- **Verification**:
  - Per-slice gates
  - The chosen outcome's downstream implications recorded explicitly
- **Commit**:
  - Outcome A: `docs(initiative): record outcome A (mirror retention) for ADR-002`
  - Outcome B: `docs(initiative): record outcome B (pre-conversion overlay) for ADR-002 with sub-initiative scope`

### Slices 3-N (only if Outcome B)

If Outcome B, additional slices for the install-flow restructuring work:

- Slice 3: design install-flow change (where does modifier inject pre-conversion?)
- Slice 4: implement install-flow extension in `scripts/setup-portable-gsd-runtime.sh`
- Slice 5: migrate one skill mirror as proof-of-concept
- Slice 6: migrate remaining skill mirrors (multiple sub-slices)
- Slice 7: phase debrief

These slices are spec'd within Phase 9 only after Outcome B is chosen. The phase plan does NOT pre-spec them.

### Final slice — Phase debrief

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/PHASE-09-debrief.md`
- **Required**: outcome chosen; rationale; carriers affected; lessons; recommendations for Phase 10
- **Commit**: `docs(initiative): phase 09 debrief and codex skill mirror outcome`

## Exit Criteria (phase boundary)

If Outcome A:
1. ADR-002 + decision-A artifact exist
2. Phase debrief written
3. Skill mirrors stay as `mode: overwrite`; no manifest changes
4. Bootstrap gate stays green; `hard_failures: []`
5. STATE.md → Phase 9 `[x]`; advance to Phase 10

If Outcome B:
1. ADR-002 + decision-B artifact exist
2. Sub-initiative slices completed; skill mirrors migrated to pre-conversion overlay
3. Install flow extended and tested under both runtimes
4. Phase debrief written
5. Bootstrap gate green; `hard_failures: []`
6. STATE.md → Phase 9 `[x]`; advance to Phase 10

## Boundary

- This phase resolves the codex skill mirror architectural question. It does NOT migrate any carrier under `mode: inject` for additive content (that was Phases 4–8).
- Outcome B's install-flow change is bounded: only the addition of pre-conversion injection. No broader install-script refactor.
- This phase does NOT touch claude-side skill routing (claude consumes `commands/gsd/*.md` directly; no synthesis); claude skill carriers stay as is.

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Outcome A locks in content-drift risk for the codex skill mirrors | accepted | low (drift is observable; can revisit later) | the ADR-002 explicitly accepts this; Phase 10 closeout records it |
| Outcome B's install-flow change breaks the bootstrap gate | medium | high (initiative blocked) | per-slice gates plus harness_canary at sub-initiative phase boundary; rollback the install-flow change if needed |
| Outcome B underestimated; sub-initiative drags on | high | medium | the operator decides at Slice 2; if effort exceeds the original estimate, fall back to Outcome A |
| The seven affected skill mirrors have differently-shaped diffs from upstream, making bulk migration hard | medium | low | per-carrier slice in Outcome B's sub-initiative |

## Notes For Future Iterations

- Outcome A is the more common choice; it's the default if the operator doesn't have a strong preference for Outcome B.
- If Outcome B is chosen and the sub-initiative drags, the operator may pause the entire initiative and resume later; the loop preserves state correctly.
