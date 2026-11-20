#!/usr/bin/env python3
"""Check systems/patreon/tokens.json against raw/computed.json.

The marketing values were read live from https://www.patreon.com/ on 2026-11-19.
tokens.json is written by hand from those readings; this script does not write it.
It checks every token: each value must appear in raw/computed.json once both are
normalised (hex, rgb(), rgba(), color(srgb ...), seconds to ms, quotes dropped), a font
stack's first family must be the one read, and every alias must resolve. A value no
reading holds is allowed only when its token's capture text says it was entered by hand
at capture time: a Reconstruction token, or one part listed in HAND_PARTS. Aliases are followed
to a final value, so a loop fails. A handful of key roles are also pinned to the exact reading.
"""
import json
import math
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parents[2]  # systems/patreon (this file is tools/build/)
TOKENS = json.loads((HERE / "tokens.json").read_text())
RAW = json.loads((HERE / "raw" / "computed.json").read_text())
HAND = "entered by hand at capture time"
# Parts of an otherwise measured token that were entered by hand; only these are exempt.
HAND_PARTS = {
    "core.typography.nav": {"lineHeight"},  # 13.5px is desktop1440.navButton fontSize; 20.25px was typed
}


def _hex(r, g, b, a=None):
    # Round half up, as browsers do when they paint color(srgb 0.3 ...) as 77, not 76.
    h = "#" + "".join(f"{math.floor(float(x) + 0.5):02x}" for x in (r, g, b))
    if a is not None and float(a) < 1:
        h += f"{math.floor(float(a) * 255 + 0.5):02x}"
    return h


def forms(text):
    """Every normalised form of one raw string: the whole string and each colour, length and time in it."""
    low = str(text).strip().lower()
    out = {low, re.sub(r"[\"']", "", low)}
    out.add(re.sub(r"[\"']", "", low.split(",")[0]).strip())  # a font stack's first family
    for m in re.finditer(r"rgba?\(\s*([\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)(?:\s*[,/]\s*([\d.]+))?\s*\)", low):
        out.add(_hex(*m.groups()))
    for m in re.finditer(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)", low):
        r, g, b, a = m.groups()
        out.add(_hex(float(r) * 255, float(g) * 255, float(b) * 255, a))
    for m in re.finditer(r"#([0-9a-f]{3})\b", low):
        out.add("#" + "".join(c * 2 for c in m.group(1)))
    out.update(m.group(0) for m in re.finditer(r"#[0-9a-f]{6,8}\b", low))
    out.update(m.group(0) for m in re.finditer(r"-?[\d.]+(?:px|ms)\b", low))
    out.update(f"{float(m.group(1)) * 1000:g}ms" for m in re.finditer(r"(-?[\d.]+)s\b", low))
    for m in re.finditer(r"cubic-bezier\(([^)]*)\)", low):
        out.add("cubic-bezier" + repr(tuple(float(n) for n in m.group(1).split(","))))
    return out


def raw_forms():
    acc = set()

    def walk(node):
        if isinstance(node, dict):
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
        else:
            acc.update(forms(node))

    walk(RAW)
    return acc


def leaves(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
    elif isinstance(node, dict):
        for key, child in node.items():
            if not key.startswith("$"):
                yield from leaves(child, f"{path}.{key}" if path else key)


def lookup(set_name, ref):
    for root in (TOKENS.get(set_name, {}), TOKENS["core"]):
        node = root
        for part in ref.strip("{}").split("."):
            node = node.get(part) if isinstance(node, dict) else None
        if isinstance(node, dict) and "$value" in node:
            return node
    return None


def alias_problem(set_name, ref, trail):
    """Follow an alias to a final value, set-first like the catalog: None, or what is wrong."""
    if ref in trail:
        return "alias loop " + " -> ".join(trail + [ref])
    node = lookup(set_name, ref)
    if node is None:
        return f"alias {ref} resolves to nothing"
    value = node["$value"]
    nxt = [value] if isinstance(value, str) else list(value.values()) if isinstance(value, dict) else []
    for v in nxt:
        if isinstance(v, str) and v.startswith("{"):
            found = alias_problem(set_name, v, trail + [ref])
            if found:
                return found
    return None


def capture(token):
    src = token.get("$extensions", {}).get("source", {})
    return src.get("capture", "") if isinstance(src, dict) else str(src)


def values(token, skip=()):
    """The literal values a token carries: a font stack as its first family, a cubicBezier list as
    the cubic-bezier() it was read as, and a composite's parts other than those in `skip`."""
    value = token["$value"]
    if token["$type"] == "fontFamily":
        return [str(value).split(",")[0].strip()]
    if token["$type"] == "cubicBezier" and isinstance(value, list):
        return ["cubic-bezier" + repr(tuple(float(n) for n in value))]
    if isinstance(value, dict):
        return [str(v) for k, v in value.items() if k not in skip and not str(v).startswith("{")]
    if isinstance(value, list) or (isinstance(value, str) and value.startswith("{")):
        return []
    return [str(value)]


def evidence(token):
    src = token.get("$extensions", {}).get("source", {})
    return src.get("evidence", "") if isinstance(src, dict) else ""


def check():
    resolved = RAW["resolved"]
    problems = []
    seen = raw_forms()
    for set_name in ("core", "light", "dark"):
        for path, token in leaves(TOKENS.get(set_name, {})):
            name = f"{set_name}.{path}"
            refs = [token["$value"]] if isinstance(token["$value"], str) else (
                list(token["$value"].values()) if isinstance(token["$value"], dict) else [])
            for ref in refs:
                if isinstance(ref, str) and ref.startswith("{"):
                    found = alias_problem(set_name, ref, ["{" + path + "}"])
                    if found:
                        problems.append(f"{name}: {found}")
            if evidence(token) == "Reconstruction":
                if HAND not in capture(token):
                    problems.append(f"{name}: Reconstruction without saying it was {HAND}")
                continue
            for value in values(token, HAND_PARTS.get(name, ())):
                low = value.lower()
                if not ({low, re.sub(r"[\"']", "", low)} & seen):
                    problems.append(f"{name}: {value} is in no reading in raw/computed.json")
    expect = {
        ("core", "color", "primary"): resolved["--color-primary"],
        ("core", "color", "highlight"): resolved["--color-highlight"],
        ("core", "color", "red"): resolved["--color-red"],
        ("core", "color", "green"): resolved["--color-green"],
        ("core", "color", "yellow"): resolved["--color-yellow"],
    }
    for path, raw in expect.items():
        node = TOKENS
        for part in path:
            node = node[part]
        got = node["$value"].lower()
        if got != raw.lower():
            problems.append(f"{'.'.join(path)} is {got}, reading is {raw}")
    desktop = RAW["computed"]["desktop1440"]
    button = TOKENS["core"]["size"]["button"]["$value"]
    if button != desktop["getStarted"]["height"]:
        problems.append(f"button height {button} != {desktop['getStarted']['height']}")
    if TOKENS["core"]["radius"]["pill"]["$value"] != desktop["getStarted"]["radius"]:
        problems.append("pill radius drifted from the Get Started reading")
    login = RAW["computed"]["login"]
    if TOKENS["core"]["size"]["login-control"]["$value"] != login["continue"]["height"]:
        problems.append("login control height drifted")
    return problems


def main():
    problems = check()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print("tokens.json matches raw/computed.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
