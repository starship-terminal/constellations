# MoMA components

Public signed-out surfaces, measured 2026-11-19 in headed Chrome. Crops are 256-colour PNGs. Read colours from [tokens.json](tokens.json).

## Button

**Plan your visit** is a black fill, white MoMA Sans, weight 900, square corners. Seen on [home-light-default](screenshots/home-light-default.png).

**Join or renew** is the same black fill on the membership cards. [join-default](components/crops/join-default.png). Hover did not change the computed background (`rgba(0,0,0,0)` on the link itself; the black fill is the parent's). [join-hover](components/crops/join-hover.png).

**Gift it** is a white control beside Join. [gift-default](components/crops/gift-default.png).

**Continue** on `/auth/login` is a black rectangle with white text. The login host returned a Cloudflare challenge on the second launch, so hover and focus were not measured. [login-light-default](screenshots/login-light-default.png).

## Link

Nav items are black, weight 900, about 18px, with an underline on the current section. Visit is underlined on [visit-light-default](screenshots/visit-light-default.png). Computed Visit button: 13.333px, weight 400, padding 8px, on the control that wraps the label. [nav-visit-default](components/crops/nav-visit-default.png).

## Tickets and Donate

Tickets carries `$color/background:brand:10`, resolved `#00b7f2`, black text, square corners. Donate carries `$color/background:gray:eee`, `#eeeeee`. Both sit in the header. [donate-default](components/crops/donate-default.png). Tickets is in the header of [home-light-default](screenshots/home-light-default.png). The crop pass missed the Tickets node because the label sits in a child.

## Text field

Search opens as a 40px field, placeholder "Search moma.org", colour `rgba(0, 0, 0, 0.54)`, 1110 by 48px, no border on the input (a rule sits under the row). [home-light-search](screenshots/home-light-search.png).

The login email field is an underline: computed padding `0px 2px 4px`, font 18px, weight 700, no border on the input itself. [login-light-default](screenshots/login-light-default.png). The field was focused and not submitted.

## Card

Exhibition cards are square-cornered links, no shadow, image above a 30px title and a `#767676` date. [exhibitions-light-default](screenshots/exhibitions-light-default.png).

Membership tier cards use the membership palette. Access fill measured `rgb(213, 250, 234)`, which is `--color--membership--6` `#d5faea`. Explore fill measured `rgb(246, 193, 230)`, `--color--membership--15` `#f6c1e6`. Radius 0. [membership-card-access](components/crops/membership-card-access.png) and [membership-light-default](screenshots/membership-light-default.png).

## Menu

Membership opens a small panel: Become a member, Log in. [home-light-membership-menu](screenshots/home-light-membership-menu.png).

## Wordmark

The header mark is an inline SVG, 209 by 53 in the file, about 225 by 69 on the page. [wordmark-default](components/crops/wordmark-default.png).

## Gaps

| Component | Status |
|---|---|
| Text area | Not present on the captured public pages |
| Select | Not captured. Visit page has location disclosure controls. Not opened as a select. |
| Checkbox, radio, switch | Not present on the captured pages |
| Tabs | Not present |
| Tooltip | Not present |
| Dialog | Cookie notice is a bottom bar, not a dialog. [home-light-cookie](screenshots/home-light-cookie.png). Not accepted. |
| Toast | Not present |
| Table | Not present |
| Avatar, badge | Not present on these surfaces |
| Disabled, loading, error of a form | Not captured. Empty Continue was not reached: `/auth/login` challenged on the second launch. |
| Focus ring | `--focus-thickness` 0.2rem and `--focus-radius` 0.4rem are declared. A live focus-visible ring was not cropped. |
