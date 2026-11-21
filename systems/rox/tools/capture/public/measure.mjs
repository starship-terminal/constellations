// Measures Rox public components from the live page. Does not type or submit.
//
//   PLAYWRIGHT=... node measure.mjs
//
// Writes raw/components-computed.json and components/crops/{name}-{state}.png
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE } from './lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..', '..');
const RAW = path.join(REF, 'raw');
const CROPS = path.join(REF, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const PROPS = [
  'display', 'position', 'width', 'height', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'borderTopWidth', 'borderTopStyle', 'borderTopColor', 'borderTopLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform', 'color',
  'textDecorationLine', 'transitionDuration', 'transitionTimingFunction', 'opacity', 'cursor',
];

function noUrl(v) {
  return typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))[^)]*\)/g, 'url(…)') : v;
}

async function readStyle(loc) {
  return loc.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = cs[p];
    return {
      tag: el.tagName.toLowerCase(),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style,
    };
  }, PROPS);
}

async function crop(loc, name) {
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 6;
  const file = path.join(CROPS, name + '.png');
  await loc.page().screenshot({
    path: file,
    clip: {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(box.width + pad * 2, 1440),
      height: Math.min(box.height + pad * 2, 400),
    },
  });
  return 'components/crops/' + name + '.png';
}

async function states(page, loc, slug) {
  const out = {};
  if (!(await loc.count())) return out;
  const el = loc.first();
  await el.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  out.default = await readStyle(el);
  out.default.crop = await crop(el, slug + '-default');
  await el.hover().catch(() => {});
  await page.waitForTimeout(250);
  out.hover = await readStyle(el);
  out.hover.crop = await crop(el, slug + '-hover');
  await el.focus().catch(() => {});
  await page.waitForTimeout(200);
  out['focus-visible'] = await readStyle(el);
  out['focus-visible'].crop = await crop(el, slug + '-focus-visible');
  await page.mouse.move(2, 2);
  return out;
}

const browser = await chromium.launch({ headless: true });
const out = { readAt: new Date().toISOString().slice(0, 10), source: 'live www.rox.com, signed out, Playwright Chromium', pages: {}, components: {} };

async function open(pathName, mobile = false) {
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const page = await ctx.newPage();
  await page.goto('https://www.rox.com' + pathName, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1500);
  const vp = await page.evaluate(() => ({
    innerWidth, innerHeight, devicePixelRatio,
    visualViewport: visualViewport && { width: visualViewport.width, height: visualViewport.height, scale: visualViewport.scale },
  }));
  return { ctx, page, vp };
}

{
  const { ctx, page, vp } = await open('/');
  out.pages.home = { url: 'https://www.rox.com/', viewport: vp };
  out.components['nav-link'] = await states(page, page.locator('a').filter({ hasText: /^Platform$/ }).first(), 'nav-link');
  out.components['primary-link'] = await states(page, page.locator('a').filter({ hasText: /^Contact Sales$/ }).first(), 'primary-link');
  out.components['start-link'] = await states(page, page.locator('a').filter({ hasText: /^Start now$/ }).first(), 'start-link');
  out.components.announcement = await states(page, page.locator('a').filter({ hasText: /Series B/ }).first(), 'announcement');
  out.components['story-card'] = await states(page, page.locator('a').filter({ hasText: /^Open story$/ }).first(), 'story-card');
  const roles = await page.evaluate(() => {
    const pick = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const cs = getComputedStyle(el);
      return {
        text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60),
        fontFamily: cs.fontFamily, fontSize: cs.fontSize, fontWeight: cs.fontWeight,
        lineHeight: cs.lineHeight, letterSpacing: cs.letterSpacing, color: cs.color,
      };
    };
    const h1 = [...document.querySelectorAll('h1, h2, p, a')].filter((el) => el.getBoundingClientRect().width > 40);
    const sample = (pred) => {
      const el = h1.find(pred);
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { text: (el.innerText || '').trim().slice(0, 50), fontFamily: cs.fontFamily, fontSize: cs.fontSize, fontWeight: cs.fontWeight, lineHeight: cs.lineHeight, letterSpacing: cs.letterSpacing, color: cs.color };
    };
    return {
      body: { background: getComputedStyle(document.body).backgroundColor, color: getComputedStyle(document.body).color, font: getComputedStyle(document.body).fontFamily },
      display: sample((el) => parseFloat(getComputedStyle(el).fontSize) >= 40),
      heading: sample((el) => { const s = parseFloat(getComputedStyle(el).fontSize); return s >= 24 && s < 40; }),
      bodyText: sample((el) => parseFloat(getComputedStyle(el).fontSize) >= 16 && parseFloat(getComputedStyle(el).fontSize) < 20 && (el.innerText || '').length > 40),
    };
  });
  out.pages.home.roles = roles;
  await ctx.close();
}

{
  const { ctx, page, vp } = await open('/pricing');
  out.pages.pricing = { url: 'https://www.rox.com/pricing', viewport: vp };
  out.components['plan-card'] = await states(page, page.getByText('INDIVIDUAL', { exact: false }).locator('xpath=ancestor::*[self::div][3]').first(), 'plan-card');
  out.components['plan-cta'] = await states(page, page.locator('a').filter({ hasText: /Start for free|Try for free|Contact/i }).first(), 'plan-cta');
  await ctx.close();
}

{
  const { ctx, page, vp } = await open('/contact');
  out.pages.contact = { url: 'https://www.rox.com/contact', viewport: vp };
  out.components['text-field'] = await states(page, page.locator('input[name="Email"]').first(), 'text-field');
  out.components.select = await states(page, page.locator('select[name="How did you hear"]').first(), 'select');
  out.components.textarea = await states(page, page.locator('textarea[name="Message"]').first(), 'textarea');
  out.components['submit-button'] = await states(page, page.locator('button').filter({ hasText: /Get in touch/i }).first(), 'submit-button');
  await ctx.close();
}

{
  const { ctx, page, vp } = await open('/docs/about-rox/readme');
  out.pages.docs = { url: 'https://www.rox.com/docs/about-rox/readme', viewport: vp };
  out.components['docs-search'] = await states(page, page.locator('input[placeholder*="Search"]').first(), 'docs-search');
  out.components['docs-nav'] = await states(page, page.locator('a').filter({ hasText: /^Architecture$/ }).first(), 'docs-nav');
  await page.keyboard.press('Control+k');
  await page.waitForTimeout(500);
  const dlg = page.locator('[role="dialog"]').first();
  if (await dlg.count()) {
    out.components['search-dialog'] = { default: await readStyle(dlg), };
    out.components['search-dialog'].default.crop = await crop(dlg, 'search-dialog-default');
  }
  await ctx.close();
}

{
  const { ctx, page, vp } = await open('/', true);
  out.pages.mobile = { url: 'https://www.rox.com/', viewport: vp };
  const burger = page.locator('.framer-dkldq9').first();
  if (await burger.count()) {
    out.components['menu-button'] = await states(page, burger, 'menu-button');
    await burger.click().catch(() => {});
    await page.waitForTimeout(500);
    out.components['drawer-link'] = await states(page, page.locator('a').filter({ hasText: /^Pricing$/ }).first(), 'drawer-link');
  }
  await ctx.close();
}

for (const comp of Object.values(out.components)) {
  for (const st of Object.values(comp)) {
    if (st && st.style) {
      for (const k of Object.keys(st.style)) st.style[k] = noUrl(st.style[k]);
    }
  }
}

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote components', Object.keys(out.components).join(', '));
await browser.close();
