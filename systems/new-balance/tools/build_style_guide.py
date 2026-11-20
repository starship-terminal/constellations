#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: the captured site had no dark theme."""
import html as htmllib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if str(k).startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


def resolve(path, seen=None):
    seen = seen or set()
    if path in seen:
        raise SystemExit(f"alias loop at {path}")
    node = T["core"] if path.split(".")[0] in T["core"] else T["light"]
    # Aliases in this file are core paths (color.white) or already-qualified.
    if path.split(".")[0] in ("core", "light"):
        node = T
        parts = path.split(".")
    else:
        node = T["core"] if path.split(".")[0] in T["core"] else T["light"]
        parts = path.split(".")
    for part in parts:
        node = node[part]
    value = node["$value"]
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        return resolve(value[1:-1], seen | {path})
    if isinstance(value, dict):
        return {k: resolve(v[1:-1], seen | {path}) if isinstance(v, str) and v.startswith("{") else v
                for k, v in value.items()}
    return value


def swatch(name, path):
    value = resolve(path)
    return (
        f'<div class="sw"><i style="background:{value}"></i>'
        f'<div><code>{name}</code><span>{value}</span><small>{path}</small></div></div>'
    )


colours = "\n".join(swatch(name, f"core.color.{name}") for name, _tok in flat(T["core"]["color"]))
roles = "\n".join(
    swatch(name, path)
    for name, path in [
        ("page", "light.background.page"),
        ("surface", "light.background.surface"),
        ("text", "light.text.primary"),
        ("muted", "light.text.muted"),
        ("accent", "light.action.primary"),
        ("brand", "light.action.brand"),
        ("border", "light.border.default"),
    ]
)

def attr(value):
    """A token value inside a double-quoted attribute or text: a quoted font name must not end the attribute."""
    return htmllib.escape(str(value), quote=True)


type_rows = []
for name, tok in flat(T["core"]["typography"]):
    v = resolve(f"core.typography.{name}")
    type_rows.append(
        f'<div class="ty" style="font-family:{attr(v["fontFamily"])};font-weight:{attr(v["fontWeight"])};'
        f'font-size:{attr(v["fontSize"])};line-height:{attr(v["lineHeight"])}">'
        f'<code>{attr(name)}</code><span>{attr(v["fontSize"])} / {attr(v["lineHeight"])} · {attr(v["fontWeight"])}</span>'
        f'<p>New Balance</p></div>'
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>New Balance style guide</title>
<style>
  :root {{ color-scheme: light; }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: #fff; color: #000; font: 300 14px/20px "Helvetica Neue", Helvetica, Arial, sans-serif; }}
  header, main {{ max-width: 960px; margin: 0 auto; padding: 24px 20px; }}
  header {{ background: #151415; color: #fff; max-width: none; }}
  header .in {{ max-width: 960px; margin: 0 auto; }}
  h1 {{ font-weight: 500; font-size: 32px; line-height: 40px; margin: 0 0 8px; }}
  h2 {{ font-weight: 500; font-size: 24px; margin: 32px 0 12px; }}
  p {{ max-width: 68ch; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .sw {{ display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: center; }}
  .sw i {{ width: 44px; height: 44px; border-radius: 2px; box-shadow: inset 0 0 0 1px #dee0e1; }}
  .sw code, .ty code {{ font: 12px/16px ui-monospace, Menlo, monospace; }}
  .sw span, .sw small, .ty span {{ display: block; color: #5c6268; font-size: 12px; }}
  .ty {{ padding: 12px 0; border-bottom: 1px solid #dee0e1; }}
  .ty p {{ margin: 4px 0 0; }}
  .btn {{ display: inline-block; margin: 0 8px 8px 0; padding: 16px 12px; border-radius: 2px; font: 300 14px/20px "Helvetica Neue", Helvetica, Arial, sans-serif; text-decoration: none; }}
  .primary {{ background: #151415; color: #fff; border: 1px solid #151415; }}
  .secondary {{ background: #fff; color: #151415; border: 1px solid #e5e7e8; }}
  .field {{ display: block; width: 328px; max-width: 100%; height: 58px; padding: 28px 12px 12px; border: 1px solid #abb0b4; border-radius: 4px; font: 500 16px/23px "Helvetica Neue", Helvetica, Arial, sans-serif; }}
  .note {{ color: #5c6268; font-size: 13px; }}
</style>
</head>
<body>
<header><div class="in"><h1>New Balance</h1><p>Signed-out UK storefront, measured 2026-11-19. One light theme. Proxima Nova and ITC Garamond are licensed faces and are not loaded here.</p></div></header>
<main>
  <h2>Roles</h2>
  <div class="grid">{roles}</div>
  <h2>Palette</h2>
  <div class="grid">{colours}</div>
  <h2>Type</h2>
  {''.join(type_rows)}
  <h2>Controls</h2>
  <a class="btn primary" href="#controls">Add to Bag</a>
  <a class="btn secondary" href="#controls">Shop now</a>
  <input class="field" placeholder="Email" aria-label="Email">
  <p class="note">Button radius 2px, field radius 4px, primary height 54px, field height 58px. Focus ring on keyboard focus is 2px solid #015ecc. No dark theme was on the captured pages.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
