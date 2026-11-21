#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only.

    python3 tools/build_style_guide.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def walk(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path)


def resolve(value, seen=None):
    seen = seen or set()
    if not isinstance(value, str) or not re.fullmatch(r"\{[^{}]+\}", value):
        return value
    path = value[1:-1]
    if path in seen:
        raise SystemExit(f"alias cycle at {path}")
    seen.add(path)
    # Light aliases name a core path (color.paper), not light.color.paper.
    node = T["core"]
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            node = T
            for part in path.split("."):
                node = node[part]
            break
        node = node[part]
    return resolve(node["$value"], seen)


def css_name(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


sets = {name: dict(walk(T[name])) for name in ("core", "light")}
lines = []
for set_name, tokens in sets.items():
    for path, token in tokens.items():
        value = resolve(token["$value"])
        if isinstance(value, list):
            value = "cubic-bezier(" + ", ".join(str(v) for v in value) + ")"
        lines.append(f"  {css_name(set_name + '.' + path)}: {value};")

swatches = []
for path, token in sets["core"].items():
    if token["$type"] != "color":
        continue
    value = resolve(token["$value"])
    label = path.split(".")[-1]
    swatches.append(
        f'<div class="sw"><i style="background:{value}"></i><b>{label}</b><span>{value}</span><span>{path}</span></div>'
    )

type_rows = []
for name, size_path in (
    ("Display", "font.size.display"),
    ("Feature", "font.size.feature"),
    ("Subtitle", "font.size.subtitle"),
    ("Price", "font.size.price"),
    ("Body", "font.size.body"),
    ("Button", "font.size.button"),
):
    size = resolve(sets["core"][size_path]["$value"])
    family = "var(--core-font-family-heading)" if name in ("Display", "Feature") else "var(--core-font-family-body)"
    type_rows.append(
        f'<p class="type" style="font:{size}/1.1 {family}">{name} {size}</p>'
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bear style guide</title>
<style>
:root {{
{chr(10).join(lines)}
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font: 400 var(--core-font-size-body)/var(--core-font-line-height-body) var(--core-font-family-body);
  color: var(--light-text);
  background: var(--light-page);
}}
main {{ max-width: 960px; margin: 0 auto; padding: 48px 32px 80px; }}
h1 {{
  font: 400 var(--core-font-size-display)/1.1 var(--core-font-family-heading);
  margin: 0 0 8px;
  color: var(--light-text);
}}
h2 {{
  font: 400 13px/1 var(--core-font-family-body);
  letter-spacing: 0.04em;
  color: var(--light-muted);
  margin: 40px 0 12px;
}}
.note {{ color: var(--light-muted); max-width: 66ch; }}
.row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 148px; }}
.sw i {{
  display: block;
  height: 56px;
  border-radius: var(--core-radius-button);
  border: 1px solid var(--light-border);
}}
.sw b, .sw span {{ display: block; font: 12px/1.4 ui-monospace, Menlo, monospace; }}
.sw span {{ color: var(--light-muted); word-break: break-all; }}
.type {{ margin: 0 0 8px; color: var(--light-text); }}
.mock {{
  border: 1px solid var(--light-border);
  border-radius: var(--core-radius-card);
  overflow: hidden;
}}
.nav {{
  display: flex;
  align-items: center;
  height: var(--core-space-nav);
  padding: 0 24px;
  background: var(--light-component-nav-background);
  color: var(--light-component-nav-text);
  gap: 20px;
}}
.nav b {{ font-family: var(--core-font-family-heading); }}
.nav span {{ color: var(--light-muted); }}
.hero {{ padding: 40px 32px 32px; }}
.hero h3 {{
  margin: 0;
  font: 400 var(--core-font-size-display)/1.1 var(--core-font-family-heading);
  color: var(--light-text);
}}
.hero p {{ color: var(--light-muted); font-size: var(--core-font-size-subtitle); line-height: 1.4; max-width: 36ch; }}
.btn {{
  display: inline-flex;
  align-items: center;
  padding: var(--core-space-button-y) var(--core-space-button-x);
  border-radius: var(--core-radius-button);
  background: var(--light-accent);
  color: var(--light-on-accent);
  letter-spacing: var(--core-font-letter-spacing-button);
  text-decoration: none;
}}
.card {{
  margin: 0 32px 32px;
  padding: 24px;
  background: var(--light-surface);
  border-radius: var(--core-radius-card);
  color: var(--light-text);
}}
.tags {{ display: flex; gap: 8px; margin-top: 12px; }}
.tag {{
  color: var(--light-on-accent);
  padding: 0 0.3em;
  border-radius: var(--core-radius-tag);
  font-weight: 700;
}}
.offer {{
  background: var(--core-color-offer);
  color: var(--light-text);
  border-radius: var(--core-radius-offer);
  padding: 0 6px;
  font-size: var(--core-font-size-offer);
}}
.focus {{
  outline: 1px auto var(--light-focus);
  outline-offset: 2px;
}}
</style>
</head>
<body>
<main>
  <h1>Bear</h1>
  <p class="note">Generated from tokens.json. Public marketing site, signed out, light only. Bear Sans is not bundled, so this page falls back to the system sans.</p>
  <h2>Colour</h2>
  <div class="row">
    {''.join(swatches)}
  </div>
  <h2>Type</h2>
  {''.join(type_rows)}
  <h2>Chrome</h2>
  <div class="mock">
    <div class="nav"><b>Bear</b><span>Features</span><span>Pricing</span><span>Blog</span></div>
    <div class="hero">
      <h3>Markdown notes</h3>
      <p>Ink on white, one red accent, rounded cards.</p>
      <a class="btn focus">Subscribe</a>
    </div>
    <div class="card">
      Feature card, mist fill, 40px radius.
      <div class="tags">
        <span class="tag" style="background: var(--core-color-gold)">PRO</span>
        <span class="tag" style="background: var(--core-color-sky)">PRO</span>
        <span class="tag" style="background: var(--core-color-accent)">PRO</span>
        <span class="offer">-15%</span>
      </div>
    </div>
  </div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
