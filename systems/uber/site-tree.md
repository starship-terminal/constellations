# Uber public site tree

Mapped on 2026-11-21 from the public Uber marketing site, signed out, before the refresh screenshots. Product URL: https://uber.com. The working marketing home from this network is https://www.uber.com/us/en/drive/, because https://www.uber.com/ and https://www.uber.com/us/en/ redirect to `/sg/en/` and 404. `login-extracted` stays `not-started`.

Desktop CSS viewport measured `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 2. Phone CSS viewport measured 390 by 844 at device pixel ratio 2. The drive hero is black. About, safety, and help are white pages under the same black header.

A reCAPTCHA wall at `def.uber.com/en/challenge` ("One more step") blocked the rider homepage, business, cities, newsroom, and several footer links. It was not solved. Those links are listed and not followed.

## Header

Present on About, Safety, Drive, and the 404 page at 1440.

| Control | Kind | Opens |
|---|---|---|
| Uber | link | https://www.uber.com/. From this network that URL 404s at `/sg/en/`. |
| Ride | link | https://m.uber.com/looking. Not followed. The rider marketing URL `/us/en/ride/` hits the captcha wall. |
| Earn | link | https://drivers.uber.com/. Not followed. |
| Travel | link | https://www.uber.com/us/en/city-hub/. That URL hit the captcha wall. |
| Hotels | link, drive page only | A Singular deep link into the Uber app for hotels. Not followed. |
| Business | link | https://www.uber.com/us/en/business/. That URL hit the captcha wall. |
| Uber Eats | link | https://www.ubereats.com/. A separate product. Not followed. |
| About | button, `aria-haspopup=menu` | A menu. Shot: [about-menu-light-open](screenshots/about-menu-light-open.png). |
| EN | button, aria "EN - Change language" | A full-page language dialog. Shot: [language-dialog-light-open](screenshots/language-dialog-light-open.png). No language was chosen. |
| Help | link | https://help.uber.com/ |
| Log in | link | https://auth.uber.com/login-redirect?next_url=https://www.uber.com, which lands on the empty auth wall. On Drive, Log in points at https://drivers.uber.com/ and was not followed. |
| Sign up | button, aria "Sign up to ride, drive, and get delivery" | A menu. Shot: [signup-menu-light-open](screenshots/signup-menu-light-open.png). No item was followed. |

About menu items, from the live menu and the header dump:

| Item | Href |
|---|---|
| About us | https://www.uber.com/us/en/about/ |
| Our offerings | https://www.uber.com/us/en/about/uber-offerings/ |
| How Uber works | https://www.uber.com/us/en/about/how-does-uber-work/ |
| Sustainability | https://www.uber.com/us/en/about/sustainability/ (captcha on a later load) |
| Newsroom | https://www.uber.com/us/en/newsroom/ (captcha) |
| Investor relations | https://investor.uber.com/ |
| Autonomous | https://www.uber.com/us/en/autonomous/ |
| Chauffeur | https://www.uber.com/us/en/ride/elite/ |
| Uber Advertising | https://www.uber.com/us/en/advertising/ |
| Merchants | https://merchants.ubereats.com/ |
| Blog | https://www.uber.com/us/en/blog/ |
| Careers | https://jobs.uber.com/en/ |

Sign up menu items, photographed and not followed:

| Item | Where it points |
|---|---|
| Ride | https://m.uber.com/login-redirect/ |
| Earn | https://drivers.uber.com/ |
| Uber Eats | https://ubereats.com/login-redirect/ |
| Business | https://business.uber.com/ |

The language dialog is titled "Select your preferred language" and shows English, Chinese, and Spanish on the first row, with a close control. No language was selected. Escape was pressed.

## Drive page

https://www.uber.com/us/en/drive/ is the public driver page that loaded. Headline "Drive when you want, make what you need". A second bar under the header lists Sign up, Requirements, Vehicle solutions, Your first trip, Using the app, Earnings, Uber Pro, Safety, What's new, and Contact us.

| Control | Opens |
|---|---|
| Sign up | https://www.uber.com/us/en/drive/ (same page) |
| Requirements | https://www.uber.com/us/en/drive/requirements/ |
| Vehicle solutions | https://www.uber.com/us/en/drive/vehicle-solutions/ |
| Your first trip | https://www.uber.com/us/en/drive/basics/ |
| Using the app | https://www.uber.com/us/en/drive/driver-app/ |
| Earnings | https://www.uber.com/us/en/drive/how-much-drivers-make/ |
| Uber Pro | https://www.uber.com/us/en/drive/uber-pro/ |
| Safety | https://www.uber.com/us/en/drive/safety/ |
| What's new | https://www.uber.com/us/en/u/only-on-uber/ |
| Contact us | https://www.uber.com/us/en/drive/contact/ |
| Get started | Stays on the page. The phone field was not filled. |
| Already have an account? Sign in | https://drivers.uber.com/. Not followed. |
| View rental options | https://bonjour.uber.com/marketplace/. Not followed. |

The phone field shows a country control and the placeholder `(999) 999-9999`. Nothing was typed. Get started was not clicked.

## About, safety, offerings, how it works, blog

| Page | URL | What the first screen shows |
|---|---|---|
| About | /us/en/about/ | Hero "About us", then "We reimagine the way the world moves for the better" |
| How Uber works | /us/en/about/how-does-uber-work/ | "How Uber works" |
| Offerings | /us/en/about/uber-offerings/ | "Uber's technology offerings" |
| Safety | /us/en/safety/ | "Our commitment to safety" |
| Blog | /us/en/blog/ | "Uber Blog" header, Explore menu, article cards. Explore was not opened. |
| Driver requirements | /us/en/drive/requirements/ | "Driver requirements" |
| Driver safety | /us/en/drive/safety/ | "Drive with confidence" |

About body links that were not followed from the cards: Dara's letter on investor.uber.com, sustainability, leadership, integrity, newsroom.

## Help

https://help.uber.com/ loaded as a public support home. Shot: [help-light-default](screenshots/help-light-default.png).

| Control | Opens |
|---|---|
| Uber | https://uber.com/ |
| EN | Language button. Not used to change language. |
| Log in | /login on help.uber.com. A direct load returned HTTP 429. The empty wall was photographed at https://auth.uber.com/v2/ instead. |
| Help | https://help.uber.com/ |
| Riders | /riders |
| Driving & Delivering | /driving-and-delivering |
| Uber Eats | /ubereats |
| Merchants & Restaurants | /merchants-and-restaurants |
| Bikes & Scooters | /emobility |
| Uber for Business | /business |
| Uber Health | a business section URL |
| Freight | /freight |
| Fleet | /fleet |

The riders page shows a search field ("Search questions, keywords, topics") and topic rows: Help with a trip, Account, Membership. Search was not submitted. The "Log in for personalized support" banner was not followed. Shot: [help-riders-light-default](screenshots/help-riders-light-default.png).

## Footer

Shot: [drive-light-footer](screenshots/drive-light-footer.png). Columns Company, Products, Global citizenship, Travel, plus language, city, store badges, and legal links.

| Control | Opens |
|---|---|
| Visit Help Center | https://help.uber.com/ |
| About us | /us/en/about/ |
| Our offerings | /us/en/about/uber-offerings/ |
| Newsroom | /us/en/newsroom/ (captcha) |
| Investors | https://investor.uber.com/ |
| Blog | /us/en/blog/ |
| Careers | https://jobs.uber.com/en/ |
| Uber One | /us/en/uber-one/ |
| Ride | /us/en/ride/ (captcha) |
| Drive | /us/en/drive/ |
| Deliver | /us/en/deliver/ |
| Eat | https://www.ubereats.com/ |
| Uber for Business | /us/en/business/ (captcha) |
| Uber Freight | https://www.uberfreight.com/ |
| Gift cards | /us/en/gift-cards/ |
| Uber Health | https://www.uberhealth.com/ |
| Uber Advertising | /us/en/advertising/ |
| Merchants | https://merchants.ubereats.com/ |
| Safety | /us/en/safety/ |
| Sustainability | /us/en/about/sustainability/ |
| Reserve | an app deep link with a fallback to m.uber.com/reserve. Not followed. |
| Airports | /us/en/airports/ |
| Hotels | /us/en/hotels/ |
| Cities | /us/en/r/cities/ |
| English | language button. Not used. |
| San Francisco Bay Area | city button. Not used. No address was typed. |
| Google Play, App Store | store badges. Not followed. |
| Privacy | https://www.uber.com/legal/document/?name=privacy-notice |
| Accessibility | /us/en/about/accessibility/ |
| Terms | https://www.uber.com/legal/document/?name=general-terms-of-use |
| Sign up to drive | a sticky bar on the drive page. Not clicked. |

## Phone width

The hamburger on About opens a drawer: Ride, Earn, Travel, Business, Uber Eats, About, Help, and EN. Shot: [about-light-mobile-menu](screenshots/about-light-mobile-menu.png). About was not expanded. No item was followed.

Drive at 390 shows the same black hero, the empty phone field, and Get started. Shot: [drive-light-mobile](screenshots/drive-light-mobile.png).

## Auth wall

https://auth.uber.com/v2/ is both the login and the signup wall. Headline "What's your phone number or email?". The field placeholder is "Enter phone number or email". Continue, Continue with Google, and Continue with Apple sit under it. The page says a verification code may arrive by text or WhatsApp.

Shots: [auth-light-empty](screenshots/auth-light-empty.png) and [auth-light-mobile-empty](screenshots/auth-light-mobile-empty.png). Nothing was typed. Continue was not clicked. Google and Apple were not clicked. `login-extracted` stays `not-started`.

## Empty and error

`/us/en/careers/` on www.uber.com returns the designed 404, "Signals got crossed, and we can't find your page", with links to rider, driver, and delivery pages. Shot: [not-found-light-default](screenshots/not-found-light-default.png). Those links were not followed. A bare homepage request 404s at `/sg/en/` with "Sorry, we couldn't find that page".

## Stopped

No email, password, code, phone, or address was typed. No identity provider was clicked. No ride was requested. No checkout was opened. The captcha was not solved. The signed-in app was not entered.
