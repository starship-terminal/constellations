// Read computed styles from public polar.sh pages. No typing, no submit.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const OUT = path.join(os.homedir(), '.design-systems', 'polar', 'measure.json');
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();

async function css(url, specs) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1600);
  return page.evaluate((specs) => {
    const pick = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40),
        bg: s.backgroundColor,
        color: s.color,
        font: s.fontFamily,
        size: s.fontSize,
        weight: s.fontWeight,
        lh: s.lineHeight,
        radius: s.borderRadius,
        pad: s.padding,
        border: s.border,
        h: Math.round(r.height),
        w: Math.round(r.width),
        shadow: s.boxShadow === 'none' ? null : s.boxShadow.slice(0, 120),
      };
    };
    const root = getComputedStyle(document.documentElement);
    const vars = {};
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      for (const rule of rules || []) {
        if (!rule.style) continue;
        for (const name of rule.style) {
          if (name.startsWith('--') && vars[name] == null) vars[name] = rule.style.getPropertyValue(name).trim();
        }
      }
    }
    const interesting = {};
    for (const [k, v] of Object.entries(vars)) {
      if (/color|radius|font|space|shadow|ease|duration|polar|blue|red|green|amber/.test(k) && Object.keys(interesting).length < 180) interesting[k] = v.slice(0, 80);
    }
    const out = {};
    for (const [name, sel] of Object.entries(specs)) out[name] = pick(sel);
    return {
      url: location.origin + location.pathname,
      htmlClass: document.documentElement.className,
      bodyBg: getComputedStyle(document.body).backgroundColor,
      htmlBg: root.backgroundColor,
      colorScheme: root.colorScheme,
      viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
      vars: interesting,
      specs: out,
    };
  }, specs);
}

const home = await css('https://polar.sh/', {
  body: 'body',
  h1: 'h1',
  nav: 'nav',
  primary: 'nav a[href="/signup"], header a[href="/signup"], a[href="/signup"]',
  ghost: 'nav button, header button',
});

// Better button selectors after seeing the page
const buttons = await page.evaluate(() => {
  const rows = [...document.querySelectorAll('a, button')].filter((el) => /get started|sign in/i.test(el.innerText || '')).slice(0, 8).map((el) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      tag: el.tagName,
      text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40),
      href: el.getAttribute('href'),
      bg: s.backgroundColor,
      color: s.color,
      font: s.fontFamily,
      size: s.fontSize,
      weight: s.fontWeight,
      radius: s.borderRadius,
      pad: s.padding,
      h: Math.round(r.height),
      border: s.borderTopWidth + ' ' + s.borderTopStyle + ' ' + s.borderTopColor,
    };
  });
  const main = document.querySelector('main') || document.body;
  const ms = getComputedStyle(main);
  return {
    buttons: rows,
    mainBg: ms.backgroundColor,
    mainColor: ms.color,
    bodyFont: getComputedStyle(document.body).fontFamily,
    h1: (() => {
      const h = document.querySelector('h1');
      if (!h) return null;
      const s = getComputedStyle(h);
      return { size: s.fontSize, weight: s.fontWeight, lh: s.lineHeight, color: s.color, font: s.fontFamily, ls: s.letterSpacing };
    })(),
  };
});

const docs = await css('https://polar.sh/docs/introduction', {
  body: 'body',
  h1: 'h1',
  link: 'a',
});

const theme = await page.evaluate(() => {
  const b = [...document.querySelectorAll('button')].find((el) => /theme/i.test(el.getAttribute('aria-label') || el.innerText || ''));
  return b ? (b.getAttribute('aria-label') || b.innerText) : null;
});

const pricing = await css('https://polar.sh/resources/pricing', { h1: 'h1', body: 'body' });

const auth = await css('https://polar.sh/auth', { body: 'body' });
const authBits = await page.evaluate(() => {
  const card = document.querySelector('[class*="card"], main, form, [role=dialog]') || document.body;
  const inputs = [...document.querySelectorAll('input')].map((i) => {
    const s = getComputedStyle(i);
    const r = i.getBoundingClientRect();
    return { type: i.type, placeholder: i.placeholder, bg: s.backgroundColor, color: s.color, radius: s.borderRadius, border: s.border, h: Math.round(r.height), valueLen: (i.value || '').length };
  });
  const buttons = [...document.querySelectorAll('button, a')].filter((el) => /sign in/i.test(el.innerText || '')).slice(0, 6).map((el) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return { text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40), bg: s.backgroundColor, color: s.color, radius: s.borderRadius, h: Math.round(r.height), border: s.border };
  });
  const heading = document.querySelector('h1, h2');
  const hs = heading ? getComputedStyle(heading) : null;
  return {
    pageBg: getComputedStyle(document.body).backgroundColor,
    htmlClass: document.documentElement.className,
    heading: heading ? { text: heading.innerText.slice(0, 40), size: hs.fontSize, weight: hs.fontWeight, font: hs.fontFamily, color: hs.color } : null,
    inputs,
    buttons,
    captcha: !!document.querySelector('iframe[src*="turnstile"], iframe[src*="captcha"]'),
  };
});

const out = { captured: new Date().toISOString(), viewport: { width: 1440, height: 900, dpr: 1 }, home, buttons, docs, docsThemeButton: theme, pricing, auth, authBits };
fs.writeFileSync(OUT, JSON.stringify(out, null, 2));
console.log('wrote', OUT);
console.log(JSON.stringify({
  homeClass: home.htmlClass,
  homeBg: home.bodyBg,
  h1: buttons.h1,
  buttons: buttons.buttons,
  mainBg: buttons.mainBg,
  docsClass: docs.htmlClass,
  docsBg: docs.htmlBg,
  docsTheme: theme,
  auth: authBits,
  varCount: Object.keys(home.vars || {}).length,
}, null, 2));
await browser.close();
