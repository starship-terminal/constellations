"""build_tokens.py's checks: the committed file passes, and each kind of broken file is refused."""
import copy
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
READINGS = json.loads((HERE / "raw" / "readings.json").read_text())
SRC = {"source": "Measured. test fixture"}


class Check(unittest.TestCase):
    def test_committed_tokens_pass(self):
        self.assertEqual(build_tokens.problems(TOKENS, READINGS), [])

    def broken(self, **leaf):
        t = copy.deepcopy(TOKENS)
        t["core"]["palette"]["zz-test"] = dict({"$type": "color", "$extensions": SRC}, **leaf)
        return build_tokens.problems(t, READINGS)

    def test_colour_not_in_readings_is_refused(self):
        self.assertTrue(any("in no reading" in p for p in self.broken(**{"$value": "#123457"})))

    def test_reading_colour_is_accepted(self):
        self.assertEqual(self.broken(**{"$value": "#5727E7"}), [])

    def test_dead_alias_is_refused(self):
        self.assertTrue(any("dead alias" in p for p in self.broken(**{"$value": "{palette.nope}"})))

    def test_self_alias_is_refused(self):
        self.assertTrue(any("cycle" in p for p in self.broken(**{"$value": "{palette.zz-test}"})))

    def test_unlabelled_source_is_refused(self):
        t = copy.deepcopy(TOKENS)
        t["core"]["palette"]["zz-test"] = {"$value": "#5727e7", "$type": "color", "$extensions": {"source": "guessed"}}
        self.assertTrue(any("not Measured or Derived" in p for p in build_tokens.problems(t, READINGS)))

    def test_recorded_rgb_and_rgba_token_values_are_accepted(self):
        self.assertEqual(self.broken(**{"$value": "rgb(87, 39, 231)"}), [])        # #5727e7
        self.assertEqual(self.broken(**{"$value": "rgba(27, 27, 32, 0.3)"}), [])   # #1b1b204d
        self.assertEqual(self.broken(**{"$value": "rgb(0, 0, 0)"}), [])            # #000000

    def test_unrecorded_shadow_colour_is_refused(self):
        t = copy.deepcopy(TOKENS)
        t["light"]["shadow"]["tab"]["$value"]["color"] = "#123457"
        self.assertTrue(any("light.shadow.tab" in p and "in no reading" in p for p in build_tokens.problems(t, READINGS)))

    def test_chain_through_core_resolves_from_core(self):
        # light.font.shared -> {core.font.shared} -> {font.base} reads core.font.base (Inter), not the
        # light theme's own font.base override.
        tree = {"core": {"font": {"base": {"$value": "Inter"}, "shared": {"$value": "{font.base}"}}},
                "light": {"font": {"base": {"$value": "{font.shared}"}, "shared": {"$value": "{core.font.shared}"}}}}
        self.assertIsNone(build_tokens.resolve(tree, "light", "core.font.shared", set()))
        tree["core"]["font"]["base"]["$value"] = "{font.shared}"   # now core loops on itself
        self.assertIn("cycle", build_tokens.resolve(tree, "light", "core.font.shared", set()))

    def test_rgba_alpha_rounds_half_up(self):
        self.assertIn("#1b1b204d", build_tokens.colours_in("rgba(27, 27, 32, 0.3)"))


if __name__ == "__main__":
    unittest.main()
