# Components

Public pages on hq.vevo.com, captured 2026-11-21, signed out, headless Chromium. Desktop viewport measured 1440x900 at 1x. Phone viewport measured 390x844 at 2x. The site tree is [site-tree.md](site-tree.md).

Crops are in [components/crops/](components/crops). Values below are the computed styles in [raw/components-computed.json](raw/components-computed.json). A colour that matches a token is named. Unread values stay Not captured.

## Button

Submit on the advertiser form. Default is black fill, white 18/25.2 label, height 46px, radius 999px. Hover inverts to off-white fill and near-black label.

| State | Crop | Notes |
|---|---|---|
| default | [button-default.png](components/crops/button-default.png) | `light.component.button.bg` #000000, text #ffffff |
| hover | [button-hover.png](components/crops/button-hover.png) | fill #fdfdfd, text #020202 |

Pressed, disabled, and loading were not shown. The form was not submitted, so no success or error toast appeared.

The About Us pill is a link styled as a control: white fill, black 16px label, radius 24px, height 46px. Crop: [text-link-default.png](components/crops/text-link-default.png). Hover inverts it: [text-link-hover.png](components/crops/text-link-hover.png).

## Icon button

The phone menu control is a 27x18 hamburger. Crop: [menu-button-default.png](components/crops/menu-button-default.png). Share controls on a press post are 19px. Crop: [share-button-default.png](components/crops/share-button-default.png). No separate icon set was extracted.

## Link

Header links are 14/21, white on the dark hero, #515151 on hover.

| State | Crop |
|---|---|
| default | [nav-link-default.png](components/crops/nav-link-default.png) |
| hover | [nav-link-hover.png](components/crops/nav-link-hover.png) |

The phone drawer current item is purple #9507ff. Crop: [drawer-link-default.png](components/crops/drawer-link-default.png). Privacy policy body links are underlined on the black policy page. Their colour was not read as its own token.

## Text field

Advertiser form. Height 41px, 1px border, radius 0, horizontal padding 16px, 15px text. The fill is transparent over the slate page.

| State | Crop | Border |
|---|---|---|
| default | [text-field-default.png](components/crops/text-field-default.png) | #ffffff |
| focus | [text-field-focus.png](components/crops/text-field-focus.png) | #979797 |
| blurred empty | [text-field-blurred-empty.png](components/crops/text-field-blurred-empty.png) | #a1002e, the same crimson as the stats band |

A filled state was measured and the crop was deleted, because the field held sample text.

## Text area

Height 104px, same border treatment as the field.

| State | Crop |
|---|---|
| default | [text-area-default.png](components/crops/text-area-default.png) |
| focus | [text-area-focus.png](components/crops/text-area-focus.png) |

## Select

Country dropdown, same 41px box and 1px white border. Crop: [select-default.png](components/crops/select-default.png). Open, hover, and disabled were not captured. The menu was not opened, so no option list was measured.

## Checkbox

13px box on the newsletter row. Crop: [checkbox-default.png](components/crops/checkbox-default.png). Checked, hover, focus, and disabled were not captured. The box was not toggled.

## Radio

13px circles on the artist feedback page. Crop: [radio-default.png](components/crops/radio-default.png). Selected was not captured. No radio was clicked.

## Switch

Not present.

## Tabs

Not present. Specs uses an accordion, not tabs.

## Menu

Phone drawer, 390x844, black, 22px labels, current item purple. Crop: [drawer-open.png](components/crops/drawer-open.png). Screenshot: [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

The press More actions control was clicked. The share row was already on the page. A separate menu panel was not measured.

## Tooltip

Not present on the public pages.

## Dialog

The homepage play control opens a Wix video lightbox on the same URL. Screenshot: [home-light-video.png](screenshots/home-light-video.png). The lightbox frame's own chrome was not measured apart from the page. Cookie consent is a banner, not captured as a dialog, because it was hidden and never clicked.

## Toast

Not present. No form was submitted.

## Card

News cards on the homepage are image tiles, about 404x319. Crop: [news-card-default.png](components/crops/news-card-default.png). Hover and selected were not captured.

## List row

Not present as an app list. Press recent posts are links in a column. Not measured as their own component.

## Table

Not present.

## Avatar

Not present. Artist photos are editorial images, not avatars.

## Badge

Not present.

## Accordion

Video Preroll on the specs page. Label 14/30, white. Expanding it stays on the same URL and reveals spec links.

| State | Crop |
|---|---|
| default | [accordion-default.png](components/crops/accordion-default.png) |
| expanded | [accordion-expanded.png](components/crops/accordion-expanded.png) |

## Gaps

| Item | Status |
|---|---|
| Pressed, disabled, loading | Not captured. No control showed them. |
| Switch, tabs, tooltip, toast, table, avatar, badge | Not present on the public site. |
| Select open menu | Not captured. The menu was not opened. |
| Checkbox checked, radio selected | Not captured. Neither control was toggled. |
| Focus ring | Not captured as a token. Keyboard focus on the skip link produced an empty box. The logo crop shows a blue ring from a script focus, not a measured focus token. |
| Motion | Not captured. Transitions on the measured controls read 0s. |
| Dark theme | Not present. No theme switch. |
| Artist page pink, feedback page lilac | Not captured as tokens. The pages show them. The computed background of those sections was not read. |
| Font family | Not captured. The computed family is a Wix hash. The guide uses Helvetica. |
| Signed-in app | Not captured. `https://www.vevo.com/login` returned 503 with an empty document. `/home-old` and `/label-partners` are password walls. Neither was filled. |
