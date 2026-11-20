"""The toggled-state restore in capture/public/toggle.mjs, run in Node against
a mock control: a press that failed is never undone (it would collapse the
sidebar), a press that threw after it landed is, and the restore stops once
the control is back where it started (2026-11 audit, review on PR 1254, ported here)."""
import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOGGLE = HERE / "capture" / "public" / "toggle.mjs"
MEASURE = HERE / "capture" / "public" / "measure.mjs"

SCRIPT = r"""
const { toggleBefore, toggleOpen, toggleRestore } = await import(process.argv[1]);
// one control whose state flips on each landed press
function control({ start = 'expanded', pressLands = true, pressThrows = false, restoreThrows = 0 } = {}) {
  const c = { state: start, presses: 0, restores: 0, restoreThrows };
  const flip = () => { c.state = c.state === 'expanded' ? 'collapsed' : 'expanded'; };
  c.st = {
    stateOf: async () => c.state,
    fn: async () => { if (pressLands) { flip(); c.presses++; } if (pressThrows) throw new Error('click timed out'); },
    restore: async () => { flip(); c.restores++; if (c.restoreThrows > 0) { c.restoreThrows--; throw new Error('stale'); } },
  };
  return c;
}
async function run(c, { stateOf = true } = {}) {
  const st = stateOf ? c.st : { fn: c.st.fn, restore: c.st.restore };
  const rec = await toggleBefore(st, 'loc');
  let opened = true;
  try { await toggleOpen(st, rec); } catch { opened = false; }
  const result = await toggleRestore(st, rec, async () => 'loc2').catch((e) => 'ERR ' + e.message);
  return { opened, result, state: c.state, restores: c.restores };
}
const out = {};
out.ok = await run(control());
out.pressFailed = await run(control({ pressLands: false, pressThrows: true }));
out.pressThrewAfterLanding = await run(control({ pressThrows: true }));
out.pressNoChange = await run(control({ pressLands: false }));
out.staleRestoreLanded = await run(control({ restoreThrows: 1 }));
out.flagOnlyFailed = await run(control({ pressLands: false, pressThrows: true }), { stateOf: false });
out.flagOnlyOk = await run(control(), { stateOf: false });
console.log(JSON.stringify(out));
"""


@unittest.skipUnless(shutil.which("node"), "node not installed")
class ToggleRestoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        res = subprocess.run(["node", "--input-type=module", "-e", SCRIPT, TOGGLE.as_uri()],
                             capture_output=True, text=True, check=True)
        cls.out = json.loads(res.stdout)

    def test_a_good_press_is_restored_once(self):
        self.assertEqual(self.out["ok"], {"opened": True, "result": "restored", "state": "expanded", "restores": 1})

    def test_a_failed_press_is_never_undone(self):
        # the old flag-before-press code pressed again here and collapsed the sidebar
        r = self.out["pressFailed"]
        self.assertFalse(r["opened"])
        self.assertEqual((r["result"], r["state"], r["restores"]), ("already as before", "expanded", 0))

    def test_a_press_that_threw_after_landing_is_undone(self):
        r = self.out["pressThrewAfterLanding"]
        self.assertFalse(r["opened"])
        self.assertEqual((r["result"], r["state"], r["restores"]), ("restored", "expanded", 1))

    def test_a_press_that_changed_nothing_is_not_measured_or_undone(self):
        r = self.out["pressNoChange"]
        self.assertFalse(r["opened"])
        self.assertEqual((r["state"], r["restores"]), ("expanded", 0))

    def test_a_stale_restore_that_landed_is_not_pressed_twice(self):
        r = self.out["staleRestoreLanded"]
        self.assertEqual((r["result"], r["state"], r["restores"]), ("restored", "expanded", 1))

    def test_without_state_the_flag_is_set_only_after_the_press(self):
        self.assertEqual(self.out["flagOnlyFailed"]["result"], "nothing pressed")
        self.assertEqual(self.out["flagOnlyFailed"]["restores"], 0)
        self.assertEqual(self.out["flagOnlyOk"]["result"], "pressed back")


class ToggleSpecsTest(unittest.TestCase):
    def test_toggles_with_a_restore_let_a_failed_press_throw(self):
        src = MEASURE.read_text()
        # every state with a restore: its press is not wrapped in .catch, and
        # the ones whose control has a readable state carry stateOf
        states = dict(re.findall(r"\{ name: '([\w-]+)'((?:(?!\{ name:).)*?)restore: async", src, re.S))
        self.assertEqual(len(states), 2)
        self.assertEqual(sorted(n for n, body in states.items() if "stateOf:" in body), ['playing'])
        for body in states.values():
            self.assertNotIn(".catch(() => {})", body)
        self.assertIn("toggle = await toggleBefore(st, readLoc); const alt = await toggleOpen(st, toggle);", src)
        self.assertNotIn("toggled = readLoc", src)


if __name__ == "__main__":
    unittest.main()
