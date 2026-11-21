# ElevenMusic public site tree

Mapped 2026-11-21 from [https://elevenmusic.io/](https://elevenmusic.io/) in headless Chromium at 1440×900, signed out. Every control below was opened far enough to see what it shows. A login or signup wall ends that branch. No email, name, password, or code was typed. Google and Apple were not clicked. Continue with Email was not pressed.

The Cookiebot banner was hidden with CSS. Accept was not clicked.

## Shell (every app page)

| Control | Opens |
|---|---|
| Wordmark | page [https://elevenmusic.io/](https://elevenmusic.io/) |
| Search | dialog: Log in or sign up. Branch stops. |
| Sidebar Explore | page [https://elevenmusic.io/explore](https://elevenmusic.io/explore) |
| Sidebar Create | dialog: Log in or sign up. Branch stops. |
| Sidebar Library | dialog: Log in or sign up. Branch stops. |
| Sidebar Tools | page [https://elevenmusic.io/tools](https://elevenmusic.io/tools) |
| Sidebar Sounds | page [https://elevenmusic.io/sounds](https://elevenmusic.io/sounds) |
| Sidebar Composer | dialog: Log in or sign up. Branch stops. |
| Sidebar Chat | dialog: Log in or sign up. Branch stops. |
| Publish your music | dialog: Log in or sign up. Branch stops. |
| New playlist | dialog: Log in or sign up. Branch stops. |
| Eleven Album Vol. 2 | page [https://elevenmusic.io/playlists/69eb381eb3c0fe73c21c695c](https://elevenmusic.io/playlists/69eb381eb3c0fe73c21c695c) |
| Made with v2.5 | page [https://elevenmusic.io/playlists/6aa3c77bfa25c34a5ad1e579](https://elevenmusic.io/playlists/6aa3c77bfa25c34a5ad1e579) |
| Close sidebar | local: collapses the sidebar. Reopens from the same control. |
| Top Explore | page [https://elevenmusic.io/explore](https://elevenmusic.io/explore) |
| Resources | menu: Blog, Help center, Contact, ElevenLabs. See Resources. |
| Pricing | page [https://elevenmusic.io/pricing](https://elevenmusic.io/pricing) |
| Sign in | dialog: Log in or sign up. Branch stops. |
| Start free | dialog: Log in or sign up. Branch stops. |
| Open menu (390) | sheet: the same Log in or sign up dialog. Branch stops. |

## Log in or sign up

Same wall as a dialog on the current page, and as a full page at [https://elevenmusic.io/login](https://elevenmusic.io/login).

| Control | Opens |
|---|---|
| Continue with Google | not clicked. Branch stops. |
| Continue with Apple | not clicked. Branch stops. |
| Terms of Service | page [https://elevenmusic.io/terms-of-use](https://elevenmusic.io/terms-of-use) |
| Privacy Policy | external [https://elevenlabs.io/privacy-policy](https://elevenlabs.io/privacy-policy) |
| Show other options | same dialog, extra fields. See below. |
| Hide other options | returns to the Google and Apple step. |
| Close | closes the dialog. The /login page has no close. |
| Try it first | page [https://elevenmusic.io/](https://elevenmusic.io/). Only on /login. |

Show other options adds:

| Control | Opens |
|---|---|
| Enter email address | empty field. Left empty. |
| Terms checkbox | unchecked. Not checked. |
| Continue with Email | disabled while the email field is empty. Not pressed. Copy says a magic link would be sent. |
| Terms of Service | page [https://elevenmusic.io/terms-of-use](https://elevenmusic.io/terms-of-use) |
| Privacy Policy | external [https://elevenlabs.io/privacy-policy](https://elevenlabs.io/privacy-policy) |

Direct loads that become this wall:

| URL | Lands on |
|---|---|
| /studio | [https://elevenmusic.io/login?redirect=%2Fstudio](https://elevenmusic.io/login?redirect=%2Fstudio) |
| /studio?billing=true | [https://elevenmusic.io/login?redirect=%2Fstudio](https://elevenmusic.io/login?redirect=%2Fstudio). The billing query is dropped. |
| /styles | [https://elevenmusic.io/login?redirect=%2Fstyles](https://elevenmusic.io/login?redirect=%2Fstyles) |
| /library | [https://elevenmusic.io/login?redirect=%2Flibrary](https://elevenmusic.io/login?redirect=%2Flibrary) |
| /compositions | [https://elevenmusic.io/login?redirect=%2Fcompositions](https://elevenmusic.io/login?redirect=%2Fcompositions) |
| /login | [https://elevenmusic.io/login](https://elevenmusic.io/login) |

## Home

[https://elevenmusic.io/](https://elevenmusic.io/). Title: Make music yours.

| Control | Opens |
|---|---|
| Attach | menu: From your library, Upload a file, Record. Each then opens a Log in to upload dialog. Branch stops. |
| Prompt field | local text field. Not submitted. |
| Create (submit) | stays on the page when the prompt already has placeholder text. A signed-out submit was not forced. |
| Trap beat, Loop to chop, Topline, Amapiano, Trailer cue, Techno | local: fills the prompt. Does not navigate. |
| Play, Another beat, Original, 1, 2, 3 | local demo on the marketing sections. |
| half-time drums, sliding 808s, a dusty church organ | local demo toggles. |
| Drums, Bass, Keys, Vox | local demo. Previous and Next move the demo. |
| Make this beat | page [https://elevenmusic.io/login?redirect=%2Fstudio](https://elevenmusic.io/login?redirect=%2Fstudio). Branch stops. |
| Edit a song | same login redirect. Branch stops. |
| Browse Sounds | page [https://elevenmusic.io/sounds](https://elevenmusic.io/sounds) |
| Songs / Sounds | local tabs in the genre strip. |
| Song titles in that strip | local: expands the description. |
| Browse songs | page [https://elevenmusic.io/explore](https://elevenmusic.io/explore) |
| Featured, Trending, New | local tabs on the public track row. |
| Play track | local playback on the public row. |
| Artist name on a card | page `/artists/<slug>`. One example: [GhostMKC](https://elevenmusic.io/artists/ghostmkc-5JuuiL). |
| Vocals Sign up | page [https://elevenmusic.io/login?redirect=%2Fstudio](https://elevenmusic.io/login?redirect=%2Fstudio). Branch stops. |
| Styles Sign up | page [https://elevenmusic.io/login?redirect=%2Fstyles](https://elevenmusic.io/login?redirect=%2Fstyles). Branch stops. |
| Plan Start free | same studio login redirect. Branch stops. |
| Get Pro | [https://elevenmusic.io/login?redirect=%2Fstudio](https://elevenmusic.io/login?redirect=%2Fstudio). Branch stops. |
| Download on the App Store, Scan to download | external [https://apps.apple.com/us/app/elevenmusic-by-elevenlabs/id6755965224](https://apps.apple.com/us/app/elevenmusic-by-elevenlabs/id6755965224) |
| FAQ questions | local accordion. Is it free? opens its answer. |

## Resources menu

| Item | Opens |
|---|---|
| Blog | page [https://elevenmusic.io/blog](https://elevenmusic.io/blog) |
| Help center | external [https://help.elevenlabs.io/hc/en-us/sections/46215000024337-ElevenMusic](https://help.elevenlabs.io/hc/en-us/sections/46215000024337-ElevenMusic) |
| Contact | external [https://help.elevenlabs.io/hc/en-us/requests/new](https://help.elevenlabs.io/hc/en-us/requests/new). Not submitted. |
| ElevenLabs | external [https://elevenlabs.io/](https://elevenlabs.io/) |

## Explore

[https://elevenmusic.io/explore](https://elevenmusic.io/explore). Public catalog plus a create prompt.

| Control | Opens |
|---|---|
| Create link in the prompt area | page [https://elevenmusic.io/login?redirect=%2Fstudio](https://elevenmusic.io/login?redirect=%2Fstudio). Branch stops. |
| Composer | page [https://elevenmusic.io/login?redirect=%2Fcompositions](https://elevenmusic.io/login?redirect=%2Fcompositions). Branch stops. |
| Styles | page [https://elevenmusic.io/login?redirect=%2Fstudio](https://elevenmusic.io/login?redirect=%2Fstudio). Branch stops. |
| Library | page [https://elevenmusic.io/login?redirect=%2Flibrary](https://elevenmusic.io/login?redirect=%2Flibrary). Branch stops. |
| Remix | page [https://elevenmusic.io/login?redirect=%2Fstudio](https://elevenmusic.io/login?redirect=%2Fstudio). Branch stops. |
| Like | dialog: Log in or sign up. Branch stops. |
| Tempo | dialog: Auto, BPM, Tap tempo. Local. Closed without setting a value. |
| Play track, Play playlist | local playback. |
| Playlist title | page `/playlists/<id>` |
| Artist name | page `/artists/<slug>` |

## Tools

[https://elevenmusic.io/tools](https://elevenmusic.io/tools).

| Control | Opens |
|---|---|
| Featured, Studio, All | local tabs. All reveals two more tools. |
| Voice to Song | page [https://elevenmusic.io/tools/voice-studio](https://elevenmusic.io/tools/voice-studio) |
| Genreshift | page [https://elevenmusic.io/tools/genreshift](https://elevenmusic.io/tools/genreshift) |
| Sample to Song | page [https://elevenmusic.io/tools/sample-to-song](https://elevenmusic.io/tools/sample-to-song) |
| Unplugged | page [https://elevenmusic.io/tools/unplugged](https://elevenmusic.io/tools/unplugged) |
| Voice Memo to Song (All tab) | page [https://elevenmusic.io/tools/voice-memo-to-song](https://elevenmusic.io/tools/voice-memo-to-song) |
| Hum to Song (All tab) | page [https://elevenmusic.io/tools/hum-to-song](https://elevenmusic.io/tools/hum-to-song) |

Each tool page has a public form (duration, Attach, Generate track) and a More tools row. Attach opens the same audio menu, plus Visuals. Generate track was not submitted. Signing in is required before a generation can be saved. That branch stops at the login wall if a control asks for an account.

## Sounds

[https://elevenmusic.io/sounds](https://elevenmusic.io/sounds).

| Control | Opens |
|---|---|
| Packs | page [https://elevenmusic.io/sounds/packs](https://elevenmusic.io/sounds/packs) |
| A pack card | page `/sounds/packs/<id>`. Example: Slap Bass Vol. 1. |
| Instrument | menu: Any instrument, Vocal chops, Vocal loops, Melody loops, Drum loops, Bass loops, Guitar loops, and further instrument rows. Local filter. |
| Genre | menu: Any genre, Trap, Hip hop, Afro house, Lo-fi, R&B, Drill, House, Pop, Ambient, Phonk. Local filter. |
| BPM | filter control. Present on the page. Not submitted. |
| Like | dialog: Log in or sign up. Branch stops. |
| Download | dialog: Log in to download this Sound for free. Same Google, Apple, and Show other options wall. Branch stops. |
| Turn into full song | dialog: Log in to continue. Branch stops. |
| Generate sound | public control on the page. Not submitted. |
| Tempo, Key, 4 bars, Off | local sound settings. |

## Pricing

[https://elevenmusic.io/pricing](https://elevenmusic.io/pricing).

| Control | Opens |
|---|---|
| Start free | page [https://elevenmusic.io/login?redirect=%2Fstudio](https://elevenmusic.io/login?redirect=%2Fstudio). Branch stops. |
| Get Pro | same studio login redirect. Branch stops. |
| FAQ questions | local accordion, same questions as home. |

## Tracks, charts, artists, genres

| Page | What it opens |
|---|---|
| [https://elevenmusic.io/tracks](https://elevenmusic.io/tracks) | Public track list. Genre chips go to `/genres/<slug>`. Artist names go to `/artists/<slug>`. Like and Remix stop at the login wall. Start a track stays on the page. |
| [https://elevenmusic.io/charts](https://elevenmusic.io/charts) | Public chart. Play and Shuffle play. Share opens the share dialog. Like stops at login. |
| [https://elevenmusic.io/artists](https://elevenmusic.io/artists) | Artist index. Each card is `/artists/<slug>`. |
| [https://elevenmusic.io/genres](https://elevenmusic.io/genres) | Genre index. Each card is `/genres/<slug>`. |
| A genre page | Public tracks in that genre, plus artist links. |
| An artist page | Public profile. Play plays. Follow stops at login. Share opens the share dialog. Top Songs and Latest Releases are `/artists/<slug>/top-songs` and `/artists/<slug>/releases`. |

Genre slugs linked from the index: electronic, ambient, pop, hip-hop, folk, rock, indie, rnb, classical, soul, jazz, latin, funk, country, house, metal.

## Playlist and share

A playlist page is public. Play and Shuffle play. Like stops at the login dialog.

Share opens a dialog:

| Control | Opens |
|---|---|
| Copy link | copies the public playlist URL. Not followed further. |
| Download image | local image action in the dialog. |
| X | external intent URL on x.com. Not opened. |
| Facebook | external sharer URL. Not opened. |
| LinkedIn | external share URL. Not opened. |
| Reddit | external submit URL. Not opened. |
| Email | mailto link. Not opened. |
| Close | closes the dialog. |

## Blog

[https://elevenmusic.io/blog](https://elevenmusic.io/blog).

| Control | Opens |
|---|---|
| All | [https://elevenmusic.io/blog](https://elevenmusic.io/blog) |
| Guides | [https://elevenmusic.io/blog/category/guides](https://elevenmusic.io/blog/category/guides) |
| Product | [https://elevenmusic.io/blog/category/product](https://elevenmusic.io/blog/category/product) |
| Industry | [https://elevenmusic.io/blog/category/industry](https://elevenmusic.io/blog/category/industry) |
| A post title | page `/blog/<slug>`. Example: [https://elevenmusic.io/blog/how-to-prompt-music](https://elevenmusic.io/blog/how-to-prompt-music) |

Posts seen on the index: introducing-music-v2-5, chaos, 1-million-voices, soundcloud-integration, ade-closing-party, introducing-muse, introducing-composer, introducing-sounds, achievements, how-to-prompt-music, introducing-references, introducing-vocals, summer-of-sound, introducing-mixes, introducing-tools.

## Footer

Present on marketing pages (home, pricing, blog, terms, genre index). The explore and tools shells omit it.

| Control | Opens |
|---|---|
| Browse tracks | [https://elevenmusic.io/tracks](https://elevenmusic.io/tracks) |
| Charts | [https://elevenmusic.io/charts](https://elevenmusic.io/charts) |
| Artists | [https://elevenmusic.io/artists](https://elevenmusic.io/artists) |
| All genres | [https://elevenmusic.io/genres](https://elevenmusic.io/genres) |
| Electronic, Ambient, Pop, Hip-Hop, Folk, Rock | the matching `/genres/<slug>` page |
| Blog | [https://elevenmusic.io/blog](https://elevenmusic.io/blog) |
| ElevenLabs | external [https://elevenlabs.io/](https://elevenlabs.io/) |
| Help center | external help.elevenlabs.io section |
| Contact | external help.elevenlabs.io request form. Not submitted. |
| Terms of Service | [https://elevenmusic.io/terms-of-use](https://elevenmusic.io/terms-of-use) |
| Privacy Policy | external [https://elevenlabs.io/privacy-policy](https://elevenlabs.io/privacy-policy) |
| CCPA Notice | external [https://elevenlabs.io/ccpa-notice-at-collection](https://elevenlabs.io/ccpa-notice-at-collection) |
| Cookie settings | Cookiebot. Hidden, not accepted. |
| X, Instagram, Discord | external [https://x.com/elevenmusic_io](https://x.com/elevenmusic_io), [https://instagram.com/elevenmusicio](https://instagram.com/elevenmusicio), [https://discord.gg/elevenlabs](https://discord.gg/elevenlabs) |
| English | menu: English, Arabic, German, Spanish, French, Hindi, Japanese, Korean, Dutch, Polish, Portuguese, Brazilian Portuguese, Chinese. Not switched. |
| System theme, Light theme, Dark theme | local theme. Dark is pressed by default. Light was clicked once to measure the light theme, then left. |

Terms of Service also links the Prohibited Use Policy at [https://elevenlabs.io/use-policy](https://elevenlabs.io/use-policy) and a help request form. Neither was submitted.
