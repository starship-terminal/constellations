// Maps the public signed-out tree of designmodo.com from the homepage and
// photographs distinct pages plus opened menus. Does not submit forms, type
// a password, click an identity provider, or enter a builder canvas.
//
//   PLAYWRIGHT=... node crawl.mjs
//
// Writes ~/.design-systems/designmodo/crawl.json and raw full-colour shots.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';
import { screenshotWithMetadata } from '../screenshot.mjs';

const SCRATCH = process.env.RAW || path.join(os.homedir(), '.design-systems', 'designmodo', 'raw-shots');
fs.mkdirSync(SCRATCH, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const WALL = /\/my-account\/(sign-in|sign-up|lost-password|sso)|\/auth\/|\/slides\/sign-up|\/slides\/login|accounts\.google|appleid\.apple|facebook\.com|login\.microsoft|github\.com\/login/i;
const BUILDER = /\/postcards\/app\/|\/slides\/app\/|\/startup\/app\//i;
const SKIP_PATH = /add-to-cart|\/wp-admin|\/wp-login|\/cart\/?$|\/checkout|\/feed\/?$|\.(pdf|zip|png|jpe?g|svg|css|js)$/i;

function normPath(href) {
  try {
    const u = new URL(href, BASE);
    if (!/designmodo\.com$/.test(u.hostname)) return null;
    let p = u.pathname.replace(/\/+$/, '') || '/';
    if (SKIP_PATH.test(p + u.search)) return null;
    if (/\/page\/\d+$/.test(p) && !/\/page\/2$/.test(p)) return null;
    return { host: u.hostname, path: p, url: u.origin + p + (u.hash && u.hash !== '#' ? '' : '') };
  } catch {
    return null;
  }
}

async function shot(page, file, requested) {
  await screenshotWithMetadata(page, { path: file }, requested);
}

async function pageFacts(page) {
  return page.evaluate(() => {
    const text = (document.body?.innerText || '').replace(/\s+/g, ' ').trim();
    const h1 = (document.querySelector('h1')?.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 140);
    const inputs = [...document.querySelectorAll('input, textarea, select')].slice(0, 20).map((e) => ({
      tag: e.tagName.toLowerCase(),
      type: e.getAttribute('type'),
      name: e.getAttribute('name'),
      placeholder: e.getAttribute('placeholder'),
    }));
    const buttons = [...document.querySelectorAll('button, [role="button"]')].slice(0, 30).map((e) => ({
      text: (e.innerText || e.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 60),
      aria: e.getAttribute('aria-label'),
    })).filter((b) => b.text || b.aria);
    const links = [];
    const seen = new Set();
    for (const a of document.querySelectorAll('a[href]')) {
      const href = a.href;
      const label = (a.innerText || a.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80);
      const key = href + '|' + label;
      if (seen.has(key)) continue;
      seen.add(key);
      const where = a.closest('header') ? 'header'
        : a.closest('footer') ? 'footer'
        : a.closest('.dropdown') ? 'dropdown'
        : a.closest('nav') ? 'nav'
        : 'body';
      links.push({ href, label, where });
      if (links.length > 400) break;
    }
    return {
      title: document.title,
      h1,
      snippet: text.slice(0, 280),
      loginWall: /login to designmodo|your email|password required|login with google|login with sso|create account|start using designmodo/i.test(text.slice(0, 900)),
      inputs,
      buttons,
      links,
    };
  });
}

const tree = [];
const visited = new Set();
const queue = [{ url: BASE + '/', from: 'start', control: 'open https://designmodo.com/' }];

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
const page = await context.newPage();
page.setDefaultTimeout(12000);
const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, sanitizedSourceUrl: null };

const MAX = 48;
while (queue.length && visited.size < MAX) {
  const item = queue.shift();
  const n = normPath(item.url);
  if (!n) continue;
  const key = n.host + n.path;
  if (visited.has(key)) continue;
  if (WALL.test(n.path) && visited.size > 0 && n.path !== '/my-account/sign-in') {
    tree.push({
      url: n.url, path: n.path, from: item.from, control: item.control,
      kind: 'wall', note: 'login or signup wall; branch stopped, form not filled',
    });
    visited.add(key);
    continue;
  }
  if (BUILDER.test(n.path)) {
    tree.push({
      url: n.url, path: n.path, from: item.from, control: item.control,
      kind: 'builder', note: 'builder canvas; branch stopped, not entered',
    });
    visited.add(key);
    continue;
  }
  visited.add(key);
  let status = 0;
  try {
    const resp = await page.goto(n.url, { waitUntil: 'load', timeout: 50000 });
    status = resp?.status() || 0;
    await page.waitForTimeout(1600);
    await hideConsent(page);
    await page.waitForFunction(() => {
      const text = (document.body && document.body.innerText) || '';
      return text.trim().length > 40 && document.documentElement.scrollHeight > 200;
    }, { timeout: 15000 }).catch(() => {});
    await page.waitForTimeout(500);
  } catch (e) {
    tree.push({ url: n.url, path: n.path, from: item.from, control: item.control, kind: 'error', note: String(e.message).split('\n')[0] });
    log('FAIL', n.path, e.message.split('\n')[0]);
    continue;
  }
  const final = page.url();
  const facts = await pageFacts(page);
  const wallNow = WALL.test(new URL(final).pathname) || facts.loginWall && /sign-in|sign-up|lost-password|sso/.test(final);
  const kind = wallNow ? 'wall' : /help\.designmodo/.test(final) ? 'help' : 'page';
  const slug = (n.path === '/' ? 'home' : n.path.replace(/^\//, '').replace(/\//g, '-')).slice(0, 80);
  const file = path.join(SCRATCH, `tree-${slug}-desktop.png`);
  if (kind === 'page' || n.path === '/my-account/sign-in') {
    requested.sanitizedSourceUrl = n.url;
    await shot(page, file, requested).catch((e) => log('shot fail', e.message));
  }
  const node = {
    url: final.split('?')[0],
    path: n.path,
    status,
    from: item.from,
    control: item.control,
    kind,
    title: facts.title,
    h1: facts.h1,
    snippet: facts.snippet,
    inputs: facts.inputs.filter((i) => i.type !== 'hidden'),
    shot: kind === 'page' || n.path === '/my-account/sign-in' ? path.basename(file) : null,
  };
  tree.push(node);
  log(status, kind, n.path, '|', facts.h1 || facts.title.slice(0, 60));

  if (kind === 'wall' && n.path !== '/my-account/sign-in') continue;

  // Enqueue same-host links that look like navigation, not every article.
  const interesting = /\/(postcards|slides|startup|email-templates|website-templates|articles|products|about|contacts|subscribe|pricing|black-friday|privacy|terms|cookies|dpa|resources|tools|my-account)(\/|$)/;
  let added = 0;
  for (const link of facts.links) {
    const c = normPath(link.href);
    if (!c) continue;
    if (c.host !== 'designmodo.com' && c.host !== 'www.designmodo.com' && c.host !== 'help.designmodo.com') continue;
    const k = c.host + c.path;
    if (visited.has(k)) continue;
    if (c.host === 'help.designmodo.com') {
      if (![...queue, ...tree].some((x) => x.url && x.url.includes('help.designmodo.com'))) {
        queue.push({ url: c.url, from: n.path, control: `${link.where} link "${link.label || c.path}"` });
      }
      continue;
    }
    const isNav = link.where === 'header' || link.where === 'footer' || link.where === 'nav' || link.where === 'dropdown';
    const keep = isNav || interesting.test(c.path) || c.path.split('/').length <= 2;
    if (!keep) continue;
    if (added > 24 && !isNav) continue;
    queue.push({ url: c.url, from: n.path, control: `${link.where} link "${link.label || c.path}"` });
    added++;
  }
}

fs.writeFileSync(path.join(SCRATCH, 'tree.json'), JSON.stringify(tree, null, 2));
log('tree nodes', tree.length, 'visited', visited.size);
await browser.close();
