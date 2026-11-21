# Mangomint public site tree

Mapped from https://www.mangomint.com/ in headless Chromium on 2026-11-21, before screenshots. Desktop viewport 1440x900. Phone drawer checked at 390x844. No form was submitted. No password, code, or profile field was filled.

The marketing site is one light theme (`color-scheme: normal`). There is no theme switch. The signed-in product lives at `https://app.mangomint.com/` and redirects to a login form. That branch stops.

## Top bar (desktop)

The bar is always visible. Menus are buttons, not links. Pricing, Log in, and Book a demo are links.

| Control | Opens |
|---|---|
| Logo | https://www.mangomint.com/ |
| Businesses (button) | Menu of 12 solution pages. See Businesses menu. |
| Features (button) | Menu of 20 feature pages. See Features menu. |
| AI Receptionist (button) | Menu with one public link, Learn more, which leaves the site for Meet Mira. See AI Receptionist menu. |
| Pricing | https://www.mangomint.com/pricing/ |
| Log in | https://app.mangomint.com/ (redirects to https://app.mangomint.com/login). Login wall. Stop. |
| Book a demo | https://www.mangomint.com/demo/ |
| Toggle the navigation | Hidden at 1440. At 390 it opens the phone drawer. |

## Businesses menu

Button label: Businesses. Section label on the panel: SOLUTIONS FOR…. Each row is a link.

| Label | Opens |
|---|---|
| Hair Salons | https://www.mangomint.com/solutions/hair-salon-software/ |
| Med Spas | https://www.mangomint.com/solutions/medical-spa-software/ |
| IV Therapy | https://www.mangomint.com/solutions/iv-therapy-software/ |
| Skincare Studios | https://www.mangomint.com/solutions/skincare-studio-software/ |
| Beauty Studios | https://www.mangomint.com/solutions/beauty-studio-software/ |
| Massage Studios | https://www.mangomint.com/solutions/massage-studio-software/ |
| Hair Removal | https://www.mangomint.com/solutions/hair-removal-studio-software/ |
| Tattoo & Piercing | https://www.mangomint.com/solutions/tattoo-piercing-studio-software/ |
| Nail Salons | https://www.mangomint.com/solutions/nail-salon-software/ |
| Barbershops | https://www.mangomint.com/solutions/barbershop-software/ |
| Wellness Centers | https://www.mangomint.com/solutions/wellness-center-software/ |
| Spas | https://www.mangomint.com/solutions/spa-software/ |

Sitemap also lists two solution pages that are not in this menu: `/solutions/highest-rated-aesthetics-practice-emr/` and `/solutions/highest-rated-med-spa-emr-system/`.

## Features menu

Button label: Features. Groups on the panel: SCHEDULING & PAYMENTS, CLIENT RELATIONSHIPS, MARKETING & AUTOMATION, MANAGEMENT.

| Label | Opens |
|---|---|
| Calendar & Scheduling | https://www.mangomint.com/features/scheduling/ |
| Payments & Point-of-Sale | https://www.mangomint.com/payments/ |
| Online Booking | https://www.mangomint.com/features/online-booking/ |
| Express Booking | https://www.mangomint.com/features/express-booking/ |
| Mobile Apps | https://www.mangomint.com/features/mobile-apps/ |
| Client Management | https://www.mangomint.com/features/client-management/ |
| Phone | https://www.mangomint.com/features/phone/ |
| Memberships & Packages | https://www.mangomint.com/features/memberships-and-packages/ |
| Forms & Charting | https://www.mangomint.com/features/integrated-forms/ |
| Gift Cards | https://www.mangomint.com/features/gift-cards/ |
| Automated Flows | https://www.mangomint.com/features/automated-flows/ |
| Campaigns | https://www.mangomint.com/features/campaigns/ |
| Offers & Discounts | https://www.mangomint.com/features/offers-and-discounts/ |
| Virtual Waiting Room | https://www.mangomint.com/features/virtual-waiting-room/ |
| Retail & Inventory | https://www.mangomint.com/features/retail-and-inventory/ |
| Staff Management | https://www.mangomint.com/features/staff-management/ |
| Reporting | https://www.mangomint.com/features/reporting/ |
| Multi-Location | https://www.mangomint.com/features/multi-location/ |
| Payroll Processing | https://www.mangomint.com/features/payroll-processing/ |
| Integrations | https://www.mangomint.com/integrations/ |

Sitemap also lists `/features/why-mangomint/`, which is not in this menu. The public comparison page linked from the footer is https://www.mangomint.com/why-mangomint/.

## AI Receptionist menu

Button label: AI Receptionist. The panel's public link is Learn more. The homepage banner also has a Meet Mira link. Both leave mangomint.com for https://www.meetmira.com/ with referral query parameters. That host is a different product and was not captured.

## Phone drawer (390)

Control: button `aria-label="Toggle the navigation"`. Opens a full-height drawer that repeats Pricing, the 12 solution links, the 20 feature links, Learn more (Meet Mira), Log in, and Book a demo. Closing is the same toggle.

## Homepage interactions

| Control | Opens |
|---|---|
| WATCH A VIDEO TOUR (button, class `videoSelectionButton`) | A dialog titled "Which best describes your business?" with 12 business-type choices and a Watch video button. Shot: `screenshots/home-light-video-tour.png`. No type was selected and Watch video was not pressed. That choice is a survey step, so the video itself was not reached. |
| Carousel tabs: CALENDAR, AI RECEPTIONIST, ONLINE BOOKING, SALES & POS, PHONE, MARKETING (and matching Slide 0–5 buttons) | Switches the hero product demo on the same page. Public demo, not the signed-in app. |
| Wistia buttons (customer names and studio names) | Intended testimonial video popover. Not opened: third-party player, and several labels include a person's name. |
| Try it now | https://www.mangomint.com/trial/ |
| Why We're Different | https://www.mangomint.com/why-mangomint/ |
| Watch a video tour (link) | https://www.mangomint.com/tour/ |
| Footer Blog | https://www.mangomint.com/blog/ |
| Footer Video Library | https://www.mangomint.com/videos/ |
| Footer Learning Center | https://www.mangomint.com/learn/ |
| Footer About Us | https://www.mangomint.com/about-us/ |
| Footer Careers | https://www.mangomint.com/careers/ |
| Footer Platform Updates | https://www.mangomint.com/updates/ |
| Footer Contact Us | https://www.mangomint.com/contact-us/ |
| Footer Legal | https://www.mangomint.com/legal/privacy-policy/ |
| Footer Terms of Service | https://www.mangomint.com/legal/website-terms-of-use/ |
| Footer Security Report Policy | https://www.mangomint.com/security/ |
| Footer social links | Instagram, TikTok, Facebook, LinkedIn, YouTube. Off-site. Not captured. |

## Pricing page

https://www.mangomint.com/pricing/

| Control | Opens |
|---|---|
| Decrease / Increase Locations, Users, Lines | Same-page calculator. No submit. |
| Add Phone, No credits, Add Payroll | Same-page calculator toggles. |
| Decrease / Increase Workers | Same-page calculator. |
| Scheduling & Payments, Client Relationships, Management | Same-page feature groups. |
| Book a demo / Try it now | The demo and trial walls below. |

No FAQ accordion was present as a separate dialog on the first paint. The calculator is the interaction.

## Contact page

https://www.mangomint.com/contact-us/

The page prints a published support email and a "give us your number" prompt. No screenshot of this page is kept. Start a chat did not mount a widget in headless Chromium. No message was typed. Book a demo on this page opens the demo wall.

## Walls (recorded, then stopped)

| Control | URL | What it asks | Action |
|---|---|---|---|
| Log in | https://app.mangomint.com/login | Email address and Password fields, Log In button, Forgot password link. | Stop. No credentials entered. |
| Book a demo | https://www.mangomint.com/demo/ | "Book a demo". Step asks "What services do you offer?" then Continue. | Stop. No option selected, Continue not pressed. |
| Try it now | https://www.mangomint.com/trial/ | "Try for free". "STEP 1 OF 5". Asks which services you offer, then Continue. | Stop. No option selected, Continue not pressed. |
| Personalized demo links | `/demo/a/[id]/`, `/demo/c/[id]/` | Sitemap placeholders for booked demos. | Not opened. |
| Trial variants | `/trial/c/`, `/trial/r/` | Same signup flow. | Not opened. |
| Meet links | `/meet/<name>/` (31 paths) | Named booking pages. | Not opened. Names stay out of the package. |
| Referral links | `/referral/<slug>/` (82 paths) | Partner landing pages. | Not captured as a set. One public page is enough to see the pattern is a campaign, not a new component. |
| Giveaways | `/synergy-giveaway/`, `/growth-factor-giveaway/`, `/monday-club-giveaway/` | Entry forms. | Not opened. No form submitted. |
| Go landings | `/go/*` (33 paths) | Paid and competitor landing pages, including a customer referral form. | Not captured. The referral form would ask for someone else's contact details. |

## Content indexes (public, no submit)

| Index | URL | What a row opens |
|---|---|---|
| Blog | https://www.mangomint.com/blog/ | An article, or an author page, or a category (`/blog/c/company/`, `features`, `guides`, `industry`, `tools`). 162 article paths in the sitemap. |
| Learning Center | https://www.mangomint.com/learn/ | A help article. 460 paths. |
| Video Library | https://www.mangomint.com/videos/ | A feature-spotlight page with an embedded player. 48 paths. |
| Platform Updates | https://www.mangomint.com/updates/ | Same-page changelog. |
| Integrations | https://www.mangomint.com/integrations/ | Partner list on one page. |
| About | https://www.mangomint.com/about-us/ | Marketing page. |
| Careers | https://www.mangomint.com/careers/ | Job list. An apply control that leaves the site or asks for a profile is a wall and is not followed. |
| Security | https://www.mangomint.com/security/ | Policy page. The first screen prints a street address. Not screenshotted. |
| Legal | `/legal/privacy-policy/`, `/legal/website-terms-of-use/`, `/legal/data-processing/`, `/legal/payments-terms/`, `/legal/platform-terms/`, `/legal/platform-terms/additional-product-terms/` | Long-form policy. The privacy page links a published email. Not screenshotted. |

## Sitemap remainder

https://www.mangomint.com/sitemap-0.xml lists 899 URLs. The rest are campaign slugs (`/mira/`, `/meetmira/`, `/partnerships/`, partner name pages) and the walls above. They do not add a new control type beyond a marketing page or a form wall.
