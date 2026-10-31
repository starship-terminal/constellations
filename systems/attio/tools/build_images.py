#!/usr/bin/env python3
"""Verify originals, decode to PNG, and reproduce reviewed crops.

Usage: python3 systems/attio/tools/build_images.py ~/.design-systems/attio
Without a source directory, rebuild crops from packaged screenshots only.
Original raw files stay outside git. Pillow is required.
"""
import hashlib
import io
import json
import sys
from pathlib import Path
from PIL import Image


def build_images(package, source=None):
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
    for capture, data in originals:
        with Image.open(io.BytesIO(data)) as image:
            buffer = io.BytesIO()
            image.convert('RGB').quantize(colors=256).save(buffer, format='PNG')
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
