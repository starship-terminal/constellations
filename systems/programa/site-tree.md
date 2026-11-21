# Programa public site tree

Mapped from the live public site on 2026-11-21, before screenshots, in headless Chromium. Desktop map used 1440x900. Phone menu map used 390x844. The official product is [programa.design](https://programa.design/), interior-design project management. The marketing host is Next.js on Vercel. The signed-in product is a separate host.

Nothing in this file was submitted. No email was typed. No password was typed. Google, Trimble and Xero were not clicked.

## Hosts

| Host | What it is | This capture |
|---|---|---|
| `programa.design` | Public marketing site. English default. Locale mirrors under `/au`, `/uk`, `/eu`, `/mx`, `/latam` | Captured from the default English tree |
| `app.programa.design` | The product. Login and register | Wall. Branch stops |
| `programa.com` | Older feature URLs. Two footer-adjacent links on `/features` point here | Recorded. Not treated as the product |
| `staging.programa.design` | One homepage editorial card links here | Recorded. Not captured |
| `intercom.help` | Help Centre | External. Not captured |
| `programa.homerun.co` | Careers | External. Not captured |
| Social hosts | Instagram, Facebook, Pinterest, LinkedIn, YouTube, TikTok | External. Not captured |

Sitemap at `https://programa.design/sitemap.xml` listed 441 unique paths on 2026-11-21: 169 `/blog`, 139 `/editorial`, 29 `/features`, 18 `/made-with-programa`, plus locale mirrors and campaign landers. The tree below is the control map from the homepage, not a dump of every article URL.

## Theme

One painted theme. `color-scheme` is `normal`. Body background `rgb(255, 255, 255)`, text `rgb(26, 26, 26)`. No `data-theme`, `data-mode`, or theme toggle on the public pages checked. No dark theme to capture.

## Homepage shell

URL: `https://programa.design/` (Vercel matched path `/en`). Title: Interior Design Project Management Software | Programa. H1: Freedom, by design.

Desktop header, left to right:

| Control | Opens |
|---|---|
| Logo | `https://programa.design/` |
| Features (hover or click) | Mega menu. Click also navigates to `https://programa.design/features` |
| Solutions (hover or click) | Mega menu. Click stays on `/` with hash `#` |
| Pricing | `https://programa.design/pricing` |
| Learn (hover or click) | Mega menu. Click stays on `/` with hash `#` |
| Log in | `https://app.programa.design/login/` Wall. Stop |
| Start free | `https://app.programa.design/register/` Wall. Stop |

Phone header (390): logo, then a button labelled Open menu. Open menu reveals the same three sections as collapsed buttons (aria-expanded false), plus Start free and Log in. Close menu dismisses it. Features, Solutions and Learn expand in place to the same destinations as the desktop menus.

A second Open menu and a control labelled Drag to reposition menu sit in a fixed widget (likely the site chat). They are not the site nav. Not used as a capture path.

### Features menu

| Label | Opens |
|---|---|
| Schedules | `/features/schedules-for-interior-designers` |
| Presentations | `/features/presentations-for-interior-designers` |
| Project Management | `/features/best-interior-design-project-management-software` |
| Product Library | `/features/product-libraries` |
| Mood Boards | `/features/pin-boards-mood-boards-for-interior-designers` |
| Web Clipper | `/features/interior-design-webclipper` |
| Client Dashboard and approvals | `/features/client-dashboard-for-designers-and-architects` |
| Invoicing and Payments | `/features/invoicing-and-payments-for-interior-designers` |
| Time Tracking | `/features/time-tracking-for-interior-designers` |
| Procurement | `/features/interior-design-procurement-software` |
| Quoting | `/features/quoting` |
| All New Schedules (promo card) | `/features/schedules-for-interior-designers` |

### Solutions menu

| Label | Opens |
|---|---|
| Solo designers | `/solo-designers` |
| Small studios | `/small-studios` |
| Large teams | `/large-studios` |
| Watch demo | `/designer-demo-on-demand` |

### Learn menu

| Label | Opens |
|---|---|
| Blog | `/blog` |
| Editorial | `/editorial` |
| Made with Programa | `/made-with-programa` |
| Contact us | `/contact-us` |
| Changelog | `/changelog` |

## Homepage body

| Control | Opens |
|---|---|
| Get started | `https://app.programa.design/register` Wall. Stop |
| Watch a demo / Watch demo | `/designer-demo-on-demand` |
| Pause the studio video | Pauses the hero studio video. Local. No navigation |
| Testimonial quote button | Plays a testimonial. Local |
| Play Smac Studio testimonial | Plays that testimonial. Local |
| Previous / Next | Testimonial carousel. Local |
| Specifications | `/features/specification-tools` |
| Instant product import | `/features/interior-design-automation-tool` |
| Client Dashboard | `/features/client-dashboard-for-designers-and-architects` |
| Product Library | `/features/product-libraries` |
| Project Management | `/features/best-interior-design-project-management-software` |
| Mood Boards and Presentations | `/features/pin-boards-mood-boards-for-interior-designers` |
| View our Schedules | `/features/specification-tools` |
| Our Project Management | `/au/features/best-interior-design-project-management-software` (locale mirror) |
| Explore Presentations | `/features/presentations-for-interior-designers` |
| See all | `/made-with-programa` |
| Studio cards | Editorial stories. One card points at `staging.programa.design` |
| Event and feature cards | Blog posts (`/blog/wcbf-ladw-dezeen-kelly-wearstler-paul-chan`, `/blog/london-design-festival-dezeen-cake-cupla-programa-wcbf`, `/blog/vogue-living-vl50`) |

## Footer (shared)

| Control | Opens |
|---|---|
| All features | `/features` |
| Specification tools | `/features/specification-tools` |
| Management tools | `/features/best-interior-design-project-management-software` |
| Presentation tools | `/features/client-dashboard-for-designers-and-architects` |
| For Suppliers | `/suppliers` |
| Company | `/about` |
| Careers | `programa.homerun.co` External |
| Contact | `/contact-us` |
| FAQs | `/frequently-asked-questions` |
| Pricing | `/pricing` |
| Blog | `/blog` |
| Made with Programa | `/made-with-programa` |
| Editorial | `/editorial` |
| Testimonials | `/testimonials` |
| Help Centre | `intercom.help/programa/en` External |
| Interior Design Software Guide | `/best-interior-design-software-guide` |
| How to Choose FF&E Specification Software | `/how-to-choose-ffe-specification-software` |
| What is Interior Design Procurement Software? | `/features/interior-design-procurement-software` |
| Terms and Conditions | `/terms-and-conditions` |
| Privacy Policy | `/privacy-policy` |
| Cookie Policy | `/cookie-policy` |
| Acceptable Use Policy | `/acceptable-use-policy` |
| Data Processing Addendum | `/data-processing-addendum` |
| Social icons | External hosts listed above |
| Summarize with ChatGPT / Claude / Gemini | External. Not followed |

No cookie-consent dialog was mounted on the pages opened. Cookie Policy is a page, not a banner button.

## Page controls beyond the shell

| Page | Extra control | What it does |
|---|---|---|
| `/pricing` | Toggle annual pricing | Local billing-period toggle. Does not submit |
| `/pricing` | How will I be billed? / How many users can I have in my team? / Is there a free trial? | FAQ accordions. Local |
| `/pricing` | Plan CTAs | Start free or register. Wall. Stop |
| `/features` | Feature deep links and Web Clipper download | Public feature pages, plus Chrome Web Store (external). Two links go to `programa.com` |
| `/blog` | Search field, placeholder Explore the blog, name `query` | Looked at. Not typed into. Not submitted |
| `/blog` | Article cards | `/blog/<slug>`. Index captured. Individual posts are the same article template |
| `/frequently-asked-questions` | Question buttons | Accordions. Local. No form |
| `/contact-us` | Email field with a studio-email placeholder, plus Submit | Form. Not filled. Not submitted |
| `/contact-us` | Get in touch | Opens the same contact path. Not submitted |
| `/trade-portal` | Join the waitlist | Clicked once. Stayed on the page. No dialog and no fields appeared in the headless session |
| `/trade-portal` | Book a demo | Not followed into a booking form |
| `/trade-portal` | Setup account | `app.programa.design/register`. Wall. Stop |
| `/designer-demo-on-demand` | Demo player | Public page. No form fields visible on first paint |
| `/editorial`, `/made-with-programa` | Story cards | Article templates. Indexes captured |
| `/changelog` | Update list | Public page |
| `/about`, `/team`, `/testimonials`, `/reviews` | In-page links back into the shell | Public pages |
| `/solo-designers`, `/small-studios`, `/large-studios` | Solution landers | Public. CTAs that say Get started go to register. Wall. Stop |
| Legal pages | Long text | Public. Same shell |

## Auth wall

`https://app.programa.design/login` loaded with HTTP 200. Title: Log in · Programa. H1: Log in.

The page asks for email (`user[email]`, placeholder Enter Email) and password (`user[password]`, placeholder Enter Password), plus Continue with Google, Continue with Trimble, and Continue with Xero. Password was not submitted. Email was not typed. Google, Trimble and Xero were not clicked. Register (`/register`) is the same class of wall and was not opened past the URL.

Other `app.programa.design` paths seen as links on public pages (projects, studio, pulse, settings, schedule examples) are the signed-in product. Not opened.

## Not in this tree

- Locale mirrors (`/au`, `/uk`, `/eu`, `/mx`, `/latam`) repeat the English pages. Not a separate design system.
- Campaign and partner landers in the sitemap (webinars, special offers, brand pages) share the marketing shell. Not a separate component set.
- Every blog, editorial and made-with article. The indexes are the reachable lists. One article of each family is enough for the template.
- Signed-in app screens, onboarding, plans, surveys, newsletters, and profile fields.
