# Dub public site tree

Mapped 2026-11-21 from [https://dub.co/](https://dub.co/) in headless Chromium (Playwright). Desktop is 1440×900. Phone is 390×844. Controls were hovered or opened. No form was submitted. No email was typed. Google, GitHub, and SAML SSO were not clicked. Cookie overlays were hidden, never accepted.

The sitemap lists 357 `dub.co` URLs: product pages, tools, legal pages, blog posts, changelog entries, customer stories, marketplace listings, and integrations. This tree records the control that opens each kind of page, and where a branch stops. Catalog posts, listings, and stories are one pattern each, not 300 separate walks.

Signed-in app is out of scope. Login and signup walls were loaded and stopped.

## Homepage header (desktop)

Sticky bar. Hover opens a menu (`aria-expanded` becomes true). A click on the same button closes it.

| Control | Opens |
|---|---|
| Wordmark | `/home` |
| Product (`aria-controls` ends in `-content-Product`) | Mega menu. Not a page. Links below. |
| Solutions (`aria-controls` ends in `-content-Solutions`) | Mega menu. Links below. |
| Resources (`aria-controls` ends in `-content-Resources`) | Mega menu. Links below. |
| Customers | `/customers` |
| Pricing | `/pricing` |
| Log in | `https://app.dub.co/login`. Auth wall. Stop. |
| Sign up | `https://app.dub.co/register`. Signup wall. Stop. |

No language control and no theme control sit in this header. Marketing pages paint light only. Search is not in this header.

Shot: [home-light-default.png](screenshots/home-light-default.png). Menus: [home-light-menu-product.png](screenshots/home-light-menu-product.png), [home-light-menu-solutions.png](screenshots/home-light-menu-solutions.png), [home-light-menu-resources.png](screenshots/home-light-menu-resources.png).

### Product menu

Opened by hover, 2026-11-21.

| Label | Opens |
|---|---|
| Dub Partners | `/partners` |
| Dub Analytics | `/analytics` |
| Dub Links | `/links` |
| Dub Integrations | `/integrations` |
| Dub API & MCP | `/docs/api-reference/introduction` |

Cards inside the panel show sample names and a sample address. Those are the product's published demo, not this capture's account.

### Solutions menu

Opened by hover, 2026-11-21. Three columns: Use case, Stage, SDKs.

| Label | Opens |
|---|---|
| Affiliate Management | `/partners` |
| Marketing Attribution | `/analytics` |
| For Content Creators | `/solutions/creators` |
| Enterprise | `/enterprise` |
| Startups | `/startups` |
| Typescript | `/sdks/typescript` |
| Python | `/sdks/python` |
| Go | `/sdks/go` |
| Ruby | `/sdks/ruby` |
| PHP | `/sdks/php` |

The sitemap also lists `/solutions/typescript`, `/solutions/python`, `/solutions/go`, `/solutions/ruby`, and `/solutions/php`. The menu links to `/sdks/<language>`, not those `/solutions/` paths.

### Resources menu

Opened by hover, 2026-11-21. Columns: Help and support, Company, Updates, plus a Program Marketplace row.

| Label | Opens |
|---|---|
| Docs | `/docs` |
| Help Center | `/help` |
| Contact | `/contact` (redirects to `/contact/support`) |
| About | `/about` |
| Careers | `/careers` |
| Dub Brand | `/brand` |
| Blog | `/blog` |
| Changelog | `/changelog` |
| Program Marketplace | `/marketplace` |

## Homepage body

| Control | Opens |
|---|---|
| Introducing our Startup Program | `/startups` |
| Start for free | `https://app.dub.co/register`. Signup wall. Stop. |
| Get a demo | `/contact/sales` |
| Affiliate Programs (tab) | In-page demo. Does not navigate. |
| Conversion Analytics (tab) | In-page demo. |
| Short Links (tab) | In-page demo. Shot: [home-light-tab-links.png](screenshots/home-light-tab-links.png). |

The panel under the tabs is a published product demo, not the signed-in workspace.

## Phone bar and drawer (390)

Bar: wordmark (`/home`), Log in (`https://app.dub.co/login`, stop), Sign Up (`https://app.dub.co/register`, stop), hamburger (icon button, no accessible name, top right). Close is an X in the drawer.

Opened 2026-11-21 by clicking the hamburger. Shot: [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). Closed bar: [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

| Drawer row | Opens |
|---|---|
| Product | In-drawer list. Shot: [mobile-home-light-menu-product.png](screenshots/mobile-home-light-menu-product.png). |
| Solutions | In-drawer list. Shot: [mobile-home-light-menu-solutions.png](screenshots/mobile-home-light-menu-solutions.png). |
| Resources | In-drawer list. Shot: [mobile-home-light-menu-resources.png](screenshots/mobile-home-light-menu-resources.png). |
| Customers | `/customers` |
| Pricing | `/pricing` |
| Enterprise | `/enterprise` |
| Startups | `/startups` |

Phone Product rows: Dub Partners (`/partners`), Dub Analytics (`/analytics`), Dub Links (`/links`), Dub API (`/docs/api-reference/introduction`), Dub Integrations (`/integrations`).

Phone Solutions rows: Affiliate Management (`/partners`), Marketing Attribution (`/analytics`), For Content Creators (`/solutions/creators`), then SDKS: Typescript, Python, Go, Ruby, PHP (`/sdks/<language>`). Enterprise and Startups stay as their own drawer rows, not inside this list.

Phone Resources rows: Docs (`/docs`), Help Center (`/help`), About (`/about`), Careers (`/careers`), Blog (`/blog`), Changelog (`/changelog`), Dub Brand (`/brand`), Contact (`/contact`), Program Marketplace (`/marketplace`).

## Footer

Same shell on marketing pages. Social marks leave `dub.co`.

| Control | Opens |
|---|---|
| Dub logo | `https://dub.co/` |
| Twitter | `https://twitter.com/dubdotco`. Other host. Stop. |
| LinkedIn | `https://www.linkedin.com/company/dubinc`. Other host. Stop. |
| GitHub | `https://github.com/dubinc/dub`. Other host. Stop. |
| YouTube | `https://www.youtube.com/@dubdotco`. Other host. Stop. |
| Dub Partners | `/partners` |
| Dub Analytics | `/analytics` |
| Dub Links | `/links` |
| Dub API | `/docs/api-reference/introduction` |
| Marketing attribution | `/analytics` |
| Content creators | `/solutions/creators` |
| Affiliate management | `/partners` |
| Docs | `/docs` |
| Help Center | `/help` |
| Enterprise | `/enterprise` |
| Startups | `/startups` |
| Integrations | `/integrations` |
| Pricing | `/pricing` |
| Affiliates | `https://partners.dub.co/dub`. Other host. Stop. |
| About | `/about` |
| Blog | `/blog` |
| Careers | `/careers` |
| Changelog | `/changelog` |
| Customers | `/customers` |
| Brand | `/brand` |
| Contact | `/contact` |
| Privacy | `/privacy` (lands on `/legal/privacy`) |
| Rewardful | `/blog/dub-vs-rewardful` |
| PartnerStack | `/compare/partnerstack` |
| FirstPromoter | `/blog/dub-vs-firstpromoter` |
| Tolt | `/blog/dub-vs-tolt` |
| Bitly | `/compare/bitly` |
| Rebrandly | `/compare/rebrandly` |
| Short.io | `/compare/short` |
| Bl.ink | `/compare/blink` |
| All systems operational | `https://status.dub.co/`. Other host. Stop. |
| SOC 2 mark | `/blog/soc2` |
| Tools (button, `aria-expanded`) | In-page list. Not a page. |
| Legal (button, `aria-expanded`) | In-page list. Not a page. |

Shots: [home-light-footer-tools.png](screenshots/home-light-footer-tools.png), [home-light-footer-legal.png](screenshots/home-light-footer-legal.png).

### Tools list

Opened by clicking Tools, 2026-11-21.

| Label | Opens |
|---|---|
| Affiliate Program Terms Generator | `/tools/affiliate-terms-generator` |
| UTM Builder | `/tools/utm-builder` |
| QR Code API | `/tools/qr-code` |
| Spotify Link Shortener | `/tools/spotify-link-shortener` |
| ChatGPT Link Shortener | `/tools/chatgpt-link-shortener` |
| GitHub Link Shortener | `/tools/github-link-shortener` |
| Calendar Link Shortener | `/tools/cal-link-shortener` |
| Google Link Shortener | `/tools/google-link-shortener` |
| Amazon Link Shortener | `/tools/amazon-link-shortener` |
| Figma Link Shortener | `/tools/figma-link-shortener` |
| Link Inspector | `/tools/inspector` |

The sitemap also lists `/tools`, `/tools/google-docs-link-shortener`, `/tools/google-drive-link-shortener`, `/tools/google-forms-link-shortener`, `/tools/google-sheets-link-shortener`, `/tools/google-maps-link-shortener`, and `/tools/youtube-link-shortener`. Those were not in the expanded footer list on this pass. `/tools` itself is a public index. Shot: [tools-light-default.png](screenshots/tools-light-default.png).

UTM Builder fields (Destination URL, Source, Medium, Campaign, Term, Content, Referral) and the Shorten URL button were not filled and not submitted. QR Code fields and Save changes were not submitted.

### Legal list

Opened by clicking Legal, 2026-11-21.

| Label | Opens |
|---|---|
| Affiliate Program Terms | `/legal/affiliates` |
| DPA | `/legal/dpa` |
| Partner Terms | `/legal/partners` |
| Privacy Policy | `/legal/privacy` |
| Report Abuse | `/legal/abuse` |
| SLA | `/legal/sla` |
| Subprocessors | `/legal/subprocessors` |
| Terms of Service | `/legal/terms` |

The sitemap also lists `/legal/stand-down-policy`. It was not in the expanded list. Terms shot: [legal-terms-light-default.png](screenshots/legal-terms-light-default.png).

## Product pages the header and footer open

Each of these loaded signed out on 2026-11-21. Primary actions that leave for the app are recorded and not followed past the wall.

| Page | In-page controls | Where they go |
|---|---|---|
| `/links` | Start for free, View plans, Shorten link, Copy, Show QR Code | Register wall, `/pricing/links`, in-page demo. Shorten link was not submitted. |
| `/analytics` | Marketing page | [analytics-light-default.png](screenshots/analytics-light-default.png) |
| `/partners` | Marketing page | existing [partners-light-default.png](screenshots/partners-light-default.png) |
| `/pricing` | Monthly, Yearly | In-page billing toggle. Yearly shot: [pricing-light-yearly.png](screenshots/pricing-light-yearly.png). Start 14-day trial goes to the register wall. Get a demo goes to `/contact/sales`. |
| `/customers` | Story cards, category tabs (Featured, AI, SaaS, DevTool, Creative, Consumer, Education, Health) | `/customers/<slug>` and in-page filters. One story pattern. |
| `/enterprise` | Get a demo | `/contact/sales` |
| `/startups` | Apply in 3 minutes | In-page `#apply`. The form was not filled and not submitted. Shot: [startups-light-default.png](screenshots/startups-light-default.png). |
| `/solutions/creators` | Marketing page | public |
| `/integrations` | Category tabs (All, Payments, Automation, Analytics, Support, Authentication, Social Media, Productivity, Scheduling, CMS) | In-page filter. Cards open `/integrations/<slug>`. Shot: [integrations-light-default.png](screenshots/integrations-light-default.png). |
| `/marketplace` | Category links | `/marketplace/c/<category>` and `/marketplace/<listing>`. One listing pattern. Shot: [marketplace-light-default.png](screenshots/marketplace-light-default.png). |
| `/compare/bitly` | Comparison table | public. Other compare slugs: partnerstack, rebrandly, short, blink. |
| `/about` | View all customers, case-study cards | `/customers` and `/customers/<slug>`. Shot: [about-light-default.png](screenshots/about-light-default.png). |
| `/careers` | View open roles | In-page `#open-roles`. Role pages `/careers/general-application` and `/careers/staff-software-engineer` are application forms. Not filled. Not submitted. Shot: [careers-light-default.png](screenshots/careers-light-default.png). |
| `/brand` | Download brand kit, in-page anchors, Download | `https://d.to/brand-kit` and `https://assets.dub.co/brand/*.svg`. Asset host. Not downloaded. Shot: [brand-light-default.png](screenshots/brand-light-default.png). |
| `/contact` | Redirect | Lands on `/contact/support`. |
| `/contact/sales` | Work email, How can we help?, Send message | Form. Not filled. Not submitted. |
| `/sdks/typescript` | SDK page | Same pattern for python, go, ruby, php. Shot: [sdks-typescript-light-default.png](screenshots/sdks-typescript-light-default.png). |

## Blog, changelog, customers, authors

| Control | Opens |
|---|---|
| Blog category: Overview | `/blog` |
| Company News | `/blog/category/company` |
| Education | `/blog/category/education` |
| Engineering | `/blog/category/engineering` |
| Customer Stories | `/blog/category/customers` |
| Changelog (blog nav) | `/changelog` |
| A post card | `/blog/<slug>` |
| Changelog Follow | `https://twitter.com/dubdotco`. Other host. Stop. |
| Changelog feed icon | `/atom` |
| A changelog row | `/changelog/<slug>` |
| A customer card | `/customers/<slug>` |
| An author link on a post | `/authors/<slug>` |

Sitemap counts on 2026-11-21: 64 blog URLs, 103 changelog URLs, 20 customer URLs, 9 author URLs. One of each pattern was confirmed by loading the index. Individual posts were not each photographed.

## Docs and help

Mintlify shell on `/docs` and `/help`. This is the only public theme control.

| Control | Opens |
|---|---|
| Dub home page | `https://dub.co/home` |
| Search (`button[aria-label="Open search"]`, label "Search... ⌘K") | In-page search dialog. Placeholder "Search...". Escape closes it. No query was typed. Shots: [docs-light-search.png](screenshots/docs-light-search.png), [help-light-search.png](screenshots/help-light-search.png). |
| Contact support | `/contact/support` |
| Dashboard | `https://app.dub.co/register`. Signup wall. Stop. |
| Change theme preference | Menu: System, Light, Dark. Dark applies `html.dark`. Shot of the menu: [docs-light-theme-menu.png](screenshots/docs-light-theme-menu.png). Dark page: [docs-dark-default.png](screenshots/docs-dark-default.png). |
| Developer Docs | `/docs` |
| Help Center | `/help` |
| API Reference | `/docs/api-reference/introduction` |
| Webhooks | `/docs/webhooks/introduction` |
| Sidebar group (Web installation, Mobile installation, and the same chevron rows) | In-page expand. Not a navigation. |
| Sidebar link | `/docs/<path>` or `/help/article/<slug>` |
| On this page | In-page `#` anchors |
| Copy page | Copies the page. Not a navigation. |
| More actions | Menu: Copy page, View as Markdown, Open in ChatGPT, Open in Claude, Connect to Cursor, Connect to VS Code. Those last four leave for another product. Not clicked. Shot: [docs-light-more.png](screenshots/docs-light-more.png). |
| Help sidebar groups (Getting started, Rewards and commissions, Recruiting partners, Managing partners, Sending payouts, Engaging partners, Insights and reporting, Migration guides, Joining programs, Receiving payouts, Links, Analytics, Custom domains, Additional guides) | In-page expand, then `/help/article/<slug>` |
| Help Send message | Support widget. Not opened. Not submitted. |

`/llms.txt` is linked from a docs index banner. It is a text catalog of doc URLs, not a screen.

Phone docs default: [mobile-docs-light-default.png](screenshots/mobile-docs-light-default.png). Phone docs search was attempted from the same Open search button.

## Login and signup walls

Loaded, not submitted. The email field was left empty in the filed shots. Identity providers were not clicked.

| Control | Result |
|---|---|
| `https://dub.co/login` | Redirects to `https://app.dub.co/login`. Stop. |
| `https://dub.co/register` | Redirects to `https://app.dub.co/register`. Stop. |
| Log in with email | Would submit. Not clicked. |
| Sign Up | Would submit. Not clicked. |
| Continue with Google | Identity provider. Not clicked. |
| Continue with GitHub | Identity provider. Not clicked. |
| Continue with SAML SSO | Identity provider. Login only. Not clicked. |
| Sign up / Log in (cross link) | The other wall. Stop. |
| Log in at partners.dub.co | `https://partners.dub.co/login`. Other host. Stop. |
| Sign up at partners.dub.co | `https://partners.dub.co/register`. Other host. Stop. |
| Terms of Service | `https://dub.co/legal/terms` |
| Privacy Policy | `https://dub.co/legal/privacy` |
| Read more | `https://dub.co/customers/framer` |
| Show Framer / Show Wispr Flow / Show Chatbase / Show Tella | In-page testimonial switch on the wall. |

Shots of the empty walls: [login-light-wall.png](screenshots/login-light-wall.png), [register-light-wall.png](screenshots/register-light-wall.png).

Nothing was submitted. No password was typed. No code was sent. No account was created. The signed-in workspace was not entered.

## Cookie dialog

No cookie or consent dialog was visible on the pages loaded on 2026-11-21. The capture script still hides a dialog whose text matches cookie or consent, and does not click Accept or Reject. No such control was used because none was on screen.

## Stops

| Branch | Why it stops |
|---|---|
| `app.dub.co/login` and `app.dub.co/register` | Auth wall. Empty form only. |
| Google, GitHub, SAML SSO | Identity provider. Not clicked. |
| `partners.dub.co` | Other host. |
| `status.dub.co` | Other host. |
| Twitter, LinkedIn, GitHub, YouTube | Other host. |
| `d.to` and `assets.dub.co` brand downloads | Short-link and asset hosts. Not followed. |
| ChatGPT, Claude, Cursor, VS Code from docs More actions | Other product. Not clicked. |
| Careers applications, sales form, startup apply, UTM Shorten URL, QR Save changes | Forms. Not submitted. |
| Signed-in workspace | Not in this pass. |
