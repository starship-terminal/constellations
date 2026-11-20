#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Colours come from the tokens file."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def hex_of(node) -> str:
    value = node["$value"]
    if isinstance(value, str) and value.startswith("{"):
        parts = value.strip("{}").split(".")
        cur = json.loads((ROOT / "tokens.json").read_text())
        for part in parts:
            cur = cur[part]
        return hex_of(cur)
    return value


def main() -> None:
    tokens = json.loads((ROOT / "tokens.json").read_text())
    c = tokens["core"]["color"]
    page = hex_of(tokens["light"]["background"]["page"])
    text = hex_of(tokens["light"]["text"]["primary"])
    muted = hex_of(tokens["light"]["text"]["secondary"])
    action = hex_of(tokens["light"]["background"]["action"])
    masthead = hex_of(tokens["light"]["background"]["masthead"])
    surface = hex_of(tokens["light"]["background"]["surface"])
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The New York Times style guide</title>
<style>
:root {{
  --page: {page};
  --text: {text};
  --muted: {muted};
  --action: {action};
  --on-action: {hex_of(tokens["light"]["text"]["on-action"])};
  --masthead: {masthead};
  --surface: {surface};
  --accent: {c["accent"]["$value"]};
  --positive: {c["positive"]["$value"]};
  --hairline: {c["hairline"]["$value"]};
  --serif: Georgia, "Times New Roman", times, serif;
  --sans: Helvetica, Arial, sans-serif;
  color-scheme: light;
}}
body {{ margin: 0; background: var(--page); color: var(--text); font-family: var(--sans); }}
main {{ max-width: 880px; margin: 0 auto; padding: 32px 16px 64px; }}
h1 {{ font-family: var(--serif); font-weight: 300; font-size: 48px; line-height: 52.8px; color: #363636; margin: 0 0 8px; }}
p {{ color: var(--muted); font-family: var(--serif); }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; margin: 16px 0 32px; }}
.swatch {{ width: 120px; }}
.chip {{ height: 64px; border-radius: 3px; border: 1px solid var(--hairline); }}
.meta {{ font-size: 12px; line-height: 16px; margin-top: 6px; }}
button, .ghost {{ font-family: var(--sans); font-size: 16px; font-weight: 600; height: 44px; padding: 0 16px; border-radius: 4px; }}
button.ink {{ background: var(--action); color: var(--on-action); border: 0; }}
.ghost {{ display: inline-flex; align-items: center; background: var(--page); color: var(--text); border: 1px solid var(--text); border-radius: 4px; }}
.mast {{ background: var(--masthead); color: var(--on-action); border: 1px solid #326891; border-radius: 3px; font-size: 11px; font-weight: 700; letter-spacing: 0.55px; text-transform: uppercase; padding: 8px 12px; height: auto; }}
label {{ display: block; font-size: 14px; font-weight: 600; margin-bottom: 4px; }}
input {{ box-sizing: border-box; width: 100%; max-width: 450px; height: 44px; padding: 0 12px; border: 1px solid #000000; border-radius: 3px; font: 500 16px/1 var(--sans); }}
.note {{ font-family: var(--sans); font-size: 14px; color: var(--muted); }}
</style>
</head>
<body>
<main>
<h1>With unlimited access</h1>
<p>Public signed-out tokens from nytimes.com. Proprietary faces are not loaded. Georgia and Helvetica stand in.</p>
<div class="row">
  <div class="swatch"><div class="chip" style="background:{page}"></div><div class="meta">page {page}</div></div>
  <div class="swatch"><div class="chip" style="background:{surface}"></div><div class="meta">surface {surface}</div></div>
  <div class="swatch"><div class="chip" style="background:{text}"></div><div class="meta">text {text}</div></div>
  <div class="swatch"><div class="chip" style="background:{muted}"></div><div class="meta">muted {muted}</div></div>
  <div class="swatch"><div class="chip" style="background:{action}"></div><div class="meta">action {action}</div></div>
  <div class="swatch"><div class="chip" style="background:{masthead}"></div><div class="meta">masthead {masthead}</div></div>
</div>
<button class="ink" type="button">Continue to checkout</button>
<span class="ghost">Continue with Google</span>
<button class="mast" type="button">Subscribe</button>
<p class="note">Log in or create an account</p>
<label for="email">Email address</label>
<input id="email" type="email" name="email" autocomplete="off">
</main>
</body>
</html>
"""
    (ROOT / "style-guide.html").write_text(html)
    print("wrote style-guide.html")


if __name__ == "__main__":
    main()
