// Read the rules behind Brilliant's motion, focus, state and layout behaviour from the production
// stylesheet, which the public pages and the signed-in app share (Panda CSS, one atomic sheet).
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/css-rules.mjs
// Writes raw/css-rules.json: font stacks, reduced-motion behaviour, focus rings, button3d hover and
// pressed rules, status colour use, elevation use and grid templates, each with how many rules use
// it. Every value is copied from a rule; nothing is inferred. Public pages only, headless, no account.
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'node:url';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(HERE, '..', '..', 'raw');
const PAGES = ['https://brilliant.org/', 'https://brilliant.org/courses/', 'https://brilliant.org/login/', 'https://brilliant.org/subscribe/'];

const b = await chromium.launch();
const p = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
const seen = new Map(); // rule text -> { sel, body, media }
let fonts = null;
for (const u of PAGES) {
  await p.goto(u, { waitUntil: 'load', timeout: 60000 });
  await p.waitForTimeout(2500);
  const got = await p.evaluate(() => {
    const out = [];
    const walk = (rules, media) => { for (const r of rules) {
      if (r.selectorText !== undefined) out.push({ sel: r.selectorText, body: r.style.cssText, media });
      if (r.cssRules) walk(r.cssRules, r.conditionText || (r.media && r.media.mediaText) || media);
    } };
    for (const s of document.styleSheets) { try { if (s.href && !s.href.startsWith(location.origin)) continue; walk(s.cssRules, ''); } catch {} }
    const root = getComputedStyle(document.documentElement);
    const fonts = {};
    for (const n of ['brilliant', 'robert', 'semi-mono', 'code', 'math', 'monospace']) fonts[n] = root.getPropertyValue('--panda-fonts-' + n).trim();
    return { out, fonts };
  });
  for (const r of got.out) seen.set(r.media + '|' + r.sel + '|' + r.body, r);
  fonts = fonts || got.fonts;
  console.log(u, got.out.length, 'rules');
}
await b.close();
const R = [...seen.values()];
const count = (arr) => Object.entries(arr.reduce((m, k) => (m[k] = (m[k] || 0) + 1, m), {})).sort((a, b) => b[1] - a[1] || (a[0] < b[0] ? -1 : 1)).map(([value, rules]) => ({ value, rules }));
const decl = (body, prop) => [...body.matchAll(new RegExp('(?:^|;\\s*)' + prop + ':\\s*([^;]+)', 'g'))].map((m) => m[1].trim());
// Panda's atomic class names carry the condition and the value; strip the specificity padding and
// escapes so the evidence stays readable.
const short = (sel) => sel.replace(/:not\(#(\\#)+\)/g, '').replace(/\\/g, '').slice(0, 200);

// Reduced motion: Panda's `allowMotion` condition is [data-reduced-motion="false"] on <html> (the
// app's Reduce motion preference); `motionReduce` is the OS media query.
const allow = R.filter((r) => r.sel.includes('[data-reduced-motion="false"]'));
const media = R.filter((r) => /prefers-reduced-motion/.test(r.media));
const props = (rs) => count(rs.flatMap((r) => r.body.split(';').map((d) => d.split(':')[0].trim()).filter((d) => d && !d.startsWith('--'))));
const anims = count(allow.flatMap((r) => decl(r.body, 'animation(?:-name)?')).map((v) => v.replace(/^[\d.]+m?s \S+ [\d.]+m?s \d+ \S+ \S+ running /, '')));

// Focus rings: every declaration in a rule whose selector names :focus-visible or [data-focus-visible].
const focus = R.filter((r) => /focus-visible|data-focus/.test(r.sel));
const focusDecl = count(focus.flatMap((r) => ['box-shadow', 'outline', 'outline-offset', 'outline-width', 'outline-color'].flatMap((pp) => decl(r.body, pp).map((v) => pp + ': ' + v))));

// button3d: hover and pressed rules (selectors that mention the face slot or button3d variables).
const b3 = R.filter((r) => /button3d/.test(r.sel + r.body) && /hover|active|data-pressed|data-press/.test(r.sel)).map((r) => ({ when: /:active|press/.test(r.sel) ? 'pressed' : 'hover', theme: r.sel.includes('[data-theme="dark"]') ? 'dark' : 'base', safariOnly: /safari/.test(r.sel), sel: short(r.sel), body: r.body }));

const status = count(R.flatMap((r) => [...r.body.matchAll(/--panda-colors-(?:bg|text|border|icon|status)-(?:success|warning|danger|info)[a-z-]*/g)].map((m) => m[0])));
const elevation = count(R.flatMap((r) => [...r.body.matchAll(/--panda-shadows-[a-z0-9-]+/g)].map((m) => m[0])));
const grids = count(R.flatMap((r) => decl(r.body, 'grid-template-columns')));

const out = {
  _meta: { source: 'Production stylesheet read from the CSSOM of ' + PAGES.join(', ') + ' (headless Chromium, signed out)', rules: R.length },
  fonts,
  reducedMotion: {
    note: 'allowMotion rules apply only when <html data-reduced-motion="false">; the app sets it from the Reduce motion preference. motionReduce rules apply under @media (prefers-reduced-motion: reduce).',
    allowMotionRules: allow.length, allowMotionProperties: props(allow), allowMotionAnimations: anims,
    mediaRules: media.length, mediaProperties: props(media), mediaDeclarations: count(media.map((r) => r.body)),
  },
  focus: { rules: focus.length, declarations: focusDecl },
  button3d: b3,
  status, elevation, grids,
};
fs.writeFileSync(path.join(RAW, 'css-rules.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote raw/css-rules.json', R.length, 'rules');
