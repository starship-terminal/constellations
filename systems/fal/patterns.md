# fal.ai patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (light, Webflow)

The marketing pages paint one theme on the Webflow layer (`marketing.*` tokens): the home hero is "The generative media cloud" in Focal Web 96px/86.4 at weight 500, painted cyan `#99edff` (`marketing.brand.cyan`) over the black hero field, followed by a neon-lime `#adff00` pill CTA (`light.action.hero-cta`, 134.6 x 44, 2px radius, dark-olive `rgb(64,55,0)` label). The fixed header is an 88px transparent bar (measured `mkt-header`, matches `component.mkt-header-height`) holding black text links at weight 500, a ghost `#e5ece7` Contact-Sales pill (`light.action.secondary`) and a black Get-Started pill (`light.action.primary`). The Products trigger opens a local w-dropdown disclosure — measured, its links never followed. Section headings drop to ~59px/53 (`mkt-section-h2`). The footer inverts to a pink `#ffc4d6` field (`marketing.brand.pink`). See [home-light-default](screenshots/home-light-default.png) and [home-light-full](screenshots/home-light-full.png).

Pricing is the same chrome: a 96px headline, then the usage-based `pr-price-table` — a 1337 x 364 `#e5ece7` panel of 33px `pr-price-row` rows in Focal Text — with white `pr-plan-cta` pills. There is no billing toggle or plan-card grid; the table is the pattern. See [pricing-light-full](screenshots/pricing-light-full.png).

## The app shell (dark)

`/explore`, `/models/*`, `/login` and the phone pass paint `html.dark` over `--surface-page` `#121216` (`dark.surface.page`). A 32px announcement strip (`dark` measured `app-announce`: `#142657` field, cyan `#99edff` text, a 28px dismiss X measured never pressed) sits above a 48px header (`component.app-header-height`): the fal mark, a Products trigger that opens a 322 x 201 `div.top-center` panel (`app-nav-menu`) of 308 x 65 `a.text-content-subtle` product entries on `#19191a` (`palette.neutral.950`), a Documentation link, then a ghost 64 x 32 Log-in and a solid 74 x 32 Sign-up (`dark.action.primary` — a white pill on dark).

The catalog opens on a hero carousel: a full-bleed slide with badges, a heading and two pills, `card-cta` (101 x 36 "Try it now!") and `card-docs-link` (93 x 36 "See docs"), over a row of `carousel-dot` progress segments. Under it sits the search field (953 x 24, `search-models`, focused and filled then cleared) and sections of 360 x 350 `model-card` tiles (`component.model-card-*`): artwork with badge ribbons, then the endpoint-id line (`model-card-title`, a `span.truncate` in Focal 16/20 at weight 400; cards carry no heading element) with publisher and description. A pager (`pager-next`, `pager-dot`) pages a section's tiles; `pager-next` pressed collapses to 0 x 0 mid-press animation — a real measured state, not a miss. See [explore-dark-default](screenshots/explore-dark-default.png) and [explore-dark-full](screenshots/explore-dark-full.png).

## The model page and playground

The model page composes the shell with a focal 20px/28 weight-300 heading (`mp-h1`), a violet-alpha badge `rgba(120,58,251,.2)` (`mp-badge`, `dark.action.badge`), API/billing tabs (95 x 40 `mp-tab`), an endpoint chip + copy pair (`mp-endpoint-btn`, `mp-copy`), the "Onboard your agent" prompt button, and the Open-in-Sandbox pill (`mp-sandbox-link`, measured never followed). The playground form is a 654 x 98 prompt textarea (`mp-prompt` — focused, filled, cleared; inference never run), 192 x 40 parameter option pills (`mp-param`), a "More" disclosure, and the violet `#783afb` Sign-in-to-run action (`dark.action.run`, 119 x 40, 4px radius — it links to login signed out). Result tabs (`mp-result-tab`) and a `#202022` Download pill (`mp-download`) sit below. The API tab swaps the playground for a 1070 x 347 code sample (`api-code`, chivoMono) with language tabs (`api-lang-tab`) and a copy button — the code was read for styles only, never copied. See [model-dark-default](screenshots/model-dark-default.png) and [api-dark-default](screenshots/api-dark-default.png).

## Docs (light, fumadocs)

`/docs/*` is its own surface and token layer (`docs.*`, `light.docs`/`dark.docs`): a 47px `.nav-tabs` topbar (`docs-topbar`), a 232 x 36 search trigger (`docs-search`), a light/system/dark segment (`docs-theme-btn`, measured never cycled), a fixed 350px sidebar of muted `#727075` links (`docs-sidebar`), and a "Build with fal" hero — Focal Medium 56px/56 (`docs-h1`) with a Focal lead (`docs-hero`), a 309 x 41 hero search (`docs-hero-search`), 650 x 444 section cards (`docs-card`), a 264px TOC (`docs-toc`) and code groups with a 26px copy button (`docs-code`, `docs-code-copy`). Focus is a 1px `#5718c0` ring (`palette.primary.700`). See [docs-light-default](screenshots/docs-light-default.png) and [docs-dark-dark-default](screenshots/docs-dark-dark-default.png) for the dark pass.

## Login (dark, OAuth-only)

The login page is a 400 x 389 centred card (`li-card`): the fal mark, "Login or sign up" (`li-h1`, focal 36px), 400 x 40 OAuth rows (`li-oauth-github`, `li-oauth-google`), a Use-SSO chip (`li-sso`) and a support link. Everything was measured at rest — no provider button was ever followed. See [login-dark-default](screenshots/login-dark-default.png).

## Phone (390 x 844, dark)

The explore surface collapses to a 390 x 48 header (`m-header`) with a 32 x 32 "Open navigation" button (`m-hamburger`) that toggles a nav sheet of `a[role="menuitem"]` rows (`m-nav-item`, ~32px tall with 12px vertical padding — see [mobile-explore-dark-drawer](screenshots/mobile-explore-dark-drawer.png)); Escape closed it after measuring. A compact search (`m-search`) and one-column 283 x 307 model cards (`m-model-card`) carry the catalog. The marketing home keeps its 88px chrome pattern at 390 wide ([mobile-home-light-default](screenshots/mobile-home-light-default.png)).

## Boundaries

Everything past login — the dashboard, API keys, billing, deployments, the sandbox and real inference — is an authenticated surface this package never reached. The OAuth buttons, Sign-in-to-run, Open-in-Sandbox, Download, Contact-Sales and Get-Started actions were measured, never followed. The consent card was hidden, never answered. The `/models/*` light pass hit an edge security check mid-capture (`model-light-light-default.png` is the only shot; its measurements come from the dark pass).
