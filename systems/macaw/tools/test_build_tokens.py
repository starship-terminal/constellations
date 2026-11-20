"""tokens.json matches an in-memory build; hand-entered and UA values are not labelled Measured."""
import copy
import json
import pathlib
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())


class BuildTokens(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        import build_tokens  # builds and checks on import; writes only when run as a script
        self.assertEqual(TOKENS, json.loads(json.dumps(build_tokens.tokens)))

    def test_check_refuses_a_dead_alias(self):
        import build_tokens
        doc = copy.deepcopy(build_tokens.tokens)
        doc["light"]["page"]["$value"] = "{color.nothing}"
        with self.assertRaises(SystemExit):
            build_tokens.check(doc)

    def test_check_refuses_wrong_types_and_bad_colours(self):
        import build_tokens
        for bad in ("{size.button}", "rgba(nope)", "rgb()", 16):
            doc = copy.deepcopy(build_tokens.tokens)
            doc["light"]["page"]["$value"] = bad
            with self.assertRaises(SystemExit, msg=repr(bad)):
                build_tokens.check(doc)

    def test_values_with_no_reading_say_so(self):
        font = TOKENS["core"]["font"]
        for leaf in (font["size"]["section"], font["size"]["privacy-h2"], font["lineHeight"]["heading"],
                     font["lineHeight"]["section"], font["tracking"]["heading"], font["tracking"]["section"]):
            self.assertTrue(leaf["$extensions"]["source"].startswith("Reconstruction"))
        self.assertEqual(font["lineHeight"]["display"]["$value"], "64.32px")  # raw h1 lineHeight
        self.assertTrue(TOKENS["core"]["color"]["focusRing"]["$extensions"]["source"].startswith("Observed"))

    def test_shadows_are_dtcg_layers(self):
        for name, leaf in TOKENS["core"]["elevation"].items():
            self.assertIsInstance(leaf["$value"], list, name)


if __name__ == "__main__":
    unittest.main()
