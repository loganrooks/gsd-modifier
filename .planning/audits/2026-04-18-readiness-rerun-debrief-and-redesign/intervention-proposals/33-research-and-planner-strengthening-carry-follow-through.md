Date: 2026-04-21
Status: landed follow-through

# Research And Planner Strengthening-Carry Follow-Through

## Purpose

- [g:r:i] This note records the next adjacent follow-through after the first strengthening slice landed in the planning chain.
- [d:r:i] Its job is to keep the research skill, planner/checker agent contracts, and shared planning-contract references aligned with the new strengthening-route carry rather than leaving the first slice stranded inside discuss/context/plan alone.

## What Landed

- [e:r:i] `gsd-rigorous-research` now names strengthening opportunities as explicit research carry rather than leaving them to ambient prose or generic future work.
- [e:r:i] The rigorous-research method now defines a `Strengthening Opportunity Carry` shape with:
  - current strength
  - bounded intensification move
  - optionality effect
  - carry route
- [e:r:i] The rigorous-research output template now includes a `Strengthening Opportunities` section plus a planning handoff field for current-phase intensification vs seeded later resurfacing.
- [e:r:i] The rigorous-research skill and method now use stronger non-threshold end-state language for research carry, replacing older closure-shaped framing where this surface did not need it.
- [e:r:i] `gsd-planner.toml` now carries `future_preservation.strengthening_routes` in the frontmatter contract and field description.
- [e:r:i] `gsd-plan-checker.toml` now checks that `Strengthening Opportunities` entries become concrete `future_preservation.strengthening_routes` rather than ambient future-awareness residue.
- [e:r:i] `agent-contracts.md` now describes `future_preservation` as carrying strengthening routes alongside preserved seams, explicit non-decisions, and posture assumptions.

## Runtime And Overlay Carry

- [e:r:i] These changes landed in both the live `.codex` runtime and the tracked overlay.
- [e:r:i] That keeps the strengthening family aligned across:
  - planning workflows and templates
  - planner/checker agent prompts
  - rigorous-research skill guidance
  - shared agent-contract reference prose
- [e:r:i] The planner/checker live-vs-overlay differences after re-materialization are understood runtime differences, not semantic drift: the tracked overlay keeps `__PROJECT_ROOT__` placeholders while the live generated `.toml` files resolve those placeholders to concrete repo paths.

## Verification

- [e:r:i] `scan_threshold_language.py` reported only the expected warning-layer hits in planner/checker anti-threshold instructions; the newly added research/planner carry surfaces themselves scanned clean.
- [e:r:i] `git diff --check` passed for the tracked batch before checkpointing.
- [e:r:i] `audit_refmap verify` on the active audit root still reports `0` missing local links after this follow-through note and spine update.
- [e:r:i] `./scripts/setup-portable-gsd.sh` completed successfully after the overlay updates, re-materializing the live runtime from the tracked overlay and leaving the planner/checker path differences in their expected placeholder-vs-resolved form.

## Why This Follow-Through Matters

- [d:r:i] The first strengthening slice now has an upstream research producer as well as a downstream planning consumer.
- [d:r:i] The planner/checker surfaces and shared contract surface now agree on what strengthening carry looks like instead of describing the older narrower `future_preservation` shape.
- [d:r:i] This turns the family from a local planning tweak into a wider planning-plus-research contract without widening yet into milestone, transition, or verification families.

## What This Still Holds

- [d:r:i] The standalone reference-surface object remains a later adjacent slice.
- [d:r:i] Wider lifecycle follow-through remains with the longer-horizon family rather than being absorbed here.
- [d:r:i] The next meaningful proof point should come from real research and planning artifacts using this stronger carry, not from another abstract proposal loop.

## Current Consequence

- [d:r:i] The strengthening family now has:
  - planning-chain insertion
  - research-skill carry
  - planner/checker contract carry
  - shared contract-reference carry
- [d:r:i] The next adjacent object is a later standalone reference-surface or benchmark-packet shape built from real strengthening entries rather than theory alone.
