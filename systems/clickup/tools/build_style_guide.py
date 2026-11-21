#!/usr/bin/env python3
"""ClickUp style-guide.html was written by hand for this public capture.

catalog.json was left alone, so make design-md does not own this package.
This builder checks the guide exists and exits.
"""

from pathlib import Path

ADAPTED_FOR = "clickup"

HERE = Path(__file__).resolve().parent.parent


def main() -> None:
    guide = HERE / "style-guide.html"
    if "ClickUp" not in guide.read_text():
        raise SystemExit("style-guide.html is not the ClickUp guide")
    print("clickup style-guide.html left as written")


if __name__ == "__main__":
    main()
