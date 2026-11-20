<p align="center">
  <img src="docs/assets/logo/logo-rounded.png" alt="design-systems logo" width="160">
</p>

<h1 align="center">
design-systems
</h1>

<p align="center">
  <strong>Measured tokens, components and screenshots from real products, so any project can say "make it look like Linear".</strong>
</p>

<p align="center">
  <a href="https://github.com/c-wenlong/designs/actions/workflows/check.yml"><img src="https://github.com/c-wenlong/designs/actions/workflows/check.yml/badge.svg" alt="Check"></a>
  <a href="https://github.com/c-wenlong/designs/actions/workflows/pages.yml"><img src="https://github.com/c-wenlong/designs/actions/workflows/pages.yml/badge.svg" alt="Pages"></a>
  <img src="https://img.shields.io/badge/tools-stdlib--only-brightgreen.svg" alt="stdlib only">
  <img src="https://img.shields.io/badge/repo-private-red.svg" alt="Private repo">
</p>

<p align="center">
  <a href="#setup">Setup</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#catalog">Catalog</a> ·
  <a href="#using-a-style">Using a style</a> ·
  <a href="#for-agents">For agents</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#development">Development</a>
</p>

---

**design-systems** is one library of design styles captured from real
products, so any project (and any coding agent working in it) can say "make
it look like Linear" and find measured tokens, components and screenshots in
one place instead of in whichever project first needed them.

It holds two stores of styles at two confidence levels:

- [systems/](systems): the packages, one per product (50 today), measured
  from real captures. Every value carries an evidence label saying where it
  came from. These are the only values to design from.
- [refero/](refero): a snapshot of [styles.refero.design](https://styles.refero.design)
  (1,342 styles): third-party interpreted data at lower confidence. Breadth
  for inspiration, never the source for a value a package holds.

Each package is self-contained: design tokens, a page that renders them, a
component inventory, screenshots of the real product, and the builders that
produced all of it, so a fix goes through the builders rather than a hand
edit. The library is read three ways: by a person through the gallery app
(`make dev`), by a script or agent through [catalog.json](catalog.json) and
the read-only MCP server, and by a terminal through the `ds` CLI. The repo
(`c-wenlong/designs`) stays private; [docs/RIGHTS.md](docs/RIGHTS.md) says
why.

```
$ python3 tools/catalog.py find dark chat

codex-desktop   4  Desktop coding-agent app (OpenAI's Codex for macOS, Electron): a 52px navigation rail beside a …
                  tags: desktop, electron, macos, coding, ai, agent, chat, sidebar, rail, dense, … | themes: light, dark | systems/codex-desktop/README.md
grokbot-desktop 4  Desktop chat app for AI agents in Electron: a near-black or white window with a darker sidebar of …
                  tags: desktop, electron, macos, coding, ai, agent, chat, sidebar, per-item-colour, … | themes: light, dark | systems/grokbot-desktop/README.md
opencode-desktop 4  Desktop coding agent in Electron: a near-black or white rounded panel under a title bar of session tabs, …
                  tags: desktop, electron, macos, coding, ai, agent, chat, tabs, dense, ramps, … | themes: light, dark | systems/opencode-desktop/README.md
```

## Why a library?

Without one, the same style gets re-measured in every project that wants it:

- Tokens get copied out of whichever repo needed the style first, drift
  included, and the copies never reconcile.
- Screenshots get read as measurements. Most shots here are 256-colour PNGs
  to keep the repo small; none of them is a measurement.
- A value with no provenance cannot be checked later, so nothing can be
  trusted twice.
- An agent asked to "make it look like Linear" guesses from memory instead
  of reading the product's own values.

This repo keeps every captured style in one standard package, keeps the
evidence next to the values, and puts the same front door on it for a
person (the gallery), a script ([catalog.json](catalog.json)) and a coding
agent (the MCP server and `ds`).

## Features

| Area | What you get |
| --- | --- |
| **Packages** | 50 products under [systems/](systems), all in one layout: `tokens.json` (W3C DTCG, Tokens Studio multi-set), a generated `DESIGN.md`, a `style-guide.html` rendering every token, `components.md`, `patterns.md`, screenshots, and the tools that rebuild it |
| **Evidence** | Every token says where it came from: a measured CSS read, a reconstruction, or a reviewer's call ([docs/EVIDENCE.md](docs/EVIDENCE.md)) |
| **Gallery** | One card per package with cover, icon, colour roles and fonts; per-package pages running Screenshots, Brief, Colors, Type, Spacing, Shape, Components, Icons, Health and Files (sections a package has nothing for are hidden); search over names, uses, tags and themes |
| **Refero** | 1,342 styles labelled by product type and design style, browsed beside the packages but never trusted over them |
| **Scorecard** | Every package graded against the rubric in [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md), in the wording for its platform (web, mobile or desktop), shown as a heatmap with the evidence behind each grade |
| **Agent layer** | Read-only MCP tools over stdio or hosted HTTP, a `ds` terminal client, a chat UI inside the app, and `handoff_prompt` for passing a chosen style to a coding agent |
| **Capture kit** | [tools/kit/](tools/kit): public-web, signed-in-web and native-iOS (iPhone Mirroring) capture pipelines plus the token and style-guide builders a new package starts from |
| **Freshness** | Brief, Health, `DESIGN.md` and the catalog table below are generated; `make check` fails on a stale one, so the docs cannot drift from the data |

## Setup

**Requirements:** Git LFS installed *before* cloning (every image, archive
and font is an LFS object), `python3`, and `uv` for `make setup`. The apps
need Node 22.13+ and pnpm 10. Capturing additionally needs Playwright, a
Chromium browser for the signed-in kit, and an iPhone on the same iCloud
account for the native kit; [docs/CAPTURE.md](docs/CAPTURE.md) has the
detail. Pillow, Markdown, numpy and Node-based linting are only needed by
the builders that ask for them (see `make setup`).

```bash
brew install git-lfs && git lfs install   # once per machine, before the clone
git clone git@github.com:c-wenlong/designs.git design-systems
cd design-systems
make setup                                # .venv with the site builder's and capture tools' deps
cp .env.example .env                      # fill in what you use; .env is gitignored
```

`.env` values and what uses them:

| Variable | Used by |
| --- | --- |
| `STATICRYPT_PASSWORD` | The Pages workflow, encrypting every page of the built docs site |
| `ANTHROPIC_API_KEY` | `tools/refero/classify.py`; the gallery chat's fallback provider (stays server-side) |
| `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET` | `tools/refero/upload_r2.py`, the media mirror upload |
| `DS_CHAT_MODEL` | Optional: the model the gallery chat calls when the browser has none saved |
| `DESIGN_SYSTEMS_REPO` | Optional: this checkout's path, when the app cannot find it by itself |
| `DESIGN_SYSTEMS_MEDIA`, `DESIGN_SYSTEMS_MEDIA_BASE` | Optional: where mirrored refero media lives, and the base URL for catalog media absent from the local mirror |

## Quick start

```bash
make dev                     # build web/data/, serve the app on 127.0.0.1:8800, open the gallery and scorecard
make dev PORT=9000           # another port; scripts/dev.sh --no-open skips the browser
make help                    # every target

pnpm --dir app install --frozen-lockfile && pnpm --dir app dev   # the newer research app on :8845

python3 tools/catalog.py find dark dense                 # rank packages by free text
python3 tools/catalog.py export linear                   # every token as CSS custom properties
python3 tools/catalog.py export linear --format json     # or JSON, aliases resolved
python3 tools/catalog.py contrast systems/linear/tokens.json --theme light FG:BG...
python3 tools/catalog.py scan systems/linear --redact ~/.design-systems/cleanup-redact.json
python3 tools/fetch_icon.py linear                       # refresh a package's app icon from its site

make check                   # the freshness gate: catalog, refero stores, Brief, DESIGN.md, scorecard, Health
make grade                   # re-grade scripted criteria, rewrite every Health + the catalog table below
make brief                   # regenerate every package README's Brief
make design-md               # regenerate every package's DESIGN.md (runs make brief first)
make docs                    # build docs/ into the static site/
make test                    # tools' unit tests + every package's own tools/test_*.py
make clean                   # remove generated output

python3 server/mcp.py        # stdio MCP server: the library as tools for a coding agent
ds find "dense sidebar"      # the ds CLI against a hosted /api/mcp (see For agents)
ds export linear -g light    # one token group; also ds doc, ds media, ds handoff, ds status
```

## Browse it

Everything is browsed through the Next.js app under [web/](web): the gallery,
the scorecard and the library docs under `docs/`.

```bash
make dev
```

`make dev` (or [scripts/dev.sh](scripts/dev.sh)) builds the app's data,
installs its `pnpm` dependencies on the first run, serves it at
http://127.0.0.1:8800/ and opens the gallery and the scorecard in the browser.
If the app is already running it only opens the tabs; `--port N` picks
another port and `--no-open` skips the browser. The app has three parts:

- **Gallery**: one card per package with a cover screenshot, its product icon,
  its colour roles and fonts. Each package's page at `/gallery/<slug>` reads
  in the same order, from a rail on the left: Screenshots, Brief, Colors,
  Type, Spacing, Shape (radii and shadows), Components, Icons, Health and
  Files (every Markdown file, rendered). A section the package has nothing
  for is left out of the page and the rail. Each section is an anchor, so
  `/gallery/<slug>#colors` links straight to it. Search on the gallery
  index matches names, uses, tags and themes; press `/` to focus it.
- **Scorecard**: every package graded against the checklist in
  [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md), in the wording for its
  platform (web, mobile or desktop), as a heatmap with the evidence
  behind each grade. The app reads [scorecard/](scorecard) live on each
  request; [tools/scorecard.py](tools/scorecard.py) only writes the
  published site's copy under `docs/scorecard/`.
- **Docs**: the files under [docs/](docs), rendered.

The library docs, without the gallery, are also published to GitHub Pages at
https://c-wenlong.github.io/designs/ by [tools/site.py](tools/site.py),
with every page encrypted by
StatiCrypt, so it needs the password in the `STATICRYPT_PASSWORD` repository
secret. `make help` lists the other targets (`make check` validates
[catalog.json](catalog.json) against the packages).

## Catalog

Ranked by the scorecard. Health counts the criteria in
[docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md) each package meets, leaving out
the ones a capture cannot meet; layout gaps are the standard parts from
[docs/PACKAGE.md](docs/PACKAGE.md) it lacks. Each package's README opens with a
Brief to read before designing in its style, then a Health section that lists
what is open, with the evidence.

<!-- catalog:start. Generated by tools/health.py from the newest scorecard snapshot; `make grade` rewrites it. Do not edit. -->

| Icon | Package | Good for | Captured | Themes | Health | Layout gaps |
|---|---|---|---|---|---|---|
| <img src="systems/claude/icon.png" width="20" alt="claude"> | [claude](systems/claude/README.md) | A quiet chat shell with a serif model voice: composer, thread, Artifacts, Projects, settings (cds tokens) | 2026-10-17 | light, dark | 22 of 25 met, 3 partly, 0 missing | none |
| <img src="systems/brilliant/icon.png" width="20" alt="brilliant"> | [brilliant](systems/brilliant/README.md) | Interactive problem-solving lessons, course paths, a calm editorial learning UI (Panda CSS tokens) | 2026-10-17 | light, dark | 20 of 25 met, 5 partly, 0 missing | none |
| <img src="systems/polaris/icon.png" width="20" alt="polaris"> | [polaris](systems/polaris/README.md) | Admin and commerce UI built from a published component library: semantic colour roles, buttons, cards, banners | 2026-10-17 | light, light-mobile, light-high-contrast-experimental, dark-experimental | 19 of 25 met, 6 partly, 0 missing | none |
| <img src="systems/superset-desktop/icon.png" width="20" alt="superset-desktop"> | [superset-desktop](systems/superset-desktop/README.md) | Desktop app for running coding agents in parallel workspaces, in Electron: a warm near-black or near-white window with a slightly darker sidebar of projects and workspaces, one rounded composer with small chips, ink primary buttons instead of a brand hue, shadcn/ui components on Tailwind's scale (8px controls, 10px popovers, a 3px focus ring), foreground-wash hover and selection, and each agent's CLI in a terminal pane inside a tabbed workspace | 2026-10-25 | light, dark | 19 of 25 met, 6 partly, 0 missing | `icons/` |
| <img src="systems/airtable/icon.png" width="20" alt="airtable"> | [airtable](systems/airtable/README.md) | SaaS marketing: Haas grotesque on white, a 13-hue brand accent system painting 32px-radius pastel tiles, dark ink pill CTAs, a slide-in nav drawer, a plan grid and a lead form | 2026-11-10 | light | 18 of 25 met, 7 partly, 0 missing | none |
| <img src="systems/base44/icon.png" width="20" alt="base44"> | [base44](systems/base44/README.md) | AI-app-builder marketing: warm paper ground with Dazzed display type, near-black 38px CTA pills, an orange #ff773c action accent, a hero prompt composer, and a full named token system (shadcn channels + named palette + scales) in the bundle | 2026-11-11 | light, dark (declared) | 18 of 25 met, 7 partly, 0 missing | `icons/` |
| <img src="systems/chatgpt/icon.png" width="20" alt="chatgpt"> | [chatgpt](systems/chatgpt/README.md) | The baseline chat UI: thread, composer, sidebar history, menus, dialogs, search, settings pages | 2026-10-17 | light, dark | 18 of 25 met, 7 partly, 0 missing | none |
| <img src="systems/notebooklm/icon.png" width="20" alt="notebooklm"> | [notebooklm](systems/notebooklm/README.md) | Source-grounded AI workspace: sources panel, chat, studio outputs; near-monochrome surfaces with pill buttons (luminous UI) | 2026-10-17 | light, dark | 18 of 25 met, 7 partly, 0 missing | none |
| <img src="systems/tokentracker/icon.png" width="20" alt="tokentracker"> | [tokentracker](systems/tokentracker/README.md) | Local AI usage dashboard: borderless sidebar, rounded content panel, hairline cards, one green accent for money, dense tables, limits bars | 2026-10-17 | light, dark | 18 of 25 met, 7 partly, 0 missing | none |
| <img src="systems/gauth/icon.png" width="20" alt="gauth"> | [gauth](systems/gauth/README.md) | AI tutor learning app: course catalogue, unit pages, lesson players with an Ask Tutor panel | 2026-10-17 | light | 18 of 24 met, 6 partly, 0 missing | none |
| <img src="systems/capy-desktop/icon.png" width="20" alt="capy-desktop"> | [capy-desktop](systems/capy-desktop/README.md) | Desktop app for cloud coding agents in Electron, the capy.ai web app in a desktop frame: an off-white or near-black window with a rounded content panel set into it, browser-like tabs in the title bar, a sidebar of threads by project, one composer with project, Run on and model pickers, 0.5px hairlines and Inter at 13px, muted text mixed from one ink, teal only for starting work and on-states, red only for deletion | 2026-10-25 | light, dark | 17 of 26 met, 9 partly, 0 missing | `icons/` |
| <img src="systems/airbnb/icon.png" width="20" alt="airbnb"> | [airbnb](systems/airbnb/README.md) | Public travel marketplace: the capsule Where/When/Who search bar, photo-led listing cards with the stroked wishlist heart, hairline-separated surfaces, one Rausch pink for end-of-flow actions, and a full set of declared-but-unapplied dark values | 2026-11-09 | light, dark | 17 of 25 met, 8 partly, 0 missing | `icons/` |
| <img src="systems/coursera/icon.png" width="20" alt="coursera"> | [coursera](systems/coursera/README.md) | Course catalogue, course and module pages, course cards, a mature enterprise design system (386 --cds-* variables) | 2026-10-17 | light, dark | 17 of 25 met, 8 partly, 0 missing | none |
| <img src="systems/manus/icon.png" width="20" alt="manus"> | [manus](systems/manus/README.md) | Agent app shell: multi-section sidebar, a Library of agent outputs by type and by day, task threads with deliverables | 2026-10-17 | light, dark | 17 of 25 met, 8 partly, 0 missing | none |
| <img src="systems/notion-calendar-desktop/icon.png" width="20" alt="notion-calendar-desktop"> | [notion-calendar-desktop](systems/notion-calendar-desktop/README.md) | Desktop calendar app (Notion Calendar for macOS, Electron around the calendar.notion.so web app): a 240px wash sidebar with a mini month, scheduling and per-account calendar lists beside a week grid of 48px hours with two time-zone columns, event chips in each calendar's colour with a left ribbon, a translucent 284px event popover and a centred command menu, hairline edges drawn as 1px inset shadows, 13px medium labels on 30px controls with 6px corners, one blue for primary actions, switches and focus, red only for today, and menus and tooltips that stay dark in both themes | 2026-10-25 | light, dark | 17 of 25 met, 8 partly, 0 missing | `icons/` |
| <img src="systems/researchrabbit/icon.png" width="20" alt="researchrabbit"> | [researchrabbit](systems/researchrabbit/README.md) | Interactive citation graph beside a list: node and edge styling, canvas interaction (see graph.md) | 2026-10-17 | light | 17 of 24 met, 7 partly, 0 missing | none |
| <img src="systems/anthropic/icon.png" width="20" alt="anthropic"> | [anthropic](systems/anthropic/README.md) | AI-product marketing pages, pricing pages, sales forms and developer docs; ivory editorial surfaces with serif headlines, pill nav chrome and a restrained clay accent | 2026-11-09 | light, dark | 17 of 25 met, 6 partly, 2 missing | none |
| <img src="systems/devin-desktop/icon.png" width="20" alt="devin-desktop"> | [devin-desktop](systems/devin-desktop/README.md) | Desktop coding-agent app in Electron on a VS Code workbench: a near-black or near-white page shared by the sidebar and the content, two-line session rows, one 20px-radius raised composer with a Cloud / Local segmented control, a right-aligned tinted prompt bubble over plain replies and muted work rows, every neutral one colour at fixed alphas, ink-filled page buttons with blue kept for focus and links, 6px controls and 10px popups and cards | 2026-10-25 | light, dark | 16 of 25 met, 9 partly, 0 missing | `icons/` |
| <img src="systems/refero-design/icon.png" width="20" alt="refero-design"> | [refero-design](systems/refero-design/README.md) | Design research app plus a public design-system gallery: research box, rotating screenshot galleries, video-preview style cards, per-style DESIGN.md documentation pages | 2026-11-02 | light, dark | 16 of 25 met, 9 partly, 0 missing | none |
| <img src="systems/aboard/icon.png" width="20" alt="aboard"> | [aboard](systems/aboard/README.md) | AI consultancy marketing: warm editorial Tobias serif on a cream ground, Work Sans UI, pill-everything controls, one loud bright-citrus accent, frosted floating nav, dark content bands inside a single light theme | 2026-11-09 | light | 16 of 25 met, 6 partly, 3 missing | none |
| <img src="systems/codex-desktop/icon.png" width="20" alt="codex-desktop"> | [codex-desktop](systems/codex-desktop/README.md) | Desktop coding-agent app (OpenAI's Codex for macOS, Electron): a 52px navigation rail beside a sidebar of projects and chats on a slightly darker surface, a centred new-chat heading over one raised 22px-radius composer with pill chips, a right-aligned soft prompt bubble over plain replies and folded Worked for rows, menus and cards at 15 to 25px squircle radii, every neutral built from one ink colour at fixed alphas over four theme seeds (surface, ink, accent, contrast), an ink pill for the primary action and the accent kept for switches, focus and links | 2026-10-25 | light, dark | 15 of 25 met, 10 partly, 0 missing | `icons/` |
| <img src="systems/cursor-desktop/icon.png" width="20" alt="cursor-desktop"> | [cursor-desktop](systems/cursor-desktop/README.md) | Desktop coding-agent app in Electron: a near-black or off-white window with a quiet sidebar of agents and projects, one raised composer, plain-text agent replies under a raised prompt bubble, translucent alpha tiers of one base colour for every text, fill and edge, an accent-blue primary button with ink-filled pill buttons beside it, 8px-radius rows and 12px raised menus and dialogs | 2026-10-25 | light, dark | 15 of 25 met, 10 partly, 0 missing | `icons/` |
| <img src="systems/grokbot-desktop/icon.png" width="20" alt="grokbot-desktop"> | [grokbot-desktop](systems/grokbot-desktop/README.md) | Desktop chat app for AI agents in Electron: a near-black or white window with a darker sidebar of coloured agent characters (a pinned grid over groups), one conversation per agent with the owner's bubbles in that agent's colour and neutral raised reply bubbles, a shimmering activity line while it works, pill and circle controls, an ink primary button, surfaces separated by fill rather than borders | 2026-10-25 | light, dark | 15 of 25 met, 10 partly, 0 missing | `icons/` |
| <img src="systems/luma-ios/icon.png" width="20" alt="luma-ios"> | [luma-ios](systems/luma-ios/README.md) | Native iOS events and community apps: full-bleed event lists on pure black or white with square cover thumbnails and faint status pills, grouped settings cards, a floating iOS 26 glass tab bar and round glass nav buttons, one purple accent, ink primary buttons, and event pages tinted from their cover | 2026-10-24 | light, dark | 15 of 25 met, 9 partly, 1 missing | `icons/` |
| <img src="systems/raycast-desktop/icon.png" width="20" alt="raycast-desktop"> | [raycast-desktop](systems/raycast-desktop/README.md) | Keyboard-first launcher and command palette for macOS: one floating 750 x 475 pt window with a borderless 64 pt search field, 38 pt result rows inset 8 pt, a footer action bar naming the primary action and Command-K for the rest; Raycast Dark and Raycast Light as declared in the app's own shipped stylesheet and theme definitions, where every fill is the foreground or selection colour at 5, 10, 20, 40 or 60% over a translucent grey window, checked against the window's pixels; a 13/11 Inter type scale, 46 pt settings rows on 2.5% cards, pill buttons and macOS switches in the theme's blue | 2026-10-25 | light, dark | 14 of 25 met, 11 partly, 0 missing | `icons/` |
| <img src="systems/allbirds/icon.png" width="20" alt="allbirds"> | [allbirds](systems/allbirds/README.md) | Sustainable-footwear retail: storefront chrome, collection grid with filter sheet, product page with size grid, cart drawer | 2026-11-08 | light | 14 of 25 met, 10 partly, 1 missing | `icons/` |
| <img src="systems/duolingo/icon.png" width="20" alt="duolingo"> | [duolingo](systems/duolingo/README.md) | Gamified learning: lesson flow, streaks, leaderboards, chunky 3D buttons, a mascot-led brand | 2026-10-17 | light, dark | 14 of 24 met, 10 partly, 0 missing | none |
| <img src="systems/anam/icon.png" width="20" alt="anam"> | [anam](systems/anam/README.md) | Real-time AI avatar marketing and docs: live video persona cards, frosted-glass controls over video, a single orange accent on black and white, and a Mintlify docs surface with a dark theme | 2026-11-09 | light, dark | 14 of 25 met, 9 partly, 2 missing | none |
| <img src="systems/acnestudios/icon.png" width="20" alt="acnestudios"> | [acnestudios](systems/acnestudios/README.md) | Fashion storefront: near-pure monochrome with one electric-blue accent, 12px Helvetica caps labels, hairline rules, 60px rails, 360px side drawers, mono price numerals | 2026-11-09 | light | 14 of 24 met, 8 partly, 2 missing | `icons/` |
| <img src="systems/opencode-desktop/icon.png" width="20" alt="opencode-desktop"> | [opencode-desktop](systems/opencode-desktop/README.md) | Desktop coding agent in Electron: a near-black or white rounded panel under a title bar of session tabs, no sidebar (Home lists projects and sessions), a single transcript column with the prompt as a faint blue bubble and the reply on the page, tool calls folded into one muted line, a raised composer with an ink Send button, Inter at 440 and IBM Plex Mono, grey and hue ramps behind every role | 2026-10-25 | light, dark | 13 of 25 met, 12 partly, 0 missing | `icons/` |
| <img src="systems/orca-desktop/icon.png" width="20" alt="orca-desktop"> | [orca-desktop](systems/orca-desktop/README.md) | Desktop coding-agent harness in Electron on shadcn/ui: white or near-black panes beside a grey sidebar of projects and worktree cards, a tab strip of terminals and agent chats, an inspector on the right and a usage status bar, ink (not a hue) for the primary button and switches, shadcn's 3px focus ring everywhere, 8px controls and 14px bordered cards in Geist, red only for removal | 2026-10-25 | light, dark | 13 of 25 met, 12 partly, 0 missing | `icons/` |
| <img src="systems/acctual/icon.png" width="20" alt="acctual"> | [acctual](systems/acctual/README.md) | Fintech marketing: a #fafafa ground, ink text at 70/60% for links, one #0098f2 accent on pills and check bullets, #0d111b capsule buttons on a 1px inner ring, a frosted 80px nav pill, Open Runde type, and dark Selecta panels on landing pages | 2026-11-10 | light | 13 of 25 met, 9 partly, 3 missing | none |
| <img src="systems/amie/icon.png" width="20" alt="amie"> | [amie](systems/amie/README.md) | AI-product marketing: cream-ground productivity surface with a blue action CTA, rounded-xl buttons, floating nav bar, segmented billing toggle, Radix FAQ accordions, and the app's own layout metrics in the bundle | 2026-11-11 | light | 13 of 25 met, 9 partly, 3 missing | `icons/` |
| <img src="systems/ableton/icon.png" width="20" alt="ableton"> | [ableton](systems/ableton/README.md) | Music software marketing: restrained black Futura on white, one signature #0000ff blue, zero border radius, full-bleed teaser cells, a black consent card and resting login/register forms | 2026-11-08 | light | 13 of 25 met, 8 partly, 4 missing | none |
| <img src="systems/asana/icon.png" width="20" alt="asana"> | [asana](systems/asana/README.md) | SaaS marketing + product surfaces: near-white page, near-black #0d0d0d ink, TWK Lausanne webfont, 3px control radii, near-black primary CTAs lifting to #3d3d3d, #f3f3f3 panels with #cfcfcf hairlines, and a full shipped token layer ; colour ramps, --lightmode-*/--darkmode-* roles, 16px spacing base, --media-* breakpoints, 12-col grid, --shadow-* and --transition-* scales | 2026-11-11 | light, dark | 12 of 25 met, 13 partly, 0 missing | `icons/` |
| <img src="systems/conductor-desktop/icon.png" width="20" alt="conductor-desktop"> | [conductor-desktop](systems/conductor-desktop/README.md) | Desktop coding-agent app in Tauri on Tailwind and Base UI: a warm stone palette (a brown-grey ramp, not neutral grey), a 256px sidebar of repositories and workspaces, chat tabs over a conversation whose prompt sits on a rose tint, a right panel of files, changes and run scripts, ink (not a hue) for primary buttons and switches, tan for links, the special accent and input focus, 6px controls and 12px dialogs in Geist and Geist Mono | 2026-10-25 | light, dark | 12 of 25 met, 13 partly, 0 missing | `icons/` |
| <img src="systems/grokbot/icon.png" width="20" alt="grokbot"> | [grokbot](systems/grokbot/README.md) | Native iOS agent chat: near-black or near-white page, grouped grey cards, iOS 26 glass controls over content, one colour per bot tinting its avatar, switches and the owner's bubbles, ink-coloured primary buttons | 2026-10-23 | light, dark | 12 of 25 met, 12 partly, 1 missing | `icons/` |
| <img src="systems/spotify/icon.png" width="20" alt="spotify"> | [spotify](systems/spotify/README.md) | Native iOS media app: near-black page where artwork carries the colour, dark grey tiles and cards, an artwork-tinted mini player over the tab bar, Spotify green only for what is selected or playable, white and outlined pill buttons, glass chips and bottom sheets | 2026-10-23 | dark | 12 of 25 met, 12 partly, 1 missing | `icons/` |
| <img src="systems/substack/icon.png" width="20" alt="substack"> | [substack](systems/substack/README.md) | Native iOS reading and newsletter app: near-black or white page, floating glass tab bar, one orange for the app's own actions, system blue for controls, a publication's colour on its Subscribe buttons, serif post bodies | 2026-10-24 | light, dark | 12 of 25 met, 12 partly, 1 missing | `icons/` |
| <img src="systems/acuityscheduling/icon.png" width="20" alt="acuityscheduling"> | [acuityscheduling](systems/acuityscheduling/README.md) | Booking-software marketing pages: pastel hero gradients, Clarkson Serif headlines in navy #283849, 12px-radius ink buttons, cream and lavender cards, a Squarespace account gate with square black-ruled OAuth rows | 2026-11-10 | light | 12 of 25 met, 11 partly, 2 missing | `icons/` |
| <img src="systems/appwrite/icon.png" width="20" alt="appwrite"> | [appwrite](systems/appwrite/README.md) | Developer-platform marketing: pinned-dark SvelteKit + Tailwind v4 site, brand-pink CTAs and gradient hero text, hairline-bordered cards, docs chrome with sidebar and code blocks, public sign-in form | 2026-11-10 | dark, light | 12 of 25 met, 10 partly, 3 missing | `icons/` |
| <img src="systems/linear/icon.png" width="20" alt="linear"> | [linear](systems/linear/README.md) | Dense, keyboard-first product UI in dark and light: issue boards, issue detail, menus, settings tables; plus the public marketing site | 2026-10-17 | dark, light | 12 of 25 met, 10 partly, 3 missing | `patterns.md` |
| <img src="systems/apollographql/icon.png" width="20" alt="apollographql"> | [apollographql](systems/apollographql/README.md) | Dev-tool marketing in a space theme: near-black hero fields and deep navy bands, a conic-ring primary CTA, burnt-orange pill buttons, offwhite segment toggles, 32px cards and Aeonik display type over Inter | 2026-11-10 | light, dark | 12 of 25 met, 8 partly, 5 missing | none |
| <img src="systems/aloyoga/icon.png" width="20" alt="aloyoga"> | [aloyoga](systems/aloyoga/README.md) | Fashion e-commerce storefront: monochrome black-on-white Shopify + Builder.io surface, uppercase small-cap chrome, square PDP colour tiles and grid colour dots, member-price hooks, a full --color-* ramp set behind an achromatic surface | 2026-11-11 | light | 11 of 25 met, 14 partly, 0 missing | `icons/` |
| <img src="systems/claude-ios/icon.png" width="20" alt="claude-ios"> | [claude-ios](systems/claude-ios/README.md) | Native iOS AI chat: serif replies on the page with no bubble, a grey user bubble, a slide-over sidebar instead of a tab bar, iOS 26 glass controls, bottom sheets of grouped cards, one inverse pill for the main action, blue for interactive state and orange only for the brand and send | 2026-10-24 | light, dark | 11 of 25 met, 13 partly, 1 missing | `icons/` |
| <img src="systems/cursor-ios/icon.png" width="20" alt="cursor-ios"> | [cursor-ios](systems/cursor-ios/README.md) | Native iOS coding-agent client: near-black or off-white page, plain-text agent replies with no bubbles, two-line agent rows with status dots and red-green diffstats, a 2x2 grid of rounded Inbox tiles with coloured icons, iOS 26 glass circles and a glass composer over the content, grey-on-grey sheets, one blue accent and an orange chart colour | 2026-10-24 | light, dark | 11 of 25 met, 13 partly, 1 missing | `icons/` |
| <img src="systems/gemini/icon.png" width="20" alt="gemini"> | [gemini](systems/gemini/README.md) | Native iOS AI assistant: a near-empty black or off-white page with a glow behind a floating glass composer, glass circles for navigation, the owner's messages in bubbles and replies as plain text, rimless grouped settings cards, Material primary blue for filled actions | 2026-10-24 | light, dark | 11 of 25 met, 13 partly, 1 missing | `icons/` |
| <img src="systems/github-ios/icon.png" width="20" alt="github-ios"> | [github-ios](systems/github-ios/README.md) | Native iOS developer tools: grouped cards on a near-black or pale grey page, full-bleed lists on the card colour, a floating iOS 26 glass tab bar, grey neutral buttons, coloured icon tiles per object type, filled state badges, monospace diffs with line and syntax colours | 2026-10-24 | light, dark | 11 of 25 met, 13 partly, 1 missing | `icons/` |
| <img src="systems/grab/icon.png" width="20" alt="grab"> | [grab](systems/grab/README.md) | Native iOS service app: white pages under a coloured service header, Grab green for every primary action, pale mint secondary controls, dark-teal selected chips, capsule buttons, a tab bar with a raised scan button, bottom sheets over a scrim | 2026-10-23 | light | 11 of 25 met, 13 partly, 1 missing | `icons/` |
| <img src="systems/notion-ios/icon.png" width="20" alt="notion-ios"> | [notion-ios](systems/notion-ios/README.md) | Native iOS docs and workspace app: a warm navigation grey and a content canvas, top tabs instead of a tab bar, iOS 26 glass floating at the bottom, plain text rows with grouped cards only in sheets, one blue accent, an AI chat that bubbles only the user | 2026-10-24 | light, dark | 11 of 25 met, 13 partly, 1 missing | `icons/` |
| <img src="systems/1password/icon.png" width="20" alt="1password"> | [1password](systems/1password/README.md) | Password/security product marketing: announcement strip + white nav chrome, navy gradient hero, segment-selector plan pill, pricing columns, FAQ accordions | 2026-11-08 | light | 11 of 25 met, 12 partly, 2 missing | `icons/` |
| <img src="systems/aboardhr/icon.png" width="20" alt="aboardhr"> | [aboardhr](systems/aboardhr/README.md) | HR product marketing: flat #fafafa ground, OS-ui stack semibold display type, pastel card tints (blue, mint, pink, lavender) with no borders or shadows, full-pill CTAs in a single bright blue | 2026-11-10 | light | 11 of 25 met, 11 partly, 3 missing | none |
| <img src="systems/chatgpt-ios/icon.png" width="20" alt="chatgpt-ios"> | [chatgpt-ios](systems/chatgpt-ios/README.md) | Native iOS assistant chat: black or near-white page, replies as plain text with only the owner's messages in an accent-tinted bubble, a two-row glass composer, a sidebar instead of a tab bar, iOS grouped settings, one user-chosen accent on send and primary pills | 2026-10-24 | light, dark | 10 of 25 met, 14 partly, 1 missing | `icons/` |
| <img src="systems/telegram/icon.png" width="20" alt="telegram"> | [telegram](systems/telegram/README.md) | Native iOS messaging: black or white chat list with a grey pinned band, grouped settings cards led by gradient icon tiles, iOS 26 glass nav buttons, folder chips and a floating tab bar, one blue accent, violet-to-blue (dark) or pale green (light) outgoing bubbles over a wallpaper | 2026-10-23 | light, dark | 10 of 25 met, 14 partly, 1 missing | `icons/` |
| <img src="systems/aesop/icon.png" width="20" alt="aesop"> | [aesop](systems/aesop/README.md) | Skincare storefront: one warm ink on a cream ground, a single tannin-amber accent, Suisse Intl sentence-case, 1px keylines (many drawn as box-shadows), 40px fields, 48px bars, 400px side rails | 2026-11-10 | light | 10 of 25 met, 13 partly, 2 missing | `icons/` |
| <img src="systems/youtube/icon.png" width="20" alt="youtube"> | [youtube](systems/youtube/README.md) | Native iOS video feed: near-black or white page, one neutral grey for chips and fields, rounded-rectangle filter chips that invert when selected, ink-coloured capsule buttons, edge-to-edge 16:9 thumbnails with a translucent duration badge, a five-item tab bar with a round Create button, YouTube red kept for progress and badges | 2026-10-24 | light, dark | 10 of 25 met, 13 partly, 2 missing | `icons/` |
| <img src="systems/zed-desktop/icon.png" width="20" alt="zed-desktop"> | [zed-desktop](systems/zed-desktop/README.md) | Native code editor drawn with Metal (GPUI) with an agent panel: Zed's own One Dark and One Light theme keys as declared in its open-source theme file, checked against the window's pixels; a grey title and status bar around a darker panel tier and the darkest editor, one blue accent for links, the cursor and active icons, ghost buttons that change fill on hover, 4/6/8 pt radii, 26 pt tree rows, 28 pt controls, a 610 pt command palette, IBM Plex Sans (Zed's .ZedSans) for the UI and the owner's Menlo 11 for code | 2026-10-25 | light, dark | 10 of 25 met, 13 partly, 2 missing | `icons/` |
| <img src="systems/arket/icon.png" width="20" alt="arket"> | [arket](systems/arket/README.md) | premium-minimal commerce: a white page with warm #faf8f3 beige bands, everything in the arketSansMono grotesque, 2px outlined controls that invert to black on hover, black 56px CTAs, a 538px drawer for menu/cart/filter/location | 2026-11-11 | light | 9 of 24 met, 14 partly, 1 missing | `icons/` |
| <img src="systems/asos/icon.png" width="20" alt="asos"> | [asos](systems/asos/README.md) | Fashion e-commerce storefront: flat black-on-white chrome, square zero-radius controls, one buy-green action colour, Futura tracked-uppercase labels, hash-named CSS design tokens, mega-menu and mobile side-panel navigation | 2026-11-10 | light | 9 of 25 met, 13 partly, 3 missing | `icons/` |
| <img src="systems/arcade/icon.png" width="20" alt="arcade"> | [arcade](systems/arcade/README.md) | AI-product marketing: black-on-white Webflow surface, Inter Display hero over a prompt composer with suggestion chips, black 12px pill CTAs, #f4f4f4 24px plan cards, pastel card washes and a #2142e7 blue kept for the demo pages | 2026-11-10 | light | 9 of 25 met, 12 partly, 4 missing | `icons/` |
| <img src="systems/notion-desktop/icon.png" width="20" alt="notion-desktop"> | [notion-desktop](systems/notion-desktop/README.md) | Desktop docs, notes and database workspace (Notion for macOS, Electron): a tab strip above a 270px sidebar on a warm secondary grey, a centred 720px page column of blocks (a 40px bold title, three heading levels, 16px body at a 24px line, callouts and code on soft fills), database tables with thin rules and coloured select pills, raised 10px-radius menus with a 1px ring and a soft shadow, ghost buttons everywhere but one blue accent for New, checked boxes and switches, and a docked AI side panel | 2026-10-25 | light, dark | 8 of 25 met, 17 partly, 0 missing | `icons/` |
| <img src="systems/arcsearch/icon.png" width="20" alt="arcsearch"> | [arcsearch](systems/arcsearch/README.md) | Native iOS browser and search chrome: the page edge to edge with no address bar, iOS 26 glass toolbar, launcher and page menu at the bottom of the screen, a launcher whose search field sits low with pinned rows under it, Settings as a sheet of inset groups with coloured icon tiles and one neutral grey for every control, a blue-violet accent kept for one confirm button, ticks and the caret, destructive actions as red text in glass menus | 2026-10-24 | light, dark | 8 of 25 met, 16 partly, 1 missing | `icons/` |
| <img src="systems/ballpark/icon.png" width="20" alt="ballpark"> | [ballpark](systems/ballpark/README.md) | Product-research marketing: white-ground editorial SaaS surface with Inter Display headlines, one near-black 36px pill CTA recipe, hairline ghost buttons, a coral flame ramp reserved for the NEW chip, and the full Tailwind palette under Framer's --token-* vars | 2026-11-11 | light | 8 of 25 met, 15 partly, 2 missing | `icons/` |
| <img src="systems/adidas/icon.png" width="20" alt="adidas"> | [adidas](systems/adidas/README.md) | Sportswear storefront in strict monochrome: black on white, grey steps, bold 14/20 button labels, Adihaus DIN, square corners, 48px controls | 2026-11-10 | light | 8 of 25 met, 13 partly, 4 missing | `icons/` |
| <img src="systems/aaply/icon.png" width="20" alt="aaply"> | [aaply](systems/aaply/README.md) | Playful product-marketing pages: floating pill nav, Poppins display with inline emoji atoms, lime/black CTA pairs, chat-annotation bubbles, pricing rail with lime plan card, black footer band | 2026-11-08 | light | 8 of 24 met, 12 partly, 4 missing | `icons/` |
| <img src="systems/untitled-stream/icon.png" width="20" alt="untitled-stream"> | [untitled-stream](systems/untitled-stream/README.md) | Music-collaboration product marketing: bracketed chrome, black-gradient pill CTAs, iridescent disc artwork, frosted bottom pill bar, pricing rail with plan cards | 2026-11-08 | light, dark | 8 of 25 met, 11 partly, 6 missing | `icons/` |
| <img src="systems/boords/icon.png" width="20" alt="boords"> | [boords](systems/boords/README.md) | Pre-production tooling marketing: a floating white pill header, ink #121212 on white, a #f3f3e9 cream card field, an amber #e8aa42 CTA border, 9999px buttons, 24px cards and the single matter face from 64px display to 10px legal | 2026-11-11 | light | 7 of 25 met, 17 partly, 1 missing | `icons/` |
| <img src="systems/bezi/icon.png" width="20" alt="bezi"> | [bezi](systems/bezi/README.md) | AI game-dev tooling marketing: a #0d0d0d starfield ground, a floating translucent 144px-radius pill header, one #f84503 orange CTA recipe, corner-tick index chips, pastel accents and the Framer --token-* palette | 2026-11-11 | dark | 7 of 25 met, 16 partly, 2 missing | `icons/` |
| <img src="systems/bloomberg/icon.png" width="20" alt="bloomberg"> | [bloomberg](systems/bloomberg/README.md) | Financial news surface: an all-black chrome stack (utility strip, logo bar, section nav), a live ticker of #1c1c1c pills, BWHaasGrotesk headlines on a hairline story grid, the #3523ff CTA blue on offer pages, and honest paywall furniture measured at rest | 2026-11-10 | light | 7 of 25 met, 16 partly, 2 missing | `icons/` |
| <img src="systems/hevy/icon.png" width="20" alt="hevy"> | [hevy](systems/hevy/README.md) | Native iOS workout logging: dense set table, one blue accent, pale grey fills, small corners, iOS 26 glass chrome, rest timer | 2026-10-10 | light, dark | 7 of 25 met, 16 partly, 2 missing | `patterns.md`, `components/`, `icons/` |
| <img src="systems/biosites/icon.png" width="20" alt="biosites"> | [biosites](systems/biosites/README.md) | Link-in-bio marketing: monochrome Clarkson surface on a black hero collage, 40px-radius nav pills and an 80px black CTA pill that inverts to white on hover, slate persona cards in a moving carousel, giant 70px marquee links, and a 50px-radius claim field on the signed-out editor | 2026-11-11 | light | 7 of 25 met, 15 partly, 3 missing | `icons/` |
| <img src="systems/metabase/icon.png" width="20" alt="metabase"> | [metabase](systems/metabase/README.md) | Visual query notebooks, searchable field filters, chart inspectors, analytics dashboards and drill-through tables. Official interactive Edumation demo with custom purple light branding; not the default Metabase theme. Expanded interaction evidence includes selected Dark screens; exported tokens remain Light-only. | 2026-10-31 | light | 7 of 25 met, 14 partly, 4 missing | `icons/` |
| <img src="systems/artboardstudio/icon.png" width="20" alt="artboardstudio"> | [artboardstudio](systems/artboardstudio/README.md) | design-tool marketing + library surfaces: white page, near-black olive ink #0d1400, Vend Sans display lines, 42px near-black buttons, 8px control radii / 12px cards, pill tab bars, an inner-scrolled mockup grid, #aaff00 brand green kept for highlights | 2026-11-11 | light | 7 of 24 met, 13 partly, 4 missing | `icons/` |
| <img src="systems/clerk/icon.png" width="20" alt="clerk"> | [clerk](systems/clerk/README.md) | Developer administration: settings screens, authentication forms, searchable tables, compact menus and confirmation dialogs | 2026-10-30 | dark, light | 6 of 25 met, 19 partly, 0 missing | `icons/` |
| <img src="systems/busuu/icon.png" width="20" alt="busuu"> | [busuu](systems/busuu/README.md) | Language-learning marketing and signup flow: a purple #6e00f8-to-#116eee gradient hero under a simplified header, one green #11ee92 Learn-for-free pill, the #116eee action blue riding on text and 1px borders, 16px flag cards, an indigo #221658 paywall surface with #5438dc pill CTAs, and two served faces (Nista on marketing, NistaFonts on the app-shell pages) | 2026-11-11 | light | 6 of 25 met, 18 partly, 1 missing | `icons/` |
| <img src="systems/butter/icon.png" width="20" alt="butter"> | [butter](systems/butter/README.md) | Video-editor product marketing with a restrained greyscale system: a declared --butter-* token layer, a floating #ededed header island, dark #1e1e1e pill buttons hiding a #4dc5e5 cyan accent layer, a 107px DieGrotesk display, 32px #ededed pricing cards, and a dark-only MUI app shell (#0a0909 canvas, #151515 cards, #f5f5f5 inverted buttons) that is public on /explore, /blocks and /templates | 2026-11-11 | light, dark | 6 of 25 met, 18 partly, 1 missing | `icons/` |
| <img src="systems/cloudflare/icon.png" width="20" alt="cloudflare"> | [cloudflare](systems/cloudflare/README.md) | Security dashboards, condition builders, configuration tables, analytics filters and dialogs | 2026-10-31 | light, dark | 6 of 25 met, 18 partly, 1 missing | `icons/` |
| <img src="systems/sentry/icon.png" width="20" alt="sentry"> | [sentry](systems/sentry/README.md) | Dense monitoring dashboards, trace waterfalls, diagnostic tables, query builders and filters | 2026-10-31 | light, dark | 6 of 25 met, 15 partly, 4 missing | `components/`, `icons/` |
| <img src="systems/attio/icon.png" width="20" alt="attio"> | [attio](systems/attio/README.md) | Dense CRM tables, configurable views, record panels and progressive onboarding with quiet neutral chrome and blue primary actions. | 2026-10-31 | light, dark | 5 of 25 met, 19 partly, 1 missing | `icons/` |
| <img src="systems/stable-audio/icon.png" width="20" alt="stable-audio"> | [stable-audio](systems/stable-audio/README.md) | Dark generative-audio marketing: black page, square controls, white hairline rules, Neue Haas Grotesk, a sand platform primary on pricing and a homepage accent that changes between loads | 2026-11-21 | dark | 5 of 25 met, 18 partly, 2 missing | `components/`, `icons/` |
| <img src="systems/supabase/icon.png" width="20" alt="supabase"> | [supabase](systems/supabase/README.md) | Developer dashboards, code editors, member tables, settings, log filters, invitations and responsive navigation; database editing gaps documented | 2026-10-31 | dark, light | 5 of 25 met, 18 partly, 2 missing | `icons/` |
| <img src="systems/blueapron/icon.png" width="20" alt="blueapron"> | [blueapron](systems/blueapron/README.md) | Editorial and recipe surfaces: a #002856 navy promo strip and footer around a #f2f0e5 cream field, one #2959e0 action blue on 300px pill buttons, blue Ovo serif headlines over Almarai body text, and a chrome-free masonry guide grid | 2026-11-11 | light | 5 of 25 met, 17 partly, 3 missing | `icons/` |
| <img src="systems/awwwards/icon.png" width="20" alt="awwwards"> | [awwwards](systems/awwwards/README.md) | Web-awards directory and curated gallery: near-achromatic ink-on-white chrome, Inter Tight at declared weights 300-800, six category accent triads plus a measured award gold, 8/14/72px radius steps, filter-bar dropdowns and site-card grids, hand-named CSS design tokens on :root | 2026-11-11 | light | 4 of 25 met, 17 partly, 4 missing | `icons/` |
| <img src="systems/b150/icon.png" width="20" alt="b150"> | [b150](systems/b150/README.md) | Gen-AI builders' network marketing site: Tailwind v4 with a declared @layer theme token layer (warm creams on near-black chrome, coral-to-lime accents, --text-* scale, --radius-*), Fragment Mono labels under 120px Geist display, fully-round pill CTAs, marketing sections for Vibeathon, Talent, Free Resources and a contact form | 2026-11-11 | light | 3 of 25 met, 18 partly, 4 missing | `icons/` |
| <img src="systems/avnier/icon.png" width="20" alt="avnier"> | [avnier](systems/avnier/README.md) | Fashion e-commerce storefront: achromatic black-on-white Shopify chrome, Space Mono tracked-uppercase labels, licensed display titles, square zero-radius controls, mega-menu and side-drawer navigation, scheme-name CSS design tokens | 2026-11-11 | light | 3 of 25 met, 17 partly, 5 missing | `icons/` |

<!-- catalog:end -->

[catalog.json](catalog.json) holds the same list in a form a script or an
agent can read: the entry file, the tokens file, the style guide, the themes,
search tags, how it was captured, and where it was copied from.

## Using a style

1. Read the package's `README.md` (for example
   [systems/claude/README.md](systems/claude/README.md)), starting with its
   Brief: the principles, the colour roles and scales, where the components
   are, and the contrast and focus values, all generated from the package's
   own data. The rest says what was captured, how, and what to distrust, and
   its Health section says which parts of the checklist the package does not
   cover yet.
2. Take values from the tokens file, never from a screenshot. Screenshots
   are mostly stored as 256-colour PNGs to keep the repo small (Hevy's,
   Polaris's and Linear's public-site shots are full colour), and none of
   them is a measurement.
3. Open the package's `style-guide.html` to see every token and component
   rendered with the real values. Most open straight from disk; Polaris's
   fetches data, so open it through `make dev`.
4. Check the evidence label before copying a value: a measured CSS value and
   a reconstruction are not the same thing ([docs/EVIDENCE.md](docs/EVIDENCE.md)).

To point a coding agent in another project at a style, give it the package
path and tell it to read the entry file and `tokens.json` first, or connect
it to the library directly (see [For agents](#for-agents)). To build a
design system for an app of your own, start from
[docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md): it lists the five layers a
complete system needs and how the captures here compare. The tokens
are W3C DTCG in Tokens Studio's multi-set layout, which Figma (through Tokens
Studio) and Style Dictionary both read.

## For agents

One read-only tool layer, [server/library.py](server/library.py), backs
every agent surface, so an agent sees the library exactly as the gallery
does:

| Tool | What it returns |
| --- | --- |
| `search_styles` | Styles ranked by free-text words across both stores (measured `systems/` preferred, `refero/` for breadth), with platform and design-style filters |
| `get_style` | One style's distilled catalog entry: what it is for, its themes, palette preview, which files hold the detail |
| `get_tokens` | A `systems/` package's resolved token values, one group at a time |
| `read_doc` | A text file inside a package: its README, `components.md`, `tokens.json` |
| `list_media` | A package's screenshots, component crops, icons and boards with renderable URLs |
| `view_media` | One image as an MCP image block, for the questions tags cannot answer: density, layout, mood |
| `handoff_prompt` | The apply-style prompt that hands a chosen style to a coding agent |

Three ways in:

- **MCP, stdio:** `python3 server/mcp.py` from this checkout, for a client
  that spawns a process.
- **MCP, remote:** `POST <site>/api/mcp` on a hosted deployment; the same
  tools over streamable HTTP.
- **`ds` CLI:** `curl -fsSL <site>/api/install.sh | sh` installs the
  stdlib-only terminal client. `ds find`, `ds style`, `ds export`,
  `ds doc`, `ds media`, `ds handoff`, `ds tools`, `ds status`; it takes the
  server from `--url`, `DESIGNS_URL`, or its saved config.

Inside the app, Settings > Model provider turns the gallery home into a chat
over the same tools (`ANTHROPIC_API_KEY` in `.env` is the fallback; the key
stays server-side behind `/api/chat`). The app's Settings > For agents
section prints the MCP and `ds` instructions. The `design-systems` plugin in
quiver-hub wraps all of this: its `apply-style` skill follows the steps
above, `extract-style` drives the capture pipeline in
[docs/CAPTURE.md](docs/CAPTURE.md), and `author-system` builds an app's own
system against [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md); all find this
repository through `DESIGN_SYSTEMS_HOME`.

## How it works

```mermaid
flowchart LR
  SYS["systems/&lt;slug&gt;/<br/>measured, evidence-labelled"]
  REF["refero/<br/>interpreted, lower confidence"]
  CAT["catalog.json<br/>the index"]
  AUD["scorecard/<br/>rubric + dated audits"]
  GEN["Generated README sections<br/>brief.py, health.py, design-md"]
  DATA["web/data/<br/>catalog.py build"]
  SCP["docs/scorecard/<br/>scorecard.py"]
  SITE["site/<br/>site.py + StatiCrypt"]
  DOCS["docs/*.md"]
  API["server/<br/>/api routes + MCP, read-only"]
  APP["web/ app<br/>gallery, refero, scorecard, docs, chat"]
  DS["cli/ ds"]
  PAGES["GitHub Pages<br/>encrypted"]

  SYS --> CAT --> DATA --> APP
  REF --> DATA
  CAT --> GEN
  AUD --> GEN
  AUD --> APP
  AUD --> SCP --> SITE --> PAGES
  DOCS --> SITE
  SYS --> API
  REF --> API
  API --> APP
  API --> DS
```

- **A package stands alone.** Everything under `systems/<slug>/` is evidence
  plus the tools that rebuild it. A fix goes through the package's builders
  (its `tools/`), and the builders' output is committed with the input that
  changed it; a rebuild that changes nothing is the check.
- **Tokens carry provenance.** `tokens.json` is W3C DTCG in Tokens Studio's
  multi-set layout (`core` scales, `light`/`dark` semantic sets, `$themes`),
  and every token's `$extensions.source` says where it was read. Polaris is
  the exception: its Tokens Studio file uses `value`, `type` and
  `description`, and the description names the source. `DESIGN.md`
  is the generated one-theme export for tools that read Google's spec.
- **Generated, not edited.** Every package README's Brief
  ([tools/brief.py](tools/brief.py)) and Health
  ([tools/health.py](tools/health.py)), each `DESIGN.md`
  (`tools/catalog.py design-md`), this file's catalog table, `web/data/`,
  `docs/scorecard/` and `site/` are all regenerated from their sources.
  `make check` is the freshness gate: catalog shape, the three refero stores
  agreeing, and every generated section matching a fresh write.
- **The scorecard grades against the platform's wording.**
  [scorecard/criteria.json](scorecard/criteria.json) words each criterion
  per platform (web, mobile, desktop); each audit is a dated snapshot under
  `scorecard/audits/`. `make grade` re-checks the scripted criteria (F15
  contrast, F16 provenance, K2 Do-and-don't, K3 DESIGN.md), refreshes
  package details and carries the reviewed grades forward; a human
  `tools/grade.py --review` merges the rest.
- **Refero is a separate store.** `refero/refero.db` (sqlite, LFS) is
  canonical; the `refero/<slug>/` folders and `refero/catalog.json` are
  materialised from it, and `tools/refero/check.py` (inside `make check`)
  fails when the three disagree. Screenshots and videos live outside git in
  a host-side media mirror.
- **Two deployments.** Pushes to `main` run
  [pages.yml](.github/workflows/pages.yml): `make check`, then
  `tools/site.py` builds `docs/` into `site/` (it never emits the gallery),
  StatiCrypt encrypts every HTML page (the build fails if a page lacks
  StatiCrypt's marker or a search index or sitemap appears; assets are
  copied unencrypted)
  and Pages deploys it. The home-server deployment
  ([scripts/redeploy.sh](scripts/redeploy.sh),
  [scripts/deploy_trigger.py](scripts/deploy_trigger.py)) serves the app and
  the `/api/` routes behind nginx, with the refero media mirror at
  `~/services/design-systems/media/`.
- **The agent layer is read-only.** [server/library.py](server/library.py)
  holds the tool specs once; `chat.py` maps them onto the Anthropic and
  OpenAI wire shapes, `routes.py` serves `/api/*`, `mcp.py` speaks JSON-RPC
  over stdio, and `api.py` is the home-server entry point. Nothing in the
  layer writes to a package.

## Layout

| Path | What it is |
|---|---|
| [systems/](systems) | One folder per product, all in the same layout ([docs/PACKAGE.md](docs/PACKAGE.md)). Each README opens with a file table, a generated Brief and a generated Health section |
| [refero/](refero) | The second store: a snapshot of styles.refero.design (1,342 styles), interpreted data at lower confidence. `refero.db` (sqlite, LFS) is canonical; the `<slug>/` folders and `catalog.json` are materialised from it. [refero/README.md](refero/README.md) has the layout and refresh commands |
| [catalog.json](catalog.json) | The machine-readable index, and the source the gallery is built from |
| [Makefile](Makefile) | `make setup`, `make dev`, `make docs`, `make check`, `make test`, `make clean` and more (`make help`) |
| [tools/catalog.py](tools/catalog.py) | Checks the catalog, builds the app's `web/data/`, ranks packages for a query (`find`), exports any token file as CSS variables (`export`), checks WCAG contrast between token pairs (`contrast`), finds private text left in a package (`scan`), and writes each package's generated `DESIGN.md` (`design-md`) |
| [tools/redact_images.py](tools/redact_images.py) | Paints private regions out of finished screenshots and crops from a rectangle table per screenshot family, then OCR-checks every image against the redaction patterns. Rules live in [tools/redact-rules/](tools/redact-rules) |
| [tools/kit/](tools/kit) | The capture kit a new package starts from: web (public and signed-in), native iOS through iPhone Mirroring, and the token and style-guide builders |
| [tools/refero/](tools/refero) | The refero pipeline: `fetch.py` (fetch and re-export), `classify.py` (product_type / design_style / tags labels), `check.py` (the three stores agree; part of `make check`), `mirror_media.py` (host-side media mirror), `upload_r2.py`, and `generators.js`, Refero's own export code |
| [web/](web) | The Next.js app the library is browsed through: gallery, refero, scorecard and docs. Its `web/data/` (`data.json`, `thumbs/`, `refero/`, `export/`) is generated by `tools/catalog.py build` and gitignored |
| [app/](app) | The newer design research app beside `web/` (Next.js, port 8845): research, browsing, styles, collections and AI answers over the same two stores. [app/README.md](app/README.md) has its own setup |
| [server/](server) | The agent layer: a read-only tool layer over the two stores, the chat adapters, and the same tools over MCP for coding agents — stdio (`python3 server/mcp.py`) or remote (`POST /api/mcp`) |
| [cli/](cli) | `ds`, the stdlib-only terminal client for the remote MCP endpoint, and the `install.sh` that `/api/install.sh` serves |
| [scripts/](scripts) | Ops, not library: `dev.sh` behind `make dev`, and the home-server deployment and media mirror scripts (`deploy_trigger.py`, `redeploy.sh`, `studio-deploy.sh`) |
| [example/](example) | Shallow clones of public design-system repos, gitignored except [example/README.md](example/README.md). References, never a source of values |
| [docs/](docs) | The published docs site's source: the library docs below, the home page, and the scorecard pages (generated into `docs/scorecard/`, gitignored) |
| [site/](site) | The built docs site (`make docs` writes it), gitignored; the Pages workflow encrypts and deploys it |
| [scorecard/](scorecard) | The scorecard's rubric (`criteria.json`) and one dated file per audit (`audits/<date>.json`, `<date>-2.json` for a second run that day). `make grade` writes a new one with the scripted criteria re-checked ([tools/grade.py](tools/grade.py)) |
| [tools/make_icons.py](tools/make_icons.py) | The site has two app icons, picked under Settings > Preferences. Flat, the default, is the prism mark in [docs/assets/favicon.svg](docs/assets/favicon.svg) with its renders in [docs/assets/icons/](docs/assets/icons), committed as drawn. This script derives the Glass set ([docs/assets/icons/glass/](docs/assets/icons/glass)) from its master render, [docs/assets/logo/hero-ai.png](docs/assets/logo/hero-ai.png). Every docs page's template head links the Flat favicon, the touch icon, the web app manifest ([docs/site.webmanifest](docs/site.webmanifest)) and [docs/assets/app-icon.js](docs/assets/app-icon.js), which swaps in the chosen set before first paint |
| [tools/scorecard.py](tools/scorecard.py) | Writes the scorecard pages from [scorecard/](scorecard) |
| [tools/site.py](tools/site.py) | Builds the docs site into `site/`: every `docs/**.md` page rendered with the site's own chrome |
| [tools/brief.py](tools/brief.py) | Writes the Brief section near the top of every package README: the page to read before designing in that style, generated from the package's catalog entry, tokens and README. `make brief` and `make design-md` run it; `make check` fails when one is stale |
| [tools/health.py](tools/health.py) | Writes the Health section at the top of every package README and the catalog table above, from the newest scorecard snapshot and each package's folder. `make grade` runs it; `make check` fails when one is stale |
| [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md) | What a complete design system for your own app contains, layer by layer |
| [docs/PACKAGE.md](docs/PACKAGE.md) | What a package contains, file by file |
| [docs/EVIDENCE.md](docs/EVIDENCE.md) | How every value says where it came from |
| [docs/CAPTURE.md](docs/CAPTURE.md) | How to capture a new product, and the traps that cost time before |
| [docs/RIGHTS.md](docs/RIGHTS.md) | Why this repo stays private, and what is not ours |
| [AGENTS.md](AGENTS.md) | Instructions for coding agents working here |

## Where the packages came from

The nine "reference" packages were built in
[self-learn](https://github.com/c-wenlong/self-learn) under
`docs/design/reference/` for its redesign, and copied here byte for byte at
self-learn commit `84a260ac`. The Linear and Polaris audits were built
alongside a work project's designs and copied the same way, minus
their zip bundles and `node_modules`. [catalog.json](catalog.json) records each
source path. The packages' own prose still mentions the project they were
made for; that is history, and it is left as written.

## Development

```bash
make check   # the freshness gate; run before every commit
make test    # tools' unit tests, then every systems/*/tools/test_*.py in its own interpreter
make grade   # after changing a package: re-grade scripted criteria, refresh every Health section
```

`make test` reports a package test that needs Pillow as skipped when the
interpreter lacks it; `make test PYTHON=<a python3 with Pillow>` covers
those too. `make lint-design-md` runs Google's pinned DESIGN.md linter
through `npx` in a temp dir.

CI runs four workflows:

| Workflow | What it gates |
| --- | --- |
| [check.yml](.github/workflows/check.yml) | `make check` on every push to `main` and every pull request |
| [app.yml](.github/workflows/app.yml) | Format check, media taxonomy check, typecheck, tests and a production build for `app/` when `app/**`, `systems/**`, `catalog.json`, `refero/catalog.json` or `tools/catalog.py` changes |
| [web.yml](.github/workflows/web.yml) | Typecheck and a production build for `web/` when `web/**`, `tools/catalog.py` or `catalog.json` changes |
| [pages.yml](.github/workflows/pages.yml) | `make check`, then the docs site build, StatiCrypt encryption and the Pages deploy; a stale generated section fails the deploy |

Rules that bite: Brief, Health, `DESIGN.md`, `web/data/`,
`docs/scorecard/` and `site/` are regenerated, never hand-edited; every
binary type goes through Git LFS ([.gitattributes](.gitattributes));
`systems/`, screenshots and the gallery are never published; `.env` is never
committed. [AGENTS.md](AGENTS.md) is the full brief for agents working here,
including the pre-commit checks.

## The docs

| Document | What it covers |
| --- | --- |
| [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md) | The five layers a complete design system needs; the rubric the scorecard grades against |
| [docs/PACKAGE.md](docs/PACKAGE.md) | What a package contains, file by file |
| [docs/EVIDENCE.md](docs/EVIDENCE.md) | How every value says where it came from |
| [docs/CAPTURE.md](docs/CAPTURE.md) | How to capture a new product, and the traps that cost time before |
| [docs/RIGHTS.md](docs/RIGHTS.md) | Why this repo stays private, and what is not ours |
| [docs/TODO.md](docs/TODO.md) | Open work, newest first |
| [refero/README.md](refero/README.md) | The refero snapshot: layout, provenance, refresh and the media mirror |
| [example/README.md](example/README.md) | The public reference clones and the rules for using them |
| [app/README.md](app/README.md) | The research app: running it, provider keys, its boundaries |
| [AGENTS.md](AGENTS.md) | The brief for coding agents working here, or reading the library from another project |

## Private

This repository stays private and is not pushed anywhere but
`c-wenlong/designs`. The captures include signed-in pages and products' own
artwork; [docs/RIGHTS.md](docs/RIGHTS.md) says what may leave the repo and
what may not. Borrow structure and proportions from a package; never ship a
product's logo, icons, illustrations or brand colours.
