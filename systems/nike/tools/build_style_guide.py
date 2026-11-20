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
    v = node["$value"]
    if isinstance(v, str) and v.startswith("{") and v.endswith("}"):
        return val(v[1:-1])
    return v


def attr(value):
    """A token value inside a double-quoted attribute: a quote in a font name must not end the attribute."""
    return html.escape(str(value), quote=True)


def color_rows():
    rows = []
    for name, token in T["light"].items():
        if name == "component" or not isinstance(token, dict) or "$value" not in token:
            continue
        if token.get("$type") != "color":
            continue
        rows.append(
            f'<div class="sw"><i style="background:{attr(token["$value"])}"></i>'
            f"<div><code>light.{attr(name)}</code><span>{attr(token['$value'])}</span></div></div>"
        )
    return "\n".join(rows)


def type_rows():
    rows = []
    for name, token in T["core"]["typography"].items():
        v = token["$value"]
        family = val(v["fontFamily"][1:-1]) if isinstance(v["fontFamily"], str) and v["fontFamily"].startswith("{") else v["fontFamily"]
        stack = ", ".join(family)
        rows.append(
            f'<div class="ty" style="font-family:{attr(stack)};font-size:{attr(v["fontSize"])};'
            f'font-weight:{attr(v["fontWeight"])};line-height:{attr(v["lineHeight"])}">'
            f"<code>core.typography.{attr(name)}</code> Just Do It. {attr(v['fontSize'])} / {attr(v['lineHeight'])}</div>"
        )
    return "\n".join(rows)


def main():
    page = val("light.page")
    text = val("light.text")
    muted = val("light.muted")
    surface = val("light.surface")
    accent = val("light.accent")
    on = val("light.on-accent")
    border = val("light.border")
    radius = val("core.control.button-radius")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nike style guide</title>
<style>
  body {{ margin: 0; background: {page}; color: {text}; font: 400 16px/24px Helvetica, Arial, sans-serif; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }}
  h1 {{ font-size: 24px; font-weight: 500; margin: 0 0 8px; }}
  p {{ color: {muted}; max-width: 68ch; }}
  h2 {{ font-size: 20px; font-weight: 500; margin: 40px 0 12px; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .sw {{ display: flex; gap: 10px; align-items: center; }}
  .sw i {{ width: 40px; height: 40px; border-radius: 4px; box-shadow: inset 0 0 0 1px {border}; display: block; }}
  .sw code, .ty code {{ display: block; font-size: 12px; }}
  .sw span {{ color: {muted}; font-size: 12px; }}
  .ty {{ padding: 10px 0; border-bottom: 1px solid {border}; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; background: {surface}; padding: 24px; border-radius: 8px; }}
  button.primary {{ height: 60px; padding: 18px 24px; border: 0; border-radius: {radius}; background: {accent}; color: {on}; font: 500 16px/24px Helvetica, Arial, sans-serif; }}
  button.on-image {{ height: 36px; padding: 6px 16px; border: 0; border-radius: {radius}; background: {page}; color: {text}; font: 500 16px/24px Helvetica, Arial, sans-serif; }}
  .search {{ height: 36px; width: 240px; border: 0; border-radius: 24px; background: {surface}; padding: 0 16px; font: 500 16px/24px Helvetica, Arial, sans-serif; }}
  .chip {{ height: 48px; min-width: 160px; border-radius: 4px; border: 1px solid {border}; background: {page}; color: {text}; font: 400 16px/24px Helvetica, Arial, sans-serif; }}
  .chip.disabled {{ background: {val("light.disabled-fill")}; color: {val("light.disabled-text")}; }}
</style>
</head>
<body>
<main>
  <h1>Nike</h1>
  <p>Public signed-out storefront, nike.com/sg, 2026-11-19. One light theme. Helvetica Now is proprietary and is not loaded here. The specimens fall back to Helvetica.</p>
  <h2>Colour</h2>
  <div class="swatches">
    {color_rows()}
  </div>
  <h2>Type</h2>
  {type_rows()}
  <h2>Controls</h2>
  <div class="row">
    <button class="primary">Add to Bag</button>
    <button class="on-image">Shop</button>
    <input class="search" placeholder="Search" aria-label="Search">
    <button class="chip">US M 9 / W 10.5</button>
    <button class="chip disabled">US M 6 / W 7.5</button>
  </div>
</main>
</body>
</html>
"""
    (HERE / "style-guide.html").write_text(html)
    print("wrote style-guide.html", len(html))


if __name__ == "__main__":
    main()
