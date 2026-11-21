# Super.so public site tree

Mapped on 2026-11-21 from the live public site in headless Playwright (desktop 1440x900, then phone 390x844) before package screenshots. Official product: Super, the Notion-to-website tool, at https://super.so/ (title "Super — Create Custom Websites with Notion"). The marketing site is a published Super site (Notion content plus a custom navbar). There is no theme switch on the public surface.

Nothing in this map was submitted. Sign-in, Google, Apple, passkey, email fields and newsletter fields were not used.

## Shell

Desktop header (every `super.so` marketing page):

| Control | Opens |
|---|---|
| Logo | https://super.so/ |
| Use cases (`aria-expanded` dropdown) | A panel of 26 links. Each item is a page under `/use-cases/`. See Use cases. |
| Showcase | https://super.so/showcase |
| Templates | https://super.so/templates |
| Features (`aria-expanded` dropdown) | A panel of feature pages plus "View all features". See Features. |
| Pricing | https://super.so/pricing-annual |
| Blog | https://super.so/blog |
| Sign in | https://app.super.so (login wall). Branch stopped. |
| Get started free | https://app.super.so/signup (signup wall). Branch stopped. |

Phone header (390): logo, "Get started free" (signup wall), and a hamburger (`.super-navbar__menu-open`, Lucide menu icon). The hamburger opens a full-screen drawer (`.super-navbar__menu`). The drawer lists Use cases (chevron, expands the same 26 links), Showcase, Templates, Features (chevron, expands the feature list plus View all features), Pricing, Blog, and Sign in (external, login wall). A close control replaces the hamburger while the drawer is open.

Footer (same on marketing pages) links the pages in the footer table below, plus external hosts. "Made with Super" is a badge, not a navigation control.

## Menus and in-page interactions

| Control | Where | What it opens | Capture |
|---|---|---|---|
| Use cases | Header, desktop and phone drawer | Dropdown / accordion of 26 `/use-cases/*` pages. Does not navigate until an item is chosen. | Open, do not follow every item as a separate interaction shot. |
| Features | Header, desktop and phone drawer | Dropdown / accordion of feature pages. | Open. |
| Load more | Home, blog, icons, CDN locations, some blog posts (`.notion-collection-load-more`) | Reveals more cards in the same page. No navigation. | Click once. |
| +20 more | Home, "What are you building?" chip row | Expands the use-case chip list on the same page. | Click. |
| any site | Templates sentence "Show me templates for any site" | In-page menu of site types (Website and the category list). `href="#"`, stays on `/templates`. | Open, pick one category. |
| anyone | Templates sentence "made for anyone" | In-page menu of audience filters. Stays on `/templates`. | Open. |
| Category rows | Templates sidebar (All templates, Free, Sites, Personal, …) | Filters the grid on the same page. `data-tab` anchors with `href="#"`. | Select one. |
| Search field | Templates | Text field. Typing filters the grid on the same page. Not a newsletter. Filled with the word "portfolio" and cleared. Not submitted. | Focus and filled. |
| Original / Green / Blue / Mono | Use-case pages that include a demo (25 of 26; event-page has none) | Recolours the embedded demo on the same URL. | Mono selected. |
| Start with this website | Use-case hero | Signup wall (`app.super.so/signup`). | Record URL, stop. |
| Open the demo | Use-case hero | Published customer or template site (`*.super.site`). Third-party content. | Not followed as a product surface. |
| Play | Home hero video | Plays the public launch video in place. | Not required for tokens. |
| Cookie banner | Not mounted on the pages opened. No consent control to dismiss. | | Not present. |
| Theme toggle | Not present. | | Not present. |
| Dialog / toast | None mounted on the pages opened. | | Not present. |

## Auth walls (branch stopped)

Visited once to record the wall. No email typed. No password submitted. Google, Apple and passkey were not clicked.

| URL | What is on the page |
|---|---|
| https://app.super.so/login | Title "Super App". Email address, password, Forgot password?, Log in, Sign in with Google, Sign in with Apple, Sign in with a passkey, Sign up, Terms of Service, Privacy Policy. |
| https://app.super.so | Same login wall (header "Sign in" lands here). |
| https://app.super.so/signup | Signup wall. Not filled. |

The signed-in dashboard, site editor, billing, memberships admin and password-reset form are behind this wall. Not captured.

## Marketing pages (same shell)

Captured as their own pages. Sibling pages that share the shell are listed so the tree is complete. Screenshots cover the distinct layouts, not every sibling.

| Path | Role |
|---|---|
| `/` | Home. Chip row, video, steps, logo row, Load more on the gallery. |
| `/showcase` | Customer stories index. |
| `/showcase/testimonial-*`, `/showcase/case-study-*` | Story pages. One testimonial and one case study stand in for the set. |
| `/templates` | Filterable template gallery. |
| `/pricing-annual` | Pricing (nav target). Annual. |
| `/pricing` | Pricing, monthly. Linked from the footer, not the header. |
| `/blog` | Blog index. Load more. |
| `/blog/notion-sites-vs-super` | One article. |
| `/features` | Feature index. |
| `/features/ai-chat` | Feature page (stands in for the feature set). |
| `/features/mcp` | Feature page. |
| `/features/high-performance` | Feature page. |
| `/features/high-performance/global-cdn-locations` | CDN city list. Load more. |
| `/features/custom-design` | Feature page. |
| `/features/excellent-seo` | Feature page. |
| `/features/custom-domains` | Feature page. |
| `/features/custom-code` | Feature page. |
| `/features/password-protection` | Feature page. |
| `/features/powerful-integrations` | Feature page. |
| `/features/multi-language` | Feature page (nav label is "Mutli-Language"). |
| `/features/file-upload` | Feature page. |
| `/features/memberships` | Feature page. |
| `/features/cookie-consent-banner` | Feature page. |
| `/features/rss-atom-feeds` | Feature page. |
| `/analytics` | Analytics feature page (in the Features menu, not under `/features/`). |
| `/use-cases/<slug>` | 26 pages, listed below. Website captured in full; the rest share that layout. |
| `/guides` | Guides index (Notion page). |
| `/themes` | Themes index. |
| `/icons` | Icon gallery. Load more. |
| `/builder` | Super Builder page. |
| `/community` | Community page. |
| `/create` | Create page. |
| `/trial` | Workbench Live page. |
| `/privacy` | Privacy. |
| `/terms` | Terms. |
| `/data-processing-agreement` | DPA. |
| `/report` | Report page. |
| `/4-0oooo` | Launch note linked from the home video. |
| `/illustrations` | Redirects to `/`. |

Use-case slugs (header menu and home chips): website, landing-page, startup-site, agency-site, product-page, event-page, portfolio, personal-site, link-in-bio, resume, blog, newsletter-archive, podcast, changelog, roadmap, press-kit, docs, help-center, knowledge-base, customer-portal, company-wiki, employee-onboarding, course-site, intranet, directory, job-board.

`/use-cases/event-page` has the shell and no Original/Green/Blue/Mono chips. The other 25 do.

## Footer and off-site hosts

| Control | URL | Treatment |
|---|---|---|
| Docs | https://docs.super.so/ | Separate docs host. Loaded (200). Not the marketing shell. One viewport shot. |
| Changelog | https://changelog.super.so/ | Separate host. Loaded (200). One viewport shot. |
| Status page | https://status.super.so/ | Separate host. Loaded (200). One viewport shot. |
| Roadmap | https://feedback.super.so/ | Separate host. Loaded (200). One viewport shot. |
| Affiliates | https://s.super.so/affiliates | Short link. Not followed into a form. |
| Discord | https://s.super.so/discord | Short link to a community. Not followed. |
| View this page in Notion | https://s.super.so/view-notion | Leaves the product. Not followed. |
| Twitter / YouTube / Instagram | External | Not the product. Not followed. |
| Customer sites | `*.super.site` and other published domains | Customer content, not Super's chrome. Not captured as product screens. |
| Notion affiliate | affiliate.notion.so | Third party. Not followed. |

## Dead links

These hash-id paths are linked from the home page and return the site's 404, which still paints the marketing shell:

- https://super.so/da9e218bd10ad3ce28e44d60462b039a-super
- https://super.so/c8bf19e51c30bfeba925c188fa75dfdb-super
- https://super.so/661fb276848c008a84a500287ba4be03-super

## Not on the public surface

Signed-in app, site editor, billing, memberships login for a customer site, password-reset form, destructive confirmation, toasts, form validation errors, empty dashboard, loading dashboard, onboarding, profile, plan picker, survey. A control that would open one of those stops at the login or signup URL above.
