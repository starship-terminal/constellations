import subprocess
import sys
from pathlib import Path


def test_tokens_match_readings():
    script = Path(__file__).with_name("build_tokens.py")
    result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
