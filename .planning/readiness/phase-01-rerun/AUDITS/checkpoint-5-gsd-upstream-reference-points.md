# Checkpoint 5 GSD Upstream Reference Points

## Purpose

Record the concrete upstream comparison surfaces that later hybrid mapping lanes must use.

This artifact exists so later agents do not silently mix:

- live repo-local runtime
- version-matched clean upstream baseline
- later upstream trajectory

## Source Of Truth

- npm package source: `https://github.com/gsd-build/get-shit-done.git`
- installed repo-local runtime version: `1.36.0`
  - source: [`.codex/get-shit-done/VERSION`](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/VERSION)
- npm latest observed during setup verification: `1.36.0`

## Comparison Surfaces

### 1. Repo-Local Runtime Reality

- path: [`.codex/get-shit-done`](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done)
- role: currently materialized runtime actually used inside this repo
- caveat: may already incorporate repo-local overlays, local modifications, and readiness-adjacent drift

### 2. Clean Upstream Baseline For Exact Version Comparison

- path: [`get-shit-done-upstream-v1.36.0`](/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0)
- git ref: `v1.36.0`
- commit: `201b8f1a056323c0b88f0f6d9a8aa7c82efaffb8`
- role: clean upstream baseline for exact parity comparison against the installed local `1.36.0` runtime

### 3. Later Upstream Trajectory Surface

- path: [`get-shit-done-upstream`](/home/rookslog/workspace/projects/get-shit-done-upstream)
- branch: `main`
- commit at clone time: `c35997fb0b237bd3feb1317bc6894e1871b37b17`
- describe at clone time: `v1.36.0-38-gc35997f`
- role: future-facing upstream trajectory surface for “where GSD is going” questions

## Usage Rules

- use the repo-local runtime when mapping what currently exists here
- use the pinned `v1.36.0` tree when deciding whether something is a repo-local intervention versus clean upstream truth
- use `main` only when the question is about likely future direction, newly added surfaces, or anticipated carry-forward pressure
- do not collapse the pinned tree and `main` into one generic “upstream” category

## Consequence For Mapping Program

- `a1..a4` outputs are a repo-local inventory pass, not sovereign upstream truth
- any later synthesis that wants to sound like full high-level system truth must consume a hybrid reconciliation pass first
- future-looking claims should cite the moving upstream clone or changelog directly rather than piggybacking on the version-matched baseline
