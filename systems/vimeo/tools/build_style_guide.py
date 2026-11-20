#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Light only: the signed-out pages did not expose a dark token set. Colours,
radii and type on the page come from tokens.json. ABC Repro is proprietary
and is not loaded; the page falls back to system-ui.
"""
import html
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def get(path):
    node = T
    for part in path.split("."):
        node = node[part]
    return node["$value"]


def resolve(value, seen=None):
    seen = seen or set()
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        ref = value[1:-1]
        if ref in seen:
            return value
        return resolve(get("core." + ref), seen | {ref})
    return value


def swatch(path, label):
    value = resolve(get(path))
    return (
        f'<div class="sw"><i style="background:{html.escape(str(value))}"></i>'
        f'<div><b>{html.escape(label)}</b><code>{html.escape(path)}</code>'
        f'<span>{html.escape(str(value))}</span></div></div>'
    )


def main():
    roles = [
        ("light.background.page", "Page"),
        ("light.background.surface", "Surface"),
        ("light.background.fill-brand", "Brand"),
        ("light.text.primary", "Text"),
        ("light.text.secondary", "Muted"),
        ("light.text.inverted", "Inverted text"),
        ("light.border.stroke", "Stroke"),
        ("light.border.focus", "Focus"),
        ("light.button.primary", "Primary button"),
        ("light.button.secondary", "Secondary button"),
        ("light.background.positive", "Positive"),
        ("light.background.destructive", "Destructive"),
        ("light.background.upsell", "Upsell"),
        ("light.text.link", "Link"),
    ]
    ramps = []
    for name in ("gray", "vimeo-blue", "blue", "green", "red", "orange", "purple", "yellow"):
        steps = []
        group = T["core"]["color"]
        keys = sorted(k for k in group if k.startswith(name + "-") and k.rsplit("-", 1)[-1].isdigit())
        for key in keys:
            step = key.rsplit("-", 1)[-1]
            value = group[key]["$value"]
            steps.append(f'<i title="{html.escape(key)} {html.escape(value)}" style="background:{html.escape(value)}"></i>')
        if steps:
            ramps.append(f'<div class="ramp"><b>{html.escape(name)}</b>{"".join(steps)}</div>')
    radii = []
    for key, token in T["core"]["radius"].items():
        if token["$value"] in ("999px", "9999px", "0rem"):
            continue
        radii.append(
            f'<div class="cell"><i style="border-radius:{html.escape(token["$value"])}"></i>'
            f'<span>{html.escape(key)} {html.escape(token["$value"])}</span></div>'
        )
    spaces = []
    for key in ("xs", "sm", "md", "lg", "xl", "2xl", "3xl"):
        token = T["core"]["space"][key]
        spaces.append(
            f'<div class="cell"><i style="width:{html.escape(token["$value"])}"></i>'
            f'<span>{html.escape(key)} {html.escape(token["$value"])}</span></div>'
        )
    type_rows = []
    for key, token in T["core"]["typography"].items():
        value = token["$value"]
        type_rows.append(
            "<tr><td><code>{key}</code></td><td style=\"font-size:{size};line-height:{lh};"
            "letter-spacing:{ls};font-weight:{w}\">{sample}</td>"
            "<td>{size} / {lh}</td></tr>".format(
                key=html.escape(key),
                size=html.escape(str(value["fontSize"])),
                lh=html.escape(str(value["lineHeight"])),
                ls=html.escape(str(value["letterSpacing"])),
                w=html.escape(str(value["fontWeight"])),
                sample="The quick brown fox" if key != "eyebrow" else "VIDEO MARKETING",
            )
        )
    brand = resolve(get("light.background.fill-brand"))
    ink = resolve(get("light.text.primary"))
    page = resolve(get("light.background.page"))
    surface = resolve(get("light.background.surface"))
    muted = resolve(get("light.text.secondary"))
    primary = resolve(get("light.button.primary"))
    inverted = resolve(get("light.text.inverted"))
    secondary = resolve(get("light.button.secondary"))
    stroke = resolve(get("light.border.stroke"))
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vimeo style guide</title>
<style>
:root {{
  --page: {page};
  --surface: {surface};
  --ink: {ink};
  --muted: {muted};
  --brand: {brand};
  --stroke: {stroke};
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--ink); font: 400 16px/1.4 system-ui, sans-serif; }}
header, main {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px; }}
header {{ display: flex; justify-content: space-between; align-items: center; }}
h1 {{ font-size: 32px; letter-spacing: -0.04em; margin: 0; }}
h2 {{ font-size: 20px; margin: 40px 0 12px; }}
p {{ color: var(--muted); max-width: 68ch; }}
.swatches, .ramps, .row {{ display: grid; gap: 12px; }}
.swatches {{ grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); }}
.sw {{ display: flex; gap: 12px; align-items: center; background: var(--surface); border-radius: 12px; padding: 10px; }}
.sw i {{ width: 40px; height: 40px; border-radius: 8px; box-shadow: inset 0 0 0 1px rgba(26,70,128,.12); }}
.sw b, .sw code, .sw span {{ display: block; }}
.sw code, .sw span {{ font-size: 12px; color: var(--muted); }}
.ramp {{ display: flex; gap: 4px; align-items: center; }}
.ramp b {{ width: 88px; font-size: 12px; }}
.ramp i {{ width: 28px; height: 28px; border-radius: 4px; }}
.row {{ grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); }}
.cell i {{ display: block; height: 48px; background: var(--brand); box-shadow: inset 0 0 0 1px rgba(26,70,128,.12); }}
.cell span {{ font-size: 12px; color: var(--muted); }}
.states {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }}
.btn {{ display: inline-flex; align-items: center; height: 48px; padding: 0 20px; border-radius: 16px; background: {brand}; color: #000; text-decoration: none; }}
.btn.dark {{ background: {primary}; color: {inverted}; border-radius: 12px; height: 40px; padding: 0 16px; }}
.btn.ghost {{ background: {secondary}; color: {ink}; border-radius: 12px; height: 40px; }}
.btn.social {{ background: #fff; color: {ink}; border: 1px solid {stroke}; border-radius: 10px; }}
.field {{ height: 40px; border-radius: 12px; border: 0; outline: 1px solid rgba(41,81,128,.24); background: rgba(255,255,255,.64); padding: 0 16px; width: 280px; }}
table {{ width: 100%; border-collapse: collapse; background: var(--surface); border-radius: 12px; overflow: hidden; }}
td {{ padding: 12px 16px; border-bottom: 1px solid rgba(26,70,128,.12); vertical-align: baseline; }}
code {{ font-family: ui-monospace, monospace; font-size: 12px; }}
</style>
</head>
<body>
<header>
  <h1>Vimeo</h1>
  <span class="btn">Join</span>
</header>
<main>
  <p>Signed-out public surfaces, measured 2026-11-19. Light only. Values come from tokens.json.</p>
  <h2>Colour</h2>
  <div class="swatches">{''.join(swatch(path, label) for path, label in roles)}</div>
  <h2>Ramps</h2>
  <div class="ramps">{''.join(ramps)}</div>
  <h2>Type</h2>
  <table>{''.join(type_rows)}</table>
  <h2>Radius</h2>
  <div class="row">{''.join(radii)}</div>
  <h2>Space</h2>
  <div class="row">{''.join(spaces)}</div>
  <h2>Controls</h2>
  <div class="states">
    <a class="btn">Continue with email</a>
    <a class="btn dark">Join</a>
    <a class="btn ghost">Log in</a>
    <a class="btn social">Continue with Google</a>
    <input class="field" placeholder="Enter email" aria-label="Enter email">
  </div>
</main>
</body>
</html>
"""
    (HERE / "style-guide.html").write_text(doc)
    print("wrote style-guide.html")


if __name__ == "__main__":
    main()
