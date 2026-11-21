#!/usr/bin/env python3
"""ClickUp components.md was written by hand for this public capture.

Crops were not cut. This builder checks the inventory exists and exits.
"""

from pathlib import Path

ADAPTED_FOR = "clickup"

HERE = Path(__file__).resolve().parent.parent


def main() -> None:
    text = (HERE / "components.md").read_text()
    if "Login field" not in text:
        raise SystemExit("components.md is missing the login field row")
    print("clickup components.md left as written")


if __name__ == "__main__":
    main()
