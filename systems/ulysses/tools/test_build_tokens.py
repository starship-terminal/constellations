"""The token check exits 0 against the committed readings."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def test_tokens_match_readings():
    script = ROOT / "build_tokens.py"
    result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
