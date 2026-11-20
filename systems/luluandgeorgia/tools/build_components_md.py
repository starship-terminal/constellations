#!/usr/bin/env python3
"""Write components.md from the measured public components."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]

def hexc(v):
    """rgb(26, 23, 19) -> #1a1713"""
    import re
    m = re.fullmatch(r"rgba?\((\d+), (\d+), (\d+)(?:, [\d.]+)?\)", v)
    if not m:
        raise SystemExit(f"not a colour: {v!r}")
    return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())


def st(key, state="default"):
    """One measured state. A missing reading fails the build, so the prose cannot outlive raw/."""
    v = (C.get(key) or {}).get("states", {}).get(state)
    if not v or "error" in v:
        raise SystemExit(f"{key} {state} missing from raw/components-computed.json")
    return v


def missing(key):
    return all("error" in v for v in (C.get(key) or {}).get("states", {"default": {"error": 1}}).values())


F = J["foundations"]
atc, acct, cart, nav, search, qty = st("atc"), st("icon-account"), st("icon-cart"), st("nav-link"), st("search"), st("qty")
same_fill = all(st("atc", s)["backgroundColor"] == atc["backgroundColor"] for s in ("hover", "pressed"))
if not missing("wishlist"):
    raise SystemExit("wishlist now has a reading: write its row from it")

# The inventory prose was written by hand at capture time; every measured number in it is read
# from raw/components-computed.json below.
text = f"""# Components

Public signed-out components measured on luluandgeorgia.com on 2026-11-18. Crops are in [components/crops/](components/crops). Colours are computed styles. The site paints square corners and one ink.

| Component | Status | Evidence |
|---|---|---|
| Button | captured | Add to cart is {atc['rect']['h']}px, fill {hexc(atc['backgroundColor'])}, label {hexc(atc['color'])}, weight {atc['fontWeight']}. [default](components/crops/atc-default.png), [hover](components/crops/atc-hover.png), [focus](components/crops/atc-focus.png), [pressed](components/crops/atc-pressed.png). {"Hover and pressed did not change the fill." if same_fill else "Hover or pressed changed the fill."} The focus crop is a script focus with the pointer still over the button, not a keyboard focus (see States). |
| Icon button | captured | Account {acct['rect']['w']}px and bag {cart['rect']['w']}px in the header. [account](components/crops/icon-account-default.png), [bag](components/crops/icon-cart-default.png). The wishlist button beside add to cart was not found by the measure pass, so it has no reading. |
| Link | captured | Category links are {nav['fontSize']} uppercase, {nav['letterSpacing']} tracking, ink {hexc(nav['color'])}. Sale is {hexc(F['sale']['color'])}. [furniture](components/crops/nav-link-default.png). Account drawer link in [account-link](components/crops/account-link-default.png). |
| Text field | captured | Header search is {search['rect']['h']}px, fill {hexc(search['backgroundColor'])}, placeholder {hexc(search['color'])}, radius {search['borderRadius'].replace('0px', '0')}. [default](components/crops/search-default.png), [focus](components/crops/search-focus.png), [filled](components/crops/search-filled.png). Quantity on the product page is {qty['rect']['w']}x{qty['rect']['h']}. [qty](components/crops/qty-default.png). |
| Text area | not present | No textarea on the signed-out pages. |
| Select | not captured | A variant select exists in the DOM (`select.product-variants`) and was not visible on the Sachs dining table page, which paints a single price. |
| Checkbox | observed | The Shop sign-in page paints "Email me with news and offers" checked. That page is shopify.com, not the storefront. It was not measured as a store token. See [login-light-default](screenshots/login-light-default.png). |
| Radio | not present | No radio on the signed-out storefront pages. |
| Switch | not present | No switch on the signed-out pages. |
| Tabs | not present | Product details are a disclosure (Shipping & Returns), not tabs. |
| Menu | captured | The account drawer and the filter drawer. [account](screenshots/home-light-account.png), [filter](screenshots/collection-light-filter.png). Category hover did not open a mega-menu in the nav shot. |
| Tooltip | not present | No tooltip was painted. |
| Dialog | captured | Filter drawer and account drawer are side panels, not centred dialogs. [filter](screenshots/collection-light-filter.png). |
| Toast | not present | No toast was painted. |
| Card | captured | Collection product cards. [card](components/crops/product-card-default.png). Search suggestions in [home-light-search](screenshots/home-light-search.png). |
| List row | captured | Filter groups are rows with a plus. [filter](screenshots/collection-light-filter.png). |
| Table | not present | No data table on the public pages. |
| Avatar | not present | No avatar on the signed-out storefront. |
| Badge | observed | Search suggestions paint Exclusive and New chips. The badge selector matched the whole product card ({st('badge')['rect']['w']}x{st('badge')['rect']['h']}), so `badge` in raw/ and its crop are the card, not the chip. Recapture needed. See [home-light-search](screenshots/home-light-search.png). |
| Hero button | not captured | "Shop bestsellers" is visible in the home screenshot and was not a stable locator during measurement (the hero is a carousel). See [home-light-default](screenshots/home-light-default.png). |

## States

Hover was a real pointer hover and pressed was forced (`CSS.forcePseudoState`) on add to cart. The computed fill stayed {hexc(atc['backgroundColor'])}. Focus was a script `focus()` taken with the pointer still over the button, so `:focus-visible` was not produced: the reading cannot say whether a keyboard focus draws a ring. Recapture needed (`tools/capture/public/measure.mjs` now takes a keyboard focus from rest). Disabled was not painted. Loading was not painted. A validation error was not produced, because the login form was not submitted and add to cart was not clicked.
"""
import re
dead = sorted({t for t in re.findall(r"\]\(((?:screenshots|components|raw)/[^)#\s]+)\)", text) if not (ROOT / t).exists()})
if dead:
    raise SystemExit("components.md links files that do not exist: " + ", ".join(dead))
(ROOT / "components.md").write_text(text)
print("components.md")
