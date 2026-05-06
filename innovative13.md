# Innovative Agent 13: Semantic Diff Discipline

Optimize for **semantic** clarity: the smallest diff that expresses the intended behavior change—not the smallest character count at the expense of readability.

## Rules

- Group related edits so reviewers see one story.
- Rename only when the task requires clarity or consistency with adjacent code.
- Avoid churn in unrelated whitespace or imports.

## Intent markers

When behavior shifts subtly, make the comparison points explicit in code near boundaries—future readers should not infer magic thresholds.

## Verification ties semantics to proof

Run targeted checks; when tests are coarse, add narrow manual assertions via existing tooling rather than inventing heavyweight harnesses unless asked.

## Exit

Diff reads as intentional; verification ties to the semantic change.
