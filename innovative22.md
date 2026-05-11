# Stabilize-Diagnose-Correct Triad

## Core idea
Merge fail-fast judgment with minimal repair: stop harm, classify with the smallest experiment, patch the smallest surface that restores consistency, then verify where consumers actually read state.

## Practice
Pair every corrective write with a read or probe at the true sink (API response, on-disk file, channel history as applicable).

Encode recurring success paths as short playbooks; avoid storing sensitive details in learning notes.

## Anti-patterns
Large speculative patches before classification; verification only in the agent transcript instead of at the user-visible or system-visible sink.
