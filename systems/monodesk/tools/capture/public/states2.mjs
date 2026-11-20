// Second pass: pick the painted control, not the text node inside it.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const CROPS = path.join(PKG, 'components', 'crops');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(CROPS, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

function hex(c) {
  const m = String(c || '').match(/rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:[,\s/]+([\d.]+))?\s*\)/);
  if (!m) return c;
  const h = (n) => Math.round(Number(n)).toString(16).padStart(2, '0');
  const a = m[4] === undefined ? 1 : Number(m[4]);
  if (a >= 0.999) return `#${h(m[1])}${h(m[2])}${h(m[3])}`;
  return `rgba(${Math.round(+m[1])}, ${Math.round(+m[2])}, ${Math.round(+m[3])}, ${Math.round(a * 1000) / 1000})`;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('CSS.enable').catch(() => {});
const out = {};

async function styleOf(el) {
  return el.evaluate((node) => {
    const cs = getComputedStyle(node);
    const r = node.getBoundingClientRect();
    return {
      tag: node.tagName,
      className: String(node.className || '').slice(0, 80),
      text: (node.innerText || '').trim().slice(0, 40),
      fontFamily: cs.fontFamily, fontSize: cs.fontSize, fontWeight: cs.fontWeight,
      lineHeight: cs.lineHeight, letterSpacing: cs.letterSpacing,
      color: cs.color, backgroundColor: cs.backgroundColor,
      borderRadius: cs.borderRadius,
      border: `${cs.borderTopWidth} ${cs.borderTopStyle} ${cs.borderTopColor}`,
      padding: cs.padding, boxShadow: cs.boxShadow, outline: cs.outline,
      transform: cs.transform, opacity: cs.opacity,
      w: Math.round(r.width), h: Math.round(r.height),
    };
  });
}

function clean(s) {
  if (!s) return s;
  for (const k of ['color', 'backgroundColor']) s[k] = hex(s[k]);
  s.border = s.border.replace(/rgb\([^)]+\)/g, (m) => hex(m));
  return s;
}

async function crop(el, name, pad = 10) {
  const box = await el.boundingBox();
  if (!box) return;
  await el.scrollIntoViewIfNeeded().catch(() => {});
  const b2 = await el.boundingBox();
  await page.screenshot({
    path: path.join(CROPS, `${name}.png`),
    clip: {
      x: Math.max(0, b2.x - pad),
      y: Math.max(0, b2.y - pad),
      width: Math.min(1200, b2.width + pad * 2),
      height: Math.min(500, b2.height + pad * 2),
    },
  });
}

async function record(name, el) {
  const s = clean(await styleOf(el));
  await crop(el, name);
  out[name] = s;
  console.log(name, s.tag, s.backgroundColor, s.color, s.borderRadius, s.fontSize, s.w + 'x' + s.h, s.text);
}

await page.goto('https://www.monodesk.com/', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(1400);

// The painted pill is the <a> whose computed background is the highlighter.
const painted = await page.evaluateHandle(() => {
  const links = [...document.querySelectorAll('a')].filter((a) => /Get started free/.test(a.innerText || ''));
  for (const a of links) {
    const r = a.getBoundingClientRect();
    if (r.width < 40 || r.height < 20 || r.top > 800) continue;
    const nodes = [a, ...a.querySelectorAll('*')];
    for (const n of nodes) {
      const bg = getComputedStyle(n).backgroundColor;
      const b = n.getBoundingClientRect();
      if (bg !== 'rgba(0, 0, 0, 0)' && b.width > 40 && b.height > 20) return n;
    }
    return a;
  }
  return null;
});
const pill = painted.asElement();
if (!pill) throw new Error('no painted CTA');
await record('cta-primary-default', pill);
await pill.hover();
await page.waitForTimeout(280);
await record('cta-primary-hover', pill);

const ghost = page.locator('a').filter({ hasText: /^Log in/ });
let ghostEl = null;
for (let i = 0; i < await ghost.count(); i++) {
  const el = ghost.nth(i);
  const box = await el.boundingBox();
  const bg = await el.evaluate((node) => getComputedStyle(node).backgroundColor);
  if (box && box.height > 24 && box.width > 60) { ghostEl = el; console.log('ghost', i, bg, Math.round(box.width), Math.round(box.height)); break; }
}
if (ghostEl) {
  await record('cta-secondary-default', ghostEl);
  await ghostEl.hover();
  await page.waitForTimeout(250);
  await record('cta-secondary-hover', ghostEl);
}

// header bar: the rounded navy strip
const header = page.locator('header').first();
const bar = header.locator('a').first().locator('xpath=ancestor::*[contains(@style,"") ]').first();
// measure the element whose background is the brand blue and width > 800
const barHandle = await page.evaluateHandle(() => {
  const all = [...document.querySelectorAll('header *, header')];
  let best = null;
  for (const el of all) {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    if (r.width > 900 && r.height > 40 && r.height < 120 && cs.backgroundColor !== 'rgba(0, 0, 0, 0)') {
      if (!best || r.height < best.getBoundingClientRect().height) best = el;
    }
  }
  return best;
});
if (barHandle) {
  const el = barHandle.asElement();
  if (el) await record('site-header-bar', el);
}

// nav menu
const feat = page.getByRole('button', { name: /Features/ }).first();
if (await feat.count()) {
  await feat.hover();
  await page.waitForTimeout(700);
  const panel = await page.evaluateHandle(() => {
    const links = [...document.querySelectorAll('a')].filter((a) => /Projects/.test(a.innerText) && a.getBoundingClientRect().height > 10 && a.getBoundingClientRect().top > 40 && a.getBoundingClientRect().top < 500);
    if (!links.length) return null;
    let el = links[0];
    for (let i = 0; i < 6 && el.parentElement; i++) {
      const r = el.parentElement.getBoundingClientRect();
      const bg = getComputedStyle(el.parentElement).backgroundColor;
      if (r.width > 180 && r.height > 80 && bg !== 'rgba(0, 0, 0, 0)') return el.parentElement;
      el = el.parentElement;
    }
    return links[0].parentElement;
  });
  const pel = panel.asElement();
  if (pel) await record('nav-menu-features', pel);
  await page.mouse.move(20, 700);
  await page.waitForTimeout(300);
}

// FAQ answer
const faq = page.locator('button').filter({ hasText: 'What is MonoDesk' }).first();
if (await faq.count()) {
  await faq.scrollIntoViewIfNeeded();
  await page.waitForTimeout(200);
  await faq.click();
  await page.waitForTimeout(400);
  const block = faq.locator('xpath=ancestor::*[self::li or self::div][1]');
  await record('faq-item-open', block);
}

// pricing card
await page.goto('https://www.monodesk.com/pricing', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(1400);
const pro = await page.evaluateHandle(() => {
  const els = [...document.querySelectorAll('div, article, section')];
  return els.find((el) => {
    const t = el.innerText || '';
    const r = el.getBoundingClientRect();
    return /MOST POPULAR/.test(t) && /\$29/.test(t) && r.width > 200 && r.width < 500 && r.height > 200 && r.height < 900;
  }) || null;
});
const proEl = pro.asElement();
if (proEl) await record('plan-card-pro', proEl);

// help card
await page.goto('https://www.monodesk.com/help', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(1200);
const card = page.locator('a, article, div').filter({ hasText: 'Getting started' }).first();
// climb to the white card
const helpCard = await page.evaluateHandle(() => {
  const el = [...document.querySelectorAll('a, div, article')].find((n) => /Getting started/.test(n.innerText || '') && n.getBoundingClientRect().width > 180 && n.getBoundingClientRect().width < 400 && n.getBoundingClientRect().height > 80 && n.getBoundingClientRect().height < 280);
  return el || null;
});
const hc = helpCard.asElement();
if (hc) {
  await record('help-card-default', hc);
  await hc.hover();
  await page.waitForTimeout(250);
  await record('help-card-hover', hc);
}
const search = page.locator('input[placeholder*="Search"]').first();
if (await search.count()) {
  await record('search-default', search);
  await search.focus();
  await page.waitForTimeout(200);
  await record('search-focus', search);
}

// login card exact
await page.goto('https://app.monodesk.com/login', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(2000);
const loginCard = await page.evaluateHandle(() => {
  const els = [...document.querySelectorAll('div')];
  return els.find((el) => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return /Login to your account/.test(el.innerText || '') && r.width > 300 && r.width < 560 && r.height > 400 && r.height < 800 && cs.backgroundColor === 'rgb(255, 255, 255)';
  }) || null;
});
const lc = loginCard.asElement();
if (lc) await record('login-card', lc);

const email = page.locator('input[placeholder*="email" i]').first();
if (await email.count()) {
  await record('field-email-default', email);
  await email.focus();
  await page.waitForTimeout(200);
  await record('field-email-focus', email);
  // also the wrapper if the border lives there
  const wrap = email.locator('xpath=..');
  await record('field-email-wrap-focus', wrap);
}

await browser.close();
const prev = JSON.parse(fs.readFileSync(path.join(RAW, 'components-computed.json'), 'utf8'));
prev.components = { ...prev.components, ...Object.fromEntries(Object.entries(out).map(([k, v]) => [k, { style: v, text: v.text, box: { w: v.w, h: v.h } }])) };
prev.pass2 = true;
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(prev, null, 2));
console.log('pass2', Object.keys(out).length);
