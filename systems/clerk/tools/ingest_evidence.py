#!/usr/bin/env python3
"""Copy Clerk captures from an external source directory, sanitizing before writing.

Usage: python3 systems/clerk/tools/ingest_evidence.py ~/.design-systems/clerk

Only raw-shots/*.png and readings/*.json are inputs. rejected-shots and raw
page copies are deliberately excluded. Measurements retain their original
styles, variables, className, index and rectangles. Display text has emails,
Clerk resource IDs and credential strings replaced. DOM email-mask files are
not published: their coordinate space does not reliably match the captured
PNG. Images use native-pixel Tesseract word boxes in normal and contrast-
boosted passes, the repository's redaction fills, then 256-colour quantization.
The post-write OCR check rejects any remaining detectable private string.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

PACKAGE = Path(__file__).resolve().parent.parent
REPO = PACKAGE.parent.parent
sys.path.insert(0, str(REPO / "tools"))
import redact_images as redact  # noqa: E402

# Include addresses clipped by a table column, such as local@example without
# its TLD. The source mobile table fades long addresses at its right edge.
EMAIL = re.compile(r"[\w.+-]+@[\w.-]+", re.I)
RESOURCE_ID = re.compile(r"\b(?:app|user|org|ins|sess|inv|orginv|idn|email|phone|sms|actor|saml|oauth|webhook)_[A-Za-z0-9]{16,}\b")
CREDENTIAL = re.compile(r"\b(?:sk|pk)_(?:test|live)_[A-Za-z0-9_-]+\b|\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b")
PRIVATE = (EMAIL, RESOURCE_ID, CREDENTIAL)
PRESERVE = {"styles", "variables", "className", "rect", "index"}


def sanitize(value):
    if isinstance(value, dict):
        return {key: item if key in PRESERVE else sanitize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, str):
        for pattern, replacement in ((EMAIL, "[email removed]"),
                                     (RESOURCE_ID, "[resource ID removed]"),
                                     (CREDENTIAL, "[credential removed]")):
            value = pattern.sub(replacement, value)
    return value


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def image_reads(image):
    return [redact.ocr_words(image), redact.ocr_words(image, boost=True)]


def ingest(source, package):
    source = source.expanduser().resolve()
    if source == package or package in source.parents:
        raise SystemExit("Source captures must live outside the package")
    rules_path = REPO / "tools/redact-rules/clerk.json"
    rules = json.loads(rules_path.read_text()) if rules_path.exists() else {"families": []}
    measurements, images, rejected = [], [], []
    for path in sorted((source / "readings").glob("*.json")):
        if path.stem.endswith("-masks"):
            continue
        raw = json.loads(path.read_text())
        if not isinstance(raw, dict) or not isinstance(raw.get("elements"), list):
            raise SystemExit(f"Not a computed-style reading: {path.name}")
        clean = sanitize(raw)
        # Guard the fields builders consume: sanitizing text must never edit a value.
        if raw.get("variables") != clean.get("variables"):
            raise SystemExit(f"Sanitizing changed CSS variables in {path.name}; refusing to write it")
        for before, after in zip(raw["elements"], clean["elements"]):
            if any(before.get(key) != after.get(key) for key in PRESERVE):
                raise SystemExit(f"Sanitizing changed a measured field in {path.name}; refusing to write it")
        write_json(package / "raw/readings" / path.name, clean)
        measurements.append({"file": path.name, "sourceSha256": sha256(path),
                             "elements": len(clean["elements"])})
    output_dir = package / "screenshots"
    output_dir.mkdir(parents=True, exist_ok=True)
    for path in sorted((source / "raw-shots").glob("*.png")):
        target = output_dir / path.name
        source_hash = sha256(path)
        exclusion = next((item for item in rules.get("excludeSources", [])
                          if item["file"] == path.name and item["sha256"] == source_hash), None)
        if exclusion:
            target.unlink(missing_ok=True)
            rejected.append(exclusion)
            print(f"{path.name}: rejected ({exclusion['reason']})", flush=True)
            continue
        image = redact.open_rgb(path)
        pixels = np.array(image)
        rects, regions = redact.rules_for(rules, f"screenshots/{path.name}", image.size)
        if regions:
            raise SystemExit("Clerk rules use exact rectangles; OCR-line regions are not supported")
        for rect in rects:
            redact.paint(pixels, rect)
        boxes = set()
        for words in image_reads(Image.fromarray(pixels)):
            boxes.update(redact.find_private(words, list(PRIVATE), True, []))
        for x0, y0, x1, y1 in sorted(boxes):
            rect = (max(0, x0 - redact.PAD), max(0, y0 - redact.PAD),
                    min(image.width, x1 + redact.PAD), min(image.height, y1 + redact.PAD), "solid")
            redact.paint(pixels, rect)
        redact.save_256(Image.fromarray(pixels), target)
        remaining = []
        for words in image_reads(redact.open_rgb(target)):
            remaining.extend(redact.find_private(words, list(PRIVATE), True, []))
        if remaining:
            target.unlink()
            raise SystemExit(f"Post-write OCR found private text in {path.name}; image rejected")
        images.append({"file": path.name, "sourceSha256": source_hash,
                       "size": list(image.size), "ocrMaskBoxes": len(boxes),
                       "ruleMaskBoxes": len(rects), "outputSha256": sha256(target)})
        print(f"{path.name}: {len(boxes)} OCR boxes, {len(rects)} explicit boxes, OCR clean", flush=True)
    write_json(package / "raw/readings/_ingest.json", {
        "method": "Sanitize display text; preserve all computed measurements. Native-pixel OCR in normal and local-contrast passes; exact image rules where present; solid surrounding-colour fill; median-cut 256 colours without dithering; post-write OCR.",
        "coordinateNote": "DOM email masks are excluded because their coordinate space differs from these screenshots. OCR operates directly on native PNG pixels.",
        "measurements": measurements, "images": images,
        "rejectedImages": rejected,
        "captureLimitations": rules.get("captureLimitations", {}),
        "excludedSourceDirectories": ["rejected-shots"],
        "previouslyRejectedImages": sorted(path.name for path in (source / "rejected-shots").glob("*") if path.is_file()),
    })
    print(f"Ingested {len(measurements)} readings and {len(images)} screenshots")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--package", type=Path, default=PACKAGE)
    args = parser.parse_args()
    ingest(args.source, args.package.resolve())
