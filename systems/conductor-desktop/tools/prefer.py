"""Which shot holds a part's rest (default) reading, where more than one shot measured it. PRODUCT (adapt).

A part name such as `button-outline` covers every control of that look, and the first shot to measure it
is not always the one its hover, focus-visible and pressed shots were taken on. build_tokens.py,
build_components_md.py and crops.py read a part's default from the shot named here, so a part's states
compare one control with itself. Parts not listed take the first shot that measured them.
"""
DEFAULT_SHOT = {
    "button-outline": "remove-confirm",
    "select": "settings-general",
    "settings-search": "settings-general",
    "settings-nav-item": "settings-general",
    "switch-on": "settings-general",
    "menu": "workspace-context-menu",
    "menu-item": "workspace-context-menu",
    "tree-row": "workspace",
    "panel-tab": "workspace",
    "user-message": "conversation",
    "tool-call": "conversation-top",
    "tool-arg": "conversation-top",
    "assistant-text": "conversation",
    "file-link": "conversation",
    "button-primary": "repo-dialog",
    "dialog": "remove-confirm",
    "dialog-title": "remove-confirm",
    "composer": "workspace",
    "send-button": "workspace",
}


# Readings that must not be used at all.
# The avatar selector matched the header's Finder icon, not the photo.
NOT_THIS_STATE = {("settings-account", "avatar")}


def skip(shot, part, state):
    """True when this shot's reading of the part must not be used for `state`."""
    if (shot, part) in NOT_THIS_STATE:
        return True
    return state == "default" and part in DEFAULT_SHOT and shot != DEFAULT_SHOT[part]
