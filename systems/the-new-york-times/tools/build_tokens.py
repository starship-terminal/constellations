#!/usr/bin/env python3
"""Check that tokens.json still matches the captured readings.

The New York Times package writes tokens.json by hand from
raw/computed.json and raw/tokens-resolved.json. This script does not
rebuild those files. It fails when a painted value drifts.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    tokens = json.loads((ROOT / "tokens.json").read_text())
    computed = json.loads((ROOT / "raw" / "computed.json").read_text())
    checks = {
        "core.color.ink": (tokens["core"]["color"]["ink"]["$value"], "#121212"),
        "core.color.masthead": (tokens["core"]["color"]["masthead"]["$value"], "#567b95"),
        "core.color.accent": (tokens["core"]["color"]["accent"]["$value"], "#346eb7"),
        "subscribe bg": (computed["home"]["subscribe"]["backgroundColor"], "rgb(86, 123, 149)"),
        "login continue": (computed["login"]["continue"]["backgroundColor"], "rgb(18, 18, 18)"),
        "login radius": (computed["login"]["continue"]["borderRadius"], "3px"),
    }
    bad = [name for name, (got, want) in checks.items() if got != want]
    if bad:
        print("drift: " + ", ".join(bad), file=sys.stderr)
        return 1
    print("tokens match the captured readings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
