# Exa patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

Exa's public surface is three sites with three different makeups: a warm paper marketing site (light only), a Mintlify documentation app (a real light/dark pair) and a single auth card.

## Marketing chrome (light)

The 55px header (`component.header-height`, the `--nav-height` bar) sits under a 48px "Introducing Exa 3.0" announcement strip (`--announcement-banner-height`; its text row is `component.banner-height`). Inside: the 70px `exa` wordmark, three `div.cursor-pointer` menu triggers (Products/Solutions/Resources), the Docs and Pricing links, a ghost Sign-in, a bordered Contact-sales and the black 8px-radius Sign-up pill (`light.marketing.action`→`color.neutral.black`, `radius.base`).

Hovering a trigger opens a `div.absolute.top-full` panel — the Products menu measures 380 x 485 (`component.menu-width`) with product links grouped as name + one-line description and a use-case column. It is hover chrome: a pointer move opens it, `Escape` or moving off closes it, and none of its links were followed. See [home-light-menu](screenshots/home-light-menu.png) and [mkt-menu](components/crops/mkt-menu-default.png).

## The home search demo (exa.ai/)

The hero is the product pitch compressed into a working widget: the 46px Arizona Flare headline over a 700px demo card (`component.demo-widget-width`) on the cream field:

- a single-line query field (24px measured height), pre-filled with a sample query;
- a Search/Agent segmented control;
- **LATENCY** pills — Lite `300ms` / Auto `1s` / Deep `~10s` — and **CATEGORY** pills — Full Web / News / Companies / Research / People / Financials — plain bordered chips that reconfigure the preview locally;
- **OUTPUT** tabs — Results / Answer / Structured;
- and the blue-gradient `Run preview` arrow button (32px, `light.marketing.run-fill`).

The pills and tabs were toggled as measurement states; the arrow was never pressed — signed out, the output panel shows the widget's verification message. See [home-light-demo-tabs](screenshots/home-light-demo-tabs.png) and [demo-widget](components/crops/demo-widget-default.png).

## Pricing grid (exa.ai/pricing)

"Start searching for free" over a USE CASES pill row (Coding agents / Chatbots / News monitoring / Enrichments / Voice agents / People search / Company search — local toggles that switch the estimate), then the three-tier grid: STARTER **Free**, DEVELOPER **Pay as you go**, ENTERPRISE **Custom**. The plans paint as one `divide-y` table — tier, price line, black action row, checkmarked `Includes:` rows — not independent cards. See [pricing-light-default](screenshots/pricing-light-default.png) and [pricing-light-usecase-chatbots](screenshots/pricing-light-usecase-chatbots.png).

## The docs shell (exa.ai/docs — Mintlify, light + dark)

```
+---------------+------------------------------------------------------+
| 288px sidebar | 56px topbar: logo · Documentation/API Reference/     |
| #sidebar      |   Changelog tabs · Blog · API Dashboard (blue pill)  |
| search button +------------------------------------------------------+
| Ctrl K · nav  | article: h1 · body · code blocks · CTA banner        |
| tree · theme  |  "Add Exa to your agent"                             |
| toggle        |                                                      |
+---------------+------------------------------------------------------+
```

- Sidebar (`component.docs-sidebar-width` 288px): the field-styled `Search … Ctrl K` button (267 x 36, `component.docs-search-height`), the theme preference button (30px), the nav tree — Overview, Get Started, Search, Agent, Other APIs — as 32px rows.
- Topbar: wordmark, the `Documentation | API Reference | Changelog` text tabs, a Blog link and the blue-filled `API Dashboard` pill (`light.docs.primary`/`dark.docs.accent`).
- Content: the doc article with code groups under Python/JavaScript/cURL tabs, twoslash-annotated samples (`light.docs.twoslash.*`/`dark.docs.twoslash.*`), and the blue "Add Exa to your agent" banner.
- A `textarea.chat-assistant-input` "Ask a question…" input sits in a slide-over offscreen right until the assistant opens — measured collapsed, never opened or sent.

The dark theme is a real flip (`html.dark`): the same set re-resolves — page `#0b0b10` (`dark.docs.surface`), border `#26272c` (`dark.docs.border`), primary darkened `#1840ed` with lightened accent `#5f7cff`. See [docs-light-default](screenshots/docs-light-default.png) and [docs-dark-dark-default](screenshots/docs-dark-dark-default.png).

## The sign-in card (auth.exa.ai)

dashboard.exa.ai redirects signed-out visitors here: a 360px card (`component.auth-card-width`) on white — the "Start building with Exa" Arizona Flare heading, a 50px `Continue with Google` button, a 44px `Continue with email` brand-blue button (`light.signin.action`→`color.brand.default`), the `Email` field (44px, `#e0e0e0` hairline, brand-blue focus `light.signin.field-focus`), an SSO link, and a Geist-Mono `exa.search()` code sample beside it. The field was focused and filled then cleared; nothing was submitted. See [signin-light-default](screenshots/signin-light-default.png).

## Mobile (390px)

The marketing chrome collapses to a 64px bar (`component.mobile-header-height`): wordmark, 32px hamburger (`component.hamburger`), Sign-up. The hamburger opens a `div.fixed` full-height drawer (390 x 844 measured) listing the same menu content as accordions — a local toggle, its links never followed. The docs keep the same shell scaled down. See [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png).

## Motion and focus

Controls transition cheaply — the declared default is `150ms` (`core.motion.duration`, shared by marketing, auth and docs' `--motion-duration`) with the docs' `cubic-bezier(0.2, 0, 0, 1)` standard curve (`core.motion.docs-easing`); the mega-menu animates opacity/transform over 100ms and the hero headline runs a word-swap animation (no token: `raw/css-vars.json` resolved no `--text-swap-*` value). Focus is a 1px auto outline — the browser's default `#101010` ring on marketing (no product token; listed under `_gaps` in raw/component-tokens.json), `#1840ed`/`#5f7cff` on docs, brand blue on the auth field — never a shadow ring except on the docs search button.
