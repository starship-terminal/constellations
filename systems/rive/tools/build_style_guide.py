#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Specimens use the token values. Orbitron, Inter, and JetBrains Mono load from
a public font host. PragmataPro and Tomorrow fall back to ui-monospace and
system-ui. Dark is the marketing page. Light is the login panel.
"""
import html
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def resolve(path, seen=None):
    seen = seen or set()
    if path in seen:
        return None
    node = T
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    if not isinstance(node, dict) or "$value" not in node:
        return None
    value = node["$value"]
    if isinstance(value, str):
        match = re.fullmatch(r"\{([^{}]+)\}", value.strip())
        if match:
            ref = match.group(1)
            # Aliases name core paths without the set ({color.black} is core.color.black).
            if ref.split(".")[0] not in T:
                ref = "core." + ref
            return resolve(ref, seen | {path})
    return value


def css_shadow(layers):
    return ", ".join(
        f"{layer['offsetX']} {layer['offsetY']} {layer['blur']} {layer['spread']} {layer['color']}"
        for layer in layers
    )


def swatch(name, value):
    return (
        f'<div class="swatch"><i style="background:{html.escape(value)}"></i>'
        f"<span>{html.escape(name)}</span><code>{html.escape(value)}</code></div>"
    )


roles = ("page", "surface", "text", "textMuted", "accent", "border", "action", "actionText", "focus", "danger")
dark = {k: resolve("dark." + k) for k in roles}
light = {k: resolve("light." + k) for k in roles}
colors = "".join(swatch(key, token["$value"]) for key, token in T["core"]["color"].items())
type_rows = []
for key, token in T["core"]["typography"].items():
    value = token["$value"]
    type_rows.append(
        f'<div class="type" style="font-family:{html.escape(value["fontFamily"])};'
        f'font-size:{value["fontSize"]};font-weight:{value["fontWeight"]};'
        f'line-height:{value["lineHeight"]};letter-spacing:{value["letterSpacing"]}">'
        f'<b>{html.escape(key)}</b> {html.escape(value["fontSize"])} / {html.escape(str(value["fontWeight"]))}'
        f"<span>Agent speed. Artist control.</span></div>"
    )
radius_bits = "".join(
    f'<div class="radius" style="border-radius:{token["$value"]}"><span>{html.escape(key)} {html.escape(token["$value"])}</span></div>'
    for key, token in T["core"]["radius"].items()
)
space_bits = "".join(
    f'<div class="space"><i style="width:{token["$value"]}"></i><span>{html.escape(key)} {html.escape(token["$value"])}</span></div>'
    for key, token in T["core"]["spacing"].items()
)

page = f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<title>Rive style guide</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=JetBrains+Mono:wght@400;500&family=Orbitron:wght@500;600;800;900&display=swap">
<style>
  :root {{
    --page: {dark["page"]};
    --surface: {dark["surface"]};
    --text: {dark["text"]};
    --muted: {dark["textMuted"]};
    --accent: {dark["accent"]};
    --border: {dark["border"]};
    --action: {dark["action"]};
    --action-text: {dark["actionText"]};
    --focus: {dark["focus"]};
    --danger: {dark["danger"]};
  }}
  html[data-theme="light"] {{
    --page: {light["page"]};
    --surface: {light["surface"]};
    --text: {light["text"]};
    --muted: {light["textMuted"]};
    --accent: {light["accent"]};
    --border: {light["border"]};
    --action: {light["action"]};
    --action-text: {light["actionText"]};
    --focus: {light["focus"]};
    --danger: {light["danger"]};
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 14px/1.5 Inter, system-ui, sans-serif; }}
  header, main {{ width: min(960px, calc(100% - 48px)); margin: 0 auto; }}
  header {{ display: flex; justify-content: space-between; align-items: center; padding: 32px 0; }}
  h1 {{ font-family: Orbitron, Inter, sans-serif; font-weight: 800; letter-spacing: -0.01em; font-size: 32px; margin: 0; }}
  h2 {{ font-family: Orbitron, Inter, sans-serif; font-size: 16px; letter-spacing: 0.08em; text-transform: uppercase; margin: 40px 0 12px; }}
  button.toggle {{ background: var(--surface); color: var(--text); border: 1px solid var(--border); border-radius: 2px; padding: 8px 12px; font: 12px/1 JetBrains Mono, ui-monospace, monospace; letter-spacing: 0.08em; }}
  .swatches, .radii {{ display: flex; flex-wrap: wrap; gap: 12px; }}
  .swatch {{ width: 140px; }}
  .swatch i {{ display: block; height: 48px; border-radius: 4px; border: 1px solid var(--border); }}
  .swatch span, .swatch code, .space span {{ display: block; color: var(--muted); font-size: 12px; }}
  .type {{ padding: 8px 0; border-bottom: 1px solid var(--border); }}
  .type b {{ display: block; font: 11px/1.4 Inter, sans-serif; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }}
  .radius {{ width: 120px; height: 64px; border: 1px solid var(--border); display: flex; align-items: end; padding: 8px; }}
  .space {{ display: flex; align-items: center; gap: 8px; margin: 4px 0; }}
  .space i {{ height: 8px; background: var(--accent); display: block; }}
  .row {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; margin: 12px 0; }}
  .cta {{ background: {resolve("core.color.white")}; color: {resolve("core.color.black")}; border-radius: 4px; padding: 5px 9px 6px; font: 500 12px/15.6px ui-monospace, monospace; letter-spacing: 1.2px; text-transform: uppercase; box-shadow: {css_shadow(T["core"]["shadow"]["ctaInset"]["$value"])}; text-decoration: none; }}
  .auth {{ background: {resolve("core.color.authBlue")}; color: white; border: 0; border-radius: 2px; height: 44px; padding: 0 16px; font: 500 12px/16px Orbitron, sans-serif; letter-spacing: 0.96px; text-transform: uppercase; }}
  .field {{ background: var(--surface); color: var(--text); border: 1px solid {resolve("core.color.authBorder")}; border-radius: 2px; height: 44px; padding: 0 12px; font: 16px Inter, sans-serif; width: 240px; }}
  .ghost {{ background: {resolve("core.color.white05")}; color: var(--text); border-radius: 4px; padding: 5px 9px 6px; box-shadow: {css_shadow(T["core"]["shadow"]["fieldInset"]["$value"])}; }}
  .note {{ color: var(--muted); max-width: 62ch; }}
</style>
</head>
<body>
<header>
  <h1>RIVE</h1>
  <button class="toggle" type="button" onclick="document.documentElement.dataset.theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'">TOGGLE THEME</button>
</header>
<main>
  <p class="note">Values from the public site and the signed-out login, measured 2026-11-19. Dark is the marketing page. Light is the login panel.</p>
  <h2>Colour</h2>
  <div class="swatches">{colors}</div>
  <h2>Type</h2>
  {''.join(type_rows)}
  <h2>Radius</h2>
  <div class="radii">{radius_bits}</div>
  <h2>Spacing</h2>
  {space_bits}
  <h2>Controls</h2>
  <div class="row">
    <a class="cta" href="#cta">Get started</a>
    <span class="ghost">Copy</span>
    <button class="auth" type="button">Log in</button>
    <input class="field" placeholder="Email or username" aria-label="Email or username">
  </div>
</main>
</body>
</html>
"""
if __name__ == "__main__":
    (HERE / "style-guide.html").write_text(page)
    print("wrote style-guide.html")
