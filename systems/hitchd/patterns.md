# Hitchd patterns

How the measured components compose on each public surface. Every value named here is a token in [tokens.json](tokens.json) or a reading in [raw/measurements.md](raw/measurements.md); the screenshots it points at are in [screenshots/](screenshots).

## Closure chrome (marketing site)

Pattern stack: `.top-banner` announcement strip → `.closure-header` bar → full-bleed hero → one-viewport page.

- **Announcement strip.** A full-width cream band (`surface.cream`) carrying one line of Inter UI copy in `text.ink` — currently "Hitchd is closing on 31 December 2026". Static, no dismiss control. [announcement](components/crops/announcement.png)
- **Header.** A 96px bar over the hero's imagery: wordmark left (linked SVG `/marketing/images/hitchd-home-brand-logo.svg`), `Log In` link right in `nav.ink`. See [nav](components/crops/nav.png) and [home-light-default](screenshots/home-light-default.png).
- **Hero.** `display.hero` — DDNR, weight 100 — in `text.inverse` over a photo/video field, with a `lead`-size supporting paragraph. The home page is now a single viewport: strip + header + hero and nothing else.

## Content pages (blog, terms, privacy, trips, guides)

- **Prose column.** `h1` title → `article`-size body in `text.ink` with `text.link` inline links; h2/h3 section breaks; the marketing footer (`surface.footer`) with its `footer link` row. [post-light-full](screenshots/post-light-full.png), [terms-light-full](screenshots/terms-light-full.png)
- **Blog index.** Rows of `blog-card` entries; the index is ~50,000px tall — captured to the viewport; the truncation is the documented boundary.

## Auth surfaces (couple app)

Pattern: centred `auth card` on `surface.page` → `h1` (`size.authH1`) → labelled `field`s → disabled `Continue` pill → OAuth divider → link row.

- **Card.** The form is the layout: a centred column, no visible chrome beyond the hitchd mark top-left. [auth-card](components/crops/auth-card.png)
- **Field.** 450 x 48 at 1440, `radius.field` 8px, `border.field` 1px `#d2d2d7`, label above in `text.ink`.
- **Submit.** `action.disabledFill` (`palette.disabled`) at rest until valid — a 50px pill at 48px high, label in `action.disabledInk`, weight `font.weight.button`. [auth-button](components/crops/auth-button.png)
- Never focused, typed or submitted — `/login`, `/signup`, `/forgot-password` were read at rest only.

## Guest registry

Pattern stack: `registry sample banner` → couple hero → `sort-filter` → gift grid → `gift-modal` on card tap.

- **Sample banner.** `.top-registry-sample-banner` — `nav.bar` fill with the line "Fund your dream honeymoon guilt-free." and the black `action.ctaFill` "Try It Free" pill (white `action.ctaInk` label, 100px corners). [registry-nav](components/crops/registry-nav.png)
- **Couple hero.** `h1.classic` — the display face at `size.display.registry` — plus `.couple-intro` (date, welcome paragraph, `text.hashtag` `#zoeandnoah`) over the cover photo. [registry-hero](components/crops/registry-hero.png)
- **Sort filter.** A `.toggle-dd.gift-filter` styled `<select>` — Everything / Still needed / Funded / Couple's choice. Picking re-filters the grid locally; two stacked variants render, one per width. [registry-light-sort-open](screenshots/registry-light-sort-open.png), [registry-light-filter-still-needed](screenshots/registry-light-filter-still-needed.png)
- **Gift grid.** `ol.gift-list`'s `.giftz` tiles (`radius.card`): gift photo, `h3` title, location and description; the `.bottompricing` goal containers render empty on the demo registry, so no price role is claimed. [gift-card](components/crops/gift-card.png)
- **Gift modal.** A card's own tap routes to `/zoeandnoah/<gift-slug>` and the app draws the modal over the list: `surface.modal`, title, funded-vs-goal progress, amount field, and the `Give` pill disabled until an amount exists. Read at rest — Give and everything behind it is the boundary. [gift-modal](components/crops/gift-modal.png), [registry-light-gift-modal](screenshots/registry-light-gift-modal.png)
- **Phone drawer.** `.mobile-menu` exists in the DOM hidden on the demo — it carries the owner links (contributions, payment methods, log out) but no guest-facing control opens it, so it is a boundary, not a guest pattern. Documented, not faked.

## Boundaries

| Route / state | What a signed-out guest gets | Evidence |
|---|---|---|
| `/zoeandnoah/contributions`, `/payment-methods`, `/ask`, `/quick-thanks` | Bounced back to `/` | `internal-route-bounces` in [raw/components-computed.json](raw/components-computed.json) |
| `/how-it-works`, `/about`, `/pricing`, `/press-kit`, `/*-alternative`, `/referrals`, `/honeymoon-registry` | Redirect to `/` (the site is closing) | route probe; [components.md](components.md) Gaps |
| `/blog` full page | ~50,000px of rows — tile capture bounded | shooter log; [components.md](components.md) Gaps |
| Give / contribute / payment steps | Never entered by policy | [registry-light-gift-modal](screenshots/registry-light-gift-modal.png) at rest |
| Anything behind Log In | Auth wall — never signed in | [login-light-default](screenshots/login-light-default.png) |
