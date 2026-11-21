#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: Trip.com declares no dark theme."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def swatch(name, value, source):
    if not isinstance(value, str) or not (value.startswith("#") or value.startswith("rgb")):
        return ""
    return (
        f'<div class="sw"><i style="background:{value}"></i>'
        f'<div><b>{name}</b><code>{value}</code><small>{source}</small></div></div>'
    )


def walk(node, prefix=""):
    rows = []
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}{k}"
        if isinstance(v, dict) and "$value" in v:
            rows.append((path, v))
        elif isinstance(v, dict):
            rows.extend(walk(v, path + "."))
    return rows


colors = [(n, t) for n, t in walk(T["light"]["color"]) if t["$type"] == "color" and not str(t["$value"]).startswith("{")]
core_colors = walk(T["core"]["color"])[:24]
radii = walk(T["core"]["radius"])
spaces = walk(T["core"]["spacing"])

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Trip.com style guide</title>
<style>
  body {{ margin: 0; font: 14px/1.45 system-ui, sans-serif; color: #121826; background: #fff; }}
  header {{ padding: 28px 32px; background: #2c61fe; color: #fff; }}
  header h1 {{ margin: 0; font-size: 28px; }}
  main {{ padding: 24px 32px 64px; max-width: 1100px; }}
  h2 {{ margin: 28px 0 12px; font-size: 18px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 8px; }}
  .sw {{ display: flex; gap: 10px; align-items: center; border: 1px solid #ebedf1; border-radius: 8px; padding: 8px; }}
  .sw i {{ width: 36px; height: 36px; border-radius: 4px; border: 1px solid #ebedf1; flex: none; }}
  .sw b {{ display: block; font-size: 12px; }}
  .sw code {{ font-size: 12px; color: #4f5563; }}
  .sw small {{ display: block; color: #6f7685; font-size: 11px; }}
  .btn {{ display: inline-flex; align-items: center; height: 48px; padding: 0 16px; border-radius: 4px; background: #2c61fe; color: #fff; font-weight: 700; border: 0; }}
  .btn.ghost {{ background: #fff; color: #121826; border: 1px solid #b9bec7; }}
  .note {{ color: #4f5563; max-width: 68ch; }}
</style>
</head>
<body>
<header>
  <h1>Trip.com</h1>
  <p>Public tokens measured from the homepage CSSOM, 2026-11-21. Light only.</p>
</header>
<main>
  <h2>Actions</h2>
  <p><span class="btn">Search</span> <span class="btn ghost">Sign in/register</span></p>
  <p class="note">Search is the filled brand button (#2c61fe, 4px radius, 700). The header sign-in control is a filled blue pill on the live site; the ghost here is the dialog's secondary action.</p>
  <h2>Semantic colour</h2>
  <div class="grid">
    {''.join(swatch(n, t['$value'], t['$extensions']['source'][:80]) for n, t in colors[:48])}
  </div>
  <h2>Core blue ramp (first steps)</h2>
  <div class="grid">
    {''.join(swatch(n, t['$value'], 'core') for n, t in core_colors if str(t.get('$value','')).startswith('#'))}
  </div>
  <h2>Radius</h2>
  <ul>{''.join(f'<li><code>{n}</code> {t["$value"]}</li>' for n, t in radii)}</ul>
  <h2>Spacing</h2>
  <ul>{''.join(f'<li><code>{n}</code> {t["$value"]}</li>' for n, t in spaces)}</ul>
  <h2>Not captured</h2>
  <p class="note">Dark theme, motion durations, and elevation shadows are not declared as custom properties in this reading. Trip Geom is the product's font and is not loaded here.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
