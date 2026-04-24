Date: 2026-04-22
Status: completed opus output

# Uplift Cross-Runtime Post-Annotation Next-Move Opus Review

## What The Landed Annotation Slice Now Clarifies

- [e:c+r:i] `116` does not only make one generic point about the compatibility anchor. It separates four distinct surfaces that were previously blended inside the proposal prose:
  - the durable anchor posture label in [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:79) and [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:25) still reads `observed_basis_only`
  - the durable anchor now carries a typed `held_runtime_annotation` object plus a scalar `held_runtime_annotation_summary` alongside the observed-basis fields ([UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:88) through [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:95))
  - the compatibility-check protocol itself now includes a held-runtime comparison step that did not exist before ([UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:101))
  - the helper-side carry adds a specific `.claude`-shaped reader rather than a general runtime-dir walker ([tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:23), [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:280))
- [d:r:i] The three-shape field from `114` therefore no longer travels symmetrically. Annotation posture is now instantiated in live code and durable memory. Dual-basis posture is more clearly held rather than merely deferred, because the top-level label did not move and the protocol now routes held-runtime drift through `compatibility_drift_reasons` rather than through a posture rename ([tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:341)). Typed multi-runtime carrier stays held, but the hold reason is now more observable: the helper chose a named `HELD_CLAUDE_RUNTIME_VERSION_REL_PATH` constant rather than a list-shaped or dict-shaped held-runtime registry.
- [e:c+r:i] The held-scalar versus structural-row split from `114` also resolves asymmetrically. The manifest object is structurally typed, while the state-file and report lines remain scalar summaries ([STATE.md pathway via `held_runtime_annotation_summary` in tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:1321) and the report body at [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:41)). The landed slice therefore behaves like held-scalar for operator-facing prose and like a small structural row inside the JSON carrier. A later reader can now see this hybrid directly rather than inferring it from the proposal.
- [d:r:i] The consumer chain is now exercised, but unevenly. The four read-only current-runtime surfaces in [116](../../intervention-proposals/116-uplift-compatibility-annotation-first-slice-implementation.md:32) have been touched. The uplift-side write pathway now recommends `$gsd-uplift-project --write` whenever held-runtime drift is detected ([tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:1431), [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:1441)). The rest of the operator-facing route field (transition, milestone-boundary, discuss/plan/execute-phase, verifier lifecycle, spec lifecycle) has not been reached yet.
- [e:c+r:i] The propagation family now carries three consecutive real refreshes on the compatibility route — `16`, `17`, `43` — so the typed `v2` registry is no longer at one compatibility-bearing entry point but at a small chain of them ([propagation-audit/43-uplift-compatibility-annotation-change-triggered-refresh.md](../../propagation-audit/43-uplift-compatibility-annotation-change-triggered-refresh.md:37)). That chain itself is a new readable shape; it did not exist when `114` was authored.
- [d:r:i] The observed-basis discipline inside uplift memory is therefore now carrying more weight than it did before `116`. The top-level `observed_basis_only` label must continue to mean what it said through the lifetime of the held annotation, not just at the moment the annotation was introduced.

## Adjacent Cross-Runtime Families Now Sharper

### 1. Consumer-Chain Asymmetry

- [d:r:i] Before `116`, consumer-chain asymmetry was mapped as a candidate family but had no landed carrier on either side. After `116`, the read-only side is live across four surfaces, and the uplift-side write recommendation is the only operator-facing write-path currently wired for held-runtime movement. This sharpens the question from `how should consumer-chain asymmetry be carried` toward `which specific write-side and route-translation consumers are now silent relative to the already-landed read-only four`.
- [e:c+r:i] The currently silent carriers visible in live workflow and registry surfaces include, at minimum:
  - transition workflow consumers ([propagation-audit/21-transition-lifecycle-carry-change-triggered-refresh.md](../../propagation-audit/21-transition-lifecycle-carry-change-triggered-refresh.md))
  - milestone-boundary workflow consumers ([propagation-audit/22-milestone-boundary-lifecycle-carry-change-triggered-refresh.md](../../propagation-audit/22-milestone-boundary-lifecycle-carry-change-triggered-refresh.md))
  - spec-lifecycle carriers ([propagation-audit/24-spec-lifecycle-carry-change-triggered-refresh.md](../../propagation-audit/24-spec-lifecycle-carry-change-triggered-refresh.md))
  - verifier-lifecycle carriers ([propagation-audit/19-verifier-lifecycle-carry-change-triggered-refresh.md](../../propagation-audit/19-verifier-lifecycle-carry-change-triggered-refresh.md))
  - discuss/plan/execute-phase entry points for runtime-aware routing
  - `$gsd-propagation-review` operator route ([propagation-audit/40-propagation-review-route-harden-change-triggered-refresh.md](../../propagation-audit/40-propagation-review-route-harden-change-triggered-refresh.md))
- [d:r:i] The family now has enough live basis to stop being one abstract asymmetry label and start being a mapped field of silent carriers versus already-annotated carriers.

### 2. Structural-Row Annotation

- [d:r:i] The held-scalar choice carries held-runtime information without promoting the held runtime to a first-class peer inside the anchor. That preserves top-level posture discipline, and it also defers work that a structural-row annotation would force: second-source detection for held-runtime manifest shape, explicit held-runtime schema versioning, and consumer code that treats the row as a query target rather than a summary string.
- [d:r:i] A structural-row shape is now more reachable in the sense that held-scalar has already exercised the surfaces that would receive it. It is not yet earned, because no current consumer is reading the held-runtime JSON object as a structural row; the consumer chain still reads the scalar summary ([tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md) via `held_runtime_annotation_summary`). The right next deepening is in consumer-chain direction, not in row-shape direction.

### 3. Family-6 Wider Route-Asymmetry Mapping

- [d:r:i] This family was parallelizable before `116` and remains parallelizable now. The compatibility-family shape choice is done for this cycle; family-6 does not inherit a different posture from `116`. The sharpening is that the Codex-only route field versus the current intervention-family-three framing can be surveyed without blocking on compatibility-anchor decisions.
- [d:r:i] The hold reason for typed multi-runtime carrier has also sharpened. The helper's narrow `.claude`-specific constant means that if family-6 mapping later discloses several routes that would benefit from runtime-agnostic reading, the pressure on the helper will come from there rather than from the compatibility anchor.

### 4. Route-Translation Pressure

- [d:r:i] `.claude` is now visible in the compatibility anchor, the check protocol, the read-only consumer chain, and the manifest. No `.claude/` workflow, skill, or doctrine surface has received a live parity edit. The gap between `.claude` as an annotated runtime and `.claude` as a translated runtime is more explicitly observable than before, which makes route-translation pressure more mappable without making it more urgent.
- [e:c+r:i] The version delta itself remains real: [.codex/get-shit-done/VERSION](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/VERSION) is `1.38.3` and [.claude/get-shit-done/VERSION](/home/rookslog/workspace/projects/prix-guesser/.claude/get-shit-done/VERSION) is `1.34.2`. `116` did not close that delta; it anchored it durably.

### 5. Later Standalone Carrier Pressure

- [d:r:i] A standalone cross-runtime compatibility carrier would force: its own schema versioning, its own drift-detection, its own consumer routing. Held-scalar annotation now demonstrates that these responsibilities can live inside the existing uplift anchor without a separate file. The pressure for a standalone carrier is therefore less acute, not because the later carrier is unnecessary, but because the current one is carrying more shape than a minimum-label anchor would carry.
- [d:r:i] The family-6 hold on typed-carrier work remains in force. `116` did not change the information family-6 still needs to disclose.

### 6. Later Extraction/Distribution Route Pressure From `115`

- [e:c+r:i] The helper-side implementation choice has made one extraction-relevant seam more visible. The constant [HELD_CLAUDE_RUNTIME_VERSION_REL_PATH in tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:23) is narrow by design, not generic. A later extracted installer that declared multi-runtime compatibility would either inherit this narrowness (one named held-runtime per new runtime) or refactor toward a list-shaped held-runtime registry. That decision now has a concrete incumbent.
- [d:r:i] The compatibility-policy shape that `115` flagged as something an extraction route would need to settle first has more material now. The check-protocol list in the manifest gives extraction a working contract shape, not just a posture label.

## How Those Families Interact

- [d:r:i] Consumer-chain asymmetry is now the family most directly released by `116`. Every other adjacent family is either gated by information family-6 still needs to disclose (typed-carrier, route-translation depth), preserved by the observed-basis discipline (structural-row, dual-basis), or downstream of contract sharpening that has not reached it yet (extraction). Consumer-chain asymmetry is the only family that moves from `candidate` to `reachable` because `116` landed.
- [d:r:i] Consumer-chain asymmetry and family-6 mapping still do not collide. Family-6 can open in parallel at any time. Their artifacts would live in different subtrees; their gates are different; neither needs information the other holds.
- [d:r:i] Structural-row annotation is downstream of consumer-chain asymmetry, not parallel to it. The case for promoting held-scalar to a structural row is strongest when multiple consumers are reading the held-runtime object structurally rather than through its summary string. That condition does not yet exist; the read-only four and the uplift-side write recommendation both read the scalar summary.
- [d:r:i] Typed multi-runtime carrier is downstream of family-6, not of consumer-chain asymmetry. The carrier shape question is about where cross-runtime compatibility information should live in the manifest topology, not about how many consumers read it. Family-6 still owns the prior question of how wide that topology needs to be.
- [d:r:i] Route-translation pressure interacts with family-6 rather than with consumer-chain asymmetry. A consumer-chain asymmetry slice that annotates silent write-side consumers with held-runtime awareness is not the same as translating `.claude` workflows. The two families should stay named-separately so a later consumer-chain slice does not silently become a covert translation slice.
- [d:r:i] The extraction route interacts with all of the above but does not yet have a live decision surface of its own. Its earliest useful next step is a bounded extraction-field map, not an extraction implementation.

## What Should Intensify Next

- [d:r:i] The primary bounded next move is a `consumer-chain asymmetry` proposal inside the uplift compatibility family. Its scope:
  - keep the read-only four out of the proposal's scope; they are already covered
  - map silent write-side and operator-routing carriers in the currently landed workflow/wrapper/registry space, using the propagation registry lanes `16`, `17`, `19-29`, `40`, and `43` as the inventory ([propagation-audit/43-uplift-compatibility-annotation-change-triggered-refresh.md](../../propagation-audit/43-uplift-compatibility-annotation-change-triggered-refresh.md:27))
  - decide, per carrier, whether held-runtime awareness should deepen inside the existing carrier, attach through a shared reference surface, or stay explicitly held
  - preserve `compatibility_posture: observed_basis_only` through whatever the proposal covers
  - stay inside the compatibility family rather than reaching into typed-carrier or translation territory
- [d:r:i] The secondary, parallelizable bounded next move is a family-6 wider route-asymmetry map. Its scope:
  - enumerate the Codex-only routes that are not yet part of the intervention-family three
  - classify each by whether its asymmetry is a translation question, a doctrine question, or a registry question
  - keep the classification as a field-disclosure artifact, not a translation plan
  - leave typed-carrier work held until that classification has traveled
- [d:r:i] A narrower third widening can travel inside `tooling/codex/project_uplift.py` without reopening `114` or `116`:
  - name the implementation-slice choice landed in `116` directly inside `116` itself so future readers see `narrow `.claude`-specific constant` as the live shape, not only as a possibility from `114`
  - record where the helper would change shape if a third runtime ever inherited held-runtime annotation (the `RUNTIME_DIRS` list at [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:73) already names `.gemini`, `.opencode`, `.kilo`, but `held_runtime_annotation` only reads `.claude`)
  - this is a carrier-clarity widening, not a refactor. It leaves the landed shape in place and makes the asymmetry between detection list and annotation reader durable rather than ambient.
- [d:r:i] The propagation refresh chain `16 -> 17 -> 43` should stay the active register for later compatibility movement rather than being compressed into one blended `compatibility family refreshed` label. If the consumer-chain asymmetry proposal lands, it will generate its own change-triggered refresh and extend this chain; that extension should stay typed rather than backfilled.

## What Should Remain Later

- [d:r:i] Structural-row promotion of the held-runtime object. Hold until several consumers are reading the JSON object structurally rather than through its summary string.
- [d:r:i] Dual-basis posture relabel. Hold as long as `compatibility_posture: observed_basis_only` continues to describe the real basis accurately. The held annotation does not move the basis.
- [d:r:i] Typed multi-runtime compatibility carrier separate from the uplift anchor. Hold pending family-6 mapping disclosure.
- [d:r:i] Live `.claude` route translation, `.claude` parity, or cross-runtime composition judgment. Hold until family-6 classification has separated translation questions from registry questions from doctrine questions.
- [d:r:i] Cross-runtime compatibility matrix, version-window claims, upstream-template drift compatibility. Hold as explicit entries in `compatibility_basis.held_later` ([UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:105)).
- [d:r:i] Third-runtime (`.gemini`, `.opencode`, `.kilo`) held-runtime annotation. Hold without forcing a generalization of the helper. The narrow `.claude` constant should remain the incumbent until a real third runtime carrier has earned annotation.
- [d:r:i] Extraction implementation work under the `115` route. Hold the implementation; the extraction-field map itself can be considered later, not now, and only after consumer-chain asymmetry has landed so the extraction route has one more worked compatibility-policy example to anchor against.
- [d:r:i] Any move that collapses `116`'s discipline into a `runtime-aware everywhere` parity push. The observed-basis discipline should continue to survive later widenings.

## How The Extraction Route Should Relate To This State

- [d:r:i] `115` remains correctly later, and `116` increases, not decreases, the evidence for that timing. Three specific reasons:
  - The helper chose narrow over general. A later extraction route would have to decide whether to inherit that narrowness or refactor it. That decision wants more than one held-runtime worked example to compare against, and `116` is the first and only such example.
  - The consumer chain is still asymmetric. An extracted installer's compatibility-policy shape cannot yet be factored cleanly because the write-side and operator-routing consumers have not yet inherited the held-runtime annotation. Factoring now would either overfit to the read-only pattern or invent consumer coverage that does not live in the repo.
  - Family-6 is still latent. Extraction wants to know whether the cross-runtime modifier layer's route surface is the current intervention-family three or meaningfully wider. That information is still ahead.
- [d:r:i] `116` does sharpen what a later extraction map can carry when it opens. Two concrete carry-forwards:
  - `observed_basis_only` plus a held-runtime annotation slot is a cleaner distribution contract than a symmetric multi-runtime matrix would be. The extracted installer could declare one observed runtime basis it was installed against, plus held annotations for other detected runtimes, without claiming parity.
  - The check-protocol list in [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:98) is a first draft of a compatibility-policy shape that the later extraction map can inherit rather than re-derive. It already includes both observed and held comparison, a rerun condition, and a refresh condition.
- [d:r:i] Extraction pressure should remain visible in the live-open-question register but should not be allowed to swallow the nearer consumer-chain asymmetry work. `115`'s own recommendation is not accelerated by `116`; it is made more specific.

## How This State Should Be Inherited

### Carry Forward

- [d:r:i] The `observed_basis_only` top-level compatibility posture as the continuing anchor label across `UPLIFT-REPORT.md`, `UPLIFT-MANIFEST.json`, `STATE.md`, and any later refreshes.
- [d:r:i] The held-scalar annotation shape as the landed widening of the anchor, paired with its typed JSON object inside the manifest and its scalar summary inside state and report prose.
- [d:r:i] The three-shape field — annotation posture, dual-basis posture, typed multi-runtime carrier — as an explicit option set, not a collapsed decision.
- [d:r:i] The four read-only current-runtime consumers ([progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md), [resume-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md), [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md), [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)) as the already-covered side of the consumer asymmetry, not to be re-touched by the next slice.
- [d:r:i] The helper-side narrow `.claude`-specific implementation-slice choice as the landed helper shape, with typed-carrier and runtime-dir-walker patterns still held.
- [d:r:i] The compatibility-check protocol's held-runtime comparison step as part of the protocol, not as optional commentary.
- [d:r:i] The `16 -> 17 -> 43` propagation-refresh chain as the typed register of compatibility-family movement.
- [d:r:i] The family-by-family posture. No silent collapsing of consumer-chain asymmetry, structural-row, family-6, route-translation, standalone-carrier, and extraction into one generic `cross-runtime improvement` lane.

### Revise Locally

- [d:r:i] Inside `116`, name the helper-side implementation-slice choice as `narrow .claude-specific constant` directly, in parallel with its existing Landed Shape description, so later readers do not have to reconstruct the choice from `114`'s held-choice paragraph plus the code.
- [d:r:i] Inside `116` or `43`, surface the asymmetry between the detection-list at [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:73) (which includes `.gemini`, `.opencode`, `.kilo`) and the annotation reader (which only reads `.claude`). The note is small; its absence would let a later third-runtime slice quietly assume parallel carrier coverage.
- [d:r:i] Inside the `Live Open Questions` list in [../../CURRENT-STATE.md](../../CURRENT-STATE.md:149), the question about which annotation sub-shape to land first is now answered by `116`. The replacement live question is which adjacent family to open next inside the compatibility family, not which shape to promote next inside the anchor.
- [d:r:i] Inside `117`, mark the move from `map the full adjacent field` toward `name the next bounded proposal` as now answerable, so the next-move note does not read as if the field map itself is still the open task.

### Keep Later

- [d:r:i] Structural-row promotion of the held-runtime object.
- [d:r:i] Dual-basis posture relabel.
- [d:r:i] Typed multi-runtime compatibility carrier separate from the uplift anchor.
- [d:r:i] Live `.claude` route translation or parity push.
- [d:r:i] Cross-runtime compatibility matrix, version-window claims, upstream-template drift compatibility.
- [d:r:i] Third-runtime held-runtime annotation (`.gemini`, `.opencode`, `.kilo`).
- [d:r:i] Extraction implementation and installer work under `115`.
- [d:r:i] A later standalone compatibility carrier outside uplift memory, unless later runtime-change slices show the embedded anchor straining.

### Next Bounded Move

- [d:r:i] Open one bounded `consumer-chain asymmetry` proposal inside the uplift compatibility family. Its scope is:
  - explicitly exclude the four read-only consumers already landed by `116`
  - enumerate silent write-side and operator-routing consumers using the propagation registry lanes `16 / 17 / 19-29 / 40 / 43` as the inventory
  - per carrier, classify the asymmetry as `deepen in place`, `attach through a shared reference`, or `explicitly held`
  - preserve `compatibility_posture: observed_basis_only` through the proposal
  - leave family-6 wider route-asymmetry mapping openable in parallel rather than silently sequenced behind this proposal
  - remain a proposal, not a live mutation of any operator-facing surface
- [d:r:i] Keep family-6 wider route-asymmetry mapping openable in parallel as a separately-authored field-disclosure lane.
- [d:r:i] Keep the narrower helper-clarity widening (naming the landed implementation-slice choice inside `116` and noting the detection-list versus annotation-reader asymmetry) available as a small local revision rather than as another proposal family.
- [d:r:i] Hold the extraction-field map from `115` until consumer-chain asymmetry has landed one worked example that an extracted installer's compatibility-policy shape can inherit from.
