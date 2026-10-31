"""Rebuild verified crops using reviewed native PNG coordinates."""
from pathlib import Path
import json
from PIL import Image
HERE=Path(__file__).resolve().parent.parent
def build():
    crops=json.loads((HERE/'tools/crops.json').read_text())
    lines=['# Components','', 'Observed live components. Each crop is from a reviewed viewport screenshot, not a reconstructed component. CSS readings are in [raw/](raw/). Dimensions use native screenshot pixels (1 image pixel per CSS pixel for these captures, despite desktop DPR 2).','']
    for name,(shot,box) in crops.items():
        im=Image.open(HERE/'screenshots'/f'{shot}.png')
        assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height
        im.crop(box).save(HERE/'components/crops'/f'{name}.png')
        lines += [f'## {name}',f'![{name}](components/crops/{name}.png)',f'Source: [full screenshot](screenshots/{shot}.png). Observed; see corresponding raw reading for measured values.','']
    lines += ['## Gaps','Table cells, row detail panels, schema navigation, table filters and main SQL workspace unavailable while both projects were paused. Side-panel SQL was viewed empty; no SQL was executed. No hover/pressed parity or validation errors claimed.']
    (HERE/'components.md').write_text('\n'.join(lines)+'\n')
if __name__=='__main__':build()
