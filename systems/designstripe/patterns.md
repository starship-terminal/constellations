# Visual (designstripe) patterns

How the measured components combine into the public pages. Every value resolves in [tokens.json](tokens.json); the components are in [components.md](components.md), the crops in [components/crops/](components/crops), the full pages in [screenshots/](screenshots).

## The fixed chrome

Every surface carries a fixed 1440x32 top bar over the white field (`light.background.page`, `#ffffff`): the ink `Visual` logo mark (`core.font.size.micro` 12px mono at 500 on a `#2c2c26` ink square, `core.radius.logo` 4px), mono section links (`light.text.ink`, `core.radius.nav-link` 3px) — Why Visual?, Assets, Tools, Blog — and the cream `WAITLIST` pill (`light.action.cream` `#e8e7d9` → `light.action.cream-hover` `#2c2c26` on hover, `light.action.on-cream` ink text, `core.radius.pill`). The same bar on a 390px viewport collapses to a 40px bar with the wordmark and a menu button. The menu lists HOME, WHY VISUAL?, ASSETS, TOOLS, BLOG, and JOIN WAITLIST. See [mobile-nav-light-open.png](screenshots/mobile-nav-light-open.png).

## The serif hero

The home hero centers a 708px `fontSerif` display at 96px (`core.font.family.display`, the `sec-h2`/`ast-h1`/`tool-h1`/`ct-h1` steps share the family) over 14px mono subcopy at 500 (`core.font.family.ui`, `light.text.muted` `#6d6e5e`). The same recipe scales the page displays: 96px on /assets, /tools, /contact and /about, 64px on the blog article, 48px on section H2s and the phone hero.

## The feature accordion

The dark home section is the one non-white block before the footer: a `#2c2c26` panel holding monospace accordion rows at 20px/500 (`light.text.on-dark` white text on the ink fill). A row opens in place — `feature-acc` was measured at rest, `feature-acc2` opened — no navigation, no external action.

## Asset tiles and kind links

/assets paints `ast-h1` (684x96 serif) over a grid of `aspect-square` tiles: a 569px featured tile beside 280px standards, 8px radius (`core.radius.tile`) on white with the `#d0d0c8` hairline (`light.border.control.default`), preview art inside and a mono category label. `/assets/avatars/replicants` is the same chrome with 222px avatar items (`av-item`) and a mono `/ AVATARS` kind crumb (`tool-crumb` shares the pattern). Tiles link to detail pages — measured, never followed.

## Tool cards

/tools grids 338x422 bordered cards (`tool-card`, `core.radius.card` 6px, `light.background.card` white, `light.border.control.default`) under the serif display: a mono `TOOLS / kind` crumb, a serif title, mono copy and a live preview of the tool. The breadcrumb pattern (`tool-crumb`, 12px mono) threads the library and tools surfaces.

## The editorial article

/blog articles run a 914px serif title at 64px (`post-h1`), mono body paragraphs at 14px (`post-para`, `light.text.ink-body` `#454540`) and serif inline links at 20px in the olive-gold (`light.text.link` `{color.green.700}` family — `#aaa674`/`#6e6c3f` tones) with the `rich-text` rules from the stylesheet.

## The ink footer

Every page closes on the one painted dark block: a 1440x320 `#2c2c26` footer (`light.background.ink`, matching `--card-foreground`/`--foreground`) with cream and white mono sitemap links (`light.text.on-dark` `{white}`) — 390x316 on the phone.

## Mobile

At 390 wide the nav compresses to a 40px bar (`m-nav`), the hero serif drops to 48px (`m-h1`), accordion rows hold 16px mono (`m-acc`) and the footer keeps its ink fill at 390x316 (`m-footer`).

## The waitlist dialog

WAITLIST and JOIN WAITLIST open one dialog on the current URL. It is a 720x450 white panel (`wl-dialog`) with a two-layer shadow (`light.elevation.dialog`). The fields are 40px mono inputs for First name, Work email, and Company name, plus a Company size select. The submit button is ink with white mono text (`wl-submit`). The dialog was photographed empty. Nothing was typed and Join waitlist was not pressed. See [waitlist-light-dialog.png](screenshots/waitlist-light-dialog.png).

## The public color tool

/colors/color-wheel is a public tool, not a card. It keeps the site chrome, a 96px serif heading (`wheel-h1`), a colour wheel, a hex field, an Analogous select, and an ink Export button (`wheel-export`, `#414238` on hover). Export was not pressed. See [tool-light-default.png](screenshots/tool-light-default.png).

## Boundaries

- The design agents and every screen after the waitlist need an account and were not entered.
- The waitlist dialog was opened and not submitted. Company size was not opened.
- /privacy is a footer link that paints "Privacy page not found".
- `/contact` paints copy, not a form — no field, validation or error state exists on the public surface.
- A real `.dark` block is declared in the stylesheet but no public control toggles it; the `dark` token set is evidence of intent, not of a painted surface.
- Asset tiles and article links were never followed (external/account flows).
