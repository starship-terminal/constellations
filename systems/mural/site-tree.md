# Mural public site tree

Mapped on 2026-11-21 from the signed-out homepage at `https://www.mural.co/` (title: "AI-powered visual workspace for team collaboration | Mural"), before screenshots. Viewport 1440 by 900. The h1 was "Sync up. Speed up. Stand out." `color-scheme` was `normal`. The site is a live marketing product, not a parked domain. No captcha wall blocked the homepage.

The product workspace sits behind Login and Sign up. This tree stops at those walls. Identity-provider buttons were not clicked. No email, password, or code was typed. No form was submitted.

Hover opens a header menu on this page. A click on the same toggle closes it. Escape was not required.

## Header

The nav is a floating white pill. The hamburger (`aria-label` "menu", class `navbar_menu-button`) is in the DOM and hidden at 1440. It is visible at 390.

| Control | Opens |
|---|---|
| Logo, `aria-label` "home" | `/` (this page) |
| Product | Hover: menu on this page (below). Does not navigate. |
| Solutions | Hover: menu on this page (below). Does not navigate. |
| Services | Hover: menu on this page (below). Does not navigate. |
| Enterprise | `/enterprise` |
| Resources | Hover: menu on this page (below). Does not navigate. |
| Pricing | `/pricing` |
| Login | `https://app.mural.co/signin`. Wall. Photographed, not submitted. |
| Book a demo | `/contact-us/sales` |
| Sign up free | `https://app.mural.co/signup`. Wall. Photographed, not submitted. |

### Product menu

Hover on Product sets `aria-expanded` true and shows `#w-dropdown-list-0`.

| Item | Opens |
|---|---|
| Overview | `/product` |
| Mural AI | `/mural-ai` |
| AI Safety & Regulations | `/ai/safety-and-regulations` |
| MCP | `/ai/mcp` |
| Compose | `/ai/mural-compose` |
| Templates | `/templates` |
| Integrations | `/integrations` |
| Mural for developers | `/api` |
| Trust & security | `/trust-and-security` |
| Microsoft partnership | `/partners/microsoft` |

### Solutions menu

Hover on Solutions shows `#w-dropdown-list-1`. The open panel has three columns: Teams, Use cases, and Company size. Design & UX is in the dropdown list and was not visible in the open panel at 1440.

| Item | Opens |
|---|---|
| Research & development | `/team/research-and-development` |
| Consulting | `/team/consultants` |
| Marketing | `/team/marketing` |
| Sales | `/team/sales` |
| Design & UX | `/team/design-ux` (in the list, not visible in the open panel) |
| Brainstorming & ideation | `/use-case/brainstorming-and-ideation` |
| Agile practices | `/use-case/agile-project-management` |
| Product development | `/use-case/product-development-software` |
| Strategic planning | `/use-case/strategic-planning` |
| Customer journey mapping | `/use-case/customer-journey-mapping` |
| Process mapping | `/use-case/process-mapping` |
| Research & analysis | `/use-case/research-and-analysis` |
| Client collaboration | `/use-case/client-collaboration-software` |
| Team building | `/use-case/team-building-and-ice-breakers` |
| View all use cases | `/use-cases` |
| Sign up free | `https://app.mural.co/signup`. Wall. Not entered from this menu. |
| Book a demo | `/contact-us/sales` |

### Services menu

Hover on Services shows `#w-dropdown-list-2`.

| Item | Opens |
|---|---|
| LUMA Services | `/luma` |
| Mural Accelerate | `/mural-accelerate` |

### Resources menu

Hover on Resources shows `#w-dropdown-list-3`.

| Item | Opens |
|---|---|
| Blog | `/blog` |
| Events | `/resources/events` |
| Webinars | `/resources/webinars` |
| Use cases | `/use-cases` |
| Case studies | `/case-studies` |
| Newsroom | `/newsroom` |
| Product updates | `/blog/product-release-notes` |
| Product news | `/product-news` |
| Help center | `https://support.mural.co/s/` |

## Hero

The hero is a black canvas. The email field (`#email`, placeholder "Enter your email") and the "Get started free" submit sit in the hero. A hidden Cloudflare Turnstile field is in the same form. The form was not submitted and the email field was left empty.

| Control | Opens |
|---|---|
| Collaborator Notice | `/terms/collaborator-notice` |
| Privacy Statement | `/terms/privacy-statement` |
| Get started free | Would submit the email form. Not clicked. |

"Which team are you part of?" is copy above team links further down the page, not a control in the hero form.

## Page body

These links were visible on the homepage below the hero. Template links that open `app.mural.co` were not followed.

| Control | Opens |
|---|---|
| Map your sales funnel now | `https://app.mural.co/template/...`. App wall. Not followed. |
| See more results | `/case-studies` |
| Learn more (SAP, IBM, HPE) | `/case-studies/sap-sales-efficiency-with-mural`, `/case-studies/ibm-sales`, `/case-studies/hpe` |
| Learn more about Mural AI | `/mural-ai` |
| Book a demo | `/contact-us/sales` |
| Start building | `/team/research-and-development` |
| Start closing | `/team/sales` |
| Start converting | `/team/marketing` |
| Start scaling | `/team/consultants` |
| Start collaborating | `/product` |
| Start innovating | `https://www.luma-institute.com/` |
| previous slide / next slide | Testimonial slider on this page |
| Explore customer outcomes | `/case-studies` |
| Explore resources | `/blog` |
| Start for free | `https://app.mural.co/signup`. Wall. Not followed from the body. |
| See pricing | `/pricing` |
| You can with Mural | `https://app.mural.co/signup`. Wall. Not followed. |

Team chips further down the page: Consulting `/team/consultants`, Marketing `/team/marketing`, Sales `/team/sales`, Design & UX `/team/design-ux`.

## Phone chrome

At 390 the logo and the "menu" button are the only header controls. Opening the menu shows Product, Solutions, Services, Enterprise, Resources, Pricing, Login, Book a demo, and Sign up free. The four menus are the same dropdowns as desktop. Login and Sign up free still go to the app walls.

## Footer

| Group | Items |
|---|---|
| Products | Product overview `/product`, Features `/features`, Mural AI `/mural-ai`, Templates `/templates`, Developers `/api`, Integrations `/integrations`, Trust & security `/trust-and-security`, Pricing `/pricing`, Enterprise `/enterprise` |
| Solutions | LUMA Services `/luma`, Mural Accelerate `/mural-accelerate`, Use cases `/use-cases`, Teamwork Assessment `/teamwork-assessment` |
| Resources | Events `/resources/events`, Webinars `/resources/webinars`, Blog `/blog`, Resource hub `/resources`, Microsoft partnership `/partners/microsoft`, Case studies `/case-studies`, Compare `/compare`, Accessibility `/accessibility`, Mural status `https://status.mural.co/`, Help center `https://support.mural.co/s/`, Sitemap `/sitemap` |
| Company | About us `/about-us`, Careers `/careers`, Newsroom `/newsroom`, Brand assets `/brand-assets`, Contact sales `/contact-us/sales`, Contact support `/contact-us/support` |
| Our Apps | Download our apps `/apps`, Microsoft Teams `/partners/microsoft/teams`, Surface Hub `/partners/microsoft/surface-hub` |
| Legal & privacy | Privacy statement `/terms/privacy-statement`, Legal `/legal`, California privacy `/terms/california-privacy`, Your privacy choices `/exercise-your-rights` |
| Social | Facebook, Instagram, X. External. Not followed. |
| Reviews | G2 reviews. External. Not followed. |

No cookie banner was mounted on the homepage. "Your privacy choices" is a page, not a dialog on this load.
