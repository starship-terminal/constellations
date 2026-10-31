#!/usr/bin/env python3
"""Rebuild verified native-pixel crops and their inventory from accepted screenshots."""
import json
from pathlib import Path
from PIL import Image
P=Path(__file__).resolve().parent.parent
spec=json.loads((P/'tools/crops.json').read_text())
lines=['# Components','', 'Observed live in the official Edumation demo, light theme. Crops use native screenshot pixels, not inferred CSS rectangles. Each crop was visually checked. No 2x upsampling: these are 1x captures.','', '| Component / state | Screenshot | Crop | Token group |','|---|---|---|---|']
for row in spec:
 im=Image.open(P/'screenshots'/row['source']);x,y,w,h=row['box'];assert x>=0 and y>=0 and x+w<=im.width and y+h<=im.height
 dst=P/'components/crops'/f"{row['name']}.png";im.crop((x,y,x+w,y+h)).save(dst)
 lines.append(f"| {row['label']} | [{row['source']}](screenshots/{row['source']}) | ![{row['label']}](components/crops/{row['name']}.png) | {row['tokens']} |")
lines+=['','## Additional captured states','','- [Selected donut percentage radio](screenshots/donut-percentages-both-light-desktop.png), [column Link radio](screenshots/model-column-link-radio-light-desktop.png), and [chart color picker](screenshots/donut-color-picker-light-desktop.png). These have screenshot/CSS evidence but no new component token mapping.','- [Metadata drawer](screenshots/model-info-light-desktop.png), [query error](screenshots/model-students-error-light-desktop.png), [permission error](screenshots/report-settings-denied-light-desktop.png), and [dashboard picker empty search](screenshots/report-dashboard-search-empty-light-desktop.png).','','## Gaps','','Selected Dark forms and collection states are captured in the interaction inventory; Dark tokens are not yet mapped. No persistent pressed state, toast or destructive dialog. Hover is incidental and not independently measured. Numeric fields show automatic focus; this does not establish keyboard focus-visible parity. Switches are observed on/off but their track CSS was not tokenised. Chart axes screenshot shows the upper scroll section only. Source CSS enumeration is partial, so missing variables are not proof of absent product tokens. No brand assets are licensed for reuse.']
(P/'components.md').write_text('\n'.join(lines)+'\n')
