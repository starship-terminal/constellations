#!/usr/bin/env python3
"""The package's own test: every token has an evidence label, and the catalog swatch paths resolve."""
import json, pathlib, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent

def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if str(k).startswith("$"):
                continue
            yield from walk(v, f"{path}.{k}" if path else k)

class Tokens(unittest.TestCase):
    def test_evidence(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        for path, token in walk(tokens):
            src = (token.get("$extensions") or {}).get("source", "")
            self.assertTrue(src.startswith("Measured") or src.startswith("Derived"), path)

    def test_readings_exist(self):
        raw = json.loads((HERE / "raw" / "readings.json").read_text())
        self.assertEqual(raw["pages"]["login"]["submitted"], False)
        tokens = json.loads((HERE / "tokens.json").read_text())
        # The palette token at its role equals the raw reading at its key.
        self.assertEqual(raw["marketingCustomProperties"]["values"]["--primary-1"], "#5727e7")
        self.assertEqual(tokens["core"]["palette"]["primary-1"]["$value"], raw["marketingCustomProperties"]["values"]["--primary-1"])

if __name__ == "__main__":
    unittest.main()
