#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Light values sit on :root. Dark values sit on [data-theme="dark"]. The toggle
sets that attribute. Poppins is named but not shipped; the page falls back to
the system sans.
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


def alias(v, theme):
    def repl(m):
        name = m.group(1)
        if name.startswith("color."):
            name = theme + "." + name
        return f"var({cssname(name)})"
    return re.sub(r"\{([^{}]+)\}", repl, str(v))


def css_val(token, theme):
    v, ty = token["$value"], token["$type"]
    if ty == "typography":
        family = alias(v["fontFamily"], theme)
        return f'{v["fontWeight"]} {v["fontSize"]}/{v["lineHeight"]} {family}'
    if isinstance(v, list):
        return ", ".join(str(x) for x in v)
    return alias(v, theme)


def block(setname, theme):
    return "\n".join(f"  {cssname(n)}: {css_val(t, theme)};" for n, t in flat(T[setname]))


core = block("core", "light")
light = block("light", "light")
dark = block("dark", "dark")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Runey style guide</title>
<style>
:root {{
{core}
{light}
  color-scheme: light;
  --sans: Poppins, ui-sans-serif, system-ui, sans-serif;
}}
[data-theme="dark"] {{
{dark}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--background-page); color: var(--text-primary); font: 400 16px/24px var(--sans); }}
header {{ display: flex; justify-content: space-between; align-items: center; padding: 16px 24px; position: sticky; top: 0; background: var(--background-page); border-bottom: 1px solid var(--border-default); }}
h1 {{ font-size: 18px; font-weight: 600; margin: 0; letter-spacing: -0.03em; }}
main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }}
h2 {{ font-size: 24px; font-weight: 600; letter-spacing: -0.03em; margin: 40px 0 12px; }}
p {{ color: var(--text-muted); max-width: 68ch; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
.sw {{ display: flex; gap: 10px; align-items: center; }}
.sw i {{ width: 40px; height: 40px; border-radius: 12px; border: 1px solid var(--border-default); display: block; }}
.sw b {{ display: block; font-size: 12px; font-weight: 600; }}
.sw span {{ font-size: 12px; color: var(--text-muted); }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin: 12px 0; }}
.btn {{ display: inline-flex; align-items: center; height: var(--size-control-sm); padding: 0 14px; border-radius: var(--radius-control); background: var(--color-primary); color: var(--color-primary-foreground); font-size: 13px; font-weight: 500; text-decoration: none; border: 0; }}
.btn.sec {{ height: var(--size-control-md); background: var(--background-page); color: var(--text-primary); border: 1px solid var(--border-default); font-weight: 600; font-size: 14px; }}
.quiet {{ color: var(--text-primary); text-decoration: none; font-size: 16px; }}
.field {{ height: var(--size-control-md); border-radius: var(--radius-control); border: 1px solid var(--border-default); background: var(--color-card); padding: 0 16px; width: 280px; color: var(--text-muted); display: flex; align-items: center; }}
.card {{ background: var(--background-surface); border: 1px solid var(--border-default); border-radius: var(--radius-card); padding: 16px; max-width: 420px; }}
.toggle {{ border: 1px solid var(--border-default); background: var(--background-surface); color: var(--text-primary); border-radius: 9999px; height: 32px; padding: 0 12px; font: inherit; font-size: 13px; }}
</style>
</head>
<body>
<header>
  <h1>Runey</h1>
  <button class="toggle" type="button" id="theme">Dark tokens</button>
</header>
<main>
  <p>Public marketing site, captured 2026-11-21. Light values were on the page. Dark values were read from the .dark block in the same stylesheet and were not painted on a public page.</p>
  <h2>Colour</h2>
  <div class="swatches" id="swatches"></div>
  <h2>Type</h2>
  <p style="font-size:64px;line-height:67.2px;font-weight:600;letter-spacing:-1.92px;color:var(--text-primary)">Run your business</p>
  <p style="color:var(--text-primary)">Body is Poppins 16/24. The site loads Poppins. This page uses the system fallback when Poppins is not installed.</p>
  <h2>Controls</h2>
  <div class="row">
    <a class="btn" href="#controls">Start for free</a>
    <a class="btn sec" href="#controls">See features</a>
    <a class="quiet" href="#controls">Request demo</a>
  </div>
  <div class="field">Email</div>
  <h2>Card</h2>
  <div class="card">
    <strong>Is Runey free to start?</strong>
    <p>FAQ rows are white cards with a 12px radius on the paper page.</p>
  </div>
</main>
<script>
const roles = [
  ["page", "--background-page"],
  ["surface", "--background-surface"],
  ["text", "--text-primary"],
  ["muted", "--text-muted"],
  ["primary", "--color-primary"],
  ["on accent", "--color-primary-foreground"],
  ["border", "--border-default"],
  ["success", "--color-success"],
  ["warning", "--color-warning"],
  ["danger", "--color-destructive"]
];
const box = document.getElementById("swatches");
for (const [name, variable] of roles) {{
  const el = document.createElement("div");
  el.className = "sw";
  el.innerHTML = "<i></i><div><b></b><span></span></div>";
  el.querySelector("i").style.background = "var(" + variable + ")";
  el.querySelector("b").textContent = name;
  el.querySelector("span").textContent = variable;
  box.appendChild(el);
}}
document.getElementById("theme").addEventListener("click", () => {{
  const on = document.documentElement.getAttribute("data-theme") === "dark";
  document.documentElement.toggleAttribute("data-theme", !on);
  if (!on) document.documentElement.setAttribute("data-theme", "dark");
  else document.documentElement.removeAttribute("data-theme");
}});
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html")
