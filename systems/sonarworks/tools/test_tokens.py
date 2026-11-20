"""The Sonarworks token file matches the values read on 2026-11-19."""
import json
import unittest
from pathlib import Path

TOKENS = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_page_and_nav(self):
        self.assertEqual(TOKENS["light"]["background"]["page"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["light"]["background"]["inverse"]["$value"], "#000000")
        self.assertEqual(TOKENS["light"]["text"]["secondary"]["$value"], "#96999c")

    def test_display_and_pill(self):
        display = TOKENS["core"]["typography"]["display"]["$value"]
        self.assertEqual(display["fontSize"], "44px")
        self.assertEqual(display["letterSpacing"], "-1.5px")
        self.assertEqual(TOKENS["core"]["radius"]["full"]["$value"], "9999px")

    def test_disabled_and_sale(self):
        self.assertEqual(TOKENS["light"]["background"]["disabled"]["$value"], "#d8d9da")
        self.assertEqual(TOKENS["light"]["status"]["sale"]["$value"], "#ffe701")
        self.assertEqual(TOKENS["light"]["action"]["trial"]["$value"], "#68befd")


    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not (node.get("$extensions") or {}).get("source"):
                    missing.append(path)
                return
            if isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        walk(v, f"{path}.{k}" if path else k)

        walk(TOKENS, "")
        self.assertEqual(missing, [])


# raw/ holds no value readings (readings.json and viewport.json record the pages, the viewport
# and why screenshots failed), so no token can claim a measured, declared or derived source.
# Every value was entered by hand at capture time (docs/EVIDENCE.md: Reconstruction).
RAW = Path(__file__).resolve().parent.parent / "raw"
HAND = "Reconstruction: entered by hand at capture time"
# token path -> the text in raw/ that holds its reading; empty until a recapture writes readings
RAW_BACKED = {}


def unbacked_claims(tree, backed, raw_text):
    """Token paths whose source claims a reading that raw/ does not hold."""
    bad = []

    def walk(node, path):
        if isinstance(node, dict) and "$value" in node:
            source = (node.get("$extensions") or {}).get("source", "")
            reading = backed.get(path)
            if reading is not None:
                if reading not in raw_text:
                    bad.append(path)
            elif not source.startswith(HAND):
                bad.append(path)
            return
        if isinstance(node, dict):
            for k, v in node.items():
                if not k.startswith("$"):
                    walk(v, f"{path}.{k}" if path else k)

    walk(tree, "")
    return bad


class Provenance(unittest.TestCase):
    def test_no_token_claims_a_reading_raw_does_not_hold(self):
        raw_text = "".join(p.read_text() for p in sorted(RAW.glob("*.json")))
        self.assertEqual(unbacked_claims(TOKENS, RAW_BACKED, raw_text), [])

    def test_a_measured_claim_without_a_reading_fails(self):
        tree = {"light": {"a": {"$value": "#000000", "$extensions": {"source": "Measured: body color"}},
                          "b": {"$value": "#ffffff", "$extensions": {"source": HAND + "; no raw/ file holds this reading."}}}}
        self.assertEqual(unbacked_claims(tree, {}, ""), ["light.a"])
        self.assertEqual(unbacked_claims(tree, {"light.a": "rgb(0, 0, 0)"}, "color rgb(0, 0, 0)"), [])


if __name__ == "__main__":
    unittest.main()
