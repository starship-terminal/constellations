"""Which shot holds a part's rest (default) reading, where more than one shot measured it. PRODUCT (adapt).

A part name such as `menu-row` covers every control of that look, and the first shot to measure it is
not always the one its hover, focus-visible and pressed shots were taken on: the permissions menu
measured a menu row before the profile menu, whose rows the hover shot uses. build_tokens.py,
build_components_md.py and crops.py read a part's default from the shot named here, so a part's states
compare one control with itself. Parts not listed take the first shot that measured them.
"""
DEFAULT_SHOT = {
    "menu-row": "profile-menu",
    "menu": "profile-menu",
    "dialog": "remove-project-dialog",
    "button-ghost": "remove-project-dialog",
    "select": "settings-general",
    "switch-off": "settings-general",
    "switch-on": "settings-general",
    "settings-nav": "settings-general",
    "button-secondary": "settings-general",
    "composer": "home-default",
    "icon-button": "home-default",
}


def skip(shot, part, state):
    """True when this shot's reading of the part must not be its default reading."""
    return state == "default" and part in DEFAULT_SHOT and shot != DEFAULT_SHOT[part]
