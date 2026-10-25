"""Which shot holds a part's rest (default) reading, where more than one shot measured it. PRODUCT (adapt).

A part name such as `menu-row` covers every control of that look, and the first shot to measure it is
not always the one its hover, focus-visible and pressed shots were taken on: the page row menu measured
a menu row before the page actions menu, whose rows the hover shot uses. build_tokens.py,
build_components_md.py and crops.py read a part's default from the shot named here, so a part's states
compare one control with itself. Parts not listed take the first shot that measured them.
"""
DEFAULT_SHOT = {
    "menu-row": "page-actions-menu",
    "menu": "page-actions-menu",
    "dialog": "delete-property-dialog",
    "select": "settings-preferences-parts",
    "settings-nav": "settings-preferences-parts",
    "page-row": "page-default",
    "page-row-selected": "page-default",
    "topbar-icon-button": "page-default",
    "sidebar-search": "page-default",
    "nav-tab": "page-default",
    "nav-tab-selected": "page-default",
    "tab": "tabbar-default",
    "paragraph": "page-default",
    "callout": "page-default",
    "table-cell": "database-table",
    "table-row": "database-table",
    "table-header-cell": "database-table",
    "popover": "share-menu",
}


def skip(shot, part, state):
    """True when this shot's reading of the part must not be its default reading."""
    return state == "default" and part in DEFAULT_SHOT and shot != DEFAULT_SHOT[part]
