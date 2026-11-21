#!/usr/bin/env python3
"""Run the token source check."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
raise SystemExit(subprocess.call([sys.executable, str(ROOT / "build_tokens.py")]))
