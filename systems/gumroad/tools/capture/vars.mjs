// Read every custom property gumroad.com declares and write raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// gumroad.com follows prefers-color-scheme. The same names are resolved twice:
// once with colorScheme light, once with colorScheme dark. Login stays light.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const browser = await chromium.launch({ headless: true });

async function harvest(colorScheme) {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    userAgent: UA,
    locale: 'en-US',
    colorScheme,
  });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  const page = await context.newPage();
  await page.goto('https://gumroad.com/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2500);
  const sheets = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
    try {
      return { name: s.href || 'inline-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') };
    } catch {
      return { name: s.href || 'sheet-' + i, media: '', css: '', unreadable: true };
    }
  }));
  const painted = await page.evaluate(() => ({
    bodyBg: getComputedStyle(document.body).backgroundColor,
    bodyColor: getComputedStyle(document.body).color,
    scheme: getComputedStyle(document.documentElement).colorScheme,
  }));
  await context.close();
  return { sheets, painted };
}

const light = await harvest('light');
const dark = await harvest('dark');

const probe = await browser.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : (r.cssText || '').split('{')[0].trim().slice(0, 120);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
      }
      if (n) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], file);
    }
  };
  for (const s of sheets) {
    if (!s.css) { if (s.unreadable) errors.push({ file: s.name, error: 'cross-origin to the CSSOM' }); continue; }
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e).slice(0, 180) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts, errors };
}, light.sheets);
await probe.close();

async function resolve(colorScheme, sheets) {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    userAgent: UA,
    locale: 'en-US',
    colorScheme,
  });
  const page = await context.newPage();
  await page.goto('https://gumroad.com/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1500);
  const names = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
    .filter((n) => !n.startsWith('--tw-') && !n.startsWith('--radix')).sort();
  const resolved = await page.evaluate((names) => {
    const root = getComputedStyle(document.documentElement);
    const probe = document.createElement('div');
    probe.style.cssText = 'position:absolute;left:0;top:0';
    document.body.appendChild(probe);
    const out = {};
    const hex = (c) => {
      const m = c.match(/^rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)$/);
      if (!m) return c;
      const rgb = [m[1], m[2], m[3]].map((v) => (+v).toString(16).padStart(2, '0')).join('');
      const a = m[4] === undefined ? 1 : +m[4];
      return a === 1 ? '#' + rgb : `rgba(${m[1]}, ${m[2]}, ${m[3]}, ${a})`;
    };
    for (const name of names) {
      const raw = root.getPropertyValue(name).trim();
      if (!raw) continue;
      const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
      probe.removeAttribute('style');
      probe.style.cssText = 'position:absolute;left:0;top:0';
      if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)/.test(raw)) {
        probe.style.color = raw;
        r.kind = 'color';
        r.value = hex(getComputedStyle(probe).color);
      } else if (CSS.supports('width', raw) && /px|rem|em/.test(raw) && !raw.includes(' ')) {
        probe.style.width = raw;
        r.kind = 'dimension';
        r.value = getComputedStyle(probe).width;
      } else {
        r.kind = 'other';
        r.value = raw.length > 240 ? raw.slice(0, 240) + '…' : raw;
      }
      out[name] = r;
    }
    probe.remove();
    return out;
  }, names);
  await context.close();
  return resolved;
}

const resolvedLight = await resolve('light', light.sheets);
const resolvedDark = await resolve('dark', dark.sheets);
await browser.close();

const GUM = /^--(color-|body-|accent|black|border|button-|box-shadow|breakpoint|font-|spacer|active-bg|pink|danger|success|warning|info)/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (names.every((n) => n.startsWith('--tw-') || n.startsWith('--container-'))) return 'utility';
  if (names.some((n) => GUM.test(n))) return 'token';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();

const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'gumroad.com home page stylesheets, read through the CSSOM. Resolved twice: prefers-color-scheme light and dark. Login is not themed.',
  painted: { light: light.painted, dark: dark.painted },
  sheets: light.sheets.map(({ name, media, css }) => ({ name: (name || '').slice(0, 180), media, bytes: (css || '').length, unreadable: !css })),
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: { token: names('token').length, app: names('app').length, utility: names('utility').length },
  },
  errors: result.errors,
  fonts: result.fonts.map((f) => ({ ...f, src: f.src ? 'url(…)' : f.src })),
  resolved: { light: resolvedLight, dark: resolvedDark },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('rules', result.rules.length, 'fonts', result.fonts.length);
console.log('resolved light', Object.keys(resolvedLight).length, 'dark', Object.keys(resolvedDark).length);
console.log('painted', JSON.stringify(out.painted));
