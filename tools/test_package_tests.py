"""Tests for tools/package_tests.py. Run with `make test`."""
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import package_tests  # noqa: E402


def missing(name):
    def test(self):
        raise ModuleNotFoundError(f"No module named '{name}'", name=name)
    return test


class ResultTest(unittest.TestCase):
    def run_case(self, name):
        case = type("Case", (unittest.TestCase,), {"test_it": missing(name)})("test_it")
        result = package_tests.Result(io.StringIO(), True, 0)
        with mock.patch.object(package_tests, "installed", return_value=False):
            case.run(result)
        return result

    def test_missing_pillow_is_a_skip(self):
        result = self.run_case("PIL")
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.skipped), 1)
        self.assertIn("needs Pillow", result.skipped[0][1])

    def test_missing_pillow_submodule_is_a_skip(self):
        self.assertEqual(len(self.run_case("PIL.Image").skipped), 1)

    def test_bad_import_from_an_installed_package_is_an_error(self):
        # json stands in for an installed Pillow: the real installed() finds it, and the
        # traceback formatter can import it (3.15 imports a missing submodule's parent).
        case = type("Case", (unittest.TestCase,), {"test_it": missing("json.NoSuchModule")})("test_it")
        result = package_tests.Result(io.StringIO(), True, 0)
        with mock.patch.dict(package_tests.NEEDS, {"json": "Pillow"}):
            case.run(result)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(len(result.errors), 1)

    def test_import_failing_discovery_is_a_skip(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "test_needs.py").write_text("import absent_for_this_test\n")
            suite = unittest.defaultTestLoader.discover(tmp, pattern="test_*.py", top_level_dir=tmp)
            sys.path.remove(tmp)
        result = package_tests.Result(io.StringIO(), True, 0)
        with mock.patch.dict(package_tests.NEEDS, {"absent_for_this_test": "Pillow"}):
            suite.run(result)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.skipped), 1)

    def test_other_missing_module_is_an_error(self):
        result = self.run_case("numpy")
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(len(result.errors), 1)


class PackagesTest(unittest.TestCase):
    def test_finds_package_tools_with_tests_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in ("systems/b/tools/test_x.py", "systems/b/tools/test_y.py",
                        "systems/a/tools/test_x.py", "systems/c/tools/build.py"):
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                (root / rel).write_text("")
            self.assertEqual([p.parent.name for p in package_tests.packages(root)], ["a", "b"])
            self.assertEqual([p.parent.name for p in package_tests.packages(root, ["b"])], ["b"])


def write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


SIBLING_TEST = """import unittest
import sibling
class T(unittest.TestCase):
    def test_own_sibling(self):
        self.assertEqual(sibling.SLUG, {slug!r})
"""


class MainTest(unittest.TestCase):
    """Runs the real gate over a scratch systems/ tree, one interpreter per package."""

    def tree(self, tmp, slugs, failing=()):
        root = Path(tmp)
        for slug in slugs:
            write(root, f"systems/{slug}/tools/sibling.py", f"SLUG = {slug!r}\n")
            write(root, f"systems/{slug}/tools/test_sibling.py", SIBLING_TEST.format(slug=slug))
        for slug in failing:
            write(root, f"systems/{slug}/tools/test_fail.py",
                  "import unittest\nclass T(unittest.TestCase):\n    def test_fail(self):\n        self.fail()\n")
        return root

    def main(self, root, argv=()):
        with mock.patch("sys.stdout", io.StringIO()) as out, mock.patch("sys.stderr", io.StringIO()):
            code = package_tests.main(list(argv), root)
        return code, out.getvalue()

    def test_same_named_siblings_stay_separate(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = self.main(self.tree(tmp, ["one", "two"]))
        self.assertEqual(code, 0, out)
        self.assertIn("systems/one: 1 tests OK", out)
        self.assertIn("systems/two: 1 tests OK", out)

    def test_a_failing_package_fails_the_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = self.main(self.tree(tmp, ["one", "two"], failing=["two"]))
        self.assertEqual(code, 1)
        self.assertIn("1 failed: two", out)

    def test_unknown_slug_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, _ = self.main(self.tree(tmp, ["one"]), ["nope"])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
