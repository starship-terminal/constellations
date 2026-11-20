#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
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
            yield from flat(v, prefix + k + ".")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(token):
    v = token["$value"]
    ty = token.get("$type")
    if isinstance(v, dict) and ty == "shadow":
        return f"{v['offsetX']} {v['offsetY']} {v['blur']} {v['spread']} {v['color']}"
    return alias(v)


lines = []
for path, token in flat(T["core"]):
    lines.append(f"  {cssname('core.' + path)}: {css_val(token)};")
for path, token in flat(T["light"]):
    lines.append(f"  {cssname(path)}: {css_val(token)};")

swatches = []
for path, token in list(flat(T["core"])) + list(flat(T["light"])):
    if token.get("$type") != "color":
        continue
    name = path if path.startswith("color") or "." not in path else path
    var = cssname(path if not path.startswith("color.") else "core." + path) if path.startswith("color.") else cssname(path if path.count(".") else path)
    # use the generated custom property
    full = "core." + path if path.split(".")[0] in T["core"] else path
    swatches.append((path, cssname(full if full.startswith("core") or full.split(".")[0] in T["light"] else "core." + path)))

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Parallel style guide</title>
<style>
:root {{
{chr(10).join(lines)}
  color-scheme: light;
  --sg-sans: var(--core-font-family-primary), ui-sans-serif, system-ui, sans-serif;
  --sg-display: "Iowan Old Style", Palatino, Georgia, serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--surface-page); color: var(--text-primary); font: 400 15px/1.45 var(--sg-sans); }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font-family: var(--sg-display); font-weight: 400; font-size: 48px; letter-spacing: -0.03em; margin: 0 0 8px; }}
h2 {{ font-family: var(--sg-display); font-weight: 400; font-size: 28px; margin: 40px 0 12px; }}
p {{ max-width: 68ch; }}
.pal {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
.sw {{ display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: center; }}
.dot {{ width: 44px; height: 44px; border-radius: 8px; box-shadow: inset 0 0 0 1px rgba(0,0,0,.12); }}
code {{ font-size: 12px; }}
.btn {{ display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border-radius: 999px; background: var(--text-ink); color: var(--surface-white); text-decoration: none; }}
.chip {{ display: inline-flex; height: 36px; padding: 0 14px; border-radius: 999px; border: 1px solid rgba(255,255,255,.35); color: white; background: rgba(255,255,255,.1); }}
.card {{ background: var(--surface-white); border-radius: 16px; padding: 16px; box-shadow: var(--core-shadow-tertiary, 2px 6px 10px rgba(0,0,0,.11)); }}
.hero {{ background: #111; color: var(--text-on-hero); border-radius: 24px; padding: 48px 32px; }}
</style>
</head>
<body>
<div class="wrap">
<h1>Parallel</h1>
<p>Public tokens read from useparallel.com on 2026-11-21. One light theme. Values come from tokens.json, not from the screenshots.</p>
<h2>Colour</h2>
<div class="pal">
"""
for path, token in list(flat(T["core"]["color"])):
    var = cssname("core.color." + path)
    html += f'<div class="sw"><i class="dot" style="background:{var}"></i><div><code>{path}</code><br><code>{token["$value"]}</code></div></div>\n'
html += """</div>
<h2>Roles</h2>
<div class="pal">
"""
for group, items in T["light"].items():
    for path, token in flat(items, group + "."):
        var = cssname(path)
        html += f'<div class="sw"><i class="dot" style="background:{var}"></i><div><code>{path}</code><br><code>{token["$value"]}</code></div></div>\n'
html += """</div>
<h2>Type</h2>
<p class="hero" style="font-family: var(--sg-display); font-size: 64px; line-height: 1.05; letter-spacing: -0.03em;">Find your life's work</p>
<p>Display on the live site is Advercase Demo at 100.8px. That face is not loaded here. The sample uses a serif fallback.</p>
<h2>Controls</h2>
<p><a class="btn" href="#">Sign up</a></p>
<p><span class="chip">Full time</span></p>
<div class="card"><strong>Job card</strong><br>A white card on the app background.</div>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
