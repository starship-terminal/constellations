"""pressOn() forces :active:hover on the measured element itself: the node id
DOM.requestNode returns for that element reaches CSS.forcePseudoState, and
the temporary marker is removed. Runs the function from measure.mjs in Node
against a fake page, element and CDP session; skipped without Node.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import re
import shutil
import subprocess
import unittest

SRC = (pathlib.Path(__file__).resolve().parent / "capture" / "public" / "measure.mjs").read_text()
FN = re.search(r"async function pressOn\(loc\) \{.*?\n\}\n", SRC, re.S).group(0)

HARNESS = """
const calls = [];
const el = { attrs: {}, setAttribute(k, v) { this.attrs[k] = v; }, removeAttribute(k) { delete this.attrs[k]; } };
const child = { attrs: {} };
const loc = { evaluate: async (fn) => fn(el) };
const page = { waitForTimeout: async () => {} };
const cdp = { send: async (method, params) => {
  calls.push([method, params]);
  if (method === 'Runtime.evaluate') return { result: { objectId: el.attrs['data-press-target'] ? 'obj-el' : 'obj-none' } };
  if (method === 'DOM.requestNode') return { nodeId: params.objectId === 'obj-el' ? 42 : 7 };
  if (method === 'DOM.getNodeForLocation') return { backendNodeId: 99 };
  if (method === 'DOM.pushNodesByBackendIdsToFrontend') return { nodeIds: [7] };
  return {};
} };
%s
pressOn(loc).then((id) => console.log(JSON.stringify({ id, calls, attrs: el.attrs })));
"""


@unittest.skipUnless(shutil.which("node"), "node not installed")
class PressOnTest(unittest.TestCase):
    def test_forces_the_measured_element(self):
        out = json.loads(subprocess.run(["node", "-e", HARNESS % FN], capture_output=True, text=True, check=True).stdout)
        forced = [p for m, p in out["calls"] if m == "CSS.forcePseudoState"]
        self.assertEqual(forced, [{"nodeId": 42, "forcedPseudoClasses": ["active", "hover"]}])
        self.assertEqual(out["id"], 42)
        self.assertNotIn("DOM.getNodeForLocation", [m for m, _ in out["calls"]])
        self.assertEqual(out["attrs"], {})  # the marker is removed again

    def test_unresolved_target_throws(self):
        js = (HARNESS % FN).replace("return { result: { objectId: el.attrs['data-press-target'] ? 'obj-el' : 'obj-none' } };", "return { result: {} };")
        js = js.replace("pressOn(loc).then((id) => console.log(JSON.stringify({ id, calls, attrs: el.attrs })));",
                        "pressOn(loc).then(() => console.log(JSON.stringify({ threw: false, attrs: el.attrs })), (e) => console.log(JSON.stringify({ threw: true, forced: calls.some(([m]) => m === 'CSS.forcePseudoState'), attrs: el.attrs })));")
        out = json.loads(subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True).stdout)
        self.assertTrue(out["threw"])
        self.assertFalse(out["forced"])
        self.assertEqual(out["attrs"], {})


if __name__ == "__main__":
    unittest.main()
