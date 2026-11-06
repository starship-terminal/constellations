#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Adapted from the native kit (systems/grokbot). Every token becomes a CSS custom property (its path
joined with dashes; an alias becomes a var() reference), light on :root and dark under
[data-theme="dark"], so the swatches, scales and specimens cannot drift from the file. Specimens are
drawn from tokens only; none of Zed's icons or artwork is used. Standard library only, deterministic.
"""
import html
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = PKG / "tokens.json"
OUT = PKG / "style-guide.html"
EV_CLASS = {"Measured": "ev-measured", "Sampled": "ev-sampled", "Sampled (text)": "ev-text", "Derived": "ev-derived", "Not captured": "ev-none"}


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def var(path):
    return "--" + "-".join(path).replace("_", "-")


def css(v):
    if isinstance(v, str) and v.startswith("{") and v.endswith("}"):
        return "var(%s)" % var(tuple(v[1:-1].split(".")))
    return str(v)


def esc(t):
    return html.escape(str(t), quote=True)


def resolve(v, *sets):
    while isinstance(v, str) and v.startswith("{") and v.endswith("}"):
        path = tuple(v[1:-1].split("."))
        v = next(s[path]["$value"] for s in sets if path in s)
    return v


def ev(t):
    e = t["$extensions"]["source"]["evidence"]
    return '<span class="ev %s">%s</span>' % (EV_CLASS[e], esc(e))


def build():
    data = json.loads(TOKENS.read_text())
    core = dict(walk(data["core"]))
    light = dict(walk(data["light"]))
    dark = dict(walk(data["dark"]))

    root = []
    for p, t in core.items():
        if t["$type"] == "typography":
            continue
        root.append(f"{var(p)}:{css(t['$value'])};")
    lvars = "".join(f"{var(p)}:{css(t['$value'])};" for p, t in light.items())
    dvars = "".join(f"{var(p)}:{css(t['$value'])};" for p, t in dark.items())
    type_css = []
    for p, t in core.items():
        if t["$type"] == "typography":
            v = t["$value"]
            type_css.append(".t-%s{font-family:%s;font-weight:%s;font-size:%s;line-height:%s}" % (
                p[-1], css(v["fontFamily"]), css(v["fontWeight"]), css(v["fontSize"]), css(v.get("lineHeight", "1.4"))))

    def swatch_rows(prefix):
        rows = []
        for p in light:
            if p[0] != prefix:
                continue
            cells = []
            for theme_set, other in ((light, "light"), (dark, "dark")):
                t = theme_set[p]
                shown = resolve(t["$value"], theme_set, core)
                label = t["$value"] if t["$value"] == shown else f"{t['$value']} = {shown}"
                cells.append('<td><i class="sw" style="background:%s"></i><code>%s</code> %s</td>' % (esc(shown), esc(label), ev(t)))
            rows.append("<tr><th><code>%s</code></th>%s<td class=d>%s</td></tr>" % (esc(".".join(p)), "".join(cells), esc(light[p]["$description"])))
        return "\n".join(rows)

    def core_rows(group):
        rows = []
        for p, t in core.items():
            if p[0] != group:
                continue
            v = t["$value"]
            shown = json.dumps(v) if isinstance(v, dict) else v
            demo = ""
            if group == "radius":
                demo = '<i class="rad" style="border-radius:%s"></i>' % css(v)
            elif group in ("spacing",):
                demo = '<i class="spc" style="width:%s"></i>' % css(v)
            elif group == "typography":
                demo = '<span class="t-%s">The quick brown fox, 0123</span>' % p[-1]
            rows.append("<tr><th><code>%s</code></th><td><code>%s</code> %s</td><td>%s</td><td class=d>%s</td></tr>" % (
                esc(".".join(p)), esc(shown), ev(t), demo, esc(t["$description"])))
        return "\n".join(rows)

    def v(path):
        return "var(%s)" % var(tuple(path.split(".")))

    syntax_line = lambda parts: "".join('<span style="color:%s">%s</span>' % (v("syntax." + k), esc(txt)) if k else esc(txt) for k, txt in parts)
    code = "\n".join([
        syntax_line([("keyword", "from "), ("", "dataclasses "), ("keyword", "import "), ("", "dataclass")]),
        syntax_line([("constant", "MAX_ITEMS"), ("", " = "), ("number", "24"), ("comment.default", "  # a constant")]),
        syntax_line([("attribute", "@dataclass")]),
        syntax_line([("keyword", "class "), ("type", "Item"), ("", ":")]),
        syntax_line([("", "    name: "), ("type", "str")]),
        syntax_line([("", "    "), ("keyword", "def "), ("function", "label"), ("", "(self) -> "), ("type", "str"), ("", ":")]),
        syntax_line([("", "        "), ("keyword", "return "), ("string.default", 'f"{self.name}"')]),
    ])
    specimens = f"""
<div class="win">
 <div class="bar title">zed <span class="mut">main</span><span class="btn">Restart to Update</span></div>
 <div class="tabs"><span class="tab on">inventory.py</span><span class="tab">NOTES.md</span></div>
 <div class="body">
  <div class="tree"><div class="row sel"><span style="color:{v('theme.modified.default')}">inventory.py</span><b style="color:{v('theme.modified.default')}">M</b></div><div class="row">NOTES.md</div><div class="row"><span style="color:{v('theme.created.default')}">todo.txt</span><b style="color:{v('theme.created.default')}">U</b></div></div>
  <div class="editor"><pre class="t-code"><span class="active">{code.splitlines()[0]}</span>
{chr(10).join(code.splitlines()[1:])}</pre>
   <div class="palette"><div class="q mut">Execute a command...</div><div class="it sel">agent: <span class="hl">toggle</span><span class="kb">⌥⌘B</span></div><div class="it">git panel: <span class="hl">toggle</span></div><div class="it">terminal panel: <span class="hl">toggle</span><span class="kb">⌘J</span></div></div>
  </div>
 </div>
 <div class="bar status"><span class="err">● 2</span><span class="mut">1:1</span><span>Python</span></div>
</div>
<div class="row2">
 <div class="menu"><div>Reveal in Finder<span class="kb">⌥⌘R</span></div><div>Copy Path</div><div class="dis">Paste</div><hr><div>Rename<span class="kb">F2</span></div><div>Trash</div></div>
 <div class="tip">Terminal Panel <span class="kb">⌘J</span></div>
 <div class="ctl"><span class="btn">Edit in settings.json</span> <span class="sel2">Platform Default ⌃⌄</span> <i class="sw2"></i> <i class="sw2 on"></i></div>
 <div class="msg t-code">List the files in this folder</div>
 <div class="banner">⚠ Your settings are out of date, and need to be updated.</div>
</div>"""
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zed style guide</title>
<style>
:root{{{''.join(root)}{lvars}}}
[data-theme="dark"]{{{dvars}}}
{''.join(type_css)}
body{{margin:0;font-family:var(--fontFamily-ui);font-size:14px;background:var(--role-page);color:var(--role-text-primary);padding:16px 24px}}
h1{{font-size:24px}} h2{{margin-top:40px;font-size:18px;border-bottom:1px solid var(--role-border-default);padding-bottom:6px}}
table{{border-collapse:collapse;width:100%;font-size:12px}} td,th{{text-align:left;vertical-align:top;padding:4px 6px;border-bottom:1px solid var(--role-border-subtle)}}
.wrap{{overflow-x:auto}} .d{{color:var(--role-text-secondary);max-width:520px}}
.sw{{display:inline-block;width:18px;height:18px;border-radius:3px;vertical-align:middle;margin-right:6px;border:1px solid var(--role-border-subtle)}}
.ev{{font-size:10px;padding:1px 4px;border-radius:3px;border:1px solid var(--role-border-default)}} .ev-measured{{color:var(--role-status-success)}} .ev-derived{{color:var(--role-status-warning)}} .ev-sampled{{color:var(--role-text-link)}}
.rad{{display:inline-block;width:40px;height:28px;border:1px solid var(--role-border-default);background:var(--role-surface)}} .spc{{display:inline-block;height:10px;background:var(--role-accent-default)}}
.toggle{{position:sticky;top:0;float:right;font:inherit;background:var(--role-control-default);color:inherit;border:1px solid var(--role-border-default);border-radius:var(--radius-sm);padding:4px 10px}}
.mut{{color:var(--role-text-secondary)}} .kb{{float:right;color:var(--role-text-secondary)}} .hl{{color:var(--role-text-link)}}
.win{{border:1px solid var(--role-border-default);border-radius:var(--radius-lg);overflow:hidden;max-width:960px}}
.bar{{display:flex;gap:12px;align-items:center;padding:0 10px;background:var(--role-chrome);font-size:13px}} .title{{height:var(--size-titleBar)}} .status{{height:var(--size-statusBar);justify-content:flex-end;border-top:1px solid var(--role-border-default)}}
.err{{color:var(--role-status-danger);margin-right:auto}}
.btn{{border:1px solid var(--role-border-default);border-radius:var(--radius-sm);padding:2px 8px;margin-left:auto;background:var(--component-button-bg)}} .ctl .btn{{margin:0}}
.tabs{{display:flex;height:var(--size-tabBar);background:var(--component-tab-bg);border-top:1px solid var(--role-border-default);border-bottom:1px solid var(--role-border-default);padding-left:var(--size-projectPanel)}}
.tab{{padding:0 var(--spacing-6);display:flex;align-items:center;color:var(--component-tab-text);border-right:1px solid var(--role-border-default)}} .tab.on{{background:var(--component-tab-activeBg);color:var(--theme-modified-default);margin-bottom:-1px}}
.body{{display:flex;min-height:300px}} .tree{{width:var(--size-projectPanel);background:var(--role-surface);border-right:1px solid var(--role-border-default)}}
.row{{height:var(--size-treeRow);display:flex;align-items:center;justify-content:space-between;padding:0 var(--spacing-3)}} .row.sel{{background:var(--role-accent-selected)}}
.editor{{flex:1;background:var(--role-page);position:relative;color:var(--role-text-code)}} pre{{margin:0;padding:8px 16px}} .active{{background:var(--theme-editor-active-line-background);display:inline-block;width:100%}}
.editor{{overflow:hidden}} @media (max-width:600px){{.win{{overflow-x:auto}} .win>*{{min-width:600px}}}} .palette{{box-sizing:border-box;position:absolute;top:24px;left:24px;width:var(--component-palette-width);max-width:calc(100% - 48px);background:var(--component-palette-bg);border:1px solid var(--role-border-subtle);border-radius:var(--radius-lg)}}
.q{{height:var(--size-paletteQuery);display:flex;align-items:center;padding:0 var(--spacing-3);border-bottom:1px solid var(--role-border-subtle)}} .it{{height:var(--size-paletteRow);line-height:var(--size-paletteRow);margin:0 var(--spacing-1);padding:0 8px;border-radius:var(--radius-sm)}} .it.sel{{background:var(--role-accent-selected)}}
.row2{{display:flex;flex-wrap:wrap;gap:16px;margin-top:16px;align-items:flex-start}}
.menu{{box-sizing:border-box;width:var(--size-menuWidth);background:var(--component-menu-bg);border:1px solid var(--role-border-subtle);border-radius:var(--radius-md);padding:4px 0}} .menu div{{padding:3px 12px}} .menu hr{{border:0;border-top:1px solid var(--role-border-subtle);margin:4px 0}} .dis{{color:var(--role-text-disabled)}}
.tip{{background:var(--component-tooltip-bg);border:1px solid var(--role-border-subtle);border-radius:var(--radius-lg);padding:6px 10px;min-width:160px}}
.ctl{{display:flex;gap:10px;align-items:center}} .sel2{{background:var(--component-select-bg);border:1px solid var(--role-border-subtle);border-radius:var(--radius-sm);height:var(--size-control);display:inline-flex;align-items:center;padding:0 8px}}
.sw2,.sel2{{box-sizing:border-box}} .sw2{{display:inline-block;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:999px;background:var(--role-control-default);border:1px solid var(--role-border-default);position:relative}} .sw2:after{{content:"";position:absolute;top:2px;left:3px;width:var(--size-switch-thumb);height:var(--size-switch-thumb);border-radius:50%;background:var(--role-text-secondary)}} .sw2.on{{background:var(--role-control-switchOn)}} .sw2.on:after{{left:auto;right:3px;background:var(--role-text-primary)}}
.msg{{background:var(--component-userMessage-bg);border:1px solid var(--role-border-default);border-radius:var(--radius-md);padding:var(--spacing-3);min-width:280px}}
.banner{{background:var(--role-status-warningBg);border:1px solid var(--role-border-subtle);border-radius:var(--radius-sm);padding:8px 12px}}
</style></head><body>
<button class="toggle" onclick="var r=document.documentElement;r.dataset.theme=r.dataset.theme==='dark'?'light':'dark'">Light / Dark</button>
<h1>Zed 1.25.2: One Light and One Dark</h1>
<p class="d">Every colour is Zed's own declared value from <code>assets/themes/one/one.json</code> at the v1.25.2 commit (Measured), checked against the window's pixels (raw/pixel-check.json). Sizes, radii and type sizes are read from the 2x window captures (Sampled or Derived). Specimens are drawn from the tokens only; none of Zed's icons or artwork is used. Zed's popovers cast a soft shadow that was not measured, so the specimens draw none.</p>
<h2>Specimens</h2>
{specimens}
<h2>Roles (light, dark)</h2><div class="wrap"><table>{swatch_rows("role")}</table></div>
<h2>Components</h2><div class="wrap"><table>{swatch_rows("component")}</table></div>
<h2>Typography</h2><div class="wrap"><table>{core_rows("typography")}{core_rows("fontFamily")}{core_rows("fontSize")}{core_rows("fontWeight")}{core_rows("lineHeight")}</table></div>
<h2>Radii</h2><div class="wrap"><table>{core_rows("radius")}</table></div>
<h2>Spacing</h2><div class="wrap"><table>{core_rows("spacing")}</table></div>
<h2>Sizes and borders</h2><div class="wrap"><table>{core_rows("size")}{core_rows("border")}</table></div>
<h2>Syntax (light, dark)</h2><div class="wrap"><table>{swatch_rows("syntax")}</table></div>
<h2>Players (light, dark)</h2><div class="wrap"><table>{swatch_rows("player")}</table></div>
<h2>Every theme key (light, dark)</h2><div class="wrap"><table>{swatch_rows("theme")}</table></div>
</body></html>
"""
    OUT.write_text(page)
    print("style-guide.html:", len(light), "colour tokens per theme")


if __name__ == "__main__":
    build()
