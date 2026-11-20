"""Find each token value among the package's raw readings.

forms() turns one raw string into every normalised form a token could hold: the whole string,
the string without quotes, a font stack's first family, each colour as lower-case hex (from #rgb,
#rgba, rgb(), rgba() or color(srgb ...), rounded half up as a browser paints), each px or ms
length with a leading zero restored, and each time in s as ms. reading_forms() collects them over
every raw/*.json file. missing() lists a token's literal values that no reading holds.
"""
import json
import math
import re
from pathlib import Path

HAND = "entered by hand at capture time"


def _hex(r, g, b, a=None):
    h = "#" + "".join(f"{math.floor(float(x) + 0.5):02x}" for x in (r, g, b))
    if a is not None and float(a) < 1:
        h += f"{math.floor(float(a) * 255 + 0.5):02x}"
    return h


def _num(n):
    return f"{float(n):g}"


def forms(text):
    low = str(text).strip().lower()
    bare = re.sub(r"[\"']", "", low)
    out = {low, bare, bare.split(",")[0].strip()}
    for m in re.finditer(r"rgba?\(\s*([\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", low):
        r, g, b, a = m.groups()
        if a and a.endswith("%"):
            a = float(a[:-1]) / 100
        out.add(_hex(r, g, b, a))
    for m in re.finditer(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)", low):
        r, g, b, a = m.groups()
        out.add(_hex(float(r) * 255, float(g) * 255, float(b) * 255, a))
    for m in re.finditer(r"#([0-9a-f]{3,8})\b", low):
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8 and h.endswith("ff"):
            out.add("#" + h[:6])
        out.add("#" + h)
    for m in re.finditer(r"(-?\d*\.?\d+)(px|ms)\b", low):
        out.add(_num(m.group(1)) + m.group(2))
    for m in re.finditer(r"(-?\d*\.?\d+)s\b", low):
        out.add(_num(float(m.group(1)) * 1000) + "ms")
    for m in re.finditer(r"-?\d*\.?\d+", low):
        out.add(_num(m.group(0)))
    return out


def reading_forms(raw_dir):
    acc = set()

    def walk(node):
        if isinstance(node, dict):
            for key, v in node.items():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
        else:
            acc.update(forms(node))

    for path in sorted(Path(raw_dir).glob("*.json")):
        walk(json.loads(path.read_text()))
    return acc


def literal_values(token):
    value = token["$value"]
    if token.get("$type") == "fontFamily":
        return [re.sub(r"[\"']", "", str(value).split(",")[0]).strip()]
    if isinstance(value, dict):
        return [str(v) for v in value.values() if not str(v).startswith("{")]
    if isinstance(value, list) or (isinstance(value, str) and value.startswith("{")):
        return []
    return [str(value)]


def missing(token, seen):
    out = []
    for value in literal_values(token):
        low = value.lower().strip()
        cands = {low, re.sub(r"[\"']", "", low)}
        m = re.fullmatch(r"(-?\d*\.?\d+)(px|ms)?", low)
        if m:
            cands.add(_num(m.group(1)) + (m.group(2) or ""))
        if not cands & seen:
            out.append(value)
    return out
