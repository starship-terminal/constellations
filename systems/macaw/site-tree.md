# Macaw site tree

Mapped from the live marketing site on 2026-11-21, before screenshots, in headless Chromium at 1440×900. Phone checks used 390×844. The map records which control opens which page, menu, dialog, or interaction. No form was submitted. No password, code, or profile field was filled.

The product is Macaw, a public Webflow marketing site for an AI writing product. Official host: `https://macawhq.com/`. Sitemap: `https://macawhq.com/sitemap.xml` (HTTP 200). Robots: `User-Agent: *` / `Disallow:` empty.

Theme: one light theme. `color-scheme` on the document is `normal`. No `data-theme`, `data-mode`, or `.dark` switch was found. No dark `theme-color` meta.

## Auth wall (stop)

These controls leave the marketing host. The app host did not resolve. Each branch stops at the URL.

| Control | URL | Result |
|---|---|---|
| Log in (nav), Login (footer) | `https://app.macawhq.com/sign-in` | `net::ERR_NAME_NOT_RESOLVED` |
| Start for free, Start with 3 free articles, Analyze your website, Sign up, Get started (pricing) | `https://app.macawhq.com/sign-up` | `net::ERR_NAME_NOT_RESOLVED` |
| Start free with Google | `https://app.macawhq.com/sign-in?strategy=google` | `net::ERR_NAME_NOT_RESOLVED` (Google was not clicked; the href itself does not resolve) |

Signed-in app, checkout, account, onboarding, and plan purchase are not reachable.

## Pages that load

| Path | How you get there | What loaded (2026-11-21) |
|---|---|---|
| `/` | Logo (`aria-label="home"`), Overview (footer) | Marketing home. HTTP 200. Title: Macaw - Human Quality AI Writing At Scale |
| `/#prod` | Nav link Product | Same home, anchor `prod` |
| `/#examples` | Nav link Writing examples | Same home, anchor `examples` |
| `/pricing` | Nav link Pricing, footer Pricing | Pricing page. HTTP 200. Title: Macaw Pricing. H1: Start automating your content today |
| `/contact-us` | Footer Contact | Contact page. HTTP 200. Title: Contact us - Macaw. Form present; not submitted |
| `/terms-and-conditions` | Footer Terms | Legal page. HTTP 200. Title: Terms and Conditions |
| `/privacy-policy` | Footer Privacy | Legal page. HTTP 200. Title: Privacy Policy |
| `/free-tools/blog-title-generator` | Footer Blog Title Generator | Tool landing. HTTP 200. No input rendered |
| `/free-tools/blog-post-ideas-generator` | Footer Blog Idea Generator | Tool landing. HTTP 200. No input rendered |
| `/free-tools/ai-content-idea-generator` | Footer Content Idea Generator | Tool landing. HTTP 200. No input rendered |
| `/free-tools/ai-blog-outline-generator` | Footer Blog Outline Generator | Tool landing. HTTP 200. No input rendered |

## Controls that do not open a new page

| Control | Where | Opens |
|---|---|---|
| Resources (`.navbar_dropdown-toggle`, `role="button"`) | Nav, hover | Dropdown list (`.navbar_dropdown-list`, display `block`, about 222px tall). Two links, both `href="#"`. Blog: "The best content automation resources on planet earth". Documentation: "Everything you need to be successful with Macaw". Neither navigates. A synthetic click did not open it; hover did |
| Menu (`aria-label="menu"`, `.navbar_menu-button`) | Phone header, 40×48 | Overlay nav (`.w-nav-menu` becomes `display:block`, `.w-nav-overlay` present). Links: Product, Writing examples, Pricing, Become an affiliate, Log in, Start for free. Resources children stay `href="#"` and were not visible inside the open drawer (height 0) |
| Writing-example card (`.div-block-46`, `role="button"`, `onclick` `go1()` through `go5()`) | Home `#examples` carousel | Tingle dialog (`.tingle-modal.tingle-modal--visible`) with a published sample article. Five cards, cloned by the carousel: Gong, Salesforce, Patagonia, Vanta, Intercom. Close is `.tingle-modal__close` (×). Cards sit in a moving Splide track; pause animation before clicking |
| Previous / Next / Go to slide | Home carousel | Splide pagination. Arrows and dots measured at 0×0 on desktop (`display` none or inline-block with no box). Not a separate page |
| Yearly / Monthly (`.pricing-toggle-button`) | `/pricing` | Same page. Yearly shows Starter $59, Pro $199, Scale $599 per month, "Billed annually". Monthly shows $89, $299, $899, "Billed monthly". A third `.pricing-toggle-button.background` is the sliding pill, not a third plan |
| Contact fields | `/contact-us` | First name, last name, email, message, submit. Placeholders are the site's own generic examples. Not filled. Not submitted. Placeholder strings are not copied into this file |
| Free-tool pages | `/free-tools/*` | Marketing sections and a "Try Macaw free" link to sign-up. No visible `input`, `textarea`, or generate button after load. The generator itself is not on the page |

## Dead or redirecting paths

Sitemap lists these. Each returned HTTP 200 and the home document (same H1 as `/`). They are not separate pages.

| Path | Result |
|---|---|
| `/affiliate` | Nav "Become an affiliate" and the sitemap both name it. Final URL `https://macawhq.com/`. Home content |
| `/affiliate-partner-terms` | Sitemap only. Final URL `https://macawhq.com/`. Home content |
| `/go` | Sitemap only. Final URL `https://macawhq.com/`. Home content |
| Blog, Docs (footer) | `href="#"` on the home page. No destination |

## Not present on the public site

Cookie banner, newsletter modal, theme switch, search field, toast, tooltip, table, select, checkbox, radio, switch, tabs (the pricing control is two buttons, not a tab list), destructive confirmation, empty/loading/error app states, onboarding. No dark theme.
