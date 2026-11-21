#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Self-contained. No external fonts."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def hex_of(path):
    node = T
    for part in path.split("."):
        node = node[part]
    return node["$value"]


def swatch(label, path):
    value = hex_of(path)
    return (
        f'<div class="sw"><i style="background:{value}"></i>'
        f'<b>{label}</b><code>{value}</code><small>{path}</small></div>'
    )


rows = []
for theme in ("light", "dark"):
    rows.append(f"<h2>{theme}</h2><div class='row'>")
    for label, path in [
        ("page", f"{theme}.color.page"),
        ("surface", f"{theme}.color.surface"),
        ("raised", f"{theme}.color.raised"),
        ("text", f"{theme}.color.text.primary"),
        ("muted", f"{theme}.color.text.muted"),
        ("accent", f"{theme}.color.accent.default"),
        ("border", f"{theme}.color.border.default"),
        ("danger", f"{theme}.color.status.danger"),
        ("info", f"{theme}.color.status.info"),
    ]:
        rows.append(swatch(label, path))
    rows.append("</div>")

gray = "".join(
    swatch(step, f"core.color.gray.{step}")
    for step in ["00", "25", "50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "1k"]
)
green = "".join(
    swatch(step, f"core.color.green.{step}")
    for step in ["00", "50", "100", "200", "300", "400", "500", "600", "800"]
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Peerlist style guide</title>
<style>
:root {{
  --page: {hex_of("light.color.page")};
  --text: {hex_of("light.color.text.primary")};
  --muted: {hex_of("light.color.text.muted")};
  --accent: {hex_of("light.color.accent.default")};
  --border: {hex_of("light.color.border.default")};
  --ink: {hex_of("light.color.text.primary")};
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/24px Geist, ui-sans-serif, system-ui, sans-serif; }}
main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font-family: Georgia, "Iowan Old Style", serif; font-weight: 400; font-size: 40px; line-height: 1.2; }}
h2 {{ margin-top: 36px; font-size: 14px; letter-spacing: 0; }}
.row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 120px; }}
.sw i {{ display: block; height: 56px; border-radius: 12px; border: 1px solid #e2e8f0; }}
.sw b, .sw code, .sw small {{ display: block; font-size: 12px; }}
.sw code, .sw small {{ color: var(--muted); }}
.btn {{ display: inline-flex; align-items: center; height: 32px; padding: 6px 16px; border-radius: 12px; font-size: 14px; font-weight: 600; border: 1px solid transparent; }}
.btn.accent {{ background: {hex_of("light.color.accent.default")}; color: #fff; border-color: {hex_of("light.color.accent.pressed")}; }}
.btn.ink {{ background: {hex_of("core.color.gray.900")}; color: #fff; border-radius: 16px; height: 40px; padding: 0 24px; }}
.btn.quiet {{ background: #fff; color: {hex_of("light.color.text.primary")}; border-color: {hex_of("light.color.border.default")}; }}
.card {{ border: 1px solid {hex_of("light.color.border.default")}; border-radius: 16px; padding: 16px; max-width: 360px; box-shadow: {hex_of("light.shadow.5") if False else "0 1px 1px -0.5px rgba(0,0,0,.03), 0 3px 3px -1.5px rgba(0,0,0,.03)"}; }}
label {{ display: block; font-size: 14px; font-weight: 600; margin: 12px 0 4px; }}
input {{ width: 100%; height: 32px; border-radius: 8px; border: 1px solid {hex_of("light.color.border.strong")}; padding: 0 8px; font: inherit; }}
p.note {{ color: var(--muted); font-size: 14px; }}
</style>
</head>
<body>
<main>
<h1>Peerlist</h1>
<p class="note">Rendered from tokens.json. Geist and Instrument are not loaded here; the display face falls back to Georgia. Values are the measured ones.</p>
<h2>Controls</h2>
<p>
  <span class="btn accent">Post</span>
  <span class="btn quiet">Log in</span>
  <span class="btn ink">Login</span>
</p>
<div class="card">
  <label>Email</label>
  <input placeholder="" disabled>
  <label>Password</label>
  <input disabled>
</div>
<h2>Gray ramp (light declarations)</h2>
<div class="row">{gray}</div>
<h2>Green ramp</h2>
<div class="row">{green}</div>
{''.join(rows)}
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
