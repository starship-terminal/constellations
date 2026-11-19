"""Tests for the kit's web builders (tools/kit/build/ and the capture build-measurements scripts) on a
small invented package: what they write, and that a rerun writes the same bytes. Run with `make test`;
the build-measurements halves need node and are skipped without it."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE / "kit"
NODE = shutil.which("node")

STYLE = {
    **{f"padding{d}": "0px" for d in ("Top", "Right", "Bottom", "Left")},
    **{f"border{d}Width": "0px" for d in ("Top", "Right", "Bottom", "Left")},
    **{f"border{d}Style": "none" for d in ("Top", "Right", "Bottom", "Left")},
    **{f"border{d}Color": "rgb(0, 0, 0)" for d in ("Top", "Right", "Bottom", "Left")},
    **{f"border{c}Radius": "8px" for c in ("TopLeft", "TopRight", "BottomRight", "BottomLeft")},
    "backgroundColor": "rgb(255, 255, 255)", "backgroundImage": "none", "boxShadow": "none", "backdropFilter": "none",
    "outlineStyle": "none", "outlineWidth": "0px", "outlineColor": "rgb(0, 0, 0)", "outlineOffset": "0px",
    "fontSize": "14px", "lineHeight": "20px", "fontWeight": "400", "fontFamily": "Inter, sans-serif", "color": "rgb(0, 0, 0)",
    "transitionDuration": "0s", "transitionProperty": "all", "transitionTimingFunction": "ease", "transform": "none", "opacity": "1",
}
RING = {"outlineStyle": "solid", "outlineWidth": "2px", "outlineColor": "rgb(0, 0, 255)", "outlineOffset": "2px"}


def state(style=None, **extra):
    return {"style": {**STYLE, **(style or {})}, "rect": {"x": 0, "y": 0, "w": 100, "h": 40}, **extra}


def package(d, builder, computed):
    """A package folder under d holding one kit builder (as tools/<name>) and the inputs it reads."""
    pkg = Path(d) / "pkg"
    for sub in ("tools", "raw", "screenshots", "components/crops", "icons"):
        (pkg / sub).mkdir(parents=True, exist_ok=True)
    shutil.copy(KIT / "build" / builder, pkg / "tools" / "build_components_md.py")
    (pkg / "raw" / "components-computed.json").write_text(json.dumps(computed))
    (pkg / "raw" / "layout.json").write_text("{}")
    (pkg / "tokens.json").write_text(json.dumps({"core": {"palette": {}}, "light": {}, "dark": {}}))
    (pkg / "icons" / "INDEX.tsv").write_text("file\tname\n")
    return pkg


def build(pkg):
    res = subprocess.run([sys.executable, str(pkg / "tools" / "build_components_md.py")], capture_output=True, text=True, timeout=60)
    if res.returncode:
        raise AssertionError(res.stderr[-2000:])
    return (pkg / "components.md").read_text()


PUBLIC = {
    "_meta": {"read": "2026-01-02"},
    "components": {
        "ring-button": {"title": "Ring button", "group": "Buttons", "page": "home",
                        "states": {"default": state(via="at rest"), "focus-visible": state(RING, via="Shift+Tab, Tab")}},
        "plain-button": {"title": "Plain button", "group": "Buttons", "page": "home",
                         "states": {"default": state(via="at rest"), "focus-visible": state(via="Shift+Tab, Tab")}},
        # an older run's shape: the element at rest saved under focus-visible
        "old-link": {"title": "Old link", "group": "Links", "page": "home",
                     "states": {"default": state(via="at rest"), "focus-visible": state({"backgroundColor": "rgb(1, 2, 3)"}, via="focus failed")}},
        # what measure.mjs records now
        "new-link": {"title": "New link", "group": "Links", "page": "home",
                     "states": {"default": state(via="at rest"), "focus-visible": {"skipped": "focus failed: keyboard focus did not reach the element", "via": "focus failed"}}},
    },
}


class PublicComponentsBuilder(unittest.TestCase):
    def test_a_failed_focus_is_not_counted_as_a_focus_that_draws_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            md = build(package(d, "build_components_md.public.py", PUBLIC))
        self.assertIn("2 components were given a real keyboard focus. 1 draw a ring: `ring-button` (2px solid #0000ff, offset 2px). "
                      "The other 1 draw none, so a keyboard user sees no change: `plain-button`.", md)
        self.assertIn("Focus could not be captured on 2 more (keyboard focus never landed on them, so their readings are left out): "
                      "`old-link`, `new-link`.", md)
        entry = md.split("#### Old link", 1)[1].split("####", 1)[0]
        self.assertNotIn("focus-visible", entry)
        self.assertNotIn("#010203", entry)

    def test_a_rerun_writes_the_same_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            pkg = package(d, "build_components_md.public.py", PUBLIC)
            self.assertEqual(build(pkg), build(pkg))


SIGNED_IN = {
    "_meta": {"read": "2026-01-02", "source": "copies", "snapshots": {}},
    "components": {
        "ring-button": {"title": "Ring button", "group": "Buttons", "page": "home-dark", "pages": ["home-dark"], "selector": "() => x",
                        "states": {"default": state(theme="dark", via="at rest"),
                                   "focus-visible": state(RING, theme="dark", via="keyboard", focus={"ok": True, "matches": True})}},
        "plain-row": {"title": "Plain row", "group": "Lists", "page": "home-dark", "pages": ["home-dark"], "selector": "() => x",
                      "states": {"default": state(theme="dark", via="at rest"),
                                 "focus-visible": state(theme="dark", via="keyboard", focus={"ok": True, "matches": False},
                                                        crop="components/crops/plain-row-focus-visible.png")}},
        "static-div": {"title": "Static div", "group": "Lists", "page": "home-dark", "pages": ["home-dark"], "selector": "() => x",
                       "states": {"default": state(theme="dark", via="at rest"),
                                  "focus-visible": {"theme": "dark", "snapshot": "home-dark", "skipped": "not focusable in the static copy (no tabindex)"}}},
    },
}


class SignedInComponentsBuilder(unittest.TestCase):
    def test_focus_without_focus_visible_is_left_out_of_the_tally(self):
        with tempfile.TemporaryDirectory() as d:
            pkg = package(d, "build_components_md.py", SIGNED_IN)
            (pkg / "components/crops/plain-row-focus-visible.png").write_bytes(b"png")   # an earlier run's crop
            md = build(pkg)
            self.assertEqual(md, build(pkg))
        line = next(ln for ln in md.splitlines() if ln.startswith("**Focus.**"))
        self.assertIn("Of 1 elements given a real keyboard focus in dark: 2px solid", line)
        self.assertNotIn("no ring on the element", line)
        self.assertIn("Focus could not be captured on 2 dark states", line)
        self.assertIn("`plain-row`, `static-div`", line)
        self.assertNotIn("plain-row-focus-visible.png", md)   # no image presents it as a captured focus either


@unittest.skipIf(NODE is None, "node is not on PATH")
class MeasurementBuilders(unittest.TestCase):
    def run_builder(self, d, route, computed):
        pkg = Path(d) / "pkg"
        (pkg / "tools/capture" / route).mkdir(parents=True)
        (pkg / "raw").mkdir()
        shutil.copy(KIT / "capture/css-colour.mjs", pkg / "tools/capture/css-colour.mjs")
        shutil.copy(KIT / "capture" / route / "build-measurements.mjs", pkg / "tools/capture" / route / "build-measurements.mjs")
        (pkg / "raw/components-computed.json").write_text(json.dumps(computed))
        res = subprocess.run([NODE, str(pkg / "tools/capture" / route / "build-measurements.mjs")], capture_output=True, text=True, timeout=60)
        self.assertEqual(res.returncode, 0, res.stderr)
        return (pkg / "raw/measurements.md").read_text()

    def test_public_measurements_show_a_failed_focus_as_skipped(self):
        with tempfile.TemporaryDirectory() as d:
            md = self.run_builder(d, "public", PUBLIC)
        old = md.split("#### old-link", 1)[1].split("####", 1)[0]
        self.assertIn("| Skipped | - | focus failed: keyboard focus did not reach the element |", old)
        self.assertNotIn("#010203", old)
        new = md.split("#### new-link", 1)[1].split("####", 1)[0]
        self.assertIn("| Skipped | - | focus failed: keyboard focus did not reach the element |", new)

    def test_signed_in_measurements_count_focus_without_focus_visible_apart(self):
        with tempfile.TemporaryDirectory() as d:
            md = self.run_builder(d, "signed-in", SIGNED_IN)
        self.assertIn("- **Focus-visible, dark** (1 focused states; focus could not be captured on 2 more): outline 2px solid #0000ff offset 2px (1).", md)


if __name__ == "__main__":
    unittest.main()
