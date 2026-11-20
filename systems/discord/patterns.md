# Discord patterns

How the measured components combine into the public pages. Every value resolves in [tokens.json](tokens.json); the components are in [components.md](components.md), the crops in [components/crops/](components/crops), the full pages in [screenshots/](screenshots).

## The marketing shell

Every page opens with a fixed 80px `header.nav` (`mk-nav`, `core.component.marketing-nav`) over the blurple gradient: the Clyde wordmark, Ggsans section links (Download, Nitro, Discover, Safety, Quests, Support, Blog, Developers, Careers) and the white `Log In` pill (`mk-nav-login`, 80x39, `core.radius.nav-pill` 16px, `light.action.nav-pill`). Nav links are 16px/24px in the marketing display face; the dropdowns (Discover etc.) are Webflow `w-dropdown` toggles measured, never opened through.

## The hero

The home hero stacks a 56px/48px ABC-Ginto-Nord display headline (`mk-h1`, `core.font.size.measured.display-marketing`, white on the animated blurple field) over a 20px lede (`mk-lede`, `core.font.size.measured.lede`), then the CTA pair: the white `Download for Linux` pill (`mk-cta-download`, 262x65, 12px radius) and the `#5865f2` `Open Discord in your browser` button (`mk-cta-open`, 324x65, `light.action.primary`). The same chrome frames /download (light page, `light.background.page` white) and /nitro, which drops `#1a1a1e` 96px-radius plan cards (`nt-card`, `light.background.card`, `core.shadow.nitro-card` 0 2px 32px rgba(69,42,124,0.1)) onto the white field.

## Server discovery

The app's signed-out page paints `.theme-dark.theme-darker` — a `#121214` field (`dark.background.page`, `{background.base.lowest}`) under the marketing nav. The 56px `DISCOVERABLE SERVERS` display heading (`ds-h1`, ABC Ginto Nord, `dark.text.strong`) sits over the 640x64 search box (`ds-search`, 12px radius on a 12% white wash, `core.component.search`) — the input itself is a 3px-radius field (`ds-search-input`, `core.radius.field`, focused/filled measured). Below, the category row: 57px-tall 12px-radius pills (`ds-tab`, `core.radius.control`) where the selected `All` fills `rgba(151,151,159,0.16)` (`dark.background.selected`, `{background.mod.normal}`) on a `rgba(151,151,159,0.12)` hairline (`dark.border.card-line`).

## The server card

The discovery grid's unit is 322x362 (`sc-card`, `core.component.server-card`): banner art on top, the 51x51 squircle icon (`sc-icon`, `core.component.server-icon`) overlapping the seam, then a `#202024` body (`dark.background.card`, `{background.base.low}`) on the `rgba(151,151,159,0.12)` hairline at 8px (`core.radius.card`). Inside: the 20px semibold name with verified check (`sc-name`, `dark.text.strong`), a muted description, and the `N Online · N Members` line (`sc-members`, 14px) with its `#43b581` presence dot (`dark.text.online`, `{mint.green}`). Cards are real links to `/servers/<slug>`; hover measured, never followed.

## The server detail

A `/servers/<slug>` page is profile-meets-CTA: the banner art (`sv-banner`, 1440x600 measured), the 28px Ginto name with verified badge (`sv-name`, `core.font.size.measured.section`), the member counts (`sv-members`), the `#5865f2` `Join the Conversation` button (`sv-join`, 320x48, `dark.action.primary`, `#4752c4` `dark.action.primary-hover` — hover/focus measured, never followed; joining needs an account) and the ghost `Share` button (`sv-share`, 320x44). Below: tracked ABOUT/SUPPORTED LANGUAGES section labels (`sv-about`) and `rgba(151,151,159,0.12)` category chips (`sv-chip`, 10px `core.radius.chip`, `dark.background.chip`, `{background.mod.subtle}`).

## The auth surface

`/login` and `/register` paint an oklab panel (`lg-card`, 784x414, `dark.background.panel`, 8px `core.radius.card`, `core.shadow.card` 0 2px 10px rgba(0,0,0,0.2)) on the animated brand backdrop. Inside: the 24px "Welcome back!" (`lg-h1`, `core.font.size.measured.card-title`), label+field pairs — 414x44 email (`lg-email`) and 374x38 password (`lg-pass`, `core.component.auth-field`, black@12% fill, `dark.background.field`, `rgba(151,151,159,0.2)`-ish borders), the `Forgot your password?` and `Register` links in oklab blue (`lg-forgot`, `dark.text.link`, `{text.link}`), and the 416x40 `#5865f2` `Log In` submit (`lg-submit`, `dark.action.primary`, `rgba(255,255,255,0.08)` border `dark.border.hairline`). The right side holds the 240x322 QR-code panel (`lg-qr`, `core.component.qr-panel`). Fields were focused and filled then cleared; nothing was ever submitted.

## Two themes, one page

There is no theme toggle signed out, yet both themes are real paint: the app surfaces carry `.theme-dark.theme-darker` while the marketing chrome injected into them wraps in `.theme-light`. The `light.*` set resolves `.theme-light` (the marketing palette plus the declared light app theme — the standalone app-light surface is account-gated and unpainted); `dark.*` resolves `.theme-darker` — the roles are measured dark paint, not declared guesses. `.theme-dark` and `.theme-midnight` are declared siblings, unpainted signed out.

## Mobile

At 390 wide the marketing bar compresses to 342x64 (`m-bar`), the display heading drops to 31px (`m-h1`, `core.font.size.measured.display-mobile`), and discovery stacks the 358px search and single-column server cards (`m-card`, 358x380).

## Boundaries

- The whole client needs an account — `/channels/@me` redirects to `/login`; joining a server, accepting an invite, messages and settings were never reached.
- `/invite/<code>` painted a dark frame but no invite card signed out in this pass — recorded as a boundary.
- The app's own light theme, `.theme-dark` and `.theme-midnight` variants, and the compact/cozy density classes are declared but unpainted signed out.
