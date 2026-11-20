#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Deterministic. Light theme only."""
import html
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def val(path):
    node = T
    for part in path.split("."):
        node = node[part]
    value = node["$value"]
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        return val(value[1:-1])
    return value


def color_rows():
    rows = []
    for name, token in T["light"].items():
        if name == "component" or not isinstance(token, dict) or "$value" not in token:
            continue
        if token.get("$type") != "color":
            continue
        rows.append(
            f'<div class="sw"><i style="background:{token["$value"]}"></i>'
            f"<div><code>light.{name}</code><span>{token['$value']}</span></div></div>"
        )
    return "\n".join(rows)


def type_rows():
    rows = []
    for name, token in T["core"]["typography"].items():
        v = token["$value"]
        family = val(v["fontFamily"][1:-1]) if isinstance(v["fontFamily"], str) and v["fontFamily"].startswith("{") else v["fontFamily"]
        stack = ", ".join(family)
        # Escaped, so a quoted family ("Rivian Sans") cannot close the style attribute.
        e = lambda x: html.escape(str(x), quote=True)
        rows.append(
            f'<div class="ty" style="font-family:{e(stack)};font-size:{e(v["fontSize"])};'
            f'font-weight:{e(v["fontWeight"])};line-height:{e(v["lineHeight"])};'
            f'letter-spacing:{e(v.get("letterSpacing", "normal"))}">'
            f"<code>core.typography.{e(name)}</code> Electric adventure. {e(v['fontSize'])} / {e(v['lineHeight'])}</div>"
        )
    return "\n".join(rows)


def main():
    page = val("light.page")
    text = val("light.text")
    muted = val("light.muted")
    accent = val("light.accent")
    on_accent = val("light.on-accent")
    primary = val("light.primary")
    on_primary = val("light.on-primary")
    surface = val("light.surface")
    border = val("light.border")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rivian style guide</title>
<style>
  body {{ margin: 0; background: {page}; color: {text}; font: 400 16px/24px Helvetica, Arial, sans-serif; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }}
  h1 {{ font-size: 44px; font-weight: 600; letter-spacing: -0.02em; margin: 0 0 8px; }}
  p {{ color: {muted}; max-width: 68ch; }}
  h2 {{ font-size: 24px; font-weight: 600; margin: 40px 0 12px; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .sw {{ display: flex; gap: 10px; align-items: center; }}
  .sw i {{ width: 40px; height: 40px; border-radius: 12px; box-shadow: inset 0 0 0 1px {border}; display: block; }}
  .sw code, .ty code {{ display: block; font-size: 12px; }}
  .sw span {{ color: {muted}; font-size: 12px; }}
  .ty {{ padding: 10px 0; border-bottom: 1px solid {border}; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; background: {surface}; padding: 24px; border-radius: 12px; }}
  button.brand {{ height: 32px; padding: 8px 16px; border: 0; border-radius: 9999px; background: {accent}; color: {on_accent}; font: 600 14px/16px Helvetica, Arial, sans-serif; }}
  button.primary {{ height: 56px; padding: 16px 40px; border: 0; border-radius: 9999px; background: {primary}; color: {on_primary}; font: 600 16px/18px Helvetica, Arial, sans-serif; }}
  button.hero {{ height: 56px; padding: 8px 16px; border: 0; border-radius: 40px; background: {page}; color: {text}; font: 500 14px/16px Helvetica, Arial, sans-serif; }}
  input.field {{ height: 56px; width: 280px; border: 0; border-radius: 12px; background: {surface}; padding: 0 16px; font: 400 16px/24px Helvetica, Arial, sans-serif; }}
</style>
</head>
<body>
<main>
  <h1>Rivian</h1>
  <p>Public signed-out marketing site, rivian.com, 2026-11-19. One light theme. Adventure is proprietary and is not loaded here. Specimens fall back to Helvetica.</p>
  <h2>Colour</h2>
  <div class="swatches">
    {color_rows()}
  </div>
  <h2>Type</h2>
  {type_rows()}
  <h2>Controls</h2>
  <div class="row">
    <button class="brand">Demo drive</button>
    <button class="primary">Reserve</button>
    <button class="hero">Design yours</button>
    <input class="field" placeholder="Email" aria-label="Email">
  </div>
</main>
</body>
</html>
"""
    (HERE / "style-guide.html").write_text(html)
    print("wrote style-guide.html")


if __name__ == "__main__":
    main()
