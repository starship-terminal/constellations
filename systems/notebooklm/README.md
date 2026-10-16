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

## Do and don't

1. **Do separate regions by fill alone.** The workspace is three white panels (radius 16, no border, no shadow) on the pale lavender `#edeffa` page with a 16px gutter, and the header has no fill at all; in dark the panels are `#22262b` on `#1a1d22`. Notebook cards and dialogs have no shadow either; only menus, popovers and the toast float. See [notebook-light-default](screenshots/notebook-light-default.png), [notebook-dark-flashcards-front](screenshots/notebook-dark-flashcards-front.png) and [home-light-sort-menu](screenshots/home-light-sort-menu.png).
2. **Do split filled buttons by job: black for creating, blue for confirming.** Page-level create actions ("Create new", "Create notebook", "Add note", "Try it") are black pills that turn white in dark. The blue `#4259ff` fill is kept for the last button of a dialog or step (Create, Save, Delete, the quiz's "Next") and stays the same blue in both themes. Everything else is an outlined pill with a 1px `#dde1eb` hairline, or plain text. See [home-light-default](screenshots/home-light-default.png), [home-dark-default](screenshots/home-dark-default.png), [notebook-light-configure-chat-dialog](screenshots/notebook-light-configure-chat-dialog.png) and [mobile-dark-configure-chat-dialog](screenshots/mobile-dark-configure-chat-dialog.png).
3. **Do show "selected" with the pale lavender fill.** The current section tab, the checked view-toggle segment, the Source guide pill, the user's chat bubble and the create card's plus circle all use `surface.selected` (`#edeffa`, dark `#2f334b`) rather than the accent. The one exception is the choice chips in dialogs, which fill blue with a leading check. See [home-light-collections-empty](screenshots/home-light-collections-empty.png), [notebook-light-flashcards-front](screenshots/notebook-light-flashcards-front.png) and [chip-toggle-light-states](screenshots/chip-toggle-light-states.png).
4. **Do keep colour in the content and the chrome neutral.** Colour comes from the pastel notebook cards, the pastel Studio tiles (one colour pair per output type) and the red and blue file-type icons. Icon buttons, panel titles and toolbars are black or grey, and ticked source checkboxes are grey, not blue, so a long list stays quiet. See [notebook-light-default](screenshots/notebook-light-default.png), [home-light-grid](screenshots/home-light-grid.png) and [studio-light-tile-hover](screenshots/studio-light-tile-hover.png).
5. **Don't colour destructive actions red.** The delete confirmation's "Delete" is the same blue filled button as any other confirm, beside an outlined "Cancel", and "Delete" in the card menu has the same grey outlined icon as the other items. See [home-light-delete-confirm-dialog](screenshots/home-light-delete-confirm-dialog.png) and [home-light-card-menu](screenshots/home-light-card-menu.png).

## Rebuild

```bash
python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

Edit `raw/*.tsv` or the builders, never the generated files.

## Use in Figma

Import `tokens.json` with Tokens Studio, choose the Light or Dark theme, and set fonts to Google Sans (display and headlines) and Google Sans Text (everything else) if you have them installed. Use Material Symbols Outlined for icons at 16/18/20/24px. Anything the capture could not reach is listed under Gaps in [components.md](components.md#gaps).
