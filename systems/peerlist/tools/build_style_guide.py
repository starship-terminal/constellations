#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Self-contained, no template drift."""
import html as htmllib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def rows(group):
    out = []
    for key, token in group.items():
        if isinstance(token, dict) and "$value" in token:
            out.append((key, token["$value"]))
        elif isinstance(token, dict):
            for child, nested in token.items():
                if isinstance(nested, dict) and "$value" in nested:
                    out.append((f"{key}.{child}", nested["$value"]))
    return out


colors = rows(T["core"]["color"])
type_rows = rows(T["core"]["typography"])
radii = rows(T["core"]["radius"])
space = rows(T["core"]["spacing"])

def cell(value):
    """A token value as table text: a typography composite as its parts, not a Python dict."""
    if isinstance(value, dict):
        value = " / ".join(f"{k} {v}" for k, v in value.items())
    return htmllib.escape(str(value))


def swatch(name, value):
    css = value if value.startswith("rgb") or value.startswith("#") else "#ccc"
    return f'<div class="sw"><i style="background:{css}"></i><div><b>{name}</b><span>{value}</span></div></div>'


page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Peerlist style guide</title>
<style>
  body {{ margin: 0; font: 400 16px/24px Geist, ui-sans-serif, system-ui, sans-serif; color: #0d0d0d; background: #fff; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }}
  h1 {{ font-weight: 400; font-size: 40px; line-height: 48px; margin: 0 0 8px; }}
  h2 {{ font-size: 20px; margin: 32px 0 12px; }}
  p {{ color: #334155; max-width: 68ch; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .sw {{ display: flex; gap: 10px; align-items: center; }}
  .sw i {{ width: 36px; height: 36px; border-radius: 8px; border: 1px solid #e2e8f0; display: block; }}
  .sw b {{ display: block; font-size: 13px; }}
  .sw span {{ font-size: 12px; color: #64748b; }}
  .btn {{ display: inline-flex; align-items: center; height: 32px; padding: 6px 16px; border-radius: 12px; font-weight: 600; font-size: 14px; }}
  .primary {{ background: rgb(0 170 69); color: #fff; border: 1px solid rgb(30 135 75); }}
  .secondary {{ background: #fff; color: rgb(13 13 13); border: 1px solid rgb(226 232 240); }}
  .dark {{ background: rgb(15 23 42); color: #fff; border: 1px solid rgb(13 13 13); height: 40px; border-radius: 16px; padding: 8px 24px; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 14px; }}
  td, th {{ text-align: left; padding: 8px 10px; border-bottom: 1px solid #e2e8f0; }}
  code {{ font-family: ui-monospace, monospace; font-size: 12px; }}
</style>
</head>
<body>
<main>
  <h1>Peerlist</h1>
  <p>Public signed-out surfaces measured on 18 November 2026. The live pages stayed on the light class. Dark gray tokens are declared in the stylesheet and listed in tokens.json, not painted here.</p>
  <h2>Colour</h2>
  <div class="grid">{''.join(swatch(n, v) for n, v in colors)}</div>
  <h2>Buttons</h2>
  <p>
    <span class="btn primary">Create Profile</span>
    <span class="btn secondary">Log in</span>
    <span class="btn dark">Login</span>
  </p>
  <h2>Type</h2>
  <table><tr><th>Role</th><th>Value</th></tr>
  {''.join(f'<tr><td><code>{n}</code></td><td>{cell(v)}</td></tr>' for n, v in type_rows)}
  </table>
  <h2>Radius</h2>
  <table><tr><th>Step</th><th>Value</th></tr>
  {''.join(f'<tr><td><code>{n}</code></td><td>{cell(v)}</td></tr>' for n, v in radii)}
  </table>
  <h2>Spacing</h2>
  <table><tr><th>Step</th><th>Value</th></tr>
  {''.join(f'<tr><td><code>{n}</code></td><td>{cell(v)}</td></tr>' for n, v in space)}
  </table>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(page)
print("wrote style-guide.html")
