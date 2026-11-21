# Evernote

Evernote is a public note-taking product. This package finishes the signed-out capture of [https://evernote.com/](https://evernote.com/) that [site-tree.md](site-tree.md) and [screenshots/](screenshots/) already recorded on 2026-11-22. Tokens were read from computed styles on the homepage, the plans page, the AI Features page, and the empty login wall. Nothing was typed. No cookie was accepted or rejected. No identity provider was clicked. No new screenshot was taken.

The homepage and the plans page paint a cream light theme. The AI Features page puts `class="dark"` on its header and main and paints an ink field. There is no theme switch. The measurement browser preferred dark and the homepage stayed cream.

| File or Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the pages already photographed |
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core`, `light`, and `dark`, plus `$themes` |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | How those controls sit on the public pages |
| [icon.png](icon.png) | Site icon, 128 px, scaled from the 800 px apple-touch PNG |
| [screenshots/](screenshots/) | Photographs from the earlier pass. Not recaptured |
| [raw/](raw/) | The computed-style readings the tokens were built from |
| [tools/](tools/) | `build_tokens.py` and `build_style_guide.py` |

`catalog.json` and `webapps-manifest.json` were left alone. DESIGN.md was not written.

## How the values were read

An incognito preview tab opened [https://evernote.com/](https://evernote.com/), then [https://evernote.com/en-us/compare-plans](https://evernote.com/en-us/compare-plans), then the empty wall at [https://accounts.evernote.com/login](https://accounts.evernote.com/login), then [https://evernote.com/en-us/features/ai-features](https://evernote.com/en-us/features/ai-features). Colours are `getComputedStyle` values, written as hex. Custom properties were read from `:root` and from the `.dark` header. The cookie banner was on screen and was not accepted or rejected. No button that starts login, signup, or a plan was clicked.

The elephant mark is the site favicon at `https://evernote.com/images/evernote-logo-icon.svg`, fill `#00A82D`. [icon.png](icon.png) is the apple-touch PNG at `https://evernote.com/images/evernote-logo-ios.png`, 800 px, scaled to 128 px.

## What to distrust

The stylesheet hover rule `.hover:bg-green:hover` is `#00a82d`. No button was hovered, so that green is a declared colour, not a painted hover. The dark set's secondary text and stroke tokens are computed custom properties on the dark header. They were not sampled from a painted card. The homepage dark band paints `#262626` as a section background while the page stays light. Screenshots are from the earlier pass. Read colour from [tokens.json](tokens.json).

## Fonts

Figtree is the marketing face. Inter is the body and auth face. Both load from the site as `Figtree, "Figtree Fallback"` and `Inter, "Inter Fallback"`. The font files are not in this package. The style guide falls back to the system sans.

## Coverage

| Item | Status |
|---|---|
| Colour, light | Captured. [tokens.json](tokens.json) |
| Colour, dark page | Captured on AI Features, where header and main carry `class="dark"` |
| Theme switch | None on the public pages |
| Type | Captured for h1, h2, lede, nav, and the auth field |
| Button, chip, outline, nav, field | Default only. Not clicked |
| Hover, focus, pressed, disabled loading | Not captured. Empty Continue is grey because the field is empty |
| Login, signup, Google, Apple, checkout | Stopped. Walls were already photographed |
| Cookie accept and reject | Stopped |
| New screenshots | Not taken. [screenshots/public/](screenshots/public/) stays as it was |

## Do and don't

- Paint the public page cream. The header and footer are `#f9f6f2`. [screenshots/public/home-light-desktop.png](screenshots/public/home-light-desktop.png)
- Paint Start for free ink on cream pages and lime on the AI Features page. [screenshots/public/ai-features-light-desktop.png](screenshots/public/ai-features-light-desktop.png)
- Keep the hero card sand, 16px radius, with a `#e7e7e7` hairline. Same homepage shot.
- Leave login, signup, plan start, and the cookie banner closed. [screenshots/public/login-wall-desktop.png](screenshots/public/login-wall-desktop.png)

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Those commands read [raw/readings.json](raw/readings.json) and [tokens.json](tokens.json). They do not open the site.
