"""Build the docs site: render docs/**/*.md into site/ with the gallery's chrome.

    python3 tools/site.py              write site/ (run tools/scorecard.py first)
    python3 tools/site.py --publish    the same, for the published site: the gallery
                                       copy, its nav links and its card are left out

Replaces the Zensical/Material build with a small static renderer: every page is
one markdown file wrapped in the same bar the gallery uses — full-bleed top bar
with the mark, the site nav, the search field and the ds-theme toggle — plus a
left rail for the Scorecard and Docs sections. site/ is gitignored; the Pages
workflow builds it with --publish and encrypts the rest.
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

MARK_SVG = ('<svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true">'
            '<rect x="1" y="1" width="7" height="7" rx="2"/><rect x="10" y="1" width="7" height="7" rx="3.5"/>'
            '<rect x="1" y="10" width="7" height="7" rx="3.5"/><rect x="10" y="10" width="7" height="7" rx="2"/></svg>')
SEARCH_SVG = ('<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true">'
              '<circle cx="7" cy="7" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/>'
              '<path d="M11 11l3.5 3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>')
THEME_SVG = ('<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">'
             '<path d="M8 1.5a6.5 6.5 0 1 0 0 13z" fill="currentColor"/>'
             '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>')

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
    """The section's left rail."""
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
    has_rail = page.section and "navigation" not in hidden
    body = f'<main class="doc">{rendered}</main>'
    if has_rail:
        body = f'<div class="wrap has-rail">{rail(page, rel)}{body}</div>'
    # The published site drops site/gallery/ (it shows the captures), so the nav
    # links and the search form that submits into it are left out too.
    nav = [f'<a href="{home}"{current("home")}>Home</a>']
    if not publish:
        nav += [f'<a href="{rel}gallery/index.html">Gallery</a>',
                f'<a href="{rel}gallery/index.html#/refero">Refero</a>']
    nav += [f'<a href="{rel}scorecard/"{current("scorecard")}>Scorecard</a>',
            f'<a href="{rel}DESIGN-SYSTEM/"{current("docs")}>Docs</a>']
    nav = "\n    ".join(nav)
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
<link rel="icon" href="{rel}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{rel}assets/icons/apple-touch-icon.png">
<link rel="manifest" href="{rel}site.webmanifest">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#fafafa">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#08090a">
<meta name="apple-mobile-web-app-title" content="Design">
<link rel="stylesheet" href="{rel}stylesheets/site.css">
<link rel="stylesheet" href="{rel}stylesheets/scorecard.css">
<script>
  try {{ document.documentElement.dataset.theme = localStorage.getItem('ds-theme') || 'dark'; }} catch (e) {{ document.documentElement.dataset.theme = 'dark'; }}
</script>
</head>
<body>
<header class="bar">
  <a class="brand" href="{home}">
    {MARK_SVG}
    <span>Design systems</span>
  </a>
  <nav class="site-nav" aria-label="Site">
    {nav}
  </nav>
{search}
  <button id="theme" class="icon-btn" type="button" aria-label="Toggle colour theme" title="Toggle theme">
    {THEME_SVG}
  </button>
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
