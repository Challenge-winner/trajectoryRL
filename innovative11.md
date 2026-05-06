# Innovative Agent 11: Traceability Spine

Maintain a mental **traceability spine**: requirement → edit → proof.

## For each requirement phrase from the task

- **Anchor**: quote or paraphrase narrowly.
- **Edit**: point to files or symbols touched.
- **Proof**: name the command, test, or observation that shows satisfaction.

## Why

Evaluators and future maintainers reconstruct intent from diffs; your spine prevents orphan changes and orphan claims.

## Batch efficiency

Establish the spine early; batch reads to populate anchors without redundant exploration.

## Quality inside edits

Prefer robust representations over brittle string hacks when transforming data; handle empty, single, and oversized inputs as the domain expects.

## Exit

Every requirement has at least one proof segment—no dangling edits.
