#!/usr/bin/env python3
"""Generate native-pixel crops and component index from reviewed coordinates."""
import json,pathlib
from PIL import Image
R=pathlib.Path(__file__).resolve().parents[1]
crops=json.loads((R/'tools/crops.json').read_text());lines=['# Cloudflare components','','Crops are Observed live product evidence at native capture pixels. Their paired raw readings carry Measured computed CSS. Screenshots are quantized; never sample their colors.','','| Component/state | Source | Evidence |','|---|---|---|']
for name,spec in crops.items():
 source=R/'screenshots'/spec['shot'];im=Image.open(source);box=spec['box'];assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height
 im.crop(box).save(R/'components/crops'/f'{name}.png')
 lines.append(f'| {name.replace("-"," ")} | [Full state](screenshots/{source.name}) | [Crop](components/crops/{name}.png) |')
lines+=['','## Tokens','','Inputs use `dark.component.input`, links use `dark.component.link`, headings use `core.typography.heading`. Theme colors are in `dark` and, where captured, `light`. The public site is separately labelled `marketing`. Each raw file lists element geometry and computed CSS for the same viewport state.','','## Gaps','','Not captured: exhaustive hover, held-pressed, loading, invalid-form and error variants; success toasts after writes; destructive confirmations; avatar imagery; light/dark parity for every component. Radio controls are visible in the separately captured light rule footer; the dark initial editor viewport does not establish radio coverage. Hidden one-pixel inputs are excluded from token selection.']
(R/'components.md').write_text('\n'.join(lines)+'\n')
