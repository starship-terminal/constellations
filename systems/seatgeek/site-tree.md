# SeatGeek public site tree

Mapped on 2026-11-22 from [https://seatgeek.com/](https://seatgeek.com/) in an incognito preview tab, signed out. Desktop shots are 1440 × 900 CSS pixels at 2× (PNG 2880 × 1800). They are the first viewport, not the full page. The homepage title was "SeatGeek | Your Ticket to Sports Games, Concerts & Live Shows so Fans Can Fan". The first visible heading is "Be good at seats". This is a live ticket marketplace, not a parked domain.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider or wallet was clicked. No captcha was solved. No ticket was bought. No performer was followed. `login-extracted` stays `not-started`.

origin/main already had `systems/seatgeek/` and did not have `systems/seatgeek/site-tree.md`. This walk adds the site tree and screenshots. It does not remeasure tokens. catalog.json and webapps-manifest.json were left alone.

Headless Chromium on this host got a DataDome captcha interstitial with no public page. Those frames were discarded. The shots below come from the preview tab, which loaded the public site.

## How a control opens something

| Control | Gesture | Opens |
|---|---|---|
| Header logo | link | [https://seatgeek.com/](https://seatgeek.com/) |
| Sports, Music, Shows, Cities | hover | A two-column menu. The label is also a link to the category page. |
| Sign in | click | A dialog on the current page. Login and signup wall. Branch stopped. |
| Main menu | click | A short list: Sell tickets, Help center, Language & Currency. |
| Search or ask anything | field | Not typed into. Ask was not clicked. |
| Connect to Spotify | button | Not clicked. Identity provider. |
| Footer app badges | link | seatgeek.onelink.me. Not followed. |
| Social icons | link | Facebook, Instagram, TikTok, X. Not followed. |
| Cookie or consent card | none seen | No consent dialog was on the page. |

## Header

Photographed: [home-light-1440.png](screenshots/home-light-1440.png).

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Logo | link | [https://seatgeek.com/](https://seatgeek.com/) | home |
| Sports | link and menu | [https://seatgeek.com/sports-tickets](https://seatgeek.com/sports-tickets) | menu photographed |
| Music | link and menu | [https://seatgeek.com/concert-tickets](https://seatgeek.com/concert-tickets) | menu photographed |
| Shows | link and menu | [https://seatgeek.com/theater-tickets](https://seatgeek.com/theater-tickets) | menu photographed |
| Cities | link and menu | [https://seatgeek.com/cities](https://seatgeek.com/cities) | menu photographed, page opened |
| Sign in | button | dialog on the current page | empty wall photographed, then stopped |
| Main menu | button | panel | photographed |

On inner pages the header also shows a search field. It was not typed into.

### Sports menu

Opened by hover. Photographed: [menu-sports-light-1440.png](screenshots/menu-sports-light-1440.png).

Left column, category links:

| Label | Destination |
|---|---|
| MLB | [/mlb-tickets](https://seatgeek.com/mlb-tickets) |
| NFL | [/nfl-tickets](https://seatgeek.com/nfl-tickets) |
| NBA | [/nba-tickets](https://seatgeek.com/nba-tickets) |
| NHL | [/nhl-tickets](https://seatgeek.com/nhl-tickets) |
| MLS | [/mls-tickets](https://seatgeek.com/mls-tickets) |
| NCAA Football | [/ncaa-football-tickets](https://seatgeek.com/ncaa-football-tickets) |
| NCAA Basketball | [/ncaa-basketball-tickets](https://seatgeek.com/ncaa-basketball-tickets) |
| NCAA Baseball | [/ncaa-baseball-tickets](https://seatgeek.com/ncaa-baseball-tickets) |
| WNBA | [/wnba-tickets](https://seatgeek.com/wnba-tickets) |
| More Football | [/football-tickets](https://seatgeek.com/football-tickets) |
| More Hockey | [/hockey-tickets](https://seatgeek.com/hockey-tickets) |
| More Soccer | [/soccer-tickets](https://seatgeek.com/soccer-tickets) |
| Golf | [/golf-tickets](https://seatgeek.com/golf-tickets) |
| Tennis | [/tennis-tickets](https://seatgeek.com/tennis-tickets) |
| Fighting | [/fighting-tickets](https://seatgeek.com/fighting-tickets) |

More College Sports, More Baseball, Equestrian, Motorsports, Playoffs, and More Sports are labels in the same column with no href. The right column lists teams and events for the hovered category. MLB was the open column: All MLB tickets, National League, American League, then each club. Team, event, and performer pages were not opened. Buying a ticket from one of those rows is checkout. The walk stopped before that.

### Music menu

Opened by hover. Photographed: [menu-music-light-1440.png](screenshots/menu-music-light-1440.png).

Festivals links to [/music-festival-tickets](https://seatgeek.com/music-festival-tickets). Trending, Genres, and Tours are labels with no href. The right column lists performers. Performer pages were not opened, and no performer was followed.

### Shows menu

Opened by hover. Photographed: [menu-shows-light-1440.png](screenshots/menu-shows-light-1440.png).

| Label | Destination |
|---|---|
| Broadway | [/broadway-tickets](https://seatgeek.com/broadway-tickets) |
| Musicals | [/collections/musicals-tickets](https://seatgeek.com/collections/musicals-tickets) |
| Comedy | [/comedy-tickets](https://seatgeek.com/comedy-tickets) |
| Classical Music | [/classical-music-tickets](https://seatgeek.com/classical-music-tickets) |
| Family Entertainment | [/family-entertainment-tickets](https://seatgeek.com/family-entertainment-tickets) |
| Disney on Ice | [/collections/disney-on-ice-tickets](https://seatgeek.com/collections/disney-on-ice-tickets) |
| Magic | [/magic-tickets](https://seatgeek.com/magic-tickets) |
| Circus | [/circus-tickets](https://seatgeek.com/circus-tickets) |
| Cirque du Soleil | [/cirque-du-soleil-tickets](https://seatgeek.com/cirque-du-soleil-tickets) |
| Opera | [/opera-tickets](https://seatgeek.com/opera-tickets) |
| Ballet | [/ballet-tickets](https://seatgeek.com/ballet-tickets) |
| Drag Shows | [/drag-show-tickets](https://seatgeek.com/drag-show-tickets) |
| Podcast | [/podcast-tickets](https://seatgeek.com/podcast-tickets) |
| All shows | [/theater-tickets](https://seatgeek.com/theater-tickets) |

The right column lists shows. Those pages were not opened.

### Cities menu

Opened by hover. Photographed: [menu-cities-light-1440.png](screenshots/menu-cities-light-1440.png).

It lists city guides, then All cities at [/cities](https://seatgeek.com/cities). Cities photographed: Arlington, Atlanta, Austin, Baltimore, Boston, Charlotte, Chicago, Cincinnati, Cleveland, Dallas, Denver, Detroit, Houston, Kansas City, Las Vegas, Los Angeles, Miami, Minneapolis, Nashville, New Orleans, New York, Philadelphia, Phoenix, Pittsburgh, Portland, San Diego, San Francisco, Seattle, Tampa, Washington, DC. Individual city pages were not opened.

### Main menu

Opened by click. Photographed: [menu-main-light-1440.png](screenshots/menu-main-light-1440.png).

| Label | Destination | This pass |
|---|---|---|
| Sell tickets | [/sell](https://seatgeek.com/sell) | opened, search field left empty |
| Help center | [/help](https://seatgeek.com/help) | opened |
| Language & Currency | button | not opened |

## Footer

Read from the homepage. Photographed in the first viewport of the pages below, not as its own crop.

| Column | Label | Destination | This pass |
|---|---|---|---|
| Download the App | App Store and Google Play badges | seatgeek.onelink.me | not followed |
| Resources | About | [/about](https://seatgeek.com/about) | opened |
| Resources | Jobs | [/jobs](https://seatgeek.com/jobs) | opened |
| Resources | Inclusion | [/diversity-equity-inclusion](https://seatgeek.com/diversity-equity-inclusion) | opened |
| Resources | Why Trust SeatGeek | [/is-seatgeek-legit](https://seatgeek.com/is-seatgeek-legit) | opened |
| Resources | Digital Accessibility | [/accessibility](https://seatgeek.com/accessibility) | opened |
| Resources | SeatGeek Blog | [/blog](https://seatgeek.com/blog) | opened |
| Resources | Newsroom | [/enterprise/newsroom](https://seatgeek.com/enterprise/newsroom) | opened |
| Resources | Help & Support | [/help](https://seatgeek.com/help) | opened |
| Resources | Sell on SeatGeek | [/sell](https://seatgeek.com/sell) | opened |
| Resources | SeatGeek Enterprise | [/enterprise](https://seatgeek.com/enterprise) | opened |
| Resources | SeatGeek Creators | [/ambassador](https://seatgeek.com/ambassador) | opened, then discarded |
| Social | Facebook | [facebook.com/SeatGeek](https://www.facebook.com/SeatGeek) | not followed |
| Social | Instagram | [instagram.com/seatgeek](https://www.instagram.com/seatgeek/) | not followed |
| Social | TikTok | [tiktok.com/@seatgeek](https://www.tiktok.com/@seatgeek) | not followed |
| Social | X | [x.com/seatgeek](https://x.com/seatgeek) | not followed |
| Developers | Platform | [/build](https://seatgeek.com/build) | opened |
| Developers | Developer Blog | [chairnerd.seatgeek.com](https://chairnerd.seatgeek.com/) | opened, first viewport |
| Legal | Terms | [/terms](https://seatgeek.com/terms) | opened |
| Legal | Privacy | [/privacy](https://seatgeek.com/privacy) | opened |
| Legal | Site map | [/sitemap](https://seatgeek.com/sitemap) | opened |
| Legal | English, USD | button | not opened |
| Legal | Your privacy choices | button | not opened |

The homepage also paints a category grid under the hero: NFL, Concerts, NBA, NCAA Football, NHL, MLB, MLS, NCAA Basketball, Broadway Shows, Comedy, WWE, Tennis, Golf, Music Festivals. Those are the same category destinations as the menus. They were not opened as separate pages.

## Pages opened

| URL | Title | Shot |
|---|---|---|
| [https://seatgeek.com/](https://seatgeek.com/) | SeatGeek \| Your Ticket to Sports Games, Concerts & Live Shows so Fans Can Fan | [home-light-1440.png](screenshots/home-light-1440.png) |
| [/about](https://seatgeek.com/about) | Learn More About Us \| SeatGeek | [about-light-1440.png](screenshots/about-light-1440.png) |
| [/jobs](https://seatgeek.com/jobs) | SeatGeek Jobs \| SeatGeek | [jobs-light-1440.png](screenshots/jobs-light-1440.png) |
| [/diversity-equity-inclusion](https://seatgeek.com/diversity-equity-inclusion) | DEI \| SeatGeek | [inclusion-light-1440.png](screenshots/inclusion-light-1440.png) |
| [/is-seatgeek-legit](https://seatgeek.com/is-seatgeek-legit) | Is SeatGeek Legit? \| SeatGeek | [trust-light-1440.png](screenshots/trust-light-1440.png) |
| [/accessibility](https://seatgeek.com/accessibility) | Digital Accessibility Statement \| SeatGeek | [accessibility-light-1440.png](screenshots/accessibility-light-1440.png) |
| [/blog](https://seatgeek.com/blog) | SeatGeek Blog \| SeatGeek | [blog-light-1440.png](screenshots/blog-light-1440.png) |
| [/enterprise/newsroom](https://seatgeek.com/enterprise/newsroom) | Newsroom \| SeatGeek | [newsroom-light-1440.png](screenshots/newsroom-light-1440.png) |
| [/help](https://seatgeek.com/help) | Help Center \| SeatGeek | [help-light-1440.png](screenshots/help-light-1440.png) |
| [/sell](https://seatgeek.com/sell) | Sell Tickets \| SeatGeek | [sell-light-1440.png](screenshots/sell-light-1440.png) |
| [/enterprise](https://seatgeek.com/enterprise) | Enterprise \| SeatGeek | [enterprise-light-1440.png](screenshots/enterprise-light-1440.png) |
| [/build](https://seatgeek.com/build) | Platform Overview \| SeatGeek | [platform-light-1440.png](screenshots/platform-light-1440.png) |
| [chairnerd.seatgeek.com](https://chairnerd.seatgeek.com/) | ChairNerd - Code, Design, and Growth at SeatGeek | [devblog-light-1440.png](screenshots/devblog-light-1440.png) |
| [/terms](https://seatgeek.com/terms) | Terms of Use \| SeatGeek | [terms-light-1440.png](screenshots/terms-light-1440.png) |
| [/privacy](https://seatgeek.com/privacy) | Privacy Notice \| SeatGeek | [privacy-light-1440.png](screenshots/privacy-light-1440.png) |
| [/sitemap](https://seatgeek.com/sitemap) | Sitemap \| SeatGeek | [sitemap-light-1440.png](screenshots/sitemap-light-1440.png) |
| [/cities](https://seatgeek.com/cities) | The SeatGeek guide to live events in your city \| SeatGeek | [cities-light-1440.png](screenshots/cities-light-1440.png) |
| Sign in dialog on [/sports-tickets](https://seatgeek.com/sports-tickets) | Sports Tickets \| 2026-2027 events & schedule \| SeatGeek | [login-light-1440.png](screenshots/login-light-1440.png) |

The sports page itself was open behind the menus and the login dialog. A later navigation to `/sports-tickets`, `/concert-tickets`, and `/theater-tickets` returned a DataDome captcha page. Those frames were discarded. The category pages were not re-shot.

## Auth walls

Sign in is one dialog. There is no separate signup control in the header or footer.

| Probe | Result |
|---|---|
| Header Sign in | Dialog: "Sign in or create account". One empty email field and Continue. |
| Identity providers | None in the dialog. Google, Apple, Facebook, passkey, and wallet were not shown and were not clicked. |
| Connect to Spotify | Homepage button. Not clicked. |
| Creators phone field | [/ambassador](https://seatgeek.com/ambassador) painted a phone input. The screenshot was discarded. Nothing was typed. |
| [/login](https://seatgeek.com/login) | Not opened this pass. An earlier pass recorded a DataDome interstitial. |

`login-extracted` stays `not-started`.

## Where the walk stopped

The walk stopped at the Sign in dialog. Continue was not clicked, so the next step of account creation was not seen. Checkout was not entered. No ticket row was opened. Subscribe, follow, and the creators phone field were not submitted. After the marketing pages above, DataDome started returning a captcha interstitial. That wall was not solved. The phone-width homepage was not photographed for that reason.
