#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Teachable has one captured theme. The page uses Georgia and system-ui as
stand-ins: Ivypresto Headline, Peridot PE and Reckless are proprietary and
are not loaded.
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
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(token):
    v, ty = token["$value"], token["$type"]
    if ty == "typography":
        return None
    return alias(v)


lines = []
for name, token in flat(T["core"]):
    val = css_val(token)
    if val is not None:
        lines.append(f"  {cssname(name)}: {val};")
for name, token in flat(T["light"]):
    val = css_val(token)
    if val is not None:
        lines.append(f"  {cssname(name)}: {val};")
vars_css = "\n".join(lines)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Teachable style guide</title>
<style>
:root {{
{vars_css}
  --sg-serif: Georgia, "Times New Roman", serif;
  --sg-sans: Arial, system-ui, sans-serif;
  --sg-mono: ui-monospace, Menlo, Consolas, monospace;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--color-bg-page); color: var(--color-text-body); font: 400 16px/1.5 var(--sg-sans); }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
header {{ background: var(--color-bg-nav); color: var(--color-text-onNav); padding: 16px 24px; display: flex; gap: 16px; align-items: center; }}
header a {{ color: inherit; }}
h1 {{ font: 400 40px/1 var(--sg-serif); margin: 0 0 8px; }}
h2 {{ font: 400 32px/1.1 var(--sg-serif); margin: 40px 0 8px; }}
p {{ max-width: 70ch; }}
code {{ font-family: var(--sg-mono); font-size: 12px; }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin: 16px 0; }}
.sw {{ display: flex; gap: 8px; align-items: center; min-width: 220px; }}
.sw i {{ width: 36px; height: 36px; border-radius: 8px; box-shadow: inset 0 0 0 1px #0003; display: block; }}
.btn {{ display: inline-flex; align-items: center; border-radius: var(--component-button-radius); padding: var(--component-button-padding) 22px; background: var(--component-button-background); color: var(--component-button-text); border: 1px solid var(--color-action-fillBorder); font: 600 15px/1 var(--sg-sans); text-decoration: none; }}
.btn.black {{ background: var(--color-action-black); color: var(--color-action-blackText); border-color: var(--color-action-black); }}
.btn.outline {{ background: transparent; color: var(--color-action-outlineText); border-color: var(--color-action-outline); }}
.field {{ width: 280px; height: var(--component-field-height); border-radius: var(--component-field-radius); border: 1px solid var(--color-accounts-inputBorder); padding: var(--component-field-padding) 16px; font: 400 14px/1.5 var(--sg-sans); }}
.login {{ width: 280px; height: var(--component-loginButton-height); border-radius: var(--component-loginButton-radius); background: var(--component-loginButton-background); color: var(--component-loginButton-text); border: 1px solid var(--color-accounts-buttonBorder); font: 400 14px/1 system-ui, sans-serif; }}
.navdemo {{ background: var(--component-nav-background); color: var(--component-nav-text); height: var(--component-nav-height); display: flex; align-items: center; gap: 16px; padding: 0 20px; border-radius: 8px; }}
.card {{ border: 2px solid var(--color-action-plan); border-radius: var(--radius-planFeatured); padding: 16px; width: 240px; }}
.note {{ color: var(--color-text-muted); font-size: 13px; }}
</style>
</head>
<body>
<header>
  <strong>Teachable</strong>
  <span>style guide, light only</span>
</header>
<div class="wrap">
  <h1>Teachable, measured</h1>
  <p>Values come from <code>tokens.json</code>. The public site is Webflow. The signed-out accounts page is a separate Teachable Accounts stylesheet. Ivypresto Headline, Peridot PE and Reckless are not loaded here. Display type uses Georgia. Body type uses Arial.</p>
  <h2>Colour</h2>
  <div class="row">
    <div class="sw"><i style="background:var(--color-bg-page)"></i><span>page<br><code>#ffffff</code></span></div>
    <div class="sw"><i style="background:var(--color-bg-nav)"></i><span>nav<br><code>#000000</code></span></div>
    <div class="sw"><i style="background:var(--color-action-fill)"></i><span>accent<br><code>#e6ff32</code></span></div>
    <div class="sw"><i style="background:var(--color-action-plan)"></i><span>plan<br><code>#1c4774</code></span></div>
    <div class="sw"><i style="background:var(--color-text-muted)"></i><span>muted<br><code>#666666</code></span></div>
    <div class="sw"><i style="background:var(--color-accounts-text)"></i><span>accounts ink<br><code>#212338</code></span></div>
  </div>
  <h2>Type</h2>
  <p style="font:400 48px/1 var(--sg-serif);margin:0">The future of your education business</p>
  <p class="note">h1 is Ivypresto Headline 5rem / 1. This line is Georgia.</p>
  <p style="font:400 19px/1.5 var(--sg-sans)">Body is Peridot PE 1.3rem / 1.5. This line is Arial.</p>
  <h2>Controls</h2>
  <div class="navdemo">
    <span>Pricing</span>
    <span style="text-decoration:underline">Creator login</span>
    <a class="btn outline" href="#components">Contact sales</a>
    <a class="btn" href="#components">Start for free</a>
  </div>
  <div class="row">
    <a class="btn black" href="#components">Explore demo</a>
    <div class="card"><strong>Builder</strong><p>$69/mo</p><a class="btn" style="background:var(--color-action-plan);color:#fff;border-color:var(--color-action-plan)" href="#components">Try for free</a></div>
  </div>
  <h2>Accounts sign-in</h2>
  <p style="font:400 32px/1.5 Palatino, Georgia, serif;margin:0">Log in to Teachable</p>
  <div class="row" style="flex-direction:column;align-items:flex-start">
    <input class="field" placeholder="name@example.com" aria-label="Email">
    <button class="login" type="button">Log In</button>
  </div>
  <p class="note">The accounts button radius is 4px. The marketing pill radius is 900px. They are different controls.</p>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
