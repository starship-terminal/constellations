// One rule for every route's component crops: 256 colours, and a crop wider than 1600 px or larger than
// 1.2 megapixels (a whole sidebar or section at 2x) is halved, so the folder stays small. The public and
// signed-in routes used to halve by different rules, so the same component came out at 2x on one and 1x
// on the other. Returns true when the crop was halved.
import { execFileSync } from 'node:child_process';

export const HALVE = { width: 1600, pixels: 1200000 };
const SCRIPT = [
  'import sys',
  'from PIL import Image',
  'f, w, px = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])',
  'im = Image.open(f).convert("RGB")',
  'half = im.width > w or im.width * im.height > px',
  'if half: im = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)',
  'im.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
  'print("halved" if half else "kept")',
].join('\n');

export function quantizeCrop(file, python = process.env.PYTHON || 'python3') {
  return execFileSync(python, ['-c', SCRIPT, file, String(HALVE.width), String(HALVE.pixels)], { encoding: 'utf8' }).trim() === 'halved';
}
