# Checkpoint 5 R5.18 Versus 2026-04-15 Governance Audit L2 Lifecycle / LONG-ARC Comparison Internal R1

## Research Frame

- Mode: `synthesis`
- Question:
  - are the historical lifecycle / `LONG-ARC` carry-forward concerns now being addressed by current Checkpoint 5 / `R5.18`, only partially carried, or still missing?
- Scope:
  - non-phase lifecycle doctrine carry-forward
  - `LONG-ARC` uptake outside active phase planning
  - `progress` / `transition` / `complete-milestone` / init-path continuity
- Non-goals:
  - do not evaluate Git / CI / remote-review concerns except where the monolithic comparison used them to grade lifecycle carry-forward or where they directly affect lifecycle continuity
- Stop condition:
  - split the historical lifecycle concern family into the subfamilies the current checkpoint can actually own
  - classify each subfamily using the required status set
  - judge whether the monolithic comparison graded those lifecycle concerns accurately enough
- Scope-expansion note:
  - none. Broader governance families are mentioned only where the monolithic comparison imported them into lifecycle grading.

## Path Of Inquiry

- Entry point:
  - start from the historical lifecycle-specific weak-side map in `02` plus the lifecycle carry-forward synthesis in `06`, then compare that map against the current `R5.18` boundary and launch truth rather than against unstarted implementation.
- Branches considered:
  - keep the monolithic comparison's single lifecycle row
  - split lifecycle carry-forward into entry surfaces, mid-lifecycle routing surfaces, exit surfaces, and mechanism surfaces
  - grade only first-wave files
  - grade `Bucket 1`, `Bucket 2`, and `Bucket 3` separately
- Branches pursued:
  - split the historical concern into:
    - project / milestone entry carry-forward
    - progress / transition carry-forward
    - milestone-completion doctrine-delta handling
    - init-path / metadata continuity
    - auto-path permissiveness for doctrine-sensitive lifecycle work
  - compare those against `STATUS`, `TASKS`, the Checkpoint 5 gate, `R5.18` boundary/launch artifacts, `R5.19d4/e`, and the monolithic comparison
- Branches deferred or abandoned:
  - broader Git / CI / remote-review family adjudication
  - rereading raw `R5.19a/b/c` materials
  - any claim that `R5.18` has already corrected the live surfaces

## Assumptions Surfaced

- [a:r:i] `addressed_in_r5_18` means the concern is inside the current governing `R5.18` corrective frontier as direct patch-wave ownership or explicit scope-gating work, not that the fix is implemented.
- [a:r:i] `partially_addressed_boundary_only` means the concern has current boundary truth or adjacent treatment, but the lifecycle-specific surface itself is not fully owned as an active corrective lane.
- [a:r:i] `still_missing` means the historical concern is not a current `R5.18` owner and is not preserved as an explicit active lifecycle boundary with a named present-tense route.

## Artifacts Read

### Governing Current Docs

1. `AGENTS.md`
2. `.planning/AGENTS.md`

### Historical

3. `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
4. `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
5. `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md`

### Current Readiness / Comparison Surface

6. `.planning/readiness/phase-01-rerun/STATUS.md`
7. `.planning/readiness/phase-01-rerun/TASKS.md`
8. `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md`
9. `.planning/readiness/phase-01-rerun/PROTOCOL.md`
10. `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md`
11. `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md`
12. `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md`
13. `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18d-integration-and-review-prep-launch-spec.md`
14. `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md`
15. `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19e-adjudication-reread-internal-r1.md`
16. `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-internal-r1.md`

## Historical Concern Family

- [e:c:i] The 2026-04-15 lifecycle lane did not identify one generic `LONG-ARC gap`; it identified a linked lifecycle chain with distinct weak points:
  - project creation lacked first-class durable-doctrine scaffolding and generic templates lacked long-arc carry-forward pointers (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:175-177,233-237,253-256`).
  - milestone start lacked a carry-forward translation step from doctrine into milestone posture, seams, non-decisions, and reversal-sensitive boundaries (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:178-179,199-206,238-239`).
  - `progress` routing conflated `has context` with `is doctrine-grounded`, and `transition` lacked explicit doctrine triage (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:180-183,213-223,240-248`).
  - milestone completion lacked doctrine-delta review before archival finalization (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:182-183,225-231,247-248`).
  - lifecycle continuity also depended on cheap mechanism support that did not exist: permissive auto paths and init payloads with no doctrine metadata (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:184-189,258-275`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:340-347,406-415`).
- [e:c:i] The historical synthesis in `06` preserved the same shape. It described the repo as `phase-strong but lifecycle-weak`, named `new-milestone`, `progress`, `transition`, `complete-milestone`, and init plumbing as the weak-side set, and recommended current-stage patching of lifecycle carry-forward rather than later generic maturity work (`.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:339-347,406-417,451-454`).

## Current Treatment

### Direct Evidence

- [e:c:i] Current Checkpoint 5 remains a rerun-critical harness checkpoint whose active owned surfaces are runtime-authoritative worker alignment, review / closure-pressure follow-through, launch/model-truth capture, workflow-chain follow-through, and wrapper alignment after workflow changes (`.planning/readiness/phase-01-rerun/STATUS.md:28-33,63-69,91-95`; `.planning/readiness/phase-01-rerun/TASKS.md:9-15,24`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:96-107`).
- [e:c:i] Current `R5.18c` directly owns `progress.md` and `transition.md` as part of the convergent completion / routing / runtime-authority trunk (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:5-15`).
- [e:c:i] Current `R5.18` does not name `new-project.md`, `new-milestone.md`, `complete-milestone.md`, `templates/project.md`, or `templates/roadmap.md` anywhere in `Bucket 1`, `Bucket 2`, `Bucket 3`, or the split launch bundle (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:78-235`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md:21-63`).
- [e:c:i] Current `R5.18` does pull some lifecycle-adjacent mechanism surfaces into active boundary treatment:
  - `init.cjs` is a mandatory explicit-disposition runtime-control surface in `Bucket 2B` and a conditional addition to `R5.18c` (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:144-166`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:16-29`).
  - `summary.md` and the debt-carrier mechanism are explicit `Bucket 2B` / `Bucket 3` boundary items because completion semantics remain unresolved (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:146-148,167-175,183-201`).
- [e:c:i] Current governing doctrine does strengthen long-horizon compensation outside phase-local planning:
  - root `AGENTS.md` requires thinking across current phase, next milestone, and farther doctrine surfaces (`AGENTS.md:37-46,49-72`).
  - `.planning/AGENTS.md` requires future-flexibility statusing and explicit horizon handling (`.planning/AGENTS.md:79-112`).
  - but those are governing overlays, not lifecycle workflow ownership.

### Inference And Interpretation

- [d:c+r:i] Current lifecycle uptake is concentrated in mid-lifecycle rerun-critical routing surfaces, not in lifecycle-wide doctrine carry-forward.
- [d:c+r:i] The present checkpoint is materially stronger than `nothing`: `progress.md`, `transition.md`, `init.cjs`, `summary.md`, and debt-carrier semantics are inside current boundary truth. But the historical lifecycle lane asked for entry, routing, transition, completion, and metadata continuity together, and that full set is not what current `R5.18` owns.
- [d:c+r:i] Governance strengthening in `AGENTS.md` and `.planning/AGENTS.md` compensates for lifecycle weakness, but it does not convert missing lifecycle workflow ownership into `addressed_in_r5_18`.

### Unknowns

- [o:c:i] `R5.18a/b/c/d` has not started execution, so current lifecycle grading can only use boundary truth, not implemented owner truth (`.planning/readiness/phase-01-rerun/STATUS.md:91-95,204-206`; `.planning/readiness/phase-01-rerun/TASKS.md:24`).
- [o:c+r:i] `init.cjs`, `summary.md`, and the debt-carrier mechanism could be promoted more aggressively by `R5.18a`, but no current artifact does that yet.

## Where The Monolithic Comparison Was Right

- [d:c:i] It was right to grade the overall lifecycle / `LONG-ARC` concern as not fully absorbed by current `R5.18` and to say current uptake is rerun-critical rather than lifecycle-wide (`.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-internal-r1.md:102,118,126,142`).
- [d:c:i] It was right that `progress` / `transition` are the only clearly current lifecycle surfaces inside the split corrective frontier (`.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-internal-r1.md:102,118`).
- [d:c:i] It was right that no lifecycle concern family is `superseded`; the current package narrows and defers rather than replacing the old lifecycle diagnosis with a better closed answer (`.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-internal-r1.md:96,131-134`).

## Where The Monolithic Comparison Was Too Thin Or Too Broad

- [d:c+r:i] It was too thin because it collapsed the whole lifecycle concern into one row. That row hid a real status split:
  - `progress` / `transition` are directly inside `R5.18c`
  - `new-project` / `new-milestone` / `complete-milestone` are not current `R5.18` owners at all
  - `init.cjs` and completion-representation surfaces sit in the middle as boundary-adjacent mechanism work rather than cleanly `in` or `out`
  (`.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-internal-r1.md:102,118,126`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:5-29`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:144-201`).
- [d:c+r:i] It was too thin because it treated `complete-milestone` and `completion semantics` as if they were the same issue. Current `R5.18` does boundary work on clean-versus-debt-carrying completion semantics, but it still does not own the historical `complete-milestone` doctrine-delta review surface (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:31-35`; contrast with `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:225-231,247-248`).
- [d:c+r:i] It was too broad because it let broader doctrine strengthening in `AGENTS.md` and `.planning/AGENTS.md` read as part of current lifecycle treatment. Those docs matter as compensation, but the historical lifecycle lane explicitly called for patching lifecycle workflows and lifecycle metadata, not only strengthening governing prose (`.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-internal-r1.md:118`; contrast with `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:233-275`).
- [d:c+r:i] It was also too broad for this lane because it mixed CI/local-verify and remote-review follow-through into the same integrated diagnosis. Those are useful full-bundle concerns, but they are not necessary to classify the lifecycle-only subfamilies this L2 lane is meant to grade (`.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-internal-r1.md:104-107,119-120,165-167`).

## Decision Table

| lifecycle / `LONG-ARC` subfamily | historical expectation | current treatment | status | note |
| --- | --- | --- | --- | --- |
| Non-phase lifecycle carry-forward overall | lifecycle-wide patching of entry, routing, transition, completion, and metadata continuity (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:175-189,233-275`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:339-347,406-415`) | current scope absorbs only rerun-critical mid-lifecycle and adjacent mechanism work | `partially_addressed_boundary_only` | overall family remains narrower than the 2026-04-15 near-term roadmap |
| `progress` doctrine-grounding visibility | stop treating `has context` as enough; surface doctrine-grounded readiness (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:180-181,213-215,240-245`) | `progress.md` is inside the direct `R5.18c` core trunk (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:5-15`) | `addressed_in_r5_18` | direct ownership exists, though not yet implementation truth |
| `transition` doctrine triage / carry-forward refresh | add doctrine triage after phase completion (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:182-183,217-223,245-246`) | `transition.md` is inside the direct `R5.18c` core trunk (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:5-15`) | `addressed_in_r5_18` | current checkpoint owns the transition surface directly |
| Project / milestone entry carry-forward | make doctrine first-class at `new-project`, templates, and `new-milestone` (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:176-179,194-206,235-256,277-280`) | no `new-project.md`, `new-milestone.md`, `templates/project.md`, or `templates/roadmap.md` owner appears in current `R5.18` boundary or launch bundle | `still_missing` | this is the biggest lifecycle entry gap relative to the historical lane |
| Milestone-completion doctrine delta | review doctrine before archive finalization and add milestone-level doctrine-delta handling (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:225-231,247-248,291-299`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:451-454`) | current `R5.18` owns completion semantics and summary/debt-carrier boundary work, but not `complete-milestone.md` or doctrine-delta reporting | `still_missing` | completion representation is not the same thing as milestone-completion doctrine triage |
| Init-path doctrine metadata continuity | expose `long_arc_exists` / `long_arc_path` style lifecycle metadata (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:188-189,258-263`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:347,412-415`) | `init.cjs` is inside `Bucket 2B` and may be admitted to `R5.18c`, but it is not a direct first-wave lifecycle patch site yet (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:156-158`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:27-29`) | `partially_addressed_boundary_only` | mechanism continuity is inside boundary truth, not inside settled direct ownership |
| Doctrine-blind auto-path / permissive lifecycle behavior | stop relying on permissive auto paths and hardcoded doctrine-blind behavior (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:184-187,237,272-275,284-286`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:348,415`) | no current `R5.18` task or launch lane owns live config/default posture or lifecycle auto-path alignment | `still_missing` | historical auto-path concern remains outside current checkpoint ownership |

## Operational Consequences

- [d:c+r:i] Current Checkpoint 5 can honestly claim only this lifecycle uptake:
  - direct rerun-critical ownership of `progress` and `transition`
  - boundary-adjacent handling of init metadata and completion-representation mechanisms
  - stronger governing compensation outside lifecycle workflows
  It cannot honestly claim lifecycle-wide `LONG-ARC` carry-forward closure.
- [d:c+r:i] `R5.18a` should treat this artifact as the sharper lifecycle grading surface, not the monolithic comparison alone. If `init.cjs`, `summary.md`, or the debt-carrier mechanism stay outside first-wave, the contradiction ledger should name the remaining lifecycle continuity debt explicitly rather than recording only generic scope reasons.
- [d:c+r:i] If the repo wants the historical lifecycle lane actually closed rather than merely narrowed for rerun, a later lane still has to own:
  - `new-project.md`
  - `new-milestone.md`
  - `complete-milestone.md`
  - durable-doctrine scaffolding / doctrine-delta reporting
  - doctrine metadata / auto-path alignment
- [d:c+r:i] The monolithic comparison should therefore be read as a correct high-level warning but not as the final lifecycle grading artifact. Its single lifecycle row is too compressed to govern `R5.18a` boundary decisions responsibly.

## Sources

- `AGENTS.md`
- `.planning/AGENTS.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md`
- `.planning/readiness/phase-01-rerun/STATUS.md`
- `.planning/readiness/phase-01-rerun/TASKS.md`
- `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md`
- `.planning/readiness/phase-01-rerun/PROTOCOL.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18d-integration-and-review-prep-launch-spec.md`
- `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md`
- `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19e-adjudication-reread-internal-r1.md`
- `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-internal-r1.md`
