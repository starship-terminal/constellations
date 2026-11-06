"""build_components_md.py links every crop tools/crops.json lists and stops when one of them is missing,
in either theme. The builder runs on a temporary package folder, so components.md is not rewritten."""
import importlib.util
import json
import pathlib
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent


def load():
    spec = importlib.util.spec_from_file_location("build_components_md_under_test", HERE / "build_components_md.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class CropLinks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.pkg = pathlib.Path(self.tmp.name)
        self.m = load()
        self.m.PKG, self.m.CROPS = self.pkg, self.pkg / "components" / "crops"
        self.m.CROPS.mkdir(parents=True)
        path = sorted(self.m.KNOWN)[0]
        self.m.INVENTORY = [("Button", "buttons", "A button.", [("fill", path)], [("default", "button-default")], "")]
        self.m.THEMES_OF = {"button-default": {"dark", "light"}}

    def tearDown(self):
        self.tmp.cleanup()

    def crop(self, name):
        (self.m.CROPS / name).write_bytes(b"")

    def test_both_themes_are_linked(self):
        self.crop("button-default.png")
        self.crop("button-default-light.png")
        self.m.main()
        md = (self.pkg / "components.md").read_text()
        self.assertIn("(components/crops/button-default.png)", md)
        self.assertIn("(components/crops/button-default-light.png)", md)

    def test_missing_light_crop_stops_the_build(self):
        self.crop("button-default.png")
        with self.assertRaises(SystemExit):
            self.m.main()
        self.assertFalse((self.pkg / "components.md").exists())

    def test_crop_not_in_crops_json_stops_the_build(self):
        self.m.THEMES_OF = {}
        self.crop("button-default.png")
        with self.assertRaises(SystemExit):
            self.m.main()

    def test_dark_only_crop_needs_no_light_file(self):
        self.m.THEMES_OF = {"button-default": {"dark"}}
        self.crop("button-default.png")
        self.m.main()
        self.assertNotIn("light", (self.pkg / "components.md").read_text().split("Crops:")[1].split("\n")[0])


class Manifest(unittest.TestCase):
    def test_themes_come_from_crops_json(self):
        m = load()
        crops = json.loads((HERE / "crops.json").read_text())["crops"]
        self.assertTrue(crops)
        for c in crops:
            self.assertTrue(set(c["themes"]) <= m.THEMES_OF[c["name"]], c["name"])
        self.assertEqual(set(m.THEMES_OF), {c["name"] for c in crops})

    def test_every_inventory_crop_is_in_crops_json(self):
        m = load()
        for name, _, _, _, states, _ in m.INVENTORY:
            for _, stem in states:
                self.assertIn(stem, m.THEMES_OF, f"{name}: {stem}")


if __name__ == "__main__":
    unittest.main()
