"""Which shot holds a part's rest (default) reading, where more than one shot measured it. PRODUCT (adapt).

A part name such as `menu-row` covers every control of that look, and the first shot to measure it is
not always the one its hover, focus-visible and pressed shots were taken on: several menus measured a row
before the view menu, whose rows the hover shot uses. build_tokens.py, build_components_md.py and crops.py
read a part's default from the shot named here, so a part's states compare one control with itself.
Parts not listed take the first shot that measured them.
"""
DEFAULT_SHOT = {
    "menu-row": "view-menu",
    "menu": "view-menu",
    "panel": "event-popover",
    "panel-header": "event-popover",
    "panel-title": "event-popover",
    "panel-icon-button": "event-popover",
    "panel-button": "event-popover",
    "panel-section": "event-popover",
    "dialog": "settings-general-detail",
    "select": "settings-general-detail",
    "switch-on": "settings-general-detail",
    "settings-nav": "settings-general-detail",
    "link": "settings-general-detail",
    "kbd": "settings-general-detail",
    "event-chip": "week-default",
    "day-header": "week-default",
    "today-button": "week-default",
    "command-menu": "command-menu",
    "command-input": "command-menu",
    "command-row": "command-menu",
    "search-field": "shortcuts",
    "button-secondary": "scheduling",
    "scheduling-row": "week-default",
}


def skip(shot, part, state):
    """True when this shot's reading of the part must not be its default reading."""
    return state == "default" and part in DEFAULT_SHOT and shot != DEFAULT_SHOT[part]
