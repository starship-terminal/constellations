"""Which shot holds a part's rest (default) reading, where more than one shot measured it. PRODUCT (adapt).

A part name such as `button-outline` covers every control of that look, and the first shot to measure it
is not always the one its hover, focus-visible and pressed shots were taken on: the model menu's Model
settings button is measured as `button-outline` before the gallery's Outline button that the state shots
use. build_tokens.py, build_components_md.py and crops.py read a part's default from the shot named here,
so a part's states compare one control with itself. Parts not listed take the first shot that measured them.
"""
DEFAULT_SHOT = {
    "button-accent": "design-buttons",
    "button-outline": "design-buttons",
    "button-ghost": "design-buttons",
    "button-danger": "design-buttons",
    "input": "settings-capy",
    "select": "settings-capy",
    "switch-off": "settings-capy",
    "switch-on": "settings-notifications",
    "row-button": "settings-capy",
    "settings-search": "settings-capy",
    "settings-nav": "settings-capy",
    "menu-item": "more-menu",
    "icon-button": "home",
    "tab": "home",
}


def skip(shot, part, state):
    """True when this shot's reading of the part must not be its default reading."""
    return state == "default" and part in DEFAULT_SHOT and shot != DEFAULT_SHOT[part]
