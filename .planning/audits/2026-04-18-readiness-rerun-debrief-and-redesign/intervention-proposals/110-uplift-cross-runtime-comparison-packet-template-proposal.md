Date: 2026-04-22
Status: landed bounded proposal

# Uplift Cross-Runtime Comparison Packet Template Proposal

## Purpose

- [g:r:i] Turn the now-live `cross_runtime_comparison_packet` family into one concrete packet carrier before any first comparison exercise or wider external lane opens.
- [g:r:i] Keep the move narrow:
  - one packet template
  - no runtime mutation
  - no first comparison exercise yet

## Why This Route Now

- [e:c+i] Current uplift memory now keeps ordinary routing explicit again, with no additive carriers and no pending doctrine-sensitive proposals. The remaining live posture still classifies the repo as `cross-runtime uplift` because `.codex` and `.claude` are both present. Sources:
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:5)
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:13)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:5)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:19)
- [e:c+i] The assist-pattern reference already names `cross_runtime_comparison_packet` as one of the four allowed bounded uplift-assist families and already routes its first delegated use toward Opus unless the comparison has been narrowed to one auditable repo-local packet. Source: [103-uplift-agent-assist-patterns.md](103-uplift-agent-assist-patterns.md:75).
- [d:c+i] The family has now earned that narrowing carrier, because the earlier docs-governance family no longer needs first-proof work and additive-install pressure is not currently live. Sources:
  - [109-uplift-docs-governance-runtime-proof-and-refresh.md](109-uplift-docs-governance-runtime-proof-and-refresh.md:18)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:33)

## Proposed Carrier

- [d:r:i] One reusable packet template at:
  - `entry-uplift-audit/packets/11-uplift-cross-runtime-comparison-packet-template.md`
- [d:r:i] Role:
  - define the bounded read set for `.codex` versus `.claude` comparison
  - define the output shape for one first comparison packet
  - keep the packet inside observed-basis discipline rather than accidental cross-runtime theory inflation

## Boundaries

- [d:r:i] No first comparison exercise in this slice.
- [d:r:i] No external Opus lane in this slice.
- [d:r:i] No runtime mutation in this slice.
- [d:r:i] No cross-runtime composition judgment in this slice.
- [d:r:i] No consumer-route widening in this slice.

## Current Consequence

- [d:r:i] The next bounded move is to land the reusable packet carrier, then use that carrier to assemble one first `.codex` versus `.claude` comparison packet before any Opus widening or later composition work.
