# Gemini Notebook (NotebookLM) design reference

A token set and component reference for Google's Gemini Notebook (formerly NotebookLM), for building mockups in Figma or Paper that match the product. It was extracted from notebook.google.com on 2026-09-25 while signed in, and covers the UI generation that is live for this account.

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` (palettes, type, radii, shadows, spacing, sizes, breakpoints, motion) plus `light` and `dark` semantic sets and a `$themes` list. Import with Tokens Studio → Load from file. |
| [style-guide.html](style-guide.html) | One self-contained page that renders every token and component in both themes (toggle top right). Open it in a browser, or paste sections into Paper. |
| [components.md](components.md) | The discovery list, then each component's anatomy, measurements, tokens and states with screenshots, then the Gaps. |
| [screenshots/](screenshots) | `{page}-{theme}-{state}.png` captures of the real product. |
| [raw/](raw) | The unprocessed readings: every CSS custom property value (`*.tsv`) and per-element computed styles (`measurements.md`). |
| [tools/](tools) | `build_tokens.py` (raw → tokens.json) and `build_style_guide.py` (tokens.json + template → style-guide.html). |

## How the values were read

Colours, type, radii and shadows come from the running product: CSS custom properties on `body` read with `getComputedStyle` (the product's own `--nlm-*` tokens are declared as `light-dark(light, dark)`, so one read gives both themes), `--mat-sys-*` read once per theme, and computed styles on each component. State styles (hover, focus, disabled) come from the stylesheet rules themselves where the live state could not be held. Every token records its source in `$extensions.source`. A token whose source says **estimated** was sampled from a screenshot, because that part of the UI (flashcards, quiz, mind map) renders in a cross-origin iframe.

## What the images no longer show

The captures came from the owner's account, so the screenshots showed its notebook titles (with course codes), source file names, chat and quiz text, studio items, the owner's name and email in the share dialog, and the account photo. On 2026-10-11 those regions were painted out of the finished PNGs with [tools/redact_images.py](../../tools/redact_images.py) and [tools/redact-rules/notebooklm.json](../../tools/redact-rules/notebooklm.json), because no page copies survive to render again. Every text line that is not interface wording is painted out (the rules list the interface words to keep), the header's notebook title is cleared, and photographs are pixelated. Layout, panels, icons, counts, dates and the interface's own labels are untouched. All 34 screenshots remain.

Limits: text dimmed behind a modal was found with a contrast-flattened second read and a few fixed rectangles, and can leave unreadable fragments. The Discover page's featured notebooks are Google's own cover art and are left as captured.

## Rebuild

```bash
python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

Edit `raw/*.tsv` or the builders, never the generated files.

## Use in Figma

Import `tokens.json` with Tokens Studio, choose the Light or Dark theme, and set fonts to Google Sans (display and headlines) and Google Sans Text (everything else) if you have them installed. Use Material Symbols Outlined for icons at 16/18/20/24px. Anything the capture could not reach is listed under Gaps in [components.md](components.md#gaps).
