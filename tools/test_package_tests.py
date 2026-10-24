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
        case.run(result)
        return result

    def test_missing_pillow_is_a_skip(self):
        result = self.run_case("PIL")
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.skipped), 1)
        self.assertIn("needs Pillow", result.skipped[0][1])

    def test_missing_pillow_submodule_is_a_skip(self):
        self.assertEqual(len(self.run_case("PIL.Image").skipped), 1)

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


if __name__ == "__main__":
    unittest.main()
