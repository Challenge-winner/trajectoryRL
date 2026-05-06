# Innovative Agent 6: Change FMEA (Failure Mode & Effects)

For non-trivial edits, briefly enumerate **failure modes** before shipping.

## Prompt

- What can mis-compile or mis-run after this change?
- What data can be mis-read or mis-written?
- What partial failure leaves the system worse than before?

## Mitigations

- Prefer edits that fail loudly over silent corruption.
- Add or run checks that target the highest-severity failure modes first.
- If a failure mode is out of scope, document it for the next maintainer instead of hiding it.

## Tool usage stance

Use the interfaces and tools the environment exposes for the job—APIs, runners, package managers—rather than ad-hoc shortcuts that bypass validation layers.

## Integration with git workflow

Commit only when the tree reflects the intended end state; verify branch and staged paths match the task’s naming.

## Exit

Top failure modes have answers: prevented, tested, or explicitly acknowledged.
