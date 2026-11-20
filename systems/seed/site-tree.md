# Seed site tree

Mapped from https://seed.com/ on 2026-11-21 in headless Chromium, before screenshots. Desktop 1440 x 900, phone 390 x 844. OneTrust cookie banner was hidden, never clicked. No form was submitted. No email, password, code, or profile field was typed.

The marketing site is one light theme (`color-scheme: normal`). There is no dark toggle. Phone width replaces the Shop / Science / Learn buttons with an Open menu control. Account, checkout, and quiz answers sit behind a wall and were not walked.

## Shell

| Control | Opens | Stop |
|---|---|---|
| Logo (Home) | https://seed.com/ | Public |
| Shop button (`aria-controls=panel-shop`) | Mega menu, not a page | Public links below |
| Science button (`aria-controls=panel-science`) | Mega menu | Public links below |
| Learn button (`aria-controls=panel-learn`) | Mega menu | Public links below |
| Sign in button | Overlay on the current page: "Welcome back. Enter your email to access your account." Email field and Continue. Same overlay is the known login wall. | Stop. Do not type an email. Continue not pressed. |
| Cart button (product and shop pages) | Cart dialog: "Your Cart. Your cart is empty. Total $0.00. Checkout" | Empty cart captured. Checkout not pressed (would leave the public cart). |
| Open menu (phone only, `aria-label=Open menu`) | Full-screen menu of the same destinations as the footer | Public |
| USD / United States (`aria-label=Country and currency`) | Listbox: CAD / Canada, USD / United States | Opened, not changed. No address typed. |
| Cookie Settings / OneTrust banner | Consent preferences | Hidden, never clicked. |
| Pause animations / Play or pause video | Local motion toggle | Public, no navigation |
| Newsletter "Sign up for our Newsletter" + Subscribe | Footer form | Not typed, not submitted |
| Press and Cultured "Email" + Sign Up | Separate newsletter form on those templates | Not typed, not submitted |

## Shop menu (`#panel-shop`)

| Link | URL |
|---|---|
| DS-01 Daily Synbiotic | https://seed.com/daily-synbiotic |
| DM-02 Daily Multivitamin | https://seed.com/daily-multivitamin |
| Daily Essentials Duo | https://seed.com/daily-essentials-duo |
| AM-02 Energy + Focus | https://seed.com/energy-focus |
| PM-02 Sleep + Restore | https://seed.com/sleep-restore |
| PDS-08 Pediatric Daily Synbiotic | https://seed.com/pds08-daily-kids-probiotic |
| VS-01 Vaginal Synbiotic | https://seed.com/vaginal-synbiotic |
| Shop All Products | https://seed.com/products |

## Science menu (`#panel-science`)

| Link | URL |
|---|---|
| Approach | https://seed.com/approach |
| SeedLabs | https://seed.com/seedlabs |
| Scientists | https://seed.com/approach#our-scientists |
| Sustainability | https://seed.com/sustainability |
| DS-01 reference | https://seed.com/reference/syn-wk |
| DM-02 reference | https://seed.com/reference/dm-wk |
| AM-02 reference | https://seed.com/reference/am-wk |
| PM-02 reference | https://seed.com/reference/pm-wk |
| PDS-08 reference | https://seed.com/reference/pds-wk |
| VS-01 reference | https://seed.com/reference/vs-wk |

## Learn menu (`#panel-learn`)

| Link | URL |
|---|---|
| Microbiome 101 | https://seed.com/cultured/microbiome-101 |
| Probiotics 101 | https://seed.com/cultured/probiotics-101 |
| Featured article (probiotic research) | https://seed.com/cultured/how-seed-is-fixing-probiotic-research |
| Featured article (carbon expedition) | https://seed.com/cultured/carbon-four-expedition |
| Featured article (body microbiomes) | https://seed.com/cultured/microbiomes-of-the-body |
| All Cultured articles | https://seed.com/cultured |

## Home body

| Control | Opens |
|---|---|
| Take the Quiz / Discover (quiz promo) | https://seed.com/is-ds01-right-for-you (hash quiz step) |
| Shop DS-01 | https://seed.com/daily-synbiotic |
| Shop Now on each product card | That product's page |
| Shop All | https://seed.com/products |

## Product page (example: /daily-synbiotic)

| Control | Opens | Notes |
|---|---|---|
| View larger image | Image dialog | Public |
| Benefits / Ingredients / View Clinical Trials / See Clinical Evidence | In-page tabs or anchors | Public |
| Start Now | Purchase path | Not followed (checkout / account) |
| Add To Cart (shop grid) | Cart dialog | Not used to start checkout |
| Join the Waitlist / Join International Waitlist | Account or waitlist form | Wall. Not filled. |
| Sort by: Highest rating | Review sort combobox | Public local control |
| Search reviews | Filter field | Not typed (would be a search submit) |
| Close popup | Dismisses an in-page explainer | Public |

## Quiz

https://seed.com/is-ds01-right-for-you loads as a 13-step quiz (`#how_often_poop_page` on arrival). First screen buttons: "1-2 times a day", "A few times a week", "Once a week", "Other". Continuing collects health answers. Not answered. https://seed.com/find-your-routine is a second quiz (`#what_matters_most`). Not answered.

## Footer (also the phone menu)

| Link | URL | Notes |
|---|---|---|
| Refer a Friend (Superfiliate) | https://seed.superfiliate.com/portal/sign-up | External signup. Not filled. |
| Partner (Impact) | https://app.impact.com/campaign-promo-signup/Seed-Health-Inc.brand | External signup. Not filled. |
| Practitioners | https://seed.com/practitioners | Public page. Connect form not filled. |
| Press | https://seed.com/press | Public |
| Careers | https://seed.com/join-us | Public. Job application links not followed into a form submit. |
| Help | https://help.seed.com/ | Public help center |
| Contact | https://help.seed.com/en-US/contact | Contact form. Not filled. |
| My Account | https://seed.com/account/home | Redirects to https://seed.com/login?redirect=%2Faccount%2Fhome. Email step. Stop. |
| Refer | https://seed.com/account/refer | Redirects to login. Stop. |
| International | https://seed.com/entire-world | Public shipping page |
| Instagram / Twitter / LinkedIn | External social | Not captured as product UI |
| Terms + Conditions | https://seed.com/terms-conditions | Public |
| Privacy Policy | https://seed.com/privacy-policy | Public |
| Accessibility | https://seed.com/accessibility | Public |
| Consent Preferences | `#` OneTrust | Not clicked |

## Other public pages reached from those

| URL | What it is |
|---|---|
| https://seed.com/subscription-terms | Linked from terms |
| https://seed.com/consumer-health-data | Linked from the quiz disclaimer |
| https://seed.com/ccpa-notice-applicants | Linked from privacy |
| https://seed.com/ccpa-notice-independent-contractors | Linked from privacy |
| https://seed.com/seeduniversity | Linked from press/cultured footer |
| https://seed.com/cultured/category/* | Cultured category indexes |
| https://seed.com/login | Standalone "Hi, sign in." email step |

## Walls (recorded, not entered)

| Entry | Lands on | Why stopped |
|---|---|---|
| Sign in button | Overlay on https://seed.com/ asking for email, then Continue | Known login wall. Email not typed. Password step not reached. Google and Facebook not clicked. |
| https://seed.com/login | https://seed.com/login "Hi, sign in." email field | Same wall |
| https://seed.com/account/home | https://seed.com/login?redirect=%2Faccount%2Fhome | Same wall |
| https://seed.com/account/refer | https://seed.com/login?redirect=%2Faccount%2Frefer | Same wall |
| https://seed.com/cart and https://seed.com/checkout | Redirect to https://seed.com/products | No public cart URL. Cart dialog is the public cart. |
| Quiz answer buttons | Next health question | Health survey. Not answered. |
| Practitioner connect, newsletter, contact, waitlist, partner, refer signup | Forms that ask for email or profile | Not typed, not submitted. |
