"""The style guide's script handles a colour token that sits straight under core.color."""
import json
import pathlib
import shutil
import subprocess
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


class StyleGuide(unittest.TestCase):
    def test_flat_recurses_into_objects_only(self):
        # Without the guard, core.color.white recursed through its value string until a RangeError,
        # which stopped the palette and left space, radius and layout empty.
        tpl = (PKG / "tools" / "style-guide.template.html").read_text()
        self.assertIn('typeof v === "object" ? flat(v', tpl)

    def test_single_colours_exist_to_be_drawn(self):
        color = json.loads((PKG / "tokens.json").read_text())["core"]["color"]
        singles = [k for k, v in color.items() if isinstance(v, dict) and "$value" in v]
        self.assertTrue(singles)  # white, error, success, action
        self.assertIn('node && node.t ? [["", node]]', (PKG / "tools" / "style-guide.template.html").read_text())


RUN = r"""
const vm = require('vm'), fs = require('fs');
const html = fs.readFileSync(process.argv[1], 'utf8');
const script = html.slice(html.lastIndexOf('<script>') + 8, html.lastIndexOf('</script>'));
function el() {
  return {
    html: '', children: [], className: '', row: null,
    set innerHTML(v) { this.html = v; this.row = el(); },
    get innerHTML() { return this.html; },
    insertAdjacentHTML(_, h) { this.html += h; },
    appendChild(c) { this.children.push(c); },
    querySelector() { return this.row; },
  };
}
const ids = { palette: el(), space: el(), radius: el(), layout: el() };
const document = { getElementById: (id) => ids[id], querySelector: (s) => ids[s.slice(1)], createElement: () => el() };
vm.runInNewContext(script, { document });
const count = (h) => (h.match(/<div class="sw"/g) || []).length;
console.log(JSON.stringify({
  ramps: Object.fromEntries(ids.palette.children.map((c) => [c.html.match(/<h3>(.*?)<\/h3>/)[1], count(c.row.html)])),
  space: (ids.space.html.match(/<div /g) || []).length,
  radius: (ids.radius.html.match(/<div /g) || []).length,
  layout: (ids.layout.html.match(/<tr /g) || []).length,
}));
"""


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class RenderedGuide(unittest.TestCase):
    """Runs the committed guide's script against a stub DOM, so a regression in the drawing loop fails
    here rather than only in a browser."""

    def test_single_colours_and_every_section_draw(self):
        out = subprocess.run(["node", "-e", RUN, str(PKG / "style-guide.html")], capture_output=True, text=True, check=True)
        got = json.loads(out.stdout)
        color = json.loads((PKG / "tokens.json").read_text())["core"]["color"]
        for name, tok in color.items():
            if isinstance(tok, dict) and "$value" in tok:
                self.assertEqual(got["ramps"].get(name), 1, name)  # a single colour draws one swatch
        self.assertGreater(got["space"], 0)
        self.assertGreater(got["radius"], 0)
        self.assertGreater(got["layout"], 0)


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class CaptureDates(unittest.TestCase):
    def test_measure_merge_dates(self):
        """capture/public/test_dates.mjs: a partial rerun dates only what it read."""
        test = PKG / "tools" / "capture" / "public" / "test_dates.mjs"
        out = subprocess.run(["node", "--test", str(test)], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stdout[-2000:] + out.stderr[-2000:])


if __name__ == "__main__":
    unittest.main()
