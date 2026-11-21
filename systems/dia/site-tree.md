# Dia public site tree

Mapped on 2026-11-22 from the live public site, signed out. Official domain confirmed as `https://www.diabrowser.com/` (title "Dia | The browser for better days at work.", hero "More than a browser. A better workday."). `https://diabrowser.com` 308s there. This is The Browser Company's Dia browser, not a parked page.

Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. `login-extracted` stays `not-started`.

The marketing site paints one light theme. `color-scheme` on the root was `normal`. There is no theme control. The homepage hero is a yellow photograph. Inner pages sit on cream `#FBFAF6`.

## Auth walls

No public login or signup wall was on the site.

| Path | What opened | Action |
|---|---|---|
| `/login` | Public 404. "This page could not be found." Go back home. | No email field. Not typed. |
| `/signup` | The same 404. | No email field. Not typed. |
| `https://auth.diabrowser.com/` and `/login`, `/signup`, `/sign-in`, `/sign-up` | HTTP 200 with an empty document. No fields. | Not typed. No provider clicked. |
| `account.diabrowser.com` | Name does not resolve. | Not opened. |

The signed-in app was not entered.

## Homepage header (`https://www.diabrowser.com/`)

Desktop: a white pill, centered. Logo to `/`, then What's New, Apps, Security. No login link. No menus. The pill does not open a drawer.

| Control | Opens |
|---|---|
| Logo | `/` |
| What's New | `/release-notes/latest`, which 307s to `/release-notes/1-57-find-your-flow` |
| Apps | `/apps` |
| Security | `/security` |

Phone (390): the same pill, plus an Open menu button. The open drawer is a white sheet over the yellow hero. It lists What's New, Apps, Security, then Download Dia and Watch the trailer video. Close returns to the page. No row was followed from the drawer.

## Download

| Control | Opens |
|---|---|
| Home "Download Dia for free" | `/download/thanks`. "Your download will start automatically." A manual link points at `https://releases.diabrowser.com/release/Dia-latest.dmg`. The binary was not kept. The thanks page is install steps and an FAQ. No form. |
| `/download` | "Meet Dia, the AI Browser." Download Dia. "Currently available on macOS (Apple Silicon) and Windows 11." |
| Drawer "Download Dia" | Same download path. Not followed from the drawer. |
| Drawer "Watch the trailer video" | A video control on the homepage. Not played. |

## Footer

On inner pages, after the page. Columns:

- Product: For Work (`/forwork`), Release Notes, Changelog (`/changelog`), Windows (`/windows`).
- Resources: Help (`/help`), Status (`https://status.diabrowser.com`), Privacy (`/privacy`), Terms of Use (`/termsofuse`), Security, Trust Center (`https://trust.diabrowser.com/`).
- Company: About Us and Careers (`https://thebrowser.company/`), Newsletter (Substack), Early Birds Program (`/earlybirds`).
- Connect: X, LinkedIn, Instagram. Not opened.
- Credit: Designed and Built by The Browser Company of New York.

Status, Trust Center, the company site, the newsletter, and the social hosts are other hosts. They were not captured as product pages.

## Pages opened

| Page | What it is |
|---|---|
| `https://www.diabrowser.com/` | Marketing home. Yellow hero. White nav pill. Black download pill. |
| `https://www.diabrowser.com/apps` | Apps. "All your apps, working together." Featured app cards. |
| `https://www.diabrowser.com/security` | Security. Sidebar and article. |
| `https://www.diabrowser.com/release-notes/1-57-find-your-flow` | What's New. |
| `https://www.diabrowser.com/download` | Public download. |
| `https://www.diabrowser.com/download/thanks` | Download thanks. No form. |
| `https://www.diabrowser.com/windows` | Windows page. |
| `https://www.diabrowser.com/changelog` | Changelog index. |
| `https://www.diabrowser.com/forwork` | For Work. |
| `https://www.diabrowser.com/privacy` | Privacy policy. |
| `https://www.diabrowser.com/termsofuse` | Terms. |
| `https://www.diabrowser.com/earlybirds` | Early Birds. |
| `https://www.diabrowser.com/students` | Dia for Students. |
| `https://www.diabrowser.com/this-page-does-not-exist-capture-2026` | 404. "This page could not be found." Go back home. |
| `https://www.diabrowser.com/help` | Help Center with a live chat widget and an empty message field. Photographed, then discarded so the package does not keep a chat surface. Nothing typed. Nothing sent. |
| `/pro` and `/skills` | 308 to the homepage. Not separate pages. |

Phone width was captured for the homepage (closed and with the menu open) and for Apps.
