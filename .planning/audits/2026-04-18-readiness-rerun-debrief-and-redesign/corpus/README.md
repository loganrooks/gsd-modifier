# Commentary Corpus

Status: active inquiry corpus topology  
Date: 2026-04-19

## Purpose

- This subtree isolates the `Contestation And Claim Ontology` inquiry corpus from the governing audit spine and lane outputs.
- It keeps the commentary family navigable without asking the flat audit root to carry every chunk, prompt, whole-note pass, and derivative translation directly.

## Layout

- `COMMENTARY-CORPUS-READSET.md`
  - active inheritable chunk manifest
- `source/`
  - source note and adjacent source-facing material
- `prompts/`
  - commentary-generation prompts used to build the corpus
- `whole-note/`
  - earlier whole-note and pre-chunk commentary passes
- `translation/`
  - derivative translation artifacts
- `chunks/`
  - chunk-by-chunk commentary passes

## Rule

- [g:r:i] Treat this subtree as exploratory / inquiry corpus, not governing audit doctrine.
- [g:r:i] When a workspace doc needs the active chunk corpus, prefer `COMMENTARY-CORPUS-READSET.md` over scanning `chunks/` by filename.
- [g:r:i] If later reorganization is needed, do it by bounded subtree move with scripted reference rewriting, not by silent ad hoc renames.
