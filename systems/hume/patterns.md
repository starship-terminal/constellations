# Hume AI patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md), the multi-width geometry in [raw/layout.json](raw/layout.json), and the full-page evidence in [screenshots/](screenshots).

Four public origins carry the system, each on its own token layer: **www.hume.ai** — the marketing and product site (a Next.js + Tailwind v4 build whose `:root` declares the product layer: `--background`/`--foreground`, the eleven-pastel `--accent-*` ramp, the `--gradient-*` wash stops, `--title-*` display sizes, `--font-*` stacks); **dev.hume.ai** — the Audio Decisions docs (a Fern build with the only real theme control); **demo.hume.ai** — the playground's invitation gate; and **app.hume.ai/log-in** — the platform's sign-in card on an oklch shadcn layer.

## The www frame

Every www page carries the same chrome ([home](screenshots/home-light-default.png)):

- A **NEW announcement banner** sits at the very top (the 36 px the sticky nav is offset by), then the **dark sticky nav** — `header.on-dark`, 56 px at `top:0`, z-50, painted `#1e1e1d` — with the wordmark, Emotion Science, the Products / Solutions / Benchmarks / Resources menu buttons and the white pill **"See a Demo"** CTA (`nav-cta`, `light.button.cta.bg`).
- Content lands in `max-w-300` (**1200 px** with `px-6` gutters); wider feature sections stretch to `max-w-336` (1344 px). A `progressive-blur` fixed layer sits over the scroll edge.
- The **hero is dark over a light page**: the headline block (Martina Plantijn at `clamp(40px, --k·58, 77px)` — 58 px at 1440, 77 px at 1920, ~41 px at 1024, ~37 px at 390 — the `--k` viewport factor scales the whole display ramp) sits on the near-black band with the pastel-chip audio visualisation, and the page opens onto the `bg.default` #fdfdfc ground below the fold.
- Interior pages reuse the same frame: `/benchmark` adds a `grid-cols-4` stat strip (283 px cells, 1 px gaps) and a leaderboard row grid (`1.5rem 2rem 1fr 3rem ~5rem` columns); `/blog` lists post cards that collapse to a `grid-cols-2` feed at 390; `/contact-form` is a two-column `min-h-svh` split (690 px form | 690 px panel at 1440).

## The question/answer pattern

Hume's signature surface is the **decision-model demo grammar** — a two-zone composition ([home playing](screenshots/home-light-playing.png), [decision-model](screenshots/decision-model-light-default.png)):

- The left zone is a **media card** — the customer-call player (`player-card`, `player-transport`) over a gradient wash, 340 px wide with the rubric text and a play/pause/stop transport row.
- The right zone is the **question list**: rows of `340px + 1fr` grids — a `Pick One` / `Yes/No` / `Scale` type label (80 px + content rows with 12 px gaps) and the **pastel answer chips** painted from the eleven-colour `--accent-*` ramp (pink/magenta/purple/blue/sky/mint/green/lime/orange/coral/salmon). The chips are the product's brand voice: every categorical answer is a small pastel pill, never a saturated fill.
- The same grammar recurs on `/benchmark` (the `benchmark-tab` category tabs, the leaderboard rows) and inside the blog post's embedded comparisons.

## The docs shell (dev.hume.ai)

The Fern build is a **viewport-high shell** ([docs overview](screenshots/docs-overview-light-default.png)):

- A **fixed 93 px header** (49 px at 390): the hume mark + product switcher, the Search `/` button, `Ask AI`, `Start building`, the white `Get access` pill, and the **Theme button** — the one real theme control on any surface — whose Light / Dark / System menu repaints `html.dark`.
- The **left sidebar** (`fern-sidebar-desktop`, 271–272 px at y=92) is its own scroll area (`fern-scroll-area-viewport`, ~1043 px of content in 808 px); the **right TOC aside** (272 px, sticky) tracks the article. The article body is Fellix 36 px h1 over 16/26 body.
- Reference pages split `fern-layout-reference-content` into **two 528 px columns** — prose left, the request/response code blocks right with their own inner scrollers. The docs code block is its own component (`docs-code-block`, the `docsCode.*` tokens).
- At 390 the sidebar collapses behind the header menu button's drawer ([mobile docs drawer](screenshots/mobile-docs-overview-light-drawer.png)).

## The gate surfaces

- **demo.hume.ai** is a single invitation wall ([gate](screenshots/demo-gate-light-default.png)): a 45 px header, then a centered "Start from your invitation" card with the black `Contact sales` pill (`demo-gate-cta`). The playground behind it is the documented boundary.
- **app.hume.ai/log-in** is a `fixed inset-0` centered card ([login](screenshots/login-light-default.png)): the hume mark, "Welcome back" + Fellix form — email, password with a show/hide eye, the black `LOG IN` pill on `app.background.button` #000000, and Google / Apple OAuth buttons above it. Nothing past the card was entered.
- **/explore/speech-prosody-model** is a full-viewport canvas explorer (`docH` = viewport height; the visualisation is a painted bitmap, not DOM — its internals are documented as a gap, not invented).

## Motion and focus

`core.motion` records the probe's readings (`raw/motion.json`): the www surface's component transitions run **150 ms** on `cubic-bezier(0.4, 0, 0.2, 1)` (the Tailwind default ease, nearly every property), the contact fields 150 ms `ease-in-out`, the player transport and contact submit 200 ms, the nav menu buttons 250 ms opacity; the docs shell adds 500 ms header/drawer curves on `cubic-bezier(0.32, 0.72, 0, 1)`. The reduce verdict is **partial**: the www pages carry an authored `*, ::before, ::after { transition-duration: 0.001ms; animation-duration: 0.001ms }` reset that stops every moving element (`honours`); the docs carry authored reduce rules but keep 74 of 88 moving elements running; the demo and app surfaces ignore the setting entirely — the `spin` loader loops on both. Focus rings on the www surfaces paint a thin `outline: auto` ring in the ink colour (`core.component.focus.*`, 1 px #101010); the app layer uses its accent ring (`focus-visible:ring-(color:--accent)`).

## Themes

Three of the four surfaces paint **light only** — a `.dark` class and a dark colour-scheme emulation both leave them unchanged, so `light.*` is their painted theme and no dark marketing tokens exist. The **dark set holds only the dev.hume.ai docs' painted dark** (`html.dark` repainted by the header Theme menu — the warm near-black `#1c1917` ground), and `light.docs.*` records the same declarations under `html.light`. Light was restored after every dark pass; each sidecar records the painted classes.
