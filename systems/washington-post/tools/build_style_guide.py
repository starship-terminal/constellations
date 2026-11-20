#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((HERE / "tokens.json").read_text())


def css_name(path):
    return "--" + path.replace(".", "-")


def emit_colors(group, prefix):
    lines = []
    for key, node in group.items():
        if "$value" in node:
            val = node["$value"]
            if isinstance(val, str) and val.startswith("{"):
                val = "var(" + css_name(val.strip("{}")) + ")"
            lines.append(f"  {css_name(prefix + '.' + key)}: {val};")
        else:
            lines.extend(emit_colors(node, prefix + "." + key))
    return lines


core_lines = []
# fonts, space, radius as variables the specimens use
core_lines.append("  --font-headline: " + TOK["core"]["font"]["headline"]["$value"] + ";")
core_lines.append("  --font-body: " + TOK["core"]["font"]["body"]["$value"] + ";")
core_lines.append("  --font-meta: " + TOK["core"]["font"]["meta"]["$value"] + ";")
core_lines += emit_colors(TOK["core"]["color"], "color")
core_lines += emit_colors(TOK["light"], "light")

css = "\n".join(core_lines)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Washington Post style guide</title>
<style>
:root {{
{css}
  --page: var(--light-page);
  --surface: var(--light-surface);
  --text: var(--light-text);
  --muted: var(--light-muted);
  --accent: var(--light-accent);
  --on-accent: var(--light-onAccent);
  --border: var(--light-border);
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/1.6 Georgia, "Times New Roman", serif; }}
header {{ padding: 20px 28px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: baseline; }}
header h1 {{ font: 700 22px/1.1 Georgia, serif; margin: 0; }}
header p {{ margin: 0; color: var(--muted); font: 400 13px/1.3 system-ui, sans-serif; }}
main {{ max-width: 1040px; margin: 0 auto; padding: 28px; }}
h2 {{ font: 700 20px/1.2 Georgia, serif; margin: 32px 0 12px; }}
.row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 148px; }}
.sw i {{ display: block; height: 48px; border: 1px solid var(--border); }}
.sw span {{ display: block; font: 12px/1.3 ui-monospace, monospace; margin-top: 4px; }}
.btn {{ display: inline-flex; align-items: center; height: 32px; padding: 0 14px; background: var(--accent); color: var(--on-accent); font: 700 14px/1 system-ui, sans-serif; text-decoration: none; border-radius: 9999px; }}
.quiet {{ background: transparent; color: var(--text); border: 1px solid var(--border); }}
.headline {{ font-family: Georgia, "Times New Roman", serif; font-size: 32px; line-height: 1.1; margin: 0; }}
.dek {{ font: 16px/1.4 system-ui, sans-serif; color: var(--muted); }}
.field {{ display: block; width: 280px; height: 40px; border: 0; border-bottom: 1px solid var(--text); font: 16px/1.4 system-ui, sans-serif; background: transparent; }}
.note {{ font: 13px/1.4 system-ui, sans-serif; color: var(--muted); max-width: 70ch; }}
</style>
</head>
<body>
<header>
  <h1>Washington Post</h1>
  <p>Public site, light only. Values from tokens.json.</p>
</header>
<main>
  <h2>Colour</h2>
  <div class="row">
    <div class="sw"><i style="background:var(--page)"></i><span>page</span></div>
    <div class="sw"><i style="background:var(--surface)"></i><span>surface</span></div>
    <div class="sw"><i style="background:var(--text)"></i><span>text</span></div>
    <div class="sw"><i style="background:var(--muted)"></i><span>muted</span></div>
    <div class="sw"><i style="background:var(--accent)"></i><span>accent</span></div>
    <div class="sw"><i style="background:var(--light-opinions)"></i><span>opinions</span></div>
    <div class="sw"><i style="background:var(--light-success)"></i><span>success</span></div>
    <div class="sw"><i style="background:var(--light-warning)"></i><span>warning</span></div>
    <div class="sw"><i style="background:var(--light-danger)"></i><span>danger</span></div>
  </div>
  <h2>Type</h2>
  <p class="headline">Democracy Dies in Darkness</p>
  <p class="dek">Franklin labels, Georgia body, Postoni headlines. Those faces are licensed and not loaded here.</p>
  <h2>Controls</h2>
  <p><a class="btn" href="#subscribe">Save and subscribe</a> <a class="btn quiet" href="#signin">Sign in</a></p>
  <p><input class="field" placeholder="Ask a question or search" aria-label="Search"></p>
  <p class="note">The subscribe control is a blue pill. Section links are black Franklin. Search is an underline field inside the sections drawer. No dark theme was on the public site.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
