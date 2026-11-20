"""components.md leaves focus states with no keyboard-focus reading out, as the kit's rule does.

A focus-visible state whose record says keyboard focus did not match :focus-visible (focus.matches
false), or where focus failed, holds the element at rest. components.md must say focus could not be
captured on it and must not link a crop that only such a state uses. Run from the package tools folder.
"""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def focus_not_captured(v):
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


class FocusNotCapturedTest(unittest.TestCase):
    def setUp(self):
        raw = json.loads((ROOT / "raw" / "components-computed.json").read_text())
        comps = raw.get("components", raw)
        self.states = [v for c in comps.values() for v in c["states"].values()]
        self.md = (ROOT / "components.md").read_text()

    def test_no_crop_of_a_not_captured_state_is_linked(self):
        kept = {v["crop"] for v in self.states if v.get("crop") and not focus_not_captured(v)}
        only = {v["crop"] for v in self.states if v.get("crop") and focus_not_captured(v)} - kept
        self.assertTrue(only)
        linked = set(re.findall(r"\]\((components/crops/[^)]+\.png)\)", self.md))
        self.assertEqual(sorted(linked & only), [])

    def test_each_not_captured_state_is_named(self):
        n = sum(1 for v in self.states if str(v.get("via", "")).startswith("keyboard") and focus_not_captured(v))
        self.assertGreater(n, 0)
        self.assertEqual(self.md.count("focus could not be captured on "), n)
        self.assertNotIn("cannot take keyboard focus", self.md)


if __name__ == "__main__":
    unittest.main()
