// Reads custom properties masterclass.com's stylesheets declare and writes
// raw/css-vars.json. Public signed-out only. Consent is hidden, never clicked.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, BASE, UA, blockedByChallenge, hideConsent } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const ROUTES = [
  BASE + '/',
  BASE + '/classes/revolutionize-your-workflows-with-ai',
  BASE + '/checkout',
  BASE + '/auth/login',
  BASE + '/categories',
  BASE + '/gift',
  BASE + '/for-business',
];

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US',
});
// Automation is not hidden (no webdriver mask): a bot check is recorded as a boundary, not bypassed.
const bodies = new Map();
const inline = [];
for (const route of ROUTES) {
  const p = await context.newPage();
  p.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
  });
  await p.goto(route, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch((e) => console.log('goto fail', route, e.message.split('\n')[0]));
  await p.waitForTimeout(3500);
  if (await blockedByChallenge(p)) {
    // A challenge page's CSS is not the product's: stop before anything is written.
    console.error('BLOCKED by a bot check at', route, '- raw/css-vars.json left as it was');
    await browser.close();
    process.exit(2);
  }
  await hideConsent(p);
  const blocks = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
    try { return ['inline-' + i + ' @ ' + location.pathname, [...s.cssRules].map((r) => r.cssText).join('\n')]; }
    catch { return null; }
  }).filter(Boolean));
  inline.push(...blocks);
  console.log('harvested', route, 'inline', blocks.length, 'linked so far', bodies.size);
  await p.close().catch(() => {});
}

const sheets = [...bodies.entries()].map(([name, css]) => ({ name, media: '', css, bytes: css.length }))
  .concat(inline.map(([name, css]) => ({ name, media: '', css, bytes: css.length })));
if (!sheets.length) { console.log('no sheets'); await browser.close(); process.exit(2); }

const page = await context.newPage();
const result = await page.evaluate((list) => {
  // Each page callback runs apart from this module and needs its own copy.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const walk = (cssRules, context, file) => {
    for (const r of cssRules) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { family: r.style.getPropertyValue('font-family').replace(/["']/g, ''), weight: r.style.getPropertyValue('font-weight'), style: r.style.getPropertyValue('font-style'), file };
        fonts.push(o);
        continue;
      }
      if (r.cssRules) {
        const ctx = r.conditionText ? [...context, '@' + r.constructor.name.replace('Rule', '').toLowerCase() + ' ' + r.conditionText] : context;
        walk(r.cssRules, ctx, file);
        continue;
      }
      if (!r.style) continue;
      const properties = {};
      for (const n of r.style) if (n.startsWith('--')) properties[n] = noUrl(r.style.getPropertyValue(n).trim()).slice(0, 400);
      if (Object.keys(properties).length) rules.push({ file, selector: (r.selectorText || '').slice(0, 240), context, properties });
    }
  };
  for (const s of list) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { rules.push({ file: s.name, error: String(e).slice(0, 200) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts };
}, sheets.map(({ name, css }) => ({ name, css })));

const want = [...new Set(result.rules.filter((r) => !r.error).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !n.startsWith('--tw-')).sort();

await page.setContent('<!doctype html><html><head>' + sheets.map((s) => '<style>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('') + '</head><body><div id="probe"></div></body></html>', { waitUntil: 'load' });
const resolvedLight = await page.evaluate((names) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const root = document.documentElement;
  const probe = document.getElementById('probe');
  const lin = (c) => (c <= 0.0031308 ? 12.92 * c : 1.055 * Math.pow(c, 1 / 2.4) - 0.055);
  const num = (x) => (String(x).endsWith('%') ? parseFloat(x) / 100 : parseFloat(x));
  const norm = (c) => {
    let m = c.match(/^rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)$/);
    if (!m) return c;
    const rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v));
    const a = m[4] === undefined ? 1 : +m[4];
    return a >= 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
  };
  const out = {};
  for (const name of names) {
    const raw = noUrl(getComputedStyle(root).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
    probe.removeAttribute('style');
    if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert|none)$/.test(raw)) {
      probe.style.color = raw; r.kind = 'color'; r.value = norm(getComputedStyle(probe).color);
    } else if (!raw.includes('%') && CSS.supports('width', raw) && !raw.includes(' ')) {
      probe.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(probe).width;
    } else if (CSS.supports('box-shadow', raw)) { r.kind = 'shadow'; r.value = raw; }
    else r.kind = 'other';
    out[name] = r;
  }
  return out;
}, want);

const binOf = (r) => {
  const names = Object.keys(r.properties || {});
  if (names.every((n) => n.startsWith('--tw-'))) return 'tailwind';
  if (names.some((n) => n.startsWith('--mc-'))) return 'mc';
  return 'app';
};
const ok = result.rules.filter((r) => !r.error);
for (const r of ok) r.bin = binOf(r);
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'masterclass.com public signed-out stylesheets (linked + inline), harvested in headless Chromium. The product paints one dark theme; --mc-color-* and --mc-theme-* are the declared token layer.',
  sheets: sheets.map(({ name, bytes }) => ({ name: name.slice(0, 180), bytes })),
  counts: { rules: ok.length, fonts: result.fonts.length, names: { mc: names('mc').length, app: names('app').length, tailwind: names('tailwind').length } },
  errors: result.rules.filter((r) => r.error).slice(0, 20),
  mc: ok.filter((r) => r.bin === 'mc').slice(0, 400),
  app: ok.filter((r) => r.bin === 'app').slice(0, 80),
  fonts: result.fonts.slice(0, 40),
  resolved: { dark: resolvedLight },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('css-vars.json rules', ok.length, 'resolved', Object.keys(resolvedLight).length, 'fonts', result.fonts.length);
await browser.close();
