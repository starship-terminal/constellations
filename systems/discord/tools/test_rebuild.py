"""Rebuild checks for the Discord builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/ (screenshots/, components/ and icons/ are
linked read-only), so nothing committed is rewritten.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ("build_component_tokens.py", "build_tokens.py", "build_style_guide.py", "build_components_md.py")
OUTPUTS = ("tokens.json", "raw/component-tokens.json", "style-guide.html", "components.md")


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for d in ("screenshots", "components", "icons"):
            if (PKG / d).exists():
                (root / d).symlink_to(PKG / d)
        for b in BUILDERS:
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        for f in OUTPUTS:
            self.assertEqual((PKG / f).read_text(), (self.root / f).read_text(), f)

    def test_page_fields_say_where_they_came_from(self):
        light = self.built["light"]["background"]["page"]["$extensions"]["source"]
        self.assertTrue(light.startswith("sampled, not measured"), light)
        V = json.loads((PKG / "raw" / "css-vars.json").read_text())
        dark = self.built["dark"]["background"]["page"]
        self.assertTrue(dark["$extensions"]["source"].startswith("declared --background-base-lowest"))
        self.assertEqual(V["resolved"]["dark"]["--background-base-lowest"]["value"], "#121214")

    def test_paint_layers_are_picked_by_node(self):
        spec = json.loads((self.root / "raw" / "component-tokens.json").read_text())["dark"]
        paint = {n["node"]: n["bg"] for n in self.C["sc-card"]["states"]["default"]["paint"] if n.get("bg")}
        self.assertEqual(paint["article.guildItemContainer_OnY3sU"], "rgb(32, 32, 36)")
        self.assertEqual(paint["div.dotOnline_U3tHuW"], "rgb(67, 181, 129)")
        self.assertIn("article.guildItemContainer", spec["background"]["card"]["source"])
        self.assertIn("div.dotOnline", spec["text"]["online"]["source"])
        self.assertIn("div.wrapper", spec["background"]["field"]["source"])

    def _rebuild_with(self, name, edit):
        """Run build_component_tokens.py on a fresh temp copy whose readings `edit` changed."""
        root = pathlib.Path(self.tmp.name) / name
        shutil.copytree(self.root / "tools", root / "tools")
        shutil.copytree(self.root / "raw", root / "raw")
        path = root / "raw" / "components-computed.json"
        J = json.loads(path.read_text())
        edit(J["components"])
        path.write_text(json.dumps(J))
        subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, check=True, capture_output=True)
        return json.loads((root / "raw" / "component-tokens.json").read_text())["dark"]

    def test_paint_layers_follow_their_node_not_their_colour(self):
        def edit(C):
            paint = C["sc-card"]["states"]["default"]["paint"]
            for n in paint:
                if n["node"].startswith("article.guildItemContainer"):
                    n["bg"] = "rgb(1, 2, 3)"
                elif n["node"].startswith("div.dotOnline"):
                    n["bg"] = "rgb(4, 5, 6)"
                else:  # decoys that carry the colours the old picks looked for
                    n["bg"] = "rgb(32, 32, 36)" if "listIcon" in n["node"] else "rgb(67, 181, 129)"
            for n in C["lg-pass"]["states"]["default"]["ancestors"]:
                if n["node"].startswith("div.wrapper_"):
                    n["bg"] = "rgba(7, 8, 9, 0.5)"
        dark = self._rebuild_with("moved", edit)
        self.assertEqual(dark["background"]["card"]["value"], "#010203")
        self.assertEqual(dark["text"]["online"]["value"], "#040506")
        self.assertEqual(dark["background"]["field"]["value"], "rgba(7, 8, 9, 0.5)")

    def test_missing_layer_drops_the_role(self):
        def edit(C):
            C["sc-card"]["states"]["default"]["paint"] = [n for n in C["sc-card"]["states"]["default"]["paint"]
                                                         if not n["node"].startswith(("article.guildItemContainer", "div.dotOnline"))]
            C["lg-pass"]["states"]["default"]["ancestors"] = []
        dark = self._rebuild_with("missing", edit)
        self.assertNotIn("card", dark.get("background", {}))
        self.assertNotIn("field", dark.get("background", {}))
        self.assertNotIn("online", dark.get("text", {}))

    def test_components_md_labels_each_colour_once(self):
        import re
        md = (self.root / "components.md").read_text()
        self.assertEqual(re.findall(r"`([a-z0-9.-]+)` `\1`", md), [])


if __name__ == "__main__":
    unittest.main()
