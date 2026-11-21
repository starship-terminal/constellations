#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Self-contained. No network fonts."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + "-")


def css_name(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path)


def css_val(token):
    v = token["$value"]
    if isinstance(v, list) and token["$type"] == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if isinstance(v, dict):
        return None
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({css_name(m.group(1))})", str(v))


def block(tree):
    lines = []
    for name, token in flat(tree):
        val = css_val(token)
        if val:
            lines.append("  %s: %s;" % (css_name(name), val))
    return "\n".join(lines)


def swatches(theme):
    colors = []
    node = T.get(theme, {}).get("color", {})

    def walk(n, prefix):
        for k, v in n.items():
            if k.startswith("$"):
                continue
            if isinstance(v, dict) and v.get("$type") == "color":
                colors.append((prefix + k, v["$value"]))
            elif isinstance(v, dict):
                walk(v, prefix + k + ".")
    walk(node, "")
    bits = []
    for name, value in colors:
        bits.append('<div class="sw"><i style="background:%s"></i><div><b>%s</b><span>%s</span></div></div>' % (value, name, value))
    return "\n".join(bits)


html = """<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Reown style guide</title>
<style>
:root {
%s
%s
  color-scheme: light;
  --page: var(--color-surface, #9a9a9a);
  --ink: var(--color-on-surface, #6c6c6c);
  --sans: var(--font-family-sans), ui-sans-serif, system-ui, sans-serif;
  --mono: var(--font-family-mono), ui-monospace, monospace;
}
[data-mode="dark"] {
%s
  color-scheme: dark;
  --page: var(--color-docs-background, #202020);
  --ink: #fff;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--page); color: var(--ink); font: 400 16px/1.5 var(--sans); }
header { display: flex; gap: 16px; align-items: center; padding: 16px 24px; position: sticky; top: 0; background: var(--page); }
h1 { font-size: 20px; font-weight: 400; margin: 0; }
button.theme { margin-left: auto; font: 400 14px/1 var(--mono); border-radius: 14px; border: 1px solid currentColor; background: transparent; color: inherit; padding: 10px 14px; }
main { max-width: 1100px; margin: 0 auto; padding: 8px 24px 64px; }
section { margin-top: 40px; }
h2 { font-size: 28px; font-weight: 400; letter-spacing: -0.02em; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
.sw { display: flex; gap: 10px; align-items: center; }
.sw i { width: 40px; height: 40px; border-radius: 12px; display: block; box-shadow: inset 0 0 0 1px rgba(0,0,0,.15); }
.sw b { display: block; font: 500 12px/1.3 var(--mono); }
.sw span { font-size: 12px; opacity: .7; }
.row { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin: 12px 0; }
.btn { display: inline-flex; align-items: center; height: 48px; padding: 0 18px; border-radius: 14px; font: 400 16px/1 var(--mono); letter-spacing: -0.05rem; text-decoration: none; }
.btn-blue { background: #379def; color: #202020; }
.btn-white { background: #fff; color: #202020; }
.btn-outline { background: transparent; color: #fff; box-shadow: inset 0 0 0 1px #fff; }
.card { background: #bbb; color: #202020; border-radius: 40px; padding: 24px; max-width: 420px; }
.field { background: #363636; color: #e9e9e9; border: 0; border-radius: 32px; padding: 16px 20px; font: 16px/1 var(--mono); width: 280px; }
.note { max-width: 70ch; opacity: .85; }
code { font-family: var(--mono); font-size: 13px; }
</style>
</head>
<body>
<header>
  <h1>Reown</h1>
  <span>public marketing, docs, demo</span>
  <button class="theme" type="button" id="theme">Docs dark</button>
</header>
<main>
<section>
  <h2>Marketing colours</h2>
  <p class="note">Resolved on reown.com. The page surface is grey-3 (#9a9a9a). Section classes override these locally. The toggle switches the docs dark set, which the marketing site does not use.</p>
  <div class="grid">%s</div>
</section>
<section>
  <h2>Buttons</h2>
  <div class="row">
    <a class="btn btn-blue">Learn</a>
    <a class="btn btn-white">Log in</a>
    <a class="btn btn-outline">Explore Plans</a>
  </div>
  <p class="note">Solid blue and white buttons are 48px tall, 14px radius, KH Teka Mono. Outline buttons are 44px, 16px radius.</p>
</section>
<section>
  <h2>Type</h2>
  <p style="font-size:2.25rem;line-height:1.1;letter-spacing:-0.02em;margin:0">Infrastructure for blockchain app development</p>
  <p class="note">H1 is 2.25rem, weight 400, KH Teka. Docs headings are Inter at 36px / 600.</p>
</section>
<section>
  <h2>Field</h2>
  <input class="field" placeholder="Mail" readonly>
  <p class="note">Footer newsletter field. Not submitted in the capture.</p>
</section>
<section>
  <h2>Docs colours</h2>
  <p class="note">Mintlify. Primary is #008847 in both themes. Background light #ffffff, dark #202020.</p>
  <div class="grid">%s</div>
</section>
</main>
<script>
const btn = document.getElementById('theme');
btn.addEventListener('click', () => {
  const dark = document.documentElement.getAttribute('data-mode') === 'dark';
  document.documentElement.setAttribute('data-mode', dark ? 'light' : 'dark');
  btn.textContent = dark ? 'Docs dark' : 'Marketing light';
});
</script>
</body>
</html>
""" % (block(T["core"]), block(T["light"]), block(T["dark"]), swatches("light"), swatches("dark"))

(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
