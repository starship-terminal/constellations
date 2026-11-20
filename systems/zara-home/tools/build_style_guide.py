#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. No network, no invented colours."""
import html as htmllib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def resolve(value, trail=()):
    if not isinstance(value, str) or not (value.startswith("{") and value.endswith("}")):
        return value
    path = value[1:-1]
    if path in trail:
        raise ValueError("alias cycle: " + path)
    node = TOKENS["core"]
    for part in path.split("."):
        node = node[part]
    return resolve(node["$value"], trail + (path,))


def walk(path):
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return resolve(node["$value"])


def esc(value):
    """Every token value is escaped before it lands in an attribute or text (a quoted font name
    would otherwise close style="...")."""
    return htmllib.escape(str(value), quote=True)


def swatch(name, path):
    value = esc(walk(path))
    return (
        f'<div class="swatch"><i style="background:{value}"></i>'
        f"<b>{name}</b><code>{value}</code><small>{path}</small></div>"
    )


page = walk("light.background.page")
ink = walk("light.text.primary")
muted = walk("light.text.muted")
body = walk("light.text.body")
sans = walk("core.fontFamily.sans")
focus = walk("light.border.focus")
rule = walk("light.border.rule")
for _value in (page, ink, muted, body, sans, focus, rule):
    if any(c in str(_value) for c in "<>{};"):
        raise SystemExit(f"refusing a token value that would break the stylesheet: {_value!r}")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Zara Home style guide</title>
<style>
  :root {{
    --page: {page};
    --ink: {ink};
    --muted: {muted};
    --body: {body};
    --sans: {sans};
    --focus: {focus};
    --rule: {rule};
  }}
  body {{ margin: 0; background: var(--page); color: var(--ink); font-family: Arial, "Lucida Sans Unicode", sans-serif; font-weight: 400; letter-spacing: 0.2px; }}
  main {{ max-width: 880px; margin: 0 auto; padding: 40px 24px 80px; }}
  h1 {{ font-weight: 600; font-size: 22px; line-height: 24px; letter-spacing: 0.2px; text-transform: uppercase; margin: 0 0 8px; }}
  h2 {{ font-weight: 500; font-size: 12px; line-height: 16px; letter-spacing: 0.2px; text-transform: uppercase; margin: 40px 0 12px; }}
  p.lede {{ color: var(--muted); font-size: 14px; line-height: 20px; max-width: 46em; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 12px; }}
  .swatch {{ border: 1px solid var(--ink); padding: 8px; }}
  .swatch i {{ display: block; height: 48px; border: 1px solid var(--rule); }}
  .swatch b, .swatch code, .swatch small {{ display: block; font-size: 12px; letter-spacing: 0.2px; font-weight: 400; }}
  .swatch code {{ color: var(--muted); }}
  .btn {{ display: inline-flex; align-items: center; justify-content: center; height: 36px; padding: 0 16px; background: var(--ink); color: #fff; border: 1px solid var(--ink); border-radius: 0; font-size: 12px; font-weight: 600; letter-spacing: 0.2px; text-transform: uppercase; }}
  .btn.ghost {{ background: #fff; color: rgba(0, 0, 0, 0.87); }}
  .btn.add {{ background: rgba(255, 255, 255, 0.8); color: rgba(0, 0, 0, 0.87); border: 0; width: 220px; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
  .search {{ font-size: 30px; font-weight: 500; line-height: 18px; letter-spacing: 0.2px; text-transform: uppercase; border: 0; border-bottom: 0; width: 100%; padding: 0; color: rgba(0, 0, 0, 0.87); background: transparent; }}
  .search::placeholder {{ color: rgba(0, 0, 0, 0.87); }}
  .price {{ font-size: 18px; font-weight: 600; line-height: 22px; }}
  .sku {{ color: var(--muted); font-size: 11px; line-height: 15px; }}
  .swatch-dot {{ width: 20px; height: 20px; border: 1px solid #fff; outline: 1px solid var(--ink); }}
  footer {{ margin-top: 24px; border-top: 1px solid var(--rule); padding-top: 16px; font-size: 12px; font-weight: 300; text-transform: uppercase; }}
</style>
</head>
<body>
<main>
  <h1>Sateen duvet cover</h1>
  <p class="lede">ZH-Sans is proprietary and is not loaded here. The fallback is Arial, the second family in the measured stack. Values come from tokens.json.</p>
  <h2>Colour</h2>
  <div class="swatches">
    {swatch("page", "light.background.page")}
    {swatch("ink", "light.text.primary")}
    {swatch("body ink", "light.text.body")}
    {swatch("muted", "light.text.muted")}
    {swatch("focus", "light.border.focus")}
    {swatch("rule", "light.border.rule")}
    {swatch("hover", "light.action.hover")}
    {swatch("sale declared", "core.color.sale")}
    {swatch("warn declared", "core.color.warn")}
  </div>
  <h2>Type</h2>
  <p class="price">45.99 € – 79.99 €</p>
  <p class="sku">0136/088/537</p>
  <p class="lede">Plain duvet cover in 300 thread count cotton sateen.</p>
  <h2>Controls</h2>
  <div class="row">
    <span class="btn">Go</span>
    <span class="btn ghost">No, go to the website</span>
    <span class="btn add">Add</span>
  </div>
  <p><input class="search" placeholder="What are you searching for?" aria-label="Search"></p>
  <div class="row">
    <i class="swatch-dot" style="background:{esc(walk('light.background.page'))}"></i>
    <i class="swatch-dot" style="background:{esc(walk('light.text.primary'))}"></i>
    <i class="swatch-dot" style="background:{esc(walk('light.text.muted'))}"></i>
  </div>
  <footer>Help · Contact · Stores</footer>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
