"""measure.mjs keeps going past a page that throws, then exits nonzero naming it.

The capture script drives a browser and is not run in tests. Its page
bookkeeping lives in tools/capture/public/run-pages.mjs, which this test drives
under Node with one page that returns and one that throws.
"""
import pathlib
import shutil
import subprocess
import unittest

HERE = pathlib.Path(__file__).resolve().parent
MODULE = HERE / "capture" / "public" / "run-pages.mjs"
SCRIPT = HERE / "capture" / "public" / "measure.mjs"

DRIVER = """
const { pageRunner, exitStatus } = await import(process.argv[1]);
let current;
const { finished, broken, runPage } = pageRunner(() => current, () => {});
async function good() { current = 'home'; }
async function bad() { current = 'pricing'; throw new Error('goto timeout'); }
const plan = process.argv[2] === 'throw' ? [good, bad, good] : [good];
for (const fn of plan) await runPage(fn);
console.log(JSON.stringify({ finished: [...finished], broken: [...broken.keys()] }));
process.exitCode = exitStatus(broken);
"""


@unittest.skipUnless(shutil.which("node"), "Node.js is needed to drive run-pages.mjs")
class RunPagesTest(unittest.TestCase):
    def drive(self, mode):
        return subprocess.run(["node", "--input-type=module", "-e", DRIVER, MODULE.as_uri(), mode],
                              capture_output=True, text=True)

    def test_a_throwing_page_exits_nonzero_and_is_named(self):
        r = self.drive("throw")
        self.assertEqual(r.returncode, 1, r.stderr)
        self.assertIn('"broken":["pricing"]', r.stdout)
        self.assertIn('"finished":["home"]', r.stdout)
        self.assertIn("INCOMPLETE: pages threw: pricing (goto timeout)", r.stderr)

    def test_a_clean_run_exits_zero(self):
        r = self.drive("clean")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stderr, "")


class ScriptUsesRunnerTest(unittest.TestCase):
    def test_measure_sets_the_exit_status(self):
        src = SCRIPT.read_text()
        self.assertIn("from './run-pages.mjs'", src)
        self.assertIn("process.exitCode = exitStatus(broken)", src)


if __name__ == "__main__":
    unittest.main()
