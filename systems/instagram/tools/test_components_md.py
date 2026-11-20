"""components.md is maintained by hand (no builder reproduces it; see the README's What to distrust).

So nothing regenerates it from the readings: every table row that links a crop must have that
crop's reading in raw/components-computed.json, keyed by the crop's name, and every rgb() and px
value in the row must be in that reading, apart from the statements the README names as read off
the crops or measured on another state (CROP_READ).
"""
import json
import pathlib
import re
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
MD = (PKG / "components.md").read_text()

# (crop, value): in components.md but not in that crop's reading. The README lists each.
CROP_READ = {
    ("field-help-search-default", "16px"),  # the wrapper's radius, read off the crop
    ("field-username-focus", "1px"),        # the wrapper's focus border, read off the crop
    ("link-about-cta-default", "90px"),     # the radius on hover, from link-about-cta-hover
}


class ComponentsMdTest(unittest.TestCase):
    def test_crop_rows_quote_their_readings(self):
        rows = 0
        for line in MD.splitlines():
            m = re.search(r"\(components/crops/([\w-]+)\.png\)", line)
            if not line.startswith("|") or not m:
                continue
            crop = m.group(1)
            rows += 1
            with self.subTest(crop=crop):
                self.assertIn(crop, RAW, "a crop row with no raw reading")
            reading = {v for v in RAW.get(crop, {}).values() if isinstance(v, str)}
            quoted = re.findall(r"rgba?\([^)]*\)", line) + re.findall(r"\b\d+(?:\.\d+)?px\b", line)
            for value in quoted:
                if (crop, value) in CROP_READ:
                    continue
                with self.subTest(crop=crop, value=value):
                    self.assertIn(value, reading)
        self.assertGreaterEqual(rows, 12)

    def test_the_exceptions_are_still_in_the_file(self):
        for crop, value in CROP_READ:
            with self.subTest(crop=crop, value=value):
                row = next((l for l in MD.splitlines() if l.startswith("|") and f"crops/{crop}.png" in l), "")
                self.assertIn(value, row)


if __name__ == "__main__":
    unittest.main()
