"""ClickUp public capture records measured values and a dated site tree."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicCaptureTest(unittest.TestCase):
    def test_tokens_have_sources(self):
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
        self.assertEqual(missing, [])

    def test_site_tree_is_dated(self):
        text = (ROOT / "site-tree.md").read_text()
        self.assertIn("2026-11-22", text)
        self.assertIn("November 2026", text)
        self.assertIn("https://app.clickup.com/login", text)
        self.assertIn("catalog.json", text)
        self.assertIn("login-extracted", text)

    def test_login_review_not_started(self):
        data = json.loads((ROOT / "login-review.json").read_text())
        self.assertEqual(data["loginExtracted"], "not-started")
        self.assertFalse(data["typed"])
        self.assertFalse(data["submitted"])
        self.assertFalse(data["identityProviderClicked"])
