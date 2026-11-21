#!/usr/bin/env python3
"""The token check exits 0 on the committed readings."""
import subprocess
import sys
from pathlib import Path

script = Path(__file__).with_name("build_tokens.py")
result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
if result.returncode != 0:
    sys.stderr.write(result.stdout + result.stderr)
    sys.exit(result.returncode)
print(result.stdout.strip())
