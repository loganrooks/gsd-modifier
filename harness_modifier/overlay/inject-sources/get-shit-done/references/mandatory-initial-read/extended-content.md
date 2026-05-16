**Reading packet tiers**

- `<required_reading>`
  - load all listed files before doing anything else
  - this block carries the minimum context the task cannot proceed without
- `<supporting_reading>`
  - load only after the required block
  - use it when the active route, anomaly, or user request points at one of those files
  - do not widen into the whole supporting list by reflex
- `<deeper_reading>`
  - load only when the task is blocked, the current route explicitly depends on it, or you are intentionally widening the read set for a bounded reason
  - do not treat deeper reading as default startup context

**Contextual reread rules**

- The blocks widen attention; they do not replace judgment about what the current task actually needs next.
- When a workflow or prompt provides structured helpers, summaries, manifests, or snapshots, prefer those as the first route into the task before widening into broader prose files.
- If a later route points into one specific family, reread that family deliberately rather than flattening the whole workspace into startup context.
- If a prompt or workflow explicitly says a quoted anti-pattern, prohibition, or historical example must stay visible, do not rewrite or omit it merely to keep the packet narrow.
