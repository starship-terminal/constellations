#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

The page uses the measured token values only. Franklin, Postoni and Georgia
are named; Franklin and Postoni are proprietary and fall back to the system
sans and to Georgia.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def hex_of(path):
    node = T
    for part in path.split("."):
        node = node[part]
    return node["$value"]


def rows(group, prefix):
    out = []

    def walk(node, path):
        if isinstance(node, dict) and "$value" in node and node.get("$type") == "color":
            out.append((path, node["$value"]))
        elif isinstance(node, dict):
            for key, value in node.items():
                if key.startswith("$"):
                    continue
                walk(value, path + "." + key if path else key)

    walk(group, prefix)
    return out


def swatches(items):
    html = []
    for path, value in items:
        html.append(
            '<div class="sw"><i style="background:%s"></i><div><code>%s</code><span>%s</span></div></div>'
            % (value, path, value)
        )
    return "\n".join(html)


def scale(group, prefix):
    html = []
    for key, token in group.items():
        if not isinstance(token, dict) or "$value" not in token:
            continue
        html.append("<tr><td><code>%s.%s</code></td><td>%s</td></tr>" % (prefix, key, token["$value"]))
    return "\n".join(html)


page = hex_of("dark.page")
surface = hex_of("dark.surface")
text = hex_of("dark.text")
muted = hex_of("dark.muted")
accent = hex_of("dark.accent")
border = hex_of("dark.border")
on_accent = hex_of("dark.on-accent")
light_page = hex_of("light.page")
light_text = hex_of("light.text")
light_muted = hex_of("light.muted")
field = hex_of("light.field-focus")

html = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Washington Post style guide</title>
<style>
:root {
  --page: %(page)s;
  --surface: %(surface)s;
  --text: %(text)s;
  --muted: %(muted)s;
  --accent: %(accent)s;
  --border: %(border)s;
  --on-accent: %(on_accent)s;
  --light-page: %(light_page)s;
  --light-text: %(light_text)s;
  --light-muted: %(light_muted)s;
  --field: %(field)s;
  --sans: Franklin, Franklin-fallback, Arial, Helvetica, sans-serif;
  --serif: Postoni, Postoni-fallback, Georgia, "Times New Roman", serif;
  --body: georgia, "Times New Roman", serif;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--page); color: var(--text); font: 400 16px/1.5 var(--sans); }
main { max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }
h1 { font: 700 32px/1.1 var(--serif); margin: 0 0 8px; }
h2 { font: 700 20px/1.25 var(--sans); margin: 40px 0 12px; }
p { color: var(--muted); max-width: 68ch; }
code { font: 12px/1.4 ui-monospace, SFMono-Regular, Menlo, monospace; }
.swatches { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
.sw { display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: center; }
.sw i { width: 44px; height: 44px; border-radius: 4px; box-shadow: inset 0 0 0 1px var(--border); display: block; }
.sw span, .sw code { display: block; }
.sw span { color: var(--muted); font-size: 12px; }
table { width: 100%; border-collapse: collapse; font-size: 14px; }
td, th { text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--border); vertical-align: top; }
th { color: var(--muted); font-weight: 400; }
.row { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin: 12px 0 20px; }
.pill { display: inline-flex; align-items: center; height: 32px; padding: 8px 16px; border-radius: 9999px; background: var(--accent); color: var(--on-accent); font: 700 16px/16px var(--sans); text-decoration: none; }
.ghost { display: inline-flex; align-items: center; height: 40px; padding: 8px 16px; border-radius: 9999px; color: var(--text); font: 700 16px/16px var(--sans); }
.navpill { display: inline-flex; align-items: center; height: 30px; padding: 8px 16px; border-radius: 9999px; background: var(--page); color: var(--text); font: 700 16px/16px var(--sans); }
.icon { width: 36px; height: 36px; border-radius: 9999px; display: inline-flex; align-items: center; justify-content: center; color: var(--text); font-size: 0; }
.card { width: 460px; max-width: 100%; background: var(--light-page); color: var(--light-text); border: 1px solid #e9e9e9; box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 0px 0px; padding: 16px 0 20px; }
.card .badge { display: inline-block; margin-left: 16px; border: 1px solid #111111; padding: 0 8px 0 4px; font: 700 12px/15px var(--sans); }
.card h3 { margin: 12px 0 8px; padding: 0 24px; font: 700 32px/35.2px var(--serif); color: #2a2a2a; }
.card p { color: var(--light-text); font-size: 12px; line-height: 15px; padding: 0 24px; }
.field { margin: 12px 16px; height: 50px; border: 1px solid var(--field); border-radius: 2px; background: #fff; color: #595959; font: 400 16px/48px var(--sans); padding: 0 8px; }
.next { display: block; margin: 12px 16px; height: 40px; border: 0; border-radius: 9999px; background: var(--accent); color: #fff; font: 700 16px/40px var(--sans); }
.oauth { display: block; margin: 8px 16px; height: 40px; border-radius: 9999px; border: 1px solid rgba(0, 0, 0, 0.1); background: #fff; color: #111; font: 700 16px/40px var(--sans); text-align: center; }
.story { max-width: 640px; }
.story h3 { margin: 0 0 8px; font: 700 26px/28.6px var(--serif); color: #dedede; }
.story .by { color: #a1a1a1; font-size: 14px; line-height: 17.5px; }
.article h3 { margin: 0; font: 700 48px/52.8px var(--serif); }
.article .dek { font: 300 20px/25px var(--sans); color: var(--text); }
.article .body { font: 400 20px/32px var(--body); color: var(--text); max-width: 640px; }
.slogan { font: 400 18px/22.5px Georgia, "Times New Roman", serif; color: #a1a1a1; }
</style>
</head>
<body>
<main>
<h1>The Washington Post</h1>
<p>Public signed-out surfaces, measured on 2026-11-19 from washingtonpost.com with the html class wpds-dark. Franklin and Postoni are the product's fonts and are not loaded here.</p>

<h2>Dark roles</h2>
<div class="swatches">
%(dark)s
</div>

<h2>Light card roles</h2>
<div class="swatches">
%(light)s
</div>

<h2>Core colour</h2>
<div class="swatches">
%(core)s
</div>

<h2>Type</h2>
<div class="story">
<div class="slogan">Democracy Dies in Darkness</div>
<h3>Trump's dream of nuclear deal meets reality of unwilling Russia, China</h3>
<div class="by">By Joshua Keating and Cate Cadell</div>
</div>
<div class="article" style="margin-top:24px">
<div style="font:700 16px/20px var(--sans)">Video Games</div>
<h3>Grand Theft Auto VI is an astonishing American epic</h3>
<p class="dek">The game, a rags-to-riches crime epic in which players pilot both halves of an outlaw couple, is revolutionary because of its attention to human behavior.</p>
<p class="body">Early while playing Grand Theft Auto VI, I caught myself minding my manners.</p>
</div>

<h2>Controls</h2>
<div class="row">
<span class="pill">Save and subscribe</span>
<span class="ghost">Sign in</span>
<span class="navpill">Politics</span>
<span class="icon" aria-hidden="true">search</span>
</div>
<div class="card">
<div class="badge">BLACK FRIDAY SALE</div>
<h3>Black Friday savings: 99 cents USD every four weeks</h3>
<p>Unlimited access on the web and in our apps</p>
<div class="field">Add your email address</div>
<button class="next" type="button">Next</button>
<div class="oauth">Continue with Google</div>
</div>

<h2>Space</h2>
<table><tr><th>Token</th><th>Value</th></tr>%(space)s</table>
<h2>Radius</h2>
<table><tr><th>Token</th><th>Value</th></tr>%(radius)s</table>
<h2>Type scale</h2>
<table><tr><th>Token</th><th>Value</th></tr>%(size)s</table>
</main>
</body>
</html>
"""
repl = {
    "%(page)s": page, "%(surface)s": surface, "%(text)s": text, "%(muted)s": muted,
    "%(accent)s": accent, "%(border)s": border, "%(on_accent)s": on_accent,
    "%(light_page)s": light_page, "%(light_text)s": light_text,
    "%(light_muted)s": light_muted, "%(field)s": field,
    "%(dark)s": swatches(rows(T["dark"], "dark")),
    "%(light)s": swatches(rows(T["light"], "light")),
    "%(core)s": swatches(rows(T["core"]["color"], "core.color")),
    "%(space)s": scale(T["core"]["space"], "core.space"),
    "%(radius)s": scale(T["core"]["radius"], "core.radius"),
    "%(size)s": scale(T["core"]["font"]["size"], "core.font.size"),
}
for key, value in repl.items():
    html = html.replace(key, value)

(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
