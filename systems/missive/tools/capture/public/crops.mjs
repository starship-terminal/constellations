// Crops measured controls from a fresh 2x desktop capture. Boxes come from
// getBoundingClientRect on the live page, multiplied by devicePixelRatio.
// Nothing is submitted.
import fs from 'node:fs';
import os from 'os';
import path from 'node:path';
import { launch, open, REF, BASE, MAIL } from './lib.mjs';

const OUT = path.join(REF, 'components', 'crops');
fs.mkdirSync(OUT, { recursive: true });
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'missive', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });

async function crop(page, name, selector, pad = 8) {
  const box = await page.evaluate(({ selector, pad }) => {
    const el = document.querySelector(selector);
    if (!el) return null;
    const r = el.getBoundingClientRect();
    if (r.width < 4 || r.height < 4) return null;
    return {
      x: Math.max(0, r.x - pad),
      y: Math.max(0, r.y - pad),
      width: r.width + pad * 2,
      height: r.height + pad * 2,
    };
  }, { selector, pad });
  if (!box) {
    console.log('  miss', name, selector);
    return;
  }
  const file = path.join(OUT, name + '.png');
  await page.screenshot({ path: file, clip: box });
  console.log('  crop', name, Math.round(box.width), 'x', Math.round(box.height));
}

async function pin(page, attr, finder) {
  await page.evaluate(({ attr, finder }) => {
    const fn = new Function('return (' + finder + ')')();
    const el = fn();
    if (el) el.setAttribute('data-m', attr);
  }, { attr, finder });
}

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 2 });
const page = await context.newPage();

await open(page, BASE + '/');
await pin(page, 'nav-try', `() => [...document.querySelectorAll('a')].find(el => (el.innerText||'').trim()==='Try for free' && el.getBoundingClientRect().y < 80)`);
await pin(page, 'nav-login', `() => [...document.querySelectorAll('a')].find(el => (el.innerText||'').trim()==='Log in' && el.getBoundingClientRect().y < 80)`);
await pin(page, 'nav-demo', `() => [...document.querySelectorAll('a')].find(el => (el.innerText||'').trim()==='Book a demo' && el.getBoundingClientRect().y < 80)`);
await pin(page, 'watch', `() => [...document.querySelectorAll('a')].find(el => (el.innerText||'').trim()==='Watch demo')`);
await pin(page, 'logo', `() => document.querySelector('svg.missive-logo')`);
await crop(page, 'nav-try-default', '[data-m="nav-try"]', 6);
await page.locator('[data-m="nav-try"]').hover();
await page.waitForTimeout(200);
await crop(page, 'nav-try-hover', '[data-m="nav-try"]', 6);
await crop(page, 'nav-login-default', '[data-m="nav-login"]', 4);
await page.locator('[data-m="nav-login"]').hover();
await page.waitForTimeout(150);
await crop(page, 'nav-login-hover', '[data-m="nav-login"]', 4);
await crop(page, 'nav-demo-default', '[data-m="nav-demo"]', 4);
await crop(page, 'watch-demo-default', '[data-m="watch"]', 6);
await page.locator('[data-m="watch"]').hover();
await page.waitForTimeout(150);
await crop(page, 'watch-demo-hover', '[data-m="watch"]', 6);
await crop(page, 'hero-title-default', 'h1', 4);
await crop(page, 'wordmark-default', '[data-m="logo"]', 4);

await open(page, MAIL + '/#login');
await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
await page.waitForTimeout(400);
await pin(page, 'title', `() => [...document.querySelectorAll('div')].find(el => (el.innerText||'').trim()==='Log in to Missive')`);
await pin(page, 'google', `() => [...document.querySelectorAll('button')].find(el => /Continue with Google/.test(el.innerText||''))`);
await pin(page, 'apple', `() => [...document.querySelectorAll('button')].find(el => /Continue with Apple/.test(el.innerText||''))`);
await pin(page, 'sso', `() => [...document.querySelectorAll('button')].find(el => /Single sign-on/.test(el.innerText||''))`);
await pin(page, 'forgot', `() => [...document.querySelectorAll('a')].find(el => /Forgot your password/.test(el.innerText||''))`);
await pin(page, 'create', `() => [...document.querySelectorAll('a')].find(el => /Create an account/.test(el.innerText||''))`);
await crop(page, 'login-title-default', '[data-m="title"]', 4);
await crop(page, 'login-google-default', '[data-m="google"]', 4);
await page.locator('[data-m="google"]').hover();
await page.waitForTimeout(180);
await crop(page, 'login-google-hover', '[data-m="google"]', 4);
await crop(page, 'login-apple-default', '[data-m="apple"]', 4);
await crop(page, 'login-sso-default', '[data-m="sso"]', 4);
await crop(page, 'login-email-default', 'input[type="email"]', 4);
await page.locator('input[type="email"]').focus();
await page.waitForTimeout(150);
await crop(page, 'login-email-focused', 'input[type="email"]', 6);
await crop(page, 'login-password-default', 'input[type="password"]', 4);
await crop(page, 'login-submit-default', 'button[type="submit"]', 4);
await page.locator('button[type="submit"]').hover();
await page.waitForTimeout(180);
await crop(page, 'login-submit-hover', 'button[type="submit"]', 4);
await crop(page, 'login-forgot-default', '[data-m="forgot"]', 4);
await page.locator('[data-m="forgot"]').hover();
await page.waitForTimeout(150);
await crop(page, 'login-forgot-hover', '[data-m="forgot"]', 4);
await crop(page, 'login-create-default', '[data-m="create"]', 4);

await open(page, BASE + '/pricing');
await pin(page, 'plan', `() => [...document.querySelectorAll('div')].find(el => {
  const t = (el.innerText||'').trim();
  const r = el.getBoundingClientRect();
  return t.startsWith('Starter') && t.includes('per user') && r.height > 200 && r.height < 700 && r.width > 200 && r.width < 500;
})`);
await crop(page, 'plan-card-default', '[data-m="plan"]', 2);
await pin(page, 'yearly', `() => [...document.querySelectorAll('*')].find(el => (el.innerText||'').trim()==='Billed yearly' && el.children.length < 3)`);
await crop(page, 'billing-label-default', '[data-m="yearly"]', 8);

await browser.close();
console.log('crops', fs.readdirSync(OUT).filter(n => n.endsWith('.png')).length);
