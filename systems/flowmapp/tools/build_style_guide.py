#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light is the painted theme."""
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
    return re.sub(r"\{([^{}]+)\}", lambda m: "var(%s)" % cssname(m.group(1)), str(v))


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "shadow":
        return ", ".join(
            "%s %s %s %s %s" % (s["offsetX"], s["offsetY"], s["blur"], s["spread"], alias(s["color"]))
            for s in v
        )
    if ty == "typography":
        return "%s %s/%s %s" % (alias(v["fontWeight"]), alias(v["fontSize"]), alias(v["lineHeight"]), alias(v["fontFamily"]))
    return alias(v)


def block(theme):
    lines = []
    for name, tok in flat(T[theme]):
        lines.append("  %s: %s;" % (cssname(name), css_val(tok)))
    return "\n".join(lines)


html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FlowMapp style guide</title>
<style>
:root {{
{core}
{light}
  --sg-sans: Inter, sans-serif;
}}
[data-mode="dark"] {{
{dark}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font: 400 16px/1.5 var(--sg-sans); color: var(--text); background: var(--page); }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font: 700 40px/1.1 var(--sg-sans); letter-spacing: -0.03em; margin: 0 0 8px; }}
.note {{ color: var(--muted); max-width: 68ch; }}
.row {{ display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0 28px; }}
.sw {{ width: 148px; }}
.dot {{ height: 48px; border-radius: 12px; border: 1px solid rgba(0,0,0,.08); }}
.nm {{ font: 600 12px/1.3 var(--sg-sans); margin-top: 6px; }}
.vl {{ font: 400 11px/1.3 ui-monospace, Menlo, monospace; color: var(--muted); }}
.nav {{ display: flex; align-items: center; gap: 16px; height: 64px; padding: 0 16px; background: white; border-radius: 16px; }}
.sp {{ flex: 1; }}
.btn {{ display: inline-flex; align-items: center; height: 38.5px; padding: 0 16px; border-radius: 12px; font-weight: 600; text-decoration: none; }}
.btn.ghost {{ border: 1px solid rgba(0,0,0,.1); color: black; }}
.btn.black {{ background: black; color: white; }}
.hero {{ margin-top: 28px; text-align: center; }}
.pill {{ display: inline-flex; align-items: center; justify-content: center; min-width: 280px; height: 72px; padding: 0 28px; border-radius: 999px; background: #0080ff; color: white; font-weight: 600; font-size: 22px; box-shadow: 0 8px 10px rgba(0,128,255,.34); }}
table {{ border-collapse: collapse; width: 100%; font-size: 14px; }}
td, th {{ text-align: left; padding: 6px 8px; border-bottom: 1px solid #e6e6e6; }}
</style>
</head>
<body>
<main>
<h1>FlowMapp</h1>
<p class="note">Public marketing tokens read from flowmapp.com on 2026-11-21. The painted site is light. The dark slots below are declared on :root and were not bound on a captured public page. The toggle only swaps those declared slots.</p>
<p><button type="button" id="theme">Show declared dark slots</button></p>
<h2>Painted roles</h2>
<div class="row" id="roles"></div>
<h2>Nav</h2>
<div class="nav"><b>Flowmapp</b><span>Features</span><span>Use cases</span><span>Pricing</span><span class="sp"></span><a class="btn ghost">Log in</a><a class="btn black">Try for free</a></div>
<div class="hero"><a class="pill">Start planning</a></div>
<h2>Token paths</h2>
<table id="tokens"></table>
</main>
<script>
const tokens = {tokens};
const roles = ["page","surface","text","muted","accent","border","destructive","focus"];
const box = document.getElementById("roles");
for (const role of roles) {{
  const el = document.createElement("div");
  el.className = "sw";
  el.innerHTML = '<div class="dot" style="background:var(--'+role+')"></div><div class="nm">'+role+'</div>';
  box.appendChild(el);
}}
const table = document.getElementById("tokens");
function rows(node, prefix) {{
  for (const [k,v] of Object.entries(node)) {{
    if (k.startsWith("$")) continue;
    if (v && v.$value !== undefined) {{
      const tr = document.createElement("tr");
      tr.innerHTML = "<td><code>"+prefix+k+"</code></td><td>"+JSON.stringify(v.$value)+"</td>";
      table.appendChild(tr);
    }} else if (v && typeof v === "object") rows(v, prefix+k+".");
  }}
}}
rows(tokens.light, "light.");
document.getElementById("theme").onclick = () => {{
  const on = document.documentElement.getAttribute("data-mode") === "dark";
  document.documentElement.setAttribute("data-mode", on ? "light" : "dark");
}};
</script>
</body>
</html>
""".format(core=block("core"), light=block("light"), dark=block("dark"), tokens=json.dumps({"light": T["light"], "dark": T["dark"]}))
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
