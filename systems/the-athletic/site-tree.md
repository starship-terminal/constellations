# The Athletic public site tree

Mapped on 2026-11-22 from [https://www.nytimes.com/athletic/](https://www.nytimes.com/athletic/) in an incognito preview tab, signed out. [https://theathletic.com/](https://theathletic.com/) still redirects there. Desktop shots are 1440 × 900 CSS pixels at 2× (PNG 2880 × 1800). The phone shot is 390 × 844 CSS pixels at 2× (PNG 780 × 1688). They are the first viewport, not the full page. The homepage title was "The Athletic - Sports news, stories, scores, schedules, podcasts, and more". This is a live news site, not a parked domain and not a captcha wall. `html[data-theme]` was `legacy`. The page painted white under a near-black header. `prefers-color-scheme` was dark and did not change the paint.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. No subscription was started. Checkout was not opened. `login-extracted` stays `not-started`.

origin/main already had `systems/the-athletic/` and did not have `systems/the-athletic/site-tree.md`. This walk adds the site tree and live screenshots. It does not remeasure tokens. catalog.json and webapps-manifest.json were left alone. `systems/nytimes` was not touched.

## How a control opens something

| Control | Gesture | Opens |
|---|---|---|
| Header logo | link | [https://www.nytimes.com/athletic/](https://www.nytimes.com/athletic/) |
| Hamburger | click | A full-width panel of leagues, utilities, and account links |
| League label in the bar | link | That league's public home |
| League chevron, More (`•••`) | click | A submenu under the bar. The label is a button, not a page |
| Log In | link | [https://www.nytimes.com/athletic/login2/](https://www.nytimes.com/athletic/login2/). Empty login and create-account wall. Branch stopped |
| Start a free trial | link | [https://www.nytimes.com/subscription/athletic](https://www.nytimes.com/subscription/athletic). Subscribe wall. Branch stopped |
| Search | link | [https://www.nytimes.com/athletic/search/](https://www.nytimes.com/athletic/search/). Empty search. Nothing typed |
| Edition banner | button | Offers International. Not confirmed |
| Footer columns | link | Public indexes, company pages, or a wall |

## Header

Photographed: [home-light-1440.png](screenshots/home-light-1440.png), [home-light-390.png](screenshots/home-light-390.png).

An edition strip sits under the logo: "You are viewing our U.S. edition." International and Stay on this edition are buttons. The strip was left in place.

The bar shows NFL, College Football, MLB, NBA, NHL, Fantasy Football, NCAAM, NCAAW, Premier League, then More. Log In and Start a free trial sit at the right, with a search icon.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Logo | link | [https://www.nytimes.com/athletic/](https://www.nytimes.com/athletic/) | home |
| Hamburger | button | panel | photographed |
| NFL | link | [/athletic/nfl/](https://www.nytimes.com/athletic/nfl/) | opened |
| College Football | link | [/athletic/college-football/](https://www.nytimes.com/athletic/college-football/) | listed, not opened as its own page |
| MLB | link | [/athletic/mlb/](https://www.nytimes.com/athletic/mlb/) | listed |
| NBA | link | [/athletic/nba/](https://www.nytimes.com/athletic/nba/) | listed |
| NHL | link | [/athletic/nhl/](https://www.nytimes.com/athletic/nhl/) | listed |
| Fantasy Football | link | [/athletic/fantasy/football/](https://www.nytimes.com/athletic/fantasy/football/) | listed |
| NCAAM | link | [/athletic/college-basketball/](https://www.nytimes.com/athletic/college-basketball/) | listed |
| NCAAW | link | [/athletic/womens-college-basketball/](https://www.nytimes.com/athletic/womens-college-basketball/) | listed |
| Premier League | link | [/athletic/football/premier-league/](https://www.nytimes.com/athletic/football/premier-league/) | listed |
| More | button | panel of the rest of the leagues | not opened. Same destinations are in the hamburger |
| Log In | link | [/athletic/login2/](https://www.nytimes.com/athletic/login2/?login_source=site_nav&redirect_uri=https%3A%2F%2Fwww.nytimes.com%2Fathletic%2F) | empty wall photographed, then stopped |
| Start a free trial | link | [/subscription/athletic](https://www.nytimes.com/subscription/athletic?source=athletic-bar1&onboarded=false) | wall photographed, checkout not followed |
| Search icon | link | [/athletic/search/](https://www.nytimes.com/athletic/search/) | empty page photographed |

A live strip under the bar names College Football Week 12, ATP Finals, NBA Latest, NFL Projections, CFP Projections, Fantasy Football Rankings, Dubai SailGP, and Play. Those are dated stories and tools, not standing nav. Play was opened. The rest were not.

### Hamburger

Opened by click. Photographed: [menu-hamburger-light-1440.png](screenshots/menu-hamburger-light-1440.png).

The panel lists every league in the bar, plus Champions League, WNBA, Tennis, Golf, Men's World Cup, Women's World Cup, Soccer, Women's Soccer, MLS, NWSL, Olympics, Peak, Sports Business, Global Sports, Culture, College Sports, Formula 1, Sailing, Fantasy Baseball, Betting, Memorabilia and Collectibles, Motorsports, NASCAR, Women's Hockey, MMA, Boxing, and the dated strip items. The right column is utilities:

| Label | Destination | This pass |
|---|---|---|
| Log In | [/athletic/login2/](https://www.nytimes.com/athletic/login2/?redirect_uri=https%3A%2F%2Fwww.nytimes.com%2Fathletic%2F) | empty wall photographed, then stopped |
| Subscribe Now | [/subscription/athletic](https://www.nytimes.com/subscription/athletic?source=athletic&onboarded=false) | same subscribe wall. Not followed a second time |
| Tickets by Viagogo | [/athletic/tickets/](https://www.nytimes.com/athletic/tickets/) | not opened. Partner page |
| Play Center | [/athletic/daily-play/](https://www.nytimes.com/athletic/daily-play/) | opened |
| U.S. | [/athletic/](https://www.nytimes.com/athletic/) | home |
| International | [/athletic/uk/](https://www.nytimes.com/athletic/uk/) | opened |
| Search | [/athletic/search/](https://www.nytimes.com/athletic/search/) | empty page photographed |
| Top News | [/athletic/news/](https://www.nytimes.com/athletic/news/) | opened |
| Podcasts | [/athletic/podcasts/](https://www.nytimes.com/athletic/podcasts/) | opened |

League submenus (Home, Teams, Scores & Schedule, Standings, and a few extras such as Draft or Odds) sit in the DOM behind each chevron. They were not opened. The NFL home stands in for that pattern.

## Footer

Read from the homepage. The login wall's first viewport shows the footer columns. Photographed there: [login-empty-light-1440.png](screenshots/login-empty-light-1440.png).

| Column | What it holds | This pass |
|---|---|---|
| National | 69 league and topic indexes, from Boxing through Headlines | NFL opened. The rest are the same public league pattern and were not opened one by one |
| US | City indexes such as Arizona, Atlanta, Bay Area, New York | not opened. Same location template |
| Canada | Calgary, Edmonton, Montreal, Ottawa, Toronto, Vancouver, Winnipeg | not opened |
| Partners | Odds by BetMGM, Tickets by Viagogo | not opened |
| Play Center | Connections: Sports, Connections: Soccer, Strands: Sports Edition | Play Center index opened. Individual puzzles not started |
| Editions | International, U.S. | International opened |
| Subscribe | Start Subscription, Buy a Gift, Group Subscriptions | Start Subscription is the subscribe wall. Gift and group checkout were not opened |
| HQ | About Us, Careers, Code of Conduct, Editorial Guidelines, Advertise, Business Inquiries, Press Inquiries | About, Careers, Code of Conduct, Editorial Guidelines, Business Inquiries, and Press opened. Advertise is [theathleticadvertising.com](https://www.theathleticadvertising.com/) and was not followed |
| Support | FAQ, Forgot Password?, Contact Us, Terms of Service | FAQ, Contact Us, and Terms are NYT help. Forgot Password is an account wall. None of those were entered |
| Newsletters | The Pulse, The Bounce, The Windup, Prime Tire, Full Time, Until Saturday, NFL Newsletter, The Athletic FC, MoneyCall, Red Light, Peak, No Offseason | not opened. Subscribe forms were not submitted |
| Legal | Privacy Policy, Cookie Policy, RSS, Sitemap, A New York Times Company | Sitemap opened. Privacy and cookies are NYT pages and were not followed. RSS was not followed |

Social links in the footer: Twitter, Facebook, Instagram, the App Store, and Google Play. Those were not followed.

## Pages opened

| Page | URL | Shot |
|---|---|---|
| Home, US | [https://www.nytimes.com/athletic/](https://www.nytimes.com/athletic/) | [home-light-1440.png](screenshots/home-light-1440.png), [home-light-390.png](screenshots/home-light-390.png) |
| Hamburger | same URL, panel open | [menu-hamburger-light-1440.png](screenshots/menu-hamburger-light-1440.png) |
| About | [/athletic/about/](https://www.nytimes.com/athletic/about/) | [about-light-1440.png](screenshots/about-light-1440.png) |
| NFL | [/athletic/nfl/](https://www.nytimes.com/athletic/nfl/) | [nfl-light-1440.png](screenshots/nfl-light-1440.png) |
| Podcasts | [/athletic/podcasts/](https://www.nytimes.com/athletic/podcasts/) | [podcasts-light-1440.png](screenshots/podcasts-light-1440.png) |
| Top News | [/athletic/news/](https://www.nytimes.com/athletic/news/) | [news-light-1440.png](screenshots/news-light-1440.png) |
| Search, empty | [/athletic/search/](https://www.nytimes.com/athletic/search/) | [search-empty-light-1440.png](screenshots/search-empty-light-1440.png) |
| One public article | [/athletic/7799526/2026/11/21/nfl-news-puka-cowboys-daniel-jones-colts/](https://www.nytimes.com/athletic/7799526/2026/11/21/nfl-news-puka-cowboys-daniel-jones-colts/) | [article-light-1440.png](screenshots/article-light-1440.png) |
| Careers | [/athletic/careers/](https://www.nytimes.com/athletic/careers/) | [careers-light-1440.png](screenshots/careers-light-1440.png) |
| Press | [/athletic/press/](https://www.nytimes.com/athletic/press/) | [press-light-1440.png](screenshots/press-light-1440.png) |
| Code of Conduct | [/athletic/code-of-conduct/](https://www.nytimes.com/athletic/code-of-conduct/) | [code-of-conduct-light-1440.png](screenshots/code-of-conduct-light-1440.png) |
| Editorial Guidelines | [/athletic/edit-guidelines/](https://www.nytimes.com/athletic/edit-guidelines/) | [editorial-guidelines-light-1440.png](screenshots/editorial-guidelines-light-1440.png) |
| Business Inquiries | [/athletic/contact-us/](https://www.nytimes.com/athletic/contact-us/) | [contact-light-1440.png](screenshots/contact-light-1440.png) |
| Sitemap | [/athletic/sitemap/](https://www.nytimes.com/athletic/sitemap/) | [sitemap-light-1440.png](screenshots/sitemap-light-1440.png) |
| Play Center | [/athletic/daily-play/](https://www.nytimes.com/athletic/daily-play/) | [play-light-1440.png](screenshots/play-light-1440.png) |
| International edition | [/athletic/uk/](https://www.nytimes.com/athletic/uk/) | [uk-light-1440.png](screenshots/uk-light-1440.png) |
| Login and signup wall | [/athletic/login2/](https://www.nytimes.com/athletic/login2/?login_source=site_nav&redirect_uri=https%3A%2F%2Fwww.nytimes.com%2Fathletic%2F) | [login-empty-light-1440.png](screenshots/login-empty-light-1440.png) |
| Subscribe wall | [/subscription/athletic](https://www.nytimes.com/subscription/athletic?source=athletic-bar1&onboarded=false) | [subscribe-light-1440.png](screenshots/subscribe-light-1440.png) |

The article rendered signed out: the headline and the lead were on the first viewport. No account chrome was visible.

Older reconstruction PNGs in this folder (home-light-default.png and the other `*-default.png` files) are from 2026-11-19. They are not photographs. See [screenshots/README.md](screenshots/README.md).

## Where the walk stopped

Log In and the hamburger's Log In open one wall: "Log in or create an account." The email field was empty. Continue was not clicked. Continue with Google and Continue with Apple were visible and were not clicked. There is no separate signup URL. That wall is the signup wall.

Start a free trial and footer Start Subscription open the Athletic offer page. Continue to checkout and Subscribe now point at `myaccount.nytimes.com` and were not followed. Buy a Gift and Group Subscriptions were not opened. Forgot Password was not opened.

No password, email, code, phone, or address was entered. No identity provider was clicked. No captcha was solved. No subscription was started.
