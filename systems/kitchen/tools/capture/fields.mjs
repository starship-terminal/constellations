// Re-read login, signup and blog search fields. Writes into raw/components-computed.json.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, RAW, chromium, UA, hideConsent, styleOf, crop } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
const out = JSON.parse(fs.readFileSync(OUT, 'utf8'));
const browser = await chromium.launch();
const log = (...a) => console.log(...a);

async function shot(key, url, sel, states) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
  const page = await ctx.newPage();
  await page.goto(BASE + url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2000);
  await hideConsent(page);
  const info = await page.evaluate(() => {
    const els = [...document.querySelectorAll('input, textarea, button, a.btn, .btn, form')].slice(0, 20).map((el) => {
      const r = el.getBoundingClientRect();
      return { tag: el.tagName, type: el.type, name: el.name, ph: el.placeholder, cls: el.className, w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y), vis: r.width > 0 };
    });
    return { title: document.title, url: location.href, els };
  });
  log(key, JSON.stringify(info, null, 0).slice(0, 900));
  const loc = page.locator(sel).first();
  const c = out.components[key] || { states: {}, title: key, group: 'Fields', page: key, url: BASE + url };
  if (await loc.count()) {
    const box = await loc.boundingBox();
    log(' box', box);
    if (box && box.width > 2) {
      await loc.scrollIntoViewIfNeeded();
      const s = await styleOf(loc);
      const file = await crop(page, loc, `${key}-default`, 12);
      c.states.default = { ...s, crop: file, via: 'rest' };
      c.missing = false;
      if (states.includes('focused')) {
        await loc.focus();
        await page.waitForTimeout(200);
        const s2 = await styleOf(loc);
        const file2 = await crop(page, loc, `${key}-focused`, 12);
        c.states.focused = { ...s2, crop: file2, via: 'click, nothing submitted' };
      }
    } else {
      c.states.default = { error: 'field has no box on the signed-out page', note: info.url };
      c.missing = true;
    }
  } else {
    c.missing = true;
    c.states.default = { error: 'selector matched nothing', url: info.url };
  }
  out.components[key] = c;
  await ctx.close();
}

await shot('login-field', '/login', 'input.field, input[name=domain]', ['focused']);
await shot('signup-field', '/get-started', 'input[name=email]', ['focused']);
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
await browser.close();
log('updated', OUT);
