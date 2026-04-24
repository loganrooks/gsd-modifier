# Immediate Implementation Plan

Date: 2026-04-24
Status: executable draft

## Objective

Stabilize the current `gsd-modifier` worktree after the audit import/reorganization and prepare the repo for the next deployable bridge-harness slice.

This immediate plan does not implement new bridge-harness behavior. It creates the stable ground required before that work can be done safely.

## Current Observed State

The worktree is mixed.

In-scope dirty surfaces:

- `docs/origin-audit/README.md`
- `tooling/codex/audit_refmap.py`
- `tooling/codex/tests/test_audit_refmap.py`
- imported audit/context under `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`
- imported readiness/research context under `.planning/readiness` and `.planning/research`

Known out-of-scope dirty surface:

- `tooling/portable-gsd/overlay/config.toml`

Potential unrelated dirty surfaces from previous work may include model-benchmark files. They must not be swept into this plan unless revalidated and explicitly adopted.

## Non-Goals

- Do not deploy into `prix-guesser`.
- Do not implement workflow-lane routing yet.
- Do not add new project-governance artifact generators yet.
- Do not rewrite the parity architecture.
- Do not broaden host matrix semantics before the audit/import state is stable.
- Do not delete imported audit content except clearly unwanted external clutter already identified by the user.

## Success Criteria

- The audit import is in `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign` with original identity preserved.
- The unwanted top-level `.planning/topology-map` import remains absent.
- `audit_refmap.py` supports batch move manifests that recalculate relative links inside moved source files.
- Reference rewrite is reproducible by script, not by one-off repair.
- Post-rewrite local missing-link count is compared against the pre-reorg baseline and explained.
- Tests cover moved-target rewriting and moved-source relative-link recalculation.
- Verification commands pass or failures are explicitly documented.
- Commits are split into reviewable buckets.

## Execution Strategy

### Step 0: Freeze Scope

Actions:

1. Record current `git status --short`.
2. Confirm `.planning/topology-map` is absent.
3. Confirm audit root exists at `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`.
4. Identify dirty files not owned by this plan.

Expected output:

- scope note in the implementation log or final execution summary

Pitfall:

- accidentally committing unrelated prior model-benchmark/config drift

### Step 1: Repair `audit_refmap.py` Batch Move Semantics

Actions:

1. Inspect current `rewrite_links`, `rewrite_workspace`, and `load_moves`.
2. Introduce a move index that can answer:
   - target moved by old absolute path
   - target moved by old repo-relative path
   - target moved by basename only when unambiguous
   - source file moved by current new absolute path
3. For each markdown link:
   - preserve label, brackets, and line suffix
   - skip URL, anchor, and dynamic-template targets
   - if target resolves to a moved old path, render destination relative to current source
   - else if source file was moved, resolve the old link from the old source path and re-render it relative to the new source path when the target still exists
4. Keep literal path rewriting as a separate pass.

TDD requirements:

- Add a test for source moved from root to nested directory while target is unchanged.
- Add a test for source moved and target moved.
- Add a test preserving line ranges during moved-source recalculation.
- Keep the duplicate-old-name same-target test.

Pitfalls:

- basename matching can be unsafe when duplicate filenames map to different destinations
- line suffix parsing can corrupt paths containing colons if implemented too broadly
- relative-link recalculation must use the old source parent, not the new source parent
- script must be idempotent enough that rerunning after partial repair does not create nonsense paths

Delegation:

- Do not delegate this step while the worktree is mixed unless a worker receives an explicit write scope limited to `tooling/codex/audit_refmap.py` and `tooling/codex/tests/test_audit_refmap.py`.
- If delegated, main thread must review the diff and disposition it as `accept`, `revise`, `park`, or `reject`.

### Step 2: Reproduce Reference Rewrite Through The Script

Actions:

1. Run:

```bash
python3 tooling/codex/audit_refmap.py rewrite . \
  --moves .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/reorganization-moves.tsv \
  --apply \
  --output .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/reorganization-rewrite-report.md
```

2. Run:

```bash
python3 tooling/codex/audit_refmap.py map \
  .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign \
  --output .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/reorganization-refmap-after.md
```

3. Compare counts against known reference points:
   - pre-reorg baseline: 798 markdown files, 7834 links, 7787 local existing, 47 local missing
   - current interrupted state: 800 markdown files, 7834 links, 7783 local existing, 51 local missing

Expected outcome:

- local missing links should return to the known baseline or any residual difference must be explained by generated report files or intentional import scope

Pitfalls:

- generated report markdown files can change file counts and link counts
- original imported missing references may point to absent sibling audit directories or old host paths
- do not claim all links are fixed unless the map proves it

### Step 3: Verify Tooling

Commands:

```bash
python3 -m unittest tooling.codex.tests.test_audit_refmap
python3 -m py_compile tooling/codex/audit_refmap.py
git diff --check
```

If contract-facing code is touched beyond `audit_refmap.py`, extend verification to relevant suites.

### Step 4: Stabilize Imported Audit Documentation

Actions:

1. Review `docs/origin-audit/README.md`.
2. Ensure it points to the `.planning/audits/...` location, not deleted wrapper paths.
3. Confirm it does not claim the top-level `.planning/topology-map` import exists.
4. Add a short note that the audit was imported into `.planning` to preserve relative-path assumptions.

Pitfalls:

- introducing new stale references while fixing old ones
- implying the imported audit is current runtime authority rather than carried origin context

### Step 5: Commit Buckets

Proposed commit buckets:

1. `Improve audit refmap batch move rewriting`
   - `tooling/codex/audit_refmap.py`
   - `tooling/codex/tests/test_audit_refmap.py`

2. `Import origin audit into planning`
   - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`
   - `.planning/readiness`
   - `.planning/research`
   - generated audit rewrite/refmap reports

3. `Document carried origin audit location`
   - `docs/origin-audit/README.md`

4. Separate or park unrelated changes:
   - `tooling/portable-gsd/overlay/config.toml`
   - any model-benchmark drift

Rules:

- Do not use `git add .`.
- Stage paths explicitly.
- Run `git diff --cached --stat` before each commit.
- Do not amend previous commits.

### Step 6: Create Follow-Up Planning Boundary

After the immediate stabilization commits:

1. Create or update a release-boundary note for the short-term bridge harness.
2. Route next implementation to runtime intervention surface inventory.
3. Do not start bridge behavior until the worktree is clean.

Candidate next artifact:

- `.planning/implementation-plans/<next-timestamp>/RUNTIME-INTERVENTION-SURFACES.md`

## Parallelization Plan

Parallel work is useful after Step 0, but only with disjoint write scopes.

Possible delegation:

- Worker A: implement and test `audit_refmap.py` batch source-move recalculation.
- Explorer B: read-only inventory of runtime intervention surfaces and instruction generation paths.
- Explorer C: read-only audit of imported missing links and baseline count deltas.

Do not delegate:

- commit staging
- final verification
- mixed-worktree cleanup decisions
- deletion of imported artifacts

Main thread responsibilities:

- maintain scope boundary
- review delegated diffs
- run verification
- decide commit buckets
- write final disposition summary

## Verification Matrix

| Area | Command | Required before commit |
| --- | --- | --- |
| Refmap tests | `python3 -m unittest tooling.codex.tests.test_audit_refmap` | yes |
| Syntax | `python3 -m py_compile tooling/codex/audit_refmap.py` | yes |
| Whitespace | `git diff --check` | yes |
| Refmap report | `python3 tooling/codex/audit_refmap.py map ...` | yes |
| Full deterministic CI | `bash scripts/ci/check-deterministic.sh` | before closing release boundary |
| Bootstrap CI | `bash scripts/ci/check-bootstrap.sh` | before closing release boundary |

## Audit Notes To Preserve During Execution

- Observed state and inferred explanation must stay separate.
- If missing-link count differs from baseline, record why.
- If a reference remains broken because it pointed outside the imported audit scope, record that as inherited baseline debt, not as fixed.
- If an imported artifact is intentionally not reorganized further, record that boundary.
- If a runtime parity surface is deferred, record the deferral explicitly.

