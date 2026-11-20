#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light scheme only."""
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
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    if not isinstance(v, str):
        return json.dumps(v)
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", v)


def css_val(token):
    ty = token["$type"]
    val = token["$value"]
    if ty == "typography" and isinstance(val, dict):
        return None
    if ty == "shadow":
        return alias(val)
    if ty == "cubicBezier" and isinstance(val, list):
        return "cubic-bezier(" + ", ".join(str(x) for x in val) + ")"
    if ty == "fontFamily":
        return alias(val)
    if isinstance(val, (int, float)) and ty == "number":
        return str(val)
    return alias(val)


lines = [":root {"]
for prefix, tree in (("core", T["core"]), ("light", T["light"])):
    for name, token in flat(tree):
        path = prefix + "." + name if False else name
        # flatten without set prefix so --text-primary matches light.text.primary's last path
        # Use full path so names cannot collide: --light-text-primary and also short aliases below.
        full = name
        cv = css_val(token)
        if cv is None:
            continue
        lines.append(f"  {cssname(full)}: {cv};")
lines.append("}")

# Short aliases the specimens use, pointing at the flattened names.
aliases = {
    "--page": "var(--background-page)",
    "--surface": "var(--background-surface)",
    "--ink": "var(--text-primary)",
    "--muted": "var(--text-secondary)",
    "--on-accent": "var(--text-onAccent)",
    "--accent": "var(--accent-default)",
    "--border": "var(--border-default)",
    "--linen": "var(--background-linen)",
    "--midnight": "var(--background-midnight)",
    "--sans": "var(--family-sans)",
    "--serif": "var(--family-serif)",
    "--radius-pill": "var(--radius-pill)",
    "--radius-field": "var(--radius-normal)",
    "--header-h": "var(--size-header)",
    "--input-h": "var(--size-inputMin)",
    "--ease": "var(--motion-easing)",
    "--dur": "var(--motion-duration)",
}
lines.append(":root {")
for k, v in aliases.items():
    lines.append(f"  {k}: {v};")
lines.append("}")

css = "\n".join(lines)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wealthsimple style guide</title>
<style>
{css}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--ink); font: 400 18px/1.4 var(--sans); }}
.wrap {{ max-width: 1100px; margin: 0 auto; padding: 48px 24px 80px; }}
h1 {{ font: 500 48px/1.1 var(--sans); margin: 0 0 8px; }}
h2 {{ font: 500 28px/1.2 var(--sans); margin: 40px 0 12px; }}
p {{ max-width: 68ch; color: var(--ink); }}
.note {{ color: var(--muted); font-size: 14px; }}
.row {{ display: flex; flex-wrap: wrap; gap: 16px; align-items: flex-end; }}
.sw {{ width: 120px; }}
.sw i {{ display: block; height: 64px; border-radius: 12px; border: 1px solid var(--border); }}
.sw span {{ display: block; font-size: 12px; margin-top: 6px; }}
.btn {{ display: inline-flex; align-items: center; height: 44px; padding: 12px 16px; border-radius: var(--radius-pill); border: 1.5px solid transparent; font: 500 14px/1 var(--sans); text-decoration: none; }}
.btn.solid {{ background: var(--accent); color: var(--on-accent); }}
.btn.solid:hover {{ background: color-mix(in srgb, var(--accent) 80%, transparent); }}
.btn.line {{ background: transparent; color: var(--ink); border-color: var(--ink); border-radius: var(--radius-pill); }}
.field {{ height: var(--input-h); border-radius: 100px; border: 2px solid var(--border); padding: 0 24px; font: 400 18px/1 var(--sans); background: var(--surface); color: var(--ink); min-width: 280px; }}
.card {{ background: var(--surface); border-radius: var(--radius-field); padding: 24px; box-shadow: var(--elevation-floating); max-width: 360px; }}
.hero {{ background: var(--midnight); color: var(--on-accent); border-radius: 24px; padding: 32px; }}
.hero h3 {{ font: 500 36px/1.1 var(--sans); margin: 0 0 12px; }}
nav.bar {{ display: flex; align-items: center; gap: 16px; background: color-mix(in srgb, var(--surface) 90%, transparent); border-radius: 20px; padding: 12px 16px; }}
nav.bar .logo {{ font: 500 22px/1 var(--serif); }}
nav.bar a {{ color: var(--ink); text-decoration: none; font: 500 14px/1 var(--sans); }}
</style>
</head>
<body>
<div class="wrap">
  <h1>Wealthsimple</h1>
  <p>Public marketing site, measured 2026-11-21. One light scheme. Ink on off-white, pill controls, The Future for UI, Tiempos for editorial headlines. Dark heroes are sections, not a second theme.</p>
  <p class="note">Values come from tokens.json. Proprietary fonts are not loaded here, so the sans and serif fall back.</p>

  <h2>Colour</h2>
  <div class="row">
    <div class="sw"><i style="background:var(--page)"></i><span>page</span></div>
    <div class="sw"><i style="background:var(--surface)"></i><span>surface</span></div>
    <div class="sw"><i style="background:var(--ink)"></i><span>ink</span></div>
    <div class="sw"><i style="background:var(--muted)"></i><span>muted</span></div>
    <div class="sw"><i style="background:var(--linen)"></i><span>linen</span></div>
    <div class="sw"><i style="background:var(--midnight)"></i><span>midnight</span></div>
    <div class="sw"><i style="background:var(--color-terracotta-40)"></i><span>terracotta</span></div>
    <div class="sw"><i style="background:var(--color-celery-40)"></i><span>celery</span></div>
    <div class="sw"><i style="background:var(--color-apricot-60)"></i><span>apricot</span></div>
    <div class="sw"><i style="background:var(--color-sky-50)"></i><span>sky</span></div>
  </div>

  <h2>Type</h2>
  <p style="font:500 64px/1.1 var(--sans);margin:0">More is more</p>
  <p style="font:400 64px/1.15 var(--serif);margin:8px 0">Contact us</p>
  <p style="font:400 18px/1.4 var(--sans)">Body at 18px. The place where saving money could win you $1,000,000 every month.</p>
  <p style="font:500 14px/1.2 var(--sans)">Label 14 / 500 · Get started</p>

  <h2>Controls</h2>
  <div class="row">
    <a class="btn solid" href="#components">Get started</a>
    <a class="btn line" href="#components">Log in</a>
    <input class="field" placeholder="I'm looking for..." aria-label="Search">
  </div>

  <h2>Shell</h2>
  <nav class="bar">
    <span class="logo">Wealthsimple</span>
    <a href="#components">Chequing</a>
    <a href="#components">Trade</a>
    <a href="#components">Credit card</a>
    <span style="flex:1"></span>
    <a class="btn line" href="#components">Log in</a>
    <a class="btn solid" href="#components">Get started</a>
  </nav>
  <div class="hero" style="margin-top:16px">
    <h3>The place where saving money could win you $1,000,000 every month</h3>
    <a class="btn solid" href="#components" style="background:var(--on-accent);color:var(--ink)">Register now</a>
  </div>
  <div class="card" style="margin-top:16px">
    <strong style="font:500 18px/1.2 var(--sans)">Floating panel</strong>
    <p class="note">Menu and search panels use the floating shadow and a 12px radius.</p>
  </div>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
