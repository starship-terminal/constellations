"""The committed tokens.json still matches raw/readings.json, built in memory."""
import copy
import json
import pathlib
import unittest

import build_tokens

HERE = pathlib.Path(__file__).resolve().parent.parent
LABELS = {"Measured", "Derived", "Sampled", "Observed", "Reconstruction", "Not captured"}


class TokensTest(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        # Importing build_tokens no longer writes tokens.json; render() returns the text.
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.render())

    def test_measured_values(self):
        committed = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(committed["light"]["color"]["text"]["primary"]["$value"], build_tokens.HEX["ink"])
        self.assertEqual(committed["light"]["color"]["background"]["page"]["$value"], build_tokens.HEX["page"])
        self.assertIn("source", committed["core"]["fontSize"]["display"]["$extensions"])

    def test_every_label_is_in_the_evidence_vocabulary(self):
        for set_name in ("core", "light", "dark"):
            for path, token in build_tokens.tokens_of(build_tokens.tokens[set_name]):
                with self.subTest(token=f"{set_name}.{path}"):
                    self.assertIn(token["$extensions"]["source"]["evidence"], LABELS)

    def test_dark_alias_does_not_resolve_against_light(self):
        doc = copy.deepcopy(build_tokens.tokens)
        doc["light"]["onlyInLight"] = {"$value": "#ffffff", "$type": "color",
                                       "$extensions": {"source": {"evidence": "Measured", "where": "test"}}}
        doc["dark"]["color"]["text"]["primary"]["$value"] = "{onlyInLight}"
        with self.assertRaises(SystemExit):
            build_tokens.check(doc)


if __name__ == "__main__":
    unittest.main()
