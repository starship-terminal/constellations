#!/usr/bin/env python3
"""Diff the refero.design web catalog against the systems/ packages.

    python3 tools/refero/coverage.py [--refero DIR] [--catalog FILE]

refero/directory.json lists the sites and apps in Refero's paid catalog;
catalog.json lists the measured systems/ packages. Matching is by root
domain (the last two labels, three under a ccSLD such as co.uk; a host on
its own TLD, such as gemini.google, is its own root), so a hit means "a package was captured somewhere on this domain", not necessarily
the same product — each matched package carries name_match, a token
overlap flag between the catalog names and the package slug, to flag the
false positives (an apps.apple.com store URL matches apple.com).

Packages absent from the web catalog also get ios_guess: name-token hits
in the iOS catalog, so "not a web site" does not misread as "Refero does
not cover it".

Writes refero/coverage.json. Pure derivation, no network, deterministic
output; check.py recomputes it to catch drift. Re-run after
fetch_screens.py or a systems/ capture.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dump as refero_dump  # noqa: E402  (its write_atomic)

ROOT = Path(__file__).resolve().parents[2]
REFERO = ROOT / "refero"
CATALOG = ROOT / "catalog.json"

# ccSLDs where the registrable domain is three labels, not two: the common
# commercial and organisational ones, not the whole public-suffix list.
MULTI_SLD = {
    "co.uk", "org.uk", "ac.uk", "gov.uk", "com.au", "net.au", "org.au",
    "co.nz", "co.jp", "or.jp", "ne.jp", "com.br", "com.mx", "co.in",
    "co.kr", "co.za", "com.sg", "com.hk", "com.cn", "net.cn", "com.tr",
    "com.ar", "com.tw", "org.tw", "co.id", "co.il", "org.il", "com.my",
    "com.ph", "co.th", "com.vn", "com.pk", "com.ng", "com.eg", "com.sa",
    "co.ke", "com.co", "com.pe", "com.ua",
}


def root_domain(host):
    host = (host or "").lower().strip().strip("/").removeprefix("www.")
    parts = host.split(".")
    if len(parts) >= 3 and ".".join(parts[-2:]) in MULTI_SLD:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def host_of(url):
    url = url or ""
    return urlparse(url if "://" in url else "https://" + url).hostname or ""


def tokens(text):
    return set(re.findall(r"[a-z0-9]+", (text or "").lower()))


write_atomic = refero_dump.write_atomic


def build(directory: dict, catalog: dict) -> dict:
    """The coverage object for refero/coverage.json."""
    web = {}
    for site in directory.get("web_sites") or []:
        web.setdefault(root_domain(site.get("domain")), []).append({
            "name": (site.get("name") or "").strip(),
            "domain": site.get("domain"),
            "id": site.get("id"),
        })
    ios_names = [
        {"name": (a.get("name") or "").strip(), "id": a.get("id")}
        for a in directory.get("ios_apps") or []
    ]
    pkgs = {}
    for entry in catalog.get("systems") or []:
        dom = root_domain(host_of(entry.get("url")))
        pkgs.setdefault(dom, []).append({
            "slug": entry.get("slug"),
            "name": entry.get("name"),
            "url": entry.get("url"),
        })

    matched, missing = {}, {}
    for dom in sorted(web):
        cat_names = " ".join(c["name"] for c in web[dom])
        if dom in pkgs:
            matched[dom] = {
                "catalog": web[dom],
                "pkgs": [{**p,
                          "name_match": bool(tokens(cat_names)
                                             & tokens(p["slug"]
                                                      .replace("-", " ")))}
                         for p in pkgs[dom]],
            }
        else:
            missing[dom] = web[dom]

    absent = {}
    for dom in sorted(set(pkgs) - set(web)):
        entries = []
        for p in pkgs[dom]:
            slug_toks = tokens(p["slug"].replace("-", " "))
            hits = [a["name"] for a in ios_names
                    if any(t in a["name"].lower()
                           for t in slug_toks if len(t) > 3)]
            entries.append({**p, "ios_guess": hits})
        absent[dom] = entries

    return {
        "about": "refero.design web catalog vs the systems/ packages "
                 "(measured store), matched on root domain; derived by "
                 "tools/refero/coverage.py",
        "totals": {
            "catalog_entries": sum(len(v) for v in web.values()),
            "catalog_domains": len(web),
            "system_packages": sum(len(v) for v in pkgs.values()),
            "system_domains": len(pkgs),
            "matched_domains": len(matched),
            "missing_domains": len(missing),
            "system_domains_absent_from_catalog": len(absent),
        },
        "matched": matched,
        "missing": missing,
        "systems_absent_from_catalog": absent,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refero", type=Path, default=REFERO,
                    help="the refero/ folder (default: the repo's)")
    ap.add_argument("--catalog", type=Path, default=CATALOG,
                    help="the systems catalog.json (default: the repo's)")
    args = ap.parse_args()

    directory = json.loads((args.refero / "directory.json").read_text())
    catalog = json.loads(args.catalog.read_text())
    out = build(directory, catalog)
    write_atomic(args.refero / "coverage.json",
                 json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    t = out["totals"]
    print(f"coverage: {t['matched_domains']}/{t['catalog_domains']} catalog "
          f"domains have a systems/ package; "
          f"{t['system_domains_absent_from_catalog']} package domains absent")


if __name__ == "__main__":
    main()
