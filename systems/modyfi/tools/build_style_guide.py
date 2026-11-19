#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Dark only: Modyfi publishes one theme."""
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
        return val(v[1:-1] if "." in v[1:-1] else "core.color." + v[1:-1].split(".")[-1] if False else v[1:-1])
    return v


def resolve(v):
    if isinstance(v, str) and v.startswith("{") and v.endswith("}"):
        ref = v[1:-1]
        # semantic aliases point at core groups without the set name
        for prefix in ("core.", ""):
            try:
                return resolve(val(prefix + ref) if False else _lookup(prefix + ref))
            except KeyError:
                continue
        return _lookup("core." + ref) if not ref.startswith("core.") else _lookup(ref)
    return v


def _lookup(path):
    node = T
    for part in path.split("."):
        node = node[part]
    v = node["$value"]
    if isinstance(v, str) and v.startswith("{") and v.endswith("}"):
        inner = v[1:-1]
        if not inner.startswith("core.") and inner.split(".")[0] in ("color", "font", "radius", "space"):
            return _lookup("core." + inner)
        return _lookup(inner)
    return v


colors = []
for name, token in T["core"]["color"].items():
    colors.append((name, _lookup("core.color." + name)))

html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Modyfi style guide</title>
<style>
  body { margin: 0; background: #000; color: #fff; font: 16px/1.5 Inter, Arial, sans-serif; }
  main { max-width: 960px; margin: 0 auto; padding: 48px 24px 80px; }
  h1 { font-weight: 600; letter-spacing: -1px; font-size: 40px; }
  h2 { margin-top: 40px; font-size: 22px; }
  .swatches { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 12px; }
  .swatch { border: 1px solid #182233; border-radius: 12px; overflow: hidden; }
  .chip { height: 72px; }
  .meta { padding: 8px 10px; font-size: 12px; color: #c9c9c9; }
  .meta b { color: #fff; display: block; }
  .row { display: flex; gap: 16px; align-items: center; flex-wrap: wrap; margin: 16px 0; }
  button, a.btn { border-radius: 15px; padding: 8px 16px; font-size: 13px; text-decoration: none; display: inline-block; }
  .signup { background: #ff0357; color: #fff; border: 2px solid #ff035778; }
  .cta { background: #fff; color: #000; font-weight: 600; padding: 16px 24px; border: 0; }
  .login { background: transparent; color: #ffffffcc; border: 2px solid transparent; }
  p.note { color: #c9c9c9; max-width: 62ch; }
</style>
</head>
<body>
<main>
  <h1>Modyfi</h1>
  <p class="note">Rendered from tokens.json. Values were read from the Wayback replay of www.modyfi.com on 2026-11-19. The live site is a Webflow 404. One theme.</p>
  <h2>Colour</h2>
  <div class="swatches">
"""
for name, hx in colors:
    html += f'    <div class="swatch"><div class="chip" style="background:{hx}"></div><div class="meta"><b>{name}</b>{hx}</div></div>\n'
html += """  </div>
  <h2>Type</h2>
  <p style="font-size:56px;line-height:67.2px;letter-spacing:-3px;font-weight:600;margin:0">Design without limits</p>
  <p style="font-size:48px;line-height:57.6px;letter-spacing:-1px;font-weight:600">Explore what the community has been making</p>
  <p style="font-size:17.6px;line-height:31.68px;letter-spacing:-1px;color:#c9c9c9;max-width:42ch">Modyfi is the design platform built for multidisciplinary designers.</p>
  <h2>Controls</h2>
  <div class="row">
    <a class="btn signup" href="#signup">Sign up</a>
    <a class="btn login" href="#login">Log in</a>
    <a class="btn cta" href="#cta">Start playing for free</a>
  </div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
