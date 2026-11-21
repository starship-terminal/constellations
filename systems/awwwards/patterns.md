# Awwwards patterns

How the measured components combine on each public surface of awwwards.com (signed out, 1440 x 900 and 390 x 844, en). Values are in [tokens.json](tokens.json); the per-state measurements in [raw/measurements.md](raw/measurements.md).

## Chrome: the header

The header is a 54px bar (`header`, same on mobile) — transparent on desktop, a #f8f8f8 `--bg-primary` fill on mobile. Left: the wordmark (`logo`, 30x16 SVG). Middle: the nav row — Explore (a dropdown, not a link), Directory, Academy, Jobs, Market (`nav-item`, 14px Inter Tight 500). Right: a search field ("Search by Inspiration"), Log in, Sign Up, Be Pro (`bepro-link`, an ink #222 pill, 8px radius, white label — it lifts to #383838 on hover), and the outlined Submit Website (`submit-cta`, transparent at rest — it fills #383838 and inverts the label on hover). Log in and Sign Up are visible on the 2026-11-21 shots and were not clicked. Focus is the browser's `#005fcc` ring. The Explore dropdown is [home-light-explore-open](screenshots/home-light-explore-open.png).

At 390px the bar keeps wordmark + `m-menu-button` (54x54). Its own toggle opens the mobile menu (`m-menu-open`); rows inside it are `m-nav-link` (390x54 full-width rows). The open menu is [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Winners grid

`/websites/` opens with the title (`grid-title`, 14px Inter Tight 600) and the filter bar — 42px `.nav-filters__item` tabs (Awards, Category, Tag, Technology) on the #f8f8f8 `--bg-primary` strip (`filter-item`). A tab's own toggle opens `filter-dropdown` (280x346, #f8f8f8 panel): rows are `filter-option` (264x40) that pick up the #ededed `--bg-3rd` fill on hover — [websites-light-filter-open](screenshots/websites-light-filter-open.png).

Cards (`grid-card`, 432x324 at 1440 — three across inside the 1816px `--innerWidth`) are 4px-radius image+caption rows (the home-page `site-card` is the 14px one): the site screenshot inside `grid-card-link` over a 15px Inter Tight 300 caption row. Hovering a card reveals the rollover layer (`figure-rollover__hover`) with the centred Vote Now button. It stayed `display:none` for headless measurement (recorded gap on `card-cta`). The 2026-11-21 hover shot timed out, so that state is Not captured.

## Site detail

A `/sites/` entry (whichever card first had open voting — `site_url`) stacks `site-title` (a ~127px Inter Tight 600 display heading), `score-box` (69x84 bordered score panel, 8px radius — Design/Usability/Creativity/Content averages under `score-note`), the 60px gold `vote-button` (191x60, the measured #e3c352 award gold no var declares, ink label, 8px radius), the 20x20 `visit-link` toolbar icon to the external site, and `tag-chip` category pills (179x48, 72px fully-round, 18px Inter Tight 600). The vote was never cast.

## Collections and submit

`/collections/` is the same grid language over curated lists — `coll-title` (13.3px 600) and `coll-card` (140x42 tabs on #f8f8f8). `/submit/` is the public submission gate: `submit-title` (a ~42px heading-5) over `plan-card` (1336x551 plan/pricing panel). No CTA measurable to headless (`submit-cta-2` is a recorded miss); nothing was submitted.

## Buttons and controls

One visual language: Inter Tight 500–600 labels on 8px-radius controls — the ink #222 pill (Be Pro), the outlined pill that inverts on hover (Submit Website), the gold Vote CTA, and the 72px fully-round tag chips. Hover answers with fill swaps (#383838 on the buttons, #ededed inside the dropdown), never scale or shadow. Focus is the browser `#005fcc` auto outline on links.

## Mobile

The same surfaces recompose at 390x844: `m-header` gains its #f8f8f8 fill, the nav moves into the menu layer (`m-menu-open`, `m-nav-link` rows), and cards go full-width (`m-site-card`, 358x268). The winners grid stacks cards one across.

## Overlays

The arrival view is captured before anything is hidden — [home-light-arrival](screenshots/home-light-arrival.png). No consent wall blocked the captured routes; any consent or promo layer that mounts is hidden, never answered: no Accept/Reject is ever clicked anywhere in the capture.
