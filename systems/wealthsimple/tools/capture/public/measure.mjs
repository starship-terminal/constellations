// Measure computed styles on public Wealthsimple pages. No form submit, no login typing.
// PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(HERE, '..', '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const PROPS = [
  'display', 'position', 'width', 'height', 'minHeight', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'backgroundColor', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'boxShadow', 'outline', 'opacity', 'textDecorationLine',
];

function pick(style) {
  const o = {};
  for (const k of PROPS) o[k] = style[k];
  return o;
}

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-CA' });
const page = await ctx.newPage();
await page.goto('https://www.wealthsimple.com/en-ca/pricing', { waitUntil: 'domcontentloaded', timeout: 50000 });
await page.waitForTimeout(2500);
await page.addStyleTag({ content: '#onetrust-consent-sdk,#onetrust-banner-sdk{display:none!important}' }).catch(() => {});

const readings = await page.evaluate((PROPS) => {
  const pick = (el) => {
    if (!el) return null;
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { tag: el.tagName, text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80), rect: { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y) } };
    for (const k of PROPS) o[k] = s[k];
    return o;
  };
  const byText = (sel, re) => [...document.querySelectorAll(sel)].find((el) => re.test((el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim()) && el.getBoundingClientRect().width > 20 && el.getBoundingClientRect().height > 10);
  const root = getComputedStyle(document.documentElement);
  const names = [];
  for (const sheet of document.styleSheets) {
    let rules; try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const rule of list) {
        if (rule.selectorText === ':root' && rule.style) {
          for (let i = 0; i < rule.style.length; i++) {
            const k = rule.style[i];
            if (k.startsWith('--ws-')) names.push(k);
          }
        }
        if (rule.cssRules) walk(rule.cssRules);
      }
    };
    walk(rules);
  }
  const tokens = {};
  for (const n of [...new Set(names)]) tokens[n] = root.getPropertyValue(n).trim();
  const cta = byText('a,button', /^Get started$/);
  let hover = null, focus = null, pressed = null;
  return { tokens, samples: {
    body: pick(document.body),
    h1: pick(document.querySelector('h1')),
    h2: pick(document.querySelector('h2')),
    cta: pick(cta),
    login: pick(byText('a,button', /^Log in$/)),
    nav: pick(byText('header button, nav button', /^Trade$/)),
    link: pick(document.querySelector('footer a')),
    input: pick(document.querySelector('input[type="email"], input[type="text"], input:not([type="hidden"])')),
  }, tokenCount: Object.keys(tokens).length };
}, PROPS);

// interaction states on Get started, without navigating away if possible
const states = {};
const cta = page.getByRole('link', { name: 'Get started' }).first();
async function snap(label, action) {
  try {
    await action();
    await page.waitForTimeout(200);
    states[label] = await cta.evaluate((el) => {
      const s = getComputedStyle(el);
      return { color: s.color, backgroundColor: s.backgroundColor, borderRadius: s.borderRadius, outline: s.outline, boxShadow: s.boxShadow, borderTopColor: s.borderTopColor, fontSize: s.fontSize, fontWeight: s.fontWeight, height: s.height, padding: s.padding };
    });
  } catch (e) {
    states[label] = { error: String(e.message).split('\n')[0] };
  }
}
await snap('hover', () => cta.hover());
await snap('focus', () => cta.focus());
await page.keyboard.down('Space').catch(() => {});
await snap('pressed-attempt', async () => {});
await page.keyboard.up('Space').catch(() => {});

// pricing page controls
await page.goto('https://www.wealthsimple.com/en-ca/contact', { waitUntil: 'domcontentloaded', timeout: 50000 });
await page.waitForTimeout(2000);
const contact = await page.evaluate(() => {
  const pick = (el) => {
    if (!el) return null;
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return { text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 60), w: Math.round(r.width), h: Math.round(r.height), bg: s.backgroundColor, color: s.color, radius: s.borderRadius, border: s.borderTopWidth + ' ' + s.borderTopStyle + ' ' + s.borderTopColor, font: s.fontFamily, size: s.fontSize, weight: s.fontWeight, pad: s.padding, shadow: s.boxShadow };
  };
  const field = document.querySelector('input:not([type="hidden"]), textarea');
  const submit = [...document.querySelectorAll('button')].find((b) => /send|submit|contact/i.test(b.innerText || ''));
  return { field: pick(field), submit: pick(submit), h1: pick(document.querySelector('h1')) };
});

const out = { run: '2026-11-21', source: 'computed style on www.wealthsimple.com/en-ca/pricing and /en-ca/contact, desktop 1440', readings, states, contact };
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2));
console.log('tokens', readings.tokenCount);
console.log('samples', Object.keys(readings.samples).map((k) => k + ':' + (readings.samples[k] ? readings.samples[k].fontSize + ' ' + readings.samples[k].color : 'null')).join(' | '));
console.log('states', JSON.stringify(states));
console.log('contact', JSON.stringify(contact));
await browser.close();
