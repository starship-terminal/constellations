#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Colours, radii, type and the search shadow are CSS custom properties generated
from tokens.json. The captured pages paint light only. There is no dark toggle.
"""
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


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "shadow":
        return f'{v["offsetX"]} {v["offsetY"]} {v["blur"]} {v["spread"]} {alias(v["color"])}'
    if ty == "typography":
        ls = f" {alias(v['letterSpacing'])}" if "letterSpacing" in v else ""
        return f'{alias(v["fontWeight"])} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {alias(v["fontFamily"])}{ls}'
    if ty == "fontWeight":
        return str(v)
    return alias(v)


def block(setname):
    return "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T[setname]))


HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>onefinestay style guide</title>
<style>
:root {
%s
%s
}
body { margin: 0; background: var(--light-surface-page); color: var(--light-text-primary); font: var(--core-typography-body); }
main { max-width: 960px; margin: 0 auto; padding: 48px 24px 80px; }
h1 { font: var(--core-typography-heading); margin: 0 0 8px; }
h2 { font: var(--core-typography-nav); letter-spacing: 0.35px; text-transform: uppercase; color: var(--light-accent); margin: 40px 0 12px; }
p.lede { max-width: 42rem; }
.row { display: flex; flex-wrap: wrap; gap: 12px; }
.swatch { width: 140px; }
.swatch i { display: block; height: 64px; border: 1px solid var(--light-border-field); border-radius: var(--core-radius-xs); }
.swatch span { display: block; font: var(--core-typography-label); margin-top: 6px; }
.spec { font: var(--core-typography-card-title); font-style: italic; }
.btn { display: inline-flex; align-items: center; height: var(--light-component-button-primary-height); padding: 0 16px; border-radius: var(--light-component-button-primary-radius); background: var(--light-component-button-primary-bg); color: var(--light-component-button-primary-text); font-weight: 700; border: 2px solid var(--light-component-button-primary-bg); }
.btn-brand { display: inline-flex; align-items: center; height: var(--light-component-button-brand-height); padding: 0 16px; border-radius: var(--light-component-button-brand-radius); background: var(--light-component-button-brand-bg); color: var(--light-component-button-brand-text); font-weight: 700; border: 0; }
.btn-ghost { display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border-radius: 2px; background: transparent; color: var(--light-text-primary); border: 1px solid var(--light-border-field); font-weight: 700; }
.search { display: flex; align-items: center; gap: 8px; width: 360px; height: 56px; padding: 8px; background: #fff; border-radius: 2px; box-shadow: var(--light-shadow-search); }
.search span { flex: 1; color: var(--light-text-placeholder); font-size: 14px; }
.search b { width: 40px; height: 40px; background: var(--light-component-button-search-bg); }
.field { display: flex; flex-direction: column; gap: 4px; width: 280px; border: 1px solid var(--light-border-field); border-radius: var(--light-component-field-radius); padding: 12px 16px; }
.field small { font: var(--core-typography-label); }
.field em { font-style: normal; color: var(--light-text-placeholder); }
.chip { display: inline-flex; align-items: center; height: 38px; padding: 8px 16px; border-radius: var(--core-radius-chip); border: 1px solid var(--light-border-field); font-size: 14px; }
footer.demo { margin-top: 24px; background: var(--light-surface-footer); color: var(--light-text-on-footer); padding: 64px 48px; }
</style>
</head>
<body>
<main>
<h1>onefinestay</h1>
<p class="lede">Public marketing tokens, measured on 19 November 2026. Headings are Tiempos. UI text is Akkurat. The coral search control is brand 500. The booking control is brand 900. Both fonts are proprietary and are not loaded here, so the page falls through the stack.</p>

<h2>Colour</h2>
<div class="row">
<div class="swatch"><i style="background:var(--light-surface-page)"></i><span>page</span></div>
<div class="swatch"><i style="background:var(--light-text-primary)"></i><span>text</span></div>
<div class="swatch"><i style="background:var(--light-text-muted)"></i><span>muted</span></div>
<div class="swatch"><i style="background:var(--light-accent)"></i><span>accent</span></div>
<div class="swatch"><i style="background:var(--light-brand-900)"></i><span>brand 900</span></div>
<div class="swatch"><i style="background:var(--light-surface-footer)"></i><span>footer</span></div>
<div class="swatch"><i style="background:var(--light-surface-beige)"></i><span>beige</span></div>
<div class="swatch"><i style="background:var(--light-border-field)"></i><span>field border</span></div>
<div class="swatch"><i style="background:var(--light-focus)"></i><span>focus</span></div>
</div>

<h2>Type</h2>
<p style="font:var(--core-typography-display); margin:0">Where good taste travels</p>
<p style="font:var(--core-typography-heading); margin:12px 0 0">Enjoy the finest luxury vacation rentals</p>
<p class="spec">Cadogan Street IV</p>
<p>At onefinestay, every home is carefully chosen for its perspective as much as its address.</p>
<p style="font:var(--core-typography-eyebrow); text-transform:uppercase; color:var(--light-accent)">London vacation rentals you will love</p>

<h2>Controls</h2>
<div class="row" style="align-items:center">
<button class="btn">Submit</button>
<button class="btn-brand">Check Availability</button>
<button class="btn-ghost">View all 26 photos</button>
<span class="chip">Garden</span>
</div>
<div class="search" style="margin-top:16px"><span>Dates</span><b></b></div>
<div class="field" style="margin-top:16px"><small>FIRST NAME*</small><em>First</em></div>
<footer class="demo">Footer sits on neutral 700.</footer>
</main>
</body>
</html>
""" % (block("core"), block("light"))

(HERE / "style-guide.html").write_text(HTML)
print("wrote style-guide.html")
