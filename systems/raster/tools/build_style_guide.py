#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

The page is dark by default, matching the marketing site. A toggle switches
to the docs light set. Every swatch is a custom property from tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path)


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty in ("typography", "shadow"):
        return None
    if isinstance(v, (list, dict)):
        return None
    return alias(v)


def block(group):
    lines = []
    for name, tok in flat(T[group]):
        val = css_val(tok)
        if val is None:
            continue
        lines.append(f"  {cssname(name)}: {val};")
    return "\n".join(lines)


html = f"""<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Raster style guide</title>
<style>
:root {{
{block("core")}
{block("dark")}
  color-scheme: dark;
}}
[data-mode="docs"] {{
{block("docs")}
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font: 500 14px/1.5 -apple-system, system-ui, sans-serif;
  background: var(--background-page, #000);
  color: var(--text-primary, #fff);
}}
main {{ max-width: 980px; margin: 0 auto; padding: 40px 28px 96px; }}
h1 {{ font-weight: 500; font-size: 36px; letter-spacing: -0.025em; line-height: 1.1; margin: 0 0 8px; }}
h2 {{ font-size: 13px; font-weight: 500; letter-spacing: 0.08em; text-transform: none; margin: 40px 0 12px; color: var(--text-muted, #71717a); }}
p {{ max-width: 68ch; color: var(--text-soft, rgba(255,255,255,.7)); }}
.row {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.sw {{ width: 132px; }}
.sw i {{ display: block; height: 56px; border-radius: 5.25px; border: 1px solid rgba(255,255,255,.12); }}
.sw b, .sw span {{ display: block; font-size: 11px; font-weight: 500; }}
.sw span {{ color: var(--text-muted, #71717a); font-weight: 400; }}
.btn {{
  display: inline-flex; align-items: center; height: 37px; padding: 0 28px;
  border-radius: 5.25px; border: 1px solid rgba(255,255,255,.18);
  background: var(--background-action, #ff2f66); color: #fff; font: 500 14px/1 -apple-system, sans-serif;
  box-shadow: inset 0 0 10px -10px #ff5381;
}}
.btn.sec {{ background: rgba(255,255,255,.08); border-color: rgba(255,255,255,.15); box-shadow: none; }}
.field {{
  height: 37px; width: 240px; border-radius: 5.25px; border: 1px solid rgba(255,255,255,.1);
  background: #27272a; color: #fff; padding: 0 10.5px; font: 400 14px/1 -apple-system, sans-serif;
}}
.tag {{ display: inline-flex; height: 23px; align-items: center; padding: 0 10.5px; border-radius: 9999px; font-size: 10.5px; border: 1px solid rgba(161,161,170,.2); color: #a1a1aa; }}
.tag.solid {{ background: #3f3f46; color: #d4d4d8; border-color: transparent; }}
nav.mock {{ display: flex; align-items: center; gap: 18px; height: 53px; padding: 0 20px; background: rgba(0,0,0,.5); border-bottom: 1px solid rgba(255,255,255,.08); }}
.toggle {{ margin-left: auto; background: transparent; color: inherit; border: 1px solid rgba(255,255,255,.15); border-radius: 5.25px; padding: 4px 10px; }}
</style>
</head>
<body>
<main>
  <nav class="mock">
    <strong>Raster</strong>
    <span>Product</span><span>Pricing</span>
    <button class="toggle" id="theme" type="button">Docs light</button>
  </nav>
  <h1>Raster</h1>
  <p>Public signed-out surfaces, measured 2026-11-19. Marketing is dark. Docs is a separate light surface. Raster Neue is the wordmark face; the page falls back to the system sans because the woff2 is not vendored.</p>
  <h2>Brand</h2>
  <div class="row" id="brand"></div>
  <h2>Gray</h2>
  <div class="row" id="gray"></div>
  <h2>Controls</h2>
  <div class="row">
    <span class="btn">Get started</span>
    <span class="btn sec">Book demo</span>
    <input class="field" placeholder="Work email" readonly>
    <span class="tag">approved</span>
    <span class="tag solid">product-photo</span>
  </div>
  <h2>Type</h2>
  <p style="font-size:36px;line-height:1.1;letter-spacing:-0.025em;color:#fafafa;font-weight:500">The agent-native DAM for teams that ship.</p>
  <p style="font-size:15px">Not only is Raster the fastest DAM on the planet.</p>
</main>
<script>
const T = {json.dumps({"core": T["core"], "dark": T["dark"], "docs": T["docs"]}).replace("<", "\\u003c")};
function swatches(group, root) {{
  const el = document.getElementById(root);
  const node = group.split('.').reduce((o, k) => o[k], T);
  for (const [name, tok] of Object.entries(node)) {{
    if (!tok.$value || tok.$type !== 'color') continue;
    const d = document.createElement('div');
    d.className = 'sw';
    d.innerHTML = '<i></i><b></b><span></span>';
    d.querySelector('i').style.background = tok.$value;
    d.querySelector('b').textContent = name;
    d.querySelector('span').textContent = tok.$value;
    el.appendChild(d);
  }}
}}
swatches('core.color.brand', 'brand');
swatches('core.color.gray', 'gray');
document.getElementById('theme').onclick = () => {{
  const html = document.documentElement;
  const next = html.dataset.mode === 'dark' ? 'docs' : 'dark';
  html.dataset.mode = next;
  document.getElementById('theme').textContent = next === 'dark' ? 'Docs light' : 'Marketing dark';
}};
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
