#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Light only: no dark theme was applied."""
import json, pathlib, re

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
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))

def alias(v):
    if isinstance(v, (dict, list)):
        return json.dumps(v)
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))

def css_val(token):
    v = token["$value"]
    kind = token.get("$type")
    if kind == "shadow" and isinstance(v, dict):
        return f"{v['offsetX']} {v['offsetY']} {v['blur']} {v['spread']} {alias(v['color'])}"
    if isinstance(v, dict) and "fontSize" in v:
        fam = alias(v["fontFamily"])
        return f"{v.get('fontWeight', 400)} {v['fontSize']}/{v.get('lineHeight', 'normal')} {fam}"
    return alias(v)

core = "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T["core"]))
light = "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T["light"]))

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SpatialChat style guide</title>
<style>
:root {{
{core}
{light}
  color-scheme: light;
  --sg-sans: "Satoshi", ui-sans-serif, system-ui, sans-serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--background-page); color: var(--text-primary); font: 500 16px/24px var(--sg-sans); }}
.wrap {{ max-width: 1100px; margin: 0 auto; padding: 32px 24px 64px; }}
h1 {{ font-size: 32px; font-weight: 700; margin: 0 0 8px; }}
h2 {{ font-size: 20px; margin: 36px 0 12px; }}
p {{ color: var(--text-muted); max-width: 70ch; }}
.row {{ display: flex; flex-wrap: wrap; gap: 16px; }}
.sw {{ width: 140px; }}
.sw i {{ display: block; height: 64px; border-radius: 12px; border: 1px solid var(--border-default); }}
.sw b {{ display: block; font-size: 12px; margin-top: 6px; }}
.btn {{ display: inline-flex; align-items: center; justify-content: center; height: var(--size-button); padding: 12px 24px; border-radius: var(--radius-control); background: var(--action-primary); color: var(--text-on-accent); border: 1px solid var(--border-accent); font: 500 16px/24px var(--sg-sans); text-decoration: none; }}
.btn.secondary {{ background: transparent; color: var(--text-primary); border-color: var(--border-strong); }}
.card {{ background: var(--component-card-bg); border: 1px solid var(--border-default); border-radius: var(--component-card-radius); padding: 16px; width: 280px; }}
.field {{ display: block; width: 280px; height: 48px; border-radius: 12px; border: 1px solid var(--border-accent); padding: 4px 16px; font: 400 16px/22px var(--sg-sans); }}
.badge {{ display: inline-block; background: var(--component-badge-bg); color: var(--component-badge-text); border-radius: 8px; padding: 6px 10px; font-size: 14px; }}
.tab {{ display: inline-flex; align-items: center; height: 56px; padding: 14px 24px; border-radius: 12px; background: var(--component-tab-bg); color: #fff; box-shadow: var(--shadow-tab); }}
</style>
</head>
<body>
<div class="wrap">
<h1>SpatialChat</h1>
<p>Rendered from tokens.json. Marketing site plus the signed-out login. Light only. Satoshi and Euclid Circular B are not loaded here, so the page falls back to the system face.</p>
<h2>Colour</h2>
<div class="row">
<div class="sw"><i style="background:var(--background-page)"></i><b>page</b></div>
<div class="sw"><i style="background:var(--background-accent)"></i><b>accent</b></div>
<div class="sw"><i style="background:var(--background-continue)"></i><b>continue</b></div>
<div class="sw"><i style="background:var(--background-rail)"></i><b>rail</b></div>
<div class="sw"><i style="background:var(--background-community)"></i><b>community tab</b></div>
<div class="sw"><i style="background:var(--text-primary)"></i><b>text</b></div>
<div class="sw"><i style="background:var(--text-muted)"></i><b>muted</b></div>
</div>
<h2>Controls</h2>
<div class="row">
<a class="btn">Start for Free</a>
<a class="btn secondary">Login</a>
<span class="badge">New</span>
<span class="tab">Virtual Events</span>
</div>
<h2>Field and card</h2>
<div class="row">
<input class="field" placeholder="example@mail.com" aria-label="Email">
<div class="card"><strong>Business</strong><p style="color:var(--text-price);font-size:32px;margin:8px 0">$399</p><a class="btn">Buy Now</a></div>
</div>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html")
