"""Rebuild checks for the Epidemic Sound builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ (without capture/) and raw/, with
empty stand-ins for the screenshot and crop files (only their names are read),
so nothing committed is rewritten.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


def flat(tree, path=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


def builder_fn(name, end, first=None):
    """A helper from the token builder, loaded without running the build
    (the source from `def first` or `def name` up to `end`)."""
    src = (PKG / "tools" / "build_component_tokens.py").read_text()
    start = src.index(f"def {first or name}(")
    ns = {"re": re}
    exec(src[start:src.index(end, start)], ns)
    return ns[name]


norm = builder_fn("norm_color", "\ndef have(")
MEASURED = re.compile(r"^(computed|measured) (\w+) of ([\w-]+) ([\w-]+)[ ;(]")


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for d in ("screenshots", "components/crops"):
            (root / d).mkdir(parents=True)
            for f in (PKG / d).glob("*.png"):
                (root / d / f.name).touch()
        for b in ("build_component_tokens.py", "build_tokens.py", "build_components_md.py", "build_style_guide.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.root = root
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def resolve(self, theme, v):
        while isinstance(v, str) and v.startswith("{"):
            node = None
            for s in (theme, "core"):
                node = self.built[s]
                for part in v[1:-1].split("."):
                    node = node.get(part) if isinstance(node, dict) else None
                if node:
                    break
            v = node["$value"]
        return v

    def test_committed_output_matches_rebuild(self):
        for f in ("tokens.json", "raw/component-tokens.json", "components.md", "style-guide.html"):
            self.assertEqual((PKG / f).read_text(), (self.root / f).read_text(), f)

    def test_measured_leaves_equal_their_reading(self):
        checked = 0
        for theme in ("core", "light", "dark"):
            for path, leaf in flat(self.built[theme]):
                m = MEASURED.match((leaf.get("$extensions") or {}).get("source", ""))
                if not m or m.group(2) == "transition":
                    continue
                kind, prop, comp, state = m.groups()
                rd = self.C[comp]["states"][state]
                if kind == "measured":
                    raw = "%gpx" % rd["rect"][prop]
                else:
                    # The builder reads the first text node only where the source says so.
                    first = "first text node" in leaf["$extensions"]["source"]
                    raw = ((rd.get("textStyle") or {}).get(prop) if first else None) or rd["style"][prop]
                got = self.resolve(theme, leaf["$value"])
                if leaf["$type"] == "color":
                    self.assertEqual(norm(got), norm(raw), path)
                elif prop == "fontWeight":
                    self.assertEqual(got, int(float(raw)), path)
                elif str(got).endswith("px") and raw.endswith("px"):
                    self.assertAlmostEqual(float(str(got)[:-2]), float(raw[:-2]), places=2, msg=path)
                else:
                    self.assertEqual(str(got), raw, path)
                checked += 1
        self.assertGreater(checked, 25)

    def test_transition_pairs_each_property_with_its_own_timing(self):
        transition = builder_fn("transition", "\ndef st(", first="_list")
        two = transition({"transitionProperty": "color, opacity", "transitionDuration": "0.1s, 0.3s",
                          "transitionTimingFunction": "ease, linear", "transitionDelay": "0s"})
        self.assertEqual(two, "color 0.1s ease, opacity 0.3s linear")
        self.assertEqual(transition({"transitionProperty": "all, opacity", "transitionDuration": "0.2s, 0s",
                                     "transitionTimingFunction": "linear(0, 0.8 50%, 1)"}),
                         "all 0.2s linear(0, 0.8 50%, 1), opacity 0s linear(0, 0.8 50%, 1)")
        self.assertEqual(transition(self.C["c-signup"]["states"]["default"]["style"]), "")

    def test_page_fields_are_read_from_the_body(self):
        for theme, key, comp in (("light", "page", "header"), ("dark", "canvas", "c-header")):
            leaf = self.built[theme]["background"][key]
            body = next(a["bg"] for a in self.C[comp]["states"]["default"]["ancestors"] if a["node"].startswith("body"))
            self.assertEqual(norm(self.resolve(theme, leaf["$value"])), norm(body), key)
            self.assertIn(f"ancestors of {comp} default", leaf["$extensions"]["source"])

    def test_paint_readers_pick_by_role_not_by_value(self):
        text = self.built["dark"]["text"]["text"]
        self.assertEqual(norm(self.resolve("dark", text["$value"])), norm(self.C["track-row"]["states"]["default"]["textStyle"]["color"]))
        up = self.built["dark"]["background"]["upsell"]
        self.assertIn("largest painted layer", up["$extensions"]["source"])

    def test_values_without_a_reading_say_so(self):
        for group, key in (("border", "divider"), ("action", "liked")):
            self.assertTrue(self.built["dark"][group][key]["$extensions"]["source"].startswith("entered by hand"), key)
        self.assertEqual(len(self.spec["_gaps"]), 3)

    def test_font_sizes_use_a_dtcg_type(self):
        for path, leaf in flat(self.built["core"]["font"]["size"]["measured"]):
            self.assertEqual(leaf["$type"], "dimension", path)

    def test_style_free_skipped_state_keeps_its_note(self):
        """The fixed capture saves a 0x0 state as { skipped } with no style."""
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
            shutil.copytree(PKG / "raw", root / "raw")
            shutil.copy(PKG / "tokens.json", root / "tokens.json")
            for sub in ("screenshots", "components/crops"):
                (root / sub).mkdir(parents=True)
            f = root / "raw" / "components-computed.json"
            j = json.loads(f.read_text())
            j["components"]["track-play"]["states"]["hover"] = {
                "skipped": "the element has a 0x0 box in this state (it left the layout)", "via": "mouse hover"}
            f.write_text(json.dumps(j))
            subprocess.run([sys.executable, str(root / "tools" / "build_components_md.py")], cwd=root, check=True, capture_output=True)
            entry = (root / "components.md").read_text().split("Read as `track-play`", 1)[1].split("\n#### ", 1)[0]
            self.assertIn("**Not a reading.** In `hover`", entry)

    def test_banner_layer_sizes_with_units_parse(self):
        src = (PKG / "tools" / "build_component_tokens.py").read_text()
        body = src[src.index("            def area(pl):"):src.index("            raw = max(")]
        ns = {"re": re}
        exec("\n".join(l[12:] for l in body.splitlines()), ns)
        self.assertEqual(ns["area"]({"size": "1328.0x244.0"}), 1328.0 * 244.0)
        self.assertEqual(ns["area"]({"size": "32pxx16px"}), 512.0)

    def test_zero_box_states_are_not_readings(self):
        md = (PKG / "components.md").read_text()
        entry = md.split("Read as `track-play`", 1)[1].split("\n#### ", 1)[0]
        self.assertIn("**Not a reading.**", entry)
        self.assertNotIn("| hover | size 0 x 0", entry)


if __name__ == "__main__":
    unittest.main()
