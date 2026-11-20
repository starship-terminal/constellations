// Reads every custom property zellerfeld.com declares and writes raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// The storefront serves same-origin CSS, so the live CSSOM is readable. Each
// name is resolved on :root at 1440x900 in the only theme the site ships
// (color-scheme: normal, no data-theme). Colours come back as sRGB hex.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launchBrowser, UA, BASE, hideCookies, dismissNotice } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const browser = await launchBrowser();
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(4000);
await hideCookies(page);
await dismissNotice(page);

const harvested = await page.evaluate(() => {
  const rules = [];
  const fonts = [];
  const skipped = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.cssText.split('{')[0].trim().slice(0, 140);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) props[k] = r.style.getPropertyValue(k).trim();
      }
      if (Object.keys(props).length) rules.push({ selector: r.selectorText, context: ctx, file, properties: props });
    }
  };
  for (const sheet of document.styleSheets) {
    let file = sheet.href || 'inline';
    try { walk(sheet.cssRules, [], file); }
    catch (e) { skipped.push({ file, error: String(e).slice(0, 160) }); }
  }
  const root = getComputedStyle(document.documentElement);
  const names = new Set();
  for (const rule of rules) for (const k of Object.keys(rule.properties)) names.add(k);
  const resolved = {};
  for (const name of [...names].sort()) {
    resolved[name] = root.getPropertyValue(name).trim();
  }
  return {
    href: location.origin + location.pathname,
    colorScheme: root.colorScheme,
    themeAttr: document.documentElement.getAttribute('data-theme'),
    fonts,
    skipped,
    rules,
    resolved,
  };
});

const bin = (name) => {
  if (name.startsWith('--primitive-')) return 'primitive';
  if (name.startsWith('--semantic-')) return 'semantic';
  if (name.startsWith('--font-') || name.startsWith('--radius')) return 'type';
  if (name.startsWith('--layout-') || name.startsWith('--content-') || name.startsWith('--main-grid') || name.startsWith('--min-inline') || name.startsWith('--app-')) return 'layout';
  return 'other';
};
const bins = { primitive: [], semantic: [], type: [], layout: [], other: [] };
for (const rule of harvested.rules) bins[bin(Object.keys(rule.properties)[0])]?.push(rule);

const out = {
  product: 'Zellerfeld',
  captured: new Date().toISOString(),
  page: harvested.href,
  theme: { colorScheme: harvested.colorScheme, dataTheme: harvested.themeAttr },
  source: 'live CSSOM on https://www.zellerfeld.com/ at 1440x900, headed Chrome, signed out',
  fonts: harvested.fonts.map((f) => ({
    family: f['font-family'],
    weight: f['font-weight'],
    style: f['font-style'],
    display: f['font-display'],
    file: f.file,
  })),
  skipped: harvested.skipped,
  counts: Object.fromEntries(Object.entries(bins).map(([k, v]) => [k, v.length])),
  resolved: harvested.resolved,
  rules: harvested.rules,
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('vars', Object.keys(harvested.resolved).length, 'rules', harvested.rules.length, 'fonts', harvested.fonts.length, 'skipped', harvested.skipped.length);
await browser.close();
