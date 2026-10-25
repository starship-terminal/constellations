"""probe.py <theme> <shot> <row|col> <line> <from> <to> [...more quadruples after shot]
Print colour runs along a row or column between two positions (capture pixels)."""
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "native"))
import sample
theme = sys.argv[1]
args = sys.argv[2:]
cache = {}
while args:
    shot, axis, line, a, b = args[:5]
    args = args[5:]
    if shot not in cache:
        cache[shot] = sample.read_png(str(pathlib.Path.home() / f".design-systems/zed-desktop/raw-shots/{theme}/{shot}.png"))[2]
    rows = cache[shot]
    line, a, b = int(line), int(a), int(b)
    pix = (lambda i: rows[line][i]) if axis == "row" else (lambda i: rows[i][line])
    print(f"== {shot} {axis} {line} [{a},{b})")
    start, prev = a, pix(a)
    out = []
    for i in range(a + 1, b + 1):
        p = pix(i) if i < b else None
        if p is None or max(abs(p[k] - prev[k]) for k in range(3)) > 4:
            out.append(f"{start}+{i - start} #{prev[0]:02X}{prev[1]:02X}{prev[2]:02X}")
            start, prev = i, p
    print("  " + "  ".join(out[:60]))
