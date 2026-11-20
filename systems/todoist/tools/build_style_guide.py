#!/usr/bin/env python3
"""Refresh the token parts of style-guide.html from tokens.json.

The page itself is hand-written. This script rewrites the parts that show token values, so they
cannot drift from tokens.json: the Light tokens table (one row per light token, path joined with
"-", a swatch for each colour, aliases resolved) and the primary button's fill
(light.background.action). Deterministic: the same tokens give the same page.
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def lookup(dotted):
    for scope in (T["light"], T["core"], T):
        node = scope
        for part in dotted.split("."):
            node = node.get(part) if isinstance(node, dict) else None
        if isinstance(node, dict) and "$value" in node:
            return node
    raise SystemExit(f"alias {{{dotted}}} resolves nowhere")


def resolve(value, depth=0):
    if depth > 10:
        raise SystemExit("alias loop")
    if isinstance(value, str):
        m = re.fullmatch(r"\{([^{}]+)\}", value)
        if m:
            return resolve(lookup(m.group(1))["$value"], depth + 1)
        return value
    if isinstance(value, dict):
        return {k: resolve(v, depth + 1) for k, v in value.items()}
    return value


def show(value):
    return value if isinstance(value, str) else json.dumps(value)


def render(page):
    rows = []
    for path, tok in walk(T["light"]):
        value = show(resolve(tok["$value"]))
        swatch = (f'<span class="sw" style="background:{html.escape(value, quote=True)}"></span>'
                  if tok["$type"] == "color" else "")
        rows.append(f'<tr><td>{swatch}</td><td><code>{html.escape("-".join(path))}</code></td>'
                    f'<td><code>{html.escape(value)}</code></td></tr>')
    table = "<table>" + "\n".join(rows) + "\n</table>"
    page, n = re.subn(r"<table>.*?</table>", lambda _: table, page, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("token table not found")
    action = resolve(T["light"]["background"]["action"]["$value"])
    page, n = re.subn(r"(\.btn \{ display: inline-block; background: )[^;]+;", lambda m: m.group(1) + action + ";", page, count=1)
    if n != 1:
        raise SystemExit("button rule not found")
    return page


if __name__ == "__main__":
    p = HERE / "style-guide.html"
    p.write_text(render(p.read_text()))
    print("style-guide.html refreshed:", sum(1 for _ in walk(T["light"])), "light tokens")
