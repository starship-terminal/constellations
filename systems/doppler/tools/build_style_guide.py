#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Self-contained. No external fonts."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from flat(v, path)


def resolve(value, table, seen=None):
    seen = seen or set()
    if not isinstance(value, str) or not value.startswith("{"):
        return value
    key = value.strip("{}")
    if key in seen:
        return value
    tok = table.get(key)
    if not tok:
        return value
    return resolve(tok["$value"], table, seen | {key})


core = dict(flat(T["core"]))
dark = dict(flat(T["dark"]))
light = dict(flat(T["light"]))
joined = {**core, **dark}

def R(path):
    tok = joined.get(path) or core.get(path) or dark.get(path)
    if not tok:
        return ""
    return resolve(tok["$value"], {**core, **dark})

page = R("background.page") or "#1c1624"
text = R("text.primary") or "#f1f0ec"
accent = R("accent.default") or "#00f575"
hover = R("accent.hover") or "#00c05b"
on_accent = R("text.on-accent") or "#1c1624"
docs_page = "#ffffff"
docs_ink = "#32343a"

swatches = [
    ("Warm black", R("palette.warm-black")),
    ("Warm white", R("palette.warm-white")),
    ("Fluorescent green", R("palette.fluorescent-green")),
    ("Green hover", R("palette.green-hover")),
    ("Purple", R("palette.purple")),
    ("Light purple", R("palette.light-purple")),
    ("Carmine", R("palette.carmine")),
    ("Lilac", R("palette.lilac")),
    ("Factory yellow", R("palette.factory-yellow")),
    ("Docs ink", R("palette.docs-ink")),
    ("Focus blue", R("palette.focus-blue")),
]

swatch_html = "\n".join(
    f'<div class="sw"><i style="background:{v}"></i><div><b>{n}</b><span>{v}</span></div></div>'
    for n, v in swatches if v
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Doppler style guide</title>
<style>
  :root {{
    --page: {page};
    --text: {text};
    --accent: {accent};
    --hover: {hover};
    --on-accent: {on_accent};
    --docs-page: {docs_page};
    --docs-ink: {docs_ink};
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/24px system-ui, sans-serif; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 48px 24px 96px; }}
  h1 {{ font-weight: 450; font-size: 48px; line-height: 1.2; letter-spacing: -0.02em; margin: 0 0 8px; }}
  h2 {{ font-size: 14px; letter-spacing: 0.08em; text-transform: uppercase; font-weight: 400; opacity: 0.7; margin: 48px 0 12px; }}
  p {{ max-width: 62ch; }}
  .row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
  .sw {{ display: flex; gap: 10px; align-items: center; min-width: 200px; }}
  .sw i {{ width: 36px; height: 36px; border-radius: 8px; display: block; border: 1px solid rgba(241,240,236,0.2); }}
  .sw b {{ display: block; font-weight: 400; font-size: 14px; }}
  .sw span {{ font-size: 12px; opacity: 0.7; }}
  .btn {{ display: inline-flex; align-items: center; height: 32px; padding: 8px 12px; border-radius: 12px; background: var(--accent); color: var(--on-accent); text-decoration: none; }}
  .btn.secondary {{ background: transparent; color: var(--text); border: 1px solid var(--text); height: auto; padding: 10px 16px; }}
  .docs {{ margin-top: 16px; background: var(--docs-page); color: var(--docs-ink); border-radius: 12px; padding: 24px; }}
  .docs h3 {{ margin: 0 0 8px; font-size: 31px; line-height: 1.28; }}
  code {{ font-size: 13px; }}
</style>
</head>
<body>
<main>
  <h1>Doppler</h1>
  <p>Public marketing site, one dark theme. Docs are a separate light chrome. Values come from computed styles on 2026-11-21. Take numbers from tokens.json.</p>
  <h2>Palette</h2>
  <div class="row">
    {swatch_html}
  </div>
  <h2>Buttons</h2>
  <div class="row">
    <a class="btn" href="#primary">Start for Free</a>
    <a class="btn secondary" href="#secondary">Get Demo</a>
  </div>
  <p>Primary fill {accent}, hover {hover}, label {on_accent}, radius 12px. Secondary is a 1px warm-white outline.</p>
  <h2>Docs chrome</h2>
  <div class="docs">
    <h3>Welcome</h3>
    <p>docs.doppler.com paints a white page and ink type. No theme toggle was found.</p>
  </div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
