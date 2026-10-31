#!/usr/bin/env python3
"""Decode API JPEG captures into true PNG and reproduce reviewed crops.

Usage: python3 systems/attio/tools/build_images.py ~/.design-systems/attio
Original raw files stay outside git. Pillow is required.
"""
import json,sys
from pathlib import Path
from PIL import Image
p=Path(__file__).resolve().parent.parent
if len(sys.argv)>1:
 src=Path(sys.argv[1]).expanduser()
 manifest=json.loads((p/'raw/capture-manifest.json').read_text())
 for c in manifest['captures']:
  if c['status']=='accepted':
   Image.open(src/c['file']).convert('RGB').quantize(colors=256).save(p/c['packagedFile'],format='PNG')
for c in json.loads((p/'raw/crops.json').read_text()):
 Image.open(p/c['source']).crop(c['box']).save(p/c['file'],format='PNG')
