#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. One light theme."""
import html as _html
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


def e(value):
    """Escape a token value or name for an attribute or text: a quoted font stack or a stray
    character would otherwise end the style attribute."""
    return _html.escape(str(value), quote=True)


def css_color(token):
    return token["$value"]


page = T["light"]["color"]["page"]["$value"]
text = T["light"]["color"]["text"]["$value"]
muted = T["light"]["color"]["muted"]["$value"]
accent = T["light"]["color"]["accent"]["$value"]
surface = T["light"]["color"]["surface"]["$value"]
footer = T["light"]["color"]["footer"]["$value"]

swatches = []
for name, tok in flat(T["light"]["color"]):
    if tok.get("$type") != "color":
        continue
    val = tok["$value"]
    swatches.append(
        f'<div class="sw"><i style="background:{e(val)}"></i><div><code>{e(name)}</code><span>{e(val)}</span></div></div>'
    )

type_rows = []
for name, tok in flat(T["core"]["typography"]):
    v = tok["$value"]
    type_rows.append(
        f'<div class="ty" style="font-weight:{e(v["fontWeight"])};font-size:{e(v["fontSize"])};line-height:{e(v["lineHeight"])};letter-spacing:{e(v["letterSpacing"])};font-family:Helvetica,sans-serif">{e(name)}<small>{e(v["fontSize"])} / {e(v["lineHeight"])} / {e(v["fontWeight"])}</small></div>'
    )

space_rows = "".join(
    f'<div class="sp"><i style="width:{e(t["$value"])}"></i><code>{e(n)}</code><span>{e(t["$value"])}</span></div>'
    for n, t in flat(T["core"]["spacing"])
)
radius_rows = "".join(
    f'<div class="rd" style="border-radius:{e(t["$value"])}"><code>{e(n)}</code><span>{e(t["$value"])}</span></div>'
    for n, t in flat(T["core"]["radius"])
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MoMA style guide</title>
<style>
  :root {{
    --page: {page};
    --text: {text};
    --muted: {muted};
    --accent: {accent};
    --surface: {surface};
    --footer: {footer};
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/1.4 Helvetica, sans-serif; }}
  header {{ display: flex; align-items: center; justify-content: space-between; padding: 24px 48px; border-bottom: 1px solid #eee; position: sticky; top: 0; background: #fff; }}
  header strong {{ font-weight: 900; font-size: 28px; letter-spacing: -0.02em; }}
  header span {{ background: var(--accent); color: #000; padding: 12px 16px; font-weight: 700; }}
  main {{ padding: 32px 48px 80px; max-width: 1100px; }}
  h2 {{ font-size: 28px; font-weight: 900; letter-spacing: -0.02em; margin: 40px 0 12px; }}
  .swatches, .types {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 8px; }}
  .sw {{ display: flex; gap: 10px; align-items: center; border: 1px solid #eee; padding: 8px; }}
  .sw i {{ width: 36px; height: 36px; border: 1px solid #ddd; display: block; flex: none; }}
  code {{ font-family: ui-monospace, monospace; font-size: 12px; }}
  .sw span, .ty small, .sp span {{ color: var(--muted); display: block; font-size: 12px; }}
  .ty {{ padding: 8px 0; border-bottom: 1px solid #eee; }}
  .sp {{ display: flex; align-items: center; gap: 12px; margin: 6px 0; }}
  .sp i {{ height: 12px; background: #000; display: block; }}
  .rd {{ width: 88px; height: 48px; border: 2px solid #000; display: inline-flex; align-items: center; justify-content: center; margin: 8px 8px 0 0; font-size: 12px; }}
  .controls {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }}
  .btn {{ background: #000; color: #fff; border: 0; padding: 14px 18px; font-weight: 900; font-size: 16px; }}
  .ghost {{ background: #eee; color: #000; padding: 14px 18px; font-weight: 700; }}
  .tickets {{ background: var(--accent); color: #000; padding: 14px 18px; font-weight: 700; }}
  .field {{ border: 0; border-bottom: 1px solid #000; padding: 8px 2px; font-size: 18px; width: 280px; }}
  .card {{ background: #d5faea; padding: 24px; width: 240px; }}
  .card strong {{ color: #8a015f; font-size: 28px; letter-spacing: -0.02em; }}
  footer {{ background: var(--footer); color: #fff; padding: 32px 48px; }}
</style>
</head>
<body>
<header>
  <strong>MoMA</strong>
  <span>Tickets</span>
</header>
<main>
  <h2>Colour</h2>
  <div class="swatches">{''.join(swatches)}</div>
  <h2>Type</h2>
  <p>MoMA Sans is proprietary. This page falls back to Helvetica, the stack's second family.</p>
  <div class="types">{''.join(type_rows)}</div>
  <h2>Spacing</h2>
  {space_rows}
  <h2>Radius</h2>
  {radius_rows}
  <h2>Controls</h2>
  <div class="controls">
    <button class="btn">Plan your visit</button>
    <span class="tickets">Tickets</span>
    <span class="ghost">Donate</span>
    <input class="field" placeholder="Email" aria-label="Email">
  </div>
  <h2>Membership card</h2>
  <div class="card"><strong>Access</strong><p>$110 / year</p><button class="btn">Join or renew</button></div>
</main>
<footer>MoMA footer gray 444</footer>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
