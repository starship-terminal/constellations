# Fernand public site tree

Walked on 2026-11-21 from [https://getfernand.com/](https://getfernand.com/) with Playwright, signed out. Desktop viewport requested 1440x900. Phone viewport requested 390x844. Cookie banners did not mount. None were accepted.

The marketing host published 206 URLs in [https://getfernand.com/sitemap.xml](https://getfernand.com/sitemap.xml). Every sitemap URL was opened. Template families (changelog posts, rule templates, snippet templates) share one header, one footer, and one article body. Representative shots of each family are in [screenshots/](screenshots/).

The walk stopped at the auth wall. Log in opens [https://app.getfernand.com/auth/login](https://app.getfernand.com/auth/login). Start for free opens [https://app.getfernand.com/create](https://app.getfernand.com/create). Neither form was submitted. Details are in [login-review.json](login-review.json).

## Header

The same banner is on every marketing page, including the 404.

| Control | Opens |
|---|---|
| Wordmark | [https://getfernand.com/](https://getfernand.com/) |
| About us | [https://getfernand.com/about-us/](https://getfernand.com/about-us/) |
| Pricing | [https://getfernand.com/pricing/](https://getfernand.com/pricing/) |
| Log in | [https://app.getfernand.com/auth/login](https://app.getfernand.com/auth/login). Wall. Stop. |
| Book a demo | Cal.com modal on the same page (`data-cal-link="antoineminoux/fernand-demo"`). Iframe title "Book a call". Not submitted. |
| Start for free | [https://app.getfernand.com/create](https://app.getfernand.com/create). Wall. Stop. |

Phone (390): the same links stay in the header. There is no menu button. The header shows the wordmark, About us, Pricing, Log in, and Start for free. Book a demo is not in that header row. It is visible in the hero, beside a dark Start for free control. See [screenshots/phone-home-default.png](screenshots/phone-home-default.png).

[https://getfernand.com/login](https://getfernand.com/login) is a 404 ("Uh oh That page doesn't exist"). The header does not link there.

## Footer

Present on every marketing page. Link text is the label.

| Column | Control | Opens |
|---|---|---|
| Product | Pricing | /pricing/ |
| Product | Documentation | https://help.getfernand.com/ |
| Product | Headless customer support | /feature/headless-customer-support/ |
| Product | AI agents | /feature/ai-agents/ |
| Product | Customer support automation | /customer-support-automation/ |
| Product | API reference | https://developers.getfernand.com/ |
| Product | Changelog | /updates/ |
| Product | Blog | /blog/ |
| Product | About | /about-us/ |
| Integrations | All integrations | /integrations/ |
| Integrations | Stripe | /integrations/stripe/ |
| Integrations | Linear | /integrations/linear/ |
| Integrations | GitHub | /integrations/github/ |
| Integrations | Slack | /integrations/slack/ |
| Integrations | Paddle | /integrations/paddle/ |
| Integrations | Polar | /integrations/polar/ |
| Integrations | Dodo Payments | /integrations/dodo-payments/ |
| Integrations | Lemon Squeezy | /integrations/lemon-squeezy/ |
| Integrations | API | /integrations/api/ |
| Alternatives | Intercom alternative | /alternative/intercom/ |
| Alternatives | Zendesk alternative | /alternative/zendesk/ |
| Alternatives | Help Scout alternative | /alternative/help-scout/ |
| Alternatives | Crisp alternative | /alternative/crisp/ |
| Alternatives | Front alternative | /alternative/front/ |
| Alternatives | Freshdesk alternative | /alternative/freshdesk/ |
| Alternatives | Tidio alternative | /alternative/tidio/ |
| Alternatives | Plain alternative | /alternative/plain/ |
| Alternatives | Pylon alternative | /alternative/pylon/ |
| Legal | Terms of service | /terms/ |
| Legal | Privacy policy | /privacy/ |
| Legal | GDPR compliance | /gdpr-compliance/ |
| Legal | Imprint | /imprint/ |
| Contact | Support mail link | mailto on the marketing host. Not sent. The address is not copied into this package. |
| Contact | Help center | https://help.getfernand.com/ |
| Contact | API Docs | https://developers.getfernand.com/ |
| Contact | Status page | https://status.getfernand.com/ |
| Contact | Follow us on X | https://x.com/getfernand |
| Contact | Chat with us | In-page messenger launcher (`messenger.getfernand.com`). Not a new account. |

## Home controls

| Control | Opens |
|---|---|
| Start for free | Auth wall, /create. Stop. |
| Book a demo | Cal.com modal. Not submitted. |
| Install with AI | Menu: Cursor (`cursor.com/link/prompt`), Codex (`codex://new`), Claude Code (`claude://code/new`). Not followed. |
| Watch a 2 minute demo | Dialog with a youtube-nocookie embed of `pbJFZt9ThjE`. Close control is "x". |
| Scroll left / Scroll right | Customer logo rail on the same page. |
| Changelog chip (latest update) | That update's page under /updates/. |
| Learn more rows | Either a /feature/ page, /integrations/, /customer-support-automation/, or a help.getfernand.com article. |
| Popup, Modal, Drawer | Widget preview modes on the same page. No navigation. |
| Light, Dark | Widget preview theme on the same page. The marketing page itself stays light. |
| On, Off | Widget preview toggles on the same page. |
| Left, Right | Widget preview position on the same page. |
| Open account, Manage integrations | Labels inside the product illustration. They do not navigate. |

No search field exists on the public pages.

## Sitemap

| Family | Count | What a page is |
|---|---|---|
| / | 1 | Home |
| /about-us/ | 1 | About |
| /pricing/ | 1 | Pricing |
| /blog/ and posts | 9 | Index plus 8 posts |
| /feature/ | 6 | Feature pages (ai, ai-agents, headless-customer-support, knowledge-base, shared-inbox, support-widget) |
| /integrations/ and children | 11 | Index plus github, linear, lemon-squeezy, stripe, slack, api, paddle, polar, dodo-payments, custom-data |
| /alternative/ | 9 | Comparison pages |
| /updates/ and posts | 31 | Changelog index plus 30 posts |
| /customer-support-automation/ | 1 | Automation index |
| /customer-support-automation/rules/ | 71 | Rule templates |
| /customer-support-automation/snippets/ | 61 | Snippet templates |
| /terms/ /privacy/ /gdpr-compliance/ /imprint/ | 4 | Legal |
| /login | 0 in sitemap | 404 on the marketing host |

Rule and snippet pages share the automation template: header, a title, a template body, a link to help.getfernand.com docs, and the footer. Changelog posts share the updates template.

## Off-site, recorded and not walked as the app

| Host | Why it appears | Walk |
|---|---|---|
| app.getfernand.com | Log in, Start for free, Create an account, Lost password | Opened the wall. Stopped. |
| help.getfernand.com | Documentation links | Public docs. Not the signed-in app. |
| developers.getfernand.com | API reference | Public docs. |
| api.getfernand.com | OpenAPI spec link | Not called with a key. |
| status.getfernand.com | Status page | Public status. |
| app.cal.com | Book a demo embed | Modal only. Not submitted. |
| messenger.getfernand.com | Support widget iframe | Launcher only. |
| x.com, twitter.com | Social links | Not the product. |

## Screenshots

The walk opened every sitemap URL at desktop, plus the marketing `/login` 404. Committed shots are a representative set, not one file per URL. Rule and snippet templates are represented by three pages (`inbox-tag-billing-questions`, `ask-cursor-to-draft-the-reply`, `answer-an-sso-question`). Changelog posts are represented by the updates index and one post. Blog posts are represented by the blog index and one post. Alternatives are represented by the Intercom page.

Desktop viewport files are `desk-<slug>-default.png`. Matching `desk-<slug>-full.png` files are the scrolled page for shell and index pages. Phone files are `phone-<slug>-default.png` and, where taken, `phone-<slug>-full.png`, for the shell and one page of each family. Phone auth walls were not photographed. The phone walk did not open the signup or lost-password walls.

Opened states, all desktop: `desk-home-ai-menu.png`, `desk-home-watch-demo.png`, `desk-home-book-demo.png`, `desk-home-chat-launcher.png`, `desk-home-widget-popup.png`, `desk-home-widget-modal.png`, `desk-home-widget-drawer.png`, `desk-home-widget-light.png`, `desk-home-widget-dark.png`, `desk-app-login.png`, `desk-app-create.png`, `desk-app-lost.png`.

No search control exists, so there is no search shot. Cookie banners did not mount.

Viewport proof, read from the capture sidecars before they were left out of the package: `desk-home-default` innerWidth 1440, innerHeight 900, device pixel ratio 1. `phone-home-default` innerWidth 390, innerHeight 844, device pixel ratio 2. `desk-app-login` innerWidth 1440, innerHeight 900.
