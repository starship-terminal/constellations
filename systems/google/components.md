# Components

Public Google Search, signed out, 2026-11-22. Crops are 256-colour. Read colours from [tokens.json](tokens.json).

## Button

Sign in is a blue pill, 40px tall, radius 100px, white Google Sans Text at 14px weight 500. Fill `#0b57d0`.

Google Search and I'm Feeling Lucky are quiet buttons, 36px tall, radius 8px, face `#f8f9fa`, border `#dadce0`, label `#202124`, Arial 14px. Horizontal padding 16px.

The accounts Next button is a different blue, `#1a73e8`, radius 4px, 36px tall. It was not clicked.

Hover, pressed, disabled and loading were not measured, except the Search button shadow read while the pointer was over it.

Crops: [components/crops/signin.png](components/crops/signin.png), [components/crops/buttons.png](components/crops/buttons.png).

## Text field

Homepage search field: white, 52px tall, 584px wide at 1440, radius 26px, 1px border `#dadce0`, shadow `rgba(31, 31, 31, 0.08) 0px 3px 10px`. Input text is 16px on a 22px line. Focus drops the bottom radius and deepens the shadow, and opens trending searches. No query was typed.

The sign-in identifier is 56px tall and was left empty.

Crop: [components/crops/field.png](components/crops/field.png).

## Link

Header links are 14px Arial, `#16171a`, no underline. The doodle promo is 13px `#1a0dab`. Footer links sit on the `#ececed` band.

## Menu

Settings opens a white menu: Search settings, Advanced search, Your data in Search, Search history, Search help, Send feedback, Dark theme: Off.

Google apps opens a card of product icons with no account. "Sign in to arrange apps."

Phone Main menu is a sheet of settings rows, not the apps grid.

Crop: [components/crops/settings-menu.png](components/crops/settings-menu.png), [components/crops/apps.png](components/crops/apps.png).

## Dialog

Search by voice covers the page with "Waiting..." and a close control. Closed without speaking.

## List row

Search settings uses rounded rows (Search customisation, SafeSearch). The phone menu uses the same row shape. Advanced search uses labelled empty fields and native selects. Nothing was submitted.

## Gaps

Icon button states, checkbox, radio, switch, tabs, tooltip, toast, table, avatar and badge were not isolated. The phone homepage has ALL and IMAGES tabs. Dark theme was not switched. No error, loading or disabled control was held.
