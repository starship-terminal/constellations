# Raster public site tree

Mapped from https://raster.app/ on 2026-11-21, signed out, in an incognito preview tab. The homepage returned a live title, "Raster - The agent-native DAM for teams that ship". `html` carried class `dark` and `color-scheme: dark`. This is a live marketing site, not a parked domain.

T3 `preview_snapshot` failed twice with "The browser is not producing screenshot frames." The tree was read from the DOM. The shots were taken with headless Playwright after that.

No email was typed. No password was typed. No code was typed. No phone was typed. No address was typed. No form was submitted. Continue with Google was not clicked. Email link to sign in was not clicked. No checkout was started.

## Header (desktop, 1440)

The wordmark, Product, Pricing, and Resources sit in the bar. Sign in, Start for free, and Book demo sit on the right. Resources is a hover and focus menu (`group-hover` / `group-focus-within`). It is not a click toggle.

| Control | Opens | Stop? |
|---|---|---|
| Raster (wordmark) | `/` | |
| Product | `/product` | |
| Pricing | `/pricing` | |
| Resources | A panel on the same page: Blog, Design, Docs, Changelog | Photographed open, then left |
| Sign in | `/sign-in` | Stop. Empty wall only |
| Start for free | `/sign-in` | Stop. Empty wall only |
| Book demo | `mailto:support@raster.app` | Not opened |

Resources cards:

| Card | Opens | Copy |
|---|---|---|
| Blog | `/blog` | Product notes, essays, and team updates. |
| Design | `/design` | Raster Neue, colors, components, and craft. |
| Docs | `https://raster.app/docs` (new tab) | API references and implementation guides. |
| Changelog | `/changelog` | Recent product changes and releases. |

## Homepage

The page is one long dark page. There is no dialog on load. The frame under the hero is a `<video>` (`https://rstr.in/raster/website/hkFuWsozH7y`). At capture time it had not painted a frame (`readyState` 0, paused), so the hero frame is black in the shots.

| Control | Opens | Stop? |
|---|---|---|
| Get started | `/sign-in` | Stop. Empty wall only |
| Onboard your agent | A chip on the same page. Click changes the label to "Paste to your agent" and reveals a checkmark. No dialog opened. The text field beside it stayed empty | Nothing was typed. Nothing was pasted |
| Logo row | Off-site customer sites (Vercel, MacStadium, and others) | Not opened |
| Edit, Review, Share, Measure, Connect | Changelog posts (`/changelog/2026-10-09`, `/changelog/2026-10-19`, `/changelog/2026-10-30`, `/changelog/2026-10-21`) | |
| Open gallery | `/s/q7Wm2xKp` | The public share is gone. Photographed the empty state. Not an account |
| Integration cards | Contentful, DatoCMS, Figma, Sanity marketplaces | Off-site. Not opened |
| Build your own with the Raster SDK | `/changelog/2026-10-21` | |
| Changelog cards | `/changelog/2026-11-20`, `/changelog/2026-10-30`, `/changelog/2026-10-23` | |
| View all | `/changelog` | |
| Get started (footer band) | `/sign-in` | Stop |

## Mobile drawer (390)

The labels collapse. A button labelled "Toggle navigation" opens a full-height drawer. A close control sits beside Start for free.

| Control | Opens | Stop? |
|---|---|---|
| Product | `/product` | |
| Pricing | `/pricing` | |
| Blog | `/blog` | |
| Design | `/design` | |
| Docs | `/docs` | |
| Changelog | `/changelog` | |
| Sign in | `/sign-in` | Stop. Empty wall only |
| Start for free | `/sign-in` | Stop |

## Product

`/product` is a public feature page. Sections are Asset management, AI search, Agent workflows, Headless DAM, Image delivery, Integrations, and Collaboration. The library in the hero is a painted demo (search "interior", library names such as Brand and Campaigns).

| Control | Opens | Stop? |
|---|---|---|
| Get started | `/sign-in` | Stop |
| Explore features | `#features` on the same page | |
| Integration cards | Off-site marketplaces | Not opened |

## Pricing

`/pricing` is public. Three columns: Personal (Free, forever), Team ($20 per user, per month), Enterprise (custom). Contact Sales is a mailto. No card form and no checkout button.

| Control | Opens | Stop? |
|---|---|---|
| Get started / Get Started | `/sign-in` | Stop |
| Contact Sales | `mailto:support@raster.app` | Not opened |

## Blog, design, changelog

| Page | What it is |
|---|---|
| `/blog` | "The Raster Journal". Public posts, including `/blog/the-agent-native-dam-is-here` |
| `/design` | Public design playground: Accordion, Avatar, Button, Tag, Color, Form, Tabs, Glass, Icon. Specimens only. Nothing was submitted |
| `/changelog` | Dated public notes. One entry photographed: `/changelog/2026-11-20` |
| `/privacy`, `/terms` | Public legal pages |

## Docs

`/docs` loads dark (`html.dark`). A theme control labelled "Toggle Theme" switches it to `html.light`. Both were photographed. Light was not left as the only record.

| Control | Opens |
|---|---|
| Search | A button labelled Search, shortcut ⌘K. Nothing was typed |
| Guides | A sidebar section |
| API Reference | `/docs/api` |
| Integrations | `/docs/integrations` |
| Organizations & Libraries | `/docs/guides/organizations-and-libraries` |
| Importing Images | `/docs/guides/importing-images` |
| Organizing Images | `/docs/guides/organizing-images` |
| Serving Images | `/docs/guides/serving-images` |
| Open Raster | `https://raster.app` |
| Copy Markdown | Not clicked |
| Open | Not clicked |

## Footer

| Group | Items |
|---|---|
| Product | Overview (`/product`), Asset management, AI search, Agent workflows, Headless DAM |
| Resources | Blog, Docs, Changelog, Pricing, Design system (`/design`) |
| Legal | Privacy Policy (`/privacy`), Terms (`/terms`) |
| Social | X, LinkedIn, Product Hunt |
| Status | `https://status.raster.app/` ("All systems operational") |

X, LinkedIn, Product Hunt, and the status site were not opened.

## Auth wall

| URL | Lands on | What it shows |
|---|---|---|
| `/sign-in` | `/sign-in` | "Sign in to Raster". Continue with Google. Email link to sign in. The email field stays hidden until that button is pressed. It was not pressed. A hidden `cf-turnstile-response` input was present and was not touched |
| `/sign-up` | `/sign-in` | The same empty wall. There is no separate signup form |
| `/signup` | `/sign-in` | The same redirect |
| `/login` | `/sign-in` | The same redirect |
| `/register` | `/sign-in` | The same redirect |
| `/not-a-real-page-raster` | `/sign-in` | Unknown paths redirect to the empty wall. There is no public 404 page |

The email field was empty. Email link to sign in was not clicked. Continue with Google was not clicked. The turnstile was not solved.

## Empty state

The homepage "Open gallery" control points at `/s/q7Wm2xKp`. That public share now says "This shared library is no longer available." It shows no account chrome and no inbox. "Create your own library" points at `/sign-in` and was not followed.
