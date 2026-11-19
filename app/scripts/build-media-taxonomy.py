#!/usr/bin/env python3
"""Materialize local media classifications from canonical package metadata.

Run `python3 app/scripts/build-media-taxonomy.py` from any directory. No generated
web/data files, image reads, network calls or third-party Python packages needed.
`--check` compares against the committed seed without writing it. The application
imports this seed only in migration v5; rebuilding it never overwrites app edits.

These are conservative local classifications based on explicit capture names,
not Refero-assigned classifications or a visual review. Names that give no signal
stay unassigned. Flows require verified ordered evidence and are never inferred.
Font evidence is inherited from the package's recorded primary token families;
this does not assert that every pixel in each capture uses that family. Generic
families, fallback stack entries, aliases and unmatched custom names are skipped.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "app/src/data/media-taxonomy.json"
spec = importlib.util.spec_from_file_location("capture_catalog", ROOT / "tools/catalog.py")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)

# Each expression matches complete hyphen/underscore-delimited filename tokens,
# never package names, package descriptions, or arbitrary path substrings.
# Explicit page/screen types apply only to full screenshots, not isolated crops.
PAGE_RULES = [
    ("page-login", r"(?:log-?in|sign-?in)", "Log In"),
    ("page-signup", r"(?:sign-?up|register|registration)", "Sign Up"),
    ("page-reset-password", r"(?:reset-password|password-reset|forgot-password)", "Reset Password"),
    ("page-settings", r"settings", "Settings"),
    ("page-profile", r"(?:profile|account)", "Profile & Account"),
    ("page-dashboard", r"dashboard", "Dashboard"),
    ("page-catalog", r"catalog", "Catalog Page"),
    ("page-checkout", r"checkout", "Checkout"),
    ("page-cart", r"(?:cart|bag)", "Carts & Bags"),
    ("page-order-history", r"order-history", "Order History"),
    ("page-paywall", r"paywall", "Paywall & Subscription"),
    ("page-delete-account", r"(?:delete-account|account-delete)", "Delete Account"),
    ("page-cancel-subscription", r"(?:cancel-subscription|subscription-cancel)", "Cancel Subscription"),
    ("page-privacy", r"privacy-policy", "Privacy Policy"),
    ("page-terms", r"(?:terms-and-conditions|terms-conditions)", "Terms & Conditions"),
    ("page-about", r"about", "About"),
    ("page-contacts", r"contacts?", "Contacts"),
    ("page-support", r"(?:support|help)", "Support & Help"),
    ("page-home", r"home", "Home Page"),
]
UI_RULES = [
    ("ui-button", r"buttons?", "Button"),
    ("ui-checkbox-radio", r"(?:checkbox(?:es)?|radio)", "Checkbox & Radio"),
    ("ui-toggle", r"(?:switch(?:es)?|toggles?)", "Switch & Toggle"),
    ("ui-text-field", r"(?:text-?field|text-?input)", "Text Field"),
    ("ui-search-field", r"(?:search-field|search-input|searchbox|search-focused|search-typed)", "Search Field"),
    ("ui-slider", r"slider", "Slider"),
    ("ui-tabs", r"tabs?", "Tabs"),
    ("ui-sidebar", r"(?:sidebar|drawer)", "Sidebar & Drawer"),
    ("ui-toolbar", r"toolbar", "Toolbar"),
    ("ui-navbar", r"(?:navbar|navigation-bar)", "Navigation Bar"),
    ("ui-footer", r"footer", "Footer"),
    ("ui-dialog", r"(?:dialog|modal)", "Dialog & Modal Window"),
    ("ui-tooltip", r"(?:tooltip|tooltips)", "Tooltip"),
    ("ui-popover", r"popover", "Popover"),
    ("ui-dropdown", r"dropdown", "Dropdown"),
    ("ui-menu", r"(?:dropdown-menu|context-menu|account-menu|user-menu|model-menu|project-menu)", "Dropdown Menu"),
    ("ui-toast", r"(?:toast|toasts|notification-toast)", "Notifications & Toast"),
    ("ui-avatar", r"avatars?", "Avatar"),
    ("ui-badge", r"badges?", "Badge"),
    ("ui-chips", r"(?:chips?|pills?)", "Tags & Chips"),
    ("ui-cards", r"(?:cards?|tiles?)", "Cards & Tiles"),
    ("ui-list", r"(?:list|rows)", "List"),
    ("ui-table", r"tables?", "Table"),
    ("ui-tree", r"(?:tree|treeview|tree-view)", "Tree View"),
    ("ui-accordion", r"(?:accordion|collapse|collapsible)", "Accordion & Collapse"),
    ("ui-carousel", r"carousel", "Carousel"),
    ("ui-breadcrumb", r"breadcrumbs?", "Breadcrumb"),
    ("ui-skeleton", r"skeleton", "Skeleton"),
    ("ui-progress", r"progress-bar", "Progress Bar"),
    ("ui-pagination", r"(?:pagination|page-control)", "Page Control & Pagination"),
    ("ui-stepper", r"stepper", "Stepper"),
    ("ui-code", r"(?:code-snippet|code-block)", "Code Snippet"),
    ("ui-color-picker", r"colou?r-picker", "Color Picker"),
    ("ui-date-picker", r"(?:date-picker|time-picker|datetime-picker)", "Date & Time Picker"),
    # "source-map" (a build artefact) and "address-map" (an IP list) show no map.
    ("ui-map", r"(?<!source-)(?<!address-)map", "Map"),
    ("ui-photo", r"photo", "Photo"),
    ("ui-image", r"product-image", "Product Image"),
    ("ui-thumbnail", r"thumbnail", "Thumbnail"),
    ("ui-illustration", r"illustration", "Illustration"),
    ("ui-icon", r"icons?", "Icon"),
    ("ui-bottom-sheet", r"bottom-sheet", "Bottom Sheet"),
    ("ui-action-sheet", r"action-sheet", "Action Sheet"),
    ("ui-side-sheet", r"side-sheet", "Side Sheet"),
    ("ui-keyboard", r"keyboard", "Onscreen Keyboard"),
    ("ui-tabbar", r"tabbar", "Tabbar"),
]
UX_RULES = [
    ("ux-empty-state", r"empty-state", "Empty State"),
    ("ux-error", r"error", "Error"),
    ("ux-loading", r"(?:loading|connecting)", "Loading & Connecting"),
    ("ux-confirmation", r"(?:confirm|confirmation)", "Confirmation"),
    ("ux-success", r"success", "Success"),
    ("ux-permission", r"permission", "Permission"),
    ("ux-search", r"(?:search|searching)", "Searching"),
    ("ux-filter-sort", r"(?:filters?|sorting|sort)", "Filter & Sorting"),
    ("ux-calendar", r"calendar", "Calendar"),
    # A bare "message" token on a form capture is the contact/sales textarea,
    # not a chat surface: field-message, contact-message, c-message,
    # cf7-message, sales-message and message-field stay out of Chat & Messages.
    ("ux-chat", r"(?:chat|(?<!contact-)(?<!cf7-)(?<!field-)(?<!sales-)(?<!form-)(?<!c-)messages?(?!-field))", "Chat & Messages"),
    ("ux-comments", r"comments?", "Comments"),
    ("ux-share", r"share", "Share"),
    ("ux-user-menu", r"(?:user-menu|account-menu)", "User Menu"),
    ("ux-billing", r"(?:billing|subscription-plans|pricing-plans)", "Billing & Plans"),
    ("ux-payments", r"payment-method", "Payment Method"),
    ("ux-playlist", r"playlist", "Playlist"),
    ("ux-bookmark", r"(?:bookmarks?|wishlist|wish-list)", "Wish List & Bookmark"),
    ("ux-leaderboard", r"leaderboard", "Leaderboard"),
    ("ux-achievement", r"(?:achievements?|awards?)", "Achievements & Awards"),
    ("ux-templates", r"templates?", "Templates"),
    ("ux-upload-download", r"(?:uploads?|downloads?)", "Upload & Download"),
    ("ux-feedback", r"(?:feedback|survey)", "Feedback & Survey"),
    ("ux-faq", r"faq", "FAQ"),
    ("ux-archive", r"(?:trash|archive)", "Trash & Archive"),
    ("ux-notification-feed", r"(?:activity-feed|notification-feed)", "Activity & Notification Feed"),
    ("ux-video-player", r"video-player", "Video Player"),
    ("ux-audio-player", r"audio-player", "Audio Player"),
    ("ux-timer", r"(?:timer|clock)", "Timer & Clock"),
    ("ux-history", r"(?:timeline|history)", "Timeline & History"),
]


def term_id(group: str, label: str) -> str:
    """Mirror taxonomyTermId in app/src/contracts/taxonomy.ts exactly."""
    value = unicodedata.normalize("NFKC", label).lower()
    slug = re.sub("-+", "-", "".join(c if c.isalnum() else "-" for c in value)).strip("-")
    # A label with no letters or digits (say "&" or an emoji) would otherwise
    # give an empty, colliding ID; the app falls back to its code points.
    fallback = "-".join(format(ord(c), "x") for c in value)
    return f"{group}:{slug or f'u-{fallback}'}"


def build() -> dict:
    snapshot = json.loads((ROOT / "app/src/data/refero-catalog-taxonomy.json").read_text(encoding="utf-8"))
    terms = {g["id"]: {t["label"]: term_id(g["id"], t["label"]) for t in g["terms"]} for g in snapshot["groups"]}
    rules = {}
    for scope, definitions in [("page", PAGE_RULES), ("ui", UI_RULES), ("ux", UX_RULES)]:
        for rule_id, expression, label in definitions:
            rules[rule_id] = {
                "pattern": expression,
                "label": label,
                "reason": f"Capture filename explicitly names {label.lower()}; local classification from recorded capture metadata.",
            }
    rules["font-primary"] = {
        "reason": "Exact primary family recorded by this package's preview font token. Inherited package typography evidence, not a claim about every rendered capture; fallback stack entries and inferred aliases are excluded.",
    }
    assignments = []
    packages = []
    for system in catalog.load_catalog()["systems"]:
        prefix = "ios" if system["platform"] == "mobile" else "web"
        page_group = f"{prefix}-{'screen-types' if prefix == 'ios' else 'page-types'}"
        fonts = [f for f in catalog.fonts(system) if f["family"] in terms["web-fonts"]]
        counts = {"media": 0, "assignedMedia": 0}
        for folder, extensions in [("screenshots", catalog.IMAGE_EXT), ("components", catalog.COMPONENT_EXT)]:
            for media in catalog.list_images(system, folder, extensions):
                counts["media"] += 1
                name = Path(media["path"]).stem.lower().replace("_", "-")
                found = {}
                definitions = [(page_group, PAGE_RULES)] if folder == "screenshots" else []
                definitions += [(f"{prefix}-ui-elements", UI_RULES), (f"{prefix}-ux-patterns", UX_RULES)]
                for group, entries in definitions:
                    for rule_id, expression, original_label in entries:
                        label = "Home" if original_label == "Home Page" and prefix == "ios" else original_label
                        if label not in terms[group] or not re.search(rf"(?:^|-)(?:{expression})(?:-|$)", name):
                            continue
                        # forhers filenames this capture added that match a rule
                        # without being that control. Accordion and menu toggles
                        # are triggers, not switches. "pill" in wegovy-pill is
                        # the medicine, not a chip. Other packages are unchanged.
                        if system["slug"] == "forhers" and rule_id == "ui-toggle" and re.search(r"(?:^|-)(?:accordion-toggle|menu-toggle)(?:-|$)", name):
                            continue
                        if system["slug"] == "forhers" and rule_id == "ui-chips" and re.search(r"(?:^|-)wegovy-pill(?:-|$)", name):
                            continue
                        if group == page_group:
                            # A profile button or account menu on another page
                            # is not evidence that the whole page is a profile.
                            if not re.match(rf"^(?:[a-z]?\d+-)?(?:{expression})(?:-|$)", name):
                                continue
                            if re.match(r"^(?:[a-z]?\d+-)?(?:profile|account)-(?:menu|avatar|button|badge|popover)(?:-|$)", name):
                                continue
                        found.setdefault(terms[group][label], {"termId": terms[group][label], "rule": rule_id, "reason": rules[rule_id]["reason"]})
                # Fonts are offered for web vocabulary only. Desktop uses the web
                # vocabulary locally; source snapshot applicability stays intact.
                if prefix == "web":
                    for font in fonts:
                        identifier = terms["web-fonts"][font["family"]]
                        found.setdefault(identifier, {
                            "termId": identifier,
                            "rule": "font-primary",
                            "reason": f"Exact primary family {font['family']} from {system['tokens']}#{font['token']}. Inherited package evidence; fallback families excluded.",
                        })
                if found:
                    counts["assignedMedia"] += 1
                    assignments.append({"referenceId": f"systems:{system['slug']}", "mediaId": media["path"], "terms": list(found.values())})
        packages.append({"referenceId": f"systems:{system['slug']}", **counts})
    return {
        "version": 1,
        "coverage": "Local filename/state classification of canonical screenshots and component captures. Unknown labels remain unassigned. Desktop locally reuses web vocabulary; responsive mobile web captures remain web. No flow assignments without verified sequences. Font matches inherit exact recorded primary package families only. Rebuild with python3 app/scripts/build-media-taxonomy.py; migrations apply this seed once and retain later app edits.",
        "rules": rules,
        "packages": packages,
        "assignments": assignments,
    }



def _branch_seed() -> tuple[dict | None, dict | None]:
    """The pull request head's seed and catalog rows, when GitHub set them."""
    sha = os.environ.get("GITHUB_HEAD_SHA") if os.environ.get("GITHUB_BASE_REF") else None
    if not sha:
        return None, None
    try:
        seed = json.loads(subprocess.run(
            ["git", "show", f"{sha}:app/src/data/media-taxonomy.json"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout)
        raw = subprocess.run(
            ["git", "show", f"{sha}:catalog.json"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout
        rows = {s.get("slug"): s for s in json.loads(raw).get("systems") or []}
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return None, None
    return seed, rows


def _same_as_branch(path: str) -> bool:
    """True when HEAD's copy of path equals the pull request head's copy."""
    sha = os.environ.get("GITHUB_HEAD_SHA") if os.environ.get("GITHUB_BASE_REF") else None
    if not sha:
        return False
    try:
        branch = subprocess.run(
            ["git", "rev-parse", f"{sha}:{path}"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout.strip()
        head = subprocess.run(
            ["git", "rev-parse", f"HEAD:{path}"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return False
    return branch == head


def _head_touches(path: str) -> bool:
    """True when the merge commit's copy of path differs from the base.

    A depth-1 checkout has no merge base, so a three-dot diff fails and
    must not be treated as an edit. Two trees compare without history."""
    base = os.environ.get("GITHUB_BASE_REF")
    if not base:
        return False
    try:
        changed = subprocess.run(
            ["git", "diff", "--name-only", f"origin/{base}", "HEAD", "--", path],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError):
        return True
    return path in changed


def base_slugs() -> set[str] | None:
    """Slugs on the pull request's base, when GitHub is merging one."""
    base = os.environ.get("GITHUB_BASE_REF")
    if not base:
        return None
    try:
        raw = subprocess.run(
            ["git", "show", f"origin/{base}:catalog.json"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout
        catalog_json = json.loads(raw)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return None
    return {s.get("slug") for s in catalog_json.get("systems") or []}


def _base_tree_files() -> set[str] | None:
    """Paths in the pull request base. None when the base tree is unreadable.

    `-z` keeps names that contain quotes, backslashes, or non-ASCII
    characters. Without it git quotes those names, and a capture such as
    café-dark.png looks newly added."""
    base = os.environ.get("GITHUB_BASE_REF")
    if not base:
        return None
    try:
        listed = subprocess.run(
            ["git", "ls-tree", "-r", "-z", "--name-only", f"origin/{base}"],
            cwd=ROOT, check=True, capture_output=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    return {path.decode("utf-8", "surrogateescape")
            for path in listed.split(b"\0") if path}


def matches_base(result: dict, committed: dict) -> bool:
    """True when this pull request only adds packages, and the committed
    seed still matches a derivation of the base catalog and base files.

    GitHub checks the merge commit. That commit adds the new package's
    screenshots, so a derivation of the working tree never equals the
    committed seed. The seed is still current when it matches the base
    tree. Editing an existing catalog row, or a file that was already in
    the base, changes that derivation and still fails."""
    slugs = base_slugs()
    if not slugs:
        return False
    head_rows = {s.get("slug"): s for s in catalog.load_catalog()["systems"]}
    # This pull request regenerated the seed, then main gained another
    # package. The committed seed matches the branch tip in that case.
    branch_seed, branch_rows = _branch_seed()
    if (branch_seed is not None and committed == branch_seed
            and branch_rows and set(branch_rows) <= set(head_rows)
            and all(head_rows.get(slug) == row for slug, row in branch_rows.items())
            and set(head_rows) - set(branch_rows)):
        return True
    if not set(head_rows) > slugs:
        return False
    # A pull request that edits this script changes the derived rules.
    # The merge commit can also carry the base copy of the script when
    # main edited it after the branch started. That is not a capture edit.
    # Reject only a script that differs from both the base and the branch.
    if (_head_touches("app/scripts/build-media-taxonomy.py")
            and not _same_as_branch("app/scripts/build-media-taxonomy.py")):
        return False
    base_files = _base_tree_files()
    if base_files is None:
        return False
    try:
        raw = subprocess.run(
            ["git", "show", f"origin/{os.environ['GITHUB_BASE_REF']}:catalog.json"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout
        base_catalog = json.loads(raw)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return False
    base_rows = {s.get("slug"): s for s in base_catalog.get("systems") or []}
    if set(base_rows) != slugs:
        return False
    if any(head_rows.get(slug) != row for slug, row in base_rows.items()):
        return False
    # A new image under a package that was already on the base changes the
    # seed. The derivation below ignores those files so it can rebuild the
    # base, so reject them here.
    for row in base_rows.values():
        for folder, exts in (
            ("screenshots", catalog.IMAGE_EXT),
            ("components", catalog.COMPONENT_EXT),
        ):
            for item in catalog.list_images(row, folder, exts):
                if item["path"] not in base_files:
                    return False
    saved_catalog = catalog.load_catalog
    saved_images = catalog.list_images

    def base_images(system, folder, exts):
        items = saved_images(system, folder, exts)
        return [item for item in items if item["path"] in base_files]

    catalog.load_catalog = lambda: base_catalog
    catalog.list_images = base_images
    try:
        base_result = build()
    finally:
        catalog.load_catalog = saved_catalog
        catalog.list_images = saved_images
    if committed == base_result:
        return True
    # The seed may lag packages already merged to the base. It is still
    # current when it is exactly the derivation of the packages it names.
    return seed_is_prior_derivation(committed, head_rows, base_files)


def seed_is_prior_derivation(committed: dict, head_rows: dict,
                             base_files: set[str]) -> bool:
    """True when the seed derives an unchanged subset of this catalog."""
    named = {p["referenceId"].removeprefix("systems:")
             for p in committed.get("packages") or []}
    if not named or not named <= set(head_rows):
        return False
    for row in head_rows.values():
        if row.get("slug") not in named:
            continue
        for folder, exts in (
            ("screenshots", catalog.IMAGE_EXT),
            ("components", catalog.COMPONENT_EXT),
        ):
            for item in catalog.list_images(row, folder, exts):
                if item["path"] not in base_files:
                    return False
    kept = [row for row in catalog.load_catalog()["systems"]
            if row.get("slug") in named]
    saved_catalog = catalog.load_catalog
    saved_images = catalog.list_images

    def kept_images(system, folder, exts):
        items = saved_images(system, folder, exts)
        return [item for item in items if item["path"] in base_files]

    catalog.load_catalog = lambda: {"systems": kept}
    catalog.list_images = kept_images
    try:
        prior = build()
    finally:
        catalog.load_catalog = saved_catalog
        catalog.list_images = saved_images
    return committed == prior


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.check:
        committed = json.loads(OUTPUT.read_text(encoding="utf-8")) if OUTPUT.exists() else None
        if committed != result and not (committed and matches_base(result, committed)):
            raise SystemExit("Media taxonomy seed is stale; run python3 app/scripts/build-media-taxonomy.py")
        print("Media taxonomy seed is current")
    else:
        catalog.atomic_write(OUTPUT, json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        print(f"Wrote {len(result['assignments'])} media records, {sum(len(a['terms']) for a in result['assignments'])} term assignments across {len(result['packages'])} packages")


if __name__ == "__main__":
    main()
