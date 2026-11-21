# Pexels components

Public site only, www.pexels.com, 2026-11-21. Values are token names from [tokens.json](tokens.json). Crops were not cut in this pass, so each row is Observed from the full-page screenshots.

## Inventory

| Component | States seen | Where |
|---|---|---|
| Button (Join) | default, hover | [home-light-default.png](screenshots/home-light-default.png). Hover fill measured as `light.action.primaryHover` (#393939). Pressed not held. |
| Icon button (more) | default, menu open | [home-light-more-menu.png](screenshots/home-light-more-menu.png) |
| Link (nav) | default, hover disclosure | Explore hover in [home-light-explore-hover.png](screenshots/home-light-explore-hover.png). License link measured. |
| Text field (search) | default, focus, filled with suggestions | [home-light-search-suggest.png](screenshots/home-light-search-suggest.png). Focus painted no ring (`light.focus.ring` outline style none). |
| Text area | not present | No public multi-line field that is not an account form. |
| Select | not present as a native select | Photos/Videos is a menu, not a select. |
| Checkbox | observed on the login wall only | Orientation filters use checkbox-like chips on [search-light-filter.png](screenshots/search-light-filter.png). The login wall has a Cloudflare checkbox. Not interacted with. |
| Radio | observed as filter chips | People count and age chips on the filter rail. Not a native radio. |
| Switch | not present | |
| Tabs | selected | Home / Videos / Leaderboard pills. Photos / Videos / Users on search. Most Viewed / Most Active on the leaderboard. |
| Menu | open | More menu, Explore menu, Photos/Videos menu, Trending/New menu. |
| Tooltip | not captured | None held open. |
| Dialog | open | Join intent dialog [home-light-join-dialog.png](screenshots/home-light-join-dialog.png). Around the world [home-light-around-world.png](screenshots/home-light-around-world.png). Login wall is a modal on desktop. |
| Toast | not present | |
| Card | default | Challenge card, photo tiles, collection cards in search suggestions. |
| List row | default | Leaderboard rows in [leaderboard-light-default.png](screenshots/leaderboard-light-default.png). More-menu rows. |
| Table | not present | |
| Avatar | default | Leaderboard and search chips. Published creator photos. |
| Badge | default | FREE pill beside Photography Series. |

## Shared values

- Control height is `core.size.control` (48px).
- Primary button radius is `core.radius.control` (12px). Selected nav pills use `core.radius.pill` (30px). Search chips use `core.radius.chip` (180px).
- Ink is `light.action.primary` (#191919), not pure black, except the selected Home pill which is `light.action.selected` (#000000).
- Green download uses `light.action.download`, aliased to the declared `--color-alien-dark` (#32ac64). The computed green on the Free download button was not read.

## Gaps

- Pressed, disabled, loading and error states were not captured. Nothing was submitted, so no validation error exists.
- Download size menu did not open. The chevron click on the photo page opened the search type menu instead. Recorded as not captured.
- Cookie banner never painted in these headless sessions, so its layout is not in a screenshot. The mapper saw its text on the first homepage load.
- Dark theme controls were not captured. `[data-mode=dark]` exists in CSS and was not applied.
- Icon SVG files were not extracted (`icons/` absent).
