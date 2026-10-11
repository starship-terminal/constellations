# Hevy design reference

A token set and component reference for Hevy, the workout-logging app for iOS, for building a native iOS fitness app (SwiftUI) that borrows its proportions and structure: a dense set table, one accent colour, a pale grey fill for everything tappable, small corners and iOS 26 glass chrome. It was captured from the shipped app, version 3.1.16 on iOS 26, with a free account on 2026-10-10, through iPhone Mirroring, in light and dark mode. The device screen is 390 x 844 pt and the captures are 1 px = 1 pt, with the screen offset by (8, 38) px inside each PNG.

It holds 200 captures: 17 light captures of the main flows, 17 dark ones, and 166 detail pages, sheets, menus, dialogs and toasts (dark). [page-tree.md](page-tree.md) lists every screen reachable in the app and whether it was opened.

This package contains no Hevy code, and no Hevy artwork has been redrawn. The screenshots and the visual system they show are Hevy's property ([docs/RIGHTS.md](../../docs/RIGHTS.md)). Borrow structure and proportions, not the logo, icons, exercise illustrations or brand colours.

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` (radii, spacing, sizes, border widths, the font family, weights and nine composite type styles), `light` and `dark` (36 semantic colours each, with identical keys: `color.bg`, `color.surface`, `color.border`, `color.divider`, `color.text`, `color.accent`, `color.tint`, `color.state`, `color.set`, `color.banner`, `color.badge`, `color.medal`, `color.scrim`, `color.switch`, `color.button`), plus `$themes` and `$metadata.tokenSetOrder`. Every token has `$value`, `$type` and `$extensions.source` = `{evidence, capture}`. Dimensions are `"16px"` and 1 px is 1 pt. |
| [style-guide.html](style-guide.html) | One self-contained page generated from `tokens.json`: every colour with light and dark side by side, radii, spacing, sizes, the type scale and component specimens (buttons, chips, set rows, the rest timer bar, a routine card, settings rows), with a Light/Dark toggle. Open it straight from disk. |
| [components.md](components.md) | The component inventory: one entry per component with size, radius, fill (as token names), states and a link to the capture that shows it, then a Gaps section. |
| [page-tree.md](page-tree.md) | Every screen, tab, sheet, menu, dialog and toast in Hevy 3.1.16 and whether it was explored, with links to the captures. |
| [screenshots/light/](screenshots/light) | 17 light captures of the main flows, `01-home.png` to `17-workout-settings-toggles.png`. |
| [screenshots/dark/](screenshots/dark) | 17 dark captures, `d01-theme-setting.png` to `d17-home.png`. |
| [screenshots/pages/](screenshots/pages) | 166 detail pages, sheets and menus (dark): `p01` to `p35` from the first pass and `t01` to `t131` from the tree pass. |
| [raw/hevy-style-measured.md](raw/hevy-style-measured.md) | The measured reference every value in `tokens.json` was taken from: colours in both themes, typography, layout, component tables and the patterns. Capture links point into `screenshots/`. |
| [tools/build_style_guide.py](tools/build_style_guide.py) | The one builder. Standard library only, deterministic. |

## Masked regions

The captures come from the owner's own account. On 2026-10-12 every region
showing who the account belongs to or who it interacts with was painted over
with the surrounding fill: usernames, display names, avatars and photos, bio,
follower counts, workout and routine titles, dates of the owner's activity,
post and comment text, other people's names and photos, and body data. A
blank area in a screenshot is a mask, not part of Hevy's design. Exercise
names, illustrations, set tables and every piece of UI chrome are untouched,
and no token was read from a masked area.

## How the values were read

Hevy is a native app, so there is no CSS to read. Every number came from the PNGs, which are lossless and 1 px = 1 pt. Surfaces were read from flat fills, which are exact. Text colours were read from the darkest (or lightest, in dark mode) anti-aliased pixel, so the true value is the same or slightly further from the background. Corner radii were estimated from the diagonal inset of each corner, and font sizes from letter height, so treat those as plus or minus 2 pt for radius and plus or minus 1 pt for size. Sizes and positions were read off pixel edges and are exact to the point.

The measured reference grades each value on four levels. They map onto the labels in [docs/EVIDENCE.md](../../docs/EVIDENCE.md) like this, and `$extensions.source.evidence` in `tokens.json` uses the right-hand column:

| Level in the measured reference | Label in tokens.json | Meaning here |
|---|---|---|
| measured (a surface, or a size read off pixel edges) | Sampled | An exact flat fill, or an exact edge position. A displayed sRGB value, not proof of the token behind it |
| measured (text) | Sampled (text) | Darkest anti-aliased pixel of the text. The true value is the same or slightly darker |
| estimated | Derived | Worked out from pixels (a radius from a diagonal inset, a font size from letter height), or a value filled in from the closest documented role |
| observed | Observed | Visible in a capture, no value read. Listed in `components.md` |
| unknown | Not captured | Not determinable from pixels. Used on `fontFamily.base` |

Where a value was documented in one theme only, the other theme is filled from the closest documented role and marked Derived, with the reason in `$description`. This happens for the light sheets (the detail pages were captured in dark only), the light medals, set types and `accent.glass`, and the dark `button.disabledGlass` and `state.live`. Three values were read from the captures while building this package because the measured reference gave no number: the two `switch.offTrack` greys (it says only "light grey") and the dark `divider`. Their `$description` says so. The sheet and wheel band values from the reference were re-checked against p10, p16, p18 and t70.

`capture` in each token's source is a path inside this package: the screenshot a value was read from, or a section of `raw/hevy-style-measured.md` where the value is a Derived scale step or has no single capture.

The logging screens were captured with throwaway workouts that were all discarded, and the appearance was switched between Light and Dark for the two sets. Other users, the owner's private profile values and nearby gyms are blurred in the captures.

## Evidence labels

| Label | Where it appears in this package |
|---|---|
| Sampled | Flat surface fills and edge-measured sizes: the page, card, raised fills, accent, tints, state fills, `size.*`, `space.*` that were measured |
| Sampled (text) | Text and icon colours, borders and the list divider, set type and destructive colours |
| Derived | Radii, font sizes and weights, the spacing scale steps, the Pro and medal colours in the theme they were not read in, the scrim |
| Observed | Components listed in `components.md` with a capture but no value read from them (the radar chart, plan cards, the share card composer) |
| Not captured | `fontFamily.base`, and everything listed in the Gaps section of `components.md` |

## What to distrust

- **The font.** Hevy's face is unknown. It is a geometric sans with a circular "o" and a two-storey "a", and it is not SF Pro. A Behance concept board used Poppins, which has a similar shape, but that was the concept author's choice and is not confirmed for the shipped app. `fontFamily.base` is `"system"`: use the platform face and expect slightly different text widths. Font sizes are estimates, and no line heights were measured.
- **Scrolling captures show the top only.** Scrolling inside iPhone Mirroring moves a few points at a time, so long pages were captured from the top, and what sits below the fold is unseen.
- **No keyboard.** iPhone Mirroring takes typing from the Mac keyboard and hides the software keyboard, so no capture has one.
- **No network error state.** Turning off the phone's connection would also cut iPhone Mirroring.
- **No pressed or long-press states, no motion.** The captures are stills made with clicks. Swipe-only content (the image carousel's second page, share card templates 2 to 8) was unreachable.
- **Radii are estimates.** `radius.control` 8, `radius.button` 10 and `radius.card` 10 are good to plus or minus 2 pt.
- **Dark text and border ranges.** `text.secondary` and `text.tertiary` are ranges in the source (dark `#64666A` to `#696B6F` and `#4A4A4A` to `#626468`; light tertiary `#AAAFB2` to `#B7BABC`). Each token holds the first value of its range and says so.
- **The scrim.** The source gives black at about 70%, but the light dialog capture shows `#434343` over white, which works out nearer 74%. The token follows the documented 70%.
- **Screenshots are 256-colour PNGs.** Flat UI colours survive exactly. Read values from the tokens, not the images.
- **System glass.** The tab bar and nav bar buttons are iOS 26 glass. Their blur and tint come from the system, so the tokens only describe the colours Hevy puts under or on them.

## Fonts

| Family | Used for |
|---|---|
| Unknown geometric sans | Everything in the interface. The style guide falls back to the system sans. No font file is committed or needed |

Type roles, sizes in points: large title 26 bold, nav bar title 17 medium, card and exercise title 17 semibold, exercise name link 16 semibold, body 16 regular, secondary lines 15 regular, small labels 13 regular, column headers 12 regular in capitals, rest timer digits 28 semibold. Weights in the source are named, not numbered: regular 400, medium 500, semibold 600 and bold 700 are the usual mapping. The timer digits' weight is a guess.

## Rebuild

`tokens.json` and `components.md` are written by hand from `raw/hevy-style-measured.md`, so there are no builders for them. The style guide is generated:

```bash
python3 tools/build_style_guide.py
```

`build_style_guide.py` reads `tokens.json` and writes `style-guide.html`, turning every token into a CSS custom property so the page cannot drift from the file. It is deterministic: a rebuild that changes nothing proves the page still matches the tokens.

```bash
python3 tools/build_style_guide.py && git status --short .
```

## Use in Figma and in SwiftUI

Import `tokens.json` with Tokens Studio and choose the Light or Dark theme, or read it with Style Dictionary. For SwiftUI, a colour asset per semantic key with a light and a dark variant maps one to one: the key names (`color.surface.raised`) are the contract, and the same keys exist in both sets. Sizes and radii in `core` are points. Use the standard iOS 26 components for the tab bar, nav bar buttons, sheets, switches and wheel pickers rather than redrawing them.

## Hevy's patterns in one place

- One accent colour does all the work. Everything else is navy-black text on white, with one pale grey-blue fill (`color.surface.raised`) for anything tappable that is not primary.
- Borders are rare. Separation comes from the grey fill, 16 pt margins and pale dividers. Routine cards and inputs are the exceptions, and dark mode drops the card border.
- Corners are small and consistent: about 8 for short controls, about 10 for buttons and cards, fully round for chips and badges.
- Lists are dense: 80 pt for two-line rows with an image, 60 pt for settings, a 47 pt pitch for set rows.
- Success green, destructive red and warm-up orange are slightly different in dark rather than reusing the light hex.
