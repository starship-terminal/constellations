// Read Stable Audio's public CSS and component states. Writes raw/ only.
// Nothing is submitted. AuthKit and signup dialogs are recorded, not filled.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node harvest.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(here, '..', '..', '..');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

const HIDE = '#onetrust-consent-sdk,#onetrust-banner-sdk,.onetrust-pc-dark-filter{display:none!important;visibility:hidden!important;pointer-events:none!important}';

function walkRules(list, ctx, out, fonts) {
  for (const r of list) {
    if (r.type === CSSRule.FONT_FACE_RULE) {
      fonts.push({
        family: r.style.getPropertyValue('font-family'),
        weight: r.style.getPropertyValue('font-weight'),
        style: r.style.getPropertyValue('font-style'),
        src: (r.style.getPropertyValue('src') || '').replace(/url\((?!\s*['"]?(?:data:|#))[^)]*\)/gi, 'url(…)').slice(0, 220),
      });
      continue;
    }
    if (r.cssRules && !r.style) {
      const head = r.cssText.split('{')[0].trim().slice(0, 180);
      try { walkRules(r.cssRules, [...ctx, head], out, fonts); } catch { /* cross-origin */ }
      continue;
    }
    if (!r.style) continue;
    const props = {};
    for (let i = 0; i < r.style.length; i++) {
      const k = r.style[i];
      if (k.startsWith('--sx-') || k.startsWith('--hn-')) props[k] = r.style.getPropertyValue(k).trim();
    }
    if (Object.keys(props).length) out.push({ selector: r.selectorText || '', context: ctx, properties: props });
  }
}

const PROPS = [
  'backgroundColor', 'color', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight',
  'letterSpacing', 'textTransform', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'height', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset', 'opacity',
  'textDecorationLine', 'gap',
];

async function readEl(page, handle) {
  return handle.evaluate((el, props) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = {
      tag: el.tagName,
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 60),
      w: Math.round(r.width),
      h: Math.round(r.height),
    };
    for (const p of props) o[p] = s[p];
    return o;
  }, PROPS);
}

async function states(page, locator, label) {
  const el = locator.first();
  if (!(await el.count())) return { label, missing: true };
  await el.scrollIntoViewIfNeeded().catch(() => {});
  const out = { label, states: {} };
  out.states.default = await readEl(page, el);
  await el.hover().catch(() => {});
  await page.waitForTimeout(180);
  out.states.hover = await readEl(page, el);
  await el.focus().catch(() => {});
  await page.waitForTimeout(120);
  out.states['focus-visible'] = await readEl(page, el);
  // CDP pressed, not a click that navigates.
  const cdp = await page.context().newCDPSession(page);
  const box = await el.boundingBox();
  if (box) {
    const x = box.x + Math.min(8, box.width / 2);
    const y = box.y + Math.min(8, box.height / 2);
    await cdp.send('Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'left', clickCount: 1 });
    await page.waitForTimeout(80);
    out.states.pressed = await readEl(page, el);
    // Release off the control so the press is not a click that navigates.
    await cdp.send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: 2, y: 2, button: 'left', clickCount: 1 });
  }
  await cdp.detach().catch(() => {});
  return out;
}

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA });
const page = await ctx.newPage();
page.setDefaultTimeout(20000);
await page.goto('https://stableaudio.com/', { waitUntil: 'load', timeout: 45000 });
await page.waitForTimeout(1200);
await page.addStyleTag({ content: HIDE });

const harvested = await page.evaluate(() => {
  const rules = [];
  const fonts = [];
  const walk = (list, ctx) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        fonts.push({
          family: r.style.getPropertyValue('font-family'),
          weight: r.style.getPropertyValue('font-weight'),
          style: r.style.getPropertyValue('font-style'),
          src: (r.style.getPropertyValue('src') || '').replace(/url\((?!\s*['"]?(?:data:|#))[^)]*\)/gi, 'url(…)').slice(0, 220),
        });
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.cssText.split('{')[0].trim().slice(0, 180);
        try { walk(r.cssRules, [...ctx, head]); } catch { /* */ }
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--sx-') || k.startsWith('--hn-')) props[k] = r.style.getPropertyValue(k).trim();
      }
      if (Object.keys(props).length) rules.push({ selector: r.selectorText || '', context: ctx, properties: props });
    }
  };
  for (const sheet of document.styleSheets) {
    try { walk(sheet.cssRules, []); } catch { /* cross-origin sheet */ }
  }
  return { rules, fonts };
});

const scopeVars = await page.evaluate(() => {
  const el = document.querySelector('.homePage_page__pMG82');
  const cs = getComputedStyle(el);
  const names = [];
  const walk = (list) => {
    for (const r of list) {
      if (r.cssRules && !r.style) { try { walk(r.cssRules); } catch { /* */ } continue; }
      if (!r.style) continue;
      for (let i = 0; i < r.style.length; i++) if (r.style[i].startsWith('--sx-') || r.style[i].startsWith('--hn-')) names.push(r.style[i]);
    }
  };
  for (const sheet of document.styleSheets) { try { walk(sheet.cssRules); } catch { /* */ } }
  const resolved = {};
  for (const k of new Set(names)) resolved[k] = cs.getPropertyValue(k).trim();
  return { className: el.className, resolved };
});

fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
  captured: '2026-11-21',
  url: 'https://stableaudio.com/',
  note: 'Declared --sx-* and --hn-* rules from same-origin stylesheets. resolved.marketing is getComputedStyle on .homePage_page__pMG82 (sx-scope sx-platform sx-dark). :root paper values are in rules where selector is :root; they are not what the public page paints.',
  fonts: harvested.fonts,
  rules: harvested.rules,
  resolved: { marketing: scopeVars.resolved },
  scopeClass: scopeVars.className,
}, null, 2) + '\n');
console.log('css-vars rules', harvested.rules.length, 'fonts', harvested.fonts.length);

const components = [];
const specs = [
  ['button-primary', 'button.Button_primary__MjY5K'],
  ['button-secondary', 'button.Button_secondary__QcMI3'],
  ['button-ghost', 'button.Button_ghost__rEAr2'],
  ['link-nav', 'a.HomeTopNav_link__'],
  ['word-chip', 'button.HeroMadLib_word__CogYq'],
  ['faq', 'summary.HomeFaq_question__y2yCc'],
];
const classDump = await page.evaluate(() => {
  const btns = [...document.querySelectorAll('button')].slice(0, 20).map((b) => ({
    text: (b.innerText || b.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 40),
    cls: String(b.className).slice(0, 100),
  }));
  return btns;
});
console.log('buttons', JSON.stringify(classDump, null, 2));
for (const [label, sel] of specs) {
  const loc = page.locator(sel);
  const n = await loc.count();
  console.log('spec', label, n);
  if (!n) { components.push({ label, missing: true, selector: sel }); continue; }
  components.push(await states(page, loc, label));
}

// nav link by text
{
  const loc = page.getByRole('link', { name: 'Pricing', exact: true }).first();
  components.push(await states(page, loc, 'link-pricing'));
}

// presets menu
{
  await page.getByRole('button', { name: 'Presets' }).first().click();
  await page.waitForTimeout(400);
  const menu = page.locator('[role="menu"]').first();
  const menuRead = await readEl(page, menu);
  const item = menu.getByRole('menuitem').first();
  const itemStates = await states(page, item, 'menu-item');
  components.push({ label: 'menu-presets', menu: menuRead, item: itemStates });
  await page.keyboard.press('Escape');
  await page.waitForTimeout(200);
}

// signup dialog, do not follow Sign up free
{
  await page.getByRole('button', { name: 'Make my mix' }).first().click();
  await page.waitForTimeout(700);
  const dialog = page.locator('[role="dialog"]').filter({ hasText: 'Sign up' }).last();
  const d = await readEl(page, dialog);
  const cta = dialog.getByRole('button', { name: /Sign up/ }).first();
  const ctaRead = await cta.count() ? await readEl(page, cta) : null;
  const notNow = dialog.getByRole('button', { name: 'Not now' }).first();
  const notNowRead = await notNow.count() ? await readEl(page, notNow) : null;
  components.push({ label: 'dialog-signup', dialog: d, cta: ctaRead, dismiss: notNowRead });
  if (await notNow.count()) await notNow.click();
  await page.waitForTimeout(300);
}

// help layer
{
  await page.getByRole('button', { name: 'Help' }).first().click();
  await page.waitForTimeout(400);
  const bar = page.locator('.Help_bar__FsSsk').first();
  components.push({ label: 'help-bar', bar: await bar.count() ? await readEl(page, bar) : { missing: true } });
  const done = page.getByRole('button', { name: 'Done' }).first();
  if (await done.count()) await done.click();
}

// faq open
{
  const sum = page.locator('summary.HomeFaq_question__y2yCc').first();
  await sum.scrollIntoViewIfNeeded();
  await sum.click();
  await page.waitForTimeout(300);
  const details = sum.locator('xpath=..');
  components.push({ label: 'faq-open', summary: await readEl(page, sum), details: await readEl(page, details) });
}

// pricing page buttons and cards
await page.goto('https://stableaudio.com/pricing', { waitUntil: 'domcontentloaded', timeout: 30000 });
await page.waitForTimeout(1000);
await page.addStyleTag({ content: HIDE });
const pricing = await page.evaluate((props) => {
  const cards = [...document.querySelectorAll('section, article, div')].filter(el => /\$0\/mo|credits/.test(el.innerText || '') && el.getBoundingClientRect().height > 180 && el.getBoundingClientRect().height < 700);
  const pick = (el) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40), cls: String(el.className).slice(0, 80), w: Math.round(r.width), h: Math.round(r.height) };
    for (const p of props) o[p] = s[p];
    return o;
  };
  const planBtns = [...document.querySelectorAll('button')].filter(b => /Start free|Get Solo|Get Session|Get Producer|Get Studio/.test(b.innerText || '')).map(pick);
  return { planBtns, cardCount: cards.length, card: cards[0] ? pick(cards[0]) : null };
}, PROPS);
components.push({ label: 'pricing', ...pricing });

// plugin os toggle
await page.goto('https://stableaudio.com/plugin', { waitUntil: 'domcontentloaded', timeout: 30000 });
await page.waitForTimeout(800);
await page.addStyleTag({ content: HIDE });
const mac = page.getByRole('button', { name: 'Mac', exact: true }).first();
const win = page.getByRole('button', { name: 'Windows', exact: true }).first();
components.push({ label: 'os-mac', ...(await states(page, mac, 'os-mac')) });
await win.click();
await page.waitForTimeout(300);
components.push({ label: 'os-windows-selected', selected: await readEl(page, win) });

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({
  captured: '2026-11-21',
  viewport: { width: 1440, height: 900 },
  components,
}, null, 2) + '\n');
console.log('components', components.length);
await browser.close();
