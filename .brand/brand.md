# Constellations brand kit

Mark 2-7. Kit folder: `.brand/`. Marks are letter-free; only the lockups and banners carry the name.

## Palette

| Role | HEX | RGB |
|---|---|---|
| Background | #0A0E1A | 10 14 26 |
| Orange | #E36F20 | 227 111 32 |
| Orange | #9B390D | 155 57 13 |
| Orange | #D25512 | 210 85 18 |
| Orange | #A53E0E | 165 62 14 |
| Orange | #C14A10 | 193 74 16 |
| Orange | #CA4F10 | 202 79 16 |
| Orange | #AE430F | 174 67 15 |
| Teal | #26707B | 38 112 123 |
| Teal | #144A51 | 20 74 81 |
| Cream | #EEC9A3 | 238 201 163 |
| Teal | #19555F | 25 85 95 |
| Cream | #FBE1C8 | 251 225 200 |
| Teal | #5A9696 | 90 150 150 |
| Mono cream / charcoal / black / white | #F2E0CC / #1C1B1F / #000000 / #FFFFFF | 242 224 204 / 28 27 31 / 0 0 0 / 255 255 255 |

The vector master has 13 colour layer(s). This is above the 2 to 3 colour house guideline because the faceted artwork depends on its shaded tones; the actual colours are kept exactly (no posterising). Use the mono set where a strict 2 to 3 colour limit applies.

Constellations sits on navy #0A0E1A rather than charcoal.

## Typeface

Cormorant Garamond (Google Fonts, SIL OFL 1.1): Bold (heaviest, for small lockups) for the name in lockups and banners, SemiBold for text and captions. Delicate high-contrast serif with an astronomical-atlas tone; the heaviest weight keeps small lockups legible. Names are outlined in every SVG/PDF; install the TTFs in `fonts/` for new text. Licence: `fonts/OFL.txt`.

## Rules

- Clear space: x = 0.25 x mark height (tight bounding box) on all sides.
- Minimum size: 32 px tall (digital) / 10 mm (print). Below that use `png/favicon-16.png`.
- Do: use the supplied files; keep clear space; cream marks go on dark or mid backgrounds, use the light version (or mono charcoal) on light.
- Don't: stretch or skew, recolour, add shadows/glow/gradients, or place on busy backgrounds.

## Files

### `png/`
Raster set (avatars, logos, mark-transparent, favicons + .ico, apple-touch/PWA icons, maskable, social preview mark-only)

`apple-touch-icon-180.png`, `avatar-1024.png`, `avatar-500.png`, `favicon-16.png`, `favicon-32.png`, `favicon-48.png`, `favicon.ico`, `icon-192.png`, `icon-512.png`, `logo-rounded-160.png`, `logo-rounded.png`, `logo-square-2048.png`, `logo-square.png`, `mark-transparent-2048.png`, `mark-transparent.png`, `maskable-512.png`, `social-preview-1280x640.png`

### `svg/`
Vector masters: full colour on background, full colour transparent, one-colour versions. Palette-exact, one filled path per colour layer

`mark-color-on-bg.svg`, `mark-color.svg`, `mark-mono-black.svg`, `mark-mono-charcoal.svg`, `mark-mono-cream.svg`, `mark-mono-white.svg`

### `pdf/`
Vector PDFs generated from the SVGs

`mark-color-on-bg.pdf`, `mark-color.pdf`, `mark-mono-black.pdf`, `mark-mono-charcoal.pdf`, `mark-mono-cream.pdf`, `mark-mono-white.pdf`

### `mono/`
One-colour marks (cream #F2E0CC, charcoal #1C1B1F, black, white) as SVG and transparent PNG, with knockouts so the silhouette reads

`mono-black.png`, `mono-black.svg`, `mono-charcoal.png`, `mono-charcoal.svg`, `mono-cream.png`, `mono-cream.svg`, `mono-white.png`, `mono-white.svg`

### `lockups/`
Mark + name (set in the mark typeface, outlined). Horizontal and stacked x dark / light / transparent (for dark use) / transparent-onlight, as SVG, PDF and PNG

`constellations-horizontal-dark.pdf`, `constellations-horizontal-dark.png`, `constellations-horizontal-dark.svg`, `constellations-horizontal-light.pdf`, `constellations-horizontal-light.png`, `constellations-horizontal-light.svg`, `constellations-horizontal-transparent-onlight.pdf`, `constellations-horizontal-transparent-onlight.png`, `constellations-horizontal-transparent-onlight.svg`, `constellations-horizontal-transparent.pdf`, `constellations-horizontal-transparent.png`, `constellations-horizontal-transparent.svg`, `constellations-stacked-dark.pdf`, `constellations-stacked-dark.png`, `constellations-stacked-dark.svg`, `constellations-stacked-light.pdf`, `constellations-stacked-light.png`, `constellations-stacked-light.svg`, `constellations-stacked-transparent-onlight.pdf`, `constellations-stacked-transparent-onlight.png`, `constellations-stacked-transparent-onlight.svg`, `constellations-stacked-transparent.pdf`, `constellations-stacked-transparent.png`, `constellations-stacked-transparent.svg`

### `banners/`
README banner 1280x320 and social preview with name 1280x640, both on dark

`banner-readme-1280x320.png`, `banner-readme-1280x320.svg`, `social-preview-name-1280x640.png`, `social-preview-name-1280x640.svg`

### `fonts/`
Static TTFs for the mark's typeface (name and body weights) and the SIL OFL licence

`CormorantGaramond-Bold.ttf`, `CormorantGaramond-SemiBold.ttf`, `OFL.txt`

`brand-sheet.pdf`: one-page brand sheet (versions, palette, typeface, clear space, minimum size, dos and don'ts). `brand.md`: this file.

## Vector fidelity

SVG (rendered at 1024) vs the flat-palette raster: 0.0004% of pixels differ by more than 40/255 away from colour edges (0.784% including the 1 px edge antialiasing); mean abs diff 0.58/255. Node counts: colour 6212, mono 1045.
