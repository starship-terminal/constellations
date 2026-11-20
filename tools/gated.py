#!/usr/bin/env python3
"""Write docs/GATED.md: the roll-up of surfaces that signed-out captures
never reached.

Reads catalog.json. For every systems/ package, collects the `access`
boundary text and the `capture.gaps` lines that describe a gated surface
(auth, account, checkout, submission, membership…). Packages whose gaps
name no gate are listed in a trailing "fully public" line only.

Usage:
    python3 tools/gated.py            # write docs/GATED.md
    python3 tools/gated.py --check    # exit 1 if the file is stale
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import catalog  # noqa: E402

OUT = ROOT / "docs" / "GATED.md"

GATE = re.compile(
    r"(sign[- ]?in|signed in|log[- ]?in|login|auth|account|register|"
    r"checkout|purchas|payment|subscri|member|dashboard|workspace|portal|"
    r"onboard|submit|booking|order|pay(?!load)|credential|oauth|invite|"
    r"sso|mfa|2fa|publish|composer|billing portal|create-account)",
    re.IGNORECASE,
)

HEADER = """# Gated surfaces

What the library has NOT captured: every surface that sits behind a sign-in,
an account, a checkout or a submission in the signed-out captures. Generated
by `python3 tools/gated.py` from `capture.gaps` and `access` in
[catalog.json](../catalog.json); do not edit by hand.

Each entry is the catalog's own words. A package appearing here is not
incomplete — the capture was scoped to public surfaces on purpose — it is
the queue for any future authenticated pass, which needs the owner's
account and a fresh capture contract (docs/CAPTURE.md, docs/RIGHTS.md).

"""


def gate_lines(entry):
    lines = []
    for gap in entry.get("capture", {}).get("gaps", []):
        if GATE.search(gap):
            lines.append(gap.strip())
    return lines


def gated_matches_base(systems, current: str) -> bool:
    """True when GitHub is checking a pull request and the committed roll-up is
    the exact render of the packages it names, leaving out only packages this
    pull request adds or main gained after the branch started.

    Rendering the named packages from the merge's own catalog, never trusting
    the branch's copy, means a hand edit, a stale row, a wrong count or a
    removed package still listed fails (tools/catalog.py lagging_subset)."""
    head_rows = {s.get("slug"): s for s in systems}
    kept = catalog.lagging_subset(slugs_in_gated(current), head_rows, ROOT)
    return kept is not None and current == render(kept)


def slugs_in_gated(text: str) -> set[str]:
    """Slugs the committed roll-up rendered a section for."""
    linked = set(re.findall(r"\]\(\.\./systems/([^)/\s]+)\)", text))
    marker = "## No gated surface recorded"
    open_slugs = set()
    if marker in text:
        open_slugs = set(re.findall(r"`([^`]+)`", text.split(marker, 1)[1]))
    return linked | open_slugs


def render(systems):
    gated, access_only, open_all = [], [], []
    for e in systems:
        lines = gate_lines(e)
        if lines:
            gated.append((e, lines))
        elif GATE.search(e.get("access", "")):
            access_only.append((e, lines))
        else:
            open_all.append((e, lines))
    out = [HEADER]
    out.append(
        f"_{len(gated)} of {len(systems)} packages name gated surfaces in their "
        f"gaps; {len(access_only)} more mark a gate in their access text; "
        f"{len(open_all)} report none._\n"
    )
    for e, lines in gated:
        slug = e["slug"]
        out.append(f"\n## [{e.get('name', slug)}](../systems/{slug}) — `{slug}`\n")
        access = e.get("access", "").strip()
        if access:
            out.append(f"Access: {access}\n")
        for line in lines:
            out.append(f"- {line}\n")
    if access_only:
        out.append("\n## Gate noted in access text only\n")
        for e, _ in access_only:
            slug = e["slug"]
            out.append(
                f"\n### [{e.get('name', slug)}](../systems/{slug}) — `{slug}`\n"
                f"{e.get('access', '').strip()}\n"
            )
    if open_all:
        names = ", ".join(f"`{e['slug']}`" for e, _ in open_all)
        out.append(f"\n## No gated surface recorded\n\n{names}\n")
    return "".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Write docs/GATED.md, the roll-up of surfaces signed-out captures never reached."
    )
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if docs/GATED.md is stale")
    args = ap.parse_args(argv)

    catalog = json.loads((ROOT / "catalog.json").read_text())
    systems = catalog["systems"]
    text = render(systems)
    if args.check:
        current = OUT.read_text() if OUT.exists() else ""
        if current != text and not gated_matches_base(systems, current):
            print("docs/GATED.md is stale — run python3 tools/gated.py")
            return 1
        print("gated ok")
        return 0
    OUT.write_text(text)
    print(f"wrote {OUT.relative_to(ROOT)} ({len(systems)} packages)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
