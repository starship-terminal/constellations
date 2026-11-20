# Scape patterns

Public pages only. Captured 2026-11-21. The site tree of what each control opens is [site-tree.md](site-tree.md).

## App shell

A promo strip, then a 72px header (logo, Our locations mega menu, text links, FIND A ROOM pill, favourites and booking circles). The home header is translucent black over the hero and cream type. A solid header is declared (`--header-solid-header-bg`) for pages that scroll under it. The footer is cream type on a dark ground, with four link columns.

Shown in [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/home-light-mobile-default.png](screenshots/home-light-mobile-default.png).

## Search and filtering

Find a room is the catalogue. Stay-type tabs sit above a row of filter chips (sort, location, booking period, price, room type, room size). Opening location keeps the visitor on `/rooms/`. See [screenshots/rooms-light-default.png](screenshots/rooms-light-default.png) and [screenshots/rooms-light-filter-location.png](screenshots/rooms-light-filter-location.png).

## Empty

Favourites with nothing saved says the list is empty and links back to Find a room. See [screenshots/favourites-light-default.png](screenshots/favourites-light-default.png).

## Loading

`/booking/` rendered a public shell whose body stayed on "Loading...". No checkout was started. See [screenshots/booking-light-default.png](screenshots/booking-light-default.png).

## Error

`/login/` is a 404. See [screenshots/notfound-light-default.png](screenshots/notfound-light-default.png).

## Form

Contact offers phone, an enquiry dialog, a call scheduler and WhatsApp. The enquiry dialog was opened and closed. Nothing was typed or submitted. See [screenshots/contact-light-enquiry-dialog.png](screenshots/contact-light-enquiry-dialog.png).

## List

Room cards are the list. A representative room page is [screenshots/room-light-default.png](screenshots/room-light-default.png). Building pages add a local nav (building, rooms, neighbourhood, social). See [screenshots/shoreditch-light-default.png](screenshots/shoreditch-light-default.png).

## Not present

Destructive confirmation, toast feedback after an action, and onboarding are not on the public marketing surface. Account and booking submit were not entered.
