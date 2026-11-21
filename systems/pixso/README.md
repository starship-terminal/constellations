# Pixso design reference

Pixso is a collaborative UI and UX design tool. This package is the public site at https://pixso.net/, captured 2026-11-21, signed out, in headless Chromium. Desktop is 1440×900. Phone is 390×844. One light theme. The signed-in editor was not opened.

The site paints black text on white, a near-black button for Get started, and a blue brand (`#336fff`) declared as `--v2--color-bg-brand-normal` and `--pxn-blue`. Figtree is the painted family. Header and footer tokens use `--pxn-*` and `--pxf-*`.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, from the favicon at pixso.net |
| [tokens.json](tokens.json) | DTCG tokens: `core` scales and `light` roles. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Generated from tokens.json and this README. One theme, no provenance. |
| [style-guide.html](style-guide.html) | Renders the light roles, type, the Get started button and a field. |
| [components.md](components.md) | Public components that were seen, with gaps. |
| [patterns.md](patterns.md) | Header, menus, pricing, contact form, login wall. |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or wall. Mapped before screenshots. |
| [screenshots/](screenshots/) | `{page}-light-{state}.png` at desktop, `mobile-` prefix at phone width. |
| [raw/](raw/) | `css-vars.json`, the declared and computed readings. |
| [tools/](tools/) | Capture runner and `build_tokens.py`, `build_style_guide.py`. |

## Brief

<!-- brief:start -->

Read [tokens.json](tokens.json) before designing in this style. This Brief is written by hand because this capture does not edit catalog.json, so `make brief` cannot see the package.

### Principles

1. Paint the page white and the text black.
2. Use the near-black button for the primary action.
3. Keep the blue brand for links and focus.
4. Set labels in Figtree.
5. Stop at the login wall.

Each rule links a screenshot under [Do and don't](#do-and-dont).

### Using tokens

| Role | light |
|---|---|
| page | #ffffff `light.background.page` |
| surface | #f7f7f9 `light.background.surface` |
| text | #000000 `light.text.primary` |
| muted | #647084 `light.text.muted` |
| accent | #336fff `light.background.brand` |
| border | #edf0f4 `light.border.default` |

Font: Figtree, then Arial, Helvetica Neue, Microsoft YaHei, Helvetica, sans-serif (`core.font.family.sans`).

### Using components

Read [components.md](components.md), [patterns.md](patterns.md), and [style-guide.html](style-guide.html). Crops were not cut.

### Accessibility

Text on page is black on white. Muted `#647084` on white is the header muted token. Focus on the login email field is a 2px `rgb(31, 97, 255)` border, measured before blur. Contrast ratios are not computed in this hand-written Brief.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. This capture does not edit catalog.json, so `make grade` was not run for this package. A catalog row would be required before the scorecard can review it.

Layout: no `components/` crops and no `icons/`. Brand artwork and product icons are not kept ([docs/RIGHTS.md](../../docs/RIGHTS.md)).

<!-- health:end -->

## How the values were read

Custom properties were read from the live home page CSSOM in headless Chromium at 1440×900 on 2026-11-21. `:root` declares a Bootstrap-like palette (`--primary`, `--success`, `--danger`) plus `--action`, `--support`, breakpoints, `--header-height` and `--content-max-width`. The header declares `--pxn-blue`, `--pxn-ink`, `--pxn-muted`, `--pxn-border`. The footer declares `--pxf-text`, `--pxf-muted`, `--pxf-rule`. Brand fill is `--v2--color-bg-brand-normal` `#336fff`, hover `--v2--color-bg-brand-hover` `#4381ff`.

Painted colours that are not those variables were read with `getComputedStyle` on the element in the named state: body, `h1`, header Pricing link, Get started (`.login-btn.px-common-btn`), Log in, the contact name field at rest, and the login email field at rest and in focus. Screenshots were not sampled.

`--font-family-sans-serif` declares Poppins. Body computed font-family is Figtree. The tokens record both. Figtree is what the page paints.

## What to distrust

- Status colours (`--success`, `--warning`, `--danger`, `--info`) are declared on `:root` and were not seen painted on a public success, warning, or error control.
- `--font-family-sans-serif` is Poppins. The painted UI is Figtree. Use `core.font.family.sans`.
- The login email field's first paint in a fresh document was already focused (2px blue border). The resting 1px border was read after blur.
- Get started hover is a screenshot only. The hover fill was not read.
- Pressed, disabled, loading, and error states were not read.
- Screenshots are 256-colour PNGs after quantize. Read colours from tokens.json.
- Community file pages and plugin details are public demos of other people's published files. They are not the signed-in editor.
- `/plugins/` and `/community/home` scroll inside `#app` (`overflow: auto`, body overflow hidden). The plugins full shot is viewport tiles of that scroller, stitched. `/developer/en/` and `/user/login/` stayed 900px tall after the same scroll. The login full shot is 1545px wide because full-page capture included horizontal overflow. The viewport shot is 1440.

## Fonts

Figtree, weights 400, 500, 600 and 700, from `@font-face` rules on the home page. The guide falls back to Arial and Helvetica. Poppins is declared in `--font-family-sans-serif` and is not the painted body. Licence of Figtree was not read from the font file. Not captured.

## Coverage

| Checklist item | Status | Where |
|---|---|---|
| Page, surface, text, muted, accent, border | captured | `light.background.*`, `light.text.*`, `light.border.*` |
| Status colours | partly | Declared `--success`, `--warning`, `--danger`, `--info`. Not seen on a painted control. |
| Dark theme | not present | `color-scheme: normal`, no theme switch |
| Type | captured | Figtree display 60/66, heading 40/46, body 16/24, label 14/20 |
| Spacing, radii, control heights | captured | `core.space`, `core.radius`, `core.size` |
| Motion | not captured | Durations were not read |
| Elevation | not captured | Header and Get started computed `box-shadow: none`. No elevation scale read. |
| Button | captured | default and hover screenshot. Fill measured at default. |
| Link | captured | Pricing and Log in |
| Text field | captured | contact field default, login field default and focus |
| Menu | captured | four header menus, phone menu |
| Card | observed | community and plugin cards. Values not read per card. |
| Icon button, text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar, badge | not captured | Not reached on the public pages, or only inside the editor |
| Pressed, disabled, loading, error | not captured | No form submitted. No control held in those states. |
| App shell | captured | desktop header and phone menu |
| Form | captured | contact page, empty. Not submitted. |
| Login wall | captured | `/user/login/`. Password not submitted. |
| Search | observed | help search field. Not typed into. |
| Signed-in editor, files, teams | not captured | `/app/` behind login. `/signin` is 404. |

## Do and don't

- **Paint the page white and the text black.** Body background is `#ffffff` and body colour is `#000000`. [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Use the near-black button for the primary action.** Get started is `#202125` with white text, radius 7px, height 34px. [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Keep the blue brand for links and focus.** `#336fff` is the declared brand. Login focus is `rgb(31, 97, 255)` at 2px. [screenshots/login-light-default.png](screenshots/login-light-default.png).
- **Set labels in Figtree.** Header links are Figtree 14/500. [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Stop at the login wall.** Log in and Get started open `/user/login/`. Do not treat that page as the editor. [screenshots/login-light-default.png](screenshots/login-light-default.png).

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/pixso/tools/capture/public/public.mjs
python3 systems/pixso/tools/capture/quantize.py
python3 systems/pixso/tools/build_tokens.py
python3 systems/pixso/tools/build_style_guide.py
```

`make design-md` needs a catalog.json entry. This capture does not add one. DESIGN.md was generated with a temporary entry that was not written to catalog.json.

## Surfaces

The site tree is [site-tree.md](site-tree.md). English only. Other locales (`/jp/`, `/kr/`, `/ru/`, `/es/`, pixso.cn) were not walked. Article posts, tip posts, and help articles beyond the indexes and one design guide were not each captured. They share the index templates.
