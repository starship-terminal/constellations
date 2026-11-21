// Read custom properties and computed role colours from the live public sites.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
//
// glassnode.com (marketing) and studio.glassnode.com (public shell) both
// paint one light theme. Stylesheet bodies are captured from network
// responses and re-parsed. Computed role colours are read from real
// elements, because Ant Design often does not expose :root custom
// properties until a theme algorithm runs.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});

async function harvest(url) {
  const page = await context.newPage();
  const bodies = new Map();
  page.on('response', async (r) => {
    const t = r.request().resourceType();
    if (t !== 'stylesheet' && !/\.css(\?|$)/.test(r.url())) return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
  });
  await page.goto(url, { waitUntil: 'load', timeout: 70000 });
  await page.waitForTimeout(3000);
  await page.evaluate(() => {
    const sr = document.querySelector('#usercentrics-root')?.shadowRoot;
    const deny = sr && [...sr.querySelectorAll('button')].find((b) => /^Deny$/i.test((b.innerText || '').trim()));
    if (deny) deny.click();
  });
  const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
    try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
  }).filter(Boolean));
  const computed = await page.evaluate(() => {
    const pick = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const s = getComputedStyle(el);
      return {
        selector: sel,
        text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40),
        color: s.color,
        backgroundColor: s.backgroundColor,
        borderTopColor: s.borderTopColor,
        borderTopWidth: s.borderTopWidth,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        borderRadius: s.borderRadius,
        padding: s.padding,
        height: s.height,
        boxShadow: s.boxShadow,
      };
    };
    const root = getComputedStyle(document.documentElement);
    const vars = [];
    for (let i = 0; i < root.length; i++) {
      const n = root[i];
      if (n.startsWith('--')) vars.push([n, root.getPropertyValue(n).trim().slice(0, 160)]);
    }
    return {
      href: location.href.split('?')[0],
      title: document.title,
      colorScheme: root.colorScheme,
      htmlClass: document.documentElement.className,
      bodyBg: getComputedStyle(document.body).backgroundColor,
      bodyColor: getComputedStyle(document.body).color,
      bodyFont: getComputedStyle(document.body).fontFamily,
      rootVarCount: vars.length,
      rootVars: vars.slice(0, 40),
      samples: {
        h1: pick('h1'),
        primary: pick('button.ant-btn-primary, a[class*="primary"], button[class*="primary"]'),
        link: pick('a'),
        input: pick('input[type="text"], input[type="search"], input[type="email"]'),
      },
    };
  });
  await page.close();
  return { url, sheets: [...bodies.entries()], inline, computed };
}

const marketing = await harvest('https://glassnode.com/');
const studio = await harvest('https://studio.glassnode.com/');
const pricing = await harvest('https://studio.glassnode.com/pricing');

const sheets = [];
for (const src of [marketing, studio, pricing]) {
  for (const [name, text] of src.sheets) sheets.push([src.computed.href + ' :: ' + name, text]);
  for (const pair of src.inline) sheets.push([src.computed.href + ' :: ' + pair[0], pair[1]]);
}

const probe = await browser.newPage();
const parsed = await probe.evaluate((list) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (cssRules, ctx, file) => {
    for (const r of cssRules) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : (r.cssText || '').split('{')[0].trim().slice(0, 80);
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
      if (n) rules.push({ file: file.slice(0, 180), selector: (r.selectorText || '').slice(0, 160), context: ctx.slice(0, 4), properties: props });
    }
  };
  for (const [name, text] of list) {
    if (!text || text.length > 4_000_000) { errors.push({ file: name.slice(0, 120), error: 'skipped size' }); continue; }
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name.slice(0, 120), error: String(e).slice(0, 160) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets.map(([n, t]) => [n, t]));

const names = [...new Set(parsed.rules.flatMap((r) => Object.keys(r.properties)))].filter((n) => n.startsWith('--ant-') || n.startsWith('--gn-') || n.startsWith('--color') || n.startsWith('--font')).sort();
await probe.setContent('<!doctype html><html><head></head><body></body></html>');
// Resolve only names that the live document actually computed. The harvest
// pages already closed, so resolve from a fresh studio load.
const live = await context.newPage();
await live.goto('https://studio.glassnode.com/', { waitUntil: 'load', timeout: 70000 });
await live.waitForTimeout(2500);
const resolved = await live.evaluate((want) => {
  const root = getComputedStyle(document.documentElement);
  const out = {};
  for (const name of want) {
    const raw = root.getPropertyValue(name).trim();
    if (raw) out[name] = raw.slice(0, 200);
  }
  // Ant tokens often live on a nested theme holder, not :root.
  const holders = [...document.querySelectorAll('[class*="css-var"], [style*="--ant"], .ant-app, #__next, body')];
  let best = null;
  let bestN = 0;
  for (const el of holders) {
    const s = getComputedStyle(el);
    let n = 0;
    for (const name of want) if (s.getPropertyValue(name).trim()) n++;
    if (n > bestN) { bestN = n; best = el; }
  }
  const holder = {};
  if (best) {
    const s = getComputedStyle(best);
    for (const name of want) {
      const raw = s.getPropertyValue(name).trim();
      if (raw) holder[name] = raw.slice(0, 200);
    }
  }
  return { root: out, holderCount: bestN, holder: Object.fromEntries(Object.entries(holder).slice(0, 400)), holderKeys: Object.keys(holder).length };
}, names);
await live.close();
await browser.close();

const binOf = (r) => {
  const ns = Object.keys(r.properties);
  if (ns.every((n) => n.startsWith('--ant-'))) return 'theme';
  if (ns.every((n) => n.startsWith('--tw-'))) return 'tailwind';
  if (/usercentrics|uc-|osano|intercom|hubspot/i.test(r.file + r.selector)) return 'vendor';
  return 'app';
};
for (const r of parsed.rules) r.bin = binOf(r);
const byBin = (bin) => parsed.rules.filter((r) => r.bin === bin);

const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'stylesheet bodies from live loads of https://glassnode.com/, https://studio.glassnode.com/ and https://studio.glassnode.com/pricing, re-parsed with CSSStyleSheet; computed role samples from those pages. One light theme. Headless Chromium, signed out. 2026-11-21.',
  counts: {
    rules: parsed.rules.length,
    fonts: parsed.fonts.length,
    names: names.length,
    theme: byBin('theme').length,
    app: byBin('app').length,
    vendor: byBin('vendor').length,
  },
  errors: parsed.errors.slice(0, 20),
  computed: {
    marketing: marketing.computed,
    studio: studio.computed,
    pricing: pricing.computed,
  },
  resolved: resolved,
  fonts: parsed.fonts.slice(0, 40),
  theme: byBin('theme').slice(0, 80),
  app: byBin('app').slice(0, 40),
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('rules', out.counts, 'resolved holder', resolved.holderKeys, 'root', Object.keys(resolved.root).length);
