# Calm public site tree

Mapped signed out on 2026-11-21 from [https://www.calm.com/](https://www.calm.com/) in headed Chrome at 1440×900. The cookie banner was hidden and never accepted or rejected. No email, password, name, or code was typed. No identity provider was clicked. No form was submitted. Login and signup branches stop at the wall.

At 1169 wide the header drops Sleep, Stress & Anxiety, and Mindfulness and shows the mobile menu button. Those three are desktop controls. The 390 menu was not opened in this pass: a later load hit PerimeterX ("Access to this page has been denied") and was not solved.

## Header, desktop 1440

The header sits over the homepage hero. Logo is a link. The rest of the visible chrome is buttons.

| Control | Opens |
|---|---|
| Logo (aria-label "Calm Logo - Link to calm.com Homepage") | https://www.calm.com/ |
| Sleep | Leaves the homepage. Destination recorded in the shot pass. Prior public capture of the signed-out shell is `/app/sleep`. |
| Stress & Anxiety | Same kind of button as Sleep. Not opened in the map pass. |
| Mindfulness | Same kind of button as Sleep. Not opened in the map pass. |
| Screening | https://screening.calm.com/ (public marketing page, title "Calm") |
| Calm Health | Menu, overlay on the homepage. See below. Escape closes it. |
| Log In (`data-testid="desktopnav-login-button"`) | Login card or page. Branch stopped. Not submitted. |
| Try Calm for Free | Signup wall. Branch stopped. Not submitted. |
| Open Mobile menu (`aria-controls="mobile-menu"`) | Hidden at 1440. Shown when the header collapses. |

Calm Health's closed menu still holds two links in the DOM: For Individuals (`https://app.calmhealth.com/`) and For Organizations (`https://health.calm.com/`). Clicking Calm Health sets `aria-expanded="true"` and shows both.

## Calm Health menu

Opened by clicking Calm Health. The panel is about 187×118, under the trigger.

| Item | Opens |
|---|---|
| For Individuals | https://app.calmhealth.com/ (account wall; not followed) |
| For Organizations | https://health.calm.com/ (public B2B site; not followed in this pass) |

## Screening

Header Screening navigates to https://screening.calm.com/. The page asks "How are you feeling right now?" and describes a GAD-7 and PHQ-8 screening for U.S. residents age 18 and older. Get Started links to `https://app.calmhealth.com/mental-health-screening`. That link was not opened. The quiz was not started.

The same header is on that host. Sleep, Stress & Anxiety, and Mindfulness are buttons there too. Footer on screening.calm.com repeats the calm.com columns, with Family Plan resolving on screening.calm.com and an extra Your Privacy Choices link to https://www.calm.com/optout.

## Homepage body

Visible controls under the hero, read on the signed-out page. None of these were submitted.

| Control | What it is |
|---|---|
| Skip to main content | In-page link to `#main-content` |
| Try Calm for Free | Second copy of the header signup control |
| Already have an account? | Button beside the hero signup control. Not clicked. |
| Stress less. / Learn More | Card button. Not opened in the map pass. |
| Sleep more. / Learn More | Card button. Not opened in the map pass. |
| Live mindfully. / Learn More | Card button. Not opened in the map pass. |
| previous / next | Review carousel arrows |
| Yearly plan (`data-testid="plan-sku-item-yearly"`) | Plan card on the homepage. Not selected as a purchase. |
| Terms | https://www.calm.com/terms |
| Cancel anytime | https://support.calm.com/hc/en-us/articles/115002473607-How-to-turn-off-auto-renewal-or-cancel-my-subscription |
| Continue | Button under the plan card. Not clicked. Would start checkout or signup. |
| Blog cards | Links under `/blog/…` |
| See all blogs | https://calm.com/blog |
| Cookie banner exit | Closes the cookie sheet. Not clicked. The sheet was hidden. |

## Cookie sheet

`#cookie-preferences-banner` paints on load. Copy says Calm and its advertising and analytics partners use cookies, and that using the site agrees to the Privacy Policy. Controls: Privacy Policy (`/privacy-policy`) and a button labelled exit. Hidden, never answered. Footer "Opt Out of Targeted Ads" has `aria-controls="cookie-preferences-banner"` and was not clicked.

## Footer

Columns on the homepage. Social icons have aria-labels and no `href` in the DOM (Facebook, Instagram, Twitter). They were not clicked.

| Column | Control | Opens |
|---|---|---|
| Company | About | https://www.calm.com/blog/about |
| Company | Careers | https://www.calm.com/careers |
| Company | Press | https://www.calm.com/blog/press |
| Company | Blog | https://www.calm.com/mindfulness-tips |
| Company | Meet our Instructor | https://www.calm.com/blog/tamara-levitt |
| Company | Calm Science | https://www.calm.com/science |
| Gifts | Buy a Gift | https://www.calm.com/gift |
| Gifts | Redeem a Gift | https://www.calm.com/redeem |
| Gifts | Family Plan | /family |
| Organizations | Organizations under 300 | https://health.calm.com/calm-for-organizations/ |
| Organizations | Organizations 300+ | https://health.calm.com/ |
| Support | FAQ | https://www.calm.com/faq/web |
| Support | Contact Us | https://support.calm.com/hc/en-us/requests/new |
| Legal | Terms | https://www.calm.com/terms |
| Legal | Privacy Policy | /privacy-policy |
| Legal | Consumer Health Data | /calm-consumer-health-data-privacy-policy |
| Legal | CCPA Notice | /privacy-policy#information-for-california-residents |
| Legal | Opt Out of Targeted Ads | Cookie preferences banner. Not opened. |
| Legal | Cookies | https://www.calm.com/cookies |
| Legal | Accessibility Statement | https://www.calm.com/accessibility-statement |
| Legal | Virtual Patent Marking | https://www.calm.com/patents |

## Walls, not followed

| Control | Stops at |
|---|---|
| Log In | Login card or page. Empty. Not submitted. |
| Try Calm for Free, hero Try Calm for Free, Continue | Signup or checkout. Not submitted. |
| For Individuals | https://app.calmhealth.com/ |
| Get Started on screening | https://app.calmhealth.com/mental-health-screening |
| Contact Us | Support request form. Not opened. |
