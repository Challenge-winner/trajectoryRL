# Innovative Agent 14: Environment Parity Brief

Start sessions by grounding **where** commands execute and **which** toolchain applies.

## Brief checklist

- Interpreter or compiler version relevant to the task.
- Package manager or runner invoked by the repo’s canonical commands.
- Required env vars or config files the task names.

## Avoid phantom execution

Commands that succeed locally but target the wrong filesystem path produce false confidence—confirm cwd and host assumptions when the task implies multiple environments.

## Reproducibility

Prefer commands from project docs or scripts over ad-hoc sequences that the next run cannot repeat.

## Exit

Stated environment facts match observed outputs for the checks you ran.
