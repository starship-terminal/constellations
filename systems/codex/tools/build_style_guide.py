#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Dark marketing set only, plus the login wall set."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    out = []
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            out.append((path, v))
        elif isinstance(v, dict):
            out.extend(flat(v, path))
    return out


def swatch(path, token):
    val = token["$value"]
    if token.get("$type") == "color":
        return f'<div class="swatch"><i style="background:{val}"></i><code>{path}</code><span>{val}</span></div>'
    return f'<div class="row"><code>{path}</code><span>{val}</span></div>'


dark = "\n".join(swatch(p, t) for p, t in flat(T["dark"]))
core = "\n".join(swatch(p, t) for p, t in flat(T["core"]))
login = "\n".join(swatch(p, t) for p, t in flat(T["login"]))

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Codex public site style guide</title>
<style>
  :root {{ color-scheme: dark; }}
  body {{ margin: 0; background: #000; color: #fff; font: 16px/1.45 "OpenAI Sans", ui-sans-serif, system-ui, sans-serif; }}
  main {{ max-width: 880px; margin: 0 auto; padding: 48px 24px 80px; }}
  h1 {{ font-size: 40px; font-weight: 500; letter-spacing: -0.02em; }}
  h2 {{ font-size: 22px; font-weight: 500; margin-top: 40px; }}
  p {{ color: rgba(255,255,255,.72); max-width: 62ch; }}
  .hero-btns {{ display: flex; gap: 8px; margin: 16px 0 28px; }}
  .btn {{ display: inline-flex; align-items: center; height: 40px; padding: 0 20px; border-radius: 40px; font-size: 14px; font-weight: 500; text-decoration: none; }}
  .btn-primary {{ background: #000; color: #fff; border: 1px solid #fff; }}
  .btn-secondary {{ background: rgba(0,0,0,.04); color: #000; }}
  .wash {{ background: linear-gradient(180deg, #d7e4ff, #efe7ff); color: #000; border-radius: 16px; padding: 28px; }}
  .grid {{ display: grid; grid-template-columns: 1fr; gap: 8px; }}
  .swatch, .row {{ display: grid; grid-template-columns: 48px 1fr auto; gap: 12px; align-items: center; border-top: 1px solid rgba(255,255,255,.12); padding: 8px 0; }}
  .row {{ grid-template-columns: 1fr auto; }}
  .swatch i {{ width: 48px; height: 28px; border-radius: 6px; border: 1px solid rgba(255,255,255,.2); display: block; }}
  code {{ font-size: 13px; }}
  .login {{ margin-top: 12px; background: #000; border: 1px solid rgba(255,255,255,.15); border-radius: 16px; padding: 28px; max-width: 384px; }}
  .login h3 {{ font-weight: 400; font-size: 30px; margin: 0 0 16px; color: #ededed; }}
  .pill {{ height: 52px; border-radius: 9999px; border: 1px solid rgba(255,255,255,.15); display: flex; align-items: center; justify-content: center; margin: 8px 0; color: #ededed; }}
  .pill.go {{ background: #ededed; color: #0d0d0d; border-color: transparent; }}
</style>
</head>
<body>
<main>
  <h1>Codex public site</h1>
  <p>Measured from openai.com/codex on 2026-11-22, signed out. Dark is the only painted marketing theme. The login card is a different host and stays in its own set.</p>
  <div class="wash">
    <h2 style="margin-top:0">Build anything with Codex</h2>
    <div class="hero-btns">
      <a class="btn btn-primary" href="#tokens">Download for macOS</a>
      <a class="btn btn-secondary" href="#tokens">Try on web</a>
    </div>
  </div>
  <h2 id="tokens">Dark marketing tokens</h2>
  <div class="grid">{dark}</div>
  <h2>Core</h2>
  <div class="grid">{core}</div>
  <h2>Login wall</h2>
  <div class="login">
    <h3>Log in or sign up</h3>
    <div class="pill">Continue with Google</div>
    <div class="pill go">Continue</div>
  </div>
  <div class="grid">{login}</div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
