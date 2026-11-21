# Aboard public site tree

Mapped from the homepage at https://www.aboardhr.com/ on 2026-11-21, signed out, before any screenshot in this refresh. The marketing site is a Framer page. The product app is a separate host. Nothing was submitted, and no identity provider was clicked.

Homepage title: "Aboard — Joyful HR". Headline: "Run people operations."

## Desktop nav (1440)

The fixed band is `nav[data-framer-name="Desktop"]`.

| Control | Opens |
|---|---|
| Logo (`a[data-framer-name="Logo"]`, href `./`) | Homepage, https://www.aboardhr.com/ |
| Product (anchor with no href) | Hover menu, not a page. Three rows, each an `a[data-framer-name="Link Dropdown Big"]`. |
| Product menu: Everyday HR ("Let the essentials run smoothly.") | Page, https://www.aboardhr.com/everyday-hr |
| Product menu: Team culture ("Where connection becomes culture.") | Page, https://www.aboardhr.com/team-culture |
| Product menu: Growth & feedback ("Support and grow your team.") | Page, https://www.aboardhr.com/growth-feedback |
| Price | Page, https://www.aboardhr.com/pricing |
| Resources (anchor with no href) | Hover menu, not a page. |
| Resources menu: What's new | Page, https://www.aboardhr.com/whats-new |
| Resources menu: Help center | External page, https://help.aboardhr.com/en/ (the link redirects from https://help.aboardhr.com/). Public Intercom help center, not a login wall. |
| Sign in | Login wall, https://app.aboardhr.com/login. Stop. |

The Product and Resources menus are overlays on the homepage. They are not dialogs: no `role="dialog"`, and they close when the pointer leaves.

## Homepage body

| Control | Opens |
|---|---|
| Release chip, "June 2026 — Welcoming new hires, celebrating your team, connecting AI" | Page, https://www.aboardhr.com/whats-new (the index, not the June post) |
| Book a demo (primary pill) | Page, https://www.aboardhr.com/book-demo. The form is public. Do not submit it. |
| Try for free | Signup wall, https://app.aboardhr.com/signup. Stop. |
| Co-pilot panel ("Ask Co-pilot") | Nothing. It is a canned marketing animation, not a control. |
| Everyday HR section, Learn more | Page, https://www.aboardhr.com/everyday-hr |
| Team culture section, Learn more | Page, https://www.aboardhr.com/team-culture |
| Growth & feedback section, Learn more | Page, https://www.aboardhr.com/growth-feedback |
| Lower Book a demo | Page, https://www.aboardhr.com/book-demo |

## Footer (same on the mapped marketing pages)

| Control | Opens |
|---|---|
| Price | Page, https://www.aboardhr.com/pricing |
| What's new | Page, https://www.aboardhr.com/whats-new |
| Help center | External page, https://help.aboardhr.com/ |
| Privacy policy | External page, https://www.teamtailor.com/en/privacy-policy/ (Teamtailor, not Aboard) |
| Terms and conditions | Page, https://www.aboardhr.com/terms |
| Data protection | Page, https://www.aboardhr.com/dataprotection |
| Made by Teamtailor | External page, https://www.teamtailor.com/ |

## Pages reached from the homepage, and what they add

| Page | Extra controls |
|---|---|
| https://www.aboardhr.com/whats-new | Four release rows, plus a public `mailto:help@aboardhr.com` link. |
| Release row, June 2026 | Page, https://www.aboardhr.com/whats-new/june-2026 |
| Release row, April 2026 | Page, https://www.aboardhr.com/whats-new/april-2026 |
| Release row, March 2026 | Page, https://www.aboardhr.com/whats-new/march-2026 |
| Release row, December 2025 | Page, https://www.aboardhr.com/whats-new/december-2025 |
| https://www.aboardhr.com/book-demo | A form (name, company, company email, location select, phone, employee-count select, "Let's talk" submit). Not submitted. |
| https://www.aboardhr.com/terms | In-page anchors (`#2`, `#3`, `#4`) and a link to https://www.aboardhr.com/subprocessors. Also links out to help articles, status.aboardhr.com, and EU/UK contract-clause PDFs. |
| https://www.aboardhr.com/dataprotection | In-page anchors (`#1` through `#9`), the same subprocessors page, and help-center articles. |
| https://www.aboardhr.com/subprocessors | Linked from the legal pages, not from the homepage. Public legal list. No extra navigation. |
| Product pages | Book a demo and Try for free, same targets as the homepage. |

https://www.aboardhr.com/teamtailor-and-aboard still returns 200 ("Teamtailor ❤️ Aboard") but no homepage, nav, or footer control opens it. It is not part of this tree.

## Phone nav (390)

The band is `nav[data-framer-name="Phone"]`, 64px tall. The logo returns to the homepage. The hamburger is the trailing icon `div[data-framer-name="Line.3.horizontal"]` at the right of the band (the older `navtrigger` hit target sits under the band and does not open the menu). A tap opens an overlay menu, not a new page:

| Menu row | Opens |
|---|---|
| Everyday HR | https://www.aboardhr.com/everyday-hr |
| Team culture | https://www.aboardhr.com/team-culture |
| Growth & feedback | https://www.aboardhr.com/growth-feedback |
| What's new | https://www.aboardhr.com/whats-new |
| Help center | https://help.aboardhr.com/en/ |
| Price | https://www.aboardhr.com/pricing |
| Book demo | https://www.aboardhr.com/book-demo |
| Sign in | https://app.aboardhr.com/login. Stop. |

## Walls (not entered)

| Control | What is on the other side |
|---|---|
| Sign in | https://app.aboardhr.com/login. "Good to see you." Offers Continue with Google, Continue with Microsoft, Sign in with passkey, an email field, and Continue. Stop. No provider clicked, no email typed. |
| Try for free | https://app.aboardhr.com/signup. Offers work email, first name, last name, company, phone number, and Create account. Stop. No form submitted. |

No cookie dialog rendered. No captcha wall rendered on the marketing pages. The site is not parked.
