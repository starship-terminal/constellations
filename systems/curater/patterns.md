# Curater patterns — page layouts

Captured signed out on 2026-11-12. Heights are the painted `scrollHeight` of each route at 1440 wide; mobile is 390 wide at DPR 2. One painted theme: every page is light (#fff page/cards over the #f2f2f2 app field).

## Shell

- **Nav rail (48x328, left edge).** Six round 48x48 icon buttons stacked vertically — the active page's button keeps the #f2f2f2 fill (`--Curater-background`); the rest paint transparent and fill #f4f4f5 + ink on hover/pressed. A 48px settings button sits at the rail's foot.
- **Header.** On content pages a top bar carries the 20px search toggle (reveals a 170x30 'Search curations...' field while the pointer stays over it), the 'Log in or sign up' 14px label (#7c7c7c, darkens to ink on hover) and the ~130x42 TasteScope pill.
- **Mobile (390 wide).** The rail collapses into a 160x40 bottom bar of 40px round buttons (`_mobileNavButton_`/`_mobileMenuButton_` classes); a menu button opens the mobile menu.

## Home (`/`; H=3760)

- **CTA.** The 'Sign in / Create account' pill: 259x58, white fill, 9999px radius, 1px hairline, `shadow-sm`; hover/press fills it #f2f2f2 and sinks it 2px (translateY).
- **Trend section.** A 544px header over the 544x492 trend card — 24px radius, 1px hairline, a soft rgba(0,0,0,0.02) 0 14px 54px lift — with 100x100 thumbs, the headline, a description, the 'Curated by' label (#afafaf, `--Curater-gray-light`) and the avatar.

## Feed (`/feed`; inner-scroll H≈27850 desktop, 57550 mobile — bounded)

- **Toolbar.** 'Featured / For You / More' tabs at ~64x40 (16px 500), the search toggle and the login label.
- **Themes.** 'Browse by themes' at 16px/500 over 224x271 theme tiles ('Visual Identity / 16 curations').
- **Curations.** A grid of curator labels (12px), 24px/500 title links (~415x212 wrap), the 28px white Save chip (9999px, hairline, `shadow-sm`), media items at 1080x540 and 540x540 album links. Content lives in an inner `.feedScrollArea` scroller — the document never grows; the capture expands the scroller and its ancestors and stops at the recorded bound.

## TasteScope (`/taste` → client-redirects to `/taste/soon`)

- **Teaser.** White 20px/500 copy in a 256x788 column over the 1360x900 BrandGlobe WebGL canvas (a 48x48 avatar canvas also renders). Locators never resolve on this route (the navigation never settles); components are measured through main-world DOM queries.

## Curation (`/curation/qDNMdxe5`; H≈2269)

- **Detail pane.** A 36px back button and 32px options button, the ~350x240 heading column, the 350x58 Google SSO button, 'SEARCH SIMILAR ON' with Pinterest/Cosmos chips, then PINS and TAGS sections. Nested `.lenis` scroll containers inside.

## Profile (`/ravi`; H≈5914)

- **Identity.** 93x24 name (16px/500), 28x28 avatar, the ~130x42 TasteScope header button, a ~379x157 bio column.
- **Items.** 268x380 profile tiles with ~268x60 titles and a 28x28 round menu button (white glyph on rgba(0,0,0,0.2)).

## Terms (`/terms`; H≈4092)

- A centred ~560px column: 55px heading, 21px body lines.
