Date: 2026-04-21
Status: landed setup/materialization robustness refresh

# Setup Portable GSD Robustness Change-Triggered Refresh

## Purpose

- [g:r:i] This note records the next bounded `change_triggered_slice_refresh` after `19`.
- [g:r:i] The trigger here is a setup/materialization contract move across installer entry, helper, contract, and fresh-install overwrite-baseline carriers.

## Trigger

- [e:c+i] The bounded setup/materialization robustness family is now carried through [55-setup-portable-gsd-robustness-and-reinstall-truth-proposal.md](../intervention-proposals/55-setup-portable-gsd-robustness-and-reinstall-truth-proposal.md) and [56-setup-portable-gsd-robustness-and-reinstall-truth-implementation.md](../intervention-proposals/56-setup-portable-gsd-robustness-and-reinstall-truth-implementation.md).
- [e:r:i] That slice changed the propagation field in four concrete ways:
  - the setup script now treats upstream exit `2` as a recoverable repo-local verification boundary rather than an immediate stop
  - a new helper now owns bounded `gsd-sdk` runtime verification and executable-bit repair
  - the shared portable contract now captures fresh-install pristine overwrite copies before overlay application
  - the strict overwrite/materialization contract now survives fresh installs that no longer ship `backup-meta.json`

## Refresh Result

- [d:r:i] The typed `v2` semantic layer should now keep the setup-script bridge, the `gsd-sdk` runtime helper, and the synthetic pristine-capture stage distinct instead of compressing them into one generic materialization row.
- [d:r:i] The declared-contract layer should now make the fresh-install pristine-capture stage explicit inside the portable contract family.
- [d:r:i] The evidence layer should now carry the landed `56` implementation note as the current anchor for this slice.

## Current Consequence

- [d:r:i] The typed `v2` registry now survives another real change-triggered refresh that is neither uplift-only nor lifecycle-only.
- [d:r:i] The propagation family now carries a clearer example of setup-entry, helper, contract, and fresh-install baseline movement that later reinstall/compatibility work can inherit from.
- [d:r:i] Later refreshes should keep following actual setup/materialization contract movement instead of reopening the whole propagation field whenever the wrapper changes.
