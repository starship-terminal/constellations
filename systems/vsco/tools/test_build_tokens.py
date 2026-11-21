"""The VSCO token builder refuses a leaf with no source."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def walk(node, path=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            assert v["$extensions"]["source"], path + k
        elif isinstance(v, dict):
            walk(v, path + k + ".")


def test_sources():
    walk(TOKENS["core"])
    walk(TOKENS["light"])
    assert "dark" not in TOKENS


def test_rebuild():
    subprocess.check_call([sys.executable, str(ROOT / "tools" / "build_tokens.py")])
    again = json.loads((ROOT / "tokens.json").read_text())
    assert again == TOKENS
