// Maps the public Nextdoor site tree from the homepage before any screenshot.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node map-tree.mjs
//
// Writes systems/nextdoor/site-tree.md and ~/.design-systems/nextdoor/site-tree.json.
// Never types, never submits, never clicks Google, Facebook, Apple, Continue,
// Log in, or Sign up. A control whose href or destination is a login or signup
// wall is recorded and that branch stops.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE } from './lib.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const OUT_MD = path.join(PKG, 'site-tree.md');
const OUT_JSON = path.join(os.homedir(), '.design-systems', 'nextdoor', 'site-tree.json');
fs.mkdirSync(path.dirname(OUT_JSON), { recursive: true });

const ALLOW = [
  'nextdoor.com',
  'about.nextdoor.com',
  'business.nextdoor.com',
  'blog.nextdoor.com',
  'help.nextdoor.com',
  'developer.nextdoor.com',
  'investors.nextdoor.com',
];

const WALL_PATH = /\/(login|signup|sign-up|sign_up|choose_address|create-business|join)(\/|$|\?)/i;
const OAUTH = /accounts\.google\.|appleid\.apple\.|facebook\.com|fb\.com/i;
const WALL_TEXT = /email or mobile number|email address[\s\S]{0,80}password|create a password|continue with google|continue with apple|continue with facebook/i;

function hostOf(url) {
  try { return new URL(url).hostname.replace(/^www\./, ''); } catch { return ''; }
}
function allowed(url) {
  const h = hostOf(url);
  return ALLOW.some((d) => h === d || h.endsWith('.' + d));
}
function canon(url) {
  try {
    const u = new URL(url);
    u.hash = '';
    u.hostname = u.hostname.replace(/^www\./, '');
    // drop tracking
    for (const k of [...u.searchParams.keys()]) {
      if (/^utm_|^hsCta|fbclid|gclid/i.test(k)) u.searchParams.delete(k);
    }
    let s = u.toString();
    if (s.endsWith('/') && u.pathname !== '/') s = s.slice(0, -1);
    return s;
  } catch { return url; }
}

function isWallUrl(url) {
  if (!url) return false;
  if (OAUTH.test(url)) return true;
  try {
    const u = new URL(url);
    if (WALL_PATH.test(u.pathname)) return true;
    if (/[?&]next=/.test(u.search) && /login/i.test(u.pathname)) return true;
  } catch { /* ignore */ }
  return false;
}

const MAX_PAGES = 36;
const seen = new Map();
const edges = [];

async function snapshot(page) {
  return page.evaluate(() => {
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return r.width > 1 && r.height > 1 && cs.visibility !== 'hidden' && cs.display !== 'none' && cs.opacity !== '0';
    };
    const txt = (el) => (el.innerText || el.getAttribute('aria-label') || el.getAttribute('title') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 140);
    const links = [...document.querySelectorAll('a[href]')].filter(vis).map((a) => ({
      kind: 'link', t: txt(a), h: a.href, region: a.closest('header, footer, nav, [role="dialog"], [role="menu"]') ? a.closest('header, footer, nav, [role="dialog"], [role="menu"]').tagName.toLowerCase() : 'body',
    }));
    const buttons = [...document.querySelectorAll('button, [role="button"]')].filter(vis).slice(0, 60).map((b) => ({
      kind: 'button', t: txt(b), expanded: b.getAttribute('aria-expanded'), popup: b.getAttribute('aria-haspopup'), id: b.id || '',
    }));
    const inputs = [...document.querySelectorAll('input, textarea, select')].slice(0, 12).map((i) => ({
      type: i.type || i.tagName.toLowerCase(), name: i.name || '', aria: i.getAttribute('aria-label') || '', ph: i.placeholder || '',
    }));
    return {
      title: document.title,
      url: location.href,
      text: (document.body?.innerText || '').replace(/\s+/g, ' ').slice(0, 600),
      links, buttons, inputs,
    };
  });
}

function credentialForm(info) {
  const inputs = info.inputs || [];
  const hasEmail = inputs.some((i) => /email|mobile|phone/i.test(`${i.aria} ${i.ph} ${i.name} ${i.type}`));
  const hasPass = inputs.some((i) => i.type === 'password' || /password/i.test(`${i.aria} ${i.ph}`));
  return hasEmail && hasPass;
}

// A dedicated wall is a login or signup page with nowhere public to go.
// The homepage embeds a signup card and also links to public pages, so it
// stays a public page: the card is recorded, and those controls are not used.
function wallFrom(info) {
  if (isWallUrl(info.url)) return true;
  if (!credentialForm(info)) return false;
  const publicLinks = (info.links || []).filter((l) => l.h && allowed(l.h) && !isWallUrl(l.h));
  return publicLinks.length < 8;
}

async function visit(context, url, from, control, depth) {
  const key = canon(url);
  if (seen.has(key)) {
    edges.push({ from, control, to: key, note: 'already mapped' });
    return;
  }
  if (isWallUrl(url) || !allowed(url)) {
    seen.set(key, { url, final: url, kind: isWallUrl(url) ? 'wall' : 'off-site', title: '', stopped: true });
    edges.push({ from, control, to: key, note: isWallUrl(url) ? 'STOP wall' : 'off-site, not followed' });
    return;
  }
  if (seen.size >= MAX_PAGES) {
    edges.push({ from, control, to: key, note: 'not visited: page cap' });
    return;
  }
  const page = await context.newPage();
  try {
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 35000 });
    await page.waitForTimeout(1800);
    const info = await snapshot(page);
    const final = canon(info.url);
    const kind = wallFrom(info) ? 'wall' : 'public';
    const rec = {
      url: key,
      final,
      status: resp && resp.status(),
      title: info.title,
      kind,
      stopped: kind === 'wall',
      credentialForm: credentialForm(info),
      text: info.text,
      buttons: info.buttons,
      inputs: info.inputs.map((i) => ({ type: i.type, aria: i.aria, ph: i.ph })),
      nLinks: info.links.length,
    };
    seen.set(key, rec);
    if (final !== key) seen.set(final, { ...rec, url: final, aliasOf: key });
    edges.push({ from, control, to: final, note: kind === 'wall' ? 'STOP wall' : 'opened' });
    if (kind === 'wall') return;

    // Open header menus that are buttons (Partners, Businesses) and record their links.
    for (const b of info.buttons.filter((x) => x.expanded === 'false' && /partners|businesses|menu|resources/i.test(x.t))) {
      try {
        const loc = page.getByRole('button', { name: b.t, exact: true });
        if (!(await loc.count())) continue;
        await loc.first().click({ timeout: 3000 });
        await page.waitForTimeout(500);
        const opened = await snapshot(page);
        const menuLinks = opened.links.filter((l) => !info.links.some((p) => p.h === l.h));
        rec.menus = rec.menus || [];
        rec.menus.push({ control: b.t, links: menuLinks.map((l) => ({ t: l.t, h: canon(l.h) })) });
        for (const l of menuLinks) {
          edges.push({ from: final, control: `menu:${b.t} → ${l.t || l.h}`, to: canon(l.h), note: 'menu item' });
        }
        await page.keyboard.press('Escape').catch(() => {});
        await page.waitForTimeout(200);
      } catch (e) {
        rec.menus = rec.menus || [];
        rec.menus.push({ control: b.t, error: String(e.message).split('\n')[0] });
      }
    }

    // Queue same-site links that are not walls. Cap per page.
    const queue = [];
    const fresh = await snapshot(page);
    for (const l of fresh.links) {
      if (!l.h || l.h.startsWith('mailto:') || l.h.startsWith('tel:') || l.h.startsWith('javascript:')) {
        edges.push({ from: final, control: l.t || l.h, to: l.h, note: 'not followed (mailto/tel/script)' });
        continue;
      }
      const c = canon(l.h);
      if (isWallUrl(c)) {
        if (!seen.has(c)) seen.set(c, { url: c, final: c, kind: 'wall', title: '', stopped: true, fromControl: l.t });
        edges.push({ from: final, control: l.t || '(unlabeled link)', to: c, note: 'STOP wall (href)' });
        continue;
      }
      if (!allowed(c)) {
        edges.push({ from: final, control: l.t || c, to: c, note: 'off-site, not followed' });
        continue;
      }
      if (l.h.includes('itunes.apple.com') || l.h.includes('play.google.com') || l.h.includes('apps.apple.com')) {
        edges.push({ from: final, control: l.t || c, to: c, note: 'app store, not followed' });
        continue;
      }
      queue.push({ c, t: l.t });
    }
    await page.close();
    const uniq = [];
    const have = new Set();
    for (const q of queue) {
      if (have.has(q.c) || seen.has(q.c)) continue;
      have.add(q.c);
      uniq.push(q);
    }
    // Prefer marketing/help/about over deep blog posts. Visit up to 18 new links per page, depth-limited.
    if (depth < 1) {
      const ranked = uniq.sort((a, b) => score(b.c) - score(a.c)).slice(0, 22);
      for (const q of ranked) await visit(context, q.c, final, q.t || q.c, depth + 1);
    } else {
      for (const q of uniq.slice(0, 8)) {
        edges.push({ from: final, control: q.t || q.c, to: q.c, note: 'linked, not crawled (depth cap)' });
      }
    }
    return;
  } catch (e) {
    seen.set(key, { url: key, final: key, kind: 'error', title: '', error: String(e.message).split('\n')[0], stopped: true });
    edges.push({ from, control, to: key, note: 'error: ' + String(e.message).split('\n')[0] });
  } finally {
    await page.close().catch(() => {});
  }
}

function score(url) {
  let s = 0;
  if (/about\.nextdoor|business\.nextdoor|help\.nextdoor|developer\.nextdoor/.test(url)) s += 5;
  if (/privacy|cookie|guideline|press|career|legal|terms|directory|agenc/.test(url)) s += 3;
  if (/blog\.nextdoor/.test(url)) s -= 1;
  if (/\/20\d\d\//.test(url)) s -= 2;
  return s;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  userAgent: UA,
  locale: 'en-US',
});
console.log('mapping from https://nextdoor.com/');
await visit(context, 'https://nextdoor.com/', '(start)', 'open homepage', 0);
await browser.close();

const pages = [...seen.values()].filter((p) => !p.aliasOf);
const md = [];
md.push('# Nextdoor public site tree');
md.push('');
md.push('Mapped from https://nextdoor.com/ in headless Playwright before any screenshot. A control that opens a login or signup wall is recorded and that branch stops. Nothing was typed or submitted. Google, Facebook and Apple were not clicked.');
md.push('');
md.push('Date: 2026-11-21. Viewport used for the map: 1440 x 900.');
md.push('');
md.push('## Pages');
md.push('');
md.push('| Start URL | Final | Kind | Title | Stopped |');
md.push('|---|---|---|---|---|');
for (const p of pages) {
  md.push(`| ${p.url} | ${p.final || ''} | ${p.kind} | ${(p.title || '').replace(/\|/g, '/')} | ${p.stopped ? 'yes' : 'no'} |`);
}
md.push('');
md.push('## Controls');
md.push('');
md.push('| From | Control | Opens | Note |');
md.push('|---|---|---|---|');
const uniqEdges = [];
const ek = new Set();
for (const e of edges) {
  const k = `${e.from}|${e.control}|${e.to}|${e.note}`;
  if (ek.has(k)) continue;
  ek.add(k);
  uniqEdges.push(e);
}
for (const e of uniqEdges) {
  const ctl = String(e.control || '').replace(/\|/g, '/').replace(/\n/g, ' ').slice(0, 120);
  md.push(`| ${e.from} | ${ctl} | ${e.to} | ${e.note} |`);
}
md.push('');
md.push('## Interactions on the homepage');
md.push('');
md.push('The homepage is a public marketing page with an embedded signup card. That card asks for an email and a password, and offers Continue, Google and Apple. Those controls are a signup wall: recorded, not used. The business-name field is part of the same card. Log in opens https://nextdoor.com/login/, which asks for email or mobile number and password, or Google, Facebook or Apple. That branch stops. Footer and header links that stay public are followed.');
md.push('');
md.push('Header buttons Partners and Businesses open menus. Their destinations are in the Controls table.');
md.push('');
fs.writeFileSync(OUT_MD, md.join('\n'));
fs.writeFileSync(OUT_JSON, JSON.stringify({ pages, edges: uniqEdges }, null, 2));
console.log('pages', pages.length, 'edges', uniqEdges.length);
console.log('wrote', OUT_MD);
