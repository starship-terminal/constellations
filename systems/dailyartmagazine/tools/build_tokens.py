#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

DailyArt Magazine publishes almost no design-system custom properties.
Values are computed styles read on 2026-11-21. One light theme. Every token
carries $extensions.source. Aliases point at core. Deterministic.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
SPEC = json.loads((HERE / "raw" / "component-tokens.json").read_text())

DIM = re.compile(r"-?\d*\.?\d+(px|rem)")


def norm_color(v):
    v = str(v).strip()
    if v.startswith("{"):
        return v
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", v)
    if m:
        return "#" + m.group(1).lower()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)", v)
    if m:
        return "rgba(%d, %d, %d, %s)" % (int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4))
    raise ValueError("not a colour: " + v)


def emit(path, spec):
    ty = spec["type"]
    if not spec.get("source"):
        raise ValueError(path + ": no source")
    val = spec["value"]
    if ty == "color":
        val = norm_color(val)
    if ty == "dimension" and not (isinstance(val, str) and (val.startswith("{") or DIM.fullmatch(val))):
        raise ValueError(f"{path}: bad dimension {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    node = {
        "$value": val,
        "$type": ty,
        "$extensions": {"source": spec["source"]},
    }
    return node


def walk(group, prefix):
    out = {}
    for key, spec in group.items():
        if "value" in spec and "type" in spec:
            out[key] = emit(prefix + key, spec)
        else:
            out[key] = walk(spec, prefix + key + ".")
    return out


tokens = {
    "core": walk(SPEC["core"], "core."),
    "light": walk(SPEC["light"], "light."),
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}
# resolve aliases exist
names = set()

def collect(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            names.add(prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")

collect(tokens["core"])
collect(tokens["light"])
alias = re.compile(r"\{([^{}]+)\}")

def check_aliases(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            val = v["$value"]
            if isinstance(val, str):
                for ref in alias.findall(val):
                    if ref not in names and not any(n.endswith("." + ref) or n == ref for n in names):
                        # aliases are unprefixed and resolve against core then the set
                        if ref not in names and ("color." + ref) not in names:
                            # stored as {color.crimson} or {font.sans}
                            if ref not in names:
                                raise SystemExit(f"{prefix}{k} alias {{{ref}}} missing")
            if isinstance(val, dict):
                for part in val.values():
                    if isinstance(part, str):
                        for ref in alias.findall(part):
                            if ref not in names:
                                raise SystemExit(f"{prefix}{k} alias {{{ref}}} missing")
        elif isinstance(v, dict):
            check_aliases(v, prefix + k + ".")

check_aliases(tokens)
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
print("tokens", sum(1 for _ in names))
