#!/usr/bin/env python3
"""Render every token and its evidence, plus actual captured screenshots."""
import html
import json
from pathlib import Path

from build_tokens import leaves

HERE = Path(__file__).resolve().parent.parent


def escape(value):
    return html.escape(str(value), quote=True)


def render_token(path, item):
    value, kind = item["$value"], item["$type"]
    css = ""
    specimen = ""
    if kind == "color":
        css = f"background:{value}"
        specimen = f'<span class="swatch" style="{escape(css)}"></span>'
    elif kind == "typography":
        css = ";".join(f"{key}:{value[prop]}{', system-ui, sans-serif' if prop == 'fontFamily' else ''}" for key, prop in (
            ("font-family", "fontFamily"), ("font-size", "fontSize"),
            ("font-weight", "fontWeight"), ("line-height", "lineHeight"),
            ("letter-spacing", "letterSpacing")))
        specimen = f'<span class="type-demo" style="{escape(css)}">Application settings 012345</span>'
    elif kind == "fontFamily":
        specimen = f'<span style="font-family:{escape(value)}, system-ui, sans-serif">Application settings 012345</span>'
    elif "radius." in path:
        specimen = f'<span class="geometry" style="border-radius:{escape(value)}"></span>'
    elif "spacing." in path:
        specimen = f'<span class="spacing" style="width:{escape(value)}"></span>'
    shown = json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else str(value)
    count = item["$extensions"].get("usageCount")
    usage = f'<small>Usage count: {count} measured element/property occurrences in captured readings. Repeated elements across states count again.</small>' if count is not None else ""
    return (f'<article class="token" data-search="{escape(path.lower())}">'
            f'<code class="name">{escape(path)}</code><span class="kind">{escape(kind)}</span>'
            f'<div class="specimen">{specimen}</div><pre>{escape(shown)}</pre>'
            f'<small>{escape(item["$extensions"]["source"])}</small>{usage}</article>')


def build():
    tokens = json.loads((HERE / "tokens.json").read_text())
    themes = [t["id"] for t in tokens["$themes"]]
    sections = []
    for setname in ("core", *themes):
        rows = list(leaves(tokens[setname]))
        sections.append(f'<section data-set="{setname}"><h2>{setname.title()} <span>{len(rows)} tokens</span></h2>' +
                        "".join(render_token(f"{setname}.{name}", item) for name, item in rows) + "</section>")
    shots = []
    for path in sorted((HERE / "screenshots").rglob("*.png")):
        relative = path.relative_to(HERE).as_posix()
        shots.append(f'<figure><a href="{escape(relative)}"><img loading="lazy" src="{escape(relative)}" alt="{escape(path.stem)}"></a><figcaption>Observed capture: {escape(path.stem)}</figcaption></figure>')
    crops = []
    crop_manifest_path = HERE / "raw" / "crops.json"
    crop_manifest = json.loads(crop_manifest_path.read_text()) if crop_manifest_path.exists() else {}
    for path in sorted((HERE / "components" / "crops").glob("*.png")):
        relative = path.relative_to(HERE).as_posix()
        source = crop_manifest.get(path.name, {}).get("screenshot", "")
        theme = next((t for t in themes if f"-{t}-" in source), "unspecified")
        source_link = f' · <a href="{escape(source)}">Source screenshot</a>' if source else ""
        crops.append(f'<figure class="component-crop" data-capture-theme="{theme}"><a href="{escape(relative)}"><img loading="lazy" src="{escape(relative)}" alt="{escape(path.stem)}, {theme}"></a><figcaption>Observed {theme} crop: {escape(path.stem)}{source_link}</figcaption></figure>')
    template = (HERE / "tools" / "style-guide.template.html").read_text()
    replacements = {
        "TOKENS": "".join(sections), "SCREENSHOTS": "".join(shots),
        "CROPS": "".join(crops),
        "THEME_OPTIONS": "".join(f'<option value="{t}">{t.title()}</option>' for t in themes),
        "INITIAL_THEME": themes[0],
        "THEME_COUNT": str(len(themes)),
        "CAPTURE_NOTE": ("The captured themes are " + ", ".join(themes) + ". " +
                         ("Light was not captured." if "light" not in themes else "Light values come from the captured light state.")),
    }
    for key, value in replacements.items():
        template = template.replace("{{" + key + "}}", value)
    (HERE / "style-guide.html").write_text(template)
    print(f"style-guide.html: {len(shots)} screenshots; every token rendered")


if __name__ == "__main__":
    build()
