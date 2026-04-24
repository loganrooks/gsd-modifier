Date: 2026-04-21
Status: landed

# Overlay Add-Vs-Overwrite Contract And Post-Materialization Gate

## What Landed

- [d:r:i] Route `C` is now explicit rather than ambient.
- [d:r:i] Route `G` is now explicit rather than ambient.
- [e:c+i] The tracked overlay now has a machine-readable ownership split at [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json). Source: [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json:1).
- [e:c+i] The installer/materialization contract is now centralized in [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py) rather than split across shell inline snippets and downstream parser guesses. Sources: [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:1), [setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:1).
- [e:c+i] `setup-portable-gsd.sh` now validates the overlay contract before copy and verifies post-materialization coherence after copy plus reasoning-default application. Source: [setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:19).
- [e:c+i] `runtime_visibility.py` now inherits install-mutation and template-materialization truth from the shared helper instead of scraping that logic back out of the shell script. Source: [runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py:11).

## Why This Matters

- [d:r:i] Before this batch, overwrite-carried and additive overlay-owned files were both just `files under overlay/`.
- [d:r:i] That meant the install path could still work while the ownership model drifted.
- [d:r:i] The new contract makes two different obligations explicit:
  - overwrite surfaces must stay aligned with `backup-meta.json`
  - additive surfaces must stay outside `backup-meta.json`

## Live Correction The Gate Surfaced

- [e:c+i] The first live installer run under the new gate surfaced a real drift case: `skills/gsd-resume-work/SKILL.md` had been treated locally as additive, but the live installer now backed it up as an upstream-shipped modified surface. Sources: [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json:1), [.codex/gsd-local-patches/backup-meta.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:1).
- [d:r:i] That drift was corrected by retyping `skills/gsd-resume-work/SKILL.md` from `add` to `overwrite` in the tracked manifest, then rerunning the full installer path.
- [e:c+i] The rerun then cleared both the pre-copy manifest validation gate and the post-materialization coherence gate with zero hard failures. Sources: [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:128), [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:214).

## Current Contract Shape

- [e:c+i] Current tracked overlay split:
  - `33` overwrite entries
  - `19` add entries
  - `52` total tracked overlay entries
  Sources: [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json:1), [backup-meta.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:1).
- [e:c+i] The post-materialization gate currently verifies:
  - every manifest entry exists in live `.codex/`
  - overwrite entries still have backup copies
  - live targets still match the materialized overlay contract after allowed reasoning-default normalization
  Source: [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:214).

## Consequence

- [d:r:i] The propagation family now has a stronger installer/materialization boundary than it had at `06`.
- [d:r:i] The next stronger question is no longer whether overlay/install integrity is still ambient.
- [d:r:i] The next stronger question is how to widen propagation mapping beyond the uplift example without losing this now-explicit contract layer.
