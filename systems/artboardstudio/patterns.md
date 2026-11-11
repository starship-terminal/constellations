# Artboard Studio patterns

How the measured components compose into artboard.studio's public pages.
Values are in [components.md](components.md) and [tokens.json](tokens.json);
the screenshots named below are in [screenshots/](screenshots).

## The shell

A 106px transparent nav bar: the Artboard Studio wordmark left, Mockup
Library / Figma plugin / Signup links right ([home-light-default](screenshots/home-light-default.png),
`header`, `nav-link`, `nav-signup`). Link hover is a text fade to `#aaa`,
not a fill change. At 390 the links collapse behind a 48px `w-nav-button`
hamburger opening a Webflow nav panel
([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)).

## The hero + category tab bar

The landing is a centred Vend Sans 60.8px h1, then a 50px pill tab bar —
Most Popular (selected) / Device / Apparel / Packaging / Print / Branding —
each `.w-tab-link` a near-black `#0d1400` 8px-radius pill with white text
([home-light-tab](screenshots/home-light-tab.png), `tab`, `tab-selected`,
`tab-switched`). Category grids of ~199px `.w-dyn-item` tiles follow under
19.2px Vend Sans section headings.

## The library pane

/mockup mounts the real library inside the page: a 56px Vend Sans title, a
~65px full-width search field (white, ink hairline, 8px radius), 50px
filter chips, then a grid of thumbnail cards — all inside an inner
`.container-category-pages` scroller rather than the document scroll
([mockup-light-default](screenshots/mockup-light-default.png),
[mockup-light-scrolled](screenshots/mockup-light-scrolled.png),
`lib-title`, `search-field`, `filter-chip`, `lib-card`).

## CTAs

Primary actions are 42px near-black `#0d1400` buttons with 8px radii and
white text; hover lifts the fill to `#222` (`plugin-cta`, `contact-cta`,
`figma-cta`). The New version / Legacy version picker cards live in a
collapsed nav dropdown.

## Footer

A wide white link-column footer on `#ffffff` with the same 42px ink link
rows and social icons ([home-light-full](screenshots/home-light-full.png),
`footer`, `footer-link`, `footer-social`).
