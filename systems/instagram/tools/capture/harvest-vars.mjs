// Read Instagram's declared design tokens from the live public pages.
// Writes raw/css-vars.json. Consent layers are hidden, never clicked.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node harvest-vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, hideConsent, patch, setDark } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const OUT = path.join(REF, 'raw', 'css-vars.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });

const PAGES = [
  { key: 'light', url: 'https://www.instagram.com/', dark: false },
  { key: 'dark', url: 'https://www.instagram.com/', dark: true },
  { key: 'signup', url: 'https://www.instagram.com/accounts/emailsignup/', dark: false },
  { key: 'about', url: 'https://about.instagram.com/', dark: false },
];

const browser = await chromium.launch({ headless: true });
const out = {
  product: 'instagram',
  captured: '2026-11-19',
  note: 'Declared custom properties harvested from the CSSOM of public Instagram pages. resolved.<theme> is getComputedStyle(document.documentElement). url() values are stripped. dark is the same login wall with __ig-dark-mode forced on the root, because the signed-out login wall ships light and the signup wall ships dark; the stylesheet declares both.',
  pages: {},
  fonts: [],
  resolved: {},
};

function slimRules(rules) {
  // Keep only selectors that look like a token root, so the file stays usable.
  return rules.filter((r) => /:root|__ig-|__fb-|data-theme|data-mode/.test(r.selector)).slice(0, 80);
}

for (const spec of PAGES) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  const page = await ctx.newPage();
  console.log('harvest', spec.key, spec.url, spec.dark ? 'DARK' : '');
  await page.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(3500);
  await hideConsent(page);
  if (spec.dark) await setDark(page);
  const data = await page.evaluate(() => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/gi, 'url(…)') : v);
    const rules = [];
    const fonts = [];
    const walk = (list, ctx) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = {};
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim()).slice(0, 160);
          fonts.push(o);
          continue;
        }
        if (r.cssRules && !r.selectorText) {
          const head = r.conditionText ? '@media ' + String(r.conditionText).slice(0, 80) : (r.cssText || '').split('{')[0].trim().slice(0, 80);
          walk(r.cssRules, [...ctx, head].slice(0, 3));
          continue;
        }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (!k.startsWith('--')) continue;
          props[k] = noUrl(r.style.getPropertyValue(k).trim()).slice(0, 160);
        }
        if (Object.keys(props).length >= 8) {
          rules.push({
            selector: (r.selectorText || '').slice(0, 140),
            context: ctx.slice(0, 2),
            count: Object.keys(props).length,
            properties: props,
          });
        }
      }
    };
    for (const sheet of document.styleSheets) {
      try { if (sheet.cssRules) walk(sheet.cssRules, []); } catch { /* cross-origin */ }
    }
    const cs = getComputedStyle(document.documentElement);
    const names = new Set();
    for (const rule of rules) for (const k of Object.keys(rule.properties)) names.add(k);
    const resolved = {};
    for (const name of names) {
      const v = cs.getPropertyValue(name);
      if (v && v.trim()) resolved[name] = noUrl(v.trim()).slice(0, 160);
    }
    const loginBtn = document.querySelector('button');
    const loginCs = loginBtn ? getComputedStyle(loginBtn) : null;
    return {
      title: document.title.slice(0, 140),
      url: location.href.split('?')[0],
      htmlClass: String(document.documentElement.className).slice(0, 180),
      bodyBg: getComputedStyle(document.body).backgroundColor,
      bodyColor: getComputedStyle(document.body).color,
      bodyFont: getComputedStyle(document.body).fontFamily.slice(0, 160),
      ruleCount: rules.length,
      nameCount: names.size,
      resolvedCount: Object.keys(resolved).length,
      buttonSample: loginCs ? {
        text: (loginBtn.innerText || '').slice(0, 40),
        bg: loginCs.backgroundColor,
        color: loginCs.color,
        radius: loginCs.borderRadius,
        font: loginCs.fontFamily.slice(0, 80),
        height: loginCs.height,
      } : null,
      rules,
      fonts,
      resolved,
    };
  });
  out.pages[spec.key] = {
    url: data.url,
    title: data.title,
    htmlClass: data.htmlClass,
    bodyBg: data.bodyBg,
    bodyColor: data.bodyColor,
    bodyFont: data.bodyFont,
    ruleCount: data.ruleCount,
    nameCount: data.nameCount,
    resolvedCount: data.resolvedCount,
    buttonSample: data.buttonSample,
  };
  out.resolved[spec.key] = data.resolved;
  if (spec.key === 'light') {
    out.fonts = data.fonts.slice(0, 40);
    out.lightRules = slimRules(data.rules).map((r) => ({ selector: r.selector, count: r.count, keys: Object.keys(r.properties).slice(0, 12) }));
  }
  console.log(' ', data.htmlClass.slice(0, 60), 'rules', data.ruleCount, 'resolved', data.resolvedCount, 'bg', data.bodyBg);
  await ctx.close();
}

fs.writeFileSync(OUT, JSON.stringify(out));
console.log('wrote', OUT, 'bytes', fs.statSync(OUT).size);
await browser.close();
