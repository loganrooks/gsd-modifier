# Phase 0 — Surface Cleanup

ID: `00-surface-cleanup`
Status: `pending`
Dependencies: none (this is the first phase)
Approval gates: none at slice level (slices are small and pre-spec'd)

## Objective

Clear the four observed drift items from the bootstrap gate's `hard_failures` list, lock the change-class trigger discipline into governance, and delete the now-ingested temp handoff. The phase produces a clean baseline against which the inject mechanism will be built.

## Rationale

Before any inject-mechanism work begins, three preconditions must hold:

1. The bootstrap gate must report zero `hard_failures` so subsequent phases can use "gate green" as a definitive signal. Today it tolerates 4 known stale-deleted carriers (3 skills + `research-phase.md`); that tolerance hides future drift behind a known-noise baseline.
2. The governance discipline (propose-evidence-approve for overlay/contract/governance changes) must be explicit so that `mode: inject` work — which will modify the manifest, the contract code, and overlay carriers — flows through approved channels.
3. The temp handoff (`docs/handoff/DELETE-AFTER-INGESTION-2026-04-24-release-readiness-and-plan-004.md`) must be removed; its durable contents have been absorbed into the orientation artifact and Plan 004 disposition update.

This is the lowest-risk phase. All slices are small. None require new infrastructure. They prepare the surface for the contract work in Phase 1+.

## Approach

Six slices in dependency order. Each slice produces one commit. Slices 1–4 reclassify the four stale carriers as `mode: add` from `harness_modifier/overlay/`. Slice 5 adds the change-class trigger taxonomy. Slice 6 deletes the temp handoff.

The reclassification approach for each carrier is identical:

1. Move (or copy if upstream still has the file) the existing source from `tooling/portable-gsd/overlay/<path>` to `harness_modifier/overlay/<path>`
2. Update `OVERLAY-MANIFEST.json` to change `mode: overwrite` → `mode: add`, both materializers if applicable, and update `source` to the new path
3. Run baseline gates
4. Commit

This preserves modifier-owned content without changing what materializes per runtime.

## Slice Catalog

### Slice 0 — Reconcile and attest baseline

- **Status**: `[ ]`
- **Type**: state reconciliation (produces a commit; the slice's WORK is the STATE.md edit)
- **Write set**:
  - `.planning/initiatives/inject-migration/STATE.md` → EDIT
  - `.planning/initiatives/inject-migration/checkpoints/<UTC-timestamp>-phase00-slice00.md` → CREATE
- **Action**: Reconcile STATE.md against git ground-truth (Last commit field; Status advance), attest worktree precondition, ensure refmap baseline is recorded in Out-Of-Scope Surfaces, and produce a commit. This is the first runtime turn after the `/goal` invocation; its purpose is to establish a clean attested baseline before any migration work.
- **Approach**:
  1. Read `git rev-parse HEAD` → call it `CURRENT_HEAD`
  2. Edit STATE.md fields per PROTOCOL.md "State-Update Protocol":
     - `Last updated` → current ISO-8601 UTC timestamp
     - `Last updated by` → `inject-migration /goal agent`
     - `Current Status → Status` → `in-progress` (was `pending`)
     - `Current Status → Slice within phase` → `1` (advance past this slice)
     - `Current Status → Last commit` → `<CURRENT_HEAD>` (will lag by one after this slice's commit — see PROTOCOL.md cold-start step 4 lag-by-one reconciliation)
     - `Current Status → Last checkpoint` → path to this slice's checkpoint
     - `Active Work → Current task` → `executing Phase 0 Slice 1 (reclassify gsd-do)`
     - `Active Work → Started` → current timestamp
     - `Counters → Slices complete` → 1 (was 0)
     - `Recent Checkpoints` → append a row for this slice (outcome `success`)
     - Confirm `Out-Of-Scope Surfaces` section exists with the refmap-baseline entry (idempotent — preserve if already present from a prior hard-stop reconciliation)
  3. Write the slice 0 checkpoint per PROTOCOL.md template (outcome `success`)
  4. Run verification gates (below)
  5. Commit
- **Verification**:
  - `git status --short --branch` shows only the modified STATE.md, the added checkpoint file, and the pre-condition untracked items
  - `git diff --check` clean
  - `python3 tooling/codex/audit_refmap.py snapshot .` runs to capture baseline (non-enforcing; exit code is NOT gated for this slice — see GUARDRAILS.md Required Discipline #8 known-baseline allowance)
- **Commit**:
  - Subject: `chore(state): reconcile inject-migration STATE.md with git ground-truth`
  - Body: includes `Why` (slice 0 baseline reconciliation), `Verification` (gates run), `Boundary` (no migration work; only state reconciliation), and the `Initiative: inject-migration phase 00 slice 0` trailer
- **Boundary**: This slice does NOT migrate any carrier. It does NOT touch contract code, manifest, or upstream files. It does NOT run the `audit_refmap.py verify .` gate (per Required Discipline #8 known-baseline allowance). It does NOT modify governance carriers.
- **Why** (for commit body): "Slice 0 is the first runtime turn after `/goal` invocation. Its job is to reconcile STATE.md against actual git ground-truth (placeholder fields become real SHAs; status advances from pending to in-progress) and to attest that the baseline matches the initiative's documented preconditions. The `audit_refmap.py verify .` gate is intentionally not enforced here — its known 8-item baseline (3 tool defects from gitignore-blind scanner; 5 stale audit-packet refs to upstream-deleted skill paths) is documented in STATE.md → Out-Of-Scope Surfaces #1 and accepted per the revised Required Discipline #8. Architectural fix is deferred to a separate reviewer-mediated initiative."
- **Checkpoint outcome**: `success` after commit lands

### Slice 1 — Reclassify `gsd-do` skill as modifier-owned

- **Status**: `[ ]`
- **Type**: overlay carrier change (per GUARDRAILS, governance-approval-required; pre-authorized by this slice spec)
- **Write set**:
  - `tooling/portable-gsd/overlay/skills/gsd-do/SKILL.md` → DELETE (move the file)
  - `harness_modifier/overlay/skills/gsd-do/SKILL.md` → CREATE (move target; same content)
  - `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` → EDIT (entry `skills/gsd-do/SKILL.md`: `mode: overwrite` → `mode: add`; `source: tooling/portable-gsd/overlay/skills/gsd-do/SKILL.md` → `harness_modifier/overlay/skills/gsd-do/SKILL.md`)
- **Approach**:
  1. Read the current SKILL.md content
  2. Create the new file at `harness_modifier/overlay/skills/gsd-do/SKILL.md` with identical content
  3. Delete the old file at `tooling/portable-gsd/overlay/skills/gsd-do/SKILL.md`
  4. Edit `OVERLAY-MANIFEST.json` entry — changes inside the `materializers.codex` block: `mode` and `source` fields only
- **Verification**:
  - `git diff --check` clean
  - `python3 tooling/codex/audit_refmap.py verify .` exit 0
  - `python3 -c "import json; m = json.load(open('tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json')); e = m['entries']['skills/gsd-do/SKILL.md']; assert e['materializers']['codex']['mode'] == 'add'; assert e['materializers']['codex']['source'] == 'harness_modifier/overlay/skills/gsd-do/SKILL.md'; print('manifest entry correct')"`
  - The moved file exists and has identical content to the deleted one (`diff` between pre-move snapshot and new file produces no output — implicit since we used Move semantics)
- **Commit**:
  - Subject: `refactor(overlay): reclassify gsd-do skill as modifier-owned add`
  - Body must include `Why`, `Verification`, `Boundary`, plus `Initiative: inject-migration phase 00 slice 1` trailer
- **Boundary**: This slice does NOT add the bootstrap gate test that the hard_failure is gone — that's confirmed by Slice 4's exit verification after all four carriers are reclassified. This slice does NOT touch the bootstrap or determinism gates (state-mutating; deferred to Slice 4).
- **Why** content (for commit body): "The orientation artifact §4.2 confirmed `gsd-do` was deleted upstream in #2790 (absorbed into `progress --do`). The bootstrap gate empirically attests this as a `hard_failure: 4 overwrite entries are missing from fresh live .codex`. Reclassifying to `mode: add` from a `harness_modifier/overlay/` source clears the hard_failure while preserving the modifier-owned skill content (modifier still ships `gsd-do` for its own users)."

### Slice 2 — Reclassify `gsd-from-gsd2` skill as modifier-owned

Same shape as Slice 1, target `gsd-from-gsd2`.

- **Write set**:
  - `tooling/portable-gsd/overlay/skills/gsd-from-gsd2/SKILL.md` → DELETE
  - `harness_modifier/overlay/skills/gsd-from-gsd2/SKILL.md` → CREATE
  - `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` → EDIT (entry `skills/gsd-from-gsd2/SKILL.md`)
- Verification, Commit, Boundary, Why: identical pattern to Slice 1, substituting `gsd-from-gsd2`
- **Status**: `[ ]`

### Slice 3 — Reclassify `gsd-plant-seed` skill as modifier-owned

Same shape as Slice 1, target `gsd-plant-seed`.

- **Write set**:
  - `tooling/portable-gsd/overlay/skills/gsd-plant-seed/SKILL.md` → DELETE
  - `harness_modifier/overlay/skills/gsd-plant-seed/SKILL.md` → CREATE
  - `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` → EDIT (entry `skills/gsd-plant-seed/SKILL.md`)
- Verification, Commit, Boundary, Why: identical pattern to Slice 1, substituting `gsd-plant-seed`
- **Status**: `[ ]`

### Slice 4 — Reclassify `research-phase` workflow as modifier-owned

This one is slightly different because it's a workflow file (under `get-shit-done/workflows/`) rather than a skill, AND because the manifest declares both `codex` and `claude` materializers (per `core_required` parity_tier).

- **Status**: `[ ]`
- **Write set**:
  - `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md` → DELETE
  - `harness_modifier/overlay/get-shit-done/workflows/research-phase.md` → CREATE
  - `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` → EDIT (entry `get-shit-done/workflows/research-phase.md`: BOTH `codex` and `claude` materializers' `mode: overwrite` → `mode: add` and `source` updated to new path)
- **Approach**:
  1. Move the file
  2. Edit both materializer entries (codex and claude); confirm both updated
  3. Verify
- **Verification**: same baseline gates plus:
  - `python3 -c "import json; m = json.load(open('tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json')); e = m['entries']['get-shit-done/workflows/research-phase.md']; assert all(e['materializers'][r]['mode'] == 'add' for r in ('codex', 'claude')); assert all('harness_modifier/overlay/' in e['materializers'][r]['source'] for r in ('codex', 'claude')); print('manifest entry correct')"`
- **Commit**: `refactor(overlay): reclassify research-phase workflow as modifier-owned add`
- **Boundary**: This is the last reclassification slice. After this slice's commit, both bootstrap and deterministic gates should report zero `hard_failures`. The next slice (5) is governance, not overlay.
- **Why**: "The orientation artifact §4.4 flagged `research-phase.md` as needs-check; intervention-strategies §1.5 confirmed it is absent from upstream `origin/main`. Bootstrap gate attests via `hard_failures` list. Reclassifying as `mode: add` (both runtimes) clears the hard_failure while preserving the workflow content modifier still wants to ship."

### Slice 5 — Add change-class trigger taxonomy to AGENTS.md and CLAUDE.md

This slice adds a governance discipline that future overlay/contract/manifest changes invoke. It pre-authorizes the inject-migration phases that touch contract code by making "overlay carrier change" and "contract surface change" explicit triggers.

- **Status**: `[ ]`
- **Type**: governance carrier change (per GUARDRAILS.md, requires explicit pre-spec'd write set; this slice spec is that authorization)
- **Write set**:
  - `AGENTS.md` → EDIT (add a new subsection under "Workflow Rules" titled "Change-Class Triggers")
  - `CLAUDE.md` → EDIT (add a parallel subsection acknowledging the AGENTS.md anchor)
  - `.planning/initiatives/inject-migration/posture-triggers.md` → CREATE (the operational checklist version)
- **Content for AGENTS.md addition** (at end of "Workflow Rules" section, before "Contract Propagation"):

```markdown

### Change-Class Triggers

The propose-evidence-approve discipline applies in full to changes in any of the following classes. Slice specs in approved plans pre-authorize specific changes within these classes; ad hoc changes outside a pre-authorized spec require explicit operator approval.

1. **Overlay carrier add/remove** — changes to `OVERLAY-MANIFEST.json` entries or files under `tooling/portable-gsd/overlay/` (and `harness_modifier/overlay/`)
2. **Contract surface change** — anything under `harness_modifier/contract/`, `tooling/codex/audit_refmap.py`, `tooling/codex/scan_threshold_language.py`
3. **Install/bootstrap script change** — `scripts/setup-portable-gsd*.sh`, `scripts/ci/check-*.sh`
4. **Governance carrier change** — `AGENTS.md`, `CLAUDE.md`, `WORKFLOW.md`, `docs/handoff/current.md`, `.planning/STATUS.md`, `.planning/CURRENT-STATE.md`
5. **Plan disposition or premise change** — `evidence/decision.md`, `evidence/implementation-disposition.md`, any decision artifact

Out of scope (small mechanical fixes proceed per §58):

- Documentation typos with no semantic change
- Test additions confirming existing behavior
- Comment-only changes
- Whitespace/formatting confined to one file
```

- **Content for CLAUDE.md addition** (in the "Workflow Discipline" section, append):

```markdown

The change-class trigger taxonomy in AGENTS.md "Workflow Rules → Change-Class Triggers" applies under Claude. The five classes (overlay carrier, contract surface, install/bootstrap, governance, plan disposition) are runtime-neutral.
```

- **Content for `posture-triggers.md`**: a short operational checklist (~50 lines) restating the five classes with examples and pointing back to AGENTS.md as authoritative.
- **Verification**:
  - `git diff --check` clean
  - `python3 tooling/codex/audit_refmap.py verify .` exit 0
  - `python3 tooling/codex/scan_threshold_language.py --ignore-meta-instruction-lines AGENTS.md CLAUDE.md` exit 0
- **Commit**: `docs(governance): add change-class triggers for overlay and contract changes`
- **Boundary**: This slice adds the trigger taxonomy but does NOT add `mode: inject` as a trigger class — that's added in Phase 1's ADR slice once the schema design exists. This slice does NOT modify other AGENTS.md / CLAUDE.md sections.
- **Why**: "Phase 0–10 of the inject migration will repeatedly modify overlay carriers, contract code, and the manifest. Making the propose-evidence-approve discipline explicit for these classes prevents drift into hidden-architecture territory and pre-authorizes the slice-spec'd changes by clearly identifying which class each falls under."

### Slice 6 — Delete temp handoff

- **Status**: `[ ]`
- **Type**: governance carrier deletion (its delete-after-ingestion contract is satisfied)
- **Write set**:
  - `docs/handoff/DELETE-AFTER-INGESTION-2026-04-24-release-readiness-and-plan-004.md` → DELETE
- **Approach**:
  1. Confirm prerequisites: orientation artifact has absorbed durable content (visible: `.planning/readiness/release-readiness-orientation-2026-05-08.md` exists; orientation §3 contains the corrected Plan 004 premise; intervention-strategies analysis exists; Phase 0 Slice 5 has added the change-class triggers); confirm via `ls .planning/readiness/`
  2. Delete the file via `git rm`
- **Verification**:
  - `git status --short` shows only the deletion staged
  - `git diff --check` clean
  - `python3 tooling/codex/audit_refmap.py verify .` exit 0 (the file was untracked, so deletion does not affect refmap)
- **Commit**: `chore(handoff): delete ingested temp handoff for plan 004`
- **Boundary**: Only the temp handoff is deleted. `docs/handoff/current.md` remains as the live re-entry document.
- **Why**: "The 2026-04-24 temp handoff explicitly carried a delete-after-ingestion instruction. The durable content has been absorbed: Plan 004 disposition correction lives in `evidence/implementation-disposition.md` (§7.1 of orientation; commit f110436); upstream-gap evidence and proposed next moves live in the orientation artifact (commit 97f00a2); change-class triggers are in AGENTS.md/CLAUDE.md (this initiative's Slice 5). The temp handoff has served its purpose; deleting it removes the second-current.md risk."

## Exit Criteria (phase boundary)

After Slice 6 commits, the phase is complete when:

1. **All slices marked `[x]`** in this file (operator-confirmable; the agent updates `[ ]` → `[x]` after each successful slice)
2. **Bootstrap gate hard_failures = 0** — verified by running `bash scripts/ci/check-bootstrap.sh` (state-mutating; phase-boundary authorized) and confirming the JSON output's `hard_failures` array is `[]`
3. **Deterministic gate clean** — `bash scripts/ci/check-deterministic.sh` exit 0 with no `hard_failures`, no `missing_*`
4. **STATE.md updated**: Phase 0 box marked `[x]`; Phase advanced to 1; counters reflect `Carriers reclassified to mode: add: 4 / 4`; `Bootstrap gate hard_failures: 0`

## Phase Boundary Verification

```bash
# State-mutating; authorized at phase boundary only
bash scripts/ci/check-deterministic.sh
bash scripts/ci/check-bootstrap.sh

# Confirm hard_failures is empty (parse the JSON output)
python3 -c "
import json, subprocess
out = subprocess.run(
    ['python3', 'harness_modifier/contract/portable_gsd_contract.py', 'apply-overlay', '.', '--all-supported'],
    capture_output=True, text=True
).stdout
# (Adjust extraction if the script wraps output; this is a sketch — use the actual gate's last JSON)
print('Phase boundary check: hard_failures must be []')
"
```

The phase-boundary verification is run by the agent in a SEPARATE iteration after Slice 6's commit lands. The agent does NOT run it within Slice 6 because the bootstrap gate is state-mutating and would pollute the slice's worktree.

## Boundary

- This phase does NOT touch contract code, the inject mechanism, or any code in `harness_modifier/contract/`. Those are Phases 1–2.
- This phase does NOT migrate any carrier to `mode: inject`. The 4 carriers move from `mode: overwrite` to `mode: add`, not to `mode: inject`.
- This phase does NOT modify upstream files or the upstream clone.
- This phase does NOT publish the modifier to any external system.
- This phase does NOT investigate the `gsd-progress` declaration anomaly (intervention-strategies §1.6); that's deferred to Phase 1 if it surfaces during ADR work, or to a follow-up if not.

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| A reclassified file's content is ALREADY drifted from upstream's last-known-good state, and moving it to `mode: add` locks in the drift | medium | low (modifier was already shipping the drifted content) | accept; record in commit body that the content reflects modifier's prior copy |
| The manifest validation tool flags `mode: add` for a carrier whose target path overlaps with an upstream-synthesized path | low (upstream synthesizes only via its installer; modifier's add lands in materialized runtime root) | medium | if it surfaces, hard-stop and ask operator |
| The temp handoff's delete-after-ingestion contract is interpreted as "ingestion required by all consumers, not just the operator" | low | low (the handoff's content is in the orientation artifact and PR documentation) | the orientation artifact and Plan 004 disposition together preserve every durable piece of the temp handoff |
| Bootstrap gate's "hard_failures" continues to report after all four reclassifications | medium | medium | indicates a fifth drift item we missed; treat as new evidence; pause and re-orient |
| AGENTS.md / CLAUDE.md edits surface a `scan_threshold_language.py` finding | low | low | edit phrasing to avoid threshold language; re-run scanner |
| The pre-existing refmap baseline (8 unclassified items since 73f130d 2026-05-08) drifts during phase work, introducing additional unclassified items | low | medium | per-slice gates require no NEW unclassified items per the revised Required Discipline #8; the 8-item baseline is documented in STATE.md → Out-Of-Scope Surfaces #1; root-cause architectural fix (gitignore-aware `audit_refmap.py:iter_markdown_files`) is deferred to a separate reviewer-mediated initiative outside this scope |

## Notes For Future Iterations

- The 4 reclassified files become the first `harness_modifier/overlay/skills/...` and `harness_modifier/overlay/get-shit-done/workflows/...` carriers under `mode: add` for these path families. Future inject migration work in Phases 4–7 may co-locate similar modifier-owned content alongside.
- The change-class trigger taxonomy added in Slice 5 will get a sixth class entry in Phase 1's ADR slice: `mode: inject` carrier addition or operation-library change.
