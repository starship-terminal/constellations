#!/usr/bin/env python3
"""Store rendered snapshots: screenshots as 256-colour PNGs, snapshots gzipped outside the repo.

usage: python3 tools/capture/store.py SNAP_DIR

SNAP_DIR holds <label>.html, <label>.json and <label>.png from unsnap.py and render.mjs. Each
label is renamed to the reference's {page}-light-{state} scheme (NAMES below) and written to
screenshots/ quantized to 256 colours; flat UI colours stay exact, so read values from tokens.json,
not the images. The HTML snapshots carry the signed-in pages, so they are gzipped into
$RR_SNAPSHOTS (default ~/.design-systems/snaps/researchrabbit), never into the repository;
measure.mjs reads them from there.
"""
import gzip, os, pathlib, shutil, sys
from PIL import Image

NAMES = {
    'graph-split-default': 'search-split-light-default',
    'graph-split-hover-input': 'search-split-light-hover-input',
    'graph-split-hover-result': 'search-split-light-hover-result',
    'graph-split-hover-list-card': 'search-split-light-hover-list-card',
    'graph-split-hover-legend-inputs': 'search-split-light-hover-legend-inputs',
    'graph-split-hover-legend-results': 'search-split-light-hover-legend-results',
    'graph-split-inspect-node': 'search-split-light-inspect-node',
    'graph-map-default': 'search-map-light-default',
    'graph-map-zoomed-in': 'search-map-light-zoomed-in',
    'graph-map-inspect-node': 'search-map-light-inspect-node',
    'graph-map-settings-x-axis': 'search-map-light-settings-x-axis',
    'graph-map-settings-y-axis': 'search-map-light-settings-y-axis',
    'graph-map-settings-size': 'search-map-light-settings-size',
    'graph-map-settings-advanced': 'search-map-light-settings-advanced',
    'graph-map-filter-popover': 'search-map-light-filter-popover',
    'search-list-default': 'search-list-light-default',
    'library-collection-map': 'library-map-light-default',
    'library-collection-map-hover': 'library-map-light-hover',
    'library-collection-map-positions-moved': 'library-map-light-positions-moved',
    'library-collection-map-positions-reset-menu': 'library-map-light-positions-reset-menu',
    'library-collection-list': 'library-list-light-default',
    'home-default': 'home-light-default',
    # 2026-10-17 refresh
    'home-refresh': 'home-light-refresh',
    'home-search-typed': 'home-light-search-typed',
    'menu-workspace-highlighted': 'home-light-workspace-menu',
    'menu-account-highlighted': 'home-light-account-menu',
    'account-profile': 'account-light-profile',
    'account-profile-edit-dialog': 'account-light-edit-profile-dialog',
    'account-delete-confirm': 'account-light-delete-confirm',
    'account-preferences': 'account-light-preferences',
    'account-subscription-empty': 'account-light-subscription-empty',
    'search-keyword-results': 'search-list-light-keyword-results',
    'search-list-loading': 'search-list-light-loading',
    'search-loading': 'search-list-light-updating-dialog',
    'search-list-selected': 'search-list-light-selected',
    'search-settings-open': 'search-list-light-settings-drawer',
    'search-settings-select-open': 'search-list-light-settings-select-open',
    'search-settings-checked': 'search-list-light-settings-checked',
    'library-all-articles': 'library-all-light-default',
    'library-table': 'library-table-light-default',
    'library-reading-empty': 'library-reading-light-empty',
    'mobile-screen-too-small': 'library-mobile-light-screen-too-small',
    'mobile-library-continue': 'library-mobile-light-continue',
    'search-start': 'search-start-light-recent',
    'library-notes-empty': 'library-all-light-notes-empty',
    'library-all-selected': 'library-all-light-selected',
    # 2026-10-17 second pass
    'library-cite-dialog': 'library-all-light-cite-dialog',
    'feedback-toast': 'library-all-light-toast',
    'search-error-citation-missing': 'search-list-light-citation-missing',
    'search-tablet-inspect': 'search-tablet-light-inspect',
    'home-narrow-stacked': 'home-narrow-light-stacked',
}

REF = pathlib.Path(__file__).resolve().parent.parent.parent
SNAP = pathlib.Path(sys.argv[1])
OUT = REF / 'screenshots'
ARCH = pathlib.Path(os.environ.get('RR_SNAPSHOTS', '~/.design-systems/snaps/researchrabbit')).expanduser()
OUT.mkdir(exist_ok=True)
ARCH.mkdir(parents=True, exist_ok=True)
for label, name in sorted(NAMES.items()):
    png = SNAP / f'{label}.png'
    if not png.exists():
        print('missing', label)
        continue
    Image.open(png).convert('RGB').quantize(256, dither=Image.Dither.NONE).save(OUT / f'{name}.png', optimize=True)
    for ext in ('html', 'json'):
        with open(SNAP / f'{label}.{ext}', 'rb') as src, gzip.GzipFile(ARCH / f'{name}.{ext}.gz', 'wb', mtime=0) as dst:
            shutil.copyfileobj(src, dst)
    print(name)
