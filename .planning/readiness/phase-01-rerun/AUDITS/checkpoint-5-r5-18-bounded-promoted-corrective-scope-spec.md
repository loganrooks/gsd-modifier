# Checkpoint 5 R5.18 Bounded Promoted Corrective Scope Spec

This artifact formalizes what `R5.18` is after the completed `R5.17e` and `R5.19d/e` stacks.

It is still not the patch plan itself.

It is the revised boundary-setting artifact that says:

- what is safely `first-wave`
- what must be explicitly dispositioned
- what must be resolved as scope-gating before patch work begins
- what remains defended exclusion
- and what contradiction ledger must exist if a live item is kept out of first-wave repair

## Why This Exists

Checkpoint 5 did not move in a straight line.

The actual sequence was:

1. Checkpoint 4 proved that the repo still had rerun-blocking harness weaknesses in workflow-chain follow-through, review/closure posture, and authority/routing semantics.
2. The first bounded Checkpoint 5 implementation slice was real work, but too narrow.
3. The implementation spec itself then had to be revised through a spec-stack audit bundle before it was safe to govern implementation.
4. `R5.16` audited propagation on the live Track B / Track C candidate bundle and showed that `keep it local` no longer survived, but it did not yet produce a clean enough promoted boundary to govern edits.
5. `R5.17` then challenged the exclusion judgments directly.
6. `R5.17e` concluded that `R5.18` was required, but only if the package separated evidence grades explicitly.
7. `R5.19` then challenged the broader exclusion / non-modification frontier directly across repo-local GSD and adjacent governance.
8. `R5.19d/e` concluded that provisional `R5.18` can now be revised and governed, but only as:
   - a widened explicit-disposition and scope-gating frontier
   - not as a settled final exclusion map
   - and not as a basis for broad new `Bucket 1` widening

So the job of `R5.18` now is:

- keep `Bucket 1` narrow and evidence-weighted
- materially widen `Bucket 2`
- convert the hardest live boundaries into explicit `Bucket 3` decisions
- shrink defended exclusion to the narrow set actually earned
- require contradiction-ledger entries for anything kept outside first-wave after entering `Bucket 2` or `Bucket 3`
- forbid the new exclusion heuristics from becoming standing doctrine

## Governing Inputs

1. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
2. [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
3. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
4. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
5. [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
6. [checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md)
7. [checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md)
8. [checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md)
9. [checkpoint-5-r5-19e-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19e-adjudication-reread-internal-r1.md)

## Core Meaning Of `Bounded`

`Bounded` here does not mean:

- smallest possible patch set
- narrow by habit
- stay near the original Track B / Track C files no matter what later evidence showed

`Bounded` here now means:

- keep `Bucket 1` to the convergent patch-now trunks that still survive after `R5.19e`
- widen `Bucket 2` and `Bucket 3` to absorb the files and boundary choices that can no longer be parked by cheap exclusion
- do not treat `R5.19` as a settled final exclusion map
- do not convert every newly surfaced file into first-wave repair
- require explicit contradiction ownership whenever a live boundary item stays out of first-wave

So `R5.18` is bounded around the earned corrective frontier between:

1. convergent first-wave corrective trunks
2. mandatory explicit-disposition surfaces
3. scope-gating decisions that must be resolved before patch work begins
4. governing authorities that must be read as authority but are not current edit-now targets
5. narrow defended exclusions and preserve-only seams

## Bucket 1: Convergent First-Wave Corrective Trunks

These are the promoted patch-now surfaces currently supported by the strongest surviving evidence.

### 1A. Review / Planning Consumer Chain

- `.codex/skills/gsd-review/SKILL.md`
- `.codex/skills/gsd-plan-phase/SKILL.md`
- `.codex/get-shit-done/workflows/review.md`
- `.codex/get-shit-done/references/planner-reviews.md`
- `.codex/get-shit-done/workflows/plan-phase.md`

Why still first-wave:

- this chain already survived `R5.17e` as safe to govern
- `R5.19d/e` did not produce evidence for broadening it by synthesis habit

### 1B. Chain-Tail Producer / Routing Trunk

- `tooling/portable-gsd/overlay/agents/gsd-verifier.toml`
- `.codex/get-shit-done/references/verification-overrides.md`
- `tooling/portable-gsd/overlay/agents/gsd-executor.toml`
- `.codex/get-shit-done/references/agent-contracts.md`
- `.codex/get-shit-done/bin/lib/phase.cjs`
- `.codex/get-shit-done/bin/lib/roadmap.cjs`
- `.codex/get-shit-done/workflows/progress.md`
- `.codex/get-shit-done/workflows/transition.md`

Why still first-wave:

- `R5.19d4` keeps this eight-file trunk as the convergent minimum chain-tail repair set
- `R5.19e` explicitly refuses broad `Bucket 1` widening beyond that evidence-backed core

## Bucket 2: Mandatory Explicit-Dispositions

These are in `R5.18` scope and cannot be silently excluded.

They are not all automatically first-wave edits, but each requires an explicit on-record disposition such as:

- `promote-now`
- `park-with-trigger`
- `accepted bounded risk`
- `pressure-only pending targeted reread`

### 2A. Skills / Wrappers / Workflow Routers

- `.codex/skills/gsd-verify-work/SKILL.md`
- `.codex/skills/gsd-execute-phase/SKILL.md`
- `.codex/skills/gsd-research-phase/SKILL.md`
- `.codex/skills/gsd-autonomous/SKILL.md`
- `.codex/skills/gsd-ship/SKILL.md`
- `.codex/skills/gsd-next/SKILL.md`
- `.codex/skills/gsd-do/SKILL.md`
- `.codex/get-shit-done/workflows/verify-work.md`
- `.codex/get-shit-done/workflows/next.md`
- `.codex/get-shit-done/workflows/resume-project.md`
- `.codex/get-shit-done/workflows/manager.md`
- `.codex/get-shit-done/workflows/ship.md`
- `.codex/get-shit-done/workflows/autonomous.md`

Rules:

- none may remain ambient
- `gsd-research-phase` is the sharpest live boundary and cannot be parked by silence
- `gsd-do` / `gsd-audit-uat` style router-pair asymmetry must be handled explicitly rather than by wrapper-only convenience

### 2B. References / Templates / Runtime-Control Surfaces

- `.codex/get-shit-done/references/checkpoints.md` outside the bounded TDD-only subsection
- `.codex/get-shit-done/templates/summary.md`
- `.codex/get-shit-done/bin/lib/commands.cjs`
- `.codex/get-shit-done/bin/lib/uat.cjs`
- `.codex/get-shit-done/bin/lib/audit.cjs`
- `.codex/get-shit-done/references/planner-source-audit.md`
- `.codex/get-shit-done/references/UAT.md`
- `.codex/get-shit-done/references/VALIDATION.md`
- `.codex/agents/gsd-executor.toml`
- `.codex/agents/gsd-verifier.toml`
- `.codex/get-shit-done/bin/lib/core.cjs`
- `.codex/get-shit-done/bin/lib/init.cjs`
- `.codex/get-shit-done/bin/lib/verify.cjs`
- `.codex/agents/gsd-code-reviewer.toml`

Rules:

- overlay-only treatment is no longer sufficient
- live `.codex/agents` counterparts must be explicitly considered when their overlay pair is already inside active scope
- `commands.cjs` / `summary.md` still carry stronger standing than `uat.cjs` / `audit.cjs`, but none may disappear by omission

### 2C. Governance / Semantic Uptake Surfaces

- reviewer-prompt tightening
- exact review / debt vocabulary disposition
- `PROTOCOL.md` disposition-ladder alignment versus justified divergence
- runtime uptake of `REVIEW-TEMPLATE.md` and `REVIEW-POLICY.yaml` semantics where needed
- explicit final status for `WORKFLOW.md`
- explicit final status for `AI-GUARDRAILS.md`
- explicit final status for `ARTIFACT-GOVERNANCE.md`

Rules:

- blanket `Bucket 4` shelter fails here
- source authority can stay `governing_authority_not_edit_now`
- but downstream semantic uptake cannot hide behind that source-authority shelter

## Bucket 3: Scope-Gating Decisions That Must Be Resolved Before Patch Work Begins

These are not ordinary file edits. They are decisions that final `R5.18` itself must carry before implementation starts.

1. Debt-carrier mechanism choice
   - fourth terminal state
   - side field
   - or both

2. Final `gsd-research-phase` classification
   - first-wave
   - bounded non-promotion
   - or park-with-trigger

3. Wave placement / severity boundary for:
   - `ship.md`
   - `autonomous.md`
   - non-TDD `checkpoints.md`
   - `summary.md`

4. Router-pair treatment
   - pair `gsd-do` with `workflows/do.md` or defend wrapper-only sufficiency
   - pair `gsd-audit-uat` with `audit-uat.md` or defend wrapper-only sufficiency

5. Research / steering control-surface classification
   - `gates.md`
   - `revision-loop.md`
   - paired `gate-prompts.md`
   - live researcher / planner / checker pairing
   - `.codex/agents/gsd-code-reviewer.toml`

6. `R5.7` split
   - active touched-surface overlay/materialization slice
   - versus parked broader hardening remainder

7. `R5.8` explicit decision
   - reaffirm named accepted bounded risk
   - or reopen the narrow branch/worktree verification lane

8. New heuristic restriction
   - `authority vs must-edit-now`
   - `intersection-not-union`
   - `mandatory conditional disposition`
   These may guide reading, but must not become standing doctrine or exclusion-justification until adversarially tested.

9. Contradiction-ledger rule
   Anything kept outside first-wave after entering `Bucket 2` or `Bucket 3` must carry:
   - the live contradiction left open
   - the reason it is not first-wave
   - the owner
   - the reopen trigger

## Bucket 4: Governing Authorities, Not Current Edit-Now Targets

These must govern `R5.18` work but are not themselves presumptive patch sites on current evidence:

- [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
- [AUDIT-SPEC-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-SPEC-TEMPLATE.md)
- [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
- [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md)
- [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml)

Meaning:

- these are authoritative inputs to the patch wave
- they should not be silently ignored
- they are not to be rewritten just because they are load-bearing
- but their runtime or downstream uptake can still enter `Bucket 2` / `Bucket 3`

## Bucket 5: Narrow Defended Exclusions And Preserve-Only Seams

These remain outside current first-wave `R5.18` edit scope, but only with explicit reasons.

### 5A. Narrow Defended Exclusions

- `.codex/skills/gsd-discuss-phase/SKILL.md`
- the bounded TDD-only subsection of `.codex/get-shit-done/references/checkpoints.md`
- `.codex/get-shit-done/references/research.md` as explicit `park-with-trigger`
- `.codex/get-shit-done/references/phase-prompt.md` as explicit `park-with-trigger`
- `tooling/codex/capture_launch_truth.py`
- narrow rerun-path separate reference/template remainders
- narrow non-phase-critical `.codex/agents` remainders

### 5B. Preserve-Only Seams / Honest Later Lanes

- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `R5.9`
- `R5.10`

Rule:

- nothing else should be spoken of as defended exclusion unless it survives the same burden
- omission or family resemblance is not enough

## Contradiction Ledger Requirement

If any file or lane in `Bucket 2` or `Bucket 3` stays outside first-wave repair, final `R5.18` must record:

1. the live contradiction being left open
2. the reason the item is not first-wave
3. the owner of that contradiction
4. the reopen trigger

This is mandatory for at least the currently named live items:

- `gsd-research-phase/SKILL.md`
- `ship.md`
- `autonomous.md`
- non-TDD `checkpoints.md`
- `summary.md`
- `research.md`
- `phase-prompt.md`
- `WORKFLOW.md`
- broader remainder of `R5.7`
- `R5.8`
- `.codex/agents/gsd-code-reviewer.toml`

## Anti-Misread Rules

- Do not read `R5.19` as a license for broad new `Bucket 1` widening.
- Do not read `R5.19` as a settled final exclusion map.
- Do not let router-pair asymmetry slip back into silence.
- Do not use the new exclusion heuristics as standing doctrine.
- Do not treat source authority as a blanket shield against downstream semantic uptake obligations.

## Immediate Next Action

Before any corrective patch wave begins:

1. write the actual `R5.18` launch / implementation spec from this revised boundary
2. make the `Bucket 2` / `Bucket 3` classifications and contradiction-ledger structure operational
3. only then begin the corrective patch wave
