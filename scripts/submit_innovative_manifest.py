#!/usr/bin/env python3
"""Submit SN11 packs from a manifest JSON (raw GitHub URLs + pack hashes).

Run after pushing pack JSON to GitHub so raw.githubusercontent.com returns 200:

    cd _publish/Bennett-Dan-4-push && git push origin main

Then (example: New1–New22 packs, 10-minute spacing):

    cd /root/Sn11
    NETUID=11 NETWORK=finney python3 scripts/submit_innovative_manifest.py \\
        --manifest _publish/new22_manifest.json --interval-seconds 600

Uses coldkey / hotkey from each manifest row (TrajectoryMiner).
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
import time
import urllib.request
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


def _verify_pack_url(pack_hash: str, pack_url: str) -> tuple[bool, str]:
    """Fetch pack JSON and confirm SHA256 matches (same as miner CLI submit)."""
    from trajectoryrl.base.miner import TrajectoryMiner

    try:
        req = urllib.request.Request(pack_url, headers={"User-Agent": "TrajectoryRL-submit-script/1"})
        with urllib.request.urlopen(req, timeout=45) as resp:
            raw = resp.read().decode("utf-8")
        pack = json.loads(raw)
    except Exception as e:
        return False, f"fetch/parse failed: {e}"
    issues = TrajectoryMiner.validate_s1(pack)
    if issues:
        return False, "validation: " + "; ".join(issues)
    got = TrajectoryMiner.compute_pack_hash(pack)
    if got != pack_hash:
        return False, f"hash mismatch (chain expects {pack_hash[:12]}…, got {got[:12]}…)"
    return True, ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Submit packs from manifest JSON.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=_ROOT / "_publish" / "innovative_manifest.json",
        help="Path to innovative_manifest.json",
    )
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    parser.add_argument(
        "--skip-fetch-check",
        action="store_true",
        help="Submit without verifying the pack URL is reachable (not recommended).",
    )
    parser.add_argument(
        "--interval-seconds",
        type=float,
        default=0.0,
        metavar="N",
        help="Wait N seconds after each submission before starting the next (e.g. 600 for 10 minutes).",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s | %(levelname)-8s | %(message)s",
    )

    try:
        from dotenv import load_dotenv

        load_dotenv(_ROOT / ".env.miner")
    except ImportError:
        pass

    from trajectoryrl.base.miner import TrajectoryMiner

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    failed = 0
    for idx, row in enumerate(manifest):
        coldkey = row["coldkey"]
        hotkey = row["hotkey"]
        pack_hash = row["pack_hash"]
        pack_url = row["pack_url"]
        miner = TrajectoryMiner(wallet_name=coldkey, wallet_hotkey=hotkey)
        try:
            logging.info("Submitting %s/%s -> %s", coldkey, hotkey, pack_url)
            do_submit = True
            if not args.skip_fetch_check:
                good, err = _verify_pack_url(pack_hash, pack_url)
                if not good:
                    logging.error("Pack URL check failed (%s/%s): %s", coldkey, hotkey, err)
                    failed += 1
                    do_submit = False
            if do_submit:
                ok = miner.submit_commitment(pack_hash, pack_url)
                if not ok:
                    logging.error("FAILED %s/%s", coldkey, hotkey)
                    failed += 1
                else:
                    logging.info("OK %s/%s", coldkey, hotkey)
        finally:
            miner.close()

        if args.interval_seconds > 0 and idx + 1 < len(manifest):
            logging.info("Waiting %.1fs before next submission…", args.interval_seconds)
            time.sleep(args.interval_seconds)

    if failed:
        logging.error("%d submission(s) failed", failed)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
