# Checkpoint Ledger

This ledger records meaningful readiness checkpoint boundaries and the commits that captured them.

## Pending Checkpoints

| Checkpoint | Intended boundary | Commit status |
|---|---|---|
| 1 | governance-doc normalization audit artifact, if independently reviewable | Pending |
| 2 | governance-doc normalization patch | Recorded |
| 3 | workflow / harness scoping artifact, if independently reviewable | Recorded |
| 4 | tandem phase-workflow / Codex+GSD harness excellence audit artifact, if independently reviewable | Recorded |
| 5 | reactivated workflow-and-harness follow-through after scope correction | In progress |
| 6 | rerun-readiness verification artifact, if produced | Pending |
| 7 | fresh Phase 01 discuss/context/plan bundle before execution approval | Pending |

## Recorded Commits

| Checkpoint | SHA | Commit message | Notes |
|---|---|---|---|
| 0 baseline | `9d1e22b` | `docs(governance): tighten claim typing and checkpoint rules` | Governance/process baseline committed before the corrective bundle pass |
| 0 baseline | `2ad87fc` | `docs(readiness): scaffold phase 01 rerun package` | Readiness control surface established |
| 0 baseline | `c38ad2a` | `docs(research): checkpoint multi-layer governance audit bundle` | Stable review baseline, but not the final corrected Checkpoint 0 closeout |
| 0 support | `33fa17b` | `docs(readiness): integrate model policy and cross-audit gates` | Readiness package updated to reflect model-policy and cross-vendor gate consequences |
| 0 support | `bfd09f1` | `docs(readiness): add research intake layer` | Added explicit research-to-package absorption surface |
| 0 support | `63bb5ce` | `docs(readiness): absorb cross-model audit findings` | Accepted cross-model integration findings as conditional follow-through, not a blocker |
| 0 support | `cffee7d` | `docs(readiness): add checkpoint review policy` | Added review matrix and checkpoint review template |
| 0 support | `bdcf4b3` | `docs(readiness): tighten autonomy and review controls` | Added machine-readable review policy, opportunity tracking, deviation taxonomy, and stronger independence rules |
| 0 support | `433bb00` | `docs(readiness): specify Claude review lanes and commands` | Made cross-vendor review concrete for this repo's current Claude lanes |
| 0 support | `f7c49c2` | `docs(workflow): add compaction continuity mitigations` | Added session continuity mitigation at the workflow layer |
| 0 support | `c919bd8` | `docs(codex): refresh readiness compact prompt` | Refreshed the temporary readiness compact prompt after later readiness-control changes |
| 0 closure input | `dd3966c` | `docs(research): repair governance audit bundle citations and markers` | Separate research-bundle repair commit. Closure evidence lives in [GATES/checkpoint-0.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-0.md) and [REVIEWS/checkpoint-0-internal-review-r2.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-0-internal-review-r2.md) |
| 1 support | `746e53a` | `docs(readiness): add checkpoint 1 audit surface` | Established `AUDITS/` as the package-side home for reusable checkpoint audit specs and outputs before delegating the Checkpoint 1 authoring lane |
| 1 closure input | `97bd603` | `docs(readiness): close checkpoint 1 and advance to checkpoint 2` | Captured the Checkpoint 1 audit artifact, review artifact, and package-state transition into Checkpoint 2 |
| 2 closure input | `bcbae15` | `docs(readiness): close checkpoint 2 and advance to checkpoint 3` | Captured the governance-doc normalization patch, its internal review, its cross-vendor Claude review, and the package-state transition into Checkpoint 3 |
| 3 support | `af9c21b` | `docs(readiness): checkpoint checkpoint-3 initial surface maps` | Committed the initial Codex and GSD mapping baseline before the split-expanded deeper GSD mapping work |
| 3 support | `6974e54` | `docs(readiness): refine checkpoint-3 split mapping bundle` | Tightened the Checkpoint 3 mapping bundle before external reread |
| 3 support | `270d43a` | `docs(readiness): add checkpoint-3 split-spec cross-vendor review` | Stored the first cross-vendor adequacy reread of the split-spec bundle |
| 3 support | `f14ecf2` | `docs(readiness): tighten checkpoint-3 split specs after review` | Accepted the split-spec reread and repaired the mapping bundle before deeper GSD mapping launched |
| 3 support | `cf174d9` | `docs(readiness): add checkpoint-3 deeper gsd maps` | Captured the three deeper GSD mapping sublanes after the split trigger fired |
| 3 support | `b10043f` | `docs(readiness): add checkpoint-3 gsd scope synthesis` | Captured the resolved GSD-side synthesis that the overall Checkpoint 3 scope audit consumes |
| 3 support | `302e6b1` | `docs(readiness): add checkpoint-3 scope audit review specs` | Stored reusable internal and cross-vendor review specs before the final scope audit reviews |
| 3 support | `5d49dc6` | `docs(readiness): raise review rigor bar` | Tightened readiness review doctrine so later checkpoint reviews push against adequacy rather than merely checking pass/fail closure |
| 3 closure input | `e215ed8` | `docs(readiness): close checkpoint 3 and advance to checkpoint 4` | Captured the final scope audit, internal and cross-vendor review outputs, and the package-state transition into Checkpoint 4 |
| 4 closure input | `7f24b1d` | `docs(readiness): finalize checkpoint 4 audit bundle` | Captured the four authored lanes, seam and converged syntheses, the cross-vendor Opus reread, and internal review/rereview artifacts before any Checkpoint 5 harness changes |
| 5 scope correction | `8e05b3d` | `docs(readiness): reactivate checkpoint 5 scope` | Preserved the original narrower Checkpoint 5 spec as history, introduced the current authoritative reactivated launch spec, and reclassified the first Checkpoint 5 implementation/review bundle as partial historical evidence |
