// Reads Fourthwall's public CSS custom properties and computed styles from
// the live page. Nothing is typed or submitted.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node tools/capture/public/read-css.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(HERE, '..', '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
await context.route(/onetrust|cookielaw|cookiebot/i, (route) => route.abort());
const page = await context.newPage();
await page.goto('https://fourthwall.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2000);
await page.locator('.nav-link', { hasText: 'Features' }).first().hover().catch(() => {});
await page.waitForTimeout(400);

const reading = await page.evaluate(() => {
  const vars = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list, context) => {
      for (const rule of list) {
        if (rule.type === CSSRule.STYLE_RULE) {
          const props = {};
          for (const name of rule.style) {
            if (name.startsWith('--')) props[name] = rule.style.getPropertyValue(name).trim();
          }
          if (Object.keys(props).length) vars.push({ selector: rule.selectorText, context, properties: props, href: sheet.href });
        } else if (rule.cssRules) {
          const ctx = rule.conditionText ? [...context, rule.conditionText] : context;
          walk(rule.cssRules, ctx);
        }
      }
    };
    if (rules) walk(rules, []);
  }
  const rootStyle = getComputedStyle(document.documentElement);
  const resolved = {};
  const names = new Set();
  for (const block of vars) for (const name of Object.keys(block.properties)) names.add(name);
  for (const name of names) resolved[name] = rootStyle.getPropertyValue(name).trim();

  function pick(sel) {
    const el = document.querySelector(sel);
    if (!el) return null;
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      selector: sel,
      text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60),
      rect: { w: Math.round(r.width), h: Math.round(r.height) },
      color: s.color,
      backgroundColor: s.backgroundColor,
      borderTopColor: s.borderTopColor,
      borderTopWidth: s.borderTopWidth,
      borderRadius: s.borderRadius,
      fontFamily: s.fontFamily,
      fontSize: s.fontSize,
      fontWeight: s.fontWeight,
      lineHeight: s.lineHeight,
      letterSpacing: s.letterSpacing,
      padding: `${s.paddingTop} ${s.paddingRight} ${s.paddingBottom} ${s.paddingLeft}`,
      boxShadow: s.boxShadow,
      textDecoration: s.textDecorationLine,
    };
  }
  const selectors = {
    body: 'body',
    nav: '.nav-bar',
    navLink: '.nav-link',
    login: '.nav-login',
    cta: '.btn-primary',
    footer: 'footer',
    footerLink: 'footer a',
    heading: 'h1',
    h2: 'h2',
    paragraph: 'main p, .hero p, p',
    mega: '.nav-dropdown .mega-link',
  };
  const computed = {};
  for (const [k, sel] of Object.entries(selectors)) computed[k] = pick(sel);
  const fonts = [...document.fonts].slice(0, 40).map((f) => ({ family: f.family, weight: f.weight, style: f.style, status: f.status }));
  return {
    title: document.title,
    varCount: names.size,
    vars,
    resolved,
    computed,
    fonts,
    theme: {
      colorScheme: rootStyle.colorScheme,
      dataTheme: document.documentElement.getAttribute('data-theme'),
      className: document.documentElement.className,
    },
  };
});

fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
  source: 'live https://fourthwall.com/ on 2026-11-21, signed out, desktop 1440',
  theme: reading.theme,
  varCount: reading.varCount,
  vars: reading.vars,
  resolved: reading.resolved,
  fonts: reading.fonts,
}, null, 2) + '\n');
fs.writeFileSync(path.join(RAW, 'computed-home.json'), JSON.stringify(reading.computed, null, 2) + '\n');
console.log('vars', reading.varCount, 'rules', reading.vars.length, 'theme', JSON.stringify(reading.theme));
console.log(JSON.stringify(reading.computed, null, 2).slice(0, 2500));
await browser.close();
