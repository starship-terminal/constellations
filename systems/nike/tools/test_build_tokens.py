#!/usr/bin/env python3
"""The committed Nike tokens.json is what build_tokens.build() makes, with a source on every token.

The build runs in memory: nothing here writes tokens.json or style-guide.html."""
import html
import json
import pathlib
import re
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(HERE))
import build_tokens  # noqa: E402


class BuildTokens(unittest.TestCase):
    def test_committed_file_is_what_the_builder_makes(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), build_tokens.build())

    def test_every_token_is_sourced(self):
        tokens = build_tokens.build()
        self.assertIn("light", tokens)
        self.assertNotIn("dark", tokens)

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                self.assertTrue(node.get("$extensions", {}).get("source"), path)
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, f"{path}.{key}")

        walk(tokens["core"], "core")
        walk(tokens["light"], "light")
        self.assertEqual(tokens["light"]["page"]["$value"], "#ffffff")
        self.assertEqual(tokens["light"]["accent"]["$value"], "#111111")
        self.assertEqual(tokens["core"]["control"]["add-height"]["$value"], "60px")

    def test_style_guide_type_rows_survive_a_quoted_font_name(self):
        # A font-family holding double quotes must not close the style attribute (finding 19-5):
        # render the real type rows from a copy of the tokens whose stack names a quoted family.
        import copy
        sys.path.insert(0, str(HERE))
        import build_style_guide
        saved = build_style_guide.T
        doc = copy.deepcopy(saved)
        doc["core"]["font"]["family"]["text"]["$value"] = ['"Helvetica Now Text"', "Helvetica"]
        build_style_guide.T = doc
        try:
            rows = build_style_guide.type_rows()
        finally:
            build_style_guide.T = saved
        style = re.search(r'<div class="ty" style="([^"]*)"', rows).group(1)
        self.assertIn("font-size:16px", style)
        self.assertEqual(html.unescape(style).split(";")[0], 'font-family:"Helvetica Now Text", Helvetica')

if __name__ == "__main__":
    unittest.main()
