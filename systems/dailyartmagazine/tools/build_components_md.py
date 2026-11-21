#!/usr/bin/env python3
"""components.md is written for this public magazine capture.

The kit's public builder expects Gauth's measurement JSON. This package's
inventory is components.md, maintained next to the readings. This script
checks that the file exists and that tokens.json still builds.
"""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
md = HERE.parent / "components.md"
if not md.exists():
    sys.exit("components.md missing")
subprocess.check_call([sys.executable, str(HERE / "build_tokens.py")])
print("components.md", md.stat().st_size)
