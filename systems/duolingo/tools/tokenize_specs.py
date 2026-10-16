#!/usr/bin/env python3
"""Write the component specs in tokens (2026-10 refresh).

The specs in components/core.md, components/product.md and their JSON twins name every colour
as '#HEX (palette-name, theme)'. This puts the token in front of each one: the semantic role in
tokens.json that aliases that palette entry in that theme, chosen by what the spec row says the
colour is for (a border, a fill, a label), or the core palette token when no semantic role
uses the colour. '#E5E5E5 (swan, light)' in a 'field border' row becomes
'`border.default` #E5E5E5 (swan, light)'. The raw value stays beside the token as the evidence.
Re-runnable: it first strips its own earlier output, so a rule change regenerates every spec, and a second run changes nothing.

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
                mod = v.get("$extensions", {}).get("studio.tokens", {}).get("modify") or {}
                alpha = float(mod["value"]) if mod.get("type") == "alpha" else None
                ALIAS[th].setdefault(m.group(2), []).append((".".join(path + [k]), alpha))
        elif isinstance(v, dict):
            walk(v, path + [k], th)
for th in ("light", "dark"):
    walk(T[th], [], th)

ROLE = [  # (words in the spec's role text, path patterns preferred, in order)
    (r"border|lip|shadow|stroke|divider|outline|ring|rule|edge|underline", [r"^border\.", r"^accent\.[a-z]+\.(lip|border)$", r"^status\.\w*Border$", r"^feedback\.tile\.\w*Border$", r"^gamification\.super\.lip$"]),
    (r"text|label|title|body|value|placeholder|caret|count|colou?r|icon|link|heading|caption|glyph|chevron|number|name|copy|word", [r"^text\.", r"^accent\.[a-z]+\.text$", r"^status\.\w*Text$", r"^feedback\.\w+\.text$", r"^feedback\.tile\.\w*Text$", r"^gamification\."]),
    (r"fill|background|bg|face|surface|track|shell|card|container|dot|item|tile|banner|scrim|backdrop|row|bar|panel|bubble|button", [r"^surface\.", r"^background\.", r"^accent\.[a-z]+\.face$", r"^status\.\w*Background$", r"^feedback\.\w+\.(background|buttonFace)$", r"^dataViz\.", r"^gamification\.", r"^unitColors\."]),
]
ORDER = ["text.", "border.", "surface.", "background.", "accent.", "status.", "feedback.", "gamification.", "dataViz.", "unitColors."]

def pick(name, theme, role, alpha=None):
    """A token that aliases this palette entry at the same opacity: a colour written with no alpha
    never takes a token that applies one (border.onColor is black at 20%), and '@ 0.4' only takes
    a token at 40% (background.scrim). With no such token the core palette token is used."""
    cands = [c for c, a in ALIAS[theme].get(name, []) if (a is None and alpha is None) or (a is not None and alpha is not None and abs(a - alpha) < 1e-6)]
    if alpha is not None and not cands:
        return f"palette.{theme}.{name}"
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

HEX = re.compile(r"(?<!` )(#[0-9A-Fa-f]{6}) \(([a-z0-9-]+)(?: = [a-z0-9-]+)?(?:, (light|dark))?(?=[,)])")
PAL = T["core"]["palette"]

def theme_of(hex_, name, stated):
    """The theme the spec states, or else the theme whose palette entry of that name has this value."""
    if stated:
        return stated
    for th in ("light", "dark"):
        if PAL[th].get(name, {}).get("$value", "").lower() == hex_.lower():
            return th
    return None

# The other ways the specs write a colour: 'owl #58CC02' and '#000000 @0.40 (black)'.
NAME_HEX = re.compile(r"(?<![`\w-])([a-z][a-z0-9]*(?:-[a-z0-9]+)*):? (#[0-9A-Fa-f]{6})\b")
HEX_ALPHA = re.compile(r"(?<!` )(#[0-9A-Fa-f]{6}) @ ?[\d.]+%? \(([a-z0-9-]+)\)")

# Semantic paths whose value is the same hex in light and in dark (unitColors.blue is macaw in
# both; text.link is not). A colour the spec gives with no theme, in a passage about both
# themes, can only take one of these; otherwise it takes the core palette token.
STABLE = {}
for th in ("light", "dark"):
    for name, paths in ALIAS[th].items():
        for path, a in paths:
            STABLE.setdefault(path, {})[th] = (PAL[th][name]["$value"].lower(), a)

def pick_stable(name, hex_, role, alpha):
    cands = [p for p, v in STABLE.items() if v.get("light") == v.get("dark") == (hex_.lower(), alpha)]
    role = role.lower()
    for words, pats in ROLE:
        if re.search(words, role):
            for pat in pats:
                hit = [c for c in cands if re.search(pat, c)]
                if hit:
                    return hit[0]
    for pre in ORDER:
        hit = [c for c in cands if c.startswith(pre)]
        if hit:
            return hit[0]
    th = theme_of(hex_, name, None)
    return f"palette.{th}.{name}"

def theme_context(text):
    """The theme a passage is about, when it says so ('Tokens (dark):', a Light column, '(dark)')."""
    t = text.lower()
    has_l, has_d = re.search(r"\blight\b", t), re.search(r"\bdark\b", t)
    return "light" if has_l and not has_d else "dark" if has_d and not has_l else None

def tokenize_segment(text, role_of, theme_at=lambda i: None):
    hits = []  # (start, name, hex, stated theme)
    def alpha_after(end):
        a = re.match(r"\)?\s*@\s*([\d.]+)(%?)", text[end:end + 16])
        return (float(a.group(1)) / (100 if a.group(2) else 1)) if a else None
    role_alpha = lambda i: (lambda a: float(a.group(1)) if a else None)(re.search(r"at ([\d.]+) alpha", role_of(i)))
    for m in HEX.finditer(text):
        hits.append((m.start(), m.group(2), m.group(1), m.group(3), alpha_after(m.end()) or role_alpha(m.start())))
    for m in HEX_ALPHA.finditer(text):
        a = re.search(r"@ ?([\d.]+)(%?)", m.group(0))
        hits.append((m.start(), m.group(2), m.group(1), None, float(a.group(1)) / (100 if a.group(2) else 1)))
    for m in NAME_HEX.finditer(text):
        if text[max(0, m.start() - 2):m.start()] != "` ":
            hits.append((m.start(), m.group(1), m.group(2), None, alpha_after(m.end())))
    out, last = [], 0
    for start, name, hex_, stated, alpha in sorted(set(hits), key=lambda h: h[0]):
        if start < last:
            continue
        ctx = None if stated else theme_at(start)
        th = theme_of(hex_, name, stated or (ctx if ctx and PAL[ctx].get(name, {}).get("$value", "").lower() == hex_.lower() else None))
        if th is None or name not in PAL[th]:
            continue
        token = pick(name, th, role_of(start), alpha) if (stated or ctx) else pick_stable(name, hex_, role_of(start), alpha)
        out.append(text[last:start] + f"`{token}` ")
        last = start
    out.append(text[last:])
    return "".join(out)

def inline_role(text):
    # outside a table the role is the text since the last list separator before the colour
    return lambda i: text[max(text.rfind(s, 0, i) for s in (";", "\n", ":", "<br>", "(")) + 1:i]

def tokenize(text, context=""):
    """Markdown or a JSON string. In a table row the role is the row's first cell plus the
    column header (the button table names its columns Face, Lip, Border, Label)."""
    lines, header = text.split("\n"), None
    for n, line in enumerate(lines):
        if not line.startswith("|"):
            header = None
            role = inline_role(line)
            lines[n] = tokenize_segment(line, lambda i, role=role: context + " " + role(i),
                                        lambda i, line=line: theme_context(context + " " + line[:i]))
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
        def theme_at(i, cells=cells, line=line):
            col = line.count("|", 0, i)
            return theme_context((header[col] if col < len(header) else "") + " " + " ".join(cells[1:3]) + " " + context)
        lines[n] = tokenize_lengths(tokenize_segment(line, role_of, theme_at), header)
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
    """Only in measurement tables (a 'Property' column), never inside a quoted CSS rule or a source
    cell. Each px value takes the group named nearest before it in its own clause ('padding 4px 8px;
    border 2px' gives space, space, borderWidth); a clause that names no group takes the row
    property's group only when the property names exactly one. Anything else stays raw."""
    if not header or not any(h.strip() == "Property" for h in header) or not line.startswith("|") or set(line) <= set("|- :"):
        return line
    cells = line.split("|")
    pcol = [h.strip() for h in header].index("Property")
    prop = " ".join(cells[1:pcol + 1]).lower()
    if "css" in prop:
        return line
    def groups_in(text):
        return [(m.start(), g) for words, g in SCALES for m in re.finditer(words, text.lower())]
    prop_groups = {g for _, g in groups_in(prop)}
    row_group = prop_groups.pop() if len(prop_groups) == 1 else None
    for i in range(pcol + 1, len(cells)):
        head = header[i].strip() if i < len(header) else ""
        cell = cells[i]
        if head == "Source" or "css:" in cell or "{" in cell or "captured" in cell:
            continue
        def sub(m, cell=cell):
            clause_start = max(cell.rfind(sep, 0, m.start()) for sep in (";", ",", "(", "/")) + 1
            named = [g for pos, g in groups_in(cell[clause_start:m.start()])]
            group = named[-1] if named else row_group
            if not group:
                return m.group(0)
            values = {v["$value"]: k for k, v in CORE[group].items() if isinstance(v, dict) and "$value" in v}
            k = values.get(m.group(0))
            return f"`{group}.{k}` {m.group(0)}" if k else m.group(0)
        cells[i] = PX.sub(sub, cell)
    return "|".join(cells)

def tokenize_json(v, key=""):
    """The JSON twins name the role in the field path ('face', '::before border color',
    'lip_box_shadow'), so the path of field names is part of the role text, and the Markdown and
    JSON pick the same token."""
    if isinstance(v, str):
        return tokenize(v, key)
    if isinstance(v, list):
        return [tokenize_json(x, key) for x in v]
    if isinstance(v, dict):
        return {k: tokenize_json(x, (key + " " + k).strip()) for k, x in v.items()}
    return v

# This script's own output: a token path in backticks followed by a space, in front of a colour
# or a length. Stripped first, so a change to the rules above regenerates every spec.
OWN = re.compile(r"`(?:palette\.(?:light|dark)|text|border|surface|background|accent|status|feedback|gamification|dataViz|unitColors|radius|space|borderWidth)\.[\w.-]+` (?=#|\d|[a-z][a-z0-9-]*:? #)")

def strip(v):
    if isinstance(v, str):
        return OWN.sub("", v)
    if isinstance(v, list):
        return [strip(x) for x in v]
    if isinstance(v, dict):
        return {k: strip(x) for k, x in v.items()}
    return v

n = 0
for md in ("components/core.md", "components/product.md"):
    p = PKG / md
    before = p.read_text()
    after = tokenize(strip(before))
    tokref = re.compile(r"`[a-zA-Z]+\.[\w.-]+` (?=#|\d)")
    n += len(tokref.findall(after)) - len(tokref.findall(before))
    p.write_text(after)
for js in ("components/core.json", "components/product.json"):
    p = PKG / js
    d = json.loads(p.read_text())
    p.write_text(json.dumps(tokenize_json(strip(d)), indent=1, ensure_ascii=False))
print("tokens placed in front of", n, "values")
