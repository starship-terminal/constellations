# Webflow public site tree

Mapped from [https://webflow.com/](https://webflow.com/) in headless Chromium before screenshots, on 2026-11-21. Desktop viewport 1440×900 (`innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 1). Phone viewport 390×844 (`innerWidth` 390, `innerHeight` 844, `devicePixelRatio` 2). The page title was "Webflow: The agentic web platform for modern businesses". `colorScheme` on the default page was `normal`. No `data-theme` attribute. Dark mode is a real public control: a button labelled "Dark mode" inside the nav dropdowns sets `localStorage.darkMode` to `true` and adds `u-mode-dark` on `html`. After that click the body background computed to `rgb(8, 8, 8)` and `colorScheme` became `dark`.

This file is the map of which control opens which page, menu, dialog, or interaction. Auth and bot walls stop the branch. Nothing here was submitted.

## Auth walls (stop)

| Control | Opens | What was visible | Stopped |
|---|---|---|---|
| Nav "Log in" | [https://webflow.com/login](https://webflow.com/login) | Email address or username, Password, Continue, Forgot your password?, Sign up. "Continue with GitHub" and "Continue with SSO" text. A Google Sign-In iframe titled "Sign in with Google Button" (`accounts.google.com/gsi/button`). Password was not typed. The Google iframe was not clicked. | Yes |
| Nav "Start for free" / "Get started" | [https://webflow.com/signup](https://webflow.com/signup) | HTTP 403, title "Access to this page has been denied", press-and-hold bot check. No fields filled. | Yes |
| Hidden dialog in the homepage DOM, not opened | "Two-factor authentication" copy ("Enter the 6-digit code…") | Mounted, not visible (`display` not a painted dialog). Not opened. No code entered. | Yes |

## Desktop header (closed)

The header is `.nav.w-nav`. Visible controls, left to right:

| Control | Kind | Opens |
|---|---|---|
| Skip to main content | link | `#main` on the same page |
| Logo "Home Page" | link | [https://webflow.com/?r=0](https://webflow.com/?r=0) |
| Platform | button, `aria-controls="dropdown_content_0"`, `aria-haspopup="true"` | Platform menu |
| Source | link | [https://webflow.com/source](https://webflow.com/source) |
| Solutions | button, `aria-controls="dropdown_content_1"` | Solutions menu |
| Resources | button, `aria-controls="dropdown_content_2"` | Resources menu |
| Enterprise | link | [https://webflow.com/enterprise](https://webflow.com/enterprise) |
| Pricing | link | [https://webflow.com/pricing](https://webflow.com/pricing) |
| Log in | link | login wall, above |
| Contact Sales | link | [https://webflow.com/enterprise/contact-sales](https://webflow.com/enterprise/contact-sales) |
| Start for free | link | signup bot wall, above |

Inside each dropdown, after the section links, the same chrome repeats: a role switcher (Marketer, Designer, Developer, Agency, each `href` `#`), and a language switcher (English `/?r=0`, French `/fr`, German `/de`, Spanish `/es`). Theme buttons "Light mode", "Dark mode", and "Auto (OS)" sit in that chrome. "← Back" is the nested-menu back control.

## Platform menu (`dropdown_content_0`)

Clicking Platform sets `aria-expanded="true"` and shows the panel (`display: block`). It does not navigate. Escape and a click outside close it.

| Link | URL |
|---|---|
| Design | /feature/design |
| Edit content | /feature/edit-content |
| Interactions | /feature/interactions-animations |
| Collaboration | /feature/collaboration |
| Page building | /feature/page-building |
| CMS | /feature/cms |
| Hosting | /feature/hosting |
| Localize | /feature/localize |
| Security | /security |
| Shared Libraries | /feature/shared-libraries |
| Analyze | /feature/analyze |
| Optimize | /feature/optimize |
| SEO | /feature/seo |
| AEO | /feature/aeo |
| Campaigns | /feature/campaigns |
| Apps | /apps |
| Figma to Webflow | /feature/figma-to-webflow |
| Webflow Cloud | /feature/cloud |
| DevLink | /feature/devlink |
| MCP | /feature/mcp |
| Learn more about Platform | /platform |
| Learn more about AI | /feature/ai |

## Solutions menu (`dropdown_content_1`)

Same open and close as Platform. Panel id `dropdown_content_1`.

| Link | URL |
|---|---|
| Brand | /solutions/brand-creative-teams |
| Performance | /solutions/performance-marketers |
| Digital Experience | /solutions/digital-experience-marketers |
| Ops | /solutions/technical-marketers |
| Engineering leaders | /solutions/engineering-leader |
| Developers | /solutions/developers |
| Agencies | /solutions/agencies |
| Freelancers | /solutions/freelancers |
| Global Alliances | /solutions/global-alliances |
| Learn more about Enterprise | /enterprise |
| Learn more about AEO | /feature/aeo |
| AEO Assessment (also in Resources) | /solutions/aeo |

## Resources menu (`dropdown_content_2`)

| Link | URL |
|---|---|
| Templates | /templates |
| Made in Webflow | /made-in-webflow |
| Hire a Certified Partner | /certified-partners |
| Developers | [https://developers.webflow.com/](https://developers.webflow.com/) |
| Webflow University | [https://university.webflow.com/](https://university.webflow.com/) |
| Blog | /blog |
| Webinars & ebooks | /resources |
| The Webflow Way | /webflow-way |
| Customer stories | /customers |
| Our Community | /community |
| Partner with Webflow | /solutions/partners |
| AEO Assessment | /solutions/aeo |
| Support | [https://help.webflow.com/](https://help.webflow.com/) |
| Join the Community | [https://community.webflow.com/](https://community.webflow.com/) |

## Homepage body

| Control | Opens |
|---|---|
| Banner "Meet Webflow Campaigns…" | /blog/campaigns-launch |
| Role switcher "marketing teams" (`role="button"`, `aria-expanded`) | In-page menu: Marketer, Designer, Developer, Agency. Does not navigate (`href` `#`). |
| "Open Dialog" buttons (`data-modal-trigger`, `aria-label="Open Dialog"`) | A full-viewport dialog (`.modal-dialog_home`, 1440×900 when opened). The first stable open showed the Optimize product dialog. The hero marquee buttons are animated and were not used as the click target. |
| YouTube cover (`aria-haspopup="dialog"`, points at a YouTube watch URL) | A dialog on the same page. Not an account chooser. |
| "←" and "→" | Hero slider, same page. |
| "Play Video" | Plays an in-page video. Does not navigate. |
| "Open" / "Close" pairs | FAQ or accordion rows on the same page. |
| "English" (`role="button"`, `aria-haspopup="menu"`) | Language menu: English, French `/fr`, German `/de`, Spanish `/es`. |
| Customer story links | /customers/copy-ai, /customers/abm, /customers/funsize, /customers/n4, /customers/arkose-labs, /customers/civilization, /customers/hunt-gather, /customers/amazon, /customers/dropbox-sign, /customers/verifone, /customers/lattice, /customers/fivetran, /customers/walker-dunlop, and logo links for Orangetheory and Docusign |
| "Get started" in the page | /signup (bot wall; branch stops) |
| "Talk to Sales" / "Contact sales" | /enterprise/contact-sales |

The contact-sales page is a form (email, company size, "How can we best support you", hidden UTM fields, a honeypot). It was not filled and not submitted.

## Pricing page

[https://webflow.com/pricing](https://webflow.com/pricing), title "Plans & pricing | Webflow".

| Control | Opens |
|---|---|
| Monthly / Yearly toggle (`input` checkbox named `toggle`) | Same page, swaps plan prices. Not a form submit. |
| Bandwidth and locale `<select>` elements | Same page, plan calculator. Not submitted. |
| Start for free on a plan | /signup (bot wall; branch stops) |
| Contact Sales | /enterprise/contact-sales |

## Other public pages reached from the homepage

| Path | Notes from the map |
|---|---|
| /templates | Marketplace listing. Search field named `query`. A "Verify" control was present. Search was not submitted. |
| /blog | Listing plus a search input. Search was not submitted. |
| /source, /enterprise, /platform, /feature/*, /solutions/*, /customers, /apps, /security, /accessibility, /webflow-way, /resources, /libraries, /glossary, /community, /made-in-webflow, /certified-partners, /company/about, /company/careers, /company/media, /webflow-ventures, /legal/terms, /legal/privacy, /legal/cookie-policy, /accessibility/statement, /vs/contentful, /vs/framer, /vs/sitecore, /vs/wix, /vs/wordpress, /migrate/business-value-calculator, /templates/applications, /solutions/affiliates, /community/livestreams, /community/become-a-global-leader, /community/webflow-network-groups, /discover/popular, /updates/page-branching-enhancements, /blog/2026-builder-keynote, /blog/webflow-conf-2026-announcements, /webflowconf/session/opening-keynote, /feature/code-components, /feature/ecommerce | Linked from the homepage or footer. Same marketing shell unless a later capture records otherwise. |
| /fr, /de, /es | Language variants of the homepage. |

## Footer

The footer repeats the Platform, Solutions, and Resources links, then company, legal, comparison, and community links. External hosts linked from the homepage (not followed as product surfaces): gsap.com, shop.webflow.com, status.webflow.com, wishlist.webflow.com, help.webflow.com, developers.webflow.com, university.webflow.com, community.webflow.com, youtube.com, x.com, facebook.com, linkedin.com, instagram.com, tiktok.com, plus customer-site links (clay.com and others). Social links are the product's own published accounts.

## Phone (390×844)

The same links are in the DOM. The visible header control is one button, `aria-label="menu"`, `aria-controls="w-nav-overlay-0"`, `aria-haspopup="menu"`, class `.w-nav-button`. Opening it is the phone path to Platform, Solutions, Resources, Log in, Start for free, and the theme buttons. Log in and Start for free stop at the same walls as desktop.

## Not a public page

The Webflow designer, dashboard, site editor, and billing sit behind login. The homepage mounts a two-factor dialog that was not opened. No password, code, profile, birthday, plan, survey, onboarding, or newsletter field was filled.
