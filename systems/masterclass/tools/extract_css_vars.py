#!/usr/bin/env python3
"""Pull MasterClass custom properties out of the captured stylesheets.

The stylesheets live outside the repo (they are the product's CSS). Point
CSS_DIR at that folder. Writes raw/css-vars.json: every --mc-*, --spacing-*
and --font-* declaration, plus the font-face families found.
"""
import json, os, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
CSS_DIR = pathlib.Path(os.environ.get("CSS_DIR", os.path.expanduser("~/.design-systems/masterclass/probe/css")))

css = ""
files = []
for f in sorted(CSS_DIR.glob("*.css")):
    text = f.read_text(encoding="utf-8", errors="replace")
    css += text + "\n"
    files.append({"file": f.name, "bytes": len(text)})

decls = re.findall(r"(--(?:mc|spacing|font)[A-Za-z0-9_-]*)\s*:\s*([^;}{]+)", css)
best = {}
counts = {}
for name, value in decls:
    value = " ".join(value.split())
    counts[name] = counts.get(name, 0) + 1
    if name not in best or (best[name].startswith("var(") and not value.startswith("var(")):
        best[name] = value

faces = []
for block in re.findall(r"@font-face\{[^}]+\}", css):
    fam = re.search(r"font-family:\s*([^;}]+)", block)
    weight = re.search(r"font-weight:\s*([^;}]+)", block)
    src = re.search(r"url\(([^)]+)\)", block)
    faces.append({
        "family": fam.group(1).strip(" \"'") if fam else None,
        "weight": weight.group(1).strip() if weight else None,
        "src": src.group(1).strip(" \"'")[:120] if src else None,
    })

out = {
    "source": "www.masterclass.com stylesheets fetched during the 2026-11-21 public capture",
    "files": files,
    "declarationCount": len(decls),
    "unique": len(best),
    "vars": {name: {"value": best[name], "declarations": counts[name]} for name in sorted(best)},
    "fontFaces": faces,
}
RAW.mkdir(parents=True, exist_ok=True)
(RAW / "css-vars.json").write_text(json.dumps(out, indent=1) + "\n")
print(f"wrote {len(best)} vars from {len(files)} sheets")
