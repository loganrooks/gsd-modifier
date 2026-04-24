Read the following files in order:

1. `/home/rookslog/workspace/projects/prix-guesser/AGENTS.md`
2. `/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md`
3. `/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-executed-patch-bundle-review-spec.md`

Then execute the review spec exactly as written.

Important:

- Treat this as a fresh checkpoint review of the executed `R5.18` patch bundle, not a reread of earlier pre-execution Checkpoint 5 reviews.
- Use `/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18d-integration-and-review-prep-launch-internal-r1.md` as the integration entry artifact, but do not trust it without directly spot-checking the executed file surfaces required by the spec.
- Do not soften findings because parts of the runtime surface are repo-ignored or untracked. Evaluate whether that creates closure risk instead of treating it as invisible.
- Write the completed review to:
  `/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-executed-patch-bundle-review-cross-vendor-opus-1m-r2.md`

Do not write to any other target artifact path.
