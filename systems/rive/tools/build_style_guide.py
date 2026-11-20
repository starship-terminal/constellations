#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. One dark theme. Deterministic."""
import html
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}{k}" if not prefix else f"{prefix}.{k}"
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from walk(v, path)


def css_escape(v):
    return html.escape(str(v), quote=True)


rows = []
for path, tok in list(walk(T["core"])) + list(walk(T["dark"])):
    val = tok["$value"]
    ty = tok.get("$type", "")
    src = tok.get("$extensions", {}).get("source", "")
    swatch = ""
    if ty == "color" and isinstance(val, str) and val.startswith(("#", "rgb")):
        swatch = f'<i style="background:{css_escape(val)}"></i>'
    rows.append(
        f'<tr><td>{swatch}</td><td><code>{html.escape(path)}</code></td>'
        f'<td>{html.escape(str(val))}</td><td>{html.escape(ty or "n/a")}</td>'
        f'<td>{html.escape(src)}</td></tr>'
    )

page = """<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rive style guide</title>
<style>
:root {
  --page: #000000;
  --text: #ffffff;
  --muted: rgba(255,255,255,0.85);
  --surface: #1d1d1d;
  --accent: #ffffff;
  --on-accent: #000000;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--page); color: var(--text); font: 400 15px/1.5 Inter, ui-sans-serif, system-ui, sans-serif; }
main { max-width: 1100px; margin: 0 auto; padding: 32px 24px 80px; }
h1 { font-family: Orbitron, Inter, sans-serif; font-weight: 900; font-size: 32px; letter-spacing: -0.03em; margin: 0 0 8px; }
h2 { font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #aaaaaa; margin: 40px 0 12px; }
p { max-width: 68ch; color: var(--muted); }
.bar { display: flex; align-items: center; gap: 18px; height: 63px; }
.bar span { font-size: 12px; font-weight: 500; letter-spacing: 0.08em; color: rgba(255,255,255,0.85); }
.cta { display: inline-flex; align-items: center; height: 27px; padding: 5px 9px 6px; border-radius: 4px; background: #fff; color: #000; font: 500 12px/1.3 ui-monospace, monospace; letter-spacing: 0.1em; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1); }
.copy { display: inline-flex; align-items: center; height: 29px; padding: 5px 9px 6px; border-radius: 4px; background: rgba(255,255,255,0.9); color: #000; border: 1px solid #fff; font: 500 12px/1.3 ui-monospace, monospace; letter-spacing: 0.1em; }
.hero { font-family: Orbitron, sans-serif; font-weight: 900; font-size: 48px; line-height: 1.02; letter-spacing: -0.03em; max-width: 16ch; }
table { width: 100%; border-collapse: collapse; font-size: 12px; }
td { border-top: 1px solid #222; padding: 6px 8px; vertical-align: top; }
td i { display: inline-block; width: 18px; height: 18px; border-radius: 4px; border: 1px solid #333; }
code { font-family: ui-monospace, monospace; }
</style>
</head>
<body>
<main>
<h1>Rive</h1>
<p>Public marketing surface of rive.app, one dark theme. Values come from tokens.json. The page ground is black, display type is Orbitron, nav labels are Inter at 12px, and the header action is a white 4px-radius chip.</p>
<h2>Shell</h2>
<div class="bar"><strong>RIVE</strong><span>PRODUCTS</span><span>USE CASES</span><span>RESOURCES</span><span>PRICING</span><span style="margin-left:auto" class="cta">GET STARTED</span></div>
<p class="hero">BUILD GAMES, APPS, AND INTERACTIVE UI</p>
<p><span class="copy">COPY</span></p>
<h2>Tokens</h2>
<table>
<tr><td></td><td>Token</td><td>Value</td><td>Type</td><td>Source</td></tr>
""" + "\n".join(rows) + """
</table>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(page)
print("wrote style-guide.html", len(rows), "tokens")
