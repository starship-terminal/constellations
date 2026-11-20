# Docusign patterns

How the measured components combine on each captured surface. Values are references into [tokens.json](tokens.json) and the per-state readings in [components.md](components.md); the pixels are in [screenshots/](screenshots).

## The chrome

Every marketing page stacks two bars:

- **Utility strip** (30px, `surface.band` deep violet `#26065d`): a promotional link on the left, then Search, Support, Access Documents and Log In on the right — all `font.size.label` 12/18 at weight 500 with `+0.2px` tracking in white.
- **Header** (69px, white, sticky): the Docusign wordmark, then `Products`/`Solutions`/`Resources` mega-menu triggers and `Enterprise`, `Plans & Pricing` links — 14/21 weight 500 in `text.secondary` (75% ink) with `radius.4` hover boxes. Right side: uppercase text actions `CONTACT SALES` and `BUY NOW` in cobalt at weight 600, then the filled `TRY FOR FREE` pill — `action.primary-bg` cobalt, white text, `radius.8`, `12px 16px` padding, 45px tall.
- **Mega-menu**: clicking Products opens a 1360 x 379 white sheet of product links — `menu-link` rows are 410px, 16/24 weight 500 ink labels over grey descriptions, `radius.4`, `64px` column gaps.
- Keyboard focus on every chrome control: `focus.ring` — 2px solid cobalt at 2px offset.

## The home hero

A `surface.band` deep-violet field (`96px 80px` padding) carries the pattern the whole brand is built on: `component.type.display` — 80/86.4 weight-300 white text at `-1.5px` tracking — over an 18/27 lede. The capture row pairs a 61px floating-label `workEmail` field (white, `border.default` ink-15 hairline, `radius.8` left corners) with an `action.ink-bg` inkwell Get-Started button (right corners only). Under it: a white opt-in checkbox row, the cobalt `Explore Docusign IAM` link and the `Country/region` select (native, opacity-0 inside its label). Focused fields trade the hairline for a cobalt border plus the `shadow.field-focus` 1px cobalt inset; focus on the band draws the `focus.ring-on-band` 2px mist ring.

## Content sections

- **Section headings** set `font.size.h2` 58/62.64 weight 300 at `-1.25px` in inkwell.
- **Card links** (blog/resource teasers) are 14-16px weight-500 cobalt or ink rows; focus rings cobalt.
- **The Docusign Assistant** is a floating sierra.chat embed: a 9999px pill, `#4014ea` fill, white 16px weight-700 text, `shadow.launcher`; on hover it inverts to white with violet text. Its own focus ring is vendor green `#089b57`.
- **OneTrust** consent is present on every page — hidden for capture, never answered.

## eSignature product page

`/products/electronic-signature` runs the same chrome plus: a 48/51.84 weight-300 h1, plan/trial CTAs, a customer-story **video dialog** — a 90% ink scrim (`overlay.scrim`) with a framed player opened by the tile's Expand button — and a **FAQ accordion**: 1280px rows, 24/29.76 weight-500 questions at `-0.25px`, `32px` vertical padding, `48px` icon gap; a row's own toggle opens the 16px panel.

## The free-trial band

`/free-trial` centres a form band: a 40/48 weight-400 heading, then 488px-wide floating-label fields (same 61px recipe as the hero), a consent checkbox row and the `GET STARTED` submit — cobalt fill, `radius.4`, `4px 12px` padding, uppercase 16px. The floating Help launcher sits bottom-right.

## Signature generator

`/signature-generator` is the only surface declaring a token layer (the `--ds-*` set + shadcn roles): an ecru `#f8f3f0` ground, a 64-72px weight-300 display title, then **Draw/Type tabs** (6px pills, mist borders, `shadow.soft`, cobalt text when active). Draw mode paints the signature canvas with **colour swatches** — 32px squares at `radius.8` that scale ×1.1 on hover and ×0.95 pressed: Black `#000`, Cobalt `#4c00ff`, Coral `#ff5252`. Type mode swaps in an 888px name field (`radius.8`, mist border → cobalt border + `rgba(76,0,255,.1)` 3px ring when focused) and six **script-face options** (438px white cards, 1px cobalt border when selected). `Download as PNG/JPEG` are `surface.mist` fills with 50%-violet text at `radius.8` — measured, never pressed.

## Customer stories

`/customer-stories`: a 56px title, `Products used`/`Industry`/`Department` filter dropdowns (53px, `radius.4`, ink-75 labels), then 328 x 446 story cards — image, `card-title` 24/29.76 weight-500 headline — and 328px logo tiles.

## The pricing storefront

`ecom.docusign.com` (served `/en-SG/` on this vantage) is a second app: Tailwind + Emotion, `DS Indigo` stack, `--dxp-primary #0069ec` declared on body. The page stacks an Annual/Monthly toggle (28px, `surface.wash` ink-05 track, `radius.4`) over white **plan cards** — 301px, `radius.16`, `border.strong` 50%-ink border — with 30/37.2 plan names and 16px `Buy now` (`action.primary-*`) / `Contact sales` (`action.ink-*`) buttons. Focus-visible draws `shadow.ring-double`: 2px white + 4px cobalt, plus a 2px offset outline. Feature rows are expandable accordion lines; `See All Features` is a cobalt outline button that fills `surface.violet` #ede5ff on hover.

## The sign-in card

`account.docusign.com` (where `apps.docusign.com/send` lands signed out): a 556px white card at `radius.4` with an `rgba(25,24,35,.15)` border and `64px` vertical padding — the wordmark, a 424px email field, the `Next` submit in `auth-deep` #260559 (`hover` #2b047f, `pressed` #37039e), a `Sign Up for Free` link and the `English (US)` language trigger. Focus rings are inkwell, not cobalt. Never filled past sample text, never submitted.

## Footer

A 974px white footer: link columns at `meta` 14/21, `eyebrow` 12px weight-600 headings at `+0.8px` tracking, the `United States` locale button (200px, `radius.4`, mist border → changes only border on focus) and legal/social rows.

## Mobile (390 wide)

The header keeps the violet strip and grows to 77px; a 24 x 30 hamburger opens the menu (Products/Solutions accordion). The hero restacks: the headline stays weight-300 display, the field + CTA pair full-width. The ecom storefront stacks its plan cards single-column.
