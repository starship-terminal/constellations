"""tokens.json is what the builder writes, and the builder refuses malformed shadows and mistyped aliases."""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


class Tokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_shadow_layer_needs_px_lengths(self):
        with self.assertRaises(ValueError):
            build_tokens.check("x", "shadow", [{"offsetX": "0", "offsetY": "0px", "blur": "0px", "spread": "1px", "color": "#000000"}])

    def test_shadow_layer_needs_a_colour(self):
        with self.assertRaises(ValueError):
            build_tokens.check("x", "shadow", [{"offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "1px", "color": "nope"}])

    def test_gradient_needs_stops(self):
        with self.assertRaises(ValueError):
            build_tokens.check("x", "gradient", "linear-gradient(red, blue)")

    def sets(self):
        import copy
        return copy.deepcopy(build_tokens.core), copy.deepcopy(build_tokens.light), copy.deepcopy(build_tokens.dark)

    def test_committed_aliases_pass(self):
        build_tokens.check_aliases(*self.sets())

    def test_colour_alias_to_a_dimension_fails(self):
        core, light, dark = self.sets()
        dim = next(n for n, t in build_tokens.tokens_of(core) if t["$type"] == "dimension")
        col = next(n for n, t in build_tokens.tokens_of(light) if t["$type"] == "color")
        node = light
        for part in col.split(".")[:-1]:
            node = node[part]
        node[col.split(".")[-1]]["$value"] = "{%s}" % dim
        with self.assertRaises(TypeError):
            build_tokens.check_aliases(core, light, dark)

    def test_typography_size_alias_to_a_font_family_fails(self):
        core, light, dark = self.sets()
        fam = next(n for n, t in build_tokens.tokens_of(core) if t["$type"] == "fontFamily")
        style = next(t for n, t in build_tokens.tokens_of(core) if t["$type"] == "typography")
        style["$value"]["fontSize"] = "{%s}" % fam
        with self.assertRaises(TypeError):
            build_tokens.check_aliases(core, light, dark)

    def test_shadow_colour_alias_to_a_dimension_fails(self):
        core, light, dark = self.sets()
        dim = next(n for n, t in build_tokens.tokens_of(core) if t["$type"] == "dimension")
        core["elevation"]["ring"]["$value"][0]["color"] = "{%s}" % dim
        with self.assertRaises(TypeError):
            build_tokens.check_aliases(core, light, dark)

    def test_gradient_needs_usable_stops(self):
        for bad in ([], [{"color": "#000000", "position": "0"}, {"color": "#ffffff", "position": 1}],
                    [{"color": "nope", "position": 0}, {"color": "#ffffff", "position": 1}]):
            with self.assertRaises(ValueError):
                build_tokens.check("x", "gradient", bad)
        build_tokens.check("x", "gradient", [{"color": "#000000", "position": 0}, {"color": "#ffffff", "position": 1}])

    def test_committed_shadow_passes(self):
        ring = build_tokens.core["elevation"]["ring"]
        build_tokens.check("core.elevation.ring", "shadow", ring["$value"])


class IconRefs(unittest.TestCase):
    """capture/svg_refs.mjs names the ids icons.mjs keeps; a <use> target must be among them."""

    FIXTURE = (
        '<svg xmlns="http://www.w3.org/2000/svg"><defs><path id="glyph" d="M0 0h8v8z"/>'
        '<linearGradient id="fade"/><path id="legacy" d="M1 1z"/><clipPath id="unused"/></defs>'
        '<use href="#glyph"/><use xlink:href=\'#legacy\'/><rect fill="url(#fade)"/>'
        '<g style="mask: url(&quot;#m1&quot;)"/><a href="https://example.com/#nope"/></svg>'
    )

    def refs(self, html):
        import json
        import shutil
        import subprocess
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        mod = (ROOT / "tools" / "capture" / "svg_refs.mjs").as_uri()
        js = f"import {{ fragmentRefs }} from {json.dumps(mod)}; console.log(JSON.stringify([...fragmentRefs(process.argv[1])].sort()))"
        out = subprocess.run([node, "--input-type=module", "-e", js, html], capture_output=True, text=True, check=True)
        return json.loads(out.stdout)

    def test_use_href_and_xlink_href_targets_are_kept(self):
        self.assertEqual(self.refs(self.FIXTURE), ["fade", "glyph", "legacy", "m1"])

    def test_unreferenced_and_external_ids_are_not(self):
        got = self.refs(self.FIXTURE)
        self.assertNotIn("unused", got)
        self.assertNotIn("nope", got)


if __name__ == "__main__":
    unittest.main()
