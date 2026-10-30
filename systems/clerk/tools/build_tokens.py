#!/usr/bin/env python3
"""Build Clerk's tokens from sanitized live computed-style readings.

Input: raw/readings/*.json (or raw/*-dark-*.json / *-light-*.json).
Each reading has variables{}, elements[{index, tag, className, styles, rect}],
width, height and theme. No browser, screenshot sampling or network is used.
Optional raw/token-map.json maps semantic paths to {reading, elementIndex,
property}, grouped by theme; these explicit mappings override the defaults.
All captured variables are preserved, including CSS expressions. Only actual
captured themes are emitted. No missing ramp steps or states are invented.
"""
import json
import re
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
COMPONENT_PROPS = {"backgroundColor": "bg", "color": "text", "borderColor": "border",
                   "borderRadius": "radius", "borderWidth": "borderWidth", "height": "height",
                   "width": "width", "padding": "padding", "gap": "gap",
                   "outlineOffset": "outlineOffset", "outline": "outline", "boxShadow": "shadow"}


def leaves(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from leaves(value, prefix + key + ".")


def put(tree, path, value):
    node = tree
    keys = path.split(".")
    for key in keys[:-1]:
        node = node.setdefault(key, {})
    node[keys[-1]] = value


def token(value, kind, source, **extra):
    return {"$value": value, "$type": kind,
            "$extensions": {"source": source, **extra}}


def color(value):
    """Normalize RGB and short hex only; retain modern CSS exactly as captured."""
    match = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", value)
    if match:
        channels = [round(float(x)) for x in match.groups()[:3]]
        if match.group(4) is not None and float(match.group(4)) < 1:
            channels.append(round(float(match.group(4)) * 255))
        return "#" + "".join(f"{x:02x}" for x in channels)
    if re.fullmatch(r"#[0-9a-fA-F]{3,4}", value):
        return "#" + "".join(x * 2 for x in value[1:]).lower()
    return value


def kind_for(name, value):
    if "shadow" in name:
        return "other"  # Preserve complex CSS without pretending it is a parsed shadow.
    if name.startswith(("--color-", "--cl-color-", "--clerk-color-")) or re.match(r"^(#|rgba?\(|lab\(|oklch\(|color-mix\()", value):
        return "color"
    if "font" in name and ("family" in name or name in ("--font-mono", "--font-suisse")):
        return "fontFamily"
    if "weight" in name or name.startswith("--cl-font-") and value.isdigit():
        return "fontWeight"
    if re.fullmatch(r"-?[\d.]+(?:px|rem|em|vh|vw)", value):
        return "dimension"
    if re.fullmatch(r"[\d.]+m?s", value):
        return "duration"
    if re.fullmatch(r"-?[\d.]+", value):
        return "number"
    return "other"


def read_all():
    paths = sorted((RAW / "readings").glob("*.json"))
    if not paths:
        paths = sorted(set(RAW.glob("*-dark-*.json")) | set(RAW.glob("*-light-*.json")))
    readings = []
    for path in paths:
        data = json.loads(path.read_text())
        if not isinstance(data.get("elements"), list) or not isinstance(data.get("variables"), dict):
            continue
        theme_classes = data.get("theme", "").split()
        explicit_themes = {name for name in ("light", "dark") if name in theme_classes}
        filename_theme = next((name for name in ("light", "dark") if f"-{name}-" in path.stem), None)
        if len(explicit_themes) > 1:
            raise ValueError(f"{path.name}: conflicting live root theme classes")
        theme = next(iter(explicit_themes), None) or filename_theme
        if theme is None:
            raise ValueError(f"{path.name}: no recorded theme; refusing to invent one")
        if explicit_themes and filename_theme and theme != filename_theme:
            raise ValueError(f"{path.name}: live theme {theme} contradicts filename {filename_theme}")
        readings.append((path, data, theme))
    if not readings:
        raise SystemExit("No live readings found under raw/readings/*.json")
    return readings


def source(path, data, subject):
    return (f"Measured: {subject}; {path.relative_to(HERE).as_posix()} "
            f"at {data['width']} x {data['height']} CSS px")


def measured(path, data, element, prop):
    value = element["styles"][prop]
    kind = "color" if prop in ("backgroundColor", "color", "borderColor") else "other" if prop in ("outline", "boxShadow") else "dimension"
    if kind == "color":
        value = color(value)
    return token(value, kind, source(path, data, f"computed {prop} of element {element['index']} ({element['tag']})"))


def observation(path, element, prop):
    return {"reading": path.relative_to(HERE).as_posix(), "elementIndex": element["index"], "property": prop}


def count_use(item, path, element, prop):
    extension = item["$extensions"]
    extension["usageCount"] = extension.get("usageCount", 0) + 1
    extension.setdefault("observations", []).append(observation(path, element, prop))


def build():
    readings = read_all()
    core, themed = {}, {}
    for path, data, theme in readings:
        tree = themed.setdefault(theme, {})
        for name, value in sorted(data["variables"].items()):
            if value == "":
                continue
            if name.startswith(("--tw-", "--_")) or re.fullmatch(r"--x[a-z0-9]+", name):
                tree.setdefault("$extensions", {}).setdefault("notTokenised", {}).setdefault("implementationVariables", {})[name] = value
                continue
            kind = kind_for(name, value)
            converted = color(value) if kind == "color" else value
            if kind in ("number", "fontWeight"):
                converted = float(value) if "." in value else int(value)
            # The first reading is stable and later overrides remain in raw evidence.
            put(tree, f"css.{name.removeprefix('--')}", tree.get("css", {}).get(name.removeprefix("--")) or token(
                converted, kind, source(path, data, f"custom property {name} resolved on the document root"), cssProperty=name))
            if name.startswith("--radius-") and kind == "dimension":
                key = name.removeprefix("--radius-")
                core.setdefault("radius", {}).setdefault(key, token(value, kind, source(path, data, f"custom property {name}")))
        for element in data["elements"]:
            styles = element.get("styles", {})
            for prop in ("backgroundColor", "color", "borderColor"):
                if not styles.get(prop):
                    continue
                value = color(styles[prop])
                key = value.lstrip("#") if value.startswith("#") else hashlib.sha256(value.encode()).hexdigest()[:12]
                item = tree.setdefault("observed", {}).setdefault("color", {}).setdefault(key, measured(path, data, element, prop))
                count_use(item, path, element, prop)
            if re.fullmatch(r"[\d.]+px", styles.get("fontSize", "")):
                key = "px" + styles["fontSize"][:-2].replace(".", "_")
                item = core.setdefault("fontSize", {}).setdefault(key, token(styles["fontSize"], "dimension", source(path, data, f"computed fontSize of element {element['index']} ({element['tag']})")))
                count_use(item, path, element, "fontSize")
            for prop in ("padding", "gap"):
                for size in sorted(set(styles.get(prop, "").split())):
                    if re.fullmatch(r"[\d.]+px", size):
                        key = "px" + size[:-2].replace(".", "_")
                        item = core.setdefault("spacing", {}).setdefault(key, token(size, "dimension", source(path, data, f"computed {prop} of element {element['index']} ({element['tag']})")))
                        count_use(item, path, element, prop)
            for size in sorted(set(styles.get("borderRadius", "").split())):
                if re.fullmatch(r"[\d.]+px", size):
                    key = "px" + size[:-2].replace(".", "_")
                    item = core.setdefault("radius", {}).setdefault(key, token(size, "dimension", source(path, data, f"computed borderRadius of element {element['index']} ({element['tag']})")))
                    count_use(item, path, element, "borderRadius")
            type_props = ("fontFamily", "fontSize", "fontWeight", "lineHeight", "letterSpacing")
            if all(styles.get(p) for p in type_props):
                values = {p: styles[p] for p in type_props}
                values["fontWeight"] = int(values["fontWeight"]) if values["fontWeight"].isdigit() else values["fontWeight"]
                # Keep CSS 'normal' intact rather than claiming an unmeasured number.
                key = re.sub(r"[^a-zA-Z0-9_-]", "_", f"text{styles['fontSize']}-w{styles['fontWeight']}-lh{styles['lineHeight']}")
                existing = core.setdefault("typography", {})
                if key in existing and existing[key]["$value"] != values:
                    key += "-" + hashlib.sha256(json.dumps(values, sort_keys=True).encode()).hexdigest()[:8]
                item = existing.setdefault(key, token(values, "typography", source(path, data, f"computed typography of element {element['index']} ({element['tag']})")))
                count_use(item, path, element, "typography")
                family = "mono" if "mono" in styles["fontFamily"].lower() else "sans"
                core.setdefault("fontFamily", {}).setdefault(family, token(styles["fontFamily"], "fontFamily", source(path, data, f"computed fontFamily of element {element['index']} ({element['tag']})")))

    # Semantic roles refer to elements bearing the product's own role classes.
    for theme, tree in themed.items():
        pool = [(p, d, e) for p, d, t in readings if t == theme for e in d["elements"]]
        brand_colors = {color(d["variables"]["--brand"]) for _, d, t in readings if t == theme and d["variables"].get("--brand")}
        roles = {
            "bg.page": (lambda e: e["tag"] == "BODY", "backgroundColor"),
            "bg.surface": (lambda e: e["tag"] == "HEADER" and "application-header-bg" in e.get("className", ""), "backgroundColor"),
            "text.primary": (lambda e: e["tag"] == "BODY", "color"),
            "text.muted": (lambda e: "text-secondary" in e.get("className", ""), "color"),
            "text.secondary": (lambda e: "text-secondary" in e.get("className", ""), "color"),
            "text.onAccent": (lambda e: "bg-brand" in e.get("className", "").split(), "color"),
            "text.link": (lambda e: e["tag"] == "A" and color(e.get("styles", {}).get("color", "")) in brand_colors, "color"),
            "bg.raised": (lambda e: e.get("role") == "dialog" and "bg-main" in e.get("className", "").split(), "backgroundColor"),
            "accent.default": (lambda e: "bg-brand" in e.get("className", "").split(), "backgroundColor"),
            "border.default": (lambda e: e.get("styles", {}).get("borderWidth", "0px") != "0px" and (e["tag"] == "TD" or "border-b" in e.get("className", "").split()), "borderColor"),
        }
        for name, (predicate, prop) in roles.items():
            found = next(((p, d, e) for p, d, e in pool if predicate(e) and prop in e.get("styles", {})), None)
            if found:
                put(tree, name, measured(*found, prop))
        if "default" not in tree.get("border", {}):
            p, d, e = next((p, d, e) for p, d, e in pool if e["tag"] == "BODY")
            put(tree, "border.default", measured(p, d, e, "borderColor"))
    map_path = RAW / "token-map.json"
    if map_path.exists():
        for theme, roles in json.loads(map_path.read_text()).items():
            for name, spec in roles.items():
                path, data, _ = next((p, d, t) for p, d, t in readings if t == theme and p.name == spec["reading"])
                element = next(e for e in data["elements"] if e["index"] == spec["elementIndex"])
                put(themed[theme], name, measured(path, data, element, spec["property"]))
    manifest_path = RAW / "components-manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        for component in manifest["components"]:
            if component.get("status") == "not-captured":
                continue
            for state in component.get("states") or [{"name": "default", **component}]:
                if state.get("observedOnly", component.get("observedOnly")):
                    continue
                filename = state.get("reading", component.get("reading"))
                index = state.get("elementIndex", component.get("elementIndex"))
                path, data, theme = next((p, d, t) for p, d, t in readings if p.name == filename)
                element = next(e for e in data["elements"] if e["index"] == index)
                for prop, target in COMPONENT_PROPS.items():
                    if prop in element["styles"] and element["styles"][prop] not in ("normal", "auto", "none", ""):
                        name = re.sub(r"[^a-zA-Z0-9_-]", "-", state.get("name", "default"))
                        put(themed[theme], f"component.{component['id']}.{name}.{target}", measured(path, data, element, prop))
    themes = [t for t in ("light", "dark") if t in themed]
    result = {"core": core, **{t: themed[t] for t in themes},
              "$themes": [{"id": t, "name": t.title(), "selectedTokenSets": {"core": "source", t: "enabled"}} for t in themes],
              "$metadata": {"tokenSetOrder": ["core", *themes]}}
    (HERE / "tokens.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print("tokens.json:", ", ".join(f"{key} {len(list(leaves(result[key])))}" for key in ("core", *themes)))


if __name__ == "__main__":
    build()
