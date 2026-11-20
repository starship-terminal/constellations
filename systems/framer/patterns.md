# Framer patterns

How the captured components combine into the public surfaces. Every page is a Framer site behind the same chrome; the community stack and the auth shell are different apps with their own look.

## The marketing chrome

Every www page mounts the same top bar (64px, measured `mkt-header`): the Framer mark (SVG + wordmark, measured `mkt-logo`), the mega-dropdown triggers **Platform / Solutions / Resources** (`a` elements without href — their panels open on pointer hover, never a click, and the page dims behind them), the **Enterprise** and **Pricing** links, then **Log in** and the **Sign up** pill. The nav link ink reads `rgba(255,255,255,.8)` (`dark.color.text.navInk` → `color.palette.alpha-white.80`); on hover it lifts to full white. The Sign up pill is a white fill (#fff) with black ink — the measured `dark.color.action.ctaFill/ctaInk`.

The Platform mega-dropdown (measured `nav-panel`, ~650px wide) lays out three link columns — **Create** (AI, Agents, Design, MCP), **Build** (CMS, Hosting, Performance, Collaborate), **Grow** (SEO, AEO, Convert, Publish) — beside an **Updates** thumbnail card. Solutions and Resources open the same shape. Screenshots: [home-dark-menu-platform](screenshots/home-dark-menu-platform.png), [home-dark-menu-solutions](screenshots/home-dark-menu-solutions.png), [home-dark-menu-resources](screenshots/home-dark-menu-resources.png).

The footer is a deep sitemap on the black field (Product, Solutions, Resources, Company columns) with social glyphs and the English/Japanese locale `select` (78x18, measured `locale-select`).

## The hero and the embedded demo

The home hero centres the display heading at **GT Walsheim Medium 54px/54px 500** (`font.size.measured.hero`, `font.family.measured.display`) in white ink over the #000 field, a muted grey subline, then the paired controls: **"Get started for free"** — a white 34px pill, 8px radius — beside the ghost **"Install the MCP"** button (a `rgba(255,255,255,.1)` fill, same shape). A right-aligned **"New: …"** badge link flags the latest feature. Below, a large rounded demo panel plays the product demo: an "Ask Framer…" chat card with a model picker and input row — pre-rendered marketing content, not the product.

The product pages repeat the shape: each of /ai/, /agents/, /design/, /mcp/, /enterprise/, /solutions/designers/ opens with a masthead, a proof band and section content, all on the same black field with `neutral-1f…24` cards and `alpha-white.7` hairlines.

## The pricing grid

/pricing opens "Start free, then scale your site" with the **"Yearly billing"** switch (a small 86x20 control with a blue-on thumb) beside the plan grid: **Free / Basic / Pro / Enterprise** columns at 300px each. Free and Enterprise carry flat CTAs; Basic and Pro carry a **"Credits per month" select** (250x34) that re-prices the tier, and Pro carries the saturated **#0099ff "Start with Pro"** CTA — the only saturated plan button (measured `color.action.planCtaFill`). Feature lists read as hairline-separated rows under the price. A **FAQ** of question rows ("What are credits?") sits below. Prices rendered in SGD during this capture — a locale artifact, not a style.

## The community gallery

/community/gallery/ is the product's community stack — a different app, also dark (#111-ish field): a slim header (**Community** menu button, Experts / Gallery / Help links, a "Search Gallery" input — 203px, measured), the **"Gallery"** masthead in walsheim, a taxonomy of category columns (Business, Agency, Software, Ecommerce, Portfolio, Organizations, Places, Health…), then the sort row — **Trending / Recent** pills and a **Vibe** dropdown (30px chips, measured `gal-filter`) — over a card grid where each site card carries a thumbnail, title, author and a dark **"Open"** button (55x30, measured `gal-open`). /marketplace/templates/ is the same stack and shape for paid templates.

## The auth boundary

/login is a light third stack: a centred card on a white field — the Framer mark, **"Welcome to Framer"** + "The web design agent" subhead, the dark **"Continue with Google"** button (230x30, `color.action.googleFill` → `neutral-22` — near-black, not branded blue), an **OR** hairline, the **"Enter your work email…"** field (228x30, 8px radius, grey placeholder) and the greyed **Continue** submit. Sign up routes here too: /signup redirects to /login. Everything past this card — the dashboard, the editor, CMS collections, publishing, workspaces — needs an account and was never reached.

## Mobile

At 390px the header keeps the mark, Log in and Sign up plus a 64x64 **menu toggle** (`data-framer-name="Mobile Menu"`). Its overlay fills the viewport with the five nav links in a left column — Platform, Solutions, Resources, Enterprise, Pricing — and an × close (measured `m-drawer`, screenshot [mobile-home-dark-drawer](screenshots/mobile-home-dark-drawer.png)). The hero stacks the same heading/CTA pair; the pricing grid scrolls its columns; the gallery moves its filters into a mobile toolbar (the DOM ships a hidden mobile copy of the same buttons ahead of the desktop row).

## Motion and focus

The motion probe found 17 moving elements on the homepage (scroll reveals, marquee/drift loops — `core.motion.*`), 1-2 on pricing and login, and 101 on the gallery (the thumbnail hover/parallax grid). Under `prefers-reduced-motion: reduce` the homepage partially slows; pricing, gallery and login ignore it. Keyboard focus lands as a visible ring on the CTA pills (measured `focus-visible`, `color.border.focusRing` #101010 on the white Sign up pill); the mega-dropdown panel closes on blur, so focus inside it could not be held.
