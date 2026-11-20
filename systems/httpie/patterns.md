# HTTPie patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md), the multi-width geometry in [raw/layout.json](raw/layout.json), and the full-page evidence in [screenshots/](screenshots).

Two surfaces carry the one system: the **marketing and docs site** (home, /desktop, /cli, /ai, /docs, /jobs, /blog, /download, /about, /terms, /privacy) and **/app**, the HTTPie-for-Web client running signed out in its "Incognito space". Both paint the same hand-written `--color-*` roles on `:root`/`.dark:root`; the marketing pages add literal rgb() styling on old-Tailwind/CSS-Modules classes (the `core.palette.*` tokens).

## The marketing frame

Every page carries the same chrome: a **top nav** (`site-nav`, `nav.Navigation_navigation`) inside a `site-container` capped at **1440 px** with **55 px side gutters** — wordmark, Desktop / Terminal / AI / Docs / Jobs / Blog links, the social icons and the solid **"Go to App →"** primary button (`nav-cta`, the `accent` role) — and a **footer** (`site-footer`) with link columns, the social buttons and the **LIGHT MODE / AUTO / DARK MODE** `ThemeToggle` radio stack, the product's real theme control. Interior sections sit on a `site-grid`: a **12-column** grid (≈88.8 px columns, **24 px** gutters inside the 1440 px container at 1440 wide; ≈58 px columns inside the docs column). A page scrolls the document; nothing on the marketing frame is sticky.

- **Home** stacks the hero (`HomeHero`, the "FLOW THROUGH APIs" headline in Pie Headline beside a layered product still), a featured-post strip, the Desktop and Terminal product sections, a 3-up testimonial wall (`testimonial-card`, `grid-cols-3` with 40 px column / 48 px row gaps), the companies logos and the newsletter forms (`newsletter-input`, `newsletter-button` — measured and clicked into, never typed or submitted).
- **/cli** is the terminal page: the install picker (`cli-install-select` pills — brew, apt, choco…) above dark **code panels** (`cli-code-block`) with copy buttons (`copy-button`, forced-state pressed only).
- **/blog** is the changelog index: rows of post previews (`post-card`, `post-title-link`); the page is ~15.5k px tall so the full shot is bounded at two chunks.
- **/desktop**, **/ai**, **/jobs**, **/download**, **/about**, **/terms**, **/privacy** reuse the frame and grid; `/pricing` 404s and is captured as the product's **not-found** page (`notfound-*`).

## The docs shell

`/docs`, `/docs/desktop` and `/docs/cli` keep the nav and footer but swap the scrolling page for a **viewport-high shell**: the left **"On this page" TOC** aside (`docs-toc`, `aside.DocsPage_tableOfContents`, 315 px at x=55, sticky at top=130) and the **article pane** (`main.DocsContent_content`, 768 px of prose inside a 1071 px grid column) scroll inside their own overflow panes — the desktop manual's article is ~96k px of content. The docs' own scroll containers are the reason the capture kit expands the pane for `-full` shots and bounds them at three chunks (42k px) with the truncation recorded in the sidecar. The docs layer adds the prose components — `docs-code-block` (the fenced block the `code.*` syntax palette paints), `docs-inline-code`, `docs-side-link` — and the ⌘K DocSearch dialog (opened for the icon collection, never queried).

## The app shell (/app, signed out)

`/app` is a fixed **viewport-high** shell — the document never scrolls; `docH` is exactly the viewport height at every width. Three rails divide it:

- The **SideMenus icon rail** (`app-sidebar`'s far-left column, **49 px** at desktop, 40 px at 390): the green mark, the spaces/apps grid icons, help, and the syncing avatar at the bottom.
- The **side panel** (`Layout_sidePanel`, ~348 px): the **"Incognito space" switcher** (`app-space-button` — its own press opens the current space's tab in the strip; no dropdown menu paints for the unsigned product), the **+ Collection** add button (which opens the Create-collection dialog — never submitted), and the **Drafts** shelf (`app-drafts-tab` header, the `app-drafts-empty` InfoBlock: "Drafts are your unsaved requests. Organize the ones you want to keep in collections"), then the "Migrate your data" import card at the foot.
- The **main workspace** (`main.Layout_content`, a ResizablePanels split): the **tab strip** of request cards (`app-request-tab`, "GET untitled"), the **request line** — a three-column grid `TabHeadingRow` (≈69 px method `app-method-button`, ~849 px URL field `app-url-field` holding the prefilled `httpie.io/hello` in Pie Monospace, ~109 px `accent` **Send** — measured, never pressed) — then the **Params / Headers / Auth / Body** panel tabs (`app-panel-tabs`, `app-panel-tab`, `app-param-checkbox` row), and the **Request / Response** split whose resting response pane is `app-response-empty` ("Not sent" — the send surface is an uncaptured boundary). The **Environments** selector (`app-env-button`) opens the environments manager as another tab in the strip (`app-env-panel`, `app-env-create`). The first-load "Introducing HTTPie AI" dialog (`app-dark-ai-promo`) mounts on some loads and is closed through its own Close button — "Try it out" was never pressed.

On the phone (`app@390`) the same shell compresses: the icon rail shrinks to 40 px, the side panel becomes a fixed sheet (300 px), and the request line's grid compresses to 63 / 211 / 68 px — the builder is a desktop-first surface and the mobile shots document that limited read.

## Motion and focus

The measured set lives under `core.motion` (the probe in `raw/motion.json`, docs/decisions/0001): transitions on the components run ~150–300 ms; `prefers-reduced-motion` is reported as **ignored** on these pages — nothing in the harvest honours it, which the package records rather than fixes. Focus rings paint through `--color-focus` (`focus.ring`); where a real keyboard focus could not be held, components.md says so (`via: focus failed`) instead of claiming a ring.

## Themes

httpie.io boots `html.dark`: `dark` is the painted default, `light` the switched set painted by the footer's own ThemeToggle radios (persisted to `localStorage.theme`, which /app reads). Both sets resolve the same `--color-*` names — `.dark:root` re-points them — so every semantic role exists in both themes, and aliases like `component.button.cta.bg` resolve per theme.
