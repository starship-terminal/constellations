# Zed public site tree

Mapped on 2026-11-22 from the live public site, signed out, in headless Chromium. Official domain confirmed as `https://zed.dev/` (title "Zed — Your last next editor", hero "Your last next editor"). The page loaded. It is not a parked domain and not a captcha wall.

Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. `login-extracted` stays `not-started`.

origin/main did not have `systems/zed/`. This is a first capture of the public web site. `systems/zed-desktop/` was left alone. The slug did not change.

The first paint of `/` is a company gate: heading "Zed Industries", two product cards (Delta and Zed). Delta's Learn More goes to `https://delta.dev/`. Zed's Learn More reveals the editor marketing page on the same URL. The shots below are that marketing page. The gate was not the page that stayed on screen.

The marketing site paints light and dark. The root class follows `prefers-color-scheme`. A command menu (the P button) lists "Turn light mode on" and "Follow the System's settings". That menu was opened and not used to change the theme. Light and dark shots come from the browser colour scheme.

The editor mock on the homepage is a public demo. Names in it (nathansobo, sample threads, sample diffs) are the site's illustration.

## Homepage header (`https://zed.dev/`)

Desktop: logo to `/`, then Product and Resources (menus), Extensions, Docs, Pricing, Delta (other host). On the right: a command menu (P), Sign up, Download.

| Control | Opens |
|---|---|
| Logo | `/` |
| Product | A menu. Does not navigate. |
| Resources | A menu. Does not navigate. |
| Extensions | `/extensions` |
| Docs | `/docs` |
| Pricing | `/pricing` |
| Delta | `https://delta.dev/` (other host, not captured as a Zed page) |
| Command menu (P) | A dialog: "Navigate…". Not typed. Esc dismisses. |
| Sign up | `/sign_up` |
| Download | `/download` |

Product menu, Core Editor:

| Item | Opens |
|---|---|
| Windows | `/windows` |
| Debugger | `/debugger` |
| Git Support | `/git` |
| Remote Development | `/remote-development` |

Product menu, Artificial Intelligence:

| Item | Opens |
|---|---|
| Parallel Agents | `/parallel-agents` |
| Agent Client Protocol | `/acp` |
| Agentic Editing | `/ai` |
| Edit Prediction | `/edit-prediction` |

Resources menu:

| Column | Item | Opens |
|---|---|---|
| Product | Releases | `/releases/stable` |
| Product | Roadmap | `/roadmap` |
| Product | Theme Builder | `/theme-builder` |
| Product | Languages | `/languages` |
| Connect | Blog | `/blog` |
| Connect | Community | `/community` |
| Connect | Events | `/community#upcoming-events` |
| Connect | Education | `/education` |
| Connect | Support | `/support` |
| Learn | Agentic Engineering | `/agentic-engineering` |
| Learn | Agent Metrics | `/agent-metrics` |
| Learn | User Stories | `/user-stories` |
| Learn | FAQ | `/faq` |
| Learn | Migrate | `https://zed.dev/docs/migrate/vs-code` |
| Company | About | `/about` |
| Company | Team | `/team` |
| Company | Values | `/values` |
| Company | Jobs | `/jobs` |
| Company | Merch | `https://merch.zed.dev/` (other host) |

Command menu rows seen, not followed: Turn light mode on, Follow the System's settings, Copy logo as SVG, Copy wordmark as SVG, View brand guidelines, Home, Download, Extensions. The search field was left empty.

## Phone (390 by 844)

The header collapses to the logo and an Open navigation menu button. The open drawer lists Home, Product, Blog, Extensions, Docs, Business, Pricing, Resources, Delta, then "Turn Dark Mode On" and Close Menu. No row was followed from the drawer. The theme row was not clicked.

## Download

`/download` is public. The heading was "1.29.2", dated November 18, 2026. Stable and Preview tabs. macOS (Apple Silicon), Windows (ARM64), and a Linux install command. The binaries were not downloaded. The newsletter email field was left empty. Subscribe was not clicked.

## Docs

`/docs` is public. Title "Getting Started | Getting Started with Zed". A left nav, an article, an on-this-page list, and an empty "Search docs…" field. The field was not typed.

## Footer

A blue band after the page. Columns: Product, Resources, Company, Social, plus account links.

| Column | Links |
|---|---|
| Account | Sign Up (`/sign_up`), Sign In (`/sign_in`), Terms of Service (`/terms`), Attributions (`/attributions`), Manage Site Cookies (a control, not clicked) |
| Product | Download, Pricing, Business (`/business`), Releases, Extensions, Roadmap, Docs, Compare (`/compare`), GitHub (other host), Status (`https://status.zed.dev`, other host) |
| Resources | FAQ, CLA (`/cla`), Community, Support, Discussions (GitHub, other host), Privacy (`/privacy`), Subscribe (`/subscribe`), Theme Builder, Yearly Recaps (`/2025`) |
| Company | Blog, About, Values, Team, Jobs, Press (`/press`), Brand (`/brand`), Merch (other host) |
| Social | Twitter, Bluesky, Instagram, YouTube, Discord, Reddit. Other hosts. Not opened. |

## Auth walls

Photographed empty. Stopped there.

| Path | What opened | Action |
|---|---|---|
| `/sign_in` | Redirects to `https://github.com/login`. Title "Sign in to GitHub · GitHub". Copy: "Sign in to GitHub to continue to Zed Industries." Empty username and password fields. Continue with Google and Continue with Apple are on the page. | Not typed. Google not clicked. Apple not clicked. Sign in not clicked. Create an account not clicked. |
| `/sign_up` | Stays on `https://zed.dev/sign_up`. Heading "Welcome to Zed". Two unchecked boxes (terms, release notes). A Cloudflare "Verify you are human" checkbox. "Sign Up with GitHub" is on the card. "Already have an account? Sign In." | Boxes not checked. Captcha not solved. GitHub not clicked. Sign In link not followed from this card. |

## Pages opened

| Page | What it is |
|---|---|
| `https://zed.dev/` | Marketing home, dark and light, and phone with the menu closed and open. |
| `https://zed.dev/download` | Public download. Version 1.29.2. |
| `https://zed.dev/docs` | Docs landing. Getting Started. |
| `https://zed.dev/pricing` | Personal $0, Pro $10, Business $30. Get Started was not clicked. |
| `https://zed.dev/extensions` | Public extension directory. Search left empty. |
| `https://zed.dev/windows` | Windows marketing page. |
| `https://zed.dev/faq` | FAQ. |
| `https://zed.dev/about` | Our Vision. |
| `https://zed.dev/blog` | From The Blog. |
| `https://zed.dev/this-page-does-not-exist-capture-2026` | 404. "Page Not Found." |
| `https://zed.dev/sign_up` | Empty signup wall. |
| `https://github.com/login` | Empty GitHub wall reached from `/sign_in`. |

Product menu destinations other than Windows, and footer pages other than the ones in this table, were mapped and not each photographed. Other hosts (delta.dev, status.zed.dev, merch.zed.dev, social) were not captured as Zed pages.
