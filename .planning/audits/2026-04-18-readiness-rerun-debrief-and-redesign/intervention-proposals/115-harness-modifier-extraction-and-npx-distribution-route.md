Date: 2026-04-22
Status: active bounded future route

# Harness Modifier Extraction And NPX Distribution Route

## Purpose

- [g:r:i] Keep the possible cross-repo extraction of this harness-modifier layer explicit instead of leaving it as ambient future pressure.
- [g:r:i] The question is not whether extraction feels attractive in the abstract.
- [g:r:i] The question is how a later extraction could preserve propagation discipline, compatibility truth, and repo-local override control without freezing moving contracts too early.

## Why This Route Opens

- [e:c+i] The repo-local harness-modifier layer is now materially larger than one-off repo glue. It already includes repo-local workflows, skills, helper tooling, propagation registry work, uplift machinery, and governing doctrine surfaces. Sources:
  - [101-repo-local-workflow-additions-and-propagation-map-orientation.md](101-repo-local-workflow-additions-and-propagation-map-orientation.md)
  - [37-entry-surface-and-project-uplift-map.md](37-entry-surface-and-project-uplift-map.md)
  - [95-upstream-pristine-propagation-baseline-first-slice.md](95-upstream-pristine-propagation-baseline-first-slice.md)
  - [96-repo-local-propagation-delta-first-slice.md](96-repo-local-propagation-delta-first-slice.md)
- [d:r:i] That makes later extraction thinkable.
- [d:r:i] Co-location with host-project planning doctrine now also creates a real scope-leak risk during horizon mapping and audit inheritance, which makes extraction pressure more concrete than abstract packaging appetite alone.
- [d:r:i] It does not yet make immediate extraction the better move, because the uplift and cross-runtime families are still actively sharpening their contracts.

## Plausible Later Shape

- [d:r:i] One later route is a separate repo that owns the harness-modifier layer itself:
  - tracked overlay deltas
  - helper/tooling package
  - installer/update bridge
  - compatibility policy
  - propagation and governance reference surfaces
  - harness-specific horizon and doctrine surfaces separated from any one host project's product-planning docs
- [d:r:i] One plausible distribution channel is an npm package with a narrow installer entry such as `npx ...`, where the installer:
  - detects whether supported GSD runtime carriers are present
  - checks the observed runtime version and related manifest truth
  - refuses, warns, or shifts mode when the local GSD basis is outside the declared compatible range
  - installs only the modifier layer rather than pretending to own the full upstream GSD runtime

## Why Not Extract Immediately

- [d:r:i] The cross-runtime compatibility-family widening route is still active in `114`, and its implementation boundary has not landed yet.
- [d:r:i] The broader project-uplift and propagation families are still disclosing which carriers are stable generic modifier surfaces versus which remain repo-specific or audit-specific.
- [d:r:i] Extracting now would increase coordination load across:
  - overlay ownership
  - setup/install/update materialization
  - compatibility policy
  - propagation registry refresh
  - project-specific governing doctrine
- [d:r:i] That means extraction now would likely widen propagation pressure before the current contracts have finished sharpening.

## What A Later Extraction Route Should Settle First

- [d:r:i] Compatibility policy shape:
  - what exact GSD runtime/version carriers govern support
  - where supported-version truth lives
  - how warning versus refusal versus degraded mode is expressed
- [d:r:i] Boundary split:
  - what remains project-specific in this repo
  - what becomes generic harness-modifier carry
- [d:r:i] Installer/update contract:
  - what the separate package installs
  - what upstream GSD still owns
  - how reinstall/update materialization keeps the modifier layer in tune
- [d:r:i] Propagation ownership:
  - how cross-repo propagation maps, compatibility anchors, and governed docs stay current when the modifier layer changes
- [d:r:i] Distribution ergonomics:
  - whether npm/`npx` is the right operator entry
  - whether a local wrapper or script-first route remains cleaner

## Current Recommendation

- [d:r:i] Treat extraction as a real future route, not as immediate execution.
- [d:r:i] Keep the current modifier layer bundled here while the uplift/cross-runtime compatibility and propagation contracts continue sharpening.
- [d:r:i] Reopen extraction after the present compatibility-family route and adjacent uplift propagation surfaces have traveled farther, so the extracted boundary reflects clearer contracts rather than moving seams.

## What This Route Does Not Authorize

- [d:r:i] No repo split now.
- [d:r:i] No npm package now.
- [d:r:i] No installer implementation now.
- [d:r:i] No support-window claim now.

## Next Bounded Move

- [d:r:i] After the current compatibility-family route and its neighboring propagation/governance updates settle further, open one dedicated extraction-field map:
  - generic modifier carriers
  - repo-specific carriers
  - installer/update boundaries
  - compatibility declaration shapes
  - propagation and governance follow-through obligations
