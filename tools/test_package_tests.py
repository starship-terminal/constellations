"""Tests for tools/package_tests.py. Run with `make test`."""
import io
import json
import shutil
import subprocess
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
    def test_finds_test_files_at_any_depth_outside_evidence_folders(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in ("systems/b/tools/test_x.py", "systems/b/tools/native/test_y.py",
                        "systems/b/tools/capture/test_serve.mjs", "systems/b/tools/capture/electron/stop.test.mjs",
                        "systems/b/native/test_z.py", "systems/b/raw/test_dump.py",
                        "systems/b/tools/capture/node_modules/x/test_dep.mjs",
                        "systems/a/tools/test_x.py", "systems/c/tools/build.py", "systems/d/tools/capture/test_q.py"):
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                (root / rel).write_text("")
            found = package_tests.packages(root)
            self.assertEqual(list(found), ["a", "b", "d"])
            self.assertEqual(found["b"], ["native/test_z.py", "tools/capture/electron/stop.test.mjs",
                                          "tools/capture/test_serve.mjs", "tools/native/test_y.py", "tools/test_x.py"])
            self.assertEqual(list(package_tests.packages(root, ["d"])), ["d"])


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
    """Runs the real gate over a scratch systems/ tree, one interpreter per test file."""

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
        with mock.patch("sys.stdout", io.StringIO()) as out, mock.patch("sys.stderr", io.StringIO()) as err:
            code = package_tests.main(list(argv), root)
        return code, out.getvalue() + err.getvalue()

    def test_same_named_siblings_stay_separate(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = self.main(self.tree(tmp, ["one", "two"]))
        self.assertEqual(code, 0, out)
        self.assertIn("systems/one/tools/test_sibling.py: 1 tests OK", out)
        self.assertIn("systems/two/tools/test_sibling.py: 1 tests OK", out)

    def test_a_nested_test_runs_from_its_own_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.tree(tmp, ["one"])
            write(root, "systems/one/tools/native/sibling.py", "SLUG = 'native'\n")
            write(root, "systems/one/tools/native/test_sibling.py", SIBLING_TEST.format(slug="native"))
            code, out = self.main(root)
        self.assertEqual(code, 0, out)
        self.assertIn("systems/one/tools/native/test_sibling.py: 1 tests OK", out)

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_mjs_tests_run_under_node(self):
        passing = "import test from 'node:test';\ntest('ok', () => {});\n"
        failing = "import test from 'node:test';\nimport assert from 'node:assert';\ntest('no', () => assert.fail());\n"
        with tempfile.TemporaryDirectory() as tmp:
            root = self.tree(tmp, ["one"])
            write(root, "systems/one/tools/capture/test_ok.mjs", passing)
            code, out = self.main(root)
            self.assertEqual(code, 0, out)
            self.assertIn("systems/one/tools/capture/test_ok.mjs: 1 tests, 0 failed (node --test)", out)
            write(root, "systems/one/tools/capture/test_no.mjs", failing)
            code, out = self.main(root)
        self.assertEqual(code, 1, out)
        self.assertIn("1 failed: systems/one/tools/capture/test_no.mjs", out)

    def test_a_failing_package_fails_the_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = self.main(self.tree(tmp, ["one", "two"], failing=["two"]))
        self.assertEqual(code, 1)
        self.assertIn("1 failed: systems/two/tools/test_fail.py", out)

    def test_an_expected_failure_is_reported_and_must_keep_failing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.tree(tmp, ["one", "two"], failing=["two"])
            listed = {"systems/two/tools/test_fail.py": "known: routed to the package owner"}
            write(root, package_tests.EXPECTED, json.dumps(listed))
            code, out = self.main(root)
            self.assertEqual(code, 0, out)
            self.assertIn("expected failure: known: routed to the package owner", out)
            # Once it passes, the run says the entry can go (a warning: it may fail elsewhere).
            write(root, "systems/two/tools/test_fail.py", "import unittest\n")
            code, out = self.main(root)
            self.assertEqual(code, 0, out)
            self.assertIn("passes here but is listed", out)
            # An entry naming no test file is stale too.
            write(root, package_tests.EXPECTED, json.dumps({"systems/two/tools/test_gone.py": "x"}))
            code, out = self.main(root)
        self.assertEqual(code, 1, out)
        self.assertIn("not a package test file", out)

    def test_a_test_that_rewrites_its_package_runs_on_a_copy(self):
        rewrite = ("import pathlib, unittest\nclass T(unittest.TestCase):\n    def test_it(self):\n"
                   "        pathlib.Path('../tokens.json').write_text('changed')\n")
        with tempfile.TemporaryDirectory() as tmp:
            root = self.tree(tmp, ["one"])
            write(root, "systems/one/tokens.json", "{}")
            write(root, "systems/one/tools/test_rewrite.py", rewrite)
            code, out = self.main(root)
            self.assertEqual(code, 0, out)
            self.assertEqual((root / "systems/one/tokens.json").read_text(), "{}")

    def test_a_test_that_writes_into_the_checkout_fails_the_run(self):
        escape = ("import pathlib, unittest\nclass T(unittest.TestCase):\n    def test_it(self):\n"
                  "        (pathlib.Path('../../..').resolve() / 'tools' / 'stray.txt').write_text('x')\n")
        with tempfile.TemporaryDirectory() as tmp:
            root = self.tree(tmp, ["one"])
            write(root, "tools/keep.txt", "")
            write(root, "systems/one/tools/test_escape.py", escape)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            code, out = self.main(root)
        self.assertEqual(code, 1, out)
        self.assertIn("a package test changed the checkout: ?? tools/stray.txt", out)

    def test_a_test_that_changes_an_already_dirty_or_untracked_file_fails_the_run(self):
        for target, change in (("tools/keep.txt", "write_text('edited again')"),   # tracked, already modified
                               ("tools/scratch.txt", "write_text('changed')"),      # untracked
                               ("tools/scratch.txt", "unlink()")):                 # untracked, removed
            escape = ("import pathlib, unittest\nclass T(unittest.TestCase):\n    def test_it(self):\n"
                      f"        (pathlib.Path('../../..').resolve() / {target!r}).{change}\n")
            with self.subTest(target=target, change=change), tempfile.TemporaryDirectory() as tmp:
                root = self.tree(tmp, ["one"])
                write(root, "tools/keep.txt", "")
                write(root, "systems/one/tools/test_escape.py", escape)
                subprocess.run(["git", "init", "-q"], cwd=root, check=True)
                subprocess.run(["git", "add", "."], cwd=root, check=True)
                write(root, "tools/keep.txt", "edited before the run")
                write(root, "tools/scratch.txt", "untracked before the run")
                code, out = self.main(root)
                self.assertEqual(code, 1, out)
                self.assertIn(f"a package test changed the checkout: ", out)
                self.assertIn(target, out.split("changed the checkout: ", 1)[1])

    def test_unknown_slug_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, _ = self.main(self.tree(tmp, ["one"]), ["nope"])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
