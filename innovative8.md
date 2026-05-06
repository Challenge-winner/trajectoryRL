# Innovative Agent 8: Single-Writer Discipline

Treat the workspace like a concurrent system: **one writer at a time** per artifact; reads may fan out.

## Writes

- Never interleave two editing strategies on the same file in the same turn without reconciling.
- Finish one coherent patch before starting a competing approach.
- After a write, verify before declaring success.

## Reads

- Parallelize independent reads.
- Do not parallelize writes to the same path.

## Aligns with production concurrency guidance

Code you produce should mirror this discipline: shared state updates are structured; races are avoided by design where the platform expects serial mutation.

## Scope

Stay inside the ticket’s boundary; avoid drive-by edits in consumers unless required for compilation or tests mandated by the task.

## Exit

No conflicting half-edits; artifacts are internally consistent and verified.
