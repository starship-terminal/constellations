#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Light only: the signed-out marketing pages did not expose a dark token set.
Colours, radii and type on the page come from tokens.json. Crimson Pro and
Inter are not loaded; the page falls back to Times New Roman and Arial.
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
        seen = seen | {ref}
        if ref.startswith("color.") or ref.startswith("font."):
            return resolve(get("core." + ref), seen)
        return resolve(get(ref), seen)
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
        ("light.background.canvas", "Canvas"),
        ("light.background.surface", "Surface"),
        ("light.background.muted", "Muted surface"),
        ("light.text.primary", "Text"),
        ("light.text.secondary", "Muted text"),
        ("light.text.on-invert", "Text on ink"),
        ("light.border.default", "Border"),
        ("light.border.focus", "Focus"),
        ("light.button.secondary", "Quiet button"),
        ("light.button.dark", "Ink button"),
        ("light.status.approve", "Approve"),
        ("light.status.switch-on", "Switch on"),
        ("light.text.error", "Error text"),
        ("light.text.success", "Success text"),
    ]
    swatches = "\n".join(swatch(p, label) for p, label in roles)
    radii = []
    for key, token in T["core"]["radius"].items():
        radii.append(
            f'<div class="cell"><i style="border-radius:{html.escape(token["$value"])}"></i>'
            f'<span>{html.escape(key)} {html.escape(token["$value"])}</span></div>'
        )
    spaces = []
    for key, token in T["core"]["space"].items():
        spaces.append(
            f'<div class="space"><i style="width:{html.escape(token["$value"])}"></i>'
            f'<span>{html.escape(key)} {html.escape(token["$value"])}</span></div>'
        )
    display = resolve(get("core.font.display"))
    body = resolve(get("core.font.body"))
    page = resolve(get("light.background.page"))
    text = resolve(get("light.text.primary"))
    muted = resolve(get("light.background.muted"))
    ink = resolve(get("light.button.dark"))
    on_ink = resolve(get("light.text.on-invert"))
    radius = resolve(get("core.radius.medium"))
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Workflow style guide</title>
<style>
  :root {{
    --page: {page};
    --text: {text};
    --muted: {muted};
    --ink: {ink};
    --on-ink: {on_ink};
    --radius: {radius};
    --display: {display};
    --body: {body};
  }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 14px/21px var(--body); }}
  main {{ max-width: 880px; margin: 0 auto; padding: 48px 24px 80px; }}
  h1 {{ font: 300 32px/32px var(--display); margin: 0 0 8px; }}
  h2 {{ font: 300 32px/32px var(--display); margin: 40px 0 12px; }}
  p {{ max-width: 62ch; }}
  .swatches, .radii, .spaces {{ display: grid; gap: 12px; }}
  .swatches {{ grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); }}
  .sw {{ display: flex; gap: 12px; align-items: center; }}
  .sw i {{ width: 48px; height: 48px; border-radius: 8px; border: 1px solid rgba(26,26,26,.12); display: block; }}
  .sw b, .sw code, .sw span {{ display: block; }}
  code {{ font: 12px/16px ui-monospace, monospace; }}
  .radii {{ grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); }}
  .cell i {{ display: block; width: 64px; height: 40px; background: var(--muted); border: 1px solid rgba(26,26,26,.2); }}
  .spaces {{ grid-template-columns: 1fr; }}
  .space {{ display: flex; align-items: center; gap: 12px; }}
  .space i {{ height: 12px; background: var(--ink); display: block; }}
  .row {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }}
  .btn {{ display: inline-flex; align-items: center; height: 40px; padding: 8px 16px; border-radius: var(--radius); text-decoration: none; }}
  .quiet {{ background: {muted}; color: {text}; }}
  .dark {{ background: {ink}; color: {on_ink}; }}
  .chip {{ border: 1px solid rgba(26,26,26,.12); border-radius: 9999px; padding: 8px 16px; height: 32px; display: inline-flex; align-items: center; }}
  .approve {{ background: #e9f6ee; color: #547e69; border-radius: 5px; padding: 6px 10px; }}
</style>
</head>
<body>
<main>
  <h1>Workflow</h1>
  <p>Light specimens from the public marketing site, measured 2026-11-19. Crimson Pro and Inter are not loaded here.</p>
  <h2>Colour</h2>
  <div class="swatches">
    {swatches}
  </div>
  <h2>Type</h2>
  <p style="font: 300 32px/32px var(--display)">Design feedback and revisions, all in one place</p>
  <p>Body is 14px Inter with a 21px line. The features page heading computed at 60.992px.</p>
  <h2>Controls</h2>
  <div class="row">
    <a class="btn quiet">Try now</a>
    <a class="btn dark">Get started for free</a>
    <span class="chip">Collecting feedback</span>
    <span class="approve">Approve</span>
  </div>
  <h2>Radius</h2>
  <div class="radii">
    {''.join(radii)}
  </div>
  <h2>Space</h2>
  <div class="spaces">
    {''.join(spaces)}
  </div>
</main>
</body>
</html>
"""
    (HERE / "style-guide.html").write_text(doc)
    print("wrote style-guide.html")


if __name__ == "__main__":
    main()
