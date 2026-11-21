# Aaply public site tree

Mapped 2026-11-21 from https://aaply.app/ in headless Chromium (Playwright), desktop 1440×900 and phone 390×844. Read-only: no form was submitted, no password or code was typed, and no Google or Apple control was clicked.

The marketing site is a Tilda site. It loaded (HTTP 200, title "Aaply — Mobile app design tool"). One light theme. No cookie banner, no newsletter form, and no dialog on the live pages.

## How the chrome opens pages

| Control | Where | Opens |
|---|---|---|
| Wordmark | Desktop nav, left | `/` |
| Features | Desktop nav | `/features` |
| Value | Desktop nav | `/value` |
| Pricing | Desktop nav | `/pricing` |
| Reviews | Desktop nav | `/reviews` |
| Log in | Desktop nav pill | `https://go.aaply.app/login` (auth wall; see boundary) |
| Sign up | Desktop nav pill | `https://go.aaply.app/signup` (auth wall) |
| Burger (`a[href="#open-nav"]`) | Phone nav, top right | In-page overlay menu (no navigation). Visible items: Log in, Sign up, Features, Figma Plugin, Pricing, Reviews, Value, Story, Team, Blog, then Twitter, Instagram, Medium, YouTube, LinkedIn. Discord and close (`#close-nav`) sit in the overlay header. |
| Close (`a[href="#close-nav"]`) | Phone menu | Closes the overlay |
| Discord mark | Nav (desktop, off the pill) and phone menu | `https://discord.gg/FWqK8e8r3S` (external; not followed) |
| Footer Features, Value, Pricing, Reviews, Story, Team, Figma Plugin | Every page footer | The matching marketing route |
| Footer Blog | Every page footer | `https://medium.com/aaply-stories` (external) |
| Footer social marks | Every page footer | Twitter, Medium, LinkedIn, YouTube, Instagram, Discord (external) |
| Footer mail link | Every page footer | A published `mailto:` contact. Not followed. The address is not copied into this tree. |

Phone menu item targets, read from the live anchors after the burger click:

| Menu item | Target |
|---|---|
| Log in | `https://go.aaply.app/sign` |
| Sign up | `https://go.aaply.app/signup` |
| Features | `/features` |
| Figma Plugin | `/figma_plugin` |
| Pricing | `/pricing` |
| Reviews | `/reviews` |
| Value | `/value` |
| Story | `/our-story` |
| Team | `/team` |
| Blog | `https://medium.com/aaply-stories` |

Desktop nav does not list Figma Plugin, Story, Team, or Blog. Those are footer and phone-menu only.

## Pages reachable from the homepage without leaving the marketing host

| Path | How it is opened | What it is | States on the page |
|---|---|---|---|
| `/` | Wordmark, or load the site | Home: hero, numbered steps, demo CTA, early-birds band, footer | Default. No menu, dialog, or form. |
| `/features` | Nav Features, footer, phone menu | Workflow walkthrough ("Here's what aaply workflow looks like") | Default. "Try DEMO project" leaves the host. |
| `/value` | Nav Value, footer, phone menu | Value page | Default. |
| `/pricing` | Nav Pricing, footer, phone menu, home "Compare Features" | Plans and feature table | Monthly and Yearly are a local segment swap. Nothing is posted. |
| `/reviews` | Nav Reviews, footer, phone menu | Review wall | Default plus carousel dots `button[aria-label="N of 6"]` (six slides). Clicking a dot does not navigate. |
| `/our-story` | Footer Story, phone menu Story | Story | Default. "Join beta!" leaves the host. |
| `/team` | Footer Team, phone menu Team | Team | Default. "Join beta!" leaves the host. "Drop a line" is a published mailto and was not followed. |
| `/figma_plugin` | Footer Figma Plugin, phone menu | Figma plugin page | Default. |
| `/early-program` | Sitemap only. No nav, footer, or phone-menu control points here. | Early Users Program | Default. "Sign up for FREE" leaves the host. The page also shows a published contact link. That address is not copied into this tree. |
| `/workflow` | Sitemap only. The word "workflow" on `/features` is a heading, not a link. | Same workflow walkthrough as `/features` (title "Features") | Default. Treated as a duplicate of `/features`, not a second product surface. |
| `/manual` | Sitemap only. No in-page control points here. | "How to get started with Aaply?" with an embedded video | Default. "Start new project" goes to `https://go.aaply.app/` (auth wall). |

## Interactions that are not pages

| Control | Result |
|---|---|
| Pricing Yearly / Monthly | Local paint swap of the held segment. Restored to Yearly after the shot. |
| Reviews carousel dots (1 of 6 through 6 of 6) | Selects a slide in place. |
| Phone `#open-nav` / `#close-nav` | Overlay menu, then close. |
| "Join the early birds" heading | Not a control. The yellow "Sign up to aaply" button beside it is the control, and it leaves the host. |
| Chat bubbles ("Yeah, it's interesting", "Looks nice!", "Give me a sec") | Static decoration. Clicking the heading does not open a dialog. |

## Auth boundary (stop)

These controls leave the marketing host. The branch stops at the URL. Nothing was typed.

| Control | URL | Result on 2026-11-21 |
|---|---|---|
| Nav Log in | `https://go.aaply.app/login` | HTTP 404, body "Not found" |
| Nav Sign up, "Sign up fo free", "Sign up to aaply", "Join beta!", "Sign up for FREE" | `https://go.aaply.app/signup` | HTTP 404, body "Not found" |
| Phone-menu Log in | `https://go.aaply.app/sign` | HTTP 404, body "Not found" |
| "Try demo project", "Try it!", "Try DEMO project" | `https://go.aaply.app/workspace/demo` | HTTP 404, body "Not found" |
| Manual "Start new project" | `https://go.aaply.app/` | HTTP 200, but the document is not Aaply. Title and h1 are a foreign site (`muay555`); body does not mention Aaply. Not an app surface. Not captured. |
| `https://app.aaply.app/` | not linked from the marketing nav | HTTP 200, foreign site, same family. Not captured. |
| `https://aaply.app/login`, `/signup` | not linked | HTTP 404, "404 Page not found" |

No app package is invented from `go.aaply.app`.

## Sitemap pages that are not the public product

`https://aaply.app/sitemap.xml` lists 13 URLs. These are drafts or Tilda internals, not opened by any control on the live marketing pages. They are recorded and not captured as product UI.

| URL | Why it is out |
|---|---|
| `/page28901772.html` | Title "Copy of Aaply". Contains a Tilda form (`form action` on `forms.tildacdn.com`) with hidden fields. Not submitted. Not captured. |
| `/page29112172.html` | Title "Blank page". Tilda block-editor placeholder plus unrelated third-party copy. Not captured. |
| `/page37280974.html` | Title "test Pricing". A pricing draft. Not linked. Not captured. |
| `/page16180841.html` and the other paths in `robots.txt` Disallow | Tilda internals (`/tilda/form*`, `/tilda/popup*`, `/members/login*`, `/thankpage`, numbered pages). Not opened. |

`https://www.aaply.app/` redirects to `https://aaply.app/`.

## External, not captured

Discord, Twitter, Medium, LinkedIn, YouTube, Instagram, and `mailto:` links. Blog is Medium, not an on-site page.
