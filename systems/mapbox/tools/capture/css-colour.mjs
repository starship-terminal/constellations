// Computed CSS colours as sRGB hex, for the build-measurements scripts: rgb()/rgba(), color(srgb),
// and lab()/oklab(), which Chromium computes for color-mix (Tailwind 4's opacity modifiers).
// A translucent colour reads "#rrggbb @ alpha".
export const hex = (c) => {
  if (!c) return c;
  return String(c).replace(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/g, (m, r, g, b, a) => {
    const h = '#' + [r, g, b].map((v) => (+v).toString(16).padStart(2, '0')).join('');
    return a === undefined || +a === 1 ? h : `${h} @ ${+a}`;
  }).replace(/color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: \/ ([\d.]+))?\)/g, (m, r, g, b, a) => {
    const h = '#' + [r, g, b].map((v) => Math.round(+v * 255).toString(16).padStart(2, '0')).join('');
    return a === undefined ? h : `${h} @ ${+a}`;
  }).replace(/(ok)?lab\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+))?\)/g, (m, ok, L, A, B, al) => {
    const [r, g, b] = ok ? oklabToSrgb(parseFloat(L) * (L.endsWith('%') ? 0.01 : 1), +A, +B) : labToSrgb(parseFloat(L), +A, +B);
    const h = '#' + [r, g, b].map((v) => Math.round(Math.min(1, Math.max(0, v)) * 255).toString(16).padStart(2, '0')).join('');
    return al === undefined || +al === 1 ? h : `${h} @ ${+al}`;
  });
};
// Tailwind 4 writes an opacity modifier (`bg-token-text-primary/3`) as color-mix, which Chromium
// computes in lab() or oklab(); both are turned back into sRGB hex here (CSS Color 4 formulas).
const gam = (x) => (x <= 0.0031308 ? 12.92 * x : 1.055 * Math.pow(x, 1 / 2.4) - 0.055);
function oklabToSrgb(L, a, b) {
  const l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3, m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3, s = (L - 0.0894841775 * a - 1.291485548 * b) ** 3;
  return [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.707614701 * s].map(gam);
}
function labToSrgb(L, a, b) {
  const fy = (L + 16) / 116, fx = fy + a / 500, fz = fy - b / 200, e = 216 / 24389, k = 24389 / 27;
  const finv = (t) => (t ** 3 > e ? t ** 3 : (116 * t - 16) / k);
  const X = finv(fx) * 0.3457 / 0.3585, Y = L > k * e ? fy ** 3 : L / k, Z = finv(fz) * (1 - 0.3457 - 0.3585) / 0.3585;
  // D50 to D65 (Bradford), then XYZ to linear sRGB.
  const x = 0.955473421488075 * X - 0.02309845494876471 * Y + 0.06325924320057072 * Z, y = -0.0283697093338637 * X + 1.0099953980813041 * Y + 0.021041441191917323 * Z, z = 0.012314014864481998 * X - 0.020507649298898964 * Y + 1.330365926242124 * Z;
  return [3.2409699419 * x - 1.5373831776 * y - 0.4986107603 * z, -0.9692436363 * x + 1.8759675015 * y + 0.0415550574 * z, 0.0556300797 * x - 0.2039769589 * y + 1.0569715142 * z].map(gam);
}
