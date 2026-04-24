Date: 2026-04-22
Status: completed local inheritance

# Harness Modifier Project Uplift Neutralization Proposal Reread Inheritance

## Local Disposition

- [d:r:i] `accept with typed-carrier split`
- [d:r:i] Keep the three neutralization targets separate:
  - runtime discovery posture
  - uplift output/path posture
  - compatibility-routing posture
- [d:r:i] Do not collapse the return into “externalize constants” or “add one config file.”

## Carry Forward

- [d:r:i] The next implementation slice should treat runtime discovery as an observation surface, not as helper-local ambient provider policy.
- [d:r:i] The next implementation slice should split uplift output/path policy from seed-contract shape policy instead of flattening them into one config bucket.
- [d:r:i] The next implementation slice should thin `project_uplift.py` as a compatibility-declaration consumer rather than letting it re-export declaration semantics through module-level globals.
- [d:r:i] Keep `.codex` as observed basis and `.claude` as held annotation.

## Land Next

- [d:r:i] Land one bounded neutralization implementation slice with:
  - typed observation carrier
  - typed uplift output-policy carrier
  - typed seed-contract-shape carrier
  - thinner declaration consumption inside `project_uplift.py`
  - downstream seed-shape carrier adoption in `seed_migration_inventory.py`
  - focused parity-preservation tests

## Keep Explicitly Later

- [d:r:i] `project_uplift.py` relocation.
- [d:r:i] `seed_migration_inventory.py` relocation.
- [d:r:i] `audit_refmap.py` movement.
- [d:r:i] second overlay tranche.
- [d:r:i] overwrite-family source split.
- [d:r:i] standalone repo boundary.
- [d:r:i] npm/`npx` packaging.
- [d:r:i] second-host exercise.
- [d:r:i] broader carrier typing of `STATIC_FILE_CARRIERS` / `MARKER_CARRIERS`.
- [d:r:i] speculative-runtime pruning or provider-widening judgment beyond the current `.codex` observed basis plus `.claude` held annotation split.

## Exact Next Move

1. [d:r:i] Implement the bounded neutralization slice the lane named.
2. [d:r:i] Refresh helper authority, roster, register, and extraction-governance surfaces around that landed slice.
3. [d:r:i] Only after that implementation lands, re-evaluate whether later `project_uplift.py` relocation is still the sharper extraction move.
