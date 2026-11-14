#!/usr/bin/env python3
"""Label every refero style with a product type, a design style and secondary tags.

Batches styles through the Anthropic Messages API (needs ANTHROPIC_API_KEY),
validates the answer against the vocabularies below, and writes labels to the
styles columns (product_type, design_style, tags as JSON) and each style's
refero/<slug>/meta.json. Resumable: rows that already have a product_type are
skipped unless --force is given.

Usage:
    python3 tools/refero/classify.py [--workers 6] [--batch 50] [--limit N] [--force]
    python3 tools/refero/classify.py --stats        # print the current label distribution
"""

import argparse
import concurrent.futures
import json
import os
import re
import sqlite3
import sys
import time
import urllib.request
from pathlib import Path

import fetch  # write_atomic, and cmd_catalog to refresh refero/catalog.json
import dump as refero_dump  # refreshes refero/.dump/ after a write
import refero_media

ROOT = Path(__file__).resolve().parents[2]
REFERO = ROOT / "refero"
DB = REFERO / "refero.db"
API = "https://api.anthropic.com/v1/messages"
MODEL = "claude-haiku-4-5"

# Primary label vocabularies. tags accepts the union of both.
PRODUCT_TYPES = {
    "ai": "AI-first assistants, agents, model companies, AI infrastructure",
    "ai-media": "AI-first generative media: image, video, audio or voice generation, AI creative suites",
    "devtools": "software for building or running software: hosting, databases, CI, APIs, observability, analytics",
    "saas": "business software for one function: CRM, support, HR, legal, marketing, operations",
    "productivity": "notes, docs, tasks, calendars, personal knowledge, email clients",
    "design-tool": "creative software that produces visual or audio work: UI design, video editing, music production, 3D, site builders",
    "fintech": "banking, payments, treasury, payroll, insurance, lending products",
    "venture": "investment funds and capital firms",
    "crypto": "blockchains, wallets, exchanges, NFTs, web3 infrastructure",
    "social": "social networks, messaging, community platforms",
    "media": "publications, magazines, editorial platforms, newsletters",
    "entertainment": "streaming, music, film, games, events, ticketing",
    "education": "learning products, courses, schools",
    "health": "medical, fitness, wellness, sleep products and providers",
    "commerce": "online shops, marketplaces, consumer goods brands (electronics, home, beauty); apparel goes to fashion, food to food-drink",
    "food-drink": "food and beverage brands, restaurants, coffee",
    "fashion": "apparel, footwear, luxury labels, and fashion retailers",
    "hardware": "physical products: devices, vehicles, audio gear, robotics, aerospace, energy",
    "agency": "studios, agencies and consultancies doing client work",
    "portfolio": "an individual practitioner's personal site",
    "design-resource": "type foundries, icon and UI kits, brand resources, mockups",
    "architecture": "architecture, interiors, real estate, landscape",
    "culture": "museums, festivals, arts institutions, nonprofits, campaigns",
    "other": "none of the above fits",
}

DESIGN_STYLES = {
    "paper": "warm craft canvas: cream, bone, parchment or linen ground, ink type, tactile print feel",
    "editorial": "magazine or broadsheet layout: display serif or grotesk headlines, ruled columns, index rhythm",
    "swiss": "strict international-style grid, sans type, monochrome plus one accent",
    "maximalist": "loud and dense: zines, posters, collage, stacked oversized type",
    "retro": "vintage, Y2K, pixel, lo-fi, period pastiche",
    "technical": "terminal, blueprint or instrument-panel feel: mono type, schematics, data-dense",
    "neon": "dark canvas with electric glow: gradients, neon accents, cyber",
    "cinematic": "full-bleed filmic imagery, dramatic lighting, letterbox framing",
    "futuristic": "sci-fi HUD, orbital, space-age chrome",
    "minimal": "whitespace-led restraint, gallery-quiet, few elements",
    "corporate": "institutional clean: safe grids, neutral palette, trust signals",
    "monochrome": "strict black-and-white or single-hue discipline",
    "playful": "mascot or illustration-led, chunky shapes, bright colour, whimsy",
    "organic": "botanical, earthy, soft natural forms",
    "luxury": "sparse premium: refined serif, dark or champagne, product as jewel",
    "brutalist": "deliberately raw: exposed structure, system fonts, harsh rules",
}

VOCAB = set(PRODUCT_TYPES) | set(DESIGN_STYLES)

SYSTEM = """You classify website design snapshots from styles.refero.design into a fixed
taxonomy. For each style you get: slug, name (the product or organisation),
host (its website domain), industry (a coarse upstream guess, often wrong or
"other"), and tagline (a one-line description of the aesthetic written as an
evocative metaphor: read the imagery for the style, not literal truth).

Assign exactly one product_type and one design_style per style, plus up to 4
secondary tags.

PRODUCT_TYPE - what the product or organisation IS:
%s

DESIGN_STYLE - the dominant aesthetic, independent of colour theme (a dark page
can still be editorial; a light page can still be technical):
%s

Rules:
- product_type describes the company; design_style describes the page. Judge
  them independently.
- tags: other values from either vocabulary that also clearly apply. Never
  repeat the primaries. Leave empty when nothing else fits.
- When torn between two styles, the dominant one wins; put the other in tags.
- Respond with a JSON array only, one object per input style:
  [{"slug": "...", "product_type": "...", "design_style": "...", "tags": ["..."]}]
""" % ("\n".join(f"- {k}: {v}" for k, v in PRODUCT_TYPES.items()),
       "\n".join(f"- {k}: {v}" for k, v in DESIGN_STYLES.items()))

FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$")


def norm(value, vocab):
    """Lowercase a label and accept it only if it is in the vocabulary."""
    if not isinstance(value, str):
        return None
    value = re.sub(r"[\s_]+", "-", value.strip().lower())
    return value if value in vocab else None


def host_of(url):
    if not isinstance(url, str) or not url:
        return None
    m = re.match(r"(?:https?://)?(?:www\.)?([^/]+)", url)
    return m.group(1) if m else None


def init_db():
    # sqlite3 would open a pointer file and fail later with "file is not a
    # database"; say what to do instead.
    if DB.exists():
        with open(DB, "rb") as f:
            if f.read(64).startswith(b"version https://git-lfs"):
                sys.exit(f"error: {DB} is a Git LFS pointer; "
                         "run: git lfs install && git lfs pull")
    db = sqlite3.connect(DB)
    have = {r[1] for r in db.execute("PRAGMA table_info(styles)")}
    for col in ("product_type", "design_style", "tags"):
        if col not in have:
            db.execute(f"ALTER TABLE styles ADD COLUMN {col} TEXT")
    db.commit()
    return db


def call_api(batch, model, tries=3):
    """Classify a list of styles; returns (results, missing, last_error).
    Valid results are kept even when other styles in the batch fail or the
    model drops them; each retry only re-asks for the slugs still missing."""
    want = {s["slug"]: s for s in batch}
    out, missing, last = {}, list(want), None
    for attempt in range(tries):
        payload = [{"slug": s["slug"], "name": s["name"], "host": s["host"],
                    "industry": s["industry"], "tagline": s["tagline"]}
                   for s in (want[k] for k in missing)]
        body = json.dumps({
            "model": model, "max_tokens": 4096, "temperature": 0,
            "system": SYSTEM,
            "messages": [{"role": "user", "content": json.dumps(payload)}],
        }).encode()
        req = urllib.request.Request(API, data=body, method="POST", headers={
            "content-type": "application/json",
            "x-api-key": os.environ["ANTHROPIC_API_KEY"],
            "anthropic-version": "2023-06-01",
        })
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                resp = json.loads(r.read())
            text = "".join(b.get("text", "") for b in resp.get("content", []))
            text = FENCE_RE.sub("", text.strip())
            start, end = text.find("["), text.rfind("]")
            items = json.loads(text[start:end + 1])
            for it in items:
                if not isinstance(it, dict) or it.get("slug") not in want:
                    continue
                pt = norm(it.get("product_type"), PRODUCT_TYPES)
                st = norm(it.get("design_style"), DESIGN_STYLES)
                if not pt or not st:
                    continue
                tags = []
                for t in it.get("tags") or []:
                    t = norm(t, VOCAB)
                    if t and t not in (pt, st) and t not in tags:
                        tags.append(t)
                out[it["slug"]] = {"product_type": pt, "design_style": st,
                                   "tags": tags[:4]}
            missing = [k for k in missing if k not in out]
            if not missing:
                break
            last = f"missing/invalid slugs: {missing[:8]}"
        except Exception as ex:
            last = str(ex)[:300]
        time.sleep(2 * (attempt + 1))
    return out, missing, last


def apply(db, results):
    """Write one batch's labels to the db and each style's meta.json, so an
    interrupted run keeps completed work for the next resume."""
    for slug, labels in results.items():
        db.execute(
            "UPDATE styles SET product_type=?, design_style=?, tags=? WHERE slug=?",
            (labels["product_type"], labels["design_style"],
             json.dumps(labels["tags"]), slug))
        write_meta(slug, labels)
    db.commit()


def write_meta(slug, labels):
    """Insert the label keys into refero/<slug>/meta.json, after 'theme'."""
    path = REFERO / slug / "meta.json"
    if not path.is_file():
        return
    try:
        meta = json.loads(path.read_text())
    except json.JSONDecodeError:
        return
    out = {}
    for k, v in meta.items():
        if k in ("product_type", "design_style", "tags"):
            continue
        out[k] = v
        if k == "theme":
            out.update({"product_type": labels["product_type"],
                        "design_style": labels["design_style"],
                        "tags": labels["tags"]})
    if "product_type" not in out:
        out.update({"product_type": labels["product_type"],
                    "design_style": labels["design_style"],
                    "tags": labels["tags"]})
    fetch.write_atomic(path, json.dumps(out, indent=2) + "\n")


def stats(db):
    print("product_type:")
    for v, n in db.execute(
            "SELECT product_type, COUNT(*) FROM styles GROUP BY product_type "
            "ORDER BY COUNT(*) DESC").fetchall():
        print(f"  {v or '(none)':<16} {n}")
    print("design_style:")
    for v, n in db.execute(
            "SELECT design_style, COUNT(*) FROM styles GROUP BY design_style "
            "ORDER BY COUNT(*) DESC").fetchall():
        print(f"  {v or '(none)':<16} {n}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--batch", type=int, default=50)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--model", default=MODEL)
    args = ap.parse_args()

    db = init_db()
    if args.stats:
        stats(db)
        return
    refero_media.load_env(("ANTHROPIC_API_KEY",))
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY is not set")
    try:
        label(db, args)
    finally:
        db.close()
        # catalog.json carries the labels too; refresh it however the run ends
        # (done, nothing to do, interrupted after some batches committed), or
        # check.py fails on every relabelled style until fetch.py --catalog-only.
        # The text dump of the db follows for the same reason.
        try:
            fetch.cmd_catalog()
        finally:
            refero_dump.refresh(DB)


def label(db, args):
    where = "" if args.force else "WHERE product_type IS NULL OR design_style IS NULL"
    rows = db.execute(
        f"""SELECT slug, name, tagline, source_url, design_system_json
            FROM styles {where} ORDER BY slug""").fetchall()
    styles = []
    for slug, name, tagline, source_url, ds_json in rows:
        industry = None
        try:
            industry = (json.loads(ds_json or "{}") or {}).get("industry")
        except json.JSONDecodeError:
            pass
        styles.append({"slug": slug, "name": name, "tagline": tagline,
                       "host": host_of(source_url), "industry": industry})
    if args.limit:
        styles = styles[:args.limit]
    batches = [styles[i:i + args.batch] for i in range(0, len(styles), args.batch)]
    print(f"to classify: {len(styles)} styles in {len(batches)} batches")
    if not batches:
        return

    by_slug = {s["slug"]: s for s in styles}
    results, failed, done = {}, [], 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(call_api, b, args.model): b for b in batches}
        for fut in concurrent.futures.as_completed(futures):
            batch = futures[fut]
            done += len(batch)
            try:
                out, missing, last = fut.result()
            except Exception as ex:
                missing, out, last = [s["slug"] for s in batch], {}, str(ex)[:300]
            if out:
                results.update(out)
                apply(db, out)
            if missing:
                failed += [by_slug[k] for k in missing]
                print(f"partial batch of {len(batch)}: {last}", file=sys.stderr)
            if done % 500 < args.batch:
                print(f"classified {len(results)}/{len(styles)}")

    # One more pass, smaller batches, over whatever the bulk pass dropped.
    still = []
    for i in range(0, len(failed), 10):
        chunk = failed[i:i + 10]
        out, missing, last = call_api(chunk, args.model)
        if out:
            results.update(out)
            apply(db, out)
        if missing:
            still += missing
            print(f"retry of {len(chunk)} still missing {len(missing)}: {last}",
                  file=sys.stderr)

    print(f"labeled {len(results)}/{len(styles)}; "
          f"{len(still)} left unlabeled")
    stats(db)


if __name__ == "__main__":
    main()
