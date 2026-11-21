// Map the public signed-out tree of discord.com. Writes a JSON crawl outside
// the repo (MAP_OUT). Does not type, submit, or follow identity providers.
//
//   PLAYWRIGHT=... node map-tree.mjs
import fs from 'node:fs';
import { chromium } from '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs';

const OUT = process.env.MAP_OUT || '/Users/kaichen/.design-systems/discord/tree.json';
const START = 'https://discord.com/';
const MAX_PAGES = Number(process.env.MAX_PAGES || 70);

const WALL_PATH = /^\/(login|register|app|channels|invite|oauth2|verify|reset|mfa|select-account)(\/|$)/i;
const IDP = /accounts\.google\.|appleid\.apple|facebook\.com\/|login\.microsoft|github\.com\/login|twitter\.com\/i\/|x\.com\/i\/|sso|openid/i;
const SKIP_HOST = new Set([
  'twitter.com', 'www.twitter.com', 'x.com', 'www.instagram.com', 'www.facebook.com',
  'www.youtube.com', 'www.tiktok.com', 'discordmerch.com',
]);

function classify(url) {
  let u;
  try { u = new URL(url); } catch { return { kind: 'bad' }; }
  const host = u.hostname.replace(/^www\./, '');
  if (IDP.test(url)) return { kind: 'idp', host, path: u.pathname };
  if (SKIP_HOST.has(u.hostname) || SKIP_HOST.has(host)) return { kind: 'external-social', host, path: u.pathname };
  if (host === 'discordstatus.com') return { kind: 'external', host, path: u.pathname };
  if (host.endsWith('discord.com') || host.endsWith('discord.gg')) {
    if (WALL_PATH.test(u.pathname) || /\/requests\/new/.test(u.pathname)) return { kind: 'wall', host, path: u.pathname + u.search };
    return { kind: 'page', host, path: u.pathname + u.search };
  }
  return { kind: 'external', host, path: u.pathname };
}

function canon(url) {
  const u = new URL(url);
  u.hash = '';
  // drop tracking
  for (const k of [...u.searchParams.keys()]) {
    if (/^(utm_|fbclid|gclid)/.test(k)) u.searchParams.delete(k);
  }
  let p = u.pathname.replace(/\/$/, '') || '/';
  return u.origin + p + (u.search ? u.search : '');
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  locale: 'en-US',
  userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
});

const pages = [];
const edges = [];
const seen = new Set();
const queue = [{ url: START, from: null, control: 'start' }];

async function harvest(page) {
  return page.evaluate(() => {
    const abs = (href) => { try { return new URL(href, location.href).href; } catch { return null; } };
    const clean = (s) => (s || '').replace(/\s+/g, ' ').trim().slice(0, 90);
    const links = [...document.querySelectorAll('a[href]')].map((a) => {
      const r = a.getBoundingClientRect();
      const vis = r.width > 0 && r.height > 0;
      const inNav = !!a.closest('header, .w-nav, nav, footer, .nav_dd_list, .dropdown-list-footer');
      return {
        href: abs(a.getAttribute('href')),
        text: clean(a.innerText || a.getAttribute('aria-label')),
        cls: String(a.className).slice(0, 60),
        vis, inNav,
      };
    }).filter((l) => l.href && !l.href.startsWith('javascript') && !l.href.startsWith('mailto:') && !l.href.endsWith('.dmg') && !l.href.includes('/api/downloads'));
    const menus = [...document.querySelectorAll('.nav_dd_trigger, .dropdown-language, .footer .w-dropdown-toggle, button')].slice(0, 40).map((el) => ({
      text: clean(el.innerText || el.getAttribute('aria-label')),
      cls: String(el.className).slice(0, 80),
      expanded: el.getAttribute('aria-expanded'),
    }));
    const h1 = document.querySelector('h1')?.innerText?.replace(/\s+/g, ' ').trim().slice(0, 140) || null;
    const inputs = [...document.querySelectorAll('input, textarea, select')].slice(0, 12).map((i) => ({
      tag: i.tagName, type: i.type, name: i.name, aria: i.getAttribute('aria-label'), placeholder: i.placeholder,
    }));
    return { h1, title: document.title, links, menus, inputs, bg: getComputedStyle(document.body).backgroundColor };
  });
}

function isWallText(info, finalUrl) {
  const c = classify(finalUrl);
  if (c.kind === 'wall' || c.kind === 'idp') return true;
  const blob = (info.h1 || '') + ' ' + (info.title || '');
  if (/welcome back|create an account|email or phone/i.test(blob) && info.inputs?.some((i) => i.type === 'password')) return true;
  return false;
}

while (queue.length && pages.length < MAX_PAGES) {
  const job = queue.shift();
  let key;
  try { key = canon(job.url); } catch { continue; }
  if (seen.has(key)) continue;
  const kind0 = classify(key);
  if (kind0.kind !== 'page') {
    edges.push({ from: job.from, control: job.control, to: key, kind: kind0.kind, stopped: true });
    seen.add(key);
    continue;
  }
  seen.add(key);
  const page = await context.newPage();
  const row = { url: key, from: job.from, control: job.control };
  try {
    const res = await page.goto(key, { waitUntil: 'domcontentloaded', timeout: 40000 });
    await page.waitForTimeout(1200);
    row.status = res && res.status();
    row.final = page.url().split('#')[0];
    const info = await harvest(page);
    row.title = info.title;
    row.h1 = info.h1;
    row.bg = info.bg;
    row.inputCount = info.inputs.length;
    row.inputs = info.inputs.map((i) => i.aria || i.name || i.type);
    if (isWallText(info, row.final)) {
      row.kind = 'wall';
      row.stopped = true;
      edges.push({ from: job.from, control: job.control, to: row.final, kind: 'wall', stopped: true, h1: row.h1 });
      pages.push(row);
      console.log('WALL', row.final, row.h1);
      await page.close();
      continue;
    }
    row.kind = 'page';
    // unique outgoing
    const outgoing = new Map();
    for (const l of info.links) {
      let c;
      try { c = canon(l.href); } catch { continue; }
      const k = classify(c);
      if (!outgoing.has(c)) outgoing.set(c, { text: l.text, kind: k.kind, inNav: l.inNav, vis: l.vis });
    }
    row.outCount = outgoing.size;
    pages.push(row);
    edges.push({ from: job.from, control: job.control, to: key, kind: 'page', h1: row.h1, status: row.status });
    console.log('PAGE', pages.length, row.status, key, '|', row.h1);
    for (const [href, meta] of outgoing) {
      if (seen.has(href)) {
        edges.push({ from: key, control: meta.text || '(link)', to: href, kind: meta.kind, already: true });
        continue;
      }
      if (meta.kind === 'page' && (meta.inNav || href.startsWith('https://discord.com/'))) {
        // stay on discord.com marketing + public discovery; skip article pagination storms
        const path = new URL(href).pathname;
        if (/^\/blog\//.test(path) && pages.filter((p) => /\/blog\//.test(p.url || '')).length >= 2) {
          edges.push({ from: key, control: meta.text, to: href, kind: 'page', note: 'blog post sample cap' });
          continue;
        }
        if (/^\/servers\//.test(path) && pages.filter((p) => /\/servers\//.test(p.url || '')).length >= 2) {
          edges.push({ from: key, control: meta.text, to: href, kind: 'page', note: 'server listing sample cap' });
          continue;
        }
        queue.push({ url: href, from: key, control: meta.text || '(link)' });
      } else {
        edges.push({ from: key, control: meta.text || '(link)', to: href, kind: meta.kind, stopped: meta.kind !== 'page' });
      }
    }
  } catch (e) {
    row.error = String(e.message).split('\n')[0];
    row.kind = 'error';
    pages.push(row);
    console.log('ERR', key, row.error);
  }
  await page.close().catch(() => {});
}

const tree = {
  capturedAt: new Date().toISOString(),
  start: START,
  pageCount: pages.length,
  queuedLeft: queue.length,
  pages,
  edges,
};
fs.mkdirSync('/Users/kaichen/.design-systems/discord', { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(tree, null, 2));
console.log('WROTE', OUT, 'pages', pages.length, 'edges', edges.length, 'left', queue.length);
await browser.close();
