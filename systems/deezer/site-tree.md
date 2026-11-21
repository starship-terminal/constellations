# Deezer public site tree

Mapped 2026-11-21 from the signed-out public site, starting at https://www.deezer.com/en/. Cookie banner was hidden in the DOM and not accepted or refused. No email, password, OAuth button, signup form, newsletter or captcha was used. Branches that open a login or signup wall stop at that URL.

Desktop captures are 1440 by 900 CSS pixels. Phone captures are 390 by 844 CSS pixels at 2x (780 by 1688 PNG).

## Shell

Marketing pages (homepage, offers, features, legal) share one header and one footer. The channel player (Explore, Charts) uses a different shell: left nav, search, bottom player, signup banner.

### Marketing header (desktop)

| Control | Opens |
|---|---|
| Logo | https://www.deezer.com/en/ |
| Plans | https://www.deezer.com/en/offers |
| Features | https://www.deezer.com/explore/features/ |
| Music | https://www.deezer.com/en/channels/explore (player shell) |
| Log in | https://account.deezer.com/en/login/ (login wall, stop) |
| Sign up | https://account.deezer.com/en/signup/ (signup wall, stop) |

### Marketing header (phone)

| Control | Opens |
|---|---|
| Logo | https://www.deezer.com/en/ |
| Sign up | https://account.deezer.com/en/signup/ (signup wall, stop) |
| Burger (`.burger-menu`) | Full-screen drawer. Items: Log in (login wall), Sign up (signup wall), Plans, Explore Channels, Features. Close returns to the page. Screenshot: [home-phone-menu-open.png](screenshots/home-phone-menu-open.png) |

### Player shell (desktop, signed out)

| Control | Opens |
|---|---|
| Home | Channel home. Playing a personal home stops at login if the route requires an account. Public channel pages loaded. |
| Explore | https://www.deezer.com/en/channels/explore |
| Search field | Focus shows the same field. No query was typed. Screenshot: [explore-desktop-search-focus.png](screenshots/explore-desktop-search-focus.png) |
| Plans | Offers page |
| Log in | Login wall, stop |
| Sign up | Signup wall, stop |
| Create a playlist | Login wall, stop |
| Play, next, shuffle, favourite, queue, volume | In-page player controls. Play started a preview track (Don't Start Now) without an account. No account action was submitted. |
| Sign up for free banner | Signup wall, stop |
| Listen on Deezer (phone) | Login or app handoff. Not followed past the wall. |

## Pages captured

| Page | URL | Desktop | Phone |
|---|---|---|---|
| Home | https://www.deezer.com/en/ | [screenshots/home-desktop-default.png](screenshots/home-desktop-default.png) | [screenshots/home-phone-default.png](screenshots/home-phone-default.png) |
| Offers | https://www.deezer.com/en/offers | [screenshots/offers-desktop-default.png](screenshots/offers-desktop-default.png) | [screenshots/offers-phone-default.png](screenshots/offers-phone-default.png) |
| Premium offer | https://www.deezer.com/en/offers/premium | [screenshots/offers-premium-desktop-default.png](screenshots/offers-premium-desktop-default.png) | [screenshots/offers-premium-phone-default.png](screenshots/offers-premium-phone-default.png) |
| Features | https://www.deezer.com/explore/features/ | [screenshots/features-desktop-default.png](screenshots/features-desktop-default.png) | [screenshots/features-phone-default.png](screenshots/features-phone-default.png) |
| Flow | https://www.deezer.com/explore/features/flow/ | [screenshots/feature-flow-desktop-default.png](screenshots/feature-flow-desktop-default.png) | [screenshots/feature-flow-phone-default.png](screenshots/feature-flow-phone-default.png) |
| Download | https://www.deezer.com/explore/download/ | [screenshots/download-desktop-default.png](screenshots/download-desktop-default.png) | [screenshots/download-phone-default.png](screenshots/download-phone-default.png) |
| Explore channels | https://www.deezer.com/en/channels/explore | [screenshots/explore-desktop-default.png](screenshots/explore-desktop-default.png) | [screenshots/explore-phone-default.png](screenshots/explore-phone-default.png) |
| Charts | https://www.deezer.com/en/channels/charts | [screenshots/charts-desktop-default.png](screenshots/charts-desktop-default.png) | [screenshots/charts-phone-default.png](screenshots/charts-phone-default.png) |
| Login wall | https://account.deezer.com/en-us/login/ | [screenshots/login-wall-desktop-default.png](screenshots/login-wall-desktop-default.png) | [screenshots/login-wall-phone-default.png](screenshots/login-wall-phone-default.png) |
| Support | https://support.deezer.com/hc/en-gb | [screenshots/support-desktop-default.png](screenshots/support-desktop-default.png) | [screenshots/support-phone-default.png](screenshots/support-phone-default.png) |
| Terms | https://www.deezer.com/legal/cgu | [screenshots/legal-desktop-default.png](screenshots/legal-desktop-default.png) | [screenshots/legal-phone-default.png](screenshots/legal-phone-default.png) |
| Accessibility | https://www.deezer.com/explore/accessibility/ | [screenshots/accessibility-desktop-default.png](screenshots/accessibility-desktop-default.png) | [screenshots/accessibility-phone-default.png](screenshots/accessibility-phone-default.png) |
| AI music detector | https://www.deezer.com/explore/ai-music-detector/ | [screenshots/ai-detector-desktop-default.png](screenshots/ai-detector-desktop-default.png) | [screenshots/ai-detector-phone-default.png](screenshots/ai-detector-phone-default.png) |

Also loaded and inventoried, screenshots not all kept: family offer, HiFi, devices, reviews, support request form (not submitted), status page.

## Homepage controls

| Control | Destination | Stop |
|---|---|---|
| a | https://www.deezer.com/ |  |
| Plans | https://www.deezer.com/en/offers/ |  |
| Features | https://www.deezer.com/explore/features/ |  |
| Music | https://www.deezer.com/en/channels/explore/ |  |
| Log in | https://account.deezer.com/en/login/ | login wall |
| Sign up | https://account.deezer.com/en/signup/ | login wall |
| Try for free | https://account.deezer.com/en/signup/ | login wall |
| PREMIUM | https://www.deezer.com/payment/go.php |  |
| Try for free | https://www.deezer.com/payment/go.php |  |
| Discover all our plans | https://www.deezer.com/en/offers |  |
| Explore our catalogue | https://www.deezer.com/channels/explore |  |
| Transfer my music | https://www.deezer.com/explore/features/transfer-playlist/ |  |
| Scan my playlists | https://www.deezer.com/explore/ai-music-detector/ |  |
| What are the advantages of a Deezer Premium subscription? | in-page control |  |
| What does offline listening mean? | in-page control |  |
| How many devices can be paired to one Deezer Premium account | in-page control |  |
| What is the difference between a Deezer Premium account and  | in-page control |  |
| Deezer Family | https://www.deezer.com/en/offers/family |  |
| a | https://www.deezer.com/en/offers/family |  |
| I've just upgraded to Deezer Premium, so why does my account | in-page control |  |
| https://www.deezer.com/legal/cgu | https://www.deezer.com/legal/cgu |  |
| a | https://apps.apple.com/us/app/deezer-music-podcast-player/id292738169 |  |
| a | https://play.google.com/store/apps/details |  |
| Download the Deezer app | https://www.deezer.com/explore/download/ |  |
| Offers | https://www.deezer.com/en/offers |  |
| Reviews | https://www.deezer.com/explore/reviews/ |  |
| Use a promo code | https://account.deezer.com/en/gift/ | login wall |
| Buy a gift card | https://www.deezer.com/payment/go.php |  |
| FAQ | https://support.deezer.com/hc/en-gb |  |
| Contact Deezer | https://support.deezer.com/hc/en-gb/requests/new |  |
| Status update | https://support.deezer.com/hc/en-gb/p/status-updates |  |
| Flow | https://www.deezer.com/explore/features/flow/ |  |
| Song identifier | https://www.deezer.com/explore/features/songcatcher/ |  |
| Transfer your music | https://www.deezer.com/explore/features/transfer-playlist/ |  |
| Listen with lyrics | https://www.deezer.com/explore/features/lyrics/ |  |
| Offline mode | https://www.deezer.com/explore/features/offline/ |  |
| HiFi sound quality | https://www.deezer.com/explore/features/hifi/ |  |
| Shared playlists | https://www.deezer.com/explore/features/shaker/ |  |
| Play Music Quiz | https://www.deezer.com/explore/features/music-quiz/ |  |
| Compatible devices | https://www.deezer.com/explore/devices/ |  |
| AI Music Labeling | https://www.deezer.com/explore/features/ai-labelling/ |  |
| My Deezer Year & My Deezer Month | https://www.deezer.com/explore/features/my-deezer-year-and-music-recap/ |  |
| Explore the catalogue | https://www.deezer.com/en/channels/explore |  |
| Top songs | https://www.deezer.com/en/channels/charts |  |
| New releases | https://www.deezer.com/en/channels/new |  |
| The Backstage - Deezer Blog | https://www.thebackstage-deezer.com/ |  |
| Deezer Community | https://en.deezercommunity.com/ |  |
| Deezer Club | https://www.deezer.com/explore/features/purpleclub/ |  |
| AI Music Detector | https://www.deezer.com/explore/ai-music-detector/ |  |
| About us | https://www.deezer.com/en/ |  |
| Press & News | https://www.newsroom-deezer.com/ |  |
| Artist-Centric Payment System (ACPS) | https://www.deezer.com/explore/artist-remuneration/ |  |
| Deezer for business | https://business.deezer.com/ |  |
| Deezer for Creators | https://creators.deezer.com/en |  |
| Deezer for Developers | https://developers.deezer.com/ |  |
| Investors | https://www.deezer-investors.com/ |  |
| Advertise on Deezer | https://business.deezer.com/advertising/ |  |
| Deezer for professionals | https://business.deezer.com/deezer-for-professionals/ |  |
| Careers | https://www.deezerjobs.com/ |  |
| Legal | https://www.deezer.com/legal/legal |  |
| Terms and Conditions | https://www.deezer.com/legal/cgu |  |
| Privacy policy | https://www.deezer.com/legal/personal-datas |  |
| Open Source Software Report | https://www.deezer.com/explore/licenses |  |
| Vulnerability Disclosure Policy | https://vdp.deezer.com/p/Welcome |  |
| Accessibility | https://www.deezer.com/explore/accessibility/ |  |
| a | https://www.deezer.com/en/ |  |
| a | https://www.facebook.com/Deezer |  |
| a | https://www.instagram.com/deezer |  |
| a | https://x.com/Deezer |  |
| a | https://www.youtube.com/@deezerglobal |  |
| Čeština Dansk Deutsch English English (us) Español Español ( | in-page control |  |

FAQ summaries on the homepage toggle an accordion in place. One was opened: [home-desktop-faq-open.png](screenshots/home-desktop-faq-open.png). The language `select` was focused and not changed.

## Login wall

https://account.deezer.com/en-us/login/ shows Email, Password, Show password, Forgotten password, Log in, Facebook, Google, Apple, and Sign up. Nothing was typed. No OAuth button was clicked. Focus was moved to the email field with the keyboard only: [login-wall-desktop-email-focus.png](screenshots/login-wall-desktop-email-focus.png).

## Stopped branches

These URLs were linked from public pages and not opened past the wall:

- https://account.deezer.com/en-us/gift
- https://account.deezer.com/en-us/login
- https://account.deezer.com/en-us/login/?redirect_uri=%2Fexplore%2Fai-music-detector
- https://account.deezer.com/en-us/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fus%2Fchannels%2Fcharts
- https://account.deezer.com/en-us/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fus%2Fchannels%2Fexplore
- https://account.deezer.com/en-us/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fus%2Fchannels%2Fnew
- https://account.deezer.com/en-us/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fus%2Fchannels%2Fpodcasts
- https://account.deezer.com/en-us/signup
- https://account.deezer.com/en-us/signup/?redirect_uri=%2Fexplore%2Fai-music-detector
- https://account.deezer.com/en-us/signup/?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fexplore%2Fen-us%2Ffeatures%2Ftransfer-playlist%2Fredirect%2F&step=0
- https://account.deezer.com/en-us/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fus%2Fchannels%2Fcharts
- https://account.deezer.com/en-us/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fus%2Fchannels%2Fexplore
- https://account.deezer.com/en-us/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fus%2Fchannels%2Fnew
- https://account.deezer.com/en-us/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fus%2Fchannels%2Fpodcasts
- https://account.deezer.com/en/gift
- https://account.deezer.com/en/login
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2F2000s
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fanimeverse
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fcharts
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fchill
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fdiscovery
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fexplore
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fexplore%2Fexplore-tab
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fforyou
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Flofi
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fnew
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fnext
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fparty
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fpiano
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fpodcasts
- https://account.deezer.com/en/login?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fworkout
- https://account.deezer.com/en/signup
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2F2000s
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fanimeverse
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fcharts
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fchill
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fdiscovery
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fexplore
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fexplore%2Fexplore-tab
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fforyou
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Flofi
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fnew
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fnext
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fparty
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fpiano
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fpodcasts
- https://account.deezer.com/en/signup?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fen%2Fchannels%2Fworkout
- https://account.deezer.com/fr/signup/?redirect_uri=https%3A%2F%2Fwww.deezer.com%2Fexplore%2Ffr%2Ffeatures%2Ftransfer-playlist%2Fredirect%2F&step=0
- https://account.deezer.com/gift
- https://account.deezer.com/signup
- https://creators.deezer.com/user/login
- https://creators.deezer.com/user/signup
- https://www.deezer.com/gift/?page=offer_gift

Payment links (`/payment/go.php`) were recorded and not followed. External sites (App Store, Play Store, newsroom, careers, community, investors, social) were recorded as off-site and not crawled.

## Channel tree

Explore links many public channel pages (`/en/channels/<slug>`). A sample loaded: charts, new, podcasts, chill, workout, piano, party, discovery, animeverse, lofi, 2000s. Each repeats the player shell and links to albums, playlists and artists. Album and artist pages are public catalogue pages. Actions that save, follow or create an account stop at the login wall. The crawl queue still held more than a thousand catalogue URLs when it was capped at 80 page loads. Those remaining URLs are the same channel pattern, not a different product surface.

