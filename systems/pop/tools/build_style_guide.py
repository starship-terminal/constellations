#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Light only. Pop's public site has no dark theme, so the page has no theme
toggle. Every colour and type style is a custom property generated from
tokens.json. Satoshi and Inter are not loaded: specimens fall back to the
system sans.
"""
import json, pathlib, re

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
    if ty == "typography":
        return f'{v["fontWeight"]} {v["fontSize"]}/{v["lineHeight"]} {v["fontFamily"]}, var(--sg-sans)'
    return alias(v)


vars_css = "\n".join(
    f"  {cssname(n)}: {css_val(t)};" for n, t in list(flat(T["core"])) + list(flat(T["light"]))
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pop Site style guide</title>
<meta name="description" content="Pop Site public marketing tokens, rendered from tokens.json. One light theme. Values measured on pop.site on 2026-11-21.">
<style>
:root {{
{vars_css}
  --sg-sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 15px/1.45 var(--sg-sans); }}
.wrap {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font: var(--typography-display); letter-spacing: -3.92px; margin: 0 0 8px; }}
h2 {{ font: 500 21px/1.3 var(--sg-sans); margin: 40px 0 12px; }}
p {{ color: var(--muted); max-width: 68ch; }}
.swatches {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 140px; }}
.sw i {{ display: block; height: 64px; border-radius: 10px; border: 1px solid var(--border); }}
.sw span {{ display: block; font-size: 12px; margin-top: 6px; }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin: 12px 0; }}
.btn {{ display: inline-flex; align-items: center; height: var(--component-button-height); padding: 0 var(--component-button-pad-x); border-radius: var(--component-button-radius); background: linear-gradient(110deg, var(--color-blue-sky), var(--color-blue-500)); color: var(--color-on-accent); font: var(--typography-button); letter-spacing: -0.45px; }}
.suffix {{ display: inline-flex; align-items: center; height: 40px; padding: 0 20px 0 12px; border-radius: 0 9999px 9999px 0; background: var(--surface); color: var(--text); font: var(--typography-button); letter-spacing: -0.45px; }}
.link {{ color: var(--text); font: var(--typography-label); letter-spacing: -0.45px; }}
.cap {{ font: var(--typography-caption); letter-spacing: -0.39px; }}
code {{ font: 12px/1.4 ui-monospace, monospace; }}
</style>
</head>
<body>
<div class="wrap">
<h1>Pop Site</h1>
<p>Public marketing surface, one light theme. Satoshi is not loaded here, so type falls back to the system sans. Take values from tokens.json.</p>
<h2>Colour</h2>
<div class="swatches">
  <div class="sw"><i style="background:var(--page)"></i><span>page</span></div>
  <div class="sw"><i style="background:var(--surface)"></i><span>surface</span></div>
  <div class="sw"><i style="background:var(--text)"></i><span>text</span></div>
  <div class="sw"><i style="background:var(--muted)"></i><span>muted</span></div>
  <div class="sw"><i style="background:var(--accent)"></i><span>accent</span></div>
  <div class="sw"><i style="background:linear-gradient(110deg,var(--color-blue-sky),var(--color-blue-500))"></i><span>claim gradient</span></div>
  <div class="sw"><i style="background:var(--focus)"></i><span>focus</span></div>
</div>
<h2>Type</h2>
<p style="font:var(--typography-display);letter-spacing:-3.92px;color:var(--text)">Free to create and share.</p>
<p style="font:var(--typography-body);letter-spacing:-0.63px">Used by 10K+ people in over 50 countries.</p>
<p class="link">Pricing</p>
<p class="cap">Terms</p>
<h2>Controls</h2>
<div class="row">
  <span class="suffix">.pop.site</span>
  <span class="btn">Claim your site</span>
</div>
<p>The claim button is a gradient from <code>#00a8f5</code> to <code>#3b82f6</code> at 110 degrees, radius 26px, height 40px. The suffix chip is <code>#fafafc</code>.</p>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
