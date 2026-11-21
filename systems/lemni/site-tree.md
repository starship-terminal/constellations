# Lemni public site tree

Mapped from https://www.lemni.com/ on 2026-11-21, signed out, before the screenshot pass. The request returned 200. The page title was "Lemni · Set up custom Ai agents in minutes". This is a live marketing site, not a parked domain.

The marketing site is Framer on `www.lemni.com`. The account shell is a separate page at `https://lemni.com/signin`. `/signup` redirects there. There is no theme switch. Home and changelog paint dark (`rgb(13, 13, 18)`). Pricing, docs, blog, company, brand, support, privacy, terms, and the sign-in shell paint light (`rgb(246, 246, 248)`).

No email was typed. No password was typed. No code was typed. No form was submitted. Continue with Google was not clicked. Continue and Try For Free were not followed into a signed-in app.

## Header

The wordmark and six items sit in a 50 px bar. They are links, not flyouts. Hovering a label did not open a menu.

| Control | Opens | Stop? |
|---|---|---|
| Lemni (wordmark) | `/` | |
| Docs | `/docs` | |
| Blog | `/blog` | |
| Company | `/company` | |
| Community | `https://community.lemni.com` | Stop. TLS failed (`ERR_SSL_VERSION_OR_CIPHER_MISMATCH`). Not opened further |
| Pricing | `/pricing` | |
| Continue | `https://lemni.com/signup`, which redirects to `https://lemni.com/signin` | Stop. Empty wall only |

On a 390-wide viewport the labels collapse. An unnamed icon at the right of the bar (`data-framer-name="Icon"`, 44 px) opens a drawer. Escape closes it.

## Mobile drawer

| Control | Opens | Stop? |
|---|---|---|
| Docs | `/docs` | |
| Blog | `/blog` | |
| Company | `/company` | |
| Community | `https://community.lemni.com` | Stop. Not followed |
| Pricing | `/pricing` | |
| Continue | `https://lemni.com/signup` | Stop. Empty wall only |

## Homepage

The page is one long dark page. There is no dialog on load.

| Control | Opens | Stop? |
|---|---|---|
| Continue (hero) | `https://lemni.com/signup` | Stop. Not followed |
| Watch Video | A YouTube embed overlay on the same page (`youtube.com/embed/dbAMT3icCac`). Close is a 40 px graphic at the top right. Escape also closes it | Opened, then closed. Not a new page |
| Read | `/blog/pre-seed-announcement` | |
| Continue (bottom) | `https://lemni.com/signup` | Stop. Not followed |

The product tiles (Inbox, Agents, Knowledge, Actions) are painted demos on the page. They are not links into the app. Sample names in those demos (Jane Doe, Trevor Amro, and the rest) are the site's own copy.

## Docs

`/docs` is the docs index. The section row and the side list are links, not tabs that stay on one URL.

| Control | Opens | Stop? |
|---|---|---|
| Basics / Overview of Lemni | `/docs` | |
| Knowledge | `/docs/knowledge` | |
| Agents | `/docs/agents` | |
| Actions | `/docs/actions` | |
| Inbox | `/docs/inbox` | |
| Overview, Workplace, Members, Connections, Usage, Plans | Anchors on the current docs page (`#overview`, `#workplace`, and the rest) | |

## Blog

| Control | Opens |
|---|---|
| Our vision for a new customer experience | `/blog/vision` |
| Lemni raises $3,5M led by Sequoia | `/blog/pre-seed-announcement` |

## Company

| Control | Opens | Stop? |
|---|---|---|
| Staff handles (`@krijnrijshouwer` and the rest) | `https://x.com/...` | Off-site. Not opened |
| Read our vision | `/blog/vision` | |
| Web Designer | `/company/web-designer` | |
| Junior Design Engineer | `/company/jr-design-engineer` | |
| Senior Design Engineer | `/company/sr-design-engineer` | |
| Junior Product Engineer | `/company/jr-product-engineer` | |
| Senior Product Engineer | `/company/sr-product-engineer` | |
| Open application | `/company/apply` | Stop. Empty form photographed only. Not filled. Not submitted |
| Investor and backer marks | Sequoia, X, LinkedIn, and other off-site profiles | Not opened |

## Pricing

| Control | Opens | Stop? |
|---|---|---|
| Try For Free | `https://lemni.com/signup` | Stop. Not followed |
| FAQ questions | Same page. The click on "How do the subscription add-ons work?" removed that row and left the others closed. No separate answer panel opened | |

There is no monthly/yearly switch on the page. The price shown is `$196` struck and `$98` / month.

## Changelog

`/changelog` paints dark, like home. Follow opens `https://x.com/lemni` and was not opened. An email field (`name@email.com`) and a submit control sit on the page. Nothing was typed. Nothing was submitted.

## Support

`/support` is a public FAQ. `support@lemni.com` is a `mailto:` link and was not opened. The questions are on the page. They did not open a dialog.

## Brand, privacy, terms

| Page | What it is |
|---|---|
| `/brand` | Logo and product-shot downloads. No account |
| `/privacy` | Privacy statement. `support@lemni.ai` is a mailto link. Not opened |
| `/terms` | Terms. Public |

## Footer band

The page has no `footer` element. The bottom band is a row of links.

| Group | Items |
|---|---|
| Product | Home, Docs, Changelog, Pricing |
| Resources | Company, Blog, Community, Support, Brand |
| Legal | Privacy, Terms |
| Social | X (`https://x.com/lemni`), GitHub (`https://github.com/lemni`), LinkedIn (`https://www.linkedin.com/company/lemni` on most pages; the home and changelog band pointed at `https://www.linkedin.com/company/input` on this visit), YouTube |

Social links were not opened.

## Login and signup walls

`/signup` and `/signin` both land on `https://lemni.com/signin`. Title: "Lemni". The form is empty.

| Control | What it is | Stop? |
|---|---|---|
| Continue with Google | Identity provider | Not clicked |
| Email | Empty field, placeholder "Email…" | Nothing typed |
| Continue | Submits the email | Not clicked |
| Privacy | `/privacy` | |
| Terms | `/terms` | |

There is no separate signup form. `/login` did not load a page (the navigation ended on a browser error page). `/register` redirected toward `/login` and did not show a form.

## Not entered

The workplace app (inbox, agents, knowledge, actions, settings, upgrade) sits behind the sign-in wall. This pass stopped at the empty wall. `login-extracted` stays `not-started`.

The application form at `/company/apply` asks for a name, an email, a role, a country, and profile URLs. It was left empty.

`https://community.lemni.com` failed TLS and was not captured.
