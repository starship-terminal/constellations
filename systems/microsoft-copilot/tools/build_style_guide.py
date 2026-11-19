#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Edit tokens, then rerun. Do not edit the HTML."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


def css_of(value):
    if isinstance(value, dict) and "color" in value and "blur" in value:
        return f"{value['offsetX']} {value['offsetY']} {value['blur']} {value['spread']} {value['color']}"
    if isinstance(value, list):
        return "cubic-bezier(" + ", ".join(str(n) for n in value) + ")"
    return str(value)


rows = []
for theme in ("light", "dark"):
    for name, tok in flat(T[theme]):
        if tok.get("$type") == "color":
            rows.append((theme, name, tok["$value"]))

swatches = "\n".join(
    f'<div class="sw"><i style="background:{v}"></i><div><b>{theme}.{name}</b><span>{v}</span></div></div>'
    for theme, name, v in rows
)

type_rows = []
for name, tok in flat(T["core"]):
    if tok.get("$type") in ("dimension", "fontFamily", "fontWeight", "duration", "cubicBezier", "shadow"):
        type_rows.append(f"<tr><td><code>core.{name}</code></td><td>{tok['$type']}</td><td>{css_of(tok['$value'])}</td></tr>")

html = f"""<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Microsoft Copilot style guide</title>
<style>
:root {{
  --page: {T['dark']['background']['page']['$value']};
  --surface: {T['dark']['background']['surface']['$value']};
  --text: {T['dark']['text']['primary']['$value']};
  --muted: {T['dark']['text']['secondary']['$value']};
  --action: {T['dark']['background']['action']['$value']};
  --on-action: {T['dark']['text']['onAction']['$value']};
  --border: {T['dark']['border']['stroke']['$value']};
  --font: {T['core']['font']['family']['ui']['$value']};
  --display: {T['core']['font']['family']['display']['$value']};
}}
[data-mode="light"] {{
  --page: {T['light']['background']['page']['$value']};
  --surface: {T['light']['background']['surface']['$value']};
  --text: {T['light']['text']['primary']['$value']};
  --muted: {T['light']['text']['secondary']['$value']};
  --action: {T['light']['background']['action']['$value']};
  --on-action: {T['light']['text']['onAction']['$value']};
  --border: {T['light']['border']['strong']['$value']};
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/24px var(--font); }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
header {{ display: flex; justify-content: space-between; align-items: center; gap: 16px; }}
h1 {{ font: 400 40px/48px var(--display); letter-spacing: -0.5px; margin: 0; }}
h2 {{ font: 400 28px/36px var(--font); margin: 40px 0 12px; }}
button.toggle {{ background: var(--action); color: var(--on-action); border: 0; border-radius: 16px; padding: 12px 24px; font: 600 15px/24px var(--font); cursor: pointer; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 12px; }}
.sw {{ display: flex; gap: 10px; align-items: center; }}
.sw i {{ width: 40px; height: 40px; border-radius: 8px; box-shadow: inset 0 0 0 1px var(--border); flex: none; }}
.sw b {{ display: block; font-size: 12px; }}
.sw span {{ color: var(--muted); font-size: 12px; }}
table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
td {{ border-bottom: 1px solid var(--border); padding: 6px 8px; vertical-align: top; }}
.btn {{ display: inline-flex; align-items: center; background: var(--action); color: var(--on-action); border-radius: 16px; padding: 12px 24px; font-weight: 600; text-decoration: none; }}
.tab {{ display: inline-block; border-radius: 200px; padding: 8px 24px; font-weight: 600; font-size: 15px; background: var(--action); color: var(--on-action); }}
.card {{ border: 1px solid var(--border); border-radius: 24px; padding: 16px; max-width: 320px; background: var(--surface); }}
p.note {{ color: var(--muted); max-width: 70ch; }}
</style>
</head>
<body>
<div class="wrap">
<header>
  <h1>Microsoft Copilot</h1>
  <button class="toggle" type="button" onclick="document.documentElement.dataset.mode = document.documentElement.dataset.mode === 'dark' ? 'light' : 'dark'">Toggle theme</button>
</header>
<p class="note">Values are the measured public signed-out page at copilot.com on 2026-11-19. The toggle swaps the semantic set. Segoe Sans and Segoe Serif Display are Microsoft faces; this page falls back when they are not installed.</p>
<h2>Colour</h2>
<div class="swatches">
{swatches}
</div>
<h2>Components</h2>
<p><a class="btn" href="#">Sign in</a></p>
<p><span class="tab">Work</span></p>
<div class="card"><strong>Get started with chat</strong><p class="note">Think through projects, summarize information, and keep work moving.</p></div>
<h2>Scales</h2>
<table>
{''.join(type_rows)}
</table>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
