"""Checks on clipchamp's committed tokens."""
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
    def test_the_semantic_set_holds_no_pixel_sample(self):
        # docs/EVIDENCE.md: a sampled colour is labelled and kept out of the semantic sets.
        for name, t in leaves(T["light"]):
            src = t["$extensions"]["source"].lower()
            self.assertNotIn("sampl", src, name)
            self.assertNotIn("raw/full/", src, name)

    def test_the_sampled_band_fill_says_sampled(self):
        self.assertTrue(T["core"]["sampled"]["surfaceDark"]["$extensions"]["source"].startswith("Sampled:"))

    def test_the_shadow_token_is_named_for_the_component_it_was_read_from(self):
        # The builder reads the first painted shadow among nav-submenu, feature-card and faq-item;
        # the token must not keep a menu name when the card supplied it.
        role = {"nav-submenu": "menu", "feature-card": "card", "faq-item": "faq"}
        for name, t in T["light"]["shadow"].items():
            src = t["$extensions"]["source"]
            read = [c for c in role if f"of {c} " in src]
            self.assertEqual(len(read), 1, src)
            self.assertEqual(name, role[read[0]], src)


if __name__ == "__main__":
    unittest.main()
