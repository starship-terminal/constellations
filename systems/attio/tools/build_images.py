#!/usr/bin/env python3
"""Verify originals, decode to PNG, and reproduce reviewed crops.

Usage: python3 systems/attio/tools/build_images.py ~/.design-systems/attio
Without a source directory, rebuild crops from packaged screenshots only.
Original raw files stay outside git. Pillow is required.
"""
import hashlib
import importlib.util
import io
import json
import sys
from pathlib import Path
import numpy as np
from PIL import Image

REPO = Path(__file__).resolve().parents[3]


def load_redact():
    """The library's masking primitives (tools/redact_images.py)."""
    spec = importlib.util.spec_from_file_location('library_redact_images', REPO / 'tools/redact_images.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def masked(redact, rules, image, rel):
    """The RGB image with every rectangle the package's rules name for rel painted over."""
    rgb = image.convert('RGB')
    rects, _ = redact.rules_for(rules, rel, rgb.size)
    if not rects:
        return rgb
    pixels = np.array(rgb)
    for rect in rects:
        redact.paint(pixels, rect)
    return Image.fromarray(pixels)


def build_images(package, source=None, rules=None):
    """rules: a redaction-rules dict; by default tools/redact-rules/<slug>.json when it exists."""
    package = Path(package)
    originals = []
    if source is not None:
        source = Path(source).expanduser()
        manifest = json.loads((package / 'raw/capture-manifest.json').read_text())
        # Validate the entire batch before preparing or overwriting any output.
        for capture in manifest['captures']:
            if capture['status'] != 'accepted':
                continue
            data = (source / capture['file']).read_bytes()
            if hashlib.sha256(data).hexdigest() != capture['sha256']:
                raise ValueError(f"{capture['file']}: original SHA-256 mismatch")
            with Image.open(io.BytesIO(data)) as image:
                if list(image.size) != capture['imageSize']:
                    raise ValueError(f"{capture['file']}: original dimensions mismatch")
                if image.format != capture['decodedFormat']:
                    raise ValueError(f"{capture['file']}: original format mismatch")
                image.load()
            originals.append((capture, data))

    outputs = {}
    redact = load_redact() if originals else None
    if rules is None:
        rules_path = redact.package_rules(package) if redact else None
        rules = json.loads(rules_path.read_text()) if rules_path else {}
    for capture, data in originals:
        with Image.open(io.BytesIO(data)) as image:
            buffer = io.BytesIO()
            # Mask with tools/redact-rules/attio.json (none yet) before the palette copy;
            # crops below are cut from these masked screenshots.
            masked(redact, rules, image, capture['packagedFile']).quantize(colors=256).save(buffer, format='PNG')
            outputs[capture['packagedFile']] = buffer.getvalue()
    for crop in json.loads((package / 'raw/crops.json').read_text()):
        data = outputs.get(crop['source'])
        if data is None:
            data = (package / crop['source']).read_bytes()
        with Image.open(io.BytesIO(data)) as image:
            buffer = io.BytesIO()
            image.crop(crop['box']).save(buffer, format='PNG')
            outputs[crop['file']] = buffer.getvalue()
    for name, data in outputs.items():
        (package / name).write_bytes(data)


if __name__ == '__main__':
    build_images(Path(__file__).resolve().parent.parent,
                 sys.argv[1] if len(sys.argv) > 1 else None)
