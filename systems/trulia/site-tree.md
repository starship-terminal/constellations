# Trulia public site tree

Mapped from the signed-out homepage at https://www.trulia.com/ on 2026-11-20, in headed Chrome (Playwright, channel `chrome`, 1440×900). Headless Chromium and curl both received HTTP 403 from PerimeterX (`Press & Hold to confirm you are a human`). Headed Chrome loaded the homepage and several public routes. A second visit in the same minute often returned the same press-and-hold wall. No password was typed, no form was submitted, and Continue with Google and Continue with Apple were not clicked.

Listing routes that show street addresses (`/STATE/City/`, `/for_rent/…`, `/houses-for-sale-near-me/`, and similar result pages) are mapped and were not opened for screenshots.

## Homepage shell

| Control | Opens | Captured |
|---|---|---|
| Logo, aria "Go to Trulia Home" | https://www.trulia.com/ | yes, this page |
| Skip main navigation | `#main-content` on the same page | in-page link, not a new surface |
| Buy (header) | https://www.trulia.com/ (same homepage). Hover reveals no extra flyout links. | yes |
| Rent (header) | https://www.trulia.com/rent/ plus a hover flyout | rent landing loaded (200). Flyout recorded, not a separate page |
| Rent flyout: Post A Rental Listing | https://www.trulia.com/post-rental/ | 403 press-and-hold. Branch stopped |
| Mortgage (header) | https://www.trulia.com/mortgages/ plus a hover flyout | mortgages landing loaded (200) |
| Mortgage flyout: Mortgage Overview | https://www.trulia.com/mortgages/ | same as Mortgage |
| Mortgage flyout: Get Pre-Qualified | https://www.trulia.com/mortgages/pre-qualified/ | not opened: lead form, would collect personal details |
| Mortgage flyout: Mortgage Rates | https://www.trulia.com/mortgage-rates/ | not opened after the press-and-hold rate rose |
| Mortgage flyout: Refinance Rates | https://www.trulia.com/refinance-rates/ | not opened, same reason |
| Mortgage flyout: Mortgage Calculator | https://www.trulia.com/mortgage-payment-calculator/ | loaded (200) |
| Mortgage flyout: Affordability Calculator | https://www.trulia.com/house-affordability-calculator/ | not opened, same bot-wall reason |
| Mortgage flyout: Refinance Calculator | https://www.trulia.com/home-loan-refinance-calculator/ | not opened, same reason |
| Mortgage flyout: Rent vs Buy Calculator | https://www.trulia.com/rent-vs-buy-calculator/ | not opened, same reason |
| Saved Homes | login dialog "Sign up or Log in" on the same URL. No saved-homes page | dialog recorded. Branch stopped. Not filled |
| Saved Searches | same login dialog | dialog recorded. Branch stopped |
| Sign up or Log in | dialog labelled "Sign in or register": Email field, Submit, OR, Continue with Google (accounts.google.com iframe), Continue with Apple, Terms of Use, Privacy Policy | dialog recorded. Email not typed. Submit not pressed. Google and Apple not clicked |
| Main Menu | right drawer, aria-label "Main Menu", 320px, `role=dialog` | opened. Close control is aria "Close Menu" |

### Main Menu drawer

| Section | Reveals | Destination |
|---|---|---|
| Sign up or Log in | the login dialog above | stopped |
| Buy | no child links. The label is the section itself | homepage |
| Rent | Post A Rental Listing | https://www.trulia.com/post-rental/ (403, stopped) |
| Mortgage | the same eight links as the header flyout | see table above |
| Local Info | All Trulia Neighborhood Guides | https://www.trulia.com/neighborhoods/ (loaded) |
| Additional Resources | Trulia Blogs | https://www.trulia.com/blog/ (loaded) |
| Additional Resources | Help Center | https://www.trulia.com/help/ redirects to https://support.trulia.com/hc/en-us (loaded) |
| Additional Resources | Get Leads by ZIP | https://www.zillow.com/premier-agent/solutions/real-estate-agent/ (off-site, not captured) |
| Additional Resources | Get Mortgage Leads | https://www.trulia.com/advertising/mortgage-leads/ (lead form, not opened) |

## Homepage interactions

| Control | Opens | Captured |
|---|---|---|
| Hero tabs Buy / Rent / Sold (`tab-button-buy`, `tab-button-rent`, `tab-button-sold`) | local search mode on the same page. Does not navigate | toggled. Search not submitted |
| Search field `#banner-search` | placeholder "Search for City, Neighborhood, Zip, County, School". Focus expands the field. Typing shows a suggestion list | focus and a typed suggestion state recorded. Submit not pressed. No suggestion link followed (those open listing results) |
| clear search | clears the field | local control |
| submit search | would run a location search | not clicked |
| Close Thanksgiving banner | dismisses the quiz promo card | local dismiss. Not used as a consent POST |
| Thanksgiving "Take the quiz" | https://www.trulia.com/thanksgiving/house-for-sale/#quiz | not opened: a survey. Instruction was not to fill survey fields |
| City cards (Atlanta, Austin, and the rest of the rail) | `/STATE/City/` result pages | mapped, not screenshotted (listing results) |
| Next / Skip on the city rail | scrolls the card rail | local carousel |
| Buy a home card | https://www.trulia.com/houses-for-sale-near-me/ | mapped, not screenshotted (listing results, and the URL is location-shaped) |
| Rent an apartment card | https://www.trulia.com/apartments/ | mapped, not screenshotted (listing results) |
| See neighborhoods card | https://www.trulia.com/neighborhoods/ | same as Local Info |
| Check out a neighborhood search `#neighborhood-search` | second location field | not submitted |
| Footer "More" (three, `aria-expanded=false`) | expands Popular Searches, Popular Rental Searches, and a third link group in place | links recorded from the DOM. Expanding was not required to read the hrefs |
| Cookie Preference | cookie preference UI | not clicked. Consent controls are hidden, not posted |

## Footer and resource pages reached from the homepage

These hrefs are in the homepage footer. Ones that loaded are marked. City, rental, and "near me" listing hrefs are omitted from the capture set on purpose.

| Link | URL | Result |
|---|---|---|
| Trulia Estimates | https://www.trulia.com/info/trulia-estimates/ | not opened after the bot wall tightened |
| Community Sitemap | https://www.trulia.com/info/communities/ | not opened |
| Contact | https://www.trulia.com/info/contact-us/ | not opened (contact form) |
| Trulia Sitemap | https://www.trulia.com/sitemaps/ | not opened |
| Popular cities sitemap | https://www.trulia.com/sitemaps/popular-cities/ | sitemap index, not a product screen |
| Popular rental cities | https://www.trulia.com/sitemaps/popular-rental-cities/ | sitemap index |
| Property Management Companies | https://www.trulia.com/sitemaps/property-management-companies/ | sitemap index |
| All Real Estate Markets | https://www.trulia.com/sitemaps/city-for-sale/ | sitemap index |
| All Rental Markets | https://www.trulia.com/sitemaps/city-for-rent/ | sitemap index |
| University markets | https://www.trulia.com/sitemaps/universities-for-sale/ and `universities-for-rent` | sitemap index |
| Popular Counties | https://www.trulia.com/county-sitemap/ | sitemap index |
| Newsroom | https://www.trulia.com/newsroom/ | loaded (200) |
| Help | https://support.trulia.com/hc/en-us | loaded (200). "Submit a request" and "Sign in" stop: a request form and a login wall |
| App badge | https://trulia.app.link/get-app | off-site app link, not opened |
| Facebook, Twitter, Instagram, Pinterest | off-site social | not captured |
| About, Careers, Investor Relations, Terms, Privacy, Ad Choices, Do Not Sell, Fair Housing, licenses, brokerage PDFs | Zillow Group, HUD, state regulator hosts | off-site, not captured |
| GreatSchools | https://www.greatschools.org/ | off-site |

## Help Center (after redirect)

https://www.trulia.com/help/ lands on https://support.trulia.com/hc/en-us (Zendesk). Visible controls: Search, Categories (Renters & Rentals, Mobile Apps, Buyers, Sellers & Homeowners), Submit a request, Sign in. Submit a request and Sign in were not followed.

## Login and signup wall

Recorded on the homepage, not on https://www.trulia.com/login (that URL was not opened in this run; a prior probe already found email and password there).

- Dialog title: Sign up or Log in. Accessible name: Sign in or register.
- Fields: Email ("Enter email address"), Submit. Not filled, not submitted.
- Continue with Google is an `accounts.google.com` iframe. Not clicked. A prior probe noted the popup did not open.
- Continue with Apple. Not clicked.
- Links inside the dialog: Terms of Use, Privacy Policy (Zillow Group hosts).

## Pages this capture treats as the public set

Loaded without a press-and-hold wall in headed Chrome:

- https://www.trulia.com/
- https://www.trulia.com/rent/
- https://www.trulia.com/mortgages/
- https://www.trulia.com/mortgage-payment-calculator/
- https://www.trulia.com/neighborhoods/
- https://www.trulia.com/blog/
- https://www.trulia.com/newsroom/
- https://support.trulia.com/hc/en-us

Blocked or stopped:

- https://www.trulia.com/buy/, https://www.trulia.com/sold/, https://www.trulia.com/post-rental/ returned the press-and-hold page.
- Saved Homes, Saved Searches, and Sign up or Log in stop at the login dialog.
- Listing and city result URLs are mapped and not screenshotted.
- Quiz, pre-qualification, contact, and lead forms were not opened.
