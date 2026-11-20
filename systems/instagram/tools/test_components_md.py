"""components.md is maintained by hand (no builder reproduces it; see the README's What to distrust).

So nothing regenerates it from the readings: every rgb() and px value in a row that links a crop
must be in that crop's reading in raw/components-computed.json, keyed by the crop's name.
"""
import json
import pathlib
import re
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
MD = (PKG / "components.md").read_text()


class ComponentsMdTest(unittest.TestCase):
    def test_crop_rows_quote_their_readings(self):
        rows = 0
        for line in MD.splitlines():
            m = re.search(r"\(components/crops/([\w-]+)\.png\)", line)
            if not line.startswith("|") or not m or m.group(1) not in RAW:
                continue
            rows += 1
            reading = {v for v in RAW[m.group(1)].values() if isinstance(v, str)}
            cells = [c.strip() for c in line.strip("|").split("|")]
            quoted = re.findall(r"rgba?\([^)]*\)", line) + [c for c in cells if re.fullmatch(r"\d+px", c)]
            for value in quoted:
                with self.subTest(crop=m.group(1), value=value):
                    self.assertIn(value, reading)
        self.assertGreaterEqual(rows, 10)


if __name__ == "__main__":
    unittest.main()
