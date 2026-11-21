# gofundme.com site tree

Mapped 2026-11-21 from https://www.gofundme.com/ in headless Chromium (Playwright), desktop 1440×900 and phone 390×844. www.gofundme.com is the public host. Every control below says what it opens: a page, a menu, an external site, or an auth wall. Auth walls were recorded and not entered. No email, name, password, or code was typed. Google, Apple, and Continue were not clicked. No form was submitted.

The Donate, Fundraise, and About buttons did not open their panels on hover or click in this headless session (`aria-expanded` stayed `false`). The panels stay mounted, so their labels and hrefs were read from the DOM. The Donate panel was photographed by forcing `hrt-header-dropdown-content--open`. That is a reconstruction of the open state, not a click the page accepted. Fundraise and About were read from the same mounted panels. Their forced screenshots also showed the consent card, so those two images were not kept. The phone menu button did open its drawer on a real click.

## Shell (desktop, every consumer page)

| Control | Opens |
|---|---|
| Promo "See the list." | page https://www.gofundme.com/kind-50 (https://www.gofundme.com/kind50 redirects) |
| Promo close | in-page dismiss of the Kind 50 banner. Not clicked on this pass. |
| Logo | page https://www.gofundme.com/ |
| Search | page https://www.gofundme.com/s |
| Donate | in-page menu. Links below. Did not open on hover or click in headless Chromium. |
| Fundraise | in-page menu. Links below. Same headless miss. |
| About | in-page menu. Links below. Same headless miss. |
| Sign in | auth wall https://www.gofundme.com/sign-in |
| Start a GoFundMe | page https://www.gofundme.com/create/fundraiser, which redirects to https://www.gofundme.com/create/fundraiser/category |

On https://www.gofundme.com/c/pricing the same header also shows Giving Funds (a "new" mark) between Fundraise and the logo, and a bell with a badge of 2. The bell was not opened. It is a signed-in-shaped control on a public page. Giving Funds was not followed. The homepage header on this pass did not show either control.

At 390px the header is the search icon, the logo, and a menu button. The menu button opens a drawer on the same URL. The drawer lists Manage your activity, Donate, Fundraise, About, Help Center, Start a GoFundMe, and Sign in. Close (×) dismisses the drawer.

| Drawer control | Opens |
|---|---|
| Manage your activity | auth wall https://www.gofundme.com/sign-in?referrer=manage_activity. Recorded, not opened. |
| Donate / Fundraise / About | in-drawer sections. Their links match the desktop menus. Not expanded on this pass. |
| Help Center | external https://support.gofundme.com/hc/en-us |
| Start a GoFundMe | page https://www.gofundme.com/create/fundraiser |
| Sign in | auth wall https://www.gofundme.com/sign-in |

## Donate menu

| Control | Opens |
|---|---|
| Categories | page https://www.gofundme.com/discover |
| Crisis relief | page https://www.gofundme.com/c/act |
| Social Impact Funds | external https://www.gofundme.org/current-funds/ |
| Supporter Space | page https://www.gofundme.com/c/supporter-space |

## Fundraise menu

| Control | Opens |
|---|---|
| How to start a GoFundMe | page https://www.gofundme.com/c/start |
| Fundraising categories | page https://www.gofundme.com/c/start/fundraising-categories |
| Team fundraising | page https://www.gofundme.com/c/fundraising-tips (the href is /c/fundraising-tips/team; the server redirects) |
| Fundraising Blog | page https://www.gofundme.com/c/blog |
| Fundraising tips | page https://www.gofundme.com/c/fundraising-tips |
| Fundraising ideas | page https://www.gofundme.com/c/fundraising-ideas |
| Charity fundraising | page https://www.gofundme.com/c/start/charity-fundraising |
| Sign up as a nonprofit | page https://www.gofundme.com/c/charity-fundraising |

## About menu

| Control | Opens |
|---|---|
| How GoFundMe works | page https://www.gofundme.com/c/how-it-works |
| GoFundMe Giving Guarantee | page https://www.gofundme.com/c/safety/gofundme-guarantee |
| Supported countries | external https://support.gofundme.com/hc/en-us/articles/360001972748 |
| Pricing | page https://www.gofundme.com/c/pricing |
| Help Center | external https://support.gofundme.com/hc/en-us |
| About GoFundMe | page https://www.gofundme.com/c/about-us |
| Newsroom | page https://www.gofundme.com/c/press |
| Careers | page https://www.gofundme.com/c/careers |
| GoFundMe.org | external https://www.gofundme.org |
| GoFundMe Partnerships | page https://www.gofundme.com/c/partnerships |

## Home https://www.gofundme.com/

| Control | Opens |
|---|---|
| Start a GoFundMe (hero) | page https://www.gofundme.com/create/fundraiser |
| Fundraiser cards in the rails | page https://www.gofundme.com/f/<slug> for that public fundraiser |
| Category chips (memorial, medical, nonprofits) | page under https://www.gofundme.com/c/start/ |
| Learn more about how GoFundMe works | page https://www.gofundme.com/c/how-it-works |

One public fundraiser from the first /f/ card on /discover was opened at rest: https://www.gofundme.com/f/amanda-somerville. Donate now and Share were not pressed.

## Search https://www.gofundme.com/s

The page has a search field ("Find fundraisers, nonprofits, and people") and four tabs: Fundraisers, Nonprofits, Profiles, Communities. The tabs stay on /s. Nothing was typed. Cards open a public /f/<slug> page.

## Discover https://www.gofundme.com/discover

Category tiles (Medical, Memorial, Emergency, Nonprofit, Education, Animal, and more) open a category page. Start a GoFundMe opens the create page. Cards open a public fundraiser.

## Create https://www.gofundme.com/create/fundraiser/category

This is the first step of the public wizard, not an account wall. It asks "Where will the funds go?" with a country select (United States was already selected) and an empty zip field, then category pills (Animals, Business, Community, and the rest). Continue was visible and was not clicked. The zip field was not filled. Sign in in the corner is the auth wall https://www.gofundme.com/sign-in. The branch stops here.

## Footer

The footer repeats the Donate, Fundraise, and About links. Extra links:

| Control | Opens |
|---|---|
| GoFundMe Pro for nonprofits | external https://pro.gofundme.com |
| More resources accordion | in-page. Links to /c/crowdfunding, /c/why-gofundme, /c/questions, /c/success, and blog articles. Not each opened. |
| Facebook, YouTube, X, Instagram | external social profiles |
| Terms | page https://www.gofundme.com/c/terms |
| Privacy Notice | page https://www.gofundme.com/c/privacy |
| Legal | page https://www.gofundme.com/c/legal |
| Accessibility Statement | page https://www.gofundme.com/c/accessibility-statement |
| Cookie Policy | page https://www.gofundme.com/c/gofundme-cookie-policy |
| Your Privacy Choices | page https://www.gofundme.com/c/opt-out-rights |
| Get it on Google Play | external Play Store |
| Available on the App Store | external App Store |
| United States · English | in-page locale control. Not opened. |
| Manage Cookie Preferences | Transcend consent card. Hidden, never answered. |

## Auth walls (stopped)

| Control or URL | Result |
|---|---|
| https://www.gofundme.com/sign-in | auth wall, HTTP 200, title "Sign In". A card says "Welcome. Sign in to GoFundMe or sign up to continue." It offers Sign in with Google, Continue with Apple, an Email Address field, and Continue. Not entered. No identity provider was clicked. Nothing was typed. |
| https://app.gofundme.com/login | HTTP 403 from CloudFront: "The request could not be satisfied." No form. Not entered. |
| Drawer "Manage your activity" | auth wall https://www.gofundme.com/sign-in?referrer=manage_activity. Recorded, not opened. |
| /account/profile, /donations, /sign-out | present as hrefs in the phone drawer markup. Not opened. They are account routes. |

A Google One Tap card ("Sign in to GoFundMe with Google", Continue) painted over the phone homepage. Its request was blocked and the card was not used. Continue was not clicked.

## Not on this tree

Signed-in donations, fundraiser management, messages, and settings sit behind the sign-in wall. The donation flow behind Donate now was not opened. support.gofundme.com, gofundme.org, and pro.gofundme.com are other hosts. One support article was opened to confirm the About menu link. The rest of those hosts were not crawled.
