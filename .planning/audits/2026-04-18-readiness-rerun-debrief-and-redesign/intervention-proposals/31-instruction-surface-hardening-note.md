Date: 2026-04-21
Status: landed instruction hardening

# Instruction-Surface Hardening Note

## Purpose

- [g:r:i] This note records a bounded hardening pass on root/planning instruction surfaces after the same recurring failures kept reappearing in audit and proposal work.

## What This Hardening Targets

- [d:r:i] Binary inheritance when a family is sound but the first slice is weakly packaged.
- [d:r:i] Risk used as a veto even when the risk can be reduced through sequencing, tooling, checkpointing, or verification.
- [d:r:i] Premature narrowing to the top few options when the stronger first move is to map the full field.
- [d:r:i] Treating extra work by itself as a blocker after the user has already made clear that the stronger move is worth the work.

## Landed Instruction Changes

- [d:r:i] Root and planning `AGENTS.md` now explicitly tell agents to prefer narrowing, splitting, or staged carry over binary accept/reject when a proposal direction is strong but its packaging is weak.
- [d:r:i] Root and planning `AGENTS.md` now explicitly tell agents to turn manageable risk into a mitigation plan with quality gates rather than using risk as a flat refusal.
- [d:r:i] Root and planning `AGENTS.md` now explicitly tell agents to decide whether a task calls for full-field mapping before ranking or narrowing.
- [d:r:i] Root and planning `AGENTS.md` now explicitly tell agents not to use work volume alone as a blocker once a stronger change has been explicitly prioritized.
- [d:r:i] Root and planning `CLAUDE.md` wrappers now carry the same bounded translation so cross-vendor lanes inherit the same corrections.

## Why This Matters

- [d:r:i] These are not style-only adjustments.
- [d:r:i] They change how the instruction layer handles proposal inheritance, cleanup pressure, and planning/research sequencing.
- [d:r:i] They also reduce the chance that the same failure patterns keep re-entering through wrappers after being corrected locally in the audit workspace.

## Scanner Interpretation

- [d:r:i] `scan_threshold_language.py` still flags the instruction files after this pass.
- [d:r:i] In this case the hits are expected warning-layer mentions inside anti-threshold doctrine itself, not live contamination in the revised proposal or updated audit spine.
- [d:r:i] That means the scanner remains useful here as a first-pass detector, but the instruction files still need human interpretation because they deliberately name the phrasing they are forbidding.

## Current Consequence

- [d:r:i] Future planning, audit, and intervention work should now be more likely to:
  - preserve a strong family while narrowing the first slice
  - respond to manageable risk with boundary and verification design
  - map the full field when that is the stronger first move
  - respect explicit user insistence on stronger cleanup or organization work instead of treating effort by itself as a blocker
