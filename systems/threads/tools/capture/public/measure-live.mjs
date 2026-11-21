// Read computed styles and declared custom properties from the live public pages.
// Writes systems/threads/raw/css-vars.json and components-computed.json.
// Does not type, submit, or click Instagram / Google / Apple / Facebook.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const log = (...a) => console.log(...a);

const PROPS = [
  'color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderRadius',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'height', 'width', 'boxShadow', 'outline', 'opacity',
];

async function measure(page, spec) {
  return page.evaluate(({ spec, PROPS }) => {
    const visible = (el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 2 && r.height > 2 && s.visibility !== 'hidden' && s.display !== 'none' && Number(s.opacity) > 0.2;
    };
    const byText = (sel, text, pred) => [...document.querySelectorAll(sel)].find((el) => {
      if (!visible(el)) return false;
      const t = (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim();
      if (text && t !== text && !t.startsWith(text)) return false;
      return pred ? pred(el) : true;
    });
    const find = () => {
      if (spec.kind === 'nav') return byText('[role="button"], a', spec.text, (el) => el.getBoundingClientRect().x < 280);
      if (spec.kind === 'login-link') return byText('a', 'Log in', (el) => el.getBoundingClientRect().x < 280 && el.getBoundingClientRect().width > 80);
      if (spec.kind === 'input') return document.querySelector(spec.sel);
      if (spec.kind === 'dialog-title') {
        const d = document.querySelector('[role="dialog"]');
        if (!d) return null;
        return [...d.querySelectorAll('div, span, h1, h2')].find((el) => (el.innerText || '').trim() === spec.text && el.children.length < 3);
      }
      if (spec.kind === 'ig') {
        const d = document.querySelector('[role="dialog"]') || document.body;
        return [...d.querySelectorAll('[role="button"], a, div')].find((el) => (el.innerText || '').replace(/\s+/g, ' ').trim() === 'Continue with Instagram' && visible(el) && el.getBoundingClientRect().height > 30 && el.getBoundingClientRect().height < 80);
      }
      if (spec.kind === 'css') return document.querySelector(spec.sel);
      return null;
    };
    const el = find();
    if (!el) return { name: spec.name, miss: true };
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of PROPS) style[p] = s[p];
    return {
      name: spec.name, state: spec.state, page: location.pathname,
      tag: el.tagName, text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40),
      box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      style,
    };
  }, { spec, PROPS });
}

async function dumpDeclared(page) {
  return page.evaluate(() => {
    const noUrl = (v) => v.replace(/url\([^)]*\)/gi, 'url(…)');
    const bins = { light: [], dark: [], other: [] };
    const fonts = [];
    let sheets = 0, blocked = 0;
    for (const sheet of document.styleSheets) {
      sheets++;
      let rules;
      try { rules = sheet.cssRules; } catch { blocked++; continue; }
      const walk = (list, ctx) => {
        for (const rule of list) {
          if (rule.type === CSSRule.FONT_FACE_RULE) {
            fonts.push({ family: rule.style.getPropertyValue('font-family'), weight: rule.style.getPropertyValue('font-weight'), style: rule.style.getPropertyValue('font-style') });
            continue;
          }
          if (rule.cssRules && !rule.style) {
            const head = rule.media ? '@media ' + rule.media.mediaText : (rule.conditionText ? '@supports ' + rule.conditionText : rule.cssText.split('{')[0].trim().slice(0, 80));
            walk(rule.cssRules, [...ctx, head]);
            continue;
          }
          if (!rule.style) continue;
          const props = {};
          for (let i = 0; i < rule.style.length; i++) {
            const k = rule.style[i];
            if (k.startsWith('--')) props[k] = noUrl(rule.style.getPropertyValue(k).trim()).slice(0, 160);
          }
          if (!Object.keys(props).length) continue;
          const sel = (rule.selectorText || '').slice(0, 180);
          const row = { selector: sel, context: ctx.slice(0, 3), properties: props };
          if (/fb-dark-mode|prefers-color-scheme:\s*dark/.test(sel + ' ' + ctx.join(' '))) bins.dark.push(row);
          else if (/fb-light-mode|:root|html/.test(sel)) bins.light.push(row);
          else bins.other.push(row);
        }
      };
      walk(rules, []);
    }
    return { sheets, blocked, fonts: fonts.slice(0, 30), counts: { light: bins.light.length, dark: bins.dark.length, other: bins.other.length }, bins };
  });
}

const browser = await chromium.launch({ headless: true });
const components = [];
const declared = {};

for (const theme of ['light', 'dark']) {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', colorScheme: theme,
  });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const page = await context.newPage();
  await page.goto('https://www.threads.com/', { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(2500);
  declared[theme] = await dumpDeclared(page);
  log(theme, 'sheets', declared[theme].sheets, 'blocked', declared[theme].blocked, 'light rules', declared[theme].counts.light, 'dark rules', declared[theme].counts.dark, 'other', declared[theme].counts.other);

  const specs = [
    { name: 'nav-home', kind: 'nav', text: 'Home', state: 'default' },
    { name: 'nav-search', kind: 'nav', text: 'Search', state: 'default' },
    { name: 'button-login', kind: 'login-link', state: 'default' },
    { name: 'nav-more', kind: 'nav', text: 'More', state: 'default' },
  ];
  for (const spec of specs) {
    const row = await measure(page, spec);
    row.theme = theme;
    components.push(row);
    log(' ', spec.name, row.miss ? 'MISS' : row.style.backgroundColor + ' ' + row.style.fontSize);
  }

  // hover login via CDP, no click
  const cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const loginBox = components.find((c) => c.name === 'button-login' && c.theme === theme && !c.miss);
  if (loginBox) {
    await page.mouse.move(loginBox.box.x + 20, loginBox.box.y + 10);
    await page.waitForTimeout(400);
    const hover = await measure(page, { name: 'button-login', kind: 'login-link', state: 'hover' });
    hover.theme = theme;
    hover.state = 'hover';
    components.push(hover);
    log('  login hover', hover.miss ? 'MISS' : hover.style.backgroundColor);
    await page.mouse.move(1400, 10);
  }

  // join dialog still up? if not, open new thread wall and measure dialog
  await page.evaluate(() => {
    const hit = [...document.querySelectorAll('[role="button"]')].find((el) => (el.innerText || '').trim() === 'New thread' && el.getBoundingClientRect().x < 280);
    hit && hit.click();
  });
  await page.waitForTimeout(700);
  for (const spec of [
    { name: 'dialog-title', kind: 'dialog-title', text: 'Sign up to post', state: 'default' },
    { name: 'button-instagram', kind: 'ig', state: 'default' },
  ]) {
    const row = await measure(page, spec);
    row.theme = theme;
    components.push(row);
    log(' ', spec.name, row.miss ? 'MISS' : row.style.color + ' / ' + row.style.backgroundColor + ' r=' + row.style.borderRadius);
  }
  await page.keyboard.press('Escape');
  await context.close();
}

// login fields, light only, no typing
{
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', colorScheme: 'light' });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const page = await context.newPage();
  await page.goto('https://www.threads.com/login', { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(2000);
  for (const spec of [
    { name: 'field-username', kind: 'input', sel: 'input[type="text"]', state: 'default' },
    { name: 'field-password', kind: 'input', sel: 'input[type="password"]', state: 'default' },
  ]) {
    const row = await measure(page, spec);
    row.theme = 'light';
    row.page = '/login';
    components.push(row);
    log('login', spec.name, row.miss ? 'MISS' : row.style.borderRadius + ' ' + row.style.height);
  }
  // focus username without typing
  await page.locator('input[type="text"]').first().focus();
  await page.waitForTimeout(300);
  const focused = await measure(page, { name: 'field-username', kind: 'input', sel: 'input[type="text"]', state: 'focus' });
  focused.theme = 'light';
  focused.state = 'focus';
  components.push(focused);
  log('login focus', focused.miss ? 'MISS' : focused.style.outline + ' ' + focused.style.boxShadow);
  await context.close();
}

fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
  source: 'CSSOM of https://www.threads.com/ on 2026-11-21, headless Chromium, light and dark color schemes',
  declared,
}, null, 1));
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({
  source: 'computed styles on live public elements, 2026-11-21',
  components,
}, null, 1));
log('wrote', components.length, 'component readings');
await browser.close();
