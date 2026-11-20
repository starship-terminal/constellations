# Grok / xAI docs patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## The docs shell (light by default)

Every docs.x.ai page is a viewport-high shell — the document never scrolls. A fixed 1440 x 80 header (`docs-header`) spans the top: the wordmark link (`docs-logo`, an svg whose aria-label is "SpaceXSI Docs home"), the product switcher ("Open API sections"), section links (`docs-section-link`, 85 x 32, 14px medium at 60% ink), the 208 x 36 `⌘K` search pill (`docs-search-pill`, 14px medium on a hairline-bordered rounded field that lifts to rgba(12,12,12,0.03) on hover), the 28 x 28 round theme button (`docs-theme-button`) and a GitHub link. Beneath it the two panes scroll independently: the 272px sidebar (`docs-sidebar`, 272 x 828) with its collapsible `peer/menu-button` groups (`docs-sidebar-group`, opened by its own chevron) and 256 x 32 page links (`docs-sidebar-link`, 13px, the same rgba(12,12,12,0.03) hover wash; the active page `docs-sidebar-active` sits on white at weight 500), and the article pane (`main.max-w-7xl`, content column 672px) which carries the page. Article pages close with a sticky bottom `footer` bar (`docs-page-footer`, border-t `border-border-l1` on `--bg-base`) holding muted 14px actions — "Copy for LLM" (`prose-copy-llm`), "Share feedback" (`docs-footer-button`) and the "View as Markdown" link (`docs-markdown-link`, 133 x 16, 12px semibold at `fg-muted`).

## Prose

The article grammar is restrained: the h1 is xVf at 48px/52.8 in an intermediate variable weight of 450 (`prose-h1`), h2s step to 30px (`prose-h2`), body is 14px/24 (`prose-p`), links (`prose-link`) carry the primary underline treatment. Inline code is the site's most characteristic detail — an `xMono` span tinted **`--darksolar` orange** (`prose-inline-code`, rgb(255, 100, 10) — the solar #ff640a) with no background fill. The faq page's questions are plain 24px h3s (`faq-question`), no accordion. A `bg-card` nav card (`docs-next-card`, 672 x 156, fill rgb(249, 248, 246) = `light.bg.card`) closes each page; hover shifts it to a slightly deeper srgb tint — the `--color-card-hover` alias.

## Code blocks and SDK tabs

Code samples sit in a dark-tinted `--bg-codeblock` panel in both themes (`docs-code-block`, xMono 13px/20 at rgb(225, 228, 232), syntax painted by the `color.shiki.*` set) — the panel stays dark even on the light page. Language selection is a Radix tablist above the sample (`docs-code-tabs`/`docs-code-tab`, 98 x 24 tabs at 12px); activating a tab is a local UI toggle that swaps the published snippet — captured as `generate-text-light-tab-python`.

## Pricing and API tables

/developers/pricing and /developers/models carry real tables (`pricing-table`, 806px wide rows of 14px/21): 14px medium `th` cells (`pricing-th`) over 70px `td` rows (`pricing-td`), bordered by the muted border role and repainted under dark (`pricing-table` dark state). The api-reference index is a landing page — base URLs, the inference and management-key API groupings — with the endpoint detail behind it.

## The ⌘K search dialog

Ctrl+K opens a cmdk command menu (`docs-search-dialog`, a 1000 x 485 white card — #0a0a0a in dark) over the page: the 1000 x 48 command field (`docs-search-input`, clicked into for the focused state, nothing typed) above resting suggestion rows (`docs-search-item`, 475 x 54 at 14px, hover washing a 10% tint). "Ask Grok" leads the suggestions; no query was ever entered, so result rows and the answer path stay uncaptured. The dialog was also measured dark — its own sequence: closed, repainted by the header theme button (which the open overlay occludes), reopened with Ctrl+K.

## Grok Bot's phone panel

/grok-bot/overview embeds the product's illustrative mock — `.gbm-panel` (`gbm-panel`, 231 x 172), a phone-shaped routine panel drawn in system-ui rather than xVf, measured light and dark.

## Mobile (390px)

The phone surface compresses to a 390 x 68 bar (`m-docs-topbar`): the 36 x 36 "Open navigation menu" hamburger (`m-docs-hamburger`), wordmark, search and theme icons. The hamburger opens a **full-screen** fixed aside (`m-docs-drawer`, 390 x 844, white surface over the page) carrying the nav — a sheet, not a side drawer — captured opened in `mobile-home-light-drawer` and measured as `opened`.

## Motion and focus

Transitions are the Tailwind `--default-transition-duration` 150ms on `--default-transition-timing-function`, with `--ease-in/-out/-in-out` curves and the `--animate-pulse`/`--animate-spin` keyframes for the loading and skeleton states; hover washes settle in that window. Focus is a plain 1px outline ring (`docs-section-link` focus-visible, outline rgb(16, 16, 16) — `light.fg` — at 1px). The motion probe's honest caveat: **prefers-reduced-motion is ignored on most pages** — the animated gradient and ambient loops keep running; only two of eight probed pages partially honour it (`raw/motion.json`).

## Theme architecture

The portal boots `html.light` (next-themes reads `localStorage.theme`) — the `light` token set is the painted default. The header's "Switch to dark theme" button flips `html.dark`, and `.dark`/`:root.dark` re-point the semantic roles: `--bg-base` #ffffff→#0a0a0a, `--fg` #0a0a0a→#d5d9e2, `--primary` inverts (black button → white), `--sidebar-background` #ffffff→#121212, `--chart-*` re-points to the dark ramp, while `--bg-codeblock` #121212 and `--fg-success` #3f9751 stay constant — the code panel is dark in both themes. Fifteen names exist only in dark (`--border`, `--input`, `--ring`, `--alert`, `--on-alert`, the `--background-*` extras, `--content-*`, `--sb-*`); they sit in the dark token set alone and were never inferred for light. Dark repaints are captured as `*-dark-*` screenshots and `dark` component states — painted by the site's own button, verified, and switched back.

## The boundary beyond the docs

This package documents the docs portal, not the product. grok.com's chat surface never cleared the Cloudflare managed challenge (bounded headless and headed attempts both failed), and x.ai, console.x.ai, status.x.ai and accounts.x.ai returned Cloudflare 403 blocks from the capture host. Those surfaces are named here as blocked boundaries — no pixel, token or component in this package claims to describe them.
