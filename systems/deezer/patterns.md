# Deezer patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (light)

The 80px top bar (`core.component.topbar-height`) carries the 107px wordmark, the Plans/Features/Download links, a ghost Log in and the purple Sign-up pill. On the home page it floats over the light hero: a white field (`light.background.page`), `#0f0d13` ink (`light.text.ink`) and the 140px/800 Deezer Brand display (`core.font.family.brand`, `core.font.size.display`), followed by a five-star ratings line and a purple 16px-pill Try-for-free (`light.action.accent`, `radius.control`). Section headings drop to 56px (`core.font.size.section`).

The same surface on the offers/features/download pages paints **dark**: the marketing site and the app share the Tempo `[data-theme="dark"]` resolution.

## Offers (dark marketing)

/en/offers centers a 78px Deezer Product headline (`core.font.size.h1`, `core.font.family.product`) over a Monthly/Annual pill toggle — a `#29282d` 256px track (`dark.background.toggle`, `radius.full`) — then `#fdfcfe` plan cards on 4px radius (`light.background.card`→`color.bg.main`, `radius.card`) with a purple PREMIUM chip (`light.action.chip-accent`) and a dark `#121216` Try-for-free action (`light.action.dark-button`→`color.bg.inverse`).

## The dark catalog shell (signed out)

The public /en/artist, /en/album and /en/playlist pages paint the whole signed-out app:

```
+--------+--------------------------------------------------+
| 243px  | search field 48px · Plans · Log in · Sign up     |
| side-  +--------------------------------------------------+
| bar    | artist/album/playlist content (tabs, track rows, |
| #141216| playlist cards, 56px rows)                        |
|        +--------------------------------------------------+
|        | lavender signup banner #ead1ff, 80px             |
|        | player bar, 80px, top divider #38373b            |
+--------+--------------------------------------------------+
```

- Sidebar (`core.component.sidebar-width`, `dark.background.surface`): wordmark, Home/Explore nav pills, a `#242326` 8px-radius playlist promo card (`dark.background.raised`, `radius.promo`), Create-playlist row.
- Header: a 48px `#242326` search field (`core.component.search-height`, `radius.control`) that gains a 2px `#ad47ff` border and `#2e2c30` lift on focus (`dark.border.focus`, `dark.background.field-focus`); Plans link, ghost Log in, purple Sign-up pill (`dark.action.accent`, `radius.pill-s`).
- Content: 56px track rows (`core.component.track-row-height`) with a round purple play (`radius.full` 256px), an overflow trigger opening a 24px-radius 308px `#141216` popover (`core.component.popover-width`, `radius.popover`, `dark.background.surface`) over a layered black shadow (`core.shadow.popover`); tabs underline in accent; artist/album headings are 56px Deezer Headline VF at wght 640 (`core.font.family.headline`, `font.weight.demi`).
- Signup banner (`core.component.banner-height`, `dark.background.banner` `#ead1ff`): "Live the music with Deezer" with a purple 16px-pill CTA.
- Player bar (`core.component.player-bar-height`): track title/artists, heart, context actions, transport controls, queue and volume — all measured, none pressed.

## Auth forms (account.deezer.com)

Dark pages matching the app theme: wordmark, e-mail and password fields with the same `#242326` fill, 16px radius and 2px accent focus border, a purple submit pill, forgotten-password link and social sign-in buttons. Measured as forms — never filled or submitted.

## Mobile (390px)

The phone surface is the same dark app: a 60px top bar (`core.component.mobile-topbar-height`) with wordmark and burger, a full-viewport `#0f0d13` nav overlay (`m-drawer`, `dark.background.canvas`), the artist hero at 40px (`core.font.size.mobile-display`), a purple signup card and the track list. No separate mobile tokens — the same dark set resolves.

## Motion and focus

Controls transition `background-color` and `border-color` over 0.2s (`core.motion.control`, matching declared `duration.normal` 200ms / `--tempo-transition-duration-normal`). Focus is a border treatment, not an outline: fields draw a 2px `#ad47ff` border (`dark.border.focus`); buttons swap their border to the accent (dark) or `#555257` (light header, `light.border.focus`).
