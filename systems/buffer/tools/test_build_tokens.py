"""The Buffer package records computed styles. It does not rebuild tokens from a dump."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_tokens_have_sources():
    data = json.loads((ROOT / "tokens.json").read_text())
    missing = []

    def walk(node, path):
        if isinstance(node, dict) and "$value" in node:
            source = (node.get("$extensions") or {}).get("source")
            if not source:
                missing.append(path)
        elif isinstance(node, dict):
            for key, value in node.items():
                if key.startswith("$"):
                    continue
                walk(value, f"{path}.{key}" if path else key)

    walk(data, "")
    assert missing == []


def test_site_tree_is_dated():
    text = (ROOT / "site-tree.md").read_text()
    assert "2026-11-22" in text
    assert "login.buffer.com/login" in text
    assert "catalog.json" in text
