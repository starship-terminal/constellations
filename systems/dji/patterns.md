# DJI patterns

How the measured components combine into screens. All values live in
[tokens.json](tokens.json); component entries are in
[components.md](components.md).

## Two header generations

The site runs two nav implementations side by side. The home page paints the
legacy `nav.dui-navbar` — a 64px transparent-over-hero bar with the DJI mark,
`.navbar-category` menu items (Camera Drones, Handheld, Lifestyle Tech,
Specialized, Explore, Support, Where to Buy), search/account glyphs, the
Singapore locale picker and the 84x32 `#0070d5` **Store** pill (radius
1408px — fully rounded). Category, product and support pages paint the newer
`.official-site-header` module (also 64px) with the same menu model. Mobile
redirects to a separate `/sg/mobile` site whose `.dui-navbar-m.site-header-m`
is a 50px row of 54px category tabs.

## The hero (dark-theme section)

The home hero is a `.dark-theme` section: 800px-tall product panels over a
photographic backdrop, white ink, and the ghost-CTA pair — Learn More and Buy
Now, 32px tall with a 64px pill radius and a 1px white border that fills
white@9% on hover and white@15% on press. A product switcher sits bottom-left;
an app-download banner rides above the nav.

## Category grids (light-theme sections)

`/camera-drones` and `/handheld` are `.light-theme` listings: a 48px
display heading (`rgba(0,0,0,0.85)` ink), then rows of
`atom-design-v1` **hero-vertical-cards** — product art, a tagline, the model
name and a Learn More link, on the white field. A pinned sub-nav carries the
`Store`/`Buy Now` pill (`#0070d5` → `#2490e3` hover → `#0058b0` pressed,
0.3s background-color transition).

## The product page

`/mavic-4-pro` opens on a `.dark-theme` hero behind a 64px sticky sub-nav
(section links + a `sub-nav-btn` Buy Now). Sections alternate: dark panels
carry `text-ms-24` eyebrow lines (white@85%), spec rows and the atom-design
CTA pair — the white **pill** (`#fff` → `@90%` → `@80%`, black@85% label,
60px radius) and the **ghost** (transparent + 1px white border → `@9%` →
`@15%`). Light sections between them carry prose in black@65%.

## Support, company, where to buy

`/support` is a light-theme portal: a 640x32 rounded search field on white,
category tiles, the standard footer. `/company` is a minimal about page;
`/where-to-buy/online-stores` lists store-type links (`a.ga-data`) under a
32px heading.

## The footer

A `#272727` slab on every page — 833px of sitemap columns with white@85%
links (`--white-8`), closing the dark section stack.

## Boundaries

Store, Login/Register and checkout gate on the DJI account (member-service
redirects); Buy/Store controls were measured, never followed. Mega-menu
hover panels exist but their items were not walked. The subscribe modal's
buttons were measured only if the dialog painted itself.
