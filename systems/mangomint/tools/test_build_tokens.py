"""tokens.json and components.md are what the builders write, built in memory or in a copy."""
import copy
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


class Tokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_check_refuses_a_dangling_alias(self):
        sets = copy.deepcopy({"core": build_tokens.core, "light": build_tokens.light})
        sets["light"]["page"] = {"$value": "{color.nothing}", "$type": "color"}
        with self.assertRaises(KeyError):
            build_tokens.check(sets)

    def test_check_refuses_a_colour_alias_to_a_dimension(self):
        sets = copy.deepcopy({"core": build_tokens.core, "light": build_tokens.light})
        sets["light"]["page"] = {"$value": "{radius.pill}", "$type": "color"}
        with self.assertRaises(TypeError):
            build_tokens.check(sets)

    def test_check_refuses_a_reference_mixed_into_text(self):
        sets = copy.deepcopy({"core": build_tokens.core, "light": build_tokens.light})
        sets["core"]["radius"]["pill"]["$value"] = "48px {radius.login}"
        with self.assertRaises(ValueError):
            build_tokens.check(sets)

    def test_check_refuses_a_self_reference(self):
        sets = copy.deepcopy({"core": build_tokens.core, "light": build_tokens.light})
        sets["core"]["radius"]["pill"]["$value"] = "{radius.pill}"
        with self.assertRaises(ValueError):
            build_tokens.check(sets)

    def test_check_refuses_a_bad_dimension(self):
        sets = copy.deepcopy({"core": build_tokens.core, "light": build_tokens.light})
        sets["core"]["radius"]["pill"]["$value"] = "48"
        with self.assertRaises(ValueError):
            build_tokens.check(sets)


class Components(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        with tempfile.TemporaryDirectory() as tmp:
            pkg = pathlib.Path(tmp) / "pkg"
            shutil.copytree(ROOT, pkg, ignore=shutil.ignore_patterns("screenshots", "components", "icons", "boards"))
            subprocess.run([sys.executable, str(pkg / "tools" / "build_components_md.py")], check=True, capture_output=True)
            self.assertEqual((pkg / "components.md").read_text(), (ROOT / "components.md").read_text())


if __name__ == "__main__":
    unittest.main()
