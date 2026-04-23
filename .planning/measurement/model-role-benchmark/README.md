# Model Role Benchmark

## Purpose

This packet defines an auditable experiment lane for deciding which Codex model and reasoning settings should be used for different agent roles in `gsd-modifier`.

It does not change production GSD defaults. It defines predictions, research dispatch, a task corpus, scoring rubrics, and a later runner design so model-profile changes can be justified by evidence rather than launch hype or isolated anecdotes.

## Extraction Tooling

Opinion mining uses repo-local extraction scripts instead of treating Codex web browsing as the durable data layer:

- `tooling/codex/model_opinion_mining/fetch_pages.py`
- `tooling/codex/model_opinion_mining/extract_text.py`
- `tooling/codex/model_opinion_mining/build_inventory.py`

Raw HTML and full extracted text stay ignored by default. Checked-in artifacts should be seed files, compact inventories, synthesis, and methodology notes.

## Packet Files

| File | Role |
| --- | --- |
| `PREDICTIONS.md` | Pre-registered expectations to test |
| `TASK-CORPUS.md` | Role-specific benchmark tasks and prompt variants |
| `RUBRIC.md` | Scoring dimensions, metric definitions, and review process |
| `RESEARCH-DISPATCH.md` | Read-only research-agent assignments and hygiene rules |
| `OPINION-MINING-PLAN.md` | Token-efficient anecdote and opinion mining protocol |
| `RUNNER-DESIGN.md` | Later executable harness shape and output contracts |
| `SOURCES.md` | Source taxonomy and current seed sources |

## Current Boundary

This is a design packet plus first-pass extraction tooling. The next step is to seed focused URLs, run the collection-first flow in `OPINION-MINING-PLAN.md`, dispatch the read-only research agents described in `RESEARCH-DISPATCH.md`, synthesize their findings, then decide whether to implement the runner in `tooling/codex/model_benchmark/`.

Production settings that remain unchanged by this packet:

- `.planning/config.json` model overrides
- repo-local GSD agent TOML files
- home-level Codex config
- live executor, planner, reviewer, or researcher defaults
