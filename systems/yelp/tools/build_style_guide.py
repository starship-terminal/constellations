#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: Yelp's public pages
ship one theme. Values are CSS variables generated from the token file."""
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
    if isinstance(v, dict):
        return "{offsetX} {offsetY} {blur} {spread} {color}".format(**{k: alias(x) for k, x in v.items()})
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def block(group, prefix):
    lines = []
    for name, tok in flat(group):
        val = tok["$value"]
        if isinstance(val, dict) and tok.get("$type") == "typography":
            continue
        if isinstance(val, dict) and tok.get("$type") == "shadow":
            val = alias(val)
        else:
            val = alias(val)
        lines.append(f"  {cssname(prefix + name)}: {val};")
    return "\n".join(lines)


CORE = block(T["core"], "")
LIGHT = block(T["light"], "")

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Yelp style guide</title>
<style>
:root {{
{CORE}
{LIGHT}
  --sg-display: var(--font-family-display);
  --sg-ui: var(--font-family-ui);
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--color-bg-default); color: var(--color-text-default); font: 400 16px/24px var(--sg-ui); }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font: 700 32px/40px var(--sg-display); margin: 0 0 8px; }}
h2 {{ font: 700 20px/28px var(--sg-display); margin: 40px 0 12px; }}
p {{ max-width: 68ch; color: var(--color-text-subtle); }}
.row {{ display: flex; flex-wrap: wrap; gap: 16px; }}
.sw {{ width: 148px; }}
.sw i {{ display: block; height: 56px; border-radius: 8px; border: 1px solid var(--color-border-subtle); }}
.sw b, .sw span {{ display: block; font-size: 12px; line-height: 16px; }}
.sw span {{ color: var(--color-text-subtle); }}
.btn {{ display: inline-flex; align-items: center; height: var(--component-signup-height); padding: 8px 16px; border-radius: var(--component-signup-radius); background: var(--component-signup-bg); color: var(--component-signup-text); border: 1px solid var(--component-signup-bg); font: 400 16px/16px var(--sg-ui); text-decoration: none; }}
.btn:focus-visible {{ outline: 2px solid var(--component-focus-outline); outline-offset: 2px; }}
.ghost {{ background: var(--component-login-bg); color: var(--component-login-text); border-color: var(--component-login-bg); border-radius: var(--component-login-radius); }}
.field {{ display: flex; height: var(--component-search-height); border-radius: var(--component-search-radius); box-shadow: var(--shadow-search); overflow: hidden; background: var(--component-search-bg); max-width: 520px; }}
.field input {{ flex: 1; border: 0; padding: 13px 15px; font: 400 16px/20px var(--sg-ui); color: var(--component-search-text); background: transparent; }}
.field button {{ width: 56px; border: 0; background: var(--component-searchButton-bg); color: var(--component-searchButton-text); border-radius: var(--component-searchButton-radius); }}
.chip {{ height: var(--component-chip-height); padding: 7px 11px; border-radius: var(--component-chip-radius); border: 1px solid var(--color-border-default); background: var(--component-chip-bg); color: var(--component-chip-text); font: 600 12px/16px var(--sg-ui); }}
.stars i {{ display: inline-block; width: 20px; height: 20px; border-radius: 4px; margin-right: 2px; }}
</style>
</head>
<body>
<main>
  <h1>Yelp</h1>
  <p>Public signed-out surfaces, measured 2026-11-19. One theme. The red is brand primary. The burst and the wordmark are Yelp's marks and are not redrawn here.</p>
  <h2>Colour</h2>
  <div class="row">
    <div class="sw"><i style="background:var(--color-bg-default)"></i><b>page</b><span>color.bg.default</span></div>
    <div class="sw"><i style="background:var(--color-surface-offset)"></i><b>surface offset</b><span>color.surface.offset</span></div>
    <div class="sw"><i style="background:var(--color-text-default)"></i><b>text</b><span>color.text.default</span></div>
    <div class="sw"><i style="background:var(--color-text-subtle)"></i><b>muted</b><span>color.text.subtle</span></div>
    <div class="sw"><i style="background:var(--color-bg-brandPrimary-strong-default)"></i><b>brand</b><span>color.bg.brandPrimary.strong.default</span></div>
    <div class="sw"><i style="background:var(--color-border-default)"></i><b>border</b><span>color.border.default</span></div>
    <div class="sw"><i style="background:var(--color-link-default)"></i><b>link</b><span>color.link.default</span></div>
    <div class="sw"><i style="background:var(--color-bg-positive-strong)"></i><b>positive</b><span>color.bg.positive.strong</span></div>
  </div>
  <h2>Rating</h2>
  <div class="stars">
    <i style="background:var(--color-rating-one)"></i>
    <i style="background:var(--color-rating-two)"></i>
    <i style="background:var(--color-rating-three)"></i>
    <i style="background:var(--color-rating-four)"></i>
    <i style="background:var(--color-rating-five)"></i>
    <i style="background:var(--color-rating-zero)"></i>
  </div>
  <h2>Controls</h2>
  <div class="row" style="align-items:center">
    <a class="btn" href="#signup">Sign Up</a>
    <a class="btn ghost" href="#login">Log In</a>
    <button class="chip" type="button">Price</button>
  </div>
  <div class="field" style="margin-top:16px">
    <input aria-label="Find" placeholder="things to do, nail salons, plumbers">
    <button type="button" aria-label="Search">Search</button>
  </div>
  <p>Focus on Sign Up, measured on the about page, is a 2px solid outline in the link colour (#007692).</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(HTML)
print("wrote", HERE / "style-guide.html")
