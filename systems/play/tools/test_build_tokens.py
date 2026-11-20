#!/usr/bin/env python3
"""The Play token file passes its check: every value is a reading in raw/ or labelled Reconstruction."""
import json
import tempfile
import unittest
from pathlib import Path

import build_tokens


class Tokens(unittest.TestCase):
    def test_tokens_match_the_readings(self):
        self.assertEqual(build_tokens.main(), 0)

    def test_a_measured_label_needs_a_reading_in_raw(self):
        seen = build_tokens.raw_strings()

        def doc(value, source):
            return {"dark": {"c": {"$type": "color", "$value": value, "$extensions": {"source": source}}}}

        # #17ffa6 is a declared Stitches colour raw/ holds; #8ca4ba (token.steel) is in no raw file.
        self.assertEqual(build_tokens.check(doc("#17ffa6", "Declared Stitches --colors-playGreen"), seen)[0], [])
        problems, _ = build_tokens.check(doc("#8ca4ba", "Declared Framer --token"), seen)
        self.assertTrue(any("no reading" in p for p in problems), problems)
        self.assertEqual(build_tokens.check(doc("#8ca4ba", "Reconstruction: entered by hand"), seen)[0], [])

    def test_rgba_readings_keep_their_alpha(self):
        # A saved rgba() reading must match the translucent token (#ffffff12), not an opaque one.
        saved = build_tokens.HERE
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "raw").mkdir()
            (Path(tmp) / "raw" / "chip.json").write_text(json.dumps({"fill": "rgba(255, 255, 255, 0.07)"}))
            build_tokens.HERE = Path(tmp)
            try:
                seen = build_tokens.raw_strings()
            finally:
                build_tokens.HERE = saved
        self.assertIn("#ffffff12", seen)
        self.assertNotIn("#ffffff", seen)


if __name__ == "__main__":
    unittest.main()
