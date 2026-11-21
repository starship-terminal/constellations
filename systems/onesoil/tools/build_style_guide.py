#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only.

OneSoil's marketing site has no dark theme, so the guide has no theme toggle.
Colours and sizes are CSS variables generated from tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from flat(value, prefix + key + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path)


def alias(value):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(value))


def css_val(token):
    value = token["$value"]
    if token["$type"] == "typography":
        return None
    if token["$type"] == "cubicBezier":
        return "cubic-bezier(" + ", ".join(str(n) for n in value) + ")"
    if token["$type"] == "shadow":
        return None
    return alias(value)


lines = []
for name, token in flat({**T["core"], **T["light"]}):
    val = css_val(token)
    if val:
        lines.append(f"  {cssname(name)}: {val};")

css = "\n".join(lines)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>OneSoil style guide</title>
<style>
:root {{
{css}
  color-scheme: light;
  --sg-sans: var(--font-family-geologica);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--color-page); color: var(--color-ink); font: 400 16px/24px var(--sg-sans); }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 64px; }}
h1 {{ font-weight: 400; font-size: 48px; line-height: 1.05; letter-spacing: -0.04em; margin: 0 0 8px; }}
h1 span {{ color: var(--color-accent-text); }}
h2 {{ font-weight: 400; font-size: 28px; margin: 40px 0 12px; }}
p {{ max-width: 68ch; }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
.swatch {{ width: 72px; height: 48px; border-radius: 12px; border: 1px solid rgba(21,21,21,0.12); }}
.btn {{ display: inline-flex; align-items: center; height: var(--size-button); padding: 12px 16px; border-radius: var(--radius-pill); color: var(--color-white); text-decoration: none; background: var(--action-primary); }}
.btn.accent {{ background: var(--action-accent); }}
.field {{ display: block; width: 320px; height: var(--size-field); padding: 12px; border-radius: var(--radius-field); border: 2px solid transparent; background: var(--color-field); color: var(--color-ink); font: inherit; }}
.chip {{ display: inline-flex; align-items: center; height: var(--size-chip); padding: 8px 16px; border-radius: var(--radius-pill); border: 1px solid var(--color-hairline); background: var(--color-white); }}
.chip.on {{ background: var(--color-chip-selected); }}
.card {{ width: 180px; height: 120px; border-radius: var(--radius-card); background: var(--color-menu-card); display: flex; align-items: flex-end; padding: 16px; }}
</style>
</head>
<body>
<div class="wrap">
<h1>Economic efficiency for agrifood, <span>made easy</span></h1>
<p>Rendered from tokens.json. Light only. OneSoil's public site does not ship a dark theme.</p>
<h2>Colour</h2>
<div class="row">
<div class="swatch" style="background:var(--color-page)"></div>
<div class="swatch" style="background:var(--color-ink)"></div>
<div class="swatch" style="background:var(--color-accent)"></div>
<div class="swatch" style="background:var(--color-accent-text)"></div>
<div class="swatch" style="background:var(--color-muted)"></div>
<div class="swatch" style="background:var(--color-focus)"></div>
</div>
<h2>Buttons</h2>
<div class="row">
<a class="btn" href="#buttons">Schedule a demo</a>
<a class="btn accent" href="#buttons">Try Free</a>
<span class="chip">Agronomist</span>
<span class="chip on">Agronomist</span>
</div>
<h2>Field</h2>
<input class="field" placeholder="Your full name" readonly>
<div class="card">OneSoil Platform</div>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
