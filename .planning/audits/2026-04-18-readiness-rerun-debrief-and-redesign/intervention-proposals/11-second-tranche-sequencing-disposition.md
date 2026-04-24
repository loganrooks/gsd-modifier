Date: 2026-04-20
Status: active sequencing disposition

# Second Tranche Sequencing Disposition

## Purpose

- [g:r:i] This note decides how to inherit the three still-live second-tranche pressures together rather than pretending they are unrelated options:
  - finer runtime-visibility splitting
  - stale-agent cleanup
  - durable snapshot discipline
- [d:r:i] The question is not which one wins forever. The question is what order gets this repo closer to the strongest harness across maintainability, runtime legibility, update resilience, intervention leverage, and operator speed.

## What The Current Evidence Now Says

- [e:c+i] The sharpened runtime-visibility report no longer leaves the main pressure inside one generic `selective overlay boundary` bucket. The current repo run resolves that pressure mainly into `133` upstream-shipped boundary surfaces, `12` install-mutation boundary surfaces, and `16` untracked live-only boundary surfaces, with `0` current unknown drift and `0` currently evidenced obsolete residue. Sources: [01-runtime-visibility-report.json](../tranche-audit/artifacts/01-runtime-visibility-report.json:6), [01-runtime-visibility-report.json](../tranche-audit/artifacts/01-runtime-visibility-report.json:15).
- [d:r:i] That means the next discriminating surface is not a repo-wide drift mystery. It is the remaining `16`-surface live-only cohort.
- [e:r:i] That cohort is not mixed across many families. It is entirely `agent_toml` carry:
  - `gsd-advisor-researcher`
  - `gsd-ai-researcher`
  - `gsd-assumptions-analyzer`
  - `gsd-code-fixer`
  - `gsd-code-reviewer`
  - `gsd-debug-session-manager`
  - `gsd-doc-classifier`
  - `gsd-doc-synthesizer`
  - `gsd-domain-researcher`
  - `gsd-eval-auditor`
  - `gsd-eval-planner`
  - `gsd-framework-selector`
  - `gsd-intel-updater`
  - `gsd-pattern-mapper`
  - `gsd-security-auditor`
  - `gsd-user-profiler`

## Cohort Split

### 1. Runtime-addressed live-only cohort

- [e:r:i] Seven of the `16` are already explicitly addressed in the tracked overlay config surface even though they remain live-only agent files:
  - `gsd-advisor-researcher`
  - `gsd-assumptions-analyzer`
  - `gsd-code-fixer`
  - `gsd-code-reviewer`
  - `gsd-intel-updater`
  - `gsd-security-auditor`
  - `gsd-user-profiler`
- [d:r:i] These are not first-pass deletion candidates. They are active runtime-authority surfaces whose live-only status reflects current overlay-boundary shape rather than obvious residue.

### 2. Workflow- or template-backed live-only cohort

- [e:r:i] The remaining `9` do not appear in tracked overlay `config.toml`, but they are still referenced by live workflow, template, or reference surfaces:
  - `gsd-ai-researcher`
  - `gsd-debug-session-manager`
  - `gsd-doc-classifier`
  - `gsd-doc-synthesizer`
  - `gsd-domain-researcher`
  - `gsd-eval-auditor`
  - `gsd-eval-planner`
  - `gsd-framework-selector`
  - `gsd-pattern-mapper`
- [d:r:i] These are not obvious residue either. They need a routing/authority pass first:
  - are they intentionally live-only,
  - should they gain tracked overlay carry,
  - or are they partially orphaned and therefore cleanup candidates?

## Sequencing Decision

### 1. First move: classify the `16`-agent cohort more finely

- [d:r:i] Do this first.
- [d:r:i] The current `untracked_live_only_outside_overlay_subset` bucket should be split into a retention/cleanup matrix with at least:
  - `runtime-addressed live-only`
  - `workflow-backed live-only`
  - `orphaned / retire-candidate`
  - `needs overlay-canon consideration`
- [d:r:i] This is the highest-leverage move because it sharpens all later work at once.

### 2. Second move: run bounded stale-agent cleanup only where the matrix earns it

- [d:r:i] Do this second.
- [d:r:i] Cleanup is still real pressure, but it should follow classification, not replace it.
- [d:r:i] The correct cleanup target is not `all live-only agents`. It is only the subset that proves to be:
  - stale by routing evidence,
  - superseded by newer surfaces,
  - or kept alive only by dead references.

### 3. Third move: add durable snapshot discipline for selected lanes

- [d:r:i] Do this third as a narrower carry layer, not as a repo-wide fossilization step.
- [d:r:i] Snapshot discipline gets stronger after the cohort cleanup pass because then we are freezing a cleaner runtime truth surface rather than preserving clutter and unresolved agent carry.
- [d:r:i] The right initial scope is selected high-stakes audit/intervention lanes, not every ordinary local edit.

### 4. Fourth move: revisit manifest/install coherence on the cleaner baseline

- [d:r:i] Manifest/install coherence remains important, but it becomes more discriminating after:
  - the live-only agent cohort is typed,
  - obvious residue is retired,
  - and selected lane snapshots can show what final runtime truth actually looked like at a decision point.

## Why This Order Is Stronger

### Maintainability

- [d:r:i] Classification first avoids turning legitimate live-only carry into accidental deletion pressure.
- [d:r:i] Cleanup second reduces long-term runtime clutter, stale references, and re-litigation load.
- [d:r:i] Snapshot discipline after cleanup avoids institutionalizing avoidable mess.

### Runtime Legibility

- [d:r:i] The current report already removed most mystery from the broad bucket.
- [d:r:i] The next real gain comes from typing the remaining live-only agent cohort more sharply, not from jumping straight to global snapshots.

### Update Resilience

- [d:r:i] Keeping manifest/install coherence later in the sequence preserves the semantic split already earned:
  - updater/custom-file boundary truth
  - tracked subset-carry metadata
  - final runtime visibility
- [d:r:i] Coherence work will be stronger after the runtime-authority cohort itself is cleaner.

### Intervention Yield

- [d:r:i] This order gives future harness work a better surface for deciding:
  - what should gain overlay canon,
  - what should remain explicitly live-only,
  - and what should be retired.

### Operator Speed

- [d:r:i] A cleaner live-only agent fleet plus selected snapshots will speed later debugging and review more than a larger early snapshot regime over unresolved clutter.

## What This Rejects

- [d:r:i] Reject `snapshots first, figure out the cohort later`.
- [d:r:i] Reject `cleanup first, ask what was active later`.
- [d:r:i] Reject treating the three pressures as equivalent backlog items with no dependency order.

## Accepted Path

- [g:r:i] Do all three, but in this order:
  1. live-only agent cohort matrix
  2. bounded stale-agent cleanup where earned
  3. durable snapshot discipline for selected lanes
  4. then cleaner manifest/install coherence follow-through

## Immediate Next Move

- [g:r:i] Write the live-only agent cohort matrix next and use it to decide whether any of the `16` current `agent_toml` surfaces are genuinely orphaned, merely selective live-only carry, or strong candidates for later overlay-canon expansion.
