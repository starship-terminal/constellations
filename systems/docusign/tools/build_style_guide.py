#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only. Values are CSS variables."""
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


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(token):
    v = token["$value"]
    if isinstance(v, list):
        return "cubic-bezier(" + ", ".join(str(x) for x in v) + ")"
    if isinstance(v, dict) and "fontSize" in v:
        return alias(v["fontWeight"]) + " " + alias(v["fontSize"]) + "/" + alias(v["lineHeight"]) + " " + alias(v["fontFamily"])
    return alias(v)


lines = [f"  {cssname(n)}: {css_val(t)};" for n, t in flat({**T["core"], **T["light"]})]
css = "\n".join(lines)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DocuSign style guide</title>
<style>
:root {{
{css}
  --sg-sans: var(--font-family-ui), Helvetica, Arial, sans-serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font: 400 16px/1.5 var(--sg-sans); color: var(--text); background: var(--page); }}
main {{ max-width: 980px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font: var(--typography-display); letter-spacing: -1.5px; margin: 0 0 8px; }}
h2 {{ font: 500 13px/1 var(--sg-sans); letter-spacing: .08em; text-transform: uppercase; color: var(--muted); margin: 40px 0 12px; }}
.note {{ color: var(--muted); max-width: 66ch; }}
.row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 140px; }}
.sw i {{ display: block; height: 56px; border-radius: var(--radius-control); border: 1px solid var(--border); }}
.sw b, .sw span {{ display: block; font: 12px/1.4 ui-monospace, Menlo, monospace; }}
.sw span {{ color: var(--muted); }}
.mock {{ border: 1px solid var(--border); border-radius: 16px; overflow: hidden; }}
.nav {{ display: flex; align-items: center; gap: 16px; padding: 16px 20px; background: var(--page); }}
.nav .sp {{ flex: 1; }}
.btn {{ display: inline-flex; align-items: center; height: var(--size-control); padding: 0 16px; border-radius: var(--radius-control); font: 600 14px/21px var(--sg-sans); letter-spacing: .2px; text-decoration: none; }}
.btn.primary {{ background: var(--accent); color: var(--onAccent); }}
.btn.ghost {{ color: var(--accent); background: transparent; }}
.hero {{ background: #26065d; color: #fff; padding: 48px 32px; }}
.hero h3 {{ margin: 0; font: var(--typography-heading); color: #fff; letter-spacing: -1.25px; }}
.hero p {{ color: rgba(255,255,255,.8); max-width: 46ch; }}
.band {{ background: var(--surface); padding: 24px; }}
.field {{ display: flex; max-width: 420px; }}
.field input {{ flex: 1; height: var(--size-field); border: 1px solid var(--border); border-radius: 8px 0 0 8px; padding: 0 12px; font: 16px var(--sg-sans); }}
.field button {{ height: var(--size-field); border: 0; border-radius: 0 8px 8px 0; background: var(--text); color: var(--onAccent); padding: 0 16px; font: 500 16px var(--sg-sans); }}
</style>
</head>
<body>
<main>
  <h1 style="font: 300 40px/1.1 var(--sg-sans); letter-spacing: -1px; color: var(--text)">DocuSign style guide</h1>
  <p class="note">Generated from tokens.json. Public marketing site, signed out, light only. DS Indigo is not bundled, so this page falls back to Helvetica.</p>
  <h2>Colour</h2>
  <div class="row">
    <div class="sw"><i style="background: var(--page)"></i><b>page</b><span>var(--page)</span></div>
    <div class="sw"><i style="background: var(--surface)"></i><b>surface</b><span>var(--surface)</span></div>
    <div class="sw"><i style="background: var(--text)"></i><b>text</b><span>var(--text)</span></div>
    <div class="sw"><i style="background: var(--muted)"></i><b>muted</b><span>var(--muted)</span></div>
    <div class="sw"><i style="background: var(--accent)"></i><b>accent</b><span>var(--accent)</span></div>
    <div class="sw"><i style="background: var(--border)"></i><b>border</b><span>var(--border)</span></div>
    <div class="sw"><i style="background: var(--focus)"></i><b>focus</b><span>var(--focus)</span></div>
  </div>
  <h2>Chrome</h2>
  <div class="mock">
    <div class="nav"><b>DocuSign</b><span>Products</span><span>Solutions</span><span class="sp"></span><a class="btn ghost">Contact sales</a><a class="btn primary">Try for free</a></div>
    <div class="hero"><h3>Everything you need to agree</h3><p>Send, sign and manage agreements. Display type is light weight at a large size.</p><a class="btn primary">Try for free</a></div>
    <div class="band">
      <p>Work email field, measured at 61px with an 8px radius on the left.</p>
      <div class="field"><input placeholder="Work email" readonly><button type="button">Get started</button></div>
    </div>
  </div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
