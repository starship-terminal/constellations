# Patterns

## Home

https://www.pexels.com/ signed out. White page, wordmark left, Explore, License, and a black Join pill on the right. Hero heading at 48px bold, tracking -2px, beside a challenge card. Search field under the heading. Pill tabs (Home, Videos, Leaderboard, Challenges, Winners Wall, Photography Series). Topic chips sit in white cards with a 1px #ededed border.

Desktop screenshot is 1440×900 CSS, PNG 2880×1800. Phone screenshot is 390×844 CSS, PNG 780×1688.

![Home](screenshots/home-light-default.png)

![Home, phone](screenshots/home-light-phone.png)

## Search

https://www.pexels.com/search/nature/ loaded in the preview tab. Heading "Nature Images" at 36px bold, tracking -2px, colour #191919. Tabs Photos, Videos, Users use the same pill as Home. Related terms are 180px-radius pills with a 1px #ededed border. Headless Chromium got a Cloudflare challenge on this URL, so there is no screenshot.

## Photo

https://www.pexels.com/photo/slow-shutter-city-night-late-night-brake-light-4057078/ loaded in the preview tab. Free download is the alien button. License reads Free. No file was downloaded. No screenshot: the headless retry hit Cloudflare.

## License and about

https://www.pexels.com/license/ and https://www.pexels.com/about/ are public. Headings use the 36px title style. Body copy on the license page is 17px, max-width 490px. Footer is white, padding 80px 30px 30px, with Pexels, Company, and download links. No screenshots: headless Chromium hit Cloudflare after the home page.

## Join and login

https://www.pexels.com/join/ asks for first name, last name, email, and password, plus Google. https://www.pexels.com/login/ asks for email and password, plus Google, with a forgot-password link to /password/new/. Neither form was submitted. The join form is not email-only, so AgentMail was not used. No card, phone, or KYC field was entered.

## Gaps

Signed-in library, upload, Pro, checkout, and account settings were not entered. Dark mode is declared and was not switched on. Phone layout was screenshotted only for home.
