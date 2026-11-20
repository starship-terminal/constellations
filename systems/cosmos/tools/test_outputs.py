"""Checks on cosmos's committed tokens."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tokens.json").read_text())


def leaves(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict) and not k.startswith("$"):
            yield from leaves(v, prefix + k + ".")


class Tokens(unittest.TestCase):
    def test_colours_are_srgb_with_the_authored_form_kept(self):
        for s in ("core", "light", "dark"):
            for name, t in leaves(T[s]):
                if t["$type"] != "color" or str(t["$value"]).startswith("{"):
                    continue
                self.assertRegex(t["$value"], r"^(#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\))$", f"{s}.{name}")
        scrim = T["light"]["color"]["alias"]["background"]["scrim"]
        self.assertEqual(scrim["$value"], "rgba(13, 13, 13, 0.4)")
        self.assertTrue(scrim["$extensions"]["authored"].startswith("color-mix("))

    def test_pill_radius_is_not_the_css_maximum(self):
        self.assertEqual(T["core"]["radius"]["full"]["$value"], "9999px")

    def test_a_wrong_element_reading_says_so(self):
        self.assertIn("recapture needed", T["light"]["component"]["hero-search-height"]["$extensions"]["source"])


if __name__ == "__main__":
    unittest.main()
