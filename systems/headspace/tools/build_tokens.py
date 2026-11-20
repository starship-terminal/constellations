#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from
raw/component-tokens.json (written by build_component_tokens.py) plus the
declared-variable evidence kept in raw/css-vars.json.

headspace.com declares no usable custom-property layer on its signed-out
surfaces (the marketing site compiles to generated Emotion classes; a probe
found zero custom properties applied), so every token carries a *measured*
$extensions.source. The small :root palette vars.mjs found declared in the
served sheets (--orange #ff7e1d, --primary-warm-grey-700, --grey-for-bg and
friends) is emitted inside the `declared` set as css-var provenance.

Sets: core (theme-independent scales), light (the painted palette), org
(the few custom properties the signed-out stylesheets declare on :root).
No dark set exists — no control, no
attribute, no dark media rules applied.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never
tokens.json.
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())
VARS = json.loads((RAW / "css-vars.json").read_text())

TYPE_MAP = {"number": "fontWeight", "string": "other"}


def emit(leaf):
    ty = TYPE_MAP.get(leaf["type"], leaf["type"])
    out = {"$value": leaf["value"], "$type": ty}
    if leaf.get("description"):
        out["$description"] = leaf["description"]
    src = leaf.get("source")
    out["$extensions"] = {"source": src or "measured"}
    return out


def walk(node):
    out = {}
    for k, v in node.items():
        if isinstance(v, dict) and "value" in v:
            out[k] = emit(v)
        elif isinstance(v, dict):
            out[k] = walk(v)
    return out


tokens = {"$metadata": {"tokenSetOrder": ["core", "light", "declared"]}}
for set_name in ("core", "light"):
    tokens[set_name] = walk(SPEC.get(set_name, {}))

# The few custom properties vars.mjs resolved anywhere on the signed-out
# surfaces (expected to be near-empty: the marketing site ships none). They
# land in the `declared` set so the declared layer stays distinct from
# measured values.
declared = {}
for name, rec in sorted((VARS.get("resolved", {}).get("light") or {}).items()):
    key = name.lstrip("-").replace("--", "-").replace("-", "/")
    val = rec.get("value") or rec.get("raw")
    if not val:
        continue
    node = declared
    parts = key.split("/")
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = {"$value": val,
                       "$type": "color" if str(val).startswith(("#", "rgb", "hsl")) else "other",
                       "$description": "A custom property declared by the signed-out surfaces' stylesheets.",
                       "$extensions": {"source": f"css-var {name} (raw/css-vars.json)"}}
tokens["declared"] = declared

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
count = 0
def tally(o):
    global count
    for v in o.values():
        if isinstance(v, dict):
            if "$value" in v: count += 1
            else: tally(v)
for k in ("core", "light", "declared"):
    tally(tokens[k])
print("tokens.json:", count, "tokens")
