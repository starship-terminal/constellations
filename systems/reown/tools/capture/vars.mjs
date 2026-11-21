// Read Reown custom properties from the live public pages.
// Marketing (reown.com), docs (docs.reown.com, light and dark), demo (demo.reown.com).
// PLAYWRIGHT=... node systems/reown/tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(HERE, '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

function bin(name, surface) {
  if (surface === 'marketing') {
    if (name.startsWith('--p-')) return 'primitive';
    if (name.startsWith('--s-')) return 'semantic';
    return 'other';
  }
  if (surface === 'docs') {
    if (name.startsWith('--tw-') || name.startsWith('--shiki-')) return 'utility';
    return 'docs';
  }
  if (surface === 'demo') {
    if (name.startsWith('--apkt-')) return 'appkit';
    if (name.startsWith('--tw-')) return 'utility';
    return 'demo';
  }
  return 'other';
}

async function readPage(page) {
  return page.evaluate(() => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))[^)]*\)/gi, 'url(…)') : v);
    const rules = [];
    const fonts = [];
    const walk = (list, ctx) => {
      if (!list) return;
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = {};
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
          fonts.push(o);
          continue;
        }
        if (r.cssRules && !r.style) {
          const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
            : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
            : r.cssText.split('{')[0].trim().slice(0, 120);
          walk(r.cssRules, [...ctx, head]);
          continue;
        }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
        }
        if (Object.keys(props).length) rules.push({ selector: (r.selectorText || '').slice(0, 240), context: ctx.slice(-4), properties: props });
      }
    };
    for (const sheet of document.styleSheets) {
      try { walk(sheet.cssRules, []); } catch { /* cross-origin */ }
    }
    const cs = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const names = new Set();
    for (const rule of rules) for (const k of Object.keys(rule.properties)) names.add(k);
    const resolved = {};
    for (const n of names) {
      const v = cs.getPropertyValue(n).trim();
      if (v) resolved[n] = noUrl(v).slice(0, 240);
    }
    const themeClasses = [...new Set([...document.querySelectorAll('[class*="theme--"]')].map((el) => (String(el.className).match(/theme--[\w-]+/) || [])[0]).filter(Boolean))];
    return {
      title: document.title,
      resolved,
      rules,
      fonts,
      themeClasses,
      body: {
        backgroundColor: body.backgroundColor,
        color: body.color,
        fontFamily: body.fontFamily,
        fontSize: body.fontSize,
      },
      htmlClass: document.documentElement.className.slice(0, 160),
    };
  });
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA });
const page = await context.newPage();

const surfaces = {};

await page.goto('https://reown.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1500);
const home = await readPage(page);
surfaces.marketing = {
  url: 'https://reown.com/',
  title: home.title,
  body: home.body,
  themeClasses: home.themeClasses,
  fonts: home.fonts,
  resolved: home.resolved,
  ruleCount: home.rules.length,
};
const marketingRules = home.rules.map((r) => ({ ...r, bin: Object.keys(r.properties).some((k) => k.startsWith('--p-') || k.startsWith('--s-')) ? 'product' : 'other' }));

await page.emulateMedia({ colorScheme: 'dark' });
await page.waitForTimeout(300);
const darkProbe = await page.evaluate(() => ({
  bg: getComputedStyle(document.body).backgroundColor,
  color: getComputedStyle(document.body).color,
  scheme: getComputedStyle(document.documentElement).colorScheme,
}));
await page.emulateMedia({ colorScheme: 'light' });

await page.goto('https://docs.reown.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1800);
const docsLight = await readPage(page);
const themeBtn = page.getByRole('button', { name: 'Change theme preference' });
if (await themeBtn.count()) {
  await themeBtn.click();
  await page.waitForTimeout(400);
  const item = page.getByRole('menuitem', { name: /Dark/ });
  if (await item.count()) await item.first().click({ force: true });
  else await page.locator('[role="menu"]').getByText('Dark', { exact: true }).click({ force: true });
  await page.waitForTimeout(800);
}
const docsDark = await readPage(page);

await page.goto('https://demo.reown.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1800);
const demo = await readPage(page);

function slimRules(rules, keep) {
  return rules.filter((r) => Object.keys(r.properties).some((k) => keep(k))).map((r) => ({
    selector: r.selector,
    context: r.context,
    properties: Object.fromEntries(Object.entries(r.properties).filter(([k]) => keep(k))),
  }));
}

const out = {
  capturedAt: new Date().toISOString(),
  product: 'Reown',
  source: 'live public pages, headless Chromium, 1440x900',
  themeProbe: { prefersColorSchemeDarkOnMarketing: darkProbe, note: 'Marketing body colors did not change under prefers-color-scheme: dark.' },
  marketing: {
    url: 'https://reown.com/',
    body: home.body,
    themeClasses: home.themeClasses,
    fonts: home.fonts.slice(0, 40),
    resolved: home.resolved,
    rules: slimRules(marketingRules, (k) => k.startsWith('--p-') || k.startsWith('--s-')),
  },
  docs: {
    url: 'https://docs.reown.com/',
    light: { htmlClass: docsLight.htmlClass, body: docsLight.body, resolved: docsLight.resolved },
    dark: { htmlClass: docsDark.htmlClass, body: docsDark.body, resolved: docsDark.resolved },
    fonts: docsLight.fonts.slice(0, 20),
    rules: slimRules(docsLight.rules, (k) => /primary|background|font|radius|border/.test(k) && !k.startsWith('--tw-') && !k.startsWith('--shiki-')).slice(0, 200),
  },
  demo: {
    url: 'https://demo.reown.com/',
    body: demo.body,
    htmlClass: demo.htmlClass,
    resolved: Object.fromEntries(Object.entries(demo.resolved).filter(([k]) => k.startsWith('--apkt-') || k === '--radius' || k.startsWith('--accent'))),
    fonts: demo.fonts.slice(0, 20),
  },
  bins: {
    marketingPrimitive: Object.keys(home.resolved).filter((k) => k.startsWith('--p-')).length,
    marketingSemantic: Object.keys(home.resolved).filter((k) => k.startsWith('--s-')).length,
    docs: Object.keys(docsLight.resolved).length,
    demoAppkit: Object.keys(demo.resolved).filter((k) => k.startsWith('--apkt-')).length,
  },
};

fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 2));
console.log('wrote css-vars.json', out.bins, 'fonts', home.fonts.length);
await browser.close();
