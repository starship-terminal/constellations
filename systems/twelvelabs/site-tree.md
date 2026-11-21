# TwelveLabs site tree

Mapped 2026-11-20 from the live site, starting at `https://playground.twelvelabs.io/` and then `https://www.twelvelabs.io/`. Controls were opened in the T3 preview (profile `default`) and the destination was read from the link or the page that loaded. The English sitemap (`/sitemap_en.xml`, 309 URLs) confirms the public tree. Blog posts, webinars, guides, partner landings and legal archives are leaves, not captured one by one.

## Entry

| Control | Opens | Result |
|---|---|---|
| `https://playground.twelvelabs.io/` | Auth0 login on `auth.twelvelabs.io` | Login wall. Email address, Continue, Sign up, Continue with Google. Not signed in. Stopped. |
| Logo (wordmark) | `https://www.twelvelabs.io/` | Marketing home |
| Hamburger (top right, 28 px icon) | Full-screen menu overlay | Sections below. Close returns to the page. |
| Try Free (hero, menu, and repeated CTAs) | `https://auth.twelvelabs.io/u/login` | Same login wall |
| Talk to Sales | `/contact` | Sales form. Fields left blank. |
| Cookie preferences (Osano, bottom right) | Cookie preferences panel | Necessary / analytics consent. Not submitted. |

The marketing site paints a near-black page. The menu overlay paints a light grey panel. No theme switch was found on the public site.

## Menu

The hamburger opens six sections. Each label expands in place.

### Platform

| Control | Opens |
|---|---|
| Platform Overview | `/product/product-overview` |
| Jockey | `/jockey` |
| Models Overview | `/product/models-overview` |
| Marengo | `/marengo` |
| Pegasus | `/pegasus` |
| Search | `/product/video-search` |
| Analyze | `/product/analyze` |
| Embed | `/product/embed` |

### Pricing

| Control | Opens |
|---|---|
| Pricing | `/pricing` |
| Pricing Calculator | `/pricing-calculator` |

### Solutions

| Control | Opens |
|---|---|
| Overview | `/solutions` |
| Media & Entertainment | `/solutions/media-and-entertainment` |
| Advertising | `/solutions/advertising` |
| Physical AI | `/solutions/physical-ai` |
| Government | `/solutions/government` |
| Case Studies | `/case-studies` |
| Enterprise Overview | `/enterprise` |

Sitemap also lists `/solutions/news-and-broadcasting`, `/solutions/marketing-and-social`, `/solutions/sports-and-broadcasting`, `/solutions/security`. Those were not in the expanded menu on this visit.

### Build

| Control | Opens |
|---|---|
| Developer Hub | `/developer-hub` |
| SDKs | `https://docs.twelvelabs.io/docs/resources/twelve-labs-sd-ks` |
| Discord | `https://discord.com/invite/mwHQKFv7En` (left the product) |
| Sample Apps | `/sample-apps` |
| Research | `/research` |

### Resources

Footer and sitemap, not fully expanded in the menu before a mis-click left the overlay:

| Control | Opens |
|---|---|
| Blog | `/blog` |
| Guides | `/guides` |
| Webinars | `/webinars` |
| Newsletter | `/newsletter` |
| Press | `/press` |

### Company

| Control | Opens |
|---|---|
| About Us | `/about-us` |
| Careers | `/careers` |
| Partners | `/partners` |
| Security | `/security` |
| Compliance | `/compliance` |
| Legal | `/legal` |

### Language

The globe combobox offers English (selected) and Korean. Korean was not selected. The Korean tree is `/sitemap_ko-KR.xml`.

## Home page, below the menu

| Control | Opens |
|---|---|
| Jockey card ("New") | `/jockey` |
| Developer Hub | `/developer-hub` |
| Learn more (Infrastructure) | `https://docs.twelvelabs.io/v1.3/docs/resources/platform-overview` |
| API + SDK, MCP, Integrations | In-page tabs on the home infrastructure block |
| Footer columns | Same product, solutions, company and legal URLs as the menu |

## Docs (`docs.twelvelabs.io`)

A separate Fern docs site. Reached from SDKs and from Learn more. Its own sidebar covers get started, guides, resources, advanced, and API reference. Treated as a second surface, not the marketing tree.

## Playground and signed-in app

`playground.twelvelabs.io` redirects to the login wall. No post-auth screen was reached. See `login-review.json`.
