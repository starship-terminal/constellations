// Reads computed styles and custom properties from Hello Ivy's public pages.
// Writes raw/readings.json. Does not submit forms or open OAuth.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node read.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, patch, hideOverlays, openMenu, closeMenu, UA, BASE, PROPS } from './lib.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(HERE, '..', '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
await patch(ctx);
const page = await ctx.newPage();

async function go(url) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2000);
  await hideOverlays(page);
}

function pick(style, keys) {
  const o = {};
  for (const k of keys) o[k] = style[k];
  return o;
}

await go(BASE + '/');
const home = await page.evaluate((props) => {
  const vis = (el) => {
    if (!el) return false;
    const r = el.getBoundingClientRect();
    const s = getComputedStyle(el);
    return r.width > 2 && r.height > 2 && s.display !== 'none' && s.visibility !== 'hidden' && Number(s.opacity) > 0.05;
  };
  const styleOf = (el) => {
    const s = getComputedStyle(el);
    const o = {};
    for (const k of props) o[k] = s[k];
    const r = el.getBoundingClientRect();
    o.rect = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    return o;
  };
  const text = (el) => (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80);
  const byText = (sel, re) => [...document.querySelectorAll(sel)].find((el) => vis(el) && re.test(text(el)));
  const painted = (el) => {
    if (!el) return null;
    const label = [...el.querySelectorAll('p, span, h1, h2, h3')].find((n) => vis(n) && text(n));
    return label || el;
  };
  const h1 = document.querySelector('h1');
  const navLink = byText('a', /^Features$/);
  const login = byText('a', /^Log in$/);
  const ctaA = byText('a', /^Get Started$/);
  const tryA = byText('a', /Try it for free/);
  const cta = painted(ctaA);
  const tryFree = painted(tryA);
  const intro = [...document.querySelectorAll('p')].find((el) => vis(el) && /constantly juggling/.test(text(el)));
  const body = document.body;
  const root = document.documentElement;
  const rootStyle = getComputedStyle(root);
  const vars = {};
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const r of list || []) {
        if (r.style) {
          for (let i = 0; i < r.style.length; i++) {
            const k = r.style[i];
            if (k.startsWith('--') && !(k in vars)) vars[k] = r.style.getPropertyValue(k).trim().slice(0, 180);
          }
        }
        if (r.cssRules) walk(r.cssRules);
      }
    };
    walk(rules);
  }
  const fonts = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const r of list || []) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          fonts.push({
            family: r.style.getPropertyValue('font-family'),
            weight: r.style.getPropertyValue('font-weight'),
            style: r.style.getPropertyValue('font-style'),
            src: (r.style.getPropertyValue('src') || '').slice(0, 120),
          });
        }
        if (r.cssRules) walk(r.cssRules);
      }
    };
    walk(rules);
  }
  // Motion: first transition that is not "all 0s".
  let motion = null;
  for (const el of document.querySelectorAll('a, button')) {
    const s = getComputedStyle(el);
    if (s.transitionDuration && s.transitionDuration !== '0s') {
      motion = { duration: s.transitionDuration, easing: s.transitionTimingFunction, property: s.transitionProperty, sample: text(el) };
      break;
    }
  }
  return {
    url: location.href,
    title: document.title,
    toggleTheme: root.getAttribute('toggle-theme'),
    colorScheme: rootStyle.colorScheme,
    bg: rootStyle.backgroundColor,
    bodyBg: getComputedStyle(body).backgroundColor,
    bodyColor: getComputedStyle(body).color,
    bodyFont: getComputedStyle(body).fontFamily,
    bodySize: getComputedStyle(body).fontSize,
    varCount: Object.keys(vars).length,
    varSample: Object.fromEntries(Object.entries(vars).slice(0, 30)),
    fontFaces: fonts.slice(0, 20),
    motion,
    h1: h1 ? styleOf(h1) : null,
    h1Text: h1 ? text(h1) : '',
    navLink: navLink ? styleOf(navLink) : null,
    login: login ? styleOf(login) : null,
    cta: cta ? styleOf(cta) : null,
    ctaBox: ctaA ? styleOf(ctaA) : null,
    tryFree: tryFree ? styleOf(tryFree) : null,
    tryBox: tryA ? styleOf(tryA) : null,
    intro: intro ? styleOf(intro) : null,
    viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
  };
}, PROPS);

await openMenu(page);
await page.waitForTimeout(500);
const menu = await page.evaluate((props) => {
  const styleOf = (el) => {
    const s = getComputedStyle(el);
    const o = {};
    for (const k of props) o[k] = s[k];
    const r = el.getBoundingClientRect();
    o.rect = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    o.text = (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40);
    return o;
  };
  const links = [...document.querySelectorAll('a')].filter((a) => /HOME|FEATURES|Free Trial/.test((a.innerText || '').replace(/\s+/g, ' ')));
  const home = links.find((a) => /HOME/.test(a.innerText));
  const trial = links.find((a) => /Free Trial/.test(a.innerText));
  const trialLabel = trial && [...trial.querySelectorAll('p, span')].find((n) => /Free Trial/.test(n.innerText || ''));
  const homeLabel = home && [...home.querySelectorAll('p, span, h1, h2')].find((n) => /HOME/.test(n.innerText || ''));
  return {
    overflow: getComputedStyle(document.documentElement).overflow,
    home: homeLabel ? styleOf(homeLabel) : (home ? styleOf(home) : null),
    trial: trialLabel ? styleOf(trialLabel) : (trial ? styleOf(trial) : null),
    trialBox: trial ? styleOf(trial) : null,
  };
}, PROPS);
await closeMenu(page);

await go(BASE + '/pricing');
const pricing = await page.evaluate((props) => {
  const styleOf = (el) => {
    const s = getComputedStyle(el);
    const o = {};
    for (const k of props) o[k] = s[k];
    const r = el.getBoundingClientRect();
    o.rect = { w: Math.round(r.width), h: Math.round(r.height) };
    o.text = (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60);
    return o;
  };
  const h1s = [...document.querySelectorAll('h1, h2')].slice(0, 6).map(styleOf);
  const ctas = [...document.querySelectorAll('a')].filter((a) => /Try for Free|Let's Talk/.test((a.innerText || '').replace(/\s+/g, ' ').trim())).slice(0, 4).map(styleOf);
  return { h1s, ctas, title: document.title };
}, PROPS);

await go('https://app.helloivy.co/login');
const login = await page.evaluate((props) => {
  const styleOf = (el) => {
    if (!el) return null;
    const s = getComputedStyle(el);
    const o = {};
    for (const k of props) o[k] = s[k];
    const r = el.getBoundingClientRect();
    o.rect = { w: Math.round(r.width), h: Math.round(r.height) };
    return o;
  };
  const email = document.querySelector('input[type="email"]');
  const password = document.querySelector('input[type="password"]');
  const cont = [...document.querySelectorAll('button')].find((b) => /Continue/.test(b.innerText || ''));
  const google = [...document.querySelectorAll('button')].find((b) => /Google/.test(b.innerText || ''));
  const card = email && email.closest('form, div');
  return {
    url: location.href,
    title: document.title,
    bodyBg: getComputedStyle(document.body).backgroundColor,
    bodyFont: getComputedStyle(document.body).fontFamily,
    bodyColor: getComputedStyle(document.body).color,
    email: styleOf(email),
    password: styleOf(password),
    continueBtn: styleOf(cont),
    googleBtn: styleOf(google),
    card: card ? styleOf(card) : null,
    h1: styleOf(document.querySelector('h1')),
  };
}, PROPS);

const out = {
  capturedAt: new Date().toISOString(),
  product: 'Hello Ivy',
  source: 'https://www.helloivy.co/',
  home, menu, pricing, login,
};
fs.writeFileSync(path.join(RAW, 'readings.json'), JSON.stringify(out, null, 2) + '\n');
console.log('wrote', path.join(RAW, 'readings.json'));
console.log('vars', home.varCount, 'h1', home.h1 && home.h1.fontSize, home.h1 && home.h1.fontFamily);
console.log('body', home.bodyBg, home.bodyColor, home.bodyFont);
console.log('cta', home.cta && home.cta.backgroundColor, home.cta && home.cta.color, home.cta && home.cta.borderRadius, home.cta && home.cta.fontSize);
console.log('login font', login.bodyFont, 'btn', login.continueBtn && login.continueBtn.backgroundColor);
await browser.close();
