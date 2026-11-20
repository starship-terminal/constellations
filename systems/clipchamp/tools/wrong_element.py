"""The three clipchamp readings taken from the wrong element (README, What is not here).

Each correction applies only while the raw reading still shows the wrong element it was
taken from, so a recapture that measures the right element keeps its own description.
"""


def _default(comp):
    return (comp.get("states") or {}).get("default") or {}


def _classes(comp):
    return _default(comp).get("classes") or ""


def _tooltip_closed(comp):
    return any("fui-Tooltip__content" in (p.get("node") or "") and p.get("size") == "0.0x0.0"
               for p in _default(comp).get("paint") or [])


# key -> (still the wrong reading?, title, description)
CORRECTIONS = {
    "content-block-dark": (
        lambda c: "_DarkBackground" in _classes(c) and "_ContentBlockDark" not in _classes(c),
        "Dark band heading",
        "A heading's `_DarkBackground` text variant inside a dark band, read instead of the band: "
        "the element paints transparent, so the band's fill is only the pixel sample `core.sampled.surfaceDark` "
        "(README, What is not here)."),
    "plan-head": (
        lambda c: "_HeadIcon" in _classes(c) and "_HeaderCell" not in _classes(c),
        "Plan header icon",
        "The 52 x 24 icon (`_HeadIcon`) inside a plan header cell, read instead of the cell with the plan "
        "name and price (README, What is not here); the header row's fill is in the plan table's child layers."),
    "feature-tooltip": (
        _tooltip_closed,
        "Tooltip cell",
        "A plan value cell (`_CellTooltip`) read with its tooltip closed: the Fluent tooltip node inside it "
        "measured 0 x 0, so this capture has no open tooltip (README, What is not here)."),
}


def corrected(components):
    """Return components with the title and description of each still-wrong reading replaced."""
    out = dict(components)
    for key, (still_wrong, title, desc) in CORRECTIONS.items():
        if key in out and still_wrong(out[key]):
            out[key] = dict(out[key], title=title, desc=desc)
    return out
