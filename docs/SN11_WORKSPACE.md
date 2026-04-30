# SN11 repository workspace (local fork layout)

This note describes how this checkout relates to **TrajectoryRL mining** and a
practical **Git branch naming** convention. For the canonical miner CLI, see
[MINER_OPERATIONS.md](MINER_OPERATIONS.md).

## What this project is

- **Python package**: `trajectoryrl` + `neurons/` — validators and the miner
  CLI (`trajectoryrl-miner`: build / validate / upload / submit / status).
- **Competition**: Miners publish a **SKILL.md** (agent instructions), baked into
  **pack.json**, hosted at a **public HTTPS URL**, then referenced in an
  **on-chain commitment** (`pack_hash|pack_url`). Validators fetch by URL and
  verify the hash.
- **GitHub**: Pushing branches to a fork or upstream is **optional** for mining;
  it does not replace upload + `submit`. You need **write access** (or a fork +
  PR) to push to someone else’s repo.

## Files in this workspace

| Path | Role |
|------|------|
| `SKILL.md` | **Active** Season 1 skill text used with `trajectoryrl-miner build SKILL.md`. Keep this non-empty and under the pack size limit. |
| `1.md` … `12.md` | Local **drafts** / alternates; pick one and copy into `SKILL.md`, or build directly: `trajectoryrl-miner build ./8.md -o pack.json`. |
| `eval_output/`, `*.sqlite3` | Local eval artifacts — do not commit unless you intend to share them. |

## Git branch naming (coldkey + date + time)

When you use Git to track or open a PR for a submission iteration, a readable
pattern is:

```text
{coldkey_name}-{YYYYMMDD}-{HHMM}
```

Example: `test51-20260430-2033` means coldkey wallet name `test51`, local date
30 Apr 2026, time 20:33.

Use **UTC** or a fixed timezone consistently if collaborators are in multiple
regions. SS58 addresses and hotkey names belong in **local** notes or your
password manager, not necessarily in public skill text.

## End-to-end miner reminder

```bash
trajectoryrl-miner build ./SKILL.md -o pack.json
trajectoryrl-miner validate pack.json
trajectoryrl-miner upload pack.json    # needs S3-compatible env (see .env.miner.example)
trajectoryrl-miner submit <public_pack_url>
```

## Why a GitHub push might fail with 403

If `git push` reports **Permission denied** for user `X`, Git authenticated as `X`
but `X` **cannot write** to that repository. Fix: use a token/account with
access, push to **your fork** and open a PR, or ask the org for collaborator
access.
