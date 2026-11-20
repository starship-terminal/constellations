#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Deterministic. Light theme only."""
import html as htmllib
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


def color_rows():
    rows = []
    for name, token in T["light"].items():
        if not isinstance(token, dict) or token.get("$type") != "color":
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
        family = val(v["fontFamily"][1:-1])
        stack = htmllib.escape(", ".join(family), quote=True)
        ls = v.get("letterSpacing", "normal")
        rows.append(
            f'<div class="ty" style="font-family:{stack};font-size:{v["fontSize"]};'
            f'font-weight:{v["fontWeight"]};line-height:{v["lineHeight"]};letter-spacing:{ls}">'
            f"<code>core.typography.{name}</code> A pixel-imperfect holiday. {v['fontSize']} / {v['lineHeight']}</div>"
        )
    return "\n".join(rows)


def main():
    page = val("light.page")
    text = val("light.text")
    surface = val("light.surface")
    accent = val("light.accent")
    on = val("light.on-accent")
    border = val("light.border")
    promo = val("light.promo")
    active = val("light.nav-active")
    highlight = val("light.highlight")
    error = val("light.error")
    radius = val("core.radius.none")
    pill = val("core.radius.pill")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Polaroid style guide</title>
<style>
  body {{ margin: 0; background: {page}; color: {text}; font: 400 16px/1.2 Arial, sans-serif; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }}
  h1 {{ font-size: 40px; font-weight: 600; line-height: 40px; margin: 0 0 8px; letter-spacing: 0; }}
  p {{ max-width: 68ch; }}
  h2 {{ font-size: 22px; font-weight: 600; margin: 40px 0 12px; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .sw {{ display: flex; gap: 10px; align-items: center; }}
  .sw i {{ width: 40px; height: 40px; border-radius: 0; box-shadow: inset 0 0 0 1px {border}; display: block; }}
  .sw code, .ty code {{ display: block; font-size: 12px; }}
  .sw span {{ font-size: 12px; }}
  .ty {{ padding: 10px 0; border-bottom: 1px solid {surface}; }}
  .promo {{ background: {promo}; color: {on}; padding: 8px 16px; font-size: 13px; }}
  .nav {{ display: flex; gap: 16px; padding: 16px 0; font-size: 13px; }}
  .nav .on {{ color: {active}; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; background: {surface}; padding: 24px; }}
  .photo {{ background: #3a2a22; padding: 24px; display: flex; gap: 12px; }}
  a.shop, button.continue, a.finder, a.compare {{
    display: inline-flex; align-items: center; justify-content: center;
    font: 400 12px/14.4px ui-monospace, monospace; letter-spacing: 0; text-transform: uppercase;
    text-decoration: none; box-sizing: border-box;
  }}
  a.shop {{ height: 42px; padding: 13px 15px; background: {page}; color: {text}; border: 0; border-radius: {radius}; }}
  a.ghost {{ height: 42px; padding: 13px 15px; background: transparent; color: {page}; border: 1px solid {page}; border-radius: {radius}; font: 400 12px/14.4px ui-monospace, monospace; text-transform: uppercase; text-decoration: none; display: inline-flex; align-items: center; }}
  button.continue {{ height: 45px; width: 280px; border: 0; border-radius: {radius}; background: {accent}; color: {on}; }}
  a.finder {{ height: 32px; padding: 0 16px; border-radius: {pill}; border: 1px solid {border}; background: {page}; color: {text}; }}
  a.compare {{ height: 32px; padding: 0 12px; border-radius: {radius}; border: 1px solid {border}; background: {page}; color: {text}; }}
  .field {{ width: 280px; }}
  .field label {{ display: block; font-size: 13px; margin-bottom: 4px; }}
  .field .box {{ height: 45px; border: 1px solid {border}; display: flex; align-items: center; padding: 0 15px; font-size: 16px; background: {page}; }}
  .note {{ font-size: 13px; }}
  .swatch-note {{ font-size: 13px; }}
</style>
</head>
<body>
<main>
  <div class="promo">Free Standard Shipping over €95</div>
  <div class="nav"><span class="on">Holidays</span><span>Cameras</span><span>Film</span><span>Support</span></div>
  <h1>Polaroid</h1>
  <p class="note">Public storefront, signed out, one light theme. Faces fall back to Arial and a monospace stand-in. Real Head and Commit Mono are proprietary and are not in this package.</p>
  <h2>Colour</h2>
  <div class="swatches">
    {color_rows()}
  </div>
  <p class="swatch-note">Highlight {highlight}. Error {error}. No separate muted text colour was computed.</p>
  <h2>Type</h2>
  {type_rows()}
  <h2>Controls</h2>
  <div class="photo">
    <a class="shop" href="#shop">Shop bundles</a>
    <a class="ghost" href="#inspired">Get inspired</a>
  </div>
  <div class="row">
    <button class="continue" type="button">Continue</button>
    <a class="finder" href="#finder">Product finder</a>
    <a class="compare" href="#compare">Compare</a>
    <div class="field"><label>Email</label><div class="box">Email</div></div>
  </div>
</main>
</body>
</html>
"""
    (HERE / "style-guide.html").write_text(html)
    print("wrote style-guide.html")


if __name__ == "__main__":
    main()
