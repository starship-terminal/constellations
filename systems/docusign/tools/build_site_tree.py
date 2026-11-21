#!/usr/bin/env python3
"""Write site-tree.md from the crawl record and the US sitemap index.

Reads ~/.design-systems/docusign/crawl.json when present, else crawl-partial.json.
Sitemap XML copied during the probe lives under /tmp/docusign-probe/ when available.
Does not invent pages the crawl did not see. Sitemap URLs are listed as indexed,
not as photographed, unless the crawl visited them.
"""
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
HOME = Path(os.environ.get("HOME", ""))
SCRATCH = HOME / ".design-systems" / "docusign"
PROBE = Path("/tmp/docusign-probe")


def load_crawl():
    for name in ("crawl.json", "crawl-partial.json"):
        p = SCRATCH / name
        if p.exists():
            return json.loads(p.read_text()), name
    return {"pages": [], "controls": [], "walls": []}, "none"


def sitemap_urls():
    main = PROBE / "main-sitemap.xml"
    blog = PROBE / "blog-sitemap.xml"
    out = {"main": [], "blog": []}
    if main.exists():
        out["main"] = re.findall(r"<loc>([^<]+)</loc>", main.read_text(errors="ignore"))
    if blog.exists():
        out["blog"] = re.findall(r"<loc>([^<]+)</loc>", blog.read_text(errors="ignore"))
    return out


def en(urls):
    keep = []
    for u in urls:
        p = urlparse(u)
        if p.netloc not in ("www.docusign.com", "docusign.com"):
            continue
        if re.match(r"^/[a-z]{2}-[a-z]{2}(/|$)", p.path):
            continue
        keep.append(u.split("?")[0].rstrip("/") or "https://www.docusign.com/")
    return sorted(set(keep))


def main():
    crawl, source = load_crawl()
    pages = [p for p in crawl.get("pages", []) if not p.get("mobile")]
    mobile = [p for p in crawl.get("pages", []) if p.get("mobile")]
    walls = crawl.get("walls", [])
    controls = crawl.get("controls", [])
    sm = sitemap_urls()
    main_en = en(sm["main"])
    blog_en = en(sm["blog"])

    lines = []
    w = lines.append
    w("# DocuSign public site tree")
    w("")
    w("Mapped from https://www.docusign.com/ on 2026-11-21, signed out, in headless Playwright (Chromium). Desktop viewport 1440 x 900. Phone viewport 390 x 844. Cookie banners were hidden and never accepted. No email, password, code, or SSO control was used.")
    w("")
    w(f"Crawl record: `{source}`. Desktop pages recorded: {len(pages)}. Phone pages recorded: {len(mobile)}. Wall stops: {len(walls)}.")
    w("")
    w("The US sitemap index lists far more URLs than this capture photographed. Indexed URLs that share a template are grouped. A grouped URL was not opened unless a row below says it was visited.")
    w("")
    w("## How the chrome opens pages")
    w("")
    w("| Control | Opens | Kind |")
    w("|---|---|---|")
    w("| Skip to main content | `#main-content` on the current page | in-page |")
    w("| Sales phone link | `tel:` link in the utility bar | external, not opened |")
    w("| Search | in-page search panel | interaction, query not typed |")
    w("| Support | https://support.docusign.com/s/?language=en_US | sibling host, not followed |")
    w("| Access Documents | https://apps.docusign.com/sign/access | login wall, branch stopped |")
    w("| Log In | https://apps.docusign.com/send | login wall, branch stopped |")
    w("| Logo | https://www.docusign.com/ | public page |")
    w("| Products | mega-menu panel | interaction |")
    w("| Solutions | mega-menu panel | interaction |")
    w("| Resources | mega-menu panel | interaction |")
    w("| Enterprise | https://www.docusign.com/solutions/enterprise | public page |")
    w("| Plans & Pricing | https://ecom.docusign.com/plans-and-pricing/esignature | checkout wall, branch stopped |")
    w("| Contact sales | https://www.docusign.com/contact-sales | public form, not submitted |")
    w("| Buy now | https://ecom.docusign.com/plans-and-pricing/esignature | checkout wall, branch stopped |")
    w("| Try for free | https://trial.docusign.com/ | signup wall, branch stopped |")
    w("| Mobile menu button | full-screen drawer of the same links | interaction at 390 |")
    w("")
    w("## Products menu")
    w("")
    w("The Products button sets `aria-expanded` and reveals a panel. Each row is a link. Opening the panel does not navigate.")
    w("")
    w("| Label | URL |")
    w("|---|---|")
    products = [
        ("Intelligent Agreement Management", "https://www.docusign.com/intelligent-agreement-management"),
        ("Contract Lifecycle Management", "https://www.docusign.com/products/clm"),
        ("Iris", "https://www.docusign.com/products/platform/ai"),
        ("Agreement Preparation", "https://www.docusign.com/products/agreement-preparation"),
        ("Agreement Manager", "https://www.docusign.com/products/platform/agreement-manager"),
        ("eSignature", "https://www.docusign.com/products/electronic-signature"),
        ("Agents", "https://www.docusign.com/products/agents"),
        ("Electronic Notarization", "https://www.docusign.com/products/notary"),
        ("Workflow Builder", "https://www.docusign.com/products/platform/workflow-builder"),
        ("Web Forms", "https://www.docusign.com/products/web-forms"),
        ("App Center", "https://www.docusign.com/products/platform/app-center"),
        ("Integrations", "https://www.docusign.com/integrations"),
        ("MCP Connectors", "https://www.docusign.com/products/mcp"),
        ("APIs", "https://www.docusign.com/products/apis"),
        ("Explore All Products", "https://www.docusign.com/products"),
    ]
    for label, url in products:
        w(f"| {label} | {url} |")
    w("")
    w("## Solutions menu")
    w("")
    w("| Label | URL |")
    w("|---|---|")
    solutions = [
        ("IAM Core", "https://www.docusign.com/solutions/iam-core"),
        ("Sales", "https://www.docusign.com/solutions/departments/sales"),
        ("Customer Experience", "https://www.docusign.com/solutions/departments/customer-experience"),
        ("Human Resources", "https://www.docusign.com/solutions/departments/human-resources"),
        ("Legal", "https://www.docusign.com/solutions/departments/legal"),
        ("Procurement", "https://www.docusign.com/solutions/departments/procurement"),
        ("View All Departments", "https://www.docusign.com/solutions"),
        ("Financial Services", "https://www.docusign.com/solutions/industries/financial-services"),
        ("Insurance", "https://www.docusign.com/solutions/industries/insurance"),
        ("Real Estate", "https://www.docusign.com/solutions/industries/real-estate"),
        ("Government", "https://www.docusign.com/solutions/industries/government"),
        ("Healthcare", "https://www.docusign.com/solutions/industries/healthcare"),
        ("Life Sciences", "https://www.docusign.com/solutions/industries/life-sciences"),
        ("View All Industries", "https://www.docusign.com/solutions"),
    ]
    for label, url in solutions:
        w(f"| {label} | {url} |")
    w("")
    w("## Resources menu")
    w("")
    w("| Label | URL | Kind |")
    w("|---|---|---|")
    resources = [
        ("Blog", "https://www.docusign.com/blog", "public"),
        ("Customer Stories", "https://www.docusign.com/customer-stories", "public"),
        ("Resource Center", "https://www.docusign.com/resources", "public"),
        ("Legality Guide", "https://www.docusign.com/products/electronic-signature/legality", "public"),
        ("Product Releases", "https://www.docusign.com/releases", "public"),
        ("Roadmap", "https://www.docusign.com/releases/roadmap", "public"),
        ("Learn Hub", "https://www.docusign.com/learn", "public"),
        ("Support Center", "https://support.docusign.com/s/?language=en_US", "sibling, not followed"),
        ("Customer Success", "https://www.docusign.com/customer-success", "public"),
        ("Docusign University", "https://dsucustomers.docusign.com/", "sibling, not followed"),
        ("Trust Center & System Status", "https://www.docusign.com/trust", "public"),
        ("Safety Center", "https://www.docusign.com/safety", "public"),
    ]
    for label, url, kind in resources:
        w(f"| {label} | {url} | {kind} |")
    w("")
    w("## Walls")
    w("")
    w("These controls leave the public marketing site. The branch stopped. Nothing was typed.")
    w("")
    w("| Control | URL | Why |")
    w("|---|---|---|")
    seen_wall = set()
    for item in walls:
        key = (item.get("control") or item.get("from"), item.get("to"))
        if key in seen_wall:
            continue
        seen_wall.add(key)
        w(f"| {item.get('control') or 'navigation'} | {item.get('to')} | {item.get('why')} |")
    if not walls:
        w("| Log In | https://apps.docusign.com/send | login wall, recorded from the utility bar, not opened |")
        w("| Try for free | https://trial.docusign.com/ | signup wall, recorded from the nav, not opened |")
        w("| Buy now | https://ecom.docusign.com/plans-and-pricing/esignature | checkout wall, recorded from the nav, not opened |")
        w("| Plans & Pricing | https://ecom.docusign.com/plans-and-pricing/esignature | checkout wall, recorded from the nav, not opened |")
        w("| Access Documents | https://apps.docusign.com/sign/access | login wall, recorded from the utility bar, not opened |")
    w("")
    w("Known probe, not repeated: https://account.docusign.com/ accepted an email and then asked for a password. No code was sent. This capture did not open that host and did not type an email.")
    w("")
    w("## In-page interactions")
    w("")
    w("| Page | Control | What it does |")
    w("|---|---|---|")
    w("| Home | Products, Solutions, Resources | Opens a mega-menu. A second press or Escape closes it. |")
    w("| Home | Search | Opens a search field. No query was typed. |")
    w("| Home at 390 | Menu button | Opens a drawer with the same destinations. |")
    w("| Product and solution pages | FAQ buttons (`aria-expanded`) | Opens one accordion item. |")
    w("| Home hero | Get Started | Sits on a form. Not clicked. The form was not filled. |")
    w("| Home hero | Country/region select | A native select of region names. Not changed. |")
    w("| Home hero | Marketing consent checkbox | Not checked. |")
    w("| Footer | Region links (`/en-ca`, `/fr-fr`, and the other locale homes) | Same marketing site in another locale. Not photographed. |")
    w("| Footer | App store badges | Store listings. Not opened. No app was downloaded. |")
    w("")
    w("## Pages photographed")
    w("")
    w("Desktop shots are `d-<path>-default.png` in the scratch folder, copied into `screenshots/` after quantising. Phone shots use the `m-` prefix.")
    w("")
    w("| URL | Title | Shot |")
    w("|---|---|---|")
    for p in pages:
        if p.get("error"):
            w(f"| {p.get('url')} | {p.get('error')} | |")
            continue
        title = (p.get("title") or "").replace("|", "/")
        w(f"| {p.get('url')} | {title} | {p.get('shot') or 'template already shot'} |")
    w("")
    w("## Phone pass")
    w("")
    if mobile:
        for p in mobile:
            w(f"- {p.get('url')} ({p.get('shot') or 'no new shot'})")
    else:
        w("Phone pass had not finished when this file was built.")
    w("")
    w("## Sitemap, not all photographed")
    w("")
    w(f"English `main-sitemap.xml` URLs: {len(main_en)}. English blog URLs: {len(blog_en)}. Locale copies (en-gb, fr-fr, ja-jp, and the rest of the index) were not crawled.")
    buckets = defaultdict(int)
    for u in main_en:
        path = urlparse(u).path.strip("/")
        buckets[path.split("/")[0] if path else "/"] += 1
    w("")
    w("| First path segment | Indexed URLs |")
    w("|---|---|")
    for k, n in sorted(buckets.items(), key=lambda kv: -kv[1]):
        w(f"| /{k} | {n} |")
    w("")
    w("Templates treated as one page for screenshots:")
    w("")
    w("- `/blog/{post}`")
    w("- `/customer-stories/{story}` and `/customer-stories/{group}/{item}`")
    w("- `/trust/alerts/{alert}`")
    w("- `/company/news-center/{item}`")
    w("- `/legal/{group}/{doc}`")
    w("- `/templates/{template}`")
    w("- `/integrations/{integration}`")
    w("- `/resources/{group}/{item}`")
    w("- `/learn/{group}/{item}`")
    w("- `/lp/{campaign}`")
    w("")
    w("## Controls recorded by the crawler")
    w("")
    w(f"{len(controls)} control rows. Wall and external rows are the ones that stop a branch.")
    w("")
    interesting = [c for c in controls if c.get("kind") in ("wall", "store", "interaction", "sibling")]
    w("| From | Control | To | Kind |")
    w("|---|---|---|---|")
    seen = set()
    for c in interesting[:80]:
        key = (c.get("control"), c.get("to"), c.get("kind"))
        if key in seen:
            continue
        seen.add(key)
        w(f"| {c.get('from')} | {c.get('control')} | {c.get('to')} | {c.get('kind')} |")
    w("")
    (ROOT / "site-tree.md").write_text("\n".join(lines) + "\n")
    print("wrote", ROOT / "site-tree.md", "pages", len(pages))


if __name__ == "__main__":
    main()
