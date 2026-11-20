#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light is the live marketing theme.
The dark set is the declared [data-theme=dark] body block."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def val(token):
    return token["$value"]


def css_color(v):
    return v


light = T["light"]
dark = T["dark"]
core = T["core"]

def swatches(group, prefix):
    rows = []
    for name, token in group.items():
        if not isinstance(token, dict) or token.get("$type") != "color":
            continue
        rows.append(
            f'<div class="sw"><i style="background:{css_color(token["$value"])}"></i>'
            f'<div><div class="nm">{prefix}.{name}</div><div class="vl">{token["$value"]}</div></div></div>'
        )
    return "\n".join(rows)

html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Scale style guide</title>
<style>
:root {{
  --page: {val(light['page'])};
  --text: {val(light['text'])};
  --muted: {val(light['muted'])};
  --surface: {val(light['surface'])};
  --border: {val(light['border'])};
  --accent: {val(light['accent'])};
  --on-accent: {val(light['onAccent'])};
  --sans: ui-sans-serif, system-ui, sans-serif;
  --mono: ui-monospace, SFMono-Regular, Menlo, monospace;
}}
[data-mode="dark"] {{
  --page: {val(dark['page'])};
  --text: {val(dark['text'])};
  --muted: {val(dark['mutedText'])};
  --surface: {val(dark['card'])};
  --border: {val(dark['border'])};
  --accent: {val(dark['primary'])};
  --on-accent: {val(dark['primaryText'])};
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/24px var(--sans); }}
header {{ display: flex; gap: 16px; align-items: center; padding: 16px 24px; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: var(--page); }}
header h1 {{ font-size: 18px; font-weight: 500; margin: 0; }}
button.switch {{ margin-left: auto; background: var(--surface); color: var(--text); border: 1px solid var(--border); border-radius: 8px; padding: 8px 12px; }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h2 {{ font-size: 28px; font-weight: 400; letter-spacing: -0.4px; margin: 40px 0 8px; }}
p {{ color: var(--muted); max-width: 70ch; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 12px; }}
.sw {{ display: grid; grid-template-columns: 40px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 40px; height: 40px; border-radius: 8px; box-shadow: inset 0 0 0 1px var(--border); display: block; }}
.nm {{ font: 600 12px/1.3 var(--mono); }}
.vl {{ font-size: 12px; color: var(--muted); }}
.btn {{ display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border-radius: 8px; background: #000; color: #fff; text-decoration: none; }}
[data-mode="dark"] .btn {{ background: #fff; color: #000; }}
.field {{ height: 40px; border-radius: 8px; border: 1px solid var(--border); background: #fff; color: #171717; padding: 0 12px; width: 240px; }}
.note {{ font-size: 13px; }}
</style>
</head>
<body>
<header>
  <h1>Scale</h1>
  <span>Public marketing tokens, 2026-11-21</span>
  <button class="switch" type="button" onclick="document.documentElement.dataset.mode = document.documentElement.dataset.mode === 'dark' ? 'light' : 'dark'">Toggle declared dark</button>
</header>
<main>
  <p class="note">Light values are computed on scale.com. Dark colour roles are the declared <code>[data-theme="dark"] body</code> custom properties, not a live marketing paint. Aeonik is not loaded; the guide uses the system sans.</p>
  <h2>Light roles</h2>
  <div class="grid">{swatches(light, 'light')}</div>
  <h2>Declared dark roles</h2>
  <div class="grid">{swatches(dark, 'dark')}</div>
  <h2>Controls</h2>
  <p><a class="btn" href="#components">Get Started</a></p>
  <p><input class="field" placeholder="First name" aria-label="Specimen field"></p>
  <h2>Type</h2>
  <p style="font-size:40px;line-height:50px;letter-spacing:-0.4px;color:var(--text)">Let's Scale Together</p>
  <p style="font-size:16px;line-height:24px;color:var(--text)">Body is 16px / 24px, weight 400, family Aeonik on the product.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
