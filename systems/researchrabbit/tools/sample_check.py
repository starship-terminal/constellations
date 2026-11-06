"""Checks each sampled colour in build_tokens.py against the screenshot pixel it names."""


def check_samples(samples, root, resolve, norm_color, tolerance=3):
    """samples: (token path, value, screenshot path relative to root, (x, y)). Each value, resolved
    and normalised to #rrggbb, must be within `tolerance` per channel of the pixel (the screenshots
    are 256-colour PNGs, so a flat fill can come back a step or two off). Needs Pillow and the
    screenshots from Git LFS; without either the check is skipped and says so. Returns how many
    samples were checked."""
    try:
        from PIL import Image
    except ImportError:
        print("note: sampled colours not checked (needs Pillow)")
        return 0
    shots, checked = {}, 0
    for path, val, shot, (x, y) in samples:
        f = root / shot
        if shot not in shots:
            head = f.read_bytes()[:8] if f.exists() else b""
            shots[shot] = Image.open(f).convert("RGB") if head.startswith(b"\x89PNG") else None
        if shots[shot] is None:
            print(f"note: {shot} is not a PNG here (git lfs pull it); its samples were not checked")
            continue
        want = norm_color(resolve(val))
        got = "#%02x%02x%02x" % shots[shot].getpixel((x, y))
        if max(abs(int(want[i:i + 2], 16) - int(got[i:i + 2], 16)) for i in (1, 3, 5)) > tolerance:
            raise ValueError(f"{path}: sampled {shot} at ({x}, {y}) is {got}, not {want}")
        checked += 1
    return checked
