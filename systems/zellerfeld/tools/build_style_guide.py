#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

One theme. CSS variables are generated from tokens.json so the page cannot
drift from the file. Proprietary faces (Lateral, Exposure, Phonic) are not
loaded; the guide uses the fallback stacks those tokens already name.
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


def css_name(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path)


def resolve(value, depth=0):
    if isinstance(value, str) and value.startswith("{") and value.endswith("}") and depth < 8:
        path = value[1:-1]
        node = T
        for part in path.split("."):
            node = node.get(part) if isinstance(node, dict) else None
            if node is None:
                return value
        if "$value" in node:
            return resolve(node["$value"], depth + 1)
    if isinstance(value, str):
        return re.sub(r"\{([^{}]+)\}", lambda m: f"var({css_name(m.group(1))})", value)
    return value


def css_val(token):
    value = resolve(token["$value"])
    kind = token.get("$type")
    if kind == "shadow" and isinstance(value, list):
        layers = []
        for layer in value:
            bits = []
            if layer.get("inset"):
                bits.append("inset")
            bits += [layer["offsetX"], layer["offsetY"], layer["blur"], layer["spread"], layer["color"]]
            layers.append(" ".join(bits))
        return ", ".join(layers)
    if kind == "cubicBezier" and isinstance(value, list):
        return "cubic-bezier(" + ", ".join(str(n) for n in value) + ")"
    if kind == "duration" and isinstance(value, dict):
        return f"{value['value']}{value['unit']}"
    if isinstance(value, (int, float)):
        return str(value)
    return str(value)


lines = [":root {"]
for name, token in list(flat(T["core"])) + list(flat(T["light"])):
    lines.append(f"  {css_name(name)}: {css_val(token)};")
lines.append("}")
css = "\n".join(lines)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zellerfeld style guide</title>
<style>
{css}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--background-page); color: var(--text-primary); font: 400 14px/20px var(--font-family-tertiary); }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font-family: var(--font-family-primary); font-weight: 400; font-size: 32px; letter-spacing: -0.03em; }}
h2 {{ font-family: var(--font-family-secondary); font-weight: 400; font-size: 22px; margin: 40px 0 12px; }}
p {{ color: var(--text-muted); max-width: 68ch; }}
.row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 148px; }}
.sw i {{ display: block; height: 64px; border-radius: var(--radius-md); box-shadow: inset 0 0 0 1px #ffffff22; }}
.sw b, .sw span {{ display: block; font-size: 11px; line-height: 1.4; }}
.sw span {{ color: var(--text-muted); }}
button.demo, a.demo {{ font: 500 14px/1 var(--font-family-tertiary); text-transform: uppercase; letter-spacing: -0.01em; border-radius: var(--radius-sm); padding: 10px 14px; }}
button.primary {{ background: var(--accent-default); color: var(--accent-foreground); border: 0; }}
button.quiet {{ background: var(--background-muted); color: var(--text-primary); border: 0; }}
a.demo {{ color: var(--text-accent); text-decoration: none; border: 1px solid var(--border-default); }}
input.demo {{ background: transparent; color: var(--text-primary); border: 1px solid var(--border-input); border-radius: 8px; padding: 8px 12px; font: 500 14px/1 var(--font-family-tertiary); text-transform: uppercase; }}
.card {{ background: var(--background-surface); border-radius: var(--radius-lg); padding: 16px; width: 220px; }}
.focus {{ outline: 2px solid var(--focus-ring); outline-offset: 2px; }}
</style>
</head>
<body>
<div class="wrap">
<h1>Zellerfeld</h1>
<p>Rendered from tokens.json. One theme. Lateral, Exposure and Phonic are not loaded; the stacks fall back to the system faces named in the tokens.</p>
<h2>Colour</h2>
<div class="row">
<div class="sw"><i style="background:var(--background-page)"></i><b>page</b><span>var(--background-page)</span></div>
<div class="sw"><i style="background:var(--background-surface)"></i><b>surface</b><span>var(--background-surface)</span></div>
<div class="sw"><i style="background:var(--background-raised)"></i><b>raised</b><span>var(--background-raised)</span></div>
<div class="sw"><i style="background:var(--accent-default)"></i><b>accent</b><span>var(--accent-default)</span></div>
<div class="sw"><i style="background:var(--text-primary)"></i><b>text</b><span>var(--text-primary)</span></div>
<div class="sw"><i style="background:var(--text-muted)"></i><b>muted</b><span>var(--text-muted)</span></div>
<div class="sw"><i style="background:var(--border-default)"></i><b>border</b><span>var(--border-default)</span></div>
<div class="sw"><i style="background:var(--focus-ring)"></i><b>focus</b><span>var(--focus-ring)</span></div>
<div class="sw"><i style="background:var(--status-success)"></i><b>success</b><span>var(--status-success)</span></div>
<div class="sw"><i style="background:var(--status-danger)"></i><b>danger</b><span>var(--status-danger)</span></div>
</div>
<h2>Type</h2>
<p style="font-family:var(--font-family-primary);font-size:32px;color:var(--text-primary)">Lateral, printed shoes</p>
<p style="font-family:var(--font-family-secondary);font-size:28px;color:var(--text-primary)">Exposure, for display lines</p>
<p style="font-family:var(--font-family-tertiary);font-size:14px;letter-spacing:-0.01em;text-transform:uppercase;color:var(--text-primary)">Phonic, for controls</p>
<h2>Controls</h2>
<div class="row">
<button class="demo primary">Buy now</button>
<button class="demo quiet">Sign in</button>
<a class="demo" href="#components">Create</a>
<input class="demo" placeholder="What are you looking for?" value="">
<button class="demo quiet focus">Focused</button>
</div>
<div class="card" style="margin-top:16px">
<b style="font-family:var(--font-family-tertiary);text-transform:uppercase">PDF Bol Sneaker</b>
<span style="color:var(--text-muted);font-size:12px">PDF Channel</span>
<div style="margin-top:12px;color:var(--text-primary)">$249.00</div>
</div>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
