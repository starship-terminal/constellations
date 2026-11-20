"""Rebuild checks for the Endel builders. Run from this folder, or via tools/package_tests.py.

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
J = json.loads((PKG / "raw" / "components-computed.json").read_text())


def flat(tree, path=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


def builder_ns():
    """stprop() and norm_color() from the token builder, loaded without running the build."""
    src = (PKG / "tools" / "build_component_tokens.py").read_text()
    ns = {"re": re, "COMP": J["components"]}
    exec(src[src.index("def stprop("):src.index("\nBY_VALUE = ")], ns)
    return ns


NS = builder_ns()
COMPUTED = re.compile(r"^computed (\S+) of ([\w-]+) ([\w-]+) \(raw/components-computed\.json\)")


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
        for b in ("build_component_tokens.py", "build_tokens.py", "build_style_guide.py", "build_components_md.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.root = root
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        cls.C = J["components"]

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

    def test_computed_leaves_equal_their_reading(self):
        checked = 0
        for theme in ("core", "dark"):
            for path, leaf in flat(self.built[theme]):
                m = COMPUTED.match((leaf.get("$extensions") or {}).get("source", ""))
                if not m:
                    continue
                prop, comp, state = m.groups()
                rd = self.C[comp]["states"][state]
                if prop in ("boxShadow", "backgroundImage", "transitionDuration", "transitionTimingFunction", "paint.0.size"):
                    continue  # parsed values; covered below
                if prop in ("rect.w", "rect.h", "icon.w"):
                    part, key = prop.split(".")
                    raw = "%gpx" % rd[part][key]
                else:
                    raw = NS["stprop"](comp, state, prop.replace("style.", ""))
                got = self.resolve(theme, leaf["$value"])
                if leaf["$type"] == "color":
                    self.assertEqual(NS["norm_color"](str(got)), NS["norm_color"](raw), path)
                else:
                    self.assertEqual(str(got), raw.split()[0] if leaf["$type"] == "dimension" else raw, path)
                checked += 1
        self.assertGreater(checked, 40)

    def test_motion_and_gradients_are_read_not_typed(self):
        s = self.C["btn-signin"]["states"]["default"]["style"]
        core = self.built["core"]
        self.assertEqual(core["duration"]["hover"]["$value"], "%gms" % (float(s["transitionDuration"].split(",")[0][:-1]) * 1000))
        self.assertEqual({x.strip() for x in s["transitionTimingFunction"].split(",")}, {"ease"})
        sheets = [r for rules in J["_meta"]["sheets"].values() for r in rules]
        enter = next(r["animation"] for r in sheets if r["selector"] == ".slide-in-out-enter")
        self.assertIn("cubic-bezier(%s)" % ", ".join("%g" % x for x in core["easing"]["sheetIn"]["$value"]), enter)
        stops = core["gradient"]["headerScrim"]["$value"]
        self.assertEqual([x["position"] for x in stops], [0, 0.5, 1])
        self.assertIn("rgba(0, 0, 0, 0.65) 50%", self.C["header"]["states"]["default"]["style"]["backgroundImage"])

    def motion_helpers(self, sheets=None):
        src = (PKG / "tools" / "build_component_tokens.py").read_text()
        ns = {"re": re, "C": {"_meta": {"sheets": sheets if sheets is not None else J["_meta"]["sheets"]}},
              "norm_color": NS["norm_color"]}
        exec(src[src.index("def one("):src.index("\n_btn = st(")], ns)
        return ns

    def test_gradient_fills_omitted_stop_positions(self):
        g = self.motion_helpers()["gradient"]
        self.assertEqual(g("linear-gradient(rgb(0, 0, 0), rgba(0, 0, 0, 0.65) 50%, rgba(0, 0, 0, 0))"),
                         [{"color": "#000000", "position": 0}, {"color": "rgba(0, 0, 0, 0.65)", "position": 0.5},
                          {"color": "rgba(0, 0, 0, 0)", "position": 1}])
        self.assertEqual([x["position"] for x in g("linear-gradient(180deg, #111111, #222222, #333333)")], [0, 0.5, 1])
        with self.assertRaises(SystemExit):
            g("linear-gradient(rgb(0, 0, 0) 0%, var(--x) 100%)")

    def test_sheet_motion_is_read_from_the_app_page(self):
        sheets = json.loads(json.dumps(J["_meta"]["sheets"]))
        self.assertEqual(self.motion_helpers(sheets)["sheet_animation"](".slide-in-out-enter"),
                         ("0.3s", "cubic-bezier(0.25, 0.46, 0.45, 0.94)"))
        sheets.pop("app-explore")
        with self.assertRaises(SystemExit):
            self.motion_helpers(sheets)["sheet_animation"](".slide-in-out-enter")
        sheets = json.loads(json.dumps(J["_meta"]["sheets"]))
        for r in sheets["app-explore"]:
            r["animation"] = r["animation"].replace("0.3s", "0.4s")
        with self.assertRaises(SystemExit):
            self.motion_helpers(sheets)["sheet_animation"](".slide-in-out-enter")

    def test_empty_font_reading_stops_the_build(self):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
            shutil.copytree(PKG / "raw", root / "raw")
            f = root / "raw" / "components-computed.json"
            j = json.loads(f.read_text())
            j["components"]["banner"]["states"]["default"]["textStyle"]["fontFamily"] = ""
            f.write_text(json.dumps(j))
            r = subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("appMediumStack", r.stderr)

    def test_flagged_components_are_refused_by_every_reader(self):
        comp = dict(self.C["btn-signin"], recaptureMissed="2026-11-20")
        ns = {"re": re, "COMP": {"x": comp}}
        src = (PKG / "tools" / "build_component_tokens.py").read_text()
        exec(src[src.index("def stprop("):src.index("\ndef norm_color(")], ns)
        with self.assertRaises(KeyError):
            ns["stprop"]("x", "default", "backgroundColor")

    def test_failed_focus_is_not_a_state_row(self):
        md = (PKG / "components.md").read_text()
        entry = md.split("Read as `button-mode`", 1)[1].split("\n#### ", 1)[0]
        self.assertIn("**Focus not capturable.**", entry)
        self.assertNotIn("focus-visible, pressed)", entry)
        meas = (PKG / "raw" / "measurements.md").read_text().split("#### button-mode", 1)[1].split("\n#### ", 1)[0]
        self.assertIn("| Skipped |", meas)

    def test_no_named_row_was_dropped(self):
        self.assertNotIn("_gaps", self.spec)


if __name__ == "__main__":
    unittest.main()
