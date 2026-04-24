Date: 2026-04-22
Status: active reread output (Opus 4.7 max r1)

# Landed Health Uplift Deepen-In-Place First Slice Reread — Opus 4.7 Max R1

## What The Landed Health Slice Now Carries More Clearly

- The repair-facing workflow now names the post-validation uplift step directly. `review_project_uplift_health_follow_through` exists as a labelled `<step>` between `verify_repairs` and `format_output`, so the route-local distinction between structural validation and read-only continuity surfacing is now a physical page element rather than a prose intention carried across two reviewers' memories. The same step carries all five headings (`Primary Compact Read`, `Supporting Narrative Read`, `Deeper Typed Read`, `Interpretation Frame`, `When To Surface`) in one contiguous block, so the widening order is legible in the carrier itself instead of being inferred from the `70` split plus the `123` reference.

- The compact-first reading order is no longer an implicit preference. `health.md` now begins the step with "Start with `.planning/STATE.md` and reread `## Project Uplift` first," widens to `.planning/UPLIFT-REPORT.md` only when the compact digest does not carry enough route-local context, and widens further to `.planning/UPLIFT-MANIFEST.json` only when basis or annotation ambiguity remains. That ordering reads the same way the milestone-boundary shared reference does, so the cross-family grammar convergence that `18-r1` anticipated is now visible across both carriers at once rather than sitting only inside the shared-reference file.

- The read-only character of the step is carried as an explicit prohibition, not only as an adjacent recommendation. The workflow now says directly: "Do not run `$gsd-uplift-project --write` from inside it." That sentence is pinned by the contract test (`tooling/codex/tests/test_health_uplift_deepen_in_place_contract.py:25`). A later refactor that dropped or paraphrased the prohibition would flip the test red, so the read-only posture is held by a machine check rather than by convention.

- The wrapper now states the three-way ownership split directly in two places — the `<objective>` paragraph and the `<process>` block — using the same framing each time: structural planning health remains the primary objective, read-only uplift continuity reread may follow once validation is complete and route-local posture pressure is still live, `$gsd-uplift-project --write` remains a later separate follow-through. The contract test grabs all three of those lines from the wrapper (test lines 55-57), so the wrapper-side three-way split is also held by executable coverage, not only by the skill card's read-only text.

- The trigger surface is now spelled out in prose that names the scalar fields the operator should read instead of a single generic "route has shifted" line. The workflow names `Compatibility posture`, `Observed runtime basis`, `Held runtime annotation`, and `Current recommendation` as the four scalar signals that count as live posture pressure, and the contract test pins each keyword (test lines 41-44). The field names match the STATE.md block exactly (`.planning/STATE.md:86-96`), so the route-local predicate and the carrier it reads are now aligned by string.

- The `--repair` ordering is now a structural check rather than a reading discipline. The contract test asserts that `<step name="verify_repairs">` appears before `<step name="review_project_uplift_health_follow_through">` and that the new step appears before `<step name="format_output">` (test lines 26-33). The "post-repair revalidation finishes first" rule that `18-r1` asked for as a local revision is now held by a machine check on step ordering instead of operator habit.

- Propagation carry is now visible at three layers, not only at the prose-note layer. `propagation-audit/46-health-uplift-deepen-in-place-change-triggered-refresh.md` records the route-local refresh in narrative form; `propagation-audit/artifacts/03-propagation-registry-v2-declared-contracts.json` registers a new `health_uplift_deepen_in_place_contract` with the contract test as its validator; `propagation-audit/artifacts/05-propagation-registry-v2-evidence-index.json` carries `health_uplift_deepen_impl_125`, `health_uplift_deepen_contract_tests`, and `health_uplift_deepen_refresh_46`; and `propagation-audit/artifacts/04-propagation-registry-v2-semantic-map.json` attaches both evidence refs to `health_workflow` and `health_skill_wrapper` and rewrites both roles to include the post-validation continuity reread explicitly. So the slice is now remembered by the registry as a typed consumer with evidence, not only as a recent commit.

- The compatibility-family chain now carries six consecutive refreshes in order (`16`, `17`, `43`, `44`, `45`, `46`), with `46` framed as "compatibility-family continuity now reaches the repair-facing `health` route through one explicit post-validation read-only step." The silent-carrier problem `119` named — that health was the next carrier where structural pressure could silently shift into later-posture pressure without any compact carrier making the shift legible — now has its explicit carrier.

## Where The Live Implementation Boundary Still Thins Or Compresses Distinct Jobs

- The workflow's top-of-file `<supporting_reading>` and `<deeper_reading>` blocks now carry some of the uplift-continuity rule that belongs inside the step itself. The `<supporting_reading>` block says: "`.planning/UPLIFT-REPORT.md` or `.planning/UPLIFT-MANIFEST.json` only inside the dedicated uplift follow-through step, and only after the compact `STATE.md` `## Project Uplift` reread has shown that route-local posture pressure is still live." That sentence is a useful ground rule, but its placement interleaves read-packet doctrine with uplift-continuity doctrine at the top of the file, and the step itself restates the same widening rule later. Two voices for the same rule at two different nesting levels leaves room for one of them to drift in a later edit without the other following.

- The workflow now carries the three-way route split in two places that are not quite identical in voice. `keep_route_boundaries_explicit` names it as a terse shorthand (health owns structural integrity; missing planning routes to `$gsd-new-project` or `$gsd-ingest-docs`; present-but-thin routes to `$gsd-uplift-project --write`). The new step's `Interpretation Frame` names it in the three-role form (`validate.health` authority, read-only continuity, later write-side refresh). They do not conflict, but they are parallel declarations about related subjects. Which one is the authoritative carrier for the split is not stated.

- The pre-existing footer line in `format_output` ("Structural health is not the same thing as repo-local posture refresh. If runtime/governing-doc/doctrine posture is the live issue, run: `$gsd-uplift-project --write`") still fires independently of the new step. The new step's `Interpretation Frame` forbids widening the footer into a second uplift workflow, but it does not say how the footer and the step relate when both are active in a single pass. In a healthy-with-posture-pressure run, the step surfaces a read-only reread and the footer suggests a write-side next move — both correct in isolation, but the live output now carries two uplift-adjacent surfaces without telling the reader how they compose.

- The trigger predicate is now materially sharper than the proposal, but the silent case still lives in prose. The step's `When To Surface` block tells the operator to keep the step silent under three conditions (planning missing, structural health unresolved, compact block signals ordinary routing). The contract test covers the presence of the trigger signals and the step's explicit write-side prohibition, but does not assert anything about the silent case — a later edit could relax "Keep it silent when" into "consider keeping it silent when" and the test would stay green. Given that the live STATE.md currently reads `Current recommendation: Continue with ordinary routing`, silence is the actual live behaviour, and that live behaviour has no executable contract yet.

- The four scalar signals the step treats as live posture pressure are still interpretive rather than directly evaluable. "`Compatibility posture` needs active interpretation instead of simple observed-basis continuation" pushes a judgment onto the operator rather than naming a comparison — for example, "`Compatibility posture` value has changed since prior uplift" or "`Compatibility posture` is not `observed_basis_only`" would be directly evaluable. The milestone-boundary reference is sharper on this point at milestone-open and milestone-close, where it names concrete scalar comparisons (observed runtime basis moved; `pending_doctrine_sensitive_proposals > 0`; `held_later_families` partial-landing relevance). The health step could inherit that sharpness without widening into a shared reference.

- The contract test couples to syntactic shapes (`<step name="verify_repairs">`, `<step name="review_project_uplift_health_follow_through">`, `<step name="format_output">`). That choice carries the ordering invariant well today, but it does not protect the meaning of the invariant — if a future refactor inlined `verify_repairs` into `offer_repair`, the test would fail even though the semantic rule (post-repair validation completes before uplift-continuity surfacing) could still be satisfied. The coupling is acceptable for one slice but should not be treated as the durable guarantee.

- The propagation registry now carries the slice as a consumer, but the registry's own role line for `health_workflow` compresses five distinct jobs into one sentence ("structural-health workflow with layered read-packet control, explicit missing-planning routing, a post-validation read-only uplift continuity reread..., and a later write-side uplift route kept separate from repair"). The compression is tolerable because the evidence refs still point at the five distinct implementation notes. But the role field is now the heaviest such field in the workflow family, and it sits one keyword-search away from future blurring.

## What The Landed Mechanics Improve In Live Use

- **Structural-health vs continuity vs later refresh separation.** Before the slice, operators had to hold the three-role split in memory across `70` (repair owns structural validation), `121` (transition owns phase-close continuity), `123` (milestone boundaries own boundary continuity), and the uplift writer (`project_uplift.py`). After the slice, the health run itself carries the three-role split in a single page with two layers of machine checks (test lines 55-57 for the wrapper; test lines 24-25 for the step's write-side prohibition). An operator reading the current health workflow for the first time does not have to reconstruct the split from four source documents.

- **Compact-to-narrative-to-typed widening order.** The five-heading grammar now appears inside `health.md` as a physical block and is pinned by the contract test (test lines 15-20). The same grammar appears inside `references/milestone-boundary-uplift-continuity.md` as a shared reference. The two carriers read the same way even though one owns its grammar locally and the other exposes it for two consumers. In live use, an operator moving from a milestone-close review into a `$gsd-health --repair` run encounters the same reading order twice, which lowers the cost of cross-carrier orientation.

- **Repair-first sequencing.** In live use, `--repair` mode triggers `run_health_check` → `keep_route_boundaries_explicit` → `offer_repair` → `verify_repairs` → the new uplift-continuity step → `format_output`. The test pins the `verify_repairs < uplift-continuity < format_output` chain, so a future refactor that moved the uplift-continuity step ahead of `verify_repairs` would fail the contract. The sequencing guarantee holds even if the surrounding structural-repair pipeline evolves, as long as `verify_repairs` remains a labelled step.

- **Compatibility anchor and held-annotation carry.** The workflow text now names `Compatibility posture: observed_basis_only` literally (pinned by the test), and the `Held runtime annotation` field is treated as one of the four live posture signals rather than as part of the top-level posture row. That preserves the `116` / `119` discipline that held-annotation stays annotation, not dual-basis relabel, at one more consumer surface. The live STATE.md currently carries `Held runtime annotation: .claude 1.34.2 (held_annotation)` and `Compatibility posture: observed_basis_only` — the health step is now positioned to read both without collapsing them.

- **Propagation visibility.** Before the slice, the repair-facing carrier was recorded in the registry at the `70` lifecycle layer only. After the slice, the same carrier is recorded at the impl layer (`health_uplift_deepen_impl_125`), the contract layer (`health_uplift_deepen_contract_tests`, `health_uplift_deepen_in_place_contract`), and the refresh layer (`health_uplift_deepen_refresh_46`). A later operator running `$gsd-propagation-review` over the workflow family now sees the health carrier as a multi-layer typed consumer of the uplift-continuity family rather than as a single structural-repair row.

- **Cross-runtime posture preservation.** The wrapper's `<objective>` block explicitly says the skill "does not by itself own broader runtime, governing-doc, or doctrine uplift refresh for older projects." That single sentence holds the line between the observed `.codex` basis (1.38.3) and the held `.claude` annotation (1.34.2, `held_annotation`) when a repair-facing operator runs health on an older project — the skill will not silently adjudicate cross-runtime posture during structural repair.

## What Still Deserves Revision Before Wider Follow-Through

- **Tighten the trigger predicate into more evaluable form.** The four prose signals ("needs active interpretation", "carries route-local relevance", "materially affects route-local interpretation", "names later repo-local refresh rather than ordinary routing") leave judgment on the operator. Sharpen each one into a scalar comparison against STATE.md fields: for example, "`Compatibility posture` is not `observed_basis_only`" OR "`Observed runtime basis` differs from the value present before the last uplift write" OR "`Held runtime annotation` is non-empty" OR "`Current recommendation` is not the literal string `Continue with ordinary routing; uplift memory keeps this posture explicit.`" This puts the trigger on the same footing as the milestone-boundary reference, which already uses scalar-comparison signals. The tightening can stay inside `health.md` — it does not need a shared reference.

- **Add contract coverage for the silent case.** A new test case should assert that when the four signals do not fire, the workflow names "silent" as the expected behaviour. The simplest form is a test that greps for `Keep it silent when` plus the three explicit silent-case lines, so a later edit that relaxed "silent" into "optional" would flip the test red. Without that coverage, the silence arm of the step is a prose-only guarantee.

- **Clarify how the pre-existing footer and the new step compose in the same pass.** The `format_output` footer recommends `$gsd-uplift-project --write` when "structural health is acceptable but repo-local posture still needs refresh." The new step surfaces read-only continuity when a similar (but not identical) condition holds. A single sentence inside `Interpretation Frame` that says the footer remains the write-side route pointer and the step remains the read-only continuity reread — and that both can fire in one pass without duplicating — would remove the only remaining ambient coexistence question.

- **Consolidate the three-way split to a single authoritative declaration.** Today the split appears in `keep_route_boundaries_explicit` as terse route shorthand and in `Interpretation Frame` as a three-role declaration. Keep `Interpretation Frame` as the authoritative declaration and have `keep_route_boundaries_explicit` point at it rather than restate it, so future edits have one place to change. This avoids the slow drift that happens when two adjacent steps each carry a version of the same rule.

- **Decouple the test's syntactic form from the semantic invariant where possible.** The current test checks for `<step name="verify_repairs">` and the surrounding step tags. Adding one semantic-level assertion (for example, "the step body names post-repair revalidation as finishing first") would survive a future refactor that renamed or inlined the step tag. The syntactic checks can stay; the semantic check reinforces them.

- **Lighten the role field for `health_workflow` in the semantic map.** The role string now compresses five jobs. If the registry grows one more slice at the same carrier, the string will become the densest in the workflow family. A later harden slice could split the role into a short primary role plus a list of auxiliary roles, mirroring how the evidence_refs array already splits the evidence.

## Later Families To Keep Explicit

- **`from-gsd2` uplift-continuity.** `70` already routes `from-gsd2` through `health` for post-migration structural validation, so `from-gsd2` is now an indirect consumer of the new step via the structural-repair path. A parallel `from-gsd2`-side uplift-continuity carrier can wait until a second repair-family wrapper acquires its own route-local uplift-continuity pressure. Opening one now would duplicate work and pull the migration surface toward repo-local posture adjudication, which `70` explicitly separates.

- **`update` follow-through uplift-continuity.** Package/runtime version movement is distinct from repo-local governing-doc / doctrine posture refresh. `28` already refreshes the `update` + `gsd-update` carrier with runtime/package versus structural-health versus later-uplift route separation. Folding uplift-continuity awareness into `update` now would blur the `71`/`72` hold that keeps those concerns separate.

- **Verifier lifecycle carriers.** `119` classifies verifier as `explicitly held` on the grounds that held-runtime awareness at verification time would widen surfacing posture into compatibility judgment under future-preservation review. The repair-family slice does not unlock that question. Keep it held until a dedicated route opens.

- **Discuss / plan / execute entry points.** `119` holds these pending family-6 wider route mapping because opening them for silent-carrier uplift continuity could pre-answer the registry-versus-translation-versus-doctrine split that family-6 still owns.

- **Helper-side `RUNTIME_DIRS` versus `HELD_CLAUDE_RUNTIME_VERSION_REL_PATH` asymmetry.** This is a helper-clarity widening and a later third-runtime frontier question. It sits outside the current slice's repair-facing scope.

- **Write-recommending drift path in `project_uplift.py`.** `compatibility_drift_reasons` should remain a bounded drift detector rather than widening into a generic write-side dispatcher during any near-term slice.

- **Setup / materialization bridge (`propagation 20`).** The installer entry, `gsd-sdk` helper, and pristine-capture stage sit at the install/runtime frontier. Widening consumer semantics here would mix install and consumer questions.

- **Broader read-packet widening for `health` beyond this one route-local uplift step.** Keep `health`'s structural-repair posture primary.

- **Auto-repair-plus-auto-refresh chaining.** The split between read-only continuity and later write-side refresh depends on these staying separate actions.

- **Wider repair/migration/update family harmonization.** The current three-way split in `health` is sharper than a shared-reference family would be at this consumer count.

- **Compatibility-family widening beyond observed-basis plus held-annotation discipline.** Matrix claims, version-window claims, upstream-template drift, structural-row promotion — all held by `118`/`119`, reaffirmed at `121` and `123`, reaffirmed again at `125`.

- **`.claude` parity / translation / third-runtime widening.** Reachable only through family-6 route mapping when it opens. Not through the repair family.

- **Cross-repo extraction and distribution from `115`.** Still held until current uplift/cross-runtime and propagation contracts sharpen further.

## Strongest Adjacent Strengthening Route

- The strongest next move is a bounded **health-uplift-continuity harden follow-through** at the same carrier, not a new single-carrier route. The case runs through three observations.

- First, the one remaining interpretive thinness in the landed slice is the trigger predicate. Four scalar signals that currently read as "needs active interpretation" can become scalar comparisons against STATE.md fields plus explicit silent-case contract coverage. That change lifts the slice's machine-checked surface from "step exists with five-heading grammar in the right order with wrapper split intact" to "step exists, is triggered by evaluable conditions, stays silent under named conditions, and the silence itself is under contract." This sharpens the slice in the one place prose still dominates.

- Second, the workspace has precedent for harden follow-throughs after first-slice landings. `87`-`88` + `36` hardens the seed-migration detect-only route; `91`-`92` + `38` hardens the operator-facing pointer bridge; `99`-`100` + `40` hardens the propagation-review route. The hardens each (a) tighten one specific thinness the first-slice reread identified, (b) add one durable output or contract surface, (c) produce a matching propagation refresh. That pattern fits here: a `126` proposal + `127` implementation pair, a tightened contract test, and a `47` propagation refresh would mirror those three precedents.

- Third, opening any of `119`'s `explicitly held` carriers (`update`, verifier lifecycle, discuss/plan/execute entry points, helper-side `RUNTIME_DIRS` asymmetry, write-recommending drift, setup/materialization bridge) would contradict `119`'s classification or widen family-6 territory prematurely. Opening `from-gsd2` as a parallel peer would duplicate work the structural-repair path already covers indirectly. Opening a shared `repair-family uplift continuity` reference would add a surface without a second peer consumer and would blur the deepen-in-place versus attach-through-shared-reference distinction that `119` was built to carry.

- The harden follow-through would carry four concrete moves:
  1. Tighten the `When To Surface` trigger into scalar-comparison form against STATE.md fields (observed-basis change; held-annotation presence; compatibility-posture value; recommendation-string match).
  2. Add contract coverage for the silent case (grep-level assertions that `Keep it silent when` + the three silent-case conditions appear literally).
  3. Add one sentence inside `Interpretation Frame` naming the relationship between the new step and the pre-existing `format_output` footer so the coexistence is explicit.
  4. Consolidate the three-way split declaration so `Interpretation Frame` is authoritative and `keep_route_boundaries_explicit` refers to it rather than restating.

- After the harden follow-through lands, the next `119` priority decision opens cleanly rather than through a half-tightened carrier. The candidates then are: (a) picking up an explicitly-held carrier from `119` when its prerequisite conditions actually open; (b) widening the family-6 route-asymmetry mapping under `118`/`119`; (c) returning to the `93` family split if upstream-baseline versus repo-local-delta pressure re-opens.

## How This Landed Slice Should Be Inherited

### Carry Forward

- The landed two-carrier scope: `health.md` plus `gsd-health` as the deepen-in-place carrier pair.
- The labelled `review_project_uplift_health_follow_through` step as the post-validation carrier for read-only uplift continuity.
- The five-heading local grammar (`Primary Compact Read`, `Supporting Narrative Read`, `Deeper Typed Read`, `Interpretation Frame`, `When To Surface`) as in-place route structure rather than as a shared-reference dependency.
- The reading gradient STATE.md `## Project Uplift` compact → `UPLIFT-REPORT.md` narrative → `UPLIFT-MANIFEST.json` typed, with widen-only-when-ambiguity-remains discipline.
- Preservation of `Compatibility posture: observed_basis_only` as the top-level anchor and `Held runtime annotation` as annotation rather than dual-basis relabel.
- The three-way ownership split (`validate.health` structural-health authority / new step read-only continuity / `$gsd-uplift-project --write` later write-side refresh) as the slice's positive structural contribution.
- The `--repair` ordering as a machine-checked invariant (`verify_repairs` < new step < `format_output`).
- The explicit read-only prohibition ("Do not run `$gsd-uplift-project --write` from inside it.") and the three additional holds landed in the workflow (no drift computation, no second-uplift-workflow footer widening, no manifest mirroring/cache surface inside health output).
- The propagation-registry carry across contracts, evidence index, and semantic-map role updates for both `health_workflow` and `health_skill_wrapper`.
- The `46` compatibility-family change-triggered refresh as the sixth consecutive compatibility refresh after `16`, `17`, `43`, `44`, `45`.
- The sibling-shape pattern (one focused contract test, one propagation refresh, one implementation note) used by `121` and `123` and now repeated at `125`/`46`/contract test.

### Revise Before Widening

- Tighten the `When To Surface` trigger from interpretive phrasing into scalar-comparison form against STATE.md fields:
  - `Compatibility posture` differs from `observed_basis_only` OR from its value at last uplift;
  - `Observed runtime basis` differs from its value at last uplift;
  - `Held runtime annotation` is non-empty (or has changed);
  - `Current recommendation` is not the ordinary-routing string literal.
- Add contract coverage for the silent case, so the "Keep it silent when" block is held by a test and cannot quietly relax into optional phrasing.
- Add one sentence inside `Interpretation Frame` that names the relationship between the new step and the existing `format_output` footer — the footer remains the write-side route pointer; the step remains the read-only continuity reread; both may fire in one pass without duplicating.
- Consolidate the three-way split declaration so `Interpretation Frame` is the authoritative carrier and `keep_route_boundaries_explicit` points at it rather than restating it in terser form.
- Move the uplift-gating sentence currently sitting in `<supporting_reading>` ("`.planning/UPLIFT-REPORT.md` or `.planning/UPLIFT-MANIFEST.json` only inside the dedicated uplift follow-through step...") into the uplift step's own preamble, so structural-health read-packet doctrine and uplift-continuity doctrine stay on separate carriers at the top of the file.
- Add one semantic-level test assertion alongside the existing syntactic checks (for example, a check that the step body names post-repair revalidation as finishing first), so the ordering invariant survives a future refactor that renamed or inlined step tags.

### Hold For Later

- Any widening of the `validate.health` helper semantics into repo-local posture adjudication.
- Any shared reference for the repair family. `from-gsd2` remains an indirect consumer of the new step via structural-repair routing; a dedicated repair-family shared reference waits until a second repair-family wrapper acquires its own route-local uplift-continuity pressure.
- Any `update`-side uplift-continuity deepen. Package/runtime movement stays distinct from repo-local posture refresh per `28` and per `119`'s explicit hold.
- Any verifier lifecycle uplift-continuity opening until family-6 route mapping makes future-preservation-under-compatibility review a well-posed question.
- Any discuss / plan / execute entry-point continuity opening until `118`/`119` family-6 widening actually runs.
- Any auto-repair-plus-auto-refresh chaining.
- Any broader read-packet widening for `health` beyond this one route-local uplift step.
- Any compatibility-matrix, version-window, parity, translation, third-runtime, or structural-row promotion claim inside the health family.
- Any cross-repo extraction movement from `115` until the uplift/cross-runtime and propagation contracts have sharpened further.
- Any widening of `compatibility_drift_reasons` in `project_uplift.py` into a generic write-side dispatcher.
- Any manifest mirroring, caching, or reformatting of uplift-manifest content into a new health-local surface.

### Next Bounded Move

- Open a health-uplift-continuity harden follow-through (proposal at `intervention-proposals/126-...`; implementation at `intervention-proposals/127-...`; matching compatibility-family refresh at `propagation-audit/47-...`; tightened contract coverage inside the existing `test_health_uplift_deepen_in_place_contract.py`).
- Keep that harden bounded to the four moves named in Section 6: trigger sharpening, silent-case coverage, step-versus-footer composition line, three-way-split consolidation.
- Keep the harden inside the repair-facing carrier itself; do not widen into `from-gsd2`, `update`, or a new shared reference.
- After the harden lands, re-evaluate the `119` priority order against the refreshed carrier surface rather than against the pre-harden surface; the held-family decisions ride on the sharpened trigger and on the registry's updated role field, not on the prior prose-only trigger.
