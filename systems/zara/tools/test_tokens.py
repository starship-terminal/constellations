"""The token file matches the raw readings."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_page_is_white(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["color"]["bg"]["page"]["$value"], "#ffffff")
        self.assertEqual(tokens["light"]["color"]["text"]["primary"]["$value"], "#000000")
        self.assertEqual(tokens["core"]["radius"]["none"]["$value"], "0px")
        self.assertIn("source", tokens["light"]["action"]["primary"]["$extensions"])

    def test_committed_file_matches_builder(self):
        # Built in memory; the committed file is never rewritten by the test.
        import build_tokens
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.render())

    def test_translucent_surfaces_are_hex(self):
        import build_tokens
        bg = build_tokens.build()["light"]["color"]["bg"]
        self.assertEqual(bg["surface"]["$value"], "#ffffffbf")  # hsla(0, 0%, 100%, 0.75)
        self.assertEqual(bg["base-alt"]["$value"], "#fffffff2")  # hsla(0, 0%, 100%, 0.95)
        self.assertEqual(bg["overlay"]["$value"], "#00000040")  # rgba(0, 0, 0, 0.25)

    def test_check_refuses_a_dangling_alias_and_a_bad_colour(self):
        import copy
        import build_tokens
        doc = build_tokens.build()
        bad = copy.deepcopy(doc)
        bad["light"]["text"]["primary"]["$value"] = "{color.text.nothing}"
        with self.assertRaises(SystemExit):
            build_tokens.check(bad)
        bad = copy.deepcopy(doc)
        bad["light"]["color"]["bg"]["page"]["$value"] = "white"
        with self.assertRaises(SystemExit):
            build_tokens.check(bad)

    def test_check_refuses_a_self_alias_a_cycle_and_a_malformed_alias(self):
        import copy
        import build_tokens
        doc = build_tokens.build()
        for value, why in (("{color.text.primary}", "cycle"), ("{color.bg.page}oops", "malformed"), ("{", "malformed")):
            bad = copy.deepcopy(doc)
            bad["light"]["color"]["text"]["primary"]["$value"] = value
            with self.subTest(value=value), self.assertRaisesRegex(SystemExit, why):
                build_tokens.check(bad)

    def test_no_dark_set(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertNotIn("dark", tokens)


if __name__ == "__main__":
    unittest.main()
