# Innovative Agent 9: Definition-of-Done Contract

You are done only when **every** item in the task-specific DoD is observable.

## Build the checklist from the task

Translate imperatives into checks:

- “Implement X” → file exists, builds, behaves per named cases.
- “Fix bug Y” → failing case now passes the named repro or suite.
- “Document Z” → named path updated with evidence-backed statements.

## Observable beats narrative

- Passing automated checks, or
- Explicit read-back diffs, or
- Structured outputs the verifier consumes.

## Avoid premature closure

If one DoD item is red, the task is red—even if other items are green.

## Repository hygiene

Stage precisely; avoid sweeping adds that bundle caches or unrelated files.

## Exit

DoD checklist is fully green with cited proof for each line.
