#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
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


def css_block(group):
    lines = []
    for name, tok in flat(T[group]):
        val = tok["$value"]
        if isinstance(val, (dict, list)):
            continue
        lines.append(f"  {cssname(name)}: {alias(val)};")
    return "\n".join(lines)


html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SavvyCal style guide</title>
<style>
:root {{
{css_block("core")}
{css_block("light")}
  --sg-sans: InterVariable, Inter, system-ui, sans-serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font: 400 16px/1.5 var(--sg-sans); color: var(--text); background: var(--page); }}
main {{ max-width: 980px; margin: 0 auto; padding: 40px 24px 80px; }}
h1 {{ font: 700 48px/0.95 GT-Alpina-Condensed, Georgia, serif; margin: 0 0 8px; }}
h2 {{ font: 500 13px/1 var(--sg-sans); letter-spacing: .08em; text-transform: uppercase; color: var(--muted); margin: 40px 0 12px; }}
.swatches {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 140px; }}
.sw i {{ display: block; height: 64px; border-radius: 12px; border: 1px solid rgba(12,12,9,.12); }}
.sw b {{ display: block; font-size: 12px; margin-top: 6px; }}
.row {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; margin: 12px 0; }}
.cta {{ display: inline-flex; align-items: center; height: var(--component-button-height); padding: 0 20px; border-radius: var(--radius-pill); background: var(--component-button-bg); color: var(--component-button-text); font-weight: 500; text-decoration: none; }}
.quiet {{ display: inline-flex; align-items: center; height: 46px; padding: 0 20px; border-radius: var(--radius-pill); color: var(--text); text-decoration: none; }}
.field {{ height: var(--component-field-height); width: 280px; border-radius: var(--component-field-radius); border: 1px solid rgba(12,12,9,.2); padding: 0 12px; background: var(--component-field-bg); }}
.card {{ background: var(--surface); border-radius: 16px; padding: 20px; max-width: 360px; }}
</style>
</head>
<body>
<main>
<h1>SavvyCal</h1>
<p>Public marketing surface, light only. Values come from tokens.json.</p>
<h2>Colour</h2>
<div class="swatches">
<div class="sw"><i style="background:var(--page)"></i><b>page</b></div>
<div class="sw"><i style="background:var(--surface)"></i><b>surface</b></div>
<div class="sw"><i style="background:var(--text)"></i><b>text</b></div>
<div class="sw"><i style="background:var(--muted)"></i><b>muted</b></div>
<div class="sw"><i style="background:var(--accent)"></i><b>accent</b></div>
<div class="sw"><i style="background:var(--neon)"></i><b>neon</b></div>
</div>
<h2>Components</h2>
<div class="row">
<a class="cta" href="#">Try SavvyCal risk-free</a>
<a class="quiet" href="#">See plans and pricing</a>
</div>
<div class="card">
<p style="margin:0 0 8px;font-weight:500">Design sync</p>
<p style="margin:0;color:var(--muted)">A sand card on the oatmeal page.</p>
</div>
<div class="row">
<input class="field" placeholder="Search integrations" aria-label="Search">
</div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html")
