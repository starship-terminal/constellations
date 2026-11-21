# Acuity Scheduling public site tree

Mapped from https://www.acuityscheduling.com/ on 2026-11-21 in headless Chromium before any screenshots. Each row is a control a signed-out visitor can reach, and what it opens. Login, signup, OAuth, and lead-form branches stop at the wall. Nothing in this map was submitted.

Query strings such as `nav-ref` and `btn` are campaign tags. They do not change the page.

## Shared chrome (every marketing page)

| Control | Opens |
|---|---|
| Wordmark | https://www.acuityscheduling.com/ |
| How It Works | https://www.acuityscheduling.com/features/how-acuity-works |
| Solutions (hover, desktop) | Mega-menu, class `dropdown solutions-dropdown dropdown-active`. Not a new page. |
| Product (hover, desktop) | Mega-menu, class `dropdown products-dropdown dropdown-active`. |
| Resources (hover, desktop) | Mega-menu, class `dropdown resources-dropdown dropdown-active`. |
| Pricing | https://www.acuityscheduling.com/pricing |
| Log in | https://secure.acuityscheduling.com/login then redirects to login.squarespace.com. **Wall. Stop.** |
| Get started (nav pill) | https://www.acuityscheduling.com/get-started then redirects to login.squarespace.com signup. **Wall. Stop.** |
| Promo code button (`NOV20AF`) | Copies the code. Toast text "Copied to clipboard". Does not navigate. |
| OFFER TERMS | PDF on squarespace.com. Off-site. Not captured. |
| Hamburger (phone, `button.hamburger-icon`) | Full-screen mobile menu sheet. |
| Mobile menu close | Dismisses the sheet. |
| Mobile Solutions / Product / Resources | Expands that column inside the sheet. |
| Footer column titles (Get Started, Features, Solutions, Resources, Support, Compare) | On phone, expand that column. On desktop the columns are already open. |
| Language control (`Open language picker`, footer) | https://www.acuityscheduling.com/language-select.php redirects home. The real picker is the footer select: English, Deutsch, Español, Français, Italiano, Português. Changing it reloads the same path in that locale. |
| Social icons | Instagram, Pinterest, Facebook, LinkedIn, YouTube. Off-site. Not captured. |

## Solutions menu

| Item | Opens |
|---|---|
| Beauty | /solutions/beauty |
| Business Services | /solutions/business-services |
| Wellness | /solutions/wellness |
| Fitness | /solutions/fitness |
| Visual and Performing Arts | /solutions/visual-and-performing-arts |
| Education | /solutions/education |
| View all solutions | /solutions |

## Product menu

| Item | Opens |
|---|---|
| Online Booking | /features/online-booking |
| Client Management | /features/client-management |
| Class Scheduling | /features/class-scheduling |
| Payments | /features/payments |
| Invoicing Software | /features/invoicing-software |
| Point of Sale | /features/point-of-sale |
| Calendar Management | /features/calendar-management |
| Availability Controls | /features/availability-controls |
| Website Builder | /features/booking-website-builder |
| Mobile App | /features/mobile-app |
| View all features | /features |

## Resources menu

| Item | Opens |
|---|---|
| About | /about |
| Support | https://help.acuityscheduling.com/ (Zendesk). Off-site help. Recorded, not walked. |
| Forum | https://forum.acuityscheduling.com/ . Off-site. Recorded, not walked. |
| Blog | /learn |
| Events | /learn/acuity-scheduling-events |
| Developers | https://developers.acuityscheduling.com/ . Off-site docs. Recorded, not walked. |

## Home page interactions

| Control | Opens |
|---|---|
| Sign up with email | /get-started?signupMethod=email then Squarespace signup. **Wall. Stop.** |
| Sign up with Google | /get-started?signupMethod=google then Squarespace signup. **Wall. Do not click Google.** |
| Industry cards (Beauty, Business Services, Wellness, Fitness, Education, Visual and Performing Arts) | The matching /solutions/ page |
| LEARN MORE on the three feature tiles | /features/no-show-prevention, /features/task-automation, /features/revenue-growth |
| Read story (carousel) | A /learn/ case-study article. Representative article captured. |
| Carousel dots | Change the visible testimonial slide. Same page. |
| Create your free booking page / Get started for free | Squarespace signup. **Wall. Stop.** |
| Terms of Service, Privacy Policy | squarespace.com. Off-site. Not captured. |

## Pricing

| Control | Opens |
|---|---|
| Pay annually / Pay monthly | Segmented control. Same page, prices swap. No navigation. |
| Plan CTA (Get started) | Squarespace signup. **Wall. Stop.** |
| Feature name with a tooltip (`span.feature-tooltip-trigger`) | Tooltip on hover or focus. Same page. |
| FAQ accordion (`button.accordion-title`) | Expands that answer. Same page. |
| Enterprise FAQ link | /enterprise |

## Feature, solution, and compare pages

Each feature and solution page repeats the marketing shell, a hero, a carousel of logos (`button` Previous / Next), an FAQ accordion, and Get started links that hit the signup wall.

Feature paths reached from the home page, menus, or footer: online-booking, client-management, class-scheduling, payments, invoicing-software, point-of-sale, calendar-management, availability-controls, booking-website-builder, mobile-app, staff-management, appointment-reminders, client-loyalty, how-acuity-works, no-show-prevention, task-automation, revenue-growth.

Compare paths from the footer: /compare/acuity-vs-calendly, /compare/acuity-vs-vagaro.

## Learn

| Control | Opens |
|---|---|
| Category chips | /learn/category/Start Scheduling, Save Time, Book Clients, Get Paid, Grow Your Business, Success Stories, Product Features, Tailored Tips |
| Article card | /learn/<slug>. Representative article captured. The rest are the same article template. |
| Events card | /learn/acuity-scheduling-events |

No search field on the public learn index.

## Integrations

| Control | Opens |
|---|---|
| Logo carousel Next / Previous | Next set of partner logos. Same page. |
| A partner card | A help.acuityscheduling.com article. Off-site. Recorded, not walked. |

No on-page search or filter on the public integrations index.

## About

FAQ accordion plus the shared shell. No form.

## Enterprise

| Control | Opens |
|---|---|
| Key-benefit buttons | Swap the active benefit panel. Same page. |
| Testimonial arrows | Next or previous quote. Same page. |
| FAQ accordion | Expands that answer. Same page. |
| Contact form (`#enterprise-contact-form`, posts to webto.salesforce.com) | Lead form: name, email, phone, company, and a submit button. **Not filled. Not submitted.** |

## Account walls (stop)

| URL | What it asks | Action |
|---|---|---|
| https://www.acuityscheduling.com/login.php | Email and password, Continue with Acuity Scheduling, Continue with Squarespace, Forgot Password | Record the URL. Do not type. Do not click Squarespace. |
| https://www.acuityscheduling.com/forgotpass.php | Password recovery. Linked from login.php. | Not opened. Recovery is a credential flow. |
| https://secure.acuityscheduling.com/login | Redirects to login.squarespace.com. Email, password, Google, Apple, Facebook. | Record the URL. Do not type. Do not click Google, Apple, or Facebook. |
| https://www.acuityscheduling.com/get-started | Redirects to login.squarespace.com signup. Google, Apple, email, MORE OPTIONS. | Record the URL. Do not type. Do not click Google or Apple. Do not open MORE OPTIONS into a signup form. |

## Off-site and dead links

| Target | Note |
|---|---|
| help.acuityscheduling.com, forum.acuityscheduling.com, developers.acuityscheduling.com | Separate products. Recorded as boundaries. |
| squarespace.com (terms, privacy, careers, imprint, webinars, experts) | Off-site. Not captured. |
| status.acuityscheduling.com | Status page. Off-site. Not captured. |
| /cart, /docs/*, /hc/* on www.acuityscheduling.com | 404. Those paths belong on the help host. |

## Dark theme

No theme switch on the public site. One light theme.
