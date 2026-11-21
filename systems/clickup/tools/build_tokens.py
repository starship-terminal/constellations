#!/usr/bin/env python3
"""ClickUp tokens were written from computed styles. This builder does not rewrite them.

The kit example stops unless ADAPTED_FOR is set. This copy is adapted so a
rebuild does not invent Claude values. It checks tokens.json and exits.
"""

import json
from pathlib import Path

ADAPTED_FOR = "clickup"

HERE = Path(__file__).resolve().parent.parent


def main() -> None:
    data = json.loads((HERE / "tokens.json").read_text())
    if "light" not in data or "core" not in data:
        raise SystemExit("tokens.json is missing core or light")
    print("clickup tokens.json left as measured")


if __name__ == "__main__":
    main()
