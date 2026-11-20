#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Dark only. No catalog lookup."""
import json
import pathlib

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


def css_name(path):
    return "--" + path.replace(".", "-")


def css_value(token):
    v, ty = token["$value"], token["$type"]
    if isinstance(v, str) and v.startswith("{"):
        return "var(%s)" % css_name(v.strip("{}"))
    if ty == "typography":
        return "%s %s/%s var(%s)" % (
            v["fontWeight"],
            v["fontSize"],
            v["lineHeight"],
            css_name(v["fontFamily"].strip("{}")),
        )
    if ty == "shadow":
        s = v
        return "%s %s %s %s %s" % (s["offsetX"], s["offsetY"], s["blur"], s["spread"], s["color"])
    if ty == "fontFamily":
        return v
    return str(v)


lines = [":root {", "  color-scheme: dark;"]
for path, token in list(flat(T["core"])) + list(flat(T["dark"])):
    lines.append("  %s: %s;" % (css_name(path), css_value(token)))
lines.append("}")

swatches = []
for path, token in flat(T["dark"]["color"]):
    swatches.append(
        '<div class="sw"><i style="background:%s"></i><div><code>%s</code><span>%s</span></div></div>'
        % (css_value(token), path, token["$value"])
    )

type_rows = []
for path, token in flat(T["core"]["typography"]):
    v = token["$value"]
    type_rows.append(
        '<div class="ty" style="font:%s"><b>%s</b> %s / %s / %s</div>'
        % (css_value(token), path, v["fontSize"], v["lineHeight"], v["fontWeight"])
    )

html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Prime Video style guide</title>
<style>
%s
* { box-sizing: border-box; }
body { margin: 0; background: var(--color-bg-page); color: var(--color-text-primary); font: 400 14px/20px var(--font-family-base); }
main { max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }
h1 { font: var(--typography-display); margin: 0 0 8px; }
h2 { font: var(--typography-heading); margin: 40px 0 12px; }
p { color: var(--color-text-muted); max-width: 68ch; }
.swatches { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
.sw { display: grid; grid-template-columns: 40px 1fr; gap: 10px; align-items: center; }
.sw i { width: 40px; height: 40px; border-radius: 8px; display: block; box-shadow: inset 0 0 0 1px var(--color-border-card); }
.sw code { display: block; font-size: 12px; }
.sw span { color: var(--color-text-muted); font-size: 12px; }
.ty { margin: 8px 0; }
.row { display: flex; gap: 16px; align-items: center; flex-wrap: wrap; margin: 16px 0; }
.btn { display: inline-flex; align-items: center; height: var(--size-joinHeight); padding: 0 14px; border-radius: var(--radius-control); background: var(--color-accent-default); color: var(--color-text-onAccent); font: var(--typography-button); letter-spacing: 0.64px; box-shadow: var(--shadow-accent); }
.btn.inv { height: var(--size-heroButtonHeight); background: var(--color-bg-buttonInverse); color: var(--color-text-onInverse); box-shadow: none; font: var(--typography-buttonLarge); }
.chip { display: inline-flex; align-items: center; height: var(--size-chipHeight); padding: 0 var(--space-chipPadX); border-radius: var(--radius-chip); background: var(--color-bg-chipSelected); color: var(--color-text-chipSelected); font-weight: 500; }
.field { width: 280px; height: 42px; border-radius: var(--radius-control); background: var(--color-bg-search); color: var(--color-text-primary); padding: 0 16px; display: flex; align-items: center; }
.card { width: 280px; padding: 16px; border-radius: var(--radius-card); background: var(--color-bg-card); border: 1px solid var(--color-border-card); }
.dialog { width: 320px; padding: 20px; border-radius: var(--radius-dialog); background: var(--color-bg-dialog); }
</style>
</head>
<body>
<main>
<h1>Prime Video</h1>
<p>Rendered from tokens.json. Dark only. Amazon Ember is not loaded; the family falls back to Arial, then the system sans.</p>
<h2>Colour</h2>
<div class="swatches">%s</div>
<h2>Type</h2>
%s
<h2>Controls</h2>
<div class="row">
  <span class="btn">Join Prime</span>
  <span class="btn inv">Prime Member? Sign in</span>
  <span class="chip">All</span>
</div>
<div class="row">
  <div class="field">Search</div>
</div>
<div class="row">
  <div class="card"><strong>Content advisory</strong><p>Muted body on a raised card.</p></div>
  <div class="dialog"><strong>Share</strong><p>Dialog radius 24px, page fill.</p></div>
</div>
</main>
</body>
</html>
""" % ("\n".join(lines), "\n".join(swatches), "\n".join(type_rows))

(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
