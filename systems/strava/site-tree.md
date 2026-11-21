# Strava public site tree

Mapped signed out on 2026-11-22 from [https://www.strava.com](https://www.strava.com). The browser stayed on [https://www.strava.com/](https://www.strava.com/). Title "Strava | Running, Cycling & Hiking App - Train, Track & Share". Headless Chromium, 1440 by 900 CSS pixels, `devicePixelRatio` 2. Visual viewport scale 1. Screenshots are 2880 by 1800. The page is a live marketing site, not a parked domain and not a captcha wall.

A Cookiebot bar covered the footer on first paint. It was removed from the DOM for the photographs. Accept All, Customize, and Reject Non-Essential were not clicked.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Log In, Sign Up, Sign Up With Google, Sign Up With Apple, and Sign Up With Email were not opened. `login-extracted` stays `not-started`.

`catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/strava/`.

Tracking query strings (`origin`, `utm_source`, `utm_medium`, `cta`, `element`, `source`) are not recorded as destinations below. The hrefs are the paths the homepage printed.

## Header

Photographed: [home-light-1440.png](screenshots/home-light-1440.png).

The bar is white, 73px. The mark and wordmark are inline SVGs, fill `#fc5200`, saved as [icons/echelon.svg](icons/echelon.svg) (20 by 28) and [icons/wordmark.svg](icons/wordmark.svg) (95 by 20). Nav labels are Boathouse, 16px, weight 400, black.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Strava | button, logo | [https://www.strava.com/](https://www.strava.com/) | home |
| Activities | button | sport menu | opened in the DOM, not photographed as its own page |
| Features | link | [/features](https://www.strava.com/features) | opened |
| Maps | link | [/maps](https://www.strava.com/maps) | listed, not opened |
| Challenges | link | [/challenges](https://www.strava.com/challenges) | listed, not opened |
| Subscription | link | [/subscribe](https://www.strava.com/subscribe) | listed, not opened |
| Log In | button | login wall | stopped. Not opened. 88 by 40, white, 1px border `rgb(224, 224, 222)`, radius 4px, label `rgb(33, 33, 31)` |

## Activities menu

The button sits in a list item that holds these public sport links. The open panel was not photographed.

| Label | Destination | This pass |
|---|---|---|
| Running | [/sports/running](https://www.strava.com/sports/running) | listed, not opened |
| Cycling | [/sports/cycling](https://www.strava.com/sports/cycling) | listed, not opened |
| Walking | [/sports/walking](https://www.strava.com/sports/walking) | listed, not opened |

A collapsed mobile nav also lists Home, Support, and Get the App. Those links were not visible at 1440.

## Homepage column

The fold is a three-part band: a cycling photograph, a white signup column, and a watch photograph. Heading "Community-Powered Motivation", 32px, weight 600, black.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Already a Member? Log In | link | [/login](https://www.strava.com/login) | stopped. Label is `#fc5200`, 16px, weight 600 |
| Sign Up With Google | button | identity provider | stopped. Not clicked. 404 by 44, fill `rgb(250, 250, 250)`, border `rgb(100, 99, 94)`, radius 4px |
| Sign Up With Apple | button | identity provider | stopped. Not clicked |
| Sign Up With Email | button | signup wall | stopped. Not clicked. 404 by 44, fill `rgb(252, 82, 0)`, white type, radius 4px |
| Terms of Service | link | [/legal/terms](https://www.strava.com/legal/terms) | listed, not opened |
| Privacy Policy | link | [/legal/privacy](https://www.strava.com/legal/privacy) | listed, not opened |

## Footer

Fill `rgb(249, 248, 245)`. The orange echelon sits above App Store and Google Play badges. Social icons point at Twitter, YouTube, Instagram, LinkedIn, and Facebook. Those off-site links were not opened.

| Column | Links | This pass |
|---|---|---|
| Features | Features `/features`, What's New `/whats-new`, Stories `https://stories.strava.com/`, Routes `/routes/hiking/usa`, About `/about` | About and Features are public. About was not photographed. Features was opened |
| Subscription | Subscription `/subscribe`, Family Plan `/family`, Bulk Subscriptions `/bulk-subscriptions`, Student Discount `/student`, Teacher, Military & Medical Discount `/subscribe#discount-plans`, Send a Gift `/gift` | listed, not opened. Gift and checkout not submitted |
| Support | Support `https://support.strava.com`, Business `https://business.strava.com/`, Partner Center `https://partners.strava.com/`, Careers `/careers`, Press `https://press.strava.com/` | listed, not opened |
| Privacy | Privacy `/legal/privacy`, Cookie Policy `/legal/cookie_policy`, Do Not Share My Personal Information (button), Terms `/legal/terms`, Log In `/login` | Log In stopped. The privacy button was not clicked |

Footer Log In is the same orange as the signup button.

## Pages opened

| Page | URL | Result |
|---|---|---|
| Home | [https://www.strava.com/](https://www.strava.com/) | Public marketing page. Photographed |
| Features | [https://www.strava.com/features](https://www.strava.com/features) | Public subscription page. Title "Strava Subscription". Photographed. The page is 8104px tall. Only the first viewport was saved |

## Stopped

Log In, Sign Up, Sign Up With Google, Sign Up With Apple, Sign Up With Email, gift, subscribe checkout, and any athlete profile. No athlete name was on either photograph.
