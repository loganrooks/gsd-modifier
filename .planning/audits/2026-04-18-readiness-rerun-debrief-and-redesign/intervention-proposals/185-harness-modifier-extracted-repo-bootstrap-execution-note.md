# 185 Harness Modifier Extracted Repo Bootstrap Execution Note

- [g:r:i] This note records that the filtered-history bootstrap route was executed, not only planned.

## Execution Result

- [d:r:i] The standalone extracted repo now exists at `/home/rookslog/workspace/projects/gsd-modifier`.
- [d:r:i] The extracted repo carries filtered history for the locked migration set:
  - `harness_modifier/`
  - `tooling/codex/`
  - `tooling/portable-gsd/overlay/`
  - `scripts/setup-portable-gsd.sh`
- [d:r:i] The extracted repo now also carries fresh bootstrap/governance surfaces on top of that filtered history:
  - `README.md`
  - `AGENTS.md`
  - `WORKFLOW.md`
  - `.planning/config.json`
  - onboarding docs for Codex and Claude
  - migration provenance docs
  - a carried historical audit archive

## Extracted Repo Checkpoint

- [d:r:i] The extracted repo bootstrap checkpoint is `86e9f1c` on branch `main`.
- [d:r:i] That checkpoint makes the extracted repo self-hosting and auditable rather than leaving it as a filtered clone with origin-specific bootstrap gaps.

## Verification

- [e:r:i] The extracted repo verification stack completed cleanly on the settled bootstrap state:
  - `./scripts/setup-portable-gsd.sh`
  - `python3 -m py_compile $(find harness_modifier tooling/codex -name '*.py' -type f | tr '\n' ' ')`
  - `python3 -m unittest discover -s tooling/codex/tests`
  - `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --strict`
  - `python3 tooling/codex/audit_refmap.py verify .`
  - `git diff --check`
- [e:r:i] The settled unit suite count in the extracted repo was `147` tests passing.
- [d:r:i] The carried historical audit is now explicit inside the extracted repo as `docs/origin-audit/archive/2026-04-18-readiness-rerun-debrief-and-redesign.tar.gz` plus `SHA256SUMS`, so the migration now includes the development audit trail without replaying that archive as the extracted repo's live planning engine.

## Consequence

- [d:r:i] The migration question is no longer only hypothetical in this origin audit family.
- [d:r:i] The next work for release-readiness, install profiles, CI sequencing, and later closure should now happen against the extracted repo as the active modifier project rather than continuing to treat `prix-guesser` as the main execution home for those steps.
