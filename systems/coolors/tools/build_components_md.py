#!/usr/bin/env python3
"""Write components.md from the Coolors computed-style record.

ADAPTED_FOR is set so this is not the kit's ChatGPT example. The kit's
reader expects a components[] list this capture does not have, so this
file writes the inventory from raw/components-computed.json directly.
"""
import json
from pathlib import Path

ADAPTED_FOR = "coolors"

ROOT = Path(__file__).resolve().parent.parent
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())
D = C["desktop"]

text = f"""# Coolors components

Measured on the signed-in Coolors page on {C["captured"]}, theme `{C["themeOnScreen"]}`, desktop CSS viewport {D["viewport"]["innerWidth"]}x{D["viewport"]["innerHeight"]} at devicePixelRatio {D["viewport"]["devicePixelRatio"]}. Phone CSS viewport was 390x844. Values are `getComputedStyle` readings in [raw/components-computed.json](raw/components-computed.json).

## Button

Header and generator toolbar buttons are `a.btn.btn--s`. Height 36px, radius 8px, padding 0 12px, Inter 15px weight 500.

| Variant | Fill | Label | Where |
|---|---|---|---|
| transparent | {D["buttonTransparent"]["backgroundColor"]} | {D["buttonTransparent"]["color"]} | Tools, View, Export, Save |
| selected | {D["buttonSelected"]["backgroundColor"]} | {D["buttonSelected"]["color"]} | open toolbar popover |
| go pro | {D["buttonGoPro"]["backgroundColor"]} | {D["buttonGoPro"]["color"]} | header Go Pro |
| primary | {D["primaryButtonAccount"]["backgroundColor"]} | {D["primaryButtonAccount"]["color"]} | account page primary |
| icon | transparent | ink | 36x36 toolbar icons |

## Header

Height {D["header"]["height"]}. Fill {D["header"]["backgroundColor"]}. Shadow `{D["header"]["boxShadow"]}`. Logo at the left, Tools, Go Pro, and the avatar at the right when signed in. Sign in and Sign up are `display: none`.

## Generator column

Desktop columns are {D["colorColumn"]["width"]} by {D["colorColumn"]["height"]} (`.generator_color_background`). The hex is Inter {D["hex"]["fontSize"]} weight {D["hex"]["fontWeight"]}, tracking {D["hex"]["letterSpacing"]}. Ink flips between white and black against the column. Phone columns stack at 390x146, and the hex chip is 16px weight 600 with a 10px radius.

## Text input

Account text fields are {D["textInputAccount"]["height"]} tall, radius {D["textInputAccount"]["borderRadius"]}, padding {D["textInputAccount"]["padding"]}, {D["textInputAccount"]["fontSize"]}. Focus border is `#3b82f6` (`--input-focus-border`). Error border is `#ef4444`.

## Display type

The account page h1 is Inter {D["h1Account"]["fontSize"]} weight {D["h1Account"]["fontWeight"]}, tracking {D["h1Account"]["letterSpacing"]}, line-height {D["h1Account"]["lineHeight"]}, color {D["h1Account"]["color"]}.

## Gaps

No focus ring was painted on the controls that were measured. Checkbox, switch, toast, table, and menu rows were not opened as their own screens. Dark theme was not switched on, because the theme control sits in the account menu and writes a preference.
"""
(ROOT / "components.md").write_text(text)
print("components.md", len(text))
