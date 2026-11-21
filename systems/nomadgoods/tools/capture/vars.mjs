// Reads custom properties and computed styles from the live Nomad storefront.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// Writes raw/css-vars.json and raw/computed-roles.json. Values that cannot
// be read stay out of the token file (Not captured), never filled from memory.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, BASE, hideCookies, closeSignup } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 1 });
const page = await context.newPage();
await page.goto(BASE + '/sg/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2500);
await hideCookies(page);
await closeSignup(page);

const result = await page.evaluate(() => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const skipped = [];
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
          : r.cssText.split('{')[0].trim().slice(0, 80);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (Object.keys(props).length) rules.push({ file, selector: (r.selectorText || '').slice(0, 140), context: ctx, properties: props });
    }
  };
  [...document.styleSheets].forEach((ss, i) => {
    const file = ss.href ? ss.href.split('/').pop().split('?')[0] : `inline-${i}`;
    try { walk(ss.cssRules, [], file); } catch { skipped.push(file); }
  });
  const rootVars = {};
  const cs = getComputedStyle(document.documentElement);
  for (const k of cs) if (k.startsWith('--')) rootVars[k] = noUrl(cs.getPropertyValue(k).trim());
  return { rules, fonts, skipped, rootVars, title: document.title };
});

const names = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))].sort();
const resolved = await page.evaluate((want) => {
  const probe = document.createElement('div');
  probe.style.cssText = 'position:absolute;left:0;top:0;visibility:hidden';
  document.body.appendChild(probe);
  const norm = (c) => {
    const m = c.match(/^rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)$/);
    if (!m) return c;
    const rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v));
    const a = m[4] === undefined ? 1 : +m[4];
    return a >= 0.999 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${Math.round(a * 1000) / 1000})`;
  };
  const out = {};
  for (const name of want) {
    const raw = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    if (!raw) continue;
    const r = { raw: raw.slice(0, 240) };
    probe.style.cssText = 'position:absolute;visibility:hidden';
    if (CSS.supports('color', raw)) {
      probe.style.color = raw;
      r.kind = 'color';
      r.value = norm(getComputedStyle(probe).color);
    } else if (CSS.supports('width', raw) && !raw.includes('%')) {
      probe.style.width = raw;
      r.kind = 'dimension';
      r.value = getComputedStyle(probe).width;
    } else r.kind = 'other';
    out[name] = r;
  }
  probe.remove();
  return out;
}, names.slice(0, 400));

// Computed roles from real elements. Selectors are roles and visible text, not class hashes.
const roles = await page.evaluate(() => {
  const pick = (el) => {
    if (!el) return null;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      tag: el.tagName,
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 40),
      fontFamily: cs.fontFamily,
      fontSize: cs.fontSize,
      fontWeight: cs.fontWeight,
      lineHeight: cs.lineHeight,
      letterSpacing: cs.letterSpacing,
      color: cs.color,
      backgroundColor: cs.backgroundColor,
      borderRadius: cs.borderRadius,
      borderTopWidth: cs.borderTopWidth,
      borderTopColor: cs.borderTopColor,
      padding: `${cs.paddingTop} ${cs.paddingRight} ${cs.paddingBottom} ${cs.paddingLeft}`,
      height: Math.round(r.height) + 'px',
      boxShadow: cs.boxShadow === 'none' ? 'none' : cs.boxShadow.slice(0, 120),
    };
  };
  const byLabel = (sel, label) => [...document.querySelectorAll(sel)].find((el) => {
    const t = (el.innerText || el.getAttribute('aria-label') || '');
    return t.includes(label) && el.getBoundingClientRect().width > 0;
  });
  const body = document.body;
  const header = document.querySelector('header') || document.querySelector('[class*=header]');
  const shop = [...document.querySelectorAll('a, button')].find((el) => (el.innerText || '').trim() === 'Shop Now' && el.getBoundingClientRect().width > 40);
  const nav = byLabel('a', 'Best Sellers');
  const sale = [...document.querySelectorAll('a')].find((el) => (el.innerText || '').trim() === 'Sale' && el.getBoundingClientRect().top < 120);
  const h1 = document.querySelector('h1');
  return {
    viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
    body: pick(body),
    header: pick(header),
    h1: pick(h1),
    shopNow: pick(shop),
    navLink: pick(nav),
    saleLink: pick(sale),
    announcement: pick(document.querySelector('header a, [class*=announcement] a') || [...document.querySelectorAll('a')].find((a) => /Black Friday/i.test(a.innerText || ''))),
  };
});

fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
  readAt: new Date().toISOString().slice(0, 10),
  source: 'live CSSOM on nomadgoods.com/sg/ at 1440x900, signed out',
  title: result.title,
  sheetsSkippedCrossOrigin: result.skipped,
  ruleCount: result.rules.length,
  fontFaceCount: result.fonts.length,
  customPropertyNames: names,
  rootVarCount: Object.keys(result.rootVars).length,
  resolved,
  fonts: result.fonts.slice(0, 40),
  sampleRules: result.rules.slice(0, 30),
}, null, 2) + '\n');
fs.writeFileSync(path.join(RAW, 'computed-roles.json'), JSON.stringify(roles, null, 2) + '\n');
console.log('rules', result.rules.length, 'names', names.length, 'fonts', result.fonts.length, 'skipped', result.skipped.length);
console.log('roles', JSON.stringify(roles, null, 2).slice(0, 2500));
await browser.close();
