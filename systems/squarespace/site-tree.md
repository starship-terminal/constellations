# Squarespace public site tree

Mapped from https://www.squarespace.com/ on 2026-11-21 in headless Chromium, before screenshots. Desktop header is a sticky bar. Phone header is a logo plus a "Navigation menu" button (`button.global-navigation__hamburger`).

Nothing in this map was submitted. Login, signup, Google, Apple and Facebook were not entered. A control that leaves the marketing host for a login wall is marked wall and that branch stops.

## Header (desktop, closed)

| Control | Opens |
|---|---|
| Logo (`a.global-navigation__logo-link`, "Squarespace homepage") | `/` |
| PRODUCTS (`button.global-navigation__header-link-item`) | Desktop menu panel. Links below. Escape closes it. |
| SOLUTIONS (same button class) | Desktop menu panel. First column is ten industries. Hovering an industry reveals its trades in a second column. Escape closes it. |
| RESOURCES (same button class) | Desktop menu panel. Links below. Escape closes it. |
| LOG IN | `/auth/protected-redirect/login?location=https://account.squarespace.com` which redirects to `login.squarespace.com`. Wall. Email and password, or Google, Apple, or Facebook. Nothing typed. |
| GET STARTED | `/templates/get-started` (public template picker, not a submitted signup) |

## PRODUCTS menu

| Label | Opens |
|---|---|
| Websites | `/website-design` |
| Website Templates | `/templates` |
| AI Website Builder | `/websites/ai-website-builder` |
| Design Intelligence | `/design-intelligence` |
| Ecommerce | `/ecommerce-website` |
| Portfolios | `/websites/create-a-portfolio` |
| Blogs | `/websites/create-a-blog` |
| Analytics | `/websites/analytics` |
| Services | `/services` |
| Online Stores | `/online-stores` |
| Invoicing | `/invoicing` |
| Scheduling | `/scheduling` |
| Limited Releases | `/ecommerce/limited-release-selling` |
| Content & Memberships | `/content` |
| Donations | `/donations` |
| Financial Solutions | `/financial-solutions` |
| Marketing Tools | `/website-marketing` |
| Email Campaigns | `/email-marketing` |
| SMS Campaigns | `/sms-marketing` |
| SEO Tools | `/marketing/seo` |
| AI Visibility | `/ai-visibility` |
| Free Tools | `/tools` |
| Domain Search | `https://domains.squarespace.com` |
| Domain Transfer | `https://domains.squarespace.com/transfer-a-domain` |
| Business Email | `/professional-email` |
| View All Features | `/feature-index` |
| Build with AI | `/templates/custom-website-templates` |
| Squarespace for Pros | `/professionals` |
| Circle | `/circle` |

## SOLUTIONS menu

First column, each a page. The second column lists trades under the hovered industry. Those trade links are the same pattern: `/solutions/<industry>/<trade>`.

| Industry | Page | Trades shown when hovered |
|---|---|---|
| Creative Services | `/solutions/creative-services` | Photographers, Graphic Designers, Artists, Interior Designers, Architects, Fashion & Apparel |
| Professional Services | `/solutions/professional-services` | Consultants, Professional Coaches, Real Estate Agents, Legal Services, Marketing Agencies, Tech & IT Services |
| Education & Training | `/solutions/education` | Exam Prep Tutors, Music Teachers, Art Instruction, Dance Schools, Language Schools, Vocational Training |
| Beauty | `/solutions/beauty` | Hair Salons, Barbershops, Nail Studios, Tattoos & Piercings, Makeup Artists, Jewelry Makers |
| Sports & Fitness | `/solutions/sports` | Sports Coaches, Sporting Goods, Fitness Centers, Sports Camps, Personal Trainers, Yoga Studios |
| Health & Wellness | `/solutions/health` | Massage Therapists, Acupuncturists, Wellness Retreats, Recovery Centers, Nutritionists, Medspas |
| Home Services | `/solutions/home-services` | Contractors, Home Decor, Landscapers, Cleaning Services, Pet Care, Auto Repair |
| Events & Experiences | `/solutions/events` | Travel Agencies, Camps, Activities, Festivals, Concerts & Shows, Restaurants & Bars |
| Charities & Nonprofits | `/solutions/nonprofits` | Faith Communities, Philanthropy & Advocacy, Community Groups, Environment & Conservation, Arts & Culture, Youth Education |
| Personal | `/solutions/personal` | Resumes & CVs, Portfolios, Weddings, Freelancers, Creators, Podcasts |

## RESOURCES menu

| Label | Opens |
|---|---|
| Help Center | `https://support.squarespace.com/` (public help, separate host) |
| Forum | `https://forum.squarespace.com/` (public forum, separate host) |
| Webinars | `https://learning.squarespace.com` (public learning host) |
| Blog | `/blog` |
| Hire an Expert | `/designer/home` |
| Made with Squarespace | `/showcase` |

## Homepage body (not the menus)

| Control | Opens |
|---|---|
| Skip to main content | `#content` (same page) |
| Promo banner "Limited time offer / 50% off all plans" | `/pricing` |
| Offer terms (`button[aria-label="Offer terms"]`) | Tooltip on the banner. Not a page. The open PRODUCTS panel covers it, so it is clicked only after the menu closes. |
| Hero GET STARTED | `/templates/get-started` |
| Previous / Next (`button.cursor-follow__area`) | Cycles the hero template carousel. Same page. |
| Pills: Services, Online Store, Invoicing, Scheduling, Donations, Memberships, Blog, Portfolio | Same-page section switch (`button.pills__pill`). Not a navigation. |
| Play (`button.king-carousel__toolbar-button`) | Starts the on-page video carousel. Not a form. |
| Previous slide / Next slide | Card carousel on the same page. |
| Domain search field + Search | `your-domain__form`. Not submitted. Focus only. |
| Accordion titles (How to build a website, FAQ, 24/7 Support, `button.faq__accordion-title`) | Expand on the same page. |
| Template names (Bloom, Radian, Reflect, Rotate, Selene, Reseda, Condesa, Adri, Hales, Minoru) | `/templates/<name>-fluid-demo` |
| Start with this template | `#reseda` (same page anchor) |
| Customer-site cards (abathhouse.com and similar) | External published customer sites. Recorded, not followed. |
| Locale button `$ SGD` | Opens a currency list (SGD, USD, and others) in the footer. Not submitted. |
| Language links (Deutsch, Español, Français, Italiano, 日本語, 한국어, Nederlands, Português) | `de.squarespace.com`, `es.squarespace.com`, `fr.squarespace.com`, `it.squarespace.com`, `ja.squarespace.com`, `ko.squarespace.com`, `nl.squarespace.com`, `pt.squarespace.com`. Same marketing site, other locales. English stays on `www`. Not captured page by page. |

## Footer

| Label | Opens |
|---|---|
| Pricing | `/pricing` |
| Templates | `/templates` |
| Feature List | `/feature-index` |
| Website Editing | `/website-design` |
| Fluid Engine | `/websites/fluid-engine` |
| Logo Maker | `/logo` |
| Business Name Generator | `/tools/business-name-generator` |
| Domain name generator | `https://domains.squarespace.com/tools/domain-name-generator` |
| TLDs | `https://domains.squarespace.com/tlds` |
| Squarespace Payments | `/payments` |
| Squarespace Capital | `/capital` |
| Extensions | `/extensions/home` |
| Acuity Scheduling | `https://www.acuityscheduling.com/` (sibling product) |
| Bio Sites | `https://www.biosites.com/` (sibling product) |
| Unfold | `https://www.unfold.com/` (sibling product) |
| Students | `/students` |
| Affiliates | `/affiliates` |
| About | `/about/company` |
| Careers | `/about/careers` |
| Press & Media | `/press-coverage` |
| Contact Us | `/contact` |
| Newsroom | `https://newsroom.squarespace.com/` |
| Developer Platform | `https://developers.squarespace.com/` |
| Developer Blog | `https://engineering.squarespace.com/` |
| Our Brand | `https://brand.squarespace.com/` |
| Squarespace Collection | `https://collection.squarespace.com/` |
| Product Updates | `/refresh` |
| System Status | `https://status.squarespace.com/` |
| Account Dashboard | `https://account.squarespace.com/` wall |
| Domains (account) | `https://account.squarespace.com/domains` wall |
| Hire an Expert (footer, with channel query) | `/designer/home` |
| Privacy | `/privacy` |
| Specific Privacy Notice | `/privacy#appendix-1`, `/privacy#appendix-2` |
| Terms | `/terms-of-service` |
| Data Privacy | `/data-privacy` |
| Security Measures | `/security` |
| Accessibility | `/accessibility` |
| EU Legal / SCTA | `/imprint` |
| Sitemap | `/sitemap.xml` |
| Turkey Privacy / Terms | `/privacy-policy-tr`, `/terms-of-service-tr` |
| Facebook, Instagram, LinkedIn, YouTube, X | Official Squarespace profiles. Not followed. |
| Log Out | `/` while signed out. No session. |

## Phone

| Control | Opens |
|---|---|
| Logo | `/` |
| Navigation menu (`button.global-navigation__hamburger`) | Full-screen nav. PRODUCTS, SOLUTIONS and RESOURCES are inside it, not in the desktop bar. |
| Promo banner | `/pricing` |
| Same body controls as desktop, stacked | Same destinations |

## Walls (stop)

| Control | Where it goes | What is on screen |
|---|---|---|
| LOG IN, Account Dashboard, account Domains | `login.squarespace.com` (OAuth authorize, then the login page) | Email and password, or Google, Apple, or Facebook. Password not submitted. Email not typed. |
| Any control that lands on that host | same | Branch stops. |

## Capture boundaries (2026-11-21)

These were found while capturing, after the map above.

- LOG IN lands on `https://login.squarespace.com` (email and password, or Google, Apple, or Facebook). Nothing was typed. Login screenshots were deleted and are not in `screenshots/`.
- `/templates/get-started` is a public wizard. The default screen was captured. NEXT was not pressed and no field was filled.
- A fast probe of every industry trade URL returned HTTP 429. Those pages were not captured. One industry page stands in for the template.
- The blog viewport shot stayed blank below the fold. The header and the MAKING IT title painted. Treat `screenshots/blog-light-default.png` as a partial. `screenshots/blog-light-full.png` is the first pass.
- Contact cards painted as empty boxes with an icon and a label. Their bodies did not fill.
- The feature-index full-page stitch was 44740px and was not kept. The viewport shot is the evidence.
- The mobile templates full-page stitch was dropped for the same reason.
- Offer terms was not opened. The open PRODUCTS panel covered the button.
- Currency `$ SGD` and the language hosts were not opened. Customer example sites were not followed.

## Not a Squarespace marketing page

Customer example sites linked from the homepage (published sites on other domains, and `*.squarespace.com` customer hosts such as `nerine-floral.squarespace.com`) are examples, not the product UI. They are listed in the homepage harvest and not captured as this package.
