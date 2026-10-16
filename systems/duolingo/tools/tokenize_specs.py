#!/usr/bin/env python3
"""Write the component specs in tokens (2026-10 refresh).

The specs in components/core.md, components/product.md and their JSON twins name every colour
as '#HEX (palette-name, theme)'. This puts the token in front of each one: the semantic role in
tokens.json that aliases that palette entry in that theme, chosen by what the spec row says the
colour is for (a border, a fill, a label), or the core palette token when no semantic role
uses the colour. '#E5E5E5 (swan, light)' in a 'field border' row becomes
'`border.default` #E5E5E5 (swan, light)'. The raw value stays beside the token as the evidence.
Idempotent: a colour that already has a token in front of it is left alone.

    python3 tools/tokenize_specs.py && python3 tools/build_components_md.py
"""
import json, pathlib, re

PKG = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((PKG / "tokens.json").read_text())

# palette name -> semantic paths that alias it, per theme (ramps are a re-listing of the palette, so they are skipped)
ALIAS = {"light": {}, "dark": {}}
def walk(node, path, th):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            m = re.fullmatch(r"\{palette\.(light|dark)\.([a-z0-9-]+)\}", str(v["$value"]))
            if m and not path[:1] == ["ramp"]:
                ALIAS[th].setdefault(m.group(2), []).append(".".join(path + [k]))
        elif isinstance(v, dict):
            walk(v, path + [k], th)
for th in ("light", "dark"):
    walk(T[th], [], th)

ROLE = [  # (words in the spec's role text, path patterns preferred, in order)
    (r"border|lip|stroke|divider|outline|ring|rule|edge|underline", [r"^border\.", r"^accent\.[a-z]+\.(lip|border)$", r"^status\.\w*Border$", r"^feedback\.tile\.\w*Border$", r"^gamification\.super\.lip$"]),
    (r"text|label|title|body|value|placeholder|caret|count|colou?r|icon|link|heading|caption|glyph|chevron|number|name|copy|word", [r"^text\.", r"^accent\.[a-z]+\.text$", r"^status\.\w*Text$", r"^feedback\.\w+\.text$", r"^feedback\.tile\.\w*Text$", r"^gamification\."]),
    (r"fill|background|bg|face|surface|track|shell|card|container|dot|item|tile|banner|scrim|backdrop|row|bar|panel|bubble|button", [r"^surface\.", r"^background\.", r"^accent\.[a-z]+\.face$", r"^status\.\w*Background$", r"^feedback\.\w+\.(background|buttonFace)$", r"^dataViz\.", r"^gamification\.", r"^unitColors\."]),
]
ORDER = ["text.", "border.", "surface.", "background.", "accent.", "status.", "feedback.", "gamification.", "dataViz.", "unitColors."]

def pick(name, theme, role):
    cands = ALIAS[theme].get(name, [])
    role = role.lower()
    for words, pats in ROLE:
        if re.search(words, role):
            for p in pats:
                hit = [c for c in cands if re.search(p, c)]
                if hit:
                    return hit[0]
    for pre in ORDER:
        hit = [c for c in cands if c.startswith(pre)]
        if hit:
            return hit[0]
    return f"palette.{theme}.{name}"

HEX = re.compile(r"(?<!` )(#[0-9A-Fa-f]{6}) \(([a-z0-9-]+)(?: = [a-z0-9-]+)?, (light|dark)\)")

def tokenize_segment(text, role_of):
    out, last = [], 0
    for m in HEX.finditer(text):
        out.append(text[last:m.start()] + f"`{pick(m.group(2), m.group(3), role_of(m.start()))}` ")
        last = m.start()
    out.append(text[last:])
    return "".join(out)

def inline_role(text):
    # outside a table the role is the text since the last list separator before the colour
    return lambda i: text[max(text.rfind(s, 0, i) for s in (";", "\n", ":", "<br>", "(")) + 1:i]

def tokenize(text):
    """Markdown or a JSON string. In a table row the role is the row's first cell plus the
    column header (the button table names its columns Face, Lip, Border, Label)."""
    lines, header = text.split("\n"), None
    for n, line in enumerate(lines):
        if not line.startswith("|"):
            header = None
            lines[n] = tokenize_segment(line, inline_role(line))
            continue
        cells = line.split("|")
        if header is None:
            header = cells
            continue
        if set(line) <= set("|- :"):
            continue
        def role_of(i, cells=cells, line=line):
            col = line.count("|", 0, i) 
            head = header[col] if col < len(header) else ""
            return cells[1] + " " + head + " " + inline_role(cells[col] if col < len(cells) else "")(len(cells[col]) if col < len(cells) else 0)
        lines[n] = tokenize_lengths(tokenize_segment(line, role_of), header)
    return "\n".join(lines)

# Lengths: in a table row about radius, spacing or border width, a px value that equals a core
# token of that group gets the token in front ('16px' in a radius row becomes '`radius.16` 16px').
# Heights and widths stay raw: several size tokens share a value and the row does not say which.
CORE = T["core"]
SCALES = [
    (r"radius|corner", "radius"),
    (r"padding|gap|margin|offset|spacing|inset", "space"),
    (r"border(?!-?radius)|stroke|rule|divider|grid line", "borderWidth"),
]
PX = re.compile(r"(?<![`\w.-])(?<!` )(\d+)px\b")

def tokenize_lengths(line, header):
    """Only in measurement tables (a 'Property' column), and never inside a quoted CSS rule or a source cell."""
    if not header or not any(h.strip() == "Property" for h in header) or not line.startswith("|") or set(line) <= set("|- :"):
        return line
    cells = line.split("|")
    pcol = [h.strip() for h in header].index("Property")
    prop = " ".join(cells[1:pcol + 1]).lower()
    for words, group in SCALES:
        if re.search(words, prop) and "css" not in prop:
            values = {v["$value"]: k for k, v in CORE[group].items() if isinstance(v, dict) and "$value" in v}
            def sub(m, group=group, values=values):
                k = values.get(m.group(0))
                return f"`{group}.{k}` {m.group(0)}" if k else m.group(0)
            for i in range(pcol + 1, len(cells)):
                head = header[i].strip() if i < len(header) else ""
                if head == "Source" or "css:" in cells[i] or "{" in cells[i] or "captured" in cells[i]:
                    continue
                cells[i] = PX.sub(sub, cells[i])
            return "|".join(cells)
    return line

def tokenize_json(v):
    if isinstance(v, str):
        return tokenize(v)
    if isinstance(v, list):
        return [tokenize_json(x) for x in v]
    if isinstance(v, dict):
        return {k: tokenize_json(x) for k, x in v.items()}
    return v

n = 0
for md in ("components/core.md", "components/product.md"):
    p = PKG / md
    before = p.read_text()
    after = tokenize(before)
    tokref = re.compile(r"`[a-zA-Z]+\.[\w.-]+` (?=#|\d)")
    n += len(tokref.findall(after)) - len(tokref.findall(before))
    p.write_text(after)
for js in ("components/core.json", "components/product.json"):
    p = PKG / js
    d = json.loads(p.read_text())
    p.write_text(json.dumps(tokenize_json(d), indent=1, ensure_ascii=False))
print("tokens placed in front of", n, "values")
