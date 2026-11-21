# Relume public site tree

Mapped on 2026-11-21 from the live site before screenshots, in headless Chromium at 1440×900 (and 390×844 for the phone menu). `https://www.relume.io/` redirects to `https://www.relume.ai/`. English (`en-US`) is the captured locale. Japanese (`/ja/`), German (`/de/`), French (`/fr/`) and Spanish (`/es/`) are the same pages in another language and are not a separate surface.

Nothing in this tree was submitted. Login, signup, Google, SSO, contact, affiliate and newsletter fields were not typed.

## Shell

| Control | Opens | Stop? |
|---|---|---|
| Logo "Relume home" | `/` | No |
| Products (button, `aria-expanded`) | Dropdown menu `#w-dropdown-list-0` (`.navbar5_dropdown-list.w--open`) | No |
| Products → Publish | `/publish` | No |
| Products → Studio | `/studio` | No |
| Products → Export | `/export` | No |
| Products → Relume MCP | `/mcp` | No |
| Products → React Library | `/react/components` | No |
| Products → featured What's New card | `/whats-new/custom-components` | No |
| Products → View All | `/whats-new` | No |
| Pricing | `/pricing` | No |
| Contact Sales | `/contact-sales` (sales form: name, phone, job, company, country, email) | Do not type. Do not submit. |
| Component Voting | `/component-voting` | No |
| Learn | `/resources/publish/docs` | No |
| Switch to dark theme | Stays on the page. Sets `data-theme="dark"` and `body.p-theme-dark`. Page background goes from `rgb(241, 240, 238)` to `rgb(16, 16, 16)`. | No. Local theme only. |
| Log in | `/app/login` | Wall. Stop. |
| Start for free | `/app/signup` | Wall. Stop. |
| Open menu (phone, `aria-controls="w-nav-overlay-0"`) | Full-screen nav overlay with the same product links, Pricing, Contact Sales, Component Voting, Learn, Log in, Start for free | No, until a link hits a wall |
| Cookie banner (Finsweet `fs-cc`) | Cookie Settings, Accept Cookies, Reject all cookies, Allow all cookies, Cancel, Save | Hidden. Never clicked. |
| Cookie Settings | Cookie preference dialog (personalization, marketing, analytics checkboxes, Cancel, Save) | Do not save. |
| Open Intercom Messenger | Chat widget | Not opened. |

## Walls (recorded, branch stopped)

| URL | What is on screen | Why the branch stops |
|---|---|---|
| `https://www.relume.ai/app/login` | "Welcome back". Email, password, Show password, Continue, Forgot password, Continue with Google, Continue with SSO, Sign up. Cloudflare Turnstile is in the DOM. | Known login wall. Password was not submitted. Google and SSO were not clicked. |
| `https://www.relume.ai/app/signup` | "Your AI Sitebuilder". Email field, Continue, Continue with Google, link to Sign in. | Signup wall. Email was not typed. |
| `https://www.relume.ai/app` | Launch Builder. Not followed past the auth host. | Assumed app shell. Stop. |
| `https://www.relume.ai/app/template/<id>` | Clone site. Three homepage cards. | App route. Stop. |
| `https://www.relume.ai/app/manage-account/plan` | Manage Billing / Upgrade. | Account. Stop. |
| `https://www.relume.ai/app/mcp` | Linked from the Studio demo. | App route. Stop. |
| `https://www.relume.ai/dashboard` | Linked from Studio demo and the library account menu. | App route. Stop. |
| `https://www.relume.ai/sites` | Linked from the Studio demo. | App route. Stop. |
| Generate Website / Generate | Homepage and product heroes. Would start a generation or an account flow. | Not clicked. |
| Attach files | Homepage composer. | Not clicked. |
| Try an example | Homepage composer. Fills the prompt. | Not clicked (it is a generation start). |
| Continue with Google / Continue with SSO | Login and signup. | Not clicked. |

## Marketing pages (public)

Each row is a page the header, Products menu, or footer opens. Theme toggle is on the shell of each marketing page.

| Page | URL | Extra controls on the page |
|---|---|---|
| Home | `/` | Hero composer (not used). Embedded product demos (Publish editor, Studio). "Open live site" goes to `*.relumesite.ai` published examples. "Clone site" is an app wall. |
| Publish | `/publish` | Same hero. Embedded editor demo: component options, style guides (Threshold, Traverse, Atelier), colour schemes, project chrome. Those controls sit inside a marketing demo, not the signed-in app. |
| Studio | `/studio` | A public demo of the Studio app: sidebar (Styles, Characters, Scenes, Upscaler), appearance toggle, model / aspect / versions / resolution menus, Spotlight sort, like and image actions. "Unlock Studio with Pro" and Upgrade go toward the app. Profile links under `/studio/profiles/` are public creator pages. |
| Export | `/export` | Product story. Generate Website is not clicked. |
| Relume MCP | `/mcp` | Product story. |
| Library MCP | `/library-mcp` | Copy URL buttons (clipboard only; not treated as a form). |
| Whitelabel | `/whitelabel` | Embedded editor demo, same style-guide and scheme controls as Publish. |
| Claude Design Export | `/claude-design-export` | Product story. |
| Chrome Extension | `/chrome-extension` | Product story. External Chrome Web Store link is not the product UI. |
| Style Guide | `/style-guide` | Marketing page for the Client-First style guide. |
| Figma Kit | `/figma-library` | Marketing page. External Figma link is not the product UI. |
| Pricing | `/pricing` | Tabs: Publish pricing (selected), Export pricing. Yearly billing control (`aria-label="Yearly billing discount"`). Page-views control (`aria-label="Monthly page views"`). Plan CTAs that go to `/app/signup` or `/app/manage-account/plan` are walls. |
| What's New index | `/whats-new` | Cards to individual release notes. |
| What's New article | `/whats-new/custom-components` (featured). Sitemap lists 40 more `/whats-new/*` notes. | Article. |
| Community Love | `/community-love` | Testimonials. Some names link to `#` or external sites. |
| Showcase | `/showcase` | Tabs: Recent, Highlights. Author menus (names are published credits). |
| Inspiration | `/inspiration` | Feed. "Build it" menus. Sitemap also has `/inspirations/<slug>` (111). |
| Component Voting | `/component-voting` | Voting UI. Votes were not cast. |
| Support | `/support` | Help links. Intercom not opened. |
| Affiliates | `/affiliates` | Application form (name, email, country, channel). Not filled. Not submitted. |
| Guides | `/guides` | Index of public website guides. |
| Legal | `/legal/privacy-policy`, `/legal/terms`, `/legal/licensing-agreement`, `/legal/cookie-policy` | Static pages. |

Footer columns repeat the product links above, plus Community Love, Showcase, Inspiration, Slack (`community.relume.io`, `slack.relume.ai`), Hire an Expert (contra.com, external), Become an Affiliate, Careers (`mailto:`, not opened), Support, Relume API Docs (`https://apis.relume.io/publish/docs`, separate host), and the legal links. Social links (X, YouTube, TikTok, Instagram, LinkedIn, Webflow, Figma) leave the product.

## Libraries (public catalogs)

| Control | Opens |
|---|---|
| Relume Library / Webflow Library | `/components` |
| React Library | `/react/components` |
| Preferences (Webflow only) | Dropdown: Relume Style Guide V3 / V2 / V1.5, Finsweet Style Guide. Local filter. |
| Layout, Elements, More Filters | Filter menus on both libraries. |
| Category chips and cards | `/categories/<slug>` (Webflow) and `/react-categories/<slug>` (React). Sitemap: 50 of each. |
| A component card | `/components/<slug>` or a React equivalent. Sitemap: 1,758 Webflow components and 1,524 React components. One sample, `/components/application-shell-1`, loaded as a public detail page. |
| Search | `/search` redirects to `/components`. |
| Related indexes | `/application-components`, `/marketing-components`, `/ecommerce-components`, `/site-components`, `/free-components`, `/page-templates`, `/ui-elements`, `/color-palettes`, `/new-components`, `/folder` |

The catalogs are the same UI repeated across thousands of slugs. Capture uses the index, one category, one detail, and the filter menus. It does not screenshot every slug.

## Docs

| Control | Opens |
|---|---|
| Learn, and the footer guide links | `/resources/publish/docs` |
| Home / Getting Started / FAQs | `/resources/publish/docs`, `/resources/publish/getting-started`, `/resources/publish/publish-faqs` |
| English | Language menu: Deutsch `/de/...`, Française `/fr/...`, Español `/es/...` |
| Sidebar articles | `/resources/publish/doc/<slug>` (getting started, wireframes, sitemap, CMS, MCP, domain, forms, and the rest of the sidebar) |
| Category hubs | `/resources/publish/publish-categories/<slug>` |
| open lightbox | Image lightbox on a doc page |
| Watch Video | `#` on the docs home |

One article, `/resources/publish/doc/getting-started-with-relume-publish`, is the representative doc page. The sidebar is the same chrome on every article.

## Homepage demos (not the app)

The homepage and `/publish` embed a fake editor. Its buttons (Component options, style guides, colour schemes, project menu, Select / Pan / Comment, Desktop / Tablet / Mobile, Preview, Analytics) change the demo. They do not open the signed-in builder. Capture treats them as public demo states.

## Not in the English marketing tree

Sitemap-only campaign landings (`/dental-websites`, `/lawyer-websites`, `/plumbing-websites`, and the `expert-*` / `*-relume-builds` variants, `/hipages`, `/howdy`, `/contra`, `/webflow`, `/money-makers`, `/landing-review`) are public ads, not linked from the main nav. They are listed as reachable from the sitemap and not walked as primary states.

`/ja/` mirrors the library and pricing. It is a locale, not a new product surface.
