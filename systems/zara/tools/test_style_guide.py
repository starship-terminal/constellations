"""style-guide.html's type specimens carry every typography value, quoted font stacks included.

Runs the committed page's script under Node with a minimal DOM stub and reads back the style of
each specimen. Skipped when Node is not installed.
"""
import json
import pathlib
import re
import shutil
import subprocess
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())

STUB = r"""
const fs = require("fs");
const html = fs.readFileSync(process.argv[1], "utf8");
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((m) => m[1]);
const byId = {};
function mk(tag) {
  return { tag, style: {}, children: [], textContent: "", className: "", attrs: {},
    append(...c) { this.children.push(...c); }, appendChild(c) { this.children.push(c); return c; },
    replaceChildren(...c) { this.children = [...c]; }, setAttribute(k, v) { this.attrs[k] = v; },
    getAttribute(k) { return this.attrs[k]; }, addEventListener() {}, classList: { add() {}, remove() {}, toggle() {} } };
}
global.document = { documentElement: mk("html"), createElement: mk,
  getElementById: (id) => (byId[id] = byId[id] || mk(id)),
  querySelector: (s) => (byId[s] = byId[s] || mk(s)), querySelectorAll: () => [] };
global.window = global;
global.localStorage = { getItem: () => null, setItem() {} };
global.matchMedia = () => ({ matches: false, addEventListener() {} });
for (const s of scripts) eval(s);
const out = (byId.type ? byId.type.children : []).map((p) => ({ text: p.textContent, style: p.style }));
process.stdout.write(JSON.stringify(out));
"""


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class TypeSpecimens(unittest.TestCase):
    def test_each_specimen_has_its_token_styles(self):
        run = subprocess.run(["node", "-e", STUB, str(HERE / "style-guide.html")],
                             capture_output=True, text=True, check=True)
        specimens = json.loads(run.stdout)
        typography = {k: v for k, v in TOKENS["core"]["typography"].items() if not k.startswith("$")}
        self.assertEqual(len(specimens), len(typography))
        quoted = [k for k, t in typography.items() if '"' in t["$value"]["fontFamily"]]
        self.assertTrue(quoted, "the fixture needs at least one quoted font stack")
        for (name, token), spec in zip(typography.items(), specimens):
            v = token["$value"]
            with self.subTest(token=name):
                self.assertTrue(spec["text"].startswith(name), spec["text"])
                for prop in ("fontFamily", "fontSize", "fontWeight", "lineHeight", "letterSpacing"):
                    self.assertEqual(spec["style"].get(prop), v[prop], prop)

    def test_no_style_attribute_is_built_from_a_string(self):
        # The template, not the built page: token sources inlined into the page may hold any text.
        page = (HERE / "tools" / "style-guide.template.html").read_text()
        script = "".join(re.findall(r"<script>([\s\S]*?)</script>", page))
        script = re.sub(r"^\s*//.*$", "", script, flags=re.M)   # comments may name what they avoid
        self.assertNotIn("innerHTML", script)
        self.assertNotIn('style="', script)


if __name__ == "__main__":
    unittest.main()
