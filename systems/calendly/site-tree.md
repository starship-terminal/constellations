# Calendly public site tree

Mapped from https://calendly.com/ on 2026-11-21 in headless Chromium, signed out, at 1440×900. Cookie banners were hidden and never clicked. No form was submitted. Identity providers were recorded and not opened. Login and signup branches stop at the empty email wall.

The homepage header, footer, and three mega menus are the whole public tree. Later pages repeat that chrome and add in-page controls.

## Header

The sticky header (`#site-header`, 68px) sits on every marketing page.

| Control | Opens |
|---|---|
| Logo | https://calendly.com/ |
| Product (hover) | Mega menu, overlay. See below. |
| Solutions (hover) | Mega menu, overlay. See below. |
| Resources (hover) | Mega menu, overlay. See below. |
| Pricing | https://calendly.com/pricing |
| Talk to sales | https://calendly.com/contact |
| Log In | https://calendly.com/login (email wall; branch stopped) |
| Get started for free | https://calendly.com/signup (email wall; branch stopped) |
| Open menu (390px only) | Full-screen nav drawer. See Mobile. |

My Account (`/event_types/user/me`) is in the DOM and not visible while signed out. It is an account wall. Branch not followed.

## Product menu

Opened by hovering Product. A scrim (`Close navigation`) covers the page. Escape or moving away closes it.

| Item | Opens |
|---|---|
| Scheduling | https://calendly.com/scheduling |
| Callie (Beta) | https://calendly.com/ai-assistant |
| Notetaker | https://calendly.com/notetaker |
| Contacts | https://calendly.com/contacts |
| Payments | https://calendly.com/payments |
| Integrations | https://calendly.com/integration |
| Security | https://calendly.com/security |
| Mobile app | https://calendly.com/features/mobile-apps |
| Browser extension | https://calendly.com/features/browser-extensions |
| Admin controls | https://calendly.com/features/admin-management |
| Sign up with email | https://calendly.com/signup (email wall; stopped) |

## Solutions menu

| Item | Opens |
|---|---|
| Individuals | https://calendly.com/solutions/individuals |
| Small business | https://calendly.com/solutions/small-business |
| Large companies | https://calendly.com/solutions/enterprise |
| Sales | https://calendly.com/solutions/sales |
| Marketing | https://calendly.com/solutions/marketing |
| Customer success | https://calendly.com/solutions/customer-success |
| Recruiting | https://calendly.com/solutions/recruiting |
| Education | https://calendly.com/solutions/education |
| Technology | https://calendly.com/solutions/technology |
| Financial Services | https://calendly.com/solutions/financial-services |
| Professional Services | https://calendly.com/solutions/professional-services |
| Sign up with email | https://calendly.com/signup (stopped) |

## Resources menu

| Item | Opens |
|---|---|
| Learning hub | https://calendly.com/learn |
| Developer docs | https://developer.calendly.com/ (external) |
| Product tour | https://calendly.com/demo |
| Blog | https://calendly.com/blog |
| Guides & webinars | https://calendly.com/resources |
| About us | https://calendly.com/about |
| What's new | https://calendly.com/release-notes |
| Customer stories | https://calendly.com/customers |
| Newsroom | https://calendly.com/newsroom |
| Help center | https://calendly.com/help |
| Community | https://community.calendly.com/ (external) |
| Contact us | https://calendly.com/contact-us |
| Sign up with email | https://calendly.com/signup (stopped) |

## Footer

Repeated on marketing pages. Columns, then store badges, socials, and the legal row.

| Column | Control | Opens |
|---|---|---|
| Product | Scheduling | /scheduling |
| Product | AI assistant | /ai-assistant |
| Product | Notetaker | /notetaker |
| Product | Contacts | /contacts |
| Product | Payments | /payments |
| Product | Security | /security |
| Features | Customizable availability | /scheduling/availability |
| Features | Event types | /scheduling/event-types |
| Features | Meeting polls | /scheduling/meeting-polls |
| Features | Reminders & follow up | /scheduling/automated-communication |
| Features | Meeting routing | /scheduling/routing |
| Features | Analytics | /features/analytics |
| Features | Admin management | /features/admin-management |
| Integrations | Google ecosystem | /integration?search=google |
| Integrations | Microsoft ecosystem | /integration?search=microsoft |
| Integrations | Video conferencing | /integration#video-conferencing |
| Integrations | Payment processors | /integration#payments |
| Integrations | Sales & CRM | /integration#sales-and-crm |
| Integrations | Recruiting & ATS | /integration#recruiting-and-ats |
| Integrations | All integrations | /integration |
| Solutions | For individuals | /solutions/individuals |
| Solutions | For teams | /solutions/small-business |
| Solutions | For large companies | /solutions/enterprise |
| Resources | Create your account | /signup (stopped) |
| Resources | Pricing and plans | /pricing |
| Resources | Product tour | /demo |
| Resources | What's new | /release-notes |
| Resources | Getting started guide | /learn/getting-started |
| Resources | Calendly community | https://community.calendly.com/ |
| Resources | Developer tools | https://developer.calendly.com/ |
| Resources | Help center | /help |
| Resources | Learning hub | /learn |
| Resources | Contact support | /help/support |
| Resources | Contact sales | /contact |
| Company | About us | /about |
| Company | Careers | /careers |
| Company | Become a partner | /partners/contact |
| Company | Blog | /blog |
| Stores | Apple, Google Play, Edge, Safari, Chrome, Firefox, Outlook | Store listings (external) |
| Social | X, Instagram, Facebook, LinkedIn, YouTube | External profiles |
| Legal | English | Language listbox (overlay; not changed) |
| Legal | Privacy Policy | /legal/privacy-notice |
| Legal | Legal | /legal |
| Legal | Status | https://www.calendlystatus.com/ |
| Legal | Cookie Settings | OneTrust preference center (not opened; banner was hidden) |
| Legal | Your Privacy Choices | OneTrust overlay (not opened) |

## Homepage in-page controls

| Control | Opens |
|---|---|
| Sign up with Google | Identity provider. Not opened. |
| Sign up with Microsoft | Identity provider. Not opened. |
| Sign up with email | /signup (stopped) |
| Previous product / Next product | In-page product carousel (Scheduling, Callie, Notetaker, Payments) |
| Scheduling, Callie, Notetaker, Payments chips | Same carousel, in page |
| Feature accordions (calendar, templates, workflows, embeds, mobile, teams) | In-page panels; links go to /scheduling |
| Conversational scheduling and sibling tabs | In-page; links go to /ai-assistant, /notetaker, /payments |
| Use case 1–5 | In-page story carousel |
| Learn more (scheduling, Callie, notetaker, payments) | Those product pages |
| Start for free | /signup (stopped) |
| View all integrations | /integration |
| Integration logos (Zoom, Google Calendar, Gmail, Meet, Salesforce, Slack, Teams, Outlook, Chrome, ChatGPT, Claude, HubSpot, Greenhouse, LinkedIn, Stripe, PayPal, Zapier, Google, Microsoft) | /integration/<name> or a help article |
| Chat bubble | Overlay. Not opened. |

## Pricing

https://calendly.com/pricing. Plan cards (Free, Standard, Teams, Enterprise). Each paid plan's CTA is Get started (/signup, stopped) or Talk to sales (/contact). FAQ rows open in page. No billing-period toggle was found. No checkout was started.

## Other marketing pages

Each repeats the header and footer. In-page CTAs are Get started (/signup, stopped), Talk to sales (/contact), or a deeper marketing URL.

| Page | In-page |
|---|---|
| /scheduling | Feature sections; links to /scheduling/availability, event-types, meeting-polls, automated-communication, routing |
| /ai-assistant | Callie marketing |
| /notetaker | Recap marketing |
| /contacts | Relationship tools |
| /payments | Payment marketing |
| /integration | Directory; each card opens /integration/<slug> |
| /integration/zoom and sibling slugs | One page per integration; Connect or Get started goes to /signup (stopped) |
| /security | Security marketing |
| /features/mobile-apps, /features/browser-extensions, /features/admin-management, /features/analytics | Feature pages |
| /solutions/* | One page per audience and industry listed in the Solutions menu |
| /demo | Product tour. No booking widget on the page. |
| /blog | Article index. Individual posts were not opened. |
| /resources | Guides and webinars index |
| /about | Company page; Careers link |
| /release-notes | Product updates |
| /customers | Story index; story cards open /customers/<slug> |
| /newsroom | Press index |
| /help | Help search and category links under /help/<topic> |
| /help/support | Contact support. Form not submitted. |
| /learn, /learn/getting-started | Learning hub |
| /contact | Sales contact. Form not submitted. |
| /contact-us | Support contact. Form not submitted. |
| /careers | Jobs index. Applications not opened. |
| /partners/contact | Partner form. Not submitted. |
| /legal, /legal/privacy-notice | Legal index and privacy notice |

Help, blog, and customer-story indexes continue for many more articles. Those are the same template. The crawl recorded 48 pages and left the rest of the index queues unopened.

## Public booking

https://calendly.com/calendly is a public scheduling profile (display name "calendly ts"). It does not require an account.

| Control | Opens |
|---|---|
| Powered by Calendly | https://calendly.com/ |
| Event row "TS" | https://calendly.com/calendly/ts (date picker) |
| Cookie settings | OneTrust. Not opened. |
| Privacy Policy | /legal/privacy-notice |

The date picker (/calendly/ts) shows November 2026 with no open times. Previous and next month are disabled. Time-zone control is on the page. No slot was selected and no booking form was opened, because no slot was available. A booking form was not submitted.

## Mobile (390)

Open menu opens a drawer: Product, Solutions, and Resources as accordions, Pricing, Talk to sales, Log In, Get started for free, and a close button. Accordion rows open the same destinations as the desktop menus. Log In and Get started stop at the email walls.

## Stopped branches

| Control | URL | Why stopped |
|---|---|---|
| Log In, Continue with email | /login and /app/login | Email wall. See login-review.json. |
| Get started, Sign up, Continue with email | /signup and /app/signup | Email wall. Name and password sit behind it. Not reached. |
| Google, Microsoft, Apple, Facebook, LinkedIn, SSO buttons | Identity provider | Not opened. |
| My Account | /event_types/user/me | Signed-in app. |
| Cookie Settings, Your Privacy Choices | OneTrust | Banner hidden, not clicked. |
| Sales, support, partner, help forms | /contact, /contact-us, /help/support, /partners/contact | Not submitted. |
| Checkout and trial CTAs | /signup | Stopped at the email wall. No trial started. |
