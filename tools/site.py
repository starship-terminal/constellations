"""Build the docs site: render docs/**/*.md into site/ with the gallery's chrome.

    python3 tools/site.py              write site/ (run tools/scorecard.py first)
    python3 tools/site.py --publish    the same, for the published site: the gallery
                                       copy, its nav links and its card are left out

Replaces the Zensical/Material build with a small static renderer: every page is
one markdown file wrapped in the same bar the gallery uses — a fixed left rail
with the mark, the site nav, the search field, the section's own links, and the
Settings link, ds-theme toggle and collapse toggle at its foot — plus the
Settings page (settings/, its Preferences hold the app icon). site/ is
gitignored; the Pages workflow builds it with --publish and encrypts the rest.
"""
import argparse
import html
import posixpath
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scorecard  # noqa: E402
from catalog import atomic_write  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "site"

MD_EXTENSIONS = ["extra", "admonition", "toc", "sane_lists"]
MD_CONFIGS = {"toc": {"permalink": "#", "toc_depth": "2-4"}}

DESCRIPTION = ("A private library of design styles captured from real products: measured tokens, "
               "components and screenshots, plus the scorecard grading each capture.")
COPYRIGHT = "Private study notes. Products and trademarks belong to their owners."



def mark_svg() -> str:
    """The bar's mark: the Flat favicon (docs/assets/favicon.svg) inline at 18 px,
    then an empty span the Glass app icon paints from CSS (assets/app-icon.js
    picks which shows). The clip path's id is namespaced so it cannot collide
    with an id on the page. docs/gallery/index.html carries the same markup."""
    svg = (DOCS / "assets" / "favicon.svg").read_text().strip()
    svg = svg.replace('id="c"', 'id="ds-mark-clip"').replace("url(#c)", "url(#ds-mark-clip)")
    svg = svg.replace("<svg ", '<svg class="mark" width="18" height="18" aria-hidden="true" ', 1)
    return svg + '<span class="mark mark-glass" aria-hidden="true"></span>'


MARK_SVG = mark_svg()
# The Flat set, the default. assets/app-icon.js swaps these for the Glass set
# when that is the stored preference, so it must load right after them.
ICON_LINKS = ('<link rel="icon" href="{rel}assets/icons/favicon.ico" sizes="32x32">\n'
              '<link rel="icon" href="{rel}assets/favicon.svg" type="image/svg+xml">\n'
              '<link rel="apple-touch-icon" href="{rel}assets/icons/apple-touch-icon.png">\n'
              '<link rel="manifest" href="{rel}site.webmanifest">\n'
              '<script src="{rel}assets/app-icon.js"></script>')
SETTINGS_SVG = ('<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true" fill="none" '
                'stroke="currentColor" stroke-width="1.4" stroke-linecap="round">'
                '<path d="M2 4.5h7M13 4.5h1M2 11.5h1M7 11.5h7"/>'
                '<circle cx="11" cy="4.5" r="2"/><circle cx="5" cy="11.5" r="2"/></svg>')
SEARCH_SVG = ('<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true">'
              '<circle cx="7" cy="7" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/>'
              '<path d="M11 11l3.5 3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>')
THEME_SVG = ('<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">'
             '<path d="M8 1.5a6.5 6.5 0 1 0 0 13z" fill="currentColor"/>'
             '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>')
COLLAPSE_SVG = ('<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true" fill="none" '
                'stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M9.5 3.5 5 8l4.5 4.5M13.5 3.5 9 8l4.5 4.5"/></svg>')


def nav_ic(inner: str) -> str:
    """A site-nav glyph, the same set docs/gallery/index.html draws."""
    return ('<svg class="nav-ic" width="17" height="17" viewBox="0 0 16 16" aria-hidden="true" fill="none" '
            'stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">'
            f'{inner}</svg>')


NAV_ICONS = {
    "home": nav_ic('<path d="M2 6.5 8 1.5l6 5V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1z"/>'),
    "gallery": nav_ic('<rect x="1.5" y="1.5" width="5.6" height="5.6" rx="1.4"/>'
                      '<rect x="8.9" y="1.5" width="5.6" height="5.6" rx="1.4"/>'
                      '<rect x="1.5" y="8.9" width="5.6" height="5.6" rx="1.4"/>'
                      '<rect x="8.9" y="8.9" width="5.6" height="5.6" rx="1.4"/>'),
    "refero": nav_ic('<path d="M8 1.8l1.5 3.9 4.2.3-3.2 2.7 1 4.1L8 10.4l-3.5 2.4 1-4.1-3.2-2.7 4.2-.3z"/>'),
    "scorecard": nav_ic('<path d="M2 14V8.5M6 14V4.5M10 14v-6M14 14V2.5"/>'),
    "docs": nav_ic('<path d="M3 2.5h8a2 2 0 0 1 2 2V13a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/>'
                   '<path d="M5.5 5.5h5M5.5 8h5M5.5 10.5h3"/>'),
}

# The Settings page (settings/). Preferences are per browser, in localStorage;
# each control talks to the script that owns its store.
SETTINGS_BODY = """<h1>Settings</h1>
<p class="lede">Choices here are saved in this browser and apply to every page of the site.</p>
<h2 id="preferences">Preferences</h2>
<div class="prefs">
  <fieldset class="pref" id="app-icon">
    <legend class="pref-name">App icon</legend>
    <p class="pref-help">The icon in the browser tab, on a home screen and in the sidebar.</p>
    <div class="pref-options">
      <label class="pref-option">
        <input type="radio" name="app-icon" value="flat">
        <img src="{rel}assets/icons/icon-192.png" alt="" width="56" height="56">
        <span><strong>Flat</strong><small>Default</small></span>
      </label>
      <label class="pref-option">
        <input type="radio" name="app-icon" value="glass">
        <img src="{rel}assets/icons/glass/icon-192.png" alt="" width="56" height="56">
        <span><strong>Glass</strong><small>Rendered prism</small></span>
      </label>
    </div>
    <p class="pref-note">An app installed from this site keeps the Flat icon: its manifest is fixed when it is installed.</p>
  </fieldset>
</div>
<script>
  (function () {
    var radios = document.querySelectorAll('input[name="app-icon"]');
    function sync() {
      for (var i = 0; i < radios.length; i++) radios[i].checked = radios[i].value === dsAppIcon.get();
    }
    for (var i = 0; i < radios.length; i++) {
      radios[i].addEventListener('change', function (e) { dsAppIcon.set(e.target.value); });
    }
    document.addEventListener('ds-icon-change', sync);
    sync();
  })();
</script>"""

# A grid-cards item that links into the gallery (the home page's Gallery card): the
# item marker, its `**[title](gallery/…)**` heading and the indented body under it.
GALLERY_CARD = re.compile(r"^ *- +\*\*\[[^\]\n]*\]\(gallery/[^\n]*\)\*\*[^\n]*\n(?: +[^\n]*\n|\n)*", re.M)
FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
HIDE_RE = re.compile(r"^\s*-\s*(navigation|toc)\s*$", re.M)
HEADING_RE = re.compile(r"^#\s+(.+)$", re.M)
TAG_RE = re.compile(r"<[^>]+>|\*\*|__|`")
LINK_RE = re.compile(r'href="([^"#]+\.md)(#[^"]*)?"')
SCHEME_RE = re.compile(r"^([a-zA-Z][a-zA-Z0-9+.-]*:|//)")


def frontmatter(md: str) -> tuple[set[str], str]:
    """Split a leading --- block off. Returns (hidden chrome names, markdown body)."""
    m = FRONT_RE.match(md)
    if not m:
        return set(), md
    return set(HIDE_RE.findall(m.group(1))), md[m.end():]


def page_title(md: str, stem: str) -> str:
    """The first h1's text, or the filename for pages that open on raw HTML."""
    m = HEADING_RE.search(md)
    if not m:
        return stem
    return TAG_RE.sub("", m.group(1)).strip()


def rewrite_links(rendered: str, page: "Page") -> str:
    """Point markdown links at the dir-style URLs the build emits.

    A link such as `../criteria.md` is relative to the source file, so resolve
    it inside docs/ first, map it to the target's output dir URL, then write it
    relative to this page's output URL. Links with a scheme or host (https://,
    //host, mailto:) are external and left alone.
    """
    src_dir = str(page.src.parent.relative_to(DOCS))
    page_dir = page.url or "."

    def repl(m: re.Match) -> str:
        path, frag = m.group(1), m.group(2) or ""
        if SCHEME_RE.match(path):
            return m.group(0)
        target = posixpath.normpath(path.lstrip("/") if path.startswith("/")
                                    else posixpath.join(src_dir, path))
        stem = target[:-len(".md")]
        if stem == "index" or stem.endswith("/index"):
            url = stem[:-len("index")]
        else:
            url = stem + "/"
        out = posixpath.relpath(url or ".", page_dir)
        if not out.endswith("/"):
            out += "/"
        return f'href="{out}{frag}"'
    return LINK_RE.sub(repl, rendered)


class Page:
    def __init__(self, src: Path, url: str, section: str | None):
        self.src = src          # docs/… .md file
        self.url = url          # site-relative dir URL: '', 'scorecard/', 'DESIGN-SYSTEM/'
        self.section = section  # 'scorecard', 'docs' or None


def url_of(src: Path) -> str:
    """The site-relative dir URL a source page lands on (foo/index.md -> foo/)."""
    parts = src.relative_to(DOCS).with_suffix("").parts
    if parts[-1] == "index":
        parts = parts[:-1]
    return "/".join(parts) + "/" if parts else ""


def pages() -> list[Page]:
    out = [Page(DOCS / "index.md", "", None)]
    out += [Page(DOCS / path, url_of(DOCS / path), "docs") for _, path in scorecard.LIBRARY_DOCS]
    out += [Page(p, url_of(p), "scorecard") for p in sorted((DOCS / "scorecard").rglob("*.md"))]
    return out


def rail(page: Page, rel: str) -> str:
    """The section's own links, rendered inside the side rail below the site nav."""
    if page.section == "scorecard":
        _, audits = scorecard.load()
        items = [("Overview", "scorecard/")]
        items += [(scorecard.short(s), f"scorecard/systems/{s['slug']}/")
                  for s in scorecard.ranked(audits[-1]["systems"])]
        items += [("Criteria and method", "scorecard/criteria/"), ("Changelog", "scorecard/changelog/")]
    else:
        items = [(title, f"{Path(path).stem}/") for title, path in scorecard.LIBRARY_DOCS]
    links = ""
    for title, url in items:
        current = ' aria-current="page"' if url == page.url else ""
        links += f'<a href="{rel}{url}"{current}>{html.escape(title)}</a>'
    return f'<aside class="rail"><nav aria-label="Section">{links}</nav></aside>'


def render(page: Page, rendered: str, hidden: set[str], publish: bool = False) -> str:
    rel = "../" * page.url.count("/")
    home = rel if rel else "./"
    current = lambda sec: ' aria-current="page"' if page.section == sec or (sec == "home" and not page.url) else ""
    body = f'<main class="doc">{rendered}</main>'
    section = rail(page, rel) if page.section and "navigation" not in hidden else ""
    # The published site drops site/gallery/ (it shows the captures), so the nav
    # links and the search form that submits into it are left out too.
    nav = [(home, "Home", "home", current("home"))]
    if not publish:
        nav += [(f"{rel}gallery/index.html", "Gallery", "gallery", ""),
                (f"{rel}gallery/index.html#/refero", "Refero", "refero", "")]
    nav += [(f"{rel}scorecard/", "Scorecard", "scorecard", current("scorecard")),
            (f"{rel}DESIGN-SYSTEM/", "Docs", "docs", current("docs"))]
    nav = "\n      ".join(f'<a href="{href}"{cur}>{NAV_ICONS[key]}<span>{label}</span></a>'
                          for href, label, key, cur in nav)
    search = "" if publish else f"""<form class="search" role="search" action="{rel}gallery/index.html" method="get">
    {SEARCH_SVG}
    <input name="q" type="search" placeholder="Search name, use, tag…" autocomplete="off" aria-label="Search design systems">
  </form>"""
    return f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page.title)} · Design systems</title>
<meta name="description" content="{html.escape(DESCRIPTION)}">
{ICON_LINKS.format(rel=rel)}
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#fafafa">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#08090a">
<meta name="apple-mobile-web-app-title" content="Design">
<link rel="stylesheet" href="{rel}stylesheets/site.css">
<link rel="stylesheet" href="{rel}stylesheets/scorecard.css">
<script>
  try {{
    document.documentElement.dataset.theme = localStorage.getItem('ds-theme') || 'dark';
    if (localStorage.getItem('ds-nav') === 'collapsed') document.documentElement.dataset.nav = 'collapsed';
  }} catch (e) {{ document.documentElement.dataset.theme = 'dark'; }}
</script>
</head>
<body>
<header class="bar">
  <a class="brand" href="{home}">
    {MARK_SVG}
    <span>Design systems</span>
  </a>
  <div class="bar-body">
    <nav class="site-nav" aria-label="Site">
      {nav}
    </nav>
{section}
  </div>
{search}
  <span class="bar-foot">
    <a class="icon-btn" href="{rel}settings/" aria-label="Settings" title="Settings"{current("settings")}>
      {SETTINGS_SVG}<span class="lbl">Settings</span>
    </a>
    <button id="theme" class="icon-btn" type="button" aria-label="Toggle colour theme" title="Toggle theme">
      {THEME_SVG}<span class="lbl">Theme</span>
    </button>
    <button id="nav-toggle" class="icon-btn" type="button" aria-pressed="false" title="Collapse sidebar">
      {COLLAPSE_SVG}<span class="lbl">Collapse</span>
    </button>
  </span>
</header>
{body}
<footer class="foot"><p>{html.escape(COPYRIGHT)}</p></footer>
<script src="{rel}assets/redeploy.js" defer></script>
<script>
  /* The theme toggle shares the gallery's ds-theme store, so a choice made on
     either side carries over. The search field submits to the gallery's own
     client-side search; --publish emits no form, and this drops the field when
     nothing answers there anyway. */
  document.getElementById('theme').onclick = function () {{
    var root = document.documentElement;
    var current = root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    root.dataset.theme = current === 'dark' ? 'light' : 'dark';
    try {{ localStorage.setItem('ds-theme', root.dataset.theme); }} catch (e) {{}}
  }};
  /* The collapse toggle pins the rail to an icon column (ds-nav, shared with
     the gallery); collapsed it still opens on hover or focus, per the CSS. */
  var navToggle = document.getElementById('nav-toggle');
  var syncNavToggle = function () {{
    var collapsed = document.documentElement.dataset.nav === 'collapsed';
    navToggle.setAttribute('aria-pressed', String(collapsed));
    navToggle.title = collapsed ? 'Expand sidebar' : 'Collapse sidebar';
    var lbl = navToggle.querySelector('.lbl');
    if (lbl) lbl.textContent = collapsed ? 'Expand' : 'Collapse';
  }};
  navToggle.onclick = function () {{
    var root = document.documentElement;
    if (root.dataset.nav === 'collapsed') {{
      delete root.dataset.nav;
      try {{ localStorage.removeItem('ds-nav'); }} catch (e) {{}}
    }} else {{
      root.dataset.nav = 'collapsed';
      try {{ localStorage.setItem('ds-nav', 'collapsed'); }} catch (e) {{}}
    }}
    // Clicking leaves focus inside the rail, whose :focus-within would hold
    // the collapsed strip open after the cursor leaves — hand it back out.
    navToggle.blur();
    syncNavToggle();
  }};
  syncNavToggle();
  (function () {{
    var f = document.querySelector('.bar .search');
    if (!f) return;
    fetch(f.getAttribute('action'), {{ method: 'HEAD' }})
      .then(function (r) {{ if (!r.ok) f.remove(); }})
      .catch(function () {{ f.remove(); }});
  }})();
</script>
</body>
</html>
"""


def build(publish: bool = False) -> None:
    import markdown

    # site/ is fully generated; start clean so removed pages and assets leave.
    shutil.rmtree(OUT, ignore_errors=True)
    # --publish leaves the gallery out entirely: it shows the captures, so the Pages
    # workflow never ships it.
    statics = ["assets", "stylesheets", "site.webmanifest"] + ([] if publish else ["gallery"])
    for name in statics:
        src, dst = DOCS / name, OUT / name
        if not src.exists():
            continue
        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    count = 0
    for page in pages():
        if not page.src.exists():
            continue
        hidden, md = frontmatter(page.src.read_text())
        if publish:
            md = GALLERY_CARD.sub("", md)  # a card linking to the dropped gallery is dead nav
        page.title = page_title(md, page.src.stem)
        body = rewrite_links(markdown.markdown(md, extensions=MD_EXTENSIONS, extension_configs=MD_CONFIGS), page)
        dest = OUT / page.url / "index.html" if page.url else OUT / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        atomic_write(dest, render(page, body, hidden, publish))
        count += 1

    settings = Page(DOCS / "index.md", "settings/", "settings")
    settings.title = "Settings"
    (OUT / "settings").mkdir(parents=True, exist_ok=True)
    atomic_write(OUT / "settings" / "index.html",
                 render(settings, SETTINGS_BODY.replace("{rel}", "../"), {"navigation"}, publish))
    count += 1

    # A 404 is served at the missing URL, whatever its depth, so the page's
    # relative links would resolve inside the missing directory. The script
    # writes <base> before the stylesheet links: the site sits at / on the
    # deploy host and under /design-systems/ on GitHub Pages.
    not_found = Page(DOCS / "index.md", "", None)
    not_found.title = "Page not found"
    base_fix = ("<script>\n  var __seg = location.pathname.split('/').filter(Boolean);\n"
                "  document.write('<base href=\"/' + (__seg[0] === 'design-systems' ? 'design-systems/' : '') + '\">');\n"
                "</script>")
    html_404 = render(not_found, "<h1>Page not found</h1><p><a href='./'>Back to the library home</a>.</p>",
                      {"navigation"}, publish).replace("<head>", "<head>\n" + base_fix, 1)
    atomic_write(OUT / "404.html", html_404)
    print(f"site: wrote {count} pages to {OUT.relative_to(ROOT)}/")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--publish", action="store_true",
                        help="build for publishing: leave out the gallery, its nav links and its card")
    args = parser.parse_args()
    build(publish=args.publish)


if __name__ == "__main__":
    main()
