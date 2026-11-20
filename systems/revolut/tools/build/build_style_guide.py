#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Light and dark, no invented values."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def swatches(theme):
    group = TOKENS[theme]
    names = ("background", "foreground", "accent", "black", "white", "grey.50", "grey.2",
             "grouped.background", "danger", "success", "warning", "positive")
    return [(name, group[name]["$value"]) for name in names]


def type_rows():
    rows = []
    for name, tok in TOKENS["core"]["typography"].items():
        v = tok["$value"]
        rows.append((name, v["fontSize"], v["fontWeight"], v["lineHeight"]))
    return rows


def html():
    def chips(theme):
        bits = []
        for name, value in swatches(theme):
            bits.append(
                f'<div class="chip"><i style="background:{value}"></i>'
                f'<span>{name}</span><code>{value}</code></div>'
            )
        return "\n".join(bits)

    types = "\n".join(
        f'<div class="type" style="font-size:{size}"><b>{name}</b> {size} / {lh} weight {weight}</div>'
        for name, size, weight, lh in type_rows()
    )
    radii = "\n".join(
        f'<div class="rad" style="border-radius:{tok["$value"]}"><span>{name}</span><code>{tok["$value"]}</code></div>'
        for name, tok in TOKENS["core"]["radius"].items()
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Revolut public surfaces</title>
<style>
  :root {{ color-scheme: light; font-family: -apple-system, system-ui, Segoe UI, Roboto, Helvetica, Arial, sans-serif; }}
  body {{ margin: 0; background: #f7f7f7; color: #1f1f1f; }}
  header, main {{ max-width: 960px; margin: 0 auto; padding: 32px 20px; }}
  h1 {{ font-weight: 500; letter-spacing: -0.02em; font-size: 40px; margin: 0 0 8px; }}
  p {{ line-height: 1.4; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; }}
  button, .btn {{ border: 0; border-radius: 9999px; padding: 10px 24px; font-size: 16px; font-weight: 500; }}
  .login {{ background: #000; color: #fff; }}
  .signup {{ background: #fff; color: #000; }}
  .download {{ background: #1f1f1f; color: #fff; }}
  section {{ margin: 28px 0; }}
  h2 {{ font-size: 20px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 8px; }}
  .chip {{ display: flex; gap: 8px; align-items: center; background: #fff; border-radius: 12px; padding: 8px; }}
  .chip i {{ width: 28px; height: 28px; border-radius: 8px; border: 1px solid rgba(0,0,0,.08); display: block; }}
  .chip code, .rad code {{ font-size: 12px; }}
  .dark {{ background: #000; color: #fff; border-radius: 16px; padding: 20px; }}
  .dark .chip {{ background: #191c1f; color: #fff; }}
  .rad {{ width: 88px; height: 56px; background: #234fa6; color: #fff; display: flex; flex-direction: column; justify-content: flex-end; padding: 6px; font-size: 11px; }}
  .type b {{ display: inline-block; min-width: 180px; font-weight: 500; }}
  nav {{ display: flex; gap: 8px; margin: 16px 0; }}
</style>
</head>
<body>
<header>
  <h1>Revolut</h1>
  <p>Public signed-out surfaces, measured 2026-11-19. Values come from tokens.json. Aeonik Pro and Inter are named in the tokens and are not loaded here.</p>
  <nav>
    <span class="btn login">Log in</span>
    <span class="btn signup">Sign up</span>
    <span class="btn download">Download the app</span>
  </nav>
</header>
<main>
  <section>
    <h2>Light colours</h2>
    <div class="grid">{chips("light")}</div>
  </section>
  <section class="dark">
    <h2>Dark colours</h2>
    <div class="grid">{chips("dark")}</div>
  </section>
  <section>
    <h2>Type scale</h2>
    {types}
  </section>
  <section>
    <h2>Radii</h2>
    <div class="row">{radii}</div>
  </section>
</main>
</body>
</html>
"""


if __name__ == "__main__":
    (HERE / "style-guide.html").write_text(html())
    print("wrote style-guide.html")
