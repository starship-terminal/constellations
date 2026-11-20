"""raw/component-tokens.json must rebuild from the raw readings, every ink step must cite a
reading that holds it (or say it was entered by hand), and the sans stack must cite a component
that paints it.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_component_tokens as bct  # noqa: E402

RAW = pathlib.Path(__file__).resolve().parent.parent / "raw"


class ComponentTokensTest(unittest.TestCase):
    def test_committed_spec_matches_builder(self):
        self.assertEqual(json.loads((RAW / "component-tokens.json").read_text()), bct.SPEC)

    def test_ink_steps_cite_a_reading_or_say_hand(self):
        text = (RAW / "components-computed.json").read_text() + (RAW / "css-vars.json").read_text()
        for name, leaf in bct.SPEC["core"]["palette"]["ink"].items():
            src = leaf["source"]
            if src.startswith("Reconstruction"):
                self.assertNotIn(leaf["value"], text, name)
            elif "raw/components-computed.json" in src:
                self.assertIn(leaf["value"], (RAW / "components-computed.json").read_text(), name)
        self.assertTrue(bct.SPEC["core"]["palette"]["ink"]["a33"]["source"].startswith("Reconstruction"))

    def test_sans_cites_a_component_that_paints_it(self):
        leaf = bct.SPEC["core"]["font"]["family"]["sans"]
        comp = leaf["source"].split(" of ")[1].split(" ")[0]
        self.assertEqual(bct.C[comp]["states"]["default"]["style"]["fontFamily"], leaf["value"])
        for wrong in ("nav-link", "footer"):
            self.assertNotEqual(bct.C[wrong]["states"]["default"]["style"]["fontFamily"], leaf["value"])

    def test_focus_ring_is_not_called_an_alias(self):
        src = bct.SPEC["light"]["focus"]["ring"]["source"]
        self.assertTrue(src.startswith("computed outlineColor"), src)


if __name__ == "__main__":
    unittest.main()
