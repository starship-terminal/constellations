# iA Writer public site tree

Walked signed out on 2026-11-21 from [https://ia.net/writer](https://ia.net/writer) (title: iA Writer: The Original Focused Markdown Writing App). HTTP 200. Desktop viewport 1440. Phone viewport 390. The painted page is light: white and near-white surfaces, black text, a blue download pill. `theme-color` is `#f9f9f9`. No page-level theme switch. No cookie banner. Query strings are stripped. This package is iA Writer only. Notebook, Presenter, and the company pages are other iA products and are linked, not captured as this package.

Opened means the control was used and the destination loaded, or the in-page result was photographed. Linked means the href was read and the page was not opened in this pass.

## Header, desktop

The wordmark is two links: `iA` to `/`, and `Writer` to `/writer`.

| Control | Opens |
|---|---|
| iA | `/` (the company home). Other product. Linked. Not captured as this package. |
| Writer | `/writer` (this page) |
| Support | `/writer/support` |
| Buy | `/writer/pricing` |
| Download | `/writer/download` |

No Log in and no Sign up in the header. The app is a download, not a signed-in web shell.

## Menu (summary "Menu")

A `details.menu__more` drawer. The summary is an icon with accessible name "Menu". Opening it stays on `/writer`. Writer is expanded by default (`aria-expanded="true"` on the Writer toggle). Each product row is a title link plus a toggle that shows or hides that row's pages.

| Control | Opens |
|---|---|
| Writer (title) | `/writer` |
| Writer / Product Information | `/writer` |
| Writer / Buy | `/writer/pricing` |
| Writer / Download | `/writer/download` |
| Writer / Support | `/writer/support` |
| Notebook (title and Product Information) | `/notebook`. Other product. Linked. Not opened. |
| Presenter (title and Product Information) | `/presenter`. Other product. Linked. Not opened. |
| Presenter / Buy | `/presenter/pricing`. Other product. Linked. Not opened. |
| Presenter / Download | `/presenter/download`. Other product. Linked. Not opened. |
| Presenter / Support | `/presenter/support`. Other product. Linked. Not opened. |
| Support (title) | `/support`. Company support index. Linked. Not opened. |
| Support / Writer | `/writer/support` |
| Support / Presenter | `/presenter/support`. Other product. Linked. Not opened. |
| Downloads (title) | `/downloads`. Company downloads index. Linked. Not opened. |
| Downloads / Writer | `/downloads/writer` |
| Downloads / Presenter | `/downloads/presenter`. Other product. Linked. Not opened. |
| Downloads / Wallpapers | `/downloads/wallpapers`. Company asset page. Linked. Not opened. |
| Downloads / Screen Savers | `/downloads/screen-savers`. Company asset page. Linked. Not opened. |
| Downloads / Fonts | `/downloads/fonts`. Company asset page. Linked. Not opened. |
| About Us (title) | `/about-us`. Company page. Linked. Not opened. |
| About Us / Contact | `/about-us`. Same page. Linked. Not opened. |
| About Us / Careers | `/careers`. Linked. Not opened. |
| About Us / Dictionary | `/dictionary`. Linked. Not opened. |
| About Us / RSS | `/feed`. Linked. Not opened. |
| Blog (title) | `/topics`. Linked. Not opened. |
| Blog / Writer | `/topics/category/writer` |
| Blog / Presenter | `/topics/category/presenter`. Other product. Linked. Not opened. |
| Blog / Design | `/topics/category/design`. Linked. Not opened. |
| Legal (title) | `/legal`. Linked. Not opened. |
| Legal / Privacy | `/legal/privacy`. Linked. Not opened. It can print a street address. |
| EN | `/writer` |
| DE | `/de/writer`. Linked. Not opened. |
| 日 | `/ja/writer`. Linked. Not opened. |
| FR | `/writer/fr`. Linked. Not opened. |
| ES | `/es/writer`. Linked. Not opened. |
| IT | `/writer/it`. Linked. Not opened. |
| PT | `/writer/pt-pt`. Linked. Not opened. |
| 简 | `/writer/zh-hans`. Linked. Not opened. |
| 繁 | `/writer/zh-hant`. Linked. Not opened. |

## Header, phone (390)

The bar collapses to the wordmark and the Menu summary. Support, Buy, and Download leave the bar. The Menu summary opens the same drawer. Photographed in [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). The download control becomes "Download on the App Store" and points at the App Store. Linked. Not opened.

## Homepage body

URL stays `/writer` unless noted. Photographed in [home-light-default.png](screenshots/home-light-default.png).

| Control | Result |
|---|---|
| Download for Mac | Button. `onclick` calls `download(this, "writer", "writer-trial")`. Starts a file download. Not pressed. |
| Download for Windows | Same download function. Not pressed. |
| iPhone, iPad, Mac, Windows (under the download buttons) | `/writer/download` |
| Download on the App Store | `https://apps.apple.com/app/id775737172`. Off-site store. Linked. Not opened. |
| Play video | In-page player. Not pressed. A press starts media. |
| More (review quotes) | Button. Expands a quote in place. One was opened. Photographed in [home-light-quote.png](screenshots/home-light-quote.png). |
| Design Award Finalist | `/topics/apple-design-award-2025`. A blog post. Linked. Not opened. |
| iA Presenter / Learn More | `/presenter`. Other product. Linked. Not opened. |
| iA Notebook / Learn More | `/notebook`. Other product. Linked. Not opened. |
| iA Notebook / Buy | Opens the shipping dialog (`notebook-shipping`) on this page. The rows link to checkout stores. Not submitted. Dialog was opened and closed. One region is marked from the visitor's network, so the dialog screenshot is not committed. Store links were not followed. |

No homepage search. No account menu. No theme switch.

## Footer

Same destinations as the menu, plus:

| Control | Opens |
|---|---|
| Newsletter | `/newsletter`. A signup form. Linked. Not opened. Not submitted. |
| Mastodon, LinkedIn, YouTube, TikTok | Off-site social. Linked. Not opened. |
| Language | In-page language list. Same locale links as the menu. |

## Public Writer pages opened from the tree

Each loaded signed out.

| Path | Result |
|---|---|
| `/writer` | HTTP 200. Product home. |
| `/writer/pricing` | HTTP 200. One-time prices, education discount copy, FAQ. A newsletter form sits in the footer (email field, topic checkboxes, submit). Left empty. Not submitted. Mailto contact links were not followed. Photographed in [pricing-light-default.png](screenshots/pricing-light-default.png). |
| `/writer/download` | HTTP 200. Platform download cards. Download buttons were not pressed. App Store links were not followed. |
| `/writer/support` | HTTP 200. Support articles index. Article links were linked, not opened one by one. |
| `/downloads/writer` | HTTP 200. Writer extras. Download buttons were not pressed. |
| `/topics/category/writer` | HTTP 200. Writer blog category. Post links were linked, not opened. |

## Walls, stopped

No login, signup, or identity-provider button is on `/writer`. Buy stays on `/writer/pricing` and does not open a card form. The Notebook Buy control opens a shipping dialog whose store links are checkout. Those links were not followed. No email, password, phone, or code was typed. No form was submitted. No captcha was solved. Google, Apple, and any other identity provider were not clicked.
