Date: 2026-04-22
Status: accepted first-slice proposal

# Codex Claude Parity Classification Carrier Proposal

## Why This Slice Exists

- [d:r:i] Lane `19` exposed a narrower stronger route than parity-install widening:
  - the repo does not currently carry active-pointer defects in `.codex`
  - the current `.claude` hits are contextual
  - the missing object is a durable classifier inside the repo-local materialization contract, not a bigger installer branch

## First Slice

- [d:r:i] Extend `tooling/codex/portable_gsd_contract.py verify-materialized` so it also emits a typed runtime-specific reference report for live `.codex/` materialization.
- [d:r:i] Keep that report narrow:
  - preserve the current known three-hit baseline with explicit classifications
  - mark any non-baseline hit as `needs contextual reread`
  - do not convert the helper into a silent wording police or a fake active-pointer oracle

## Carriers

- [d:r:i] Primary carrier:
  - [tooling/codex/portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py)
- [d:r:i] Focused contract coverage:
  - [tooling/codex/tests/test_portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_portable_gsd_contract.py)
- [d:r:i] Operator-facing note:
  - [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md)
- [d:r:i] Propagation memory:
  - [../propagation-audit/50-codex-claude-parity-classification-carrier-change-triggered-refresh.md](../propagation-audit/50-codex-claude-parity-classification-carrier-change-triggered-refresh.md)

## First-Slice Boundaries

- [d:r:i] Do not widen into `.claude` materialization.
- [d:r:i] Do not rewrite comment examples just to quiet warnings.
- [d:r:i] Do not make unreviewed hits fail the install automatically.
- [d:r:i] Do not try to prove active-pointer absence for all future hits with heuristics alone.

## Verification

- [d:r:i] The slice should prove:
  - current baseline hits classify the same way every run
  - unreviewed hits surface distinctly for contextual reread
  - existing strict materialization verification still passes on the current repo

## Later Pressure

- [d:r:i] After the classified carrier is exercised on more real materialization boundaries, later parity work can reopen:
  - installer disclosure at the single-runtime boundary
  - `.claude` freshness / maintained-carrier questions
  - larger runtime-specific install branching only if the repo actually earns it
