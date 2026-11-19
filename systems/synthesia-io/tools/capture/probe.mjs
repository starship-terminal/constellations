// Second pass: stylesheet text, component states, login wall, icons.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..');
const RAW = path.join(PKG, 'raw');
const SHOTS = path.join(PKG, 'screenshots');
const CROPS = path.join(PKG, 'components', 'crops');
const ICONS = path.join(PKG, 'icons');
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(ICONS, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();

await page.goto('https://www.synthesia.io/', { waitUntil: 'load', timeout: 90000 });
await page.waitForTimeout(4000);

const cssHrefs = await page.evaluate(() => [...document.styleSheets].map((s) => s.href).filter(Boolean));
const cssText = {};
for (const href of cssHrefs) {
  const res = await page.request.get(href);
  cssText[href] = await res.text();
}
const declared = {};
const re = /(--[A-Za-z0-9_-]+)\s*:\s*([^;}+]+)/g;
for (const [href, text] of Object.entries(cssText)) {
  let m;
  const local = re;
  local.lastIndex = 0;
  while ((m = local.exec(text))) {
    const name = m[1];
    const value = m[2].trim();
    if (!declared[name]) declared[name] = { value, href: href.split('/').pop() };
  }
}

const names = Object.keys(declared);
const resolved = await page.evaluate((names) => {
  const cs = getComputedStyle(document.documentElement);
  const out = {};
  for (const n of names) {
    const v = cs.getPropertyValue(n).trim();
    if (v) out[n] = v;
  }
  // Also any inline custom props.
  for (const p of document.documentElement.style) {
    if (p.startsWith('--')) out[p] = document.documentElement.style.getPropertyValue(p).trim();
  }
  return {
    resolved: out,
    colorScheme: cs.colorScheme,
    reduced: matchMedia('(prefers-reduced-motion: reduce)').matches,
    inlineCount: document.documentElement.style.length,
  };
}, names);

fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
  source: 'stylesheet text from cdn.prod.website-files.com on https://www.synthesia.io/ plus getComputedStyle resolution, headless Chromium 1440x900 @2x, 2026-11-19',
  sheets: cssHrefs,
  declared,
  resolved: resolved.resolved,
  colorScheme: resolved.colorScheme,
  reducedMotion: resolved.reduced,
}, null, 2));
console.log('declared', Object.keys(declared).length, 'resolved', Object.keys(resolved.resolved).length);

const styleOf = (el) => {
  const s = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  return {
    text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 80),
    cls: String(el.className || '').slice(0, 120),
    bg: s.backgroundColor, color: s.color, font: s.fontFamily, size: s.fontSize,
    weight: s.fontWeight, lh: s.lineHeight, ls: s.letterSpacing, radius: s.borderRadius,
    bw: s.borderTopWidth, bc: s.borderTopColor, pad: s.padding, shadow: s.boxShadow,
    outline: `${s.outlineWidth} ${s.outlineStyle} ${s.outlineColor}`,
    w: +r.width.toFixed(1), h: +r.height.toFixed(1), x: +r.x.toFixed(1), y: +r.y.toFixed(1),
  };
};

async function crop(locator, file) {
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return false;
  const pad = 6;
  await locator.screenshot({ path: path.join(CROPS, file) }).catch(async () => {
    await page.screenshot({
      path: path.join(CROPS, file),
      clip: {
        x: Math.max(0, box.x - pad),
        y: Math.max(0, box.y - pad),
        width: box.width + pad * 2,
        height: box.height + pad * 2,
      },
    });
  });
  return true;
}

const states = {};
const primary = page.locator('nav a.button.is-small').filter({ hasText: 'Get started' }).first();
states.buttonPrimaryDefault = await primary.evaluate(styleOf);
await crop(primary, 'button-primary-default.png');
await primary.hover();
await page.waitForTimeout(300);
states.buttonPrimaryHover = await primary.evaluate(styleOf);
await crop(primary, 'button-primary-hover.png');
await primary.focus();
await page.waitForTimeout(200);
states.buttonPrimaryFocus = await primary.evaluate(styleOf);
await crop(primary, 'button-primary-focus.png');

const login = page.locator('nav a').filter({ hasText: /^Log in$/ }).first();
states.loginDefault = await login.evaluate(styleOf);
await crop(login, 'link-login-default.png');
await login.hover();
await page.waitForTimeout(250);
states.loginHover = await login.evaluate(styleOf);
await crop(login, 'link-login-hover.png');

const h1 = page.locator('h1').first();
states.h1 = await h1.evaluate(styleOf);
await crop(h1, 'heading-hero-default.png');

const nav = page.locator('nav.navbar').first();
states.nav = await nav.evaluate(styleOf);
await page.screenshot({ path: path.join(SHOTS, 'home-light-default.png'), fullPage: false });

// Pricing cards
await page.goto('https://www.synthesia.io/pricing', { waitUntil: 'load', timeout: 90000 });
await page.waitForTimeout(3000);
const pricing = await page.evaluate(() => {
  const cards = [...document.querySelectorAll('[class*="pricing"], [class*="plan"]')].slice(0, 20).map((el) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      cls: String(el.className).slice(0, 100),
      text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 100),
      bg: s.backgroundColor, color: s.color, radius: s.borderRadius, shadow: s.boxShadow,
      w: +r.width.toFixed(1), h: +r.height.toFixed(1), y: +r.y.toFixed(1),
    };
  });
  const prices = [...document.querySelectorAll('h2, h3, [class*="price"], [class*="heading"]')].slice(0, 16).map((el) => ({
    tag: el.tagName, cls: String(el.className).slice(0, 80),
    text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60),
    size: getComputedStyle(el).fontSize, weight: getComputedStyle(el).fontWeight, color: getComputedStyle(el).color,
  }));
  return { title: document.title, h1: document.querySelector('h1')?.innerText, cards, prices };
});
fs.writeFileSync(path.join(RAW, 'pricing.json'), JSON.stringify(pricing, null, 2));
await page.screenshot({ path: path.join(SHOTS, 'pricing-light-default.png') });
const priceCard = page.locator('[class*="pricing_card"], [class*="plan-card"], [class*="pricing-card"]').first();
if (await priceCard.count()) {
  states.pricingCard = await priceCard.evaluate(styleOf);
  await crop(priceCard, 'card-pricing-default.png');
}

// Book demo form: measure fields, do not submit.
await page.goto('https://www.synthesia.io/book-a-demo', { waitUntil: 'load', timeout: 90000 });
await page.waitForTimeout(3000);
const form = await page.evaluate(() => {
  return [...document.querySelectorAll('input, textarea, select, button')].slice(0, 40).map((el) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      tag: el.tagName.toLowerCase(), type: el.type || null, name: el.name || null,
      placeholder: el.placeholder || null, label: el.getAttribute('aria-label'),
      required: !!el.required, text: (el.innerText || '').trim().slice(0, 40),
      bg: s.backgroundColor, color: s.color, border: s.borderTopColor, bw: s.borderTopWidth,
      radius: s.borderRadius, pad: s.padding, size: s.fontSize, shadow: s.boxShadow,
      w: +r.width.toFixed(1), h: +r.height.toFixed(1),
    };
  });
});
fs.writeFileSync(path.join(RAW, 'book-demo-fields.json'), JSON.stringify(form, null, 2));
const field = page.locator('input:visible').first();
if (await field.count()) {
  states.fieldDefault = await field.evaluate(styleOf);
  await crop(field, 'field-text-default.png');
  await field.focus();
  await page.waitForTimeout(200);
  states.fieldFocus = await field.evaluate(styleOf);
  await crop(field, 'field-text-focus.png');
}
await page.screenshot({ path: path.join(SHOTS, 'book-demo-light-default.png') });

// Login wall, wait for navigation to settle. Do not type.
const loginPage = await context.newPage();
try {
  const res = await loginPage.goto('https://app.synthesia.io/welcome', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await loginPage.waitForTimeout(5000);
  const info = await loginPage.evaluate(() => ({
    url: location.href,
    title: document.title,
    text: (document.body?.innerText || '').replace(/\s+/g, ' ').slice(0, 900),
    challenge: /just a moment|cf-challenge|Attention Required|cloudflare/i.test((document.title || '') + (document.body?.innerText || '').slice(0, 400)),
    controls: [...document.querySelectorAll('input, button, a')].slice(0, 40).map((el) => ({
      tag: el.tagName.toLowerCase(), type: el.type || null,
      text: (el.innerText || el.placeholder || el.getAttribute('aria-label') || '').trim().slice(0, 70),
    })),
  }));
  info.status = res ? res.status() : null;
  fs.writeFileSync(path.join(RAW, 'login-wall.json'), JSON.stringify(info, null, 2));
  if (!info.challenge) {
    await loginPage.screenshot({ path: path.join(SHOTS, 'login-light-signed-out.png') });
  }
  console.log('login', info.status, info.url, 'challenge', info.challenge, info.title);
} catch (e) {
  fs.writeFileSync(path.join(RAW, 'login-wall.json'), JSON.stringify({ error: String(e).split('\n')[0] }, null, 2));
  console.log('login error', String(e).split('\n')[0]);
}

// Inline SVG icons from home.
await page.goto('https://www.synthesia.io/', { waitUntil: 'load', timeout: 90000 });
await page.waitForTimeout(2000);
const icons = await page.evaluate(() => {
  const seen = new Set();
  const out = [];
  for (const svg of document.querySelectorAll('svg')) {
    const r = svg.getBoundingClientRect();
    if (r.width < 8 || r.width > 48 || r.height < 8 || r.height > 48) continue;
    const clone = svg.cloneNode(true);
    clone.querySelectorAll('*').forEach((n) => {
      [...n.attributes].forEach((a) => { if (a.name.startsWith('data-') || a.name === 'class') n.removeAttribute(a.name); });
    });
    const html = clone.outerHTML;
    if (html.length > 4000 || seen.has(html)) continue;
    seen.add(html);
    const host = svg.closest('a, button') || svg.parentElement;
    out.push({
      label: (host?.getAttribute('aria-label') || host?.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40),
      w: +r.width.toFixed(1), h: +r.height.toFixed(1),
      html,
    });
    if (out.length >= 24) break;
  }
  return out;
});
const index = ['file\trole\twidth\theight'];
icons.forEach((icon, i) => {
  const file = `icon-${String(i + 1).padStart(2, '0')}.svg`;
  fs.writeFileSync(path.join(ICONS, file), icon.html);
  index.push(`${file}\t${icon.label || 'unlabeled'}\t${icon.w}\t${icon.h}`);
});
fs.writeFileSync(path.join(ICONS, 'INDEX.tsv'), index.join('\n') + '\n');
fs.writeFileSync(path.join(RAW, 'states.json'), JSON.stringify(states, null, 2));
console.log('icons', icons.length, 'states', Object.keys(states));

await browser.close();
