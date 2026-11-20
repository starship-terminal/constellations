"""sendToTerminal() types into the on-screen terminal, never the off-screen copy Superset keeps.

Runs tools/capture/electron/product.mjs's sendToTerminal against a stub page under Node: two
centre-pane .xterm elements, the first off screen at x=-9999 (as in the saved run) and the second
displayed. Nothing drives the app. Skipped when Node is not installed.
"""
import json
import shutil
import subprocess
import unittest
from pathlib import Path

PRODUCT = Path(__file__).resolve().parent / "capture" / "electron" / "product.mjs"

STUB = r"""
const { sendToTerminal } = await import(process.argv[1]);
const events = [];
let active = null;
function term(name, box) {
  const input = {
    name, async focus() { active = input; },
    async evaluate(fn) { return active === input && box.width > 0 && box.x >= 0 && box.y >= 0; },
  };
  return { name, async boundingBox() { return box; }, async click() { events.push('click ' + name); },
           locator(sel) { if (sel !== '.xterm-helper-textarea') throw new Error(sel); return input; } };
}
const terms = JSON.parse(process.argv[2]).map(([n, b]) => term(n, b));
const page = {
  viewportSize: () => ({ width: 1440, height: 900 }),
  locator(sel) {
    if (!sel.includes('.xterm')) throw new Error('unexpected selector ' + sel);
    return { async count() { return terms.length; }, nth: (i) => terms[i],
             filter() { return this; }, first() { return terms[0]; } };
  },
  keyboard: { async type(t) { events.push('type ' + active.name); }, async press(k) { events.push('press ' + k); } },
  async waitForTimeout() {},
};
try { await sendToTerminal({ page }, 'hello'); } catch (e) { events.push('error ' + e.message); }
process.stdout.write(JSON.stringify(events));
"""


def run(terms):
    out = subprocess.run(["node", "--input-type=module", "-e", STUB, str(PRODUCT), json.dumps(terms)],
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class SendToTerminal(unittest.TestCase):
    def test_types_into_the_displayed_terminal_not_the_off_screen_one(self):
        events = run([["offscreen", {"x": -9999, "y": 0, "width": 800, "height": 600}],
                      ["displayed", {"x": 280, "y": 96, "width": 900, "height": 640}]])
        self.assertEqual(events, ["click displayed", "type displayed", "press Enter"])

    def test_refuses_when_no_terminal_is_on_screen(self):
        events = run([["offscreen", {"x": -9999, "y": 0, "width": 800, "height": 600}]])
        self.assertEqual(len(events), 1)
        self.assertTrue(events[0].startswith("error no terminal on screen"), events)


if __name__ == "__main__":
    unittest.main()
