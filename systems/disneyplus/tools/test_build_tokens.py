#!/usr/bin/env python3
"""Fail if a Disney+ token is missing its measured source."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    script = Path(__file__).with_name("build_tokens.py")
    result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(result.stderr or result.stdout)
    tokens = json.loads((ROOT / "tokens.json").read_text())
    if tokens["light"]["color"]["accent"]["$value"] != "#33ddff":
        raise SystemExit("accent drifted from the measured annual fill")
    print("test ok")


if __name__ == "__main__":
    main()
