#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Light page, with a dark-band section.

Matter and Mackinac are proprietary and are not loaded. The guide falls back
to ui-sans-serif and Georgia, and says so.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def val(token):
    return token["$value"]


def swatch(name, token):
    value = val(token)
    return (
        f'<div class="sw"><i style="background:{value}"></i>'
        f'<div><b>{name}</b><code>{value}</code></div></div>'
    )


def group(title, node):
    bits = [f"<h3>{title}</h3>", '<div class="grid">']
    for name, token in node.items():
        if isinstance(token, dict) and "$value" in token and str(token["$value"]).startswith(("#", "rgb")):
            bits.append(swatch(name, token))
    bits.append("</div>")
    return "\n".join(bits)


core = TOKENS["core"]
light = TOKENS["light"]
dark = TOKENS["light"]["band"]  # the hero and footer band, a group of the light set

type_rows = []
for name, token in core["typography"].items():
    v = token["$value"]
    type_rows.append(
        f'<div class="ty"><div class="meta"><b>{name}</b><code>{v["fontSize"]} / {v["lineHeight"]} · {v["fontWeight"]}</code></div>'
        f'<div style="font-size:{v["fontSize"]};line-height:{v["lineHeight"]};font-weight:{v["fontWeight"]};letter-spacing:{v.get("letterSpacing", "0")}">{name}</div></div>'
    )

radius_rows = []
for name, token in core["radius"].items():
    radius_rows.append(
        f'<div class="rad" style="border-radius:{val(token)}"><b>{name}</b><code>{val(token)}</code></div>'
    )

space_rows = []
for name, token in core["spacing"].items():
    space_rows.append(
        f'<div class="sp"><i style="width:{val(token)}"></i><span>{name} {val(token)}</span></div>'
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ShareWillow style guide</title>
<style>
  :root {{
    --page: {val(light["bg"]["page"])};
    --surface: {val(light["bg"]["surface"])};
    --ink: {val(light["text"]["primary"])};
    --muted: {val(light["text"]["muted"])};
    --accent: {val(light["accent"]["default"])};
    --border: {val(light["border"]["strong"])};
    --sans: ui-sans-serif, system-ui, -apple-system, sans-serif;
    --display: Georgia, "Iowan Old Style", serif;
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--ink); font: 400 16px/24px var(--sans); }}
  main {{ max-width: 960px; margin: 0 auto; padding: 48px 24px 80px; }}
  h1 {{ font-family: var(--display); font-weight: 500; font-size: 48px; line-height: 1; letter-spacing: -0.03em; margin: 0 0 8px; }}
  h2 {{ font-family: var(--display); font-weight: 500; font-size: 32px; line-height: 1.05; letter-spacing: -0.025em; margin: 40px 0 12px; }}
  h3 {{ font-size: 14px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); margin: 24px 0 8px; }}
  p {{ max-width: 68ch; color: var(--muted); }}
  code {{ font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 12px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 8px; }}
  .sw {{ display: flex; gap: 10px; align-items: center; background: var(--surface); border-radius: 16px; padding: 8px; }}
  .sw i {{ width: 36px; height: 36px; border-radius: 10px; display: block; box-shadow: inset 0 0 0 1px rgba(24,6,0,.12); }}
  .sw b {{ display: block; font-size: 13px; }}
  .ty {{ display: grid; grid-template-columns: 220px 1fr; gap: 16px; padding: 12px 0; border-bottom: 1px solid rgba(24,6,0,.08); align-items: baseline; }}
  .meta code {{ display: block; color: var(--muted); }}
  .rad {{ display: inline-flex; flex-direction: column; gap: 4px; margin: 0 12px 12px 0; padding: 16px; background: var(--surface); border: 1px solid rgba(24,6,0,.16); min-width: 96px; }}
  .sp {{ display: flex; align-items: center; gap: 12px; margin: 4px 0; }}
  .sp i {{ height: 12px; background: #180600; display: block; }}
  .btn {{ display: inline-flex; align-items: center; height: 36px; padding: 0 16px; border-radius: 9999px; background: #180600; color: #fff; font-size: 13px; font-weight: 500; text-decoration: none; }}
  .btn.lemon {{ background: #faf082; color: #180600; height: 48px; padding: 0 20px; font-size: 14px; }}
  .band {{ background: #0d0a07; color: #f5f2e0; border-radius: 24px; padding: 32px; margin-top: 16px; }}
  .band h2 {{ color: #f5f2e0; margin-top: 0; }}
  .note {{ font-size: 13px; }}
</style>
</head>
<body>
<main>
  <h1>ShareWillow</h1>
  <p>Measured from www.sharewillow.com and the signed-out login at app.sharewillow.com/login on 2026-11-19. Matter and Mackinac are not loaded here. This page uses system faces.</p>
  <p class="note">The marketing site is light only. The dark band below is the hero and footer palette, not a theme switch.</p>

  <h2>Colour</h2>
  {group("Page", light["bg"])}
  {group("Text", light["text"])}
  {group("Accent", light["accent"])}
  {group("Border", light["border"])}
  {group("Palette", core["palette"])}
  {group("App login", light["app"])}

  <h2>Type</h2>
  {"".join(type_rows)}

  <h2>Radius</h2>
  {"".join(radius_rows)}

  <h2>Spacing</h2>
  {"".join(space_rows)}

  <h2>Controls</h2>
  <p><a class="btn" href="#controls">Book a demo</a> <a class="btn lemon" href="#controls">Book a demo</a></p>
  <p class="note">Header pill is 36px, radius 9999px, face #180600, label #ffffff. Lemon pill is 48px, face #faf082, label #180600.</p>

  <div class="band">
    <h2>Hero and footer</h2>
    <p>Page {val(dark["bg"]["page"])}. Ink {val(dark["text"]["primary"])}. Surface {val(dark["bg"]["surface"])}.</p>
  </div>
</main>
</body>
</html>
"""

(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
