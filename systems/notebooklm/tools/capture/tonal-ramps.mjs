// Builds the hue ramps NotebookLM does not declare, and writes raw/tonal-ramps.json.
//
//   MCU=/path/to/@material/material-color-utilities/index.js node tools/capture/tonal-ramps.mjs
//
// The product declares full ramps only for --nlm-grey and --nlm-blue (and --nlm-green, with nine
// steps set to `undefined`; its step names are not tones, -50 is tone 83, so it is left as declared
// and the green hue's ramp is green-status). Every other hue exists as role colours: Angular Material's
// --mat-sys-<hue>, -container, on-<hue> and on-<hue>-container, plus the Studio accents and the
// status roles. Those roles sit on Material 3 tones (40, 80, 90, 30, 100, 20), so each ramp here is
// the Material tonal palette of a measured seed colour, built with Material's own generator:
//   - a step whose tone the product paints keeps the measured value (source "measured": the
//     variable and theme it was read from), when the measured colour is within 20 degrees of the
//     seed's hue and 3 tones of the step;
//   - every other step is the generated tone (source "derived");
//   - a measured colour on the seed's hue that falls more than 3 tones from every standard tone is
//     added as an extra measured step named by its own tone (the blue Studio accent is tone 46).
// A measured colour whose tone another measured colour already holds, or that is off every ramp's
// hue, is left out and listed under _meta.notInRamp.
// For every measured colour the generated tone at the same step is also recorded, with the RGB
// distance between the two, so the README can say how closely the generator reproduces the product.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.join(HERE, '..', '..', 'raw');
const MCU = process.env.MCU || path.join(process.env.HOME, '.design-systems/pw/node_modules/@material/material-color-utilities/index.js');
const { TonalPalette, Hct, argbFromRgb, hexFromArgb } = await import(MCU);

const VARS = JSON.parse(fs.readFileSync(path.join(RAW, 'css-vars.json'))).vars;
const TONES = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 100];
const roles = (h) => [`--mat-sys-${h}`, `--mat-sys-${h}-container`, `--mat-sys-on-${h}`, `--mat-sys-on-${h}-container`];

// name: [seed variable (light theme), members in priority order, description]
const RAMPS = {
  red: ['--mat-sys-red', [...roles('red'), ...roles('error'), '--nb-sys-color--error', '--nb-sys-color--error-container', '--nb-sys-color--on-error-container', '--nlm-red-50', '--nlm-icons-red'],
    'Errors and the red data-viz pair (Material red and error, nb-sys error, --nlm-red-50, the PDF icon).'],
  orange: ['--mat-sys-orange', [...roles('orange'), '--nb-studio-accent-warm'], 'The orange data-viz pair and the warm Studio accent.'],
  amber: ['--mat-sys-warning', [...roles('warning'), ...roles('yellow'), '--nlm-text-warning', '--nlm-fills-ui-caution-subtle'],
    'Light-theme warnings and the light yellow data-viz pair (Material warning and yellow share one value there); the dark-theme warning yellows sit on palette.yellow.'],
  yellow: ['--nlm-icons-yellow', [...roles('yellow'), ...roles('warning'), '--nlm-text-warning', '--nlm-icons-yellow', '--nb-sys-color--code-yellow-text', '--nb-studio-accent-warm', '--nlm-fills-ui-caution-subtle', '--nlm-tiles-on-yellow'],
    'Seeded from the yellow icon #fcbd00, which is also the dark warning and dark yellow data-viz colour. Code yellow, the dark warm Studio accent and the dark warning text are near this hue but at tones already held, so they are listed under notInRamp.'],
  'green-status': ['--mat-sys-success', [...roles('success'), ...roles('green'), '--nb-sys-color--positive', '--nb-sys-color--positive-container', '--nb-sys-color--on-positive-container', '--nb-studio-accent-green'],
    'Success, the green data-viz pair and the green Studio accent; the brand green is palette.green.'],
  cyan: ['--mat-sys-cyan', [...roles('cyan'), '--nb-studio-accent-teal'], 'The cyan data-viz pair and the teal Studio accent.'],
  sky: ['--nb-sys-color-acc-color--accent', ['--nb-sys-color-acc-color--accent', '--nb-sys-color-acc-color--accent-container', '--nb-sys-color-acc-color--accent-fixed', '--nb-sys-color--surface-accent'],
    'The luminous accent in light (the New notebook button, the selected chip). In dark the accent turns navy (hue 276), nearer palette.info; of the navy colours only the dark surface accent is a step there (info.14).'],
  info: ['--mat-sys-info', [...roles('info'), ...roles('blue'), '--nb-studio-accent-blue', '--nlm-icons-blue', '--nb-sys-color-acc-color--accent', '--nb-sys-color-acc-color--accent-container', '--nb-sys-color-acc-color--accent-fixed', '--nb-sys-color--surface-accent'],
    'Material info, the blue data-viz pair, the blue Studio accent and the dark luminous surface accent; the brand blue is palette.blue.'],
  purple: ['--mat-sys-purple', [...roles('purple'), '--nb-studio-accent-purple'], 'The purple data-viz pair and the purple Studio accent.'],
  pink: ['--mat-sys-pink', [...roles('pink'), '--nb-studio-accent-pink'], 'The pink data-viz pair and the pink Studio accent.'],
};

const argbOf = (c) => { const m = c && c.match(/^rgb\((\d+), (\d+), (\d+)\)$/); return m ? argbFromRgb(+m[1], +m[2], +m[3]) : null; };
const dist = (a, b) => Math.round(Math.hypot(...[16, 8, 0].map((s) => ((a >> s) & 255) - ((b >> s) & 255))));
const hueGap = (a, b) => { const d = Math.abs(a - b) % 360; return Math.min(d, 360 - d); };

const out = { _meta: { generator: 'Material color utilities 0.3.0, TonalPalette.fromInt(seed)', tones: TONES }, ramps: {} };
for (const [name, [seedVar, members, desc]] of Object.entries(RAMPS)) {
  const seed = argbOf(VARS[seedVar]?.light?.color);
  if (!seed) throw new Error(`${name}: seed ${seedVar} has no light colour`);
  const pal = TonalPalette.fromInt(seed);
  const hue = Hct.fromInt(seed).hue;
  const steps = Object.fromEntries(TONES.map((t) => [t, { hex: hexFromArgb(pal.tone(t)), source: 'derived' }]));
  const checks = [];
  for (const v of members) for (const theme of ['light', 'dark']) {
    const a = argbOf(VARS[v]?.[theme]?.color);
    if (!a) continue;
    const h = Hct.fromInt(a);
    const step = TONES.reduce((b, t) => (Math.abs(t - h.tone) < Math.abs(b - h.tone) ? t : b));
    const gen = pal.tone(step);
    const onHue = h.chroma < 8 || hueGap(h.hue, hue) <= 20;
    const onStep = Math.abs(step - h.tone) <= 3;
    const check = { var: v, theme, hex: hexFromArgb(a), tone: Math.round(h.tone), step, generated: hexFromArgb(gen), rgbDistance: dist(a, gen), pinned: false };
    if (!onHue) check.skipped = 'off hue';
    else if (!onStep) check.between = true;
    if (onHue && onStep && steps[step].source === 'derived') {
      steps[step] = { hex: hexFromArgb(a), source: 'measured', var: v, theme, generated: hexFromArgb(gen), rgbDistance: dist(a, gen) };
      check.pinned = true;
    }
    if (!checks.some((c) => c.hex === check.hex)) checks.push(check);
  }
  for (const c of checks.filter((c) => c.between)) {
    if (Object.values(steps).some((st) => st.hex === c.hex)) continue;
    const name = String(c.tone) in steps ? Hct.fromInt(argbOf(VARS[c.var][c.theme].color)).tone.toFixed(1) : String(c.tone);
    steps[name] = { hex: c.hex, source: 'measured', var: c.var, theme: c.theme, extra: true };
    c.pinned = true;
  }
  const sorted = Object.fromEntries(Object.entries(steps).sort((x, y) => +x[0] - +y[0]));
  out.ramps[name] = { seed: { var: seedVar, hex: hexFromArgb(seed), hue: Math.round(hue), chroma: Math.round(Hct.fromInt(seed).chroma) }, description: desc, steps: sorted, checks };
}
const onStep = Object.values(out.ramps).flatMap((r) => r.checks.filter((c) => !c.skipped && !c.between));
const inRamp = new Set(Object.values(out.ramps).flatMap((r) => Object.values(r.steps).map((st) => st.hex)));
out._meta.notInRamp = [...new Set(Object.values(out.ramps).flatMap((r) => r.checks.filter((c) => !inRamp.has(c.hex)).map((c) => `${c.var} (${c.theme}) ${c.hex}`)))];
out._meta.match = { measured: onStep.length, within10: onStep.filter((c) => c.rgbDistance <= 10).length, within25: onStep.filter((c) => c.rgbDistance <= 25).length };
fs.writeFileSync(path.join(RAW, 'tonal-ramps.json'), JSON.stringify(out, null, 1) + '\n');
for (const [n, r] of Object.entries(out.ramps)) console.log(n.padEnd(13), Object.values(r.steps).filter((s) => s.source === 'measured').length, 'measured of', TONES.length, ' between tones:', r.checks.filter((c) => c.between).map((c) => `${c.var}/${c.theme}`).join(' '));
console.log('measured colours on a step:', JSON.stringify(out._meta.match));
console.log('colours in no ramp:', out._meta.notInRamp);
