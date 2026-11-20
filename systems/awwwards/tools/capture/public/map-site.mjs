// Maps the public awwwards.com tree from the homepage before any screenshot pass.
// Writes systems/awwwards/site-tree.md. Never types, submits, votes, or follows
// login, signup, Google, Apple, or Facebook. A control that opens a login or
// signup wall is recorded and that branch stops.
//
//   PLAYWRIGHT=... node map-site.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE, patch } from './lib.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const OUT = path.join(PKG, 'site-tree.md');
const SCRATCH = process.env.MAP_DIR || path.join(process.env.HOME, '.design-systems', 'awwwards', 'map');
fs.mkdirSync(SCRATCH, { recursive: true });

const HOSTS = new Set(['www.awwwards.com', 'awwwards.com']);
const AUTH_PATH = /\/(login|signin|sign-in|signup|sign-up|register|auth|session|account|oauth|sso)(\/|$|\?)/i;
const AUTH_TEXT = /\b(log\s*in|sign\s*in|sign\s*up|create\s*(an\s*)?account|continue with google|continue with apple|continue with facebook|email or username|password)\b/i;
const SOCIAL = /\b(google|apple|facebook)\b/i;
const SKIP_CLICK_TEXT = /^(accept|reject|allow|deny|subscribe|join|vote|submit|send|search|apply|buy|checkout|newsletter)/i;

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

function abs(href, base) {
  try { return new URL(href, base).href; } catch { return null; }
}
function sameHost(u) {
  try { return HOSTS.has(new URL(u).hostname); } catch { return false; }
}
function pathOf(u) {
  try {
    const x = new URL(u);
    return x.pathname + (x.search || '');
  } catch { return u; }
}
function isAuth(u, text = '') {
  return AUTH_PATH.test(u || '') || AUTH_TEXT.test(text || '');
}

async function pageFacts(page) {
  return page.evaluate(() => {
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none' && Number(cs.opacity) > 0;
    };
    const label = (el) => {
      const t = (el.innerText || el.getAttribute('aria-label') || el.getAttribute('title') || '').replace(/\s+/g, ' ').trim();
      return t.slice(0, 80);
    };
    const links = [];
    const seen = new Set();
    for (const a of document.querySelectorAll('a[href]')) {
      if (!vis(a)) continue;
      const href = a.getAttribute('href') || '';
      const text = label(a);
      const key = href + '|' + text;
      if (seen.has(key)) continue;
      seen.add(key);
      const r = a.getBoundingClientRect();
      links.push({
        href,
        text,
        region: r.top < 80 ? 'header' : r.top > innerHeight - 80 ? 'sticky' : 'body',
      });
    }
    const buttons = [];
    const bseen = new Set();
    for (const el of document.querySelectorAll('button, [role="button"], summary, [aria-haspopup], [aria-expanded]')) {
      if (!vis(el)) continue;
      const text = label(el);
      const key = (el.tagName + '|' + text + '|' + (el.getAttribute('aria-controls') || '')).slice(0, 160);
      if (bseen.has(key)) continue;
      bseen.add(key);
      buttons.push({
        tag: el.tagName.toLowerCase(),
        text,
        expanded: el.getAttribute('aria-expanded'),
        controls: el.getAttribute('aria-controls'),
        popup: el.getAttribute('aria-haspopup'),
        cls: (el.className && String(el.className).slice(0, 80)) || '',
      });
    }
    const dialogs = [...document.querySelectorAll('[role="dialog"], [role="alertdialog"], dialog')].filter(vis).map((el) => ({
      text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 180),
      role: el.getAttribute('role') || el.tagName.toLowerCase(),
    }));
    const nav = [...document.querySelectorAll('nav a[href], header a[href]')].filter(vis).map((a) => ({
      text: label(a),
      href: a.getAttribute('href'),
    }));
    return {
      title: document.title,
      url: location.href,
      h1: (document.querySelector('h1')?.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 120),
      innerWidth: window.innerWidth,
      innerHeight: window.innerHeight,
      dpr: window.devicePixelRatio,
      links: links.slice(0, 250),
      buttons: buttons.slice(0, 80),
      dialogs,
      nav: nav.slice(0, 40),
      bodyStart: (document.body?.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 400),
    };
  });
}

async function launch(mobile) {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

async function open(page, url) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch((e) => ({ failed: String(e.message).split('\n')[0] }));
  await page.waitForTimeout(4500);
  const status = res && res.status ? res.status() : (res && res.failed ? 0 : null);
  return { status, failed: res && res.failed };
}

const AUTH_WALL = /email or username|password|sign in to|log in to|create your account|continue with google|continue with apple|continue with facebook/i;

async function classify(page, url) {
  const facts = await pageFacts(page).catch(() => null);
  const text = facts ? facts.bodyStart : '';
  const wall = AUTH_PATH.test(url) || AUTH_WALL.test(text);
  return { facts, wall, text };
}

async function mapWidth(mobile) {
  const label = mobile ? 'phone' : 'desktop';
  log('map', label);
  const { browser, context } = await launch(mobile);
  const page = await context.newPage();
  const pages = [];
  const controls = [];
  const walls = [];
  const external = [];
  const visited = new Set();
  const queue = ['https://www.awwwards.com/'];

  const seed = await open(page, queue[0]);
  const home = await classify(page, page.url());
  pages.push({
    url: page.url(),
    status: seed.status,
    title: home.facts?.title,
    h1: home.facts?.h1,
    width: home.facts?.innerWidth,
    height: home.facts?.innerHeight,
    dpr: home.facts?.dpr,
    wall: home.wall,
    from: 'start',
  });
  visited.add(pathOf(page.url()));
  fs.writeFileSync(path.join(SCRATCH, `${label}-home.json`), JSON.stringify(home, null, 1));

  const homeLinks = home.facts?.links || [];
  const homeButtons = home.facts?.buttons || [];
  const homeNav = home.facts?.nav || [];

  // Queue unique same-host paths from the homepage, skipping auth.
  const candidates = [];
  for (const a of homeLinks) {
    const u = abs(a.href, 'https://www.awwwards.com/');
    if (!u) continue;
    if (!sameHost(u)) {
      external.push({ text: a.text, href: u, from: '/' });
      continue;
    }
    const pth = pathOf(u);
    if (AUTH_PATH.test(pth) || AUTH_TEXT.test(a.text)) {
      walls.push({ control: a.text || a.href, opens: u, stop: 'login or signup wall', from: '/' });
      continue;
    }
    if (SOCIAL.test(a.text) && /google|apple|facebook/i.test(a.href + a.text)) {
      walls.push({ control: a.text, opens: u, stop: 'social login', from: '/' });
      continue;
    }
    candidates.push({ text: a.text, href: u, path: pth, region: a.region });
  }

  // Deduplicate by path, keep first label.
  const byPath = new Map();
  for (const c of candidates) {
    const key = c.path.replace(/\/$/, '') || '/';
    if (!byPath.has(key)) byPath.set(key, c);
  }

  // Prefer nav and header paths, then a bounded set of body paths (section indexes, not every card).
  const preferred = [...byPath.values()].sort((a, b) => {
    const score = (x) => (x.region === 'header' ? 0 : x.region === 'sticky' ? 2 : 1);
    return score(a) - score(b);
  });
  const sectionish = preferred.filter((c) => {
    const p = c.path.split('?')[0];
    const segs = p.split('/').filter(Boolean);
    // Keep indexes and one-segment pages. Skip deep site-detail slugs for the tree seed;
    // one representative /sites/ page is kept separately below.
    if (segs[0] === 'sites' && segs.length > 1) return false;
    if (segs[0] === 'websites' && segs.length > 2) return false;
    return segs.length <= 2;
  });
  const oneSite = preferred.find((c) => /\/sites\//.test(c.path));
  const toVisit = [...sectionish];
  if (oneSite) toVisit.push(oneSite);

  // Cap so a huge directory cannot run forever. Nav + section indexes first.
  const CAP = 40;
  const slice = toVisit.slice(0, CAP);
  log(label, 'home links', homeLinks.length, 'queued', slice.length, 'of', toVisit.length);

  for (const c of slice) {
    const key = (c.path.replace(/\/$/, '') || '/');
    if (visited.has(key) || visited.has(c.path)) continue;
    visited.add(key);
    const opened = await open(page, c.href);
    const landed = page.url();
    const info = await classify(page, landed);
    const row = {
      control: c.text || c.path,
      from: '/',
      requested: c.href,
      landed,
      status: opened.status,
      title: info.facts?.title,
      h1: info.facts?.h1,
      wall: info.wall || isAuth(landed, info.text),
      width: info.facts?.innerWidth,
      height: info.facts?.innerHeight,
    };
    if (row.wall) {
      walls.push({ control: row.control, opens: landed, stop: 'login or signup wall', from: '/' });
      log('  WALL', c.path);
      continue;
    }
    pages.push(row);
    log('  page', pathOf(landed), opened.status, (info.facts?.title || '').slice(0, 60));
    // Record controls on this page (do not follow them further except noting auth).
    for (const b of info.facts?.buttons || []) {
      controls.push({ page: pathOf(landed), kind: 'button', text: b.text, expanded: b.expanded, popup: b.popup, cls: b.cls });
    }
    for (const a of info.facts?.links || []) {
      const u = abs(a.href, landed);
      if (!u) continue;
      if (!sameHost(u)) {
        if (external.length < 80) external.push({ text: a.text, href: u.split('?')[0], from: pathOf(landed) });
        continue;
      }
      if (AUTH_PATH.test(u) || AUTH_TEXT.test(a.text)) {
        walls.push({ control: a.text || a.href, opens: u, stop: 'login or signup wall', from: pathOf(landed) });
      }
    }
    // Probe a few non-auth buttons that look like menus (aria-expanded or menu-like text).
    const menuish = (info.facts?.buttons || []).filter((b) => b.expanded !== null || /menu|filter|explore|more|search/i.test(b.text + b.cls));
    for (const b of menuish.slice(0, 6)) {
      if (SKIP_CLICK_TEXT.test(b.text) || AUTH_TEXT.test(b.text) || SOCIAL.test(b.text)) continue;
      const before = page.url();
      const clicked = await page.evaluate((text) => {
        const vis = (el) => {
          const r = el.getBoundingClientRect();
          const cs = getComputedStyle(el);
          return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none';
        };
        const el = [...document.querySelectorAll('button, [role="button"], summary')].find((n) => vis(n) && ((n.innerText || n.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80) === text));
        if (!el) return false;
        el.click();
        return true;
      }, b.text).catch(() => false);
      if (!clicked) continue;
      await page.waitForTimeout(900);
      const after = page.url();
      const dialogs = await page.evaluate(() => [...document.querySelectorAll('[role="dialog"], [role="alertdialog"], dialog, [aria-expanded="true"]')].filter((el) => {
        const r = el.getBoundingClientRect();
        return r.width > 40 && r.height > 20;
      }).slice(0, 4).map((el) => ({
        role: el.getAttribute('role') || el.tagName.toLowerCase(),
        text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 120),
      })));
      controls.push({
        page: pathOf(before),
        kind: 'interaction',
        text: b.text,
        opened: after !== before ? after : (dialogs[0] ? 'in-page overlay' : 'no navigation'),
        dialogs,
      });
      if (after !== before) {
        if (isAuth(after)) walls.push({ control: b.text, opens: after, stop: 'login or signup wall', from: pathOf(before) });
        await page.goto(before, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(() => {});
        await page.waitForTimeout(1500);
      } else {
        await page.keyboard.press('Escape').catch(() => {});
        await page.waitForTimeout(300);
      }
    }
  }

  // Known probe: login wall. Open it, record, do not type.
  const login = await open(page, 'https://www.awwwards.com/login');
  const loginInfo = await classify(page, page.url());
  walls.push({
    control: 'known probe /login',
    opens: page.url(),
    status: login.status,
    stop: 'asks for email or username and a password; not entered',
    evidence: (loginInfo.text || '').slice(0, 180),
  });

  await browser.close();
  return { label, home, homeNav, homeButtons, pages, controls, walls, external, visited: [...visited] };
}

const desktop = await mapWidth(false);
const phone = await mapWidth(true);

const md = [];
const esc = (s) => String(s ?? '').replace(/\|/g, '/').replace(/\n/g, ' ').slice(0, 140);
md.push('# Awwwards public site tree');
md.push('');
md.push(`Mapped ${new Date().toISOString().slice(0, 10)} from https://www.awwwards.com/ in headless Chrome (Playwright), before screenshots. Desktop 1440x900 and phone 390x844. Signed out. No form was submitted, no password typed, no social login clicked.`);
md.push('');
md.push('A control that opens a login or signup wall is listed under Walls and that branch stops.');
md.push('');
md.push('## Homepage controls (desktop)');
md.push('');
md.push('| Control | Kind | Opens |');
md.push('|---|---|---|');
for (const n of desktop.homeNav || []) {
  md.push(`| ${esc(n.text) || '(unlabeled)'} | header/nav link | ${esc(n.href)} |`);
}
for (const b of desktop.homeButtons || []) {
  md.push(`| ${esc(b.text) || '(unlabeled)'} | button ${esc(b.cls)} | ${b.popup ? 'popup ' + b.popup : b.expanded != null ? 'aria-expanded=' + b.expanded : 'in-page'} |`);
}
md.push('');
md.push('## Pages reached from the homepage');
md.push('');
md.push('Desktop walk. Phone walk is compared in the next section. Deep `/sites/<slug>` entries are represented by one sample; the directory is unbounded.');
md.push('');
md.push('| Control on / | Requested | Landed | Status | Title | Wall |');
md.push('|---|---|---|---|---|---|');
for (const p of desktop.pages) {
  md.push(`| ${esc(p.control || p.from)} | ${esc(p.requested || p.url)} | ${esc(p.landed || p.url)} | ${p.status ?? ''} | ${esc(p.title)} | ${p.wall ? 'yes' : ''} |`);
}
md.push('');
md.push('## Phone homepage');
md.push('');
md.push(`Measured viewport ${phone.pages[0]?.width}x${phone.pages[0]?.height} at dpr ${phone.pages[0]?.dpr}. Title: ${esc(phone.pages[0]?.title)}.`);
md.push('');
md.push('| Control | Kind | Opens |');
md.push('|---|---|---|');
for (const n of phone.home?.facts?.nav || []) {
  md.push(`| ${esc(n.text) || '(unlabeled)'} | header/nav link | ${esc(n.href)} |`);
}
for (const b of phone.homeButtons || phone.home?.facts?.buttons || []) {
  md.push(`| ${esc(b.text) || '(unlabeled)'} | button | ${b.popup || (b.expanded != null ? 'expanded=' + b.expanded : 'in-page')} |`);
}
md.push('');
md.push('## Interactions probed (menus, dialogs)');
md.push('');
md.push('| Page | Control | Result |');
md.push('|---|---|---|');
for (const c of [...desktop.controls, ...phone.controls].filter((c) => c.kind === 'interaction' || c.kind === 'button')) {
  if (c.kind === 'button' && !c.popup && c.expanded == null) continue;
  md.push(`| ${esc(c.page)} | ${esc(c.text)} | ${esc(c.opened || c.popup || c.expanded || '')} |`);
}
md.push('');
md.push('## Walls (branch stopped)');
md.push('');
md.push('| Control | Opens | Why stopped | From |');
md.push('|---|---|---|---|');
const wallSeen = new Set();
for (const w of [...desktop.walls, ...phone.walls]) {
  const key = (w.control || '') + '|' + (w.opens || '');
  if (wallSeen.has(key)) continue;
  wallSeen.add(key);
  md.push(`| ${esc(w.control)} | ${esc(w.opens)} | ${esc(w.stop)} | ${esc(w.from)} |`);
}
md.push('');
md.push('## External links (not followed)');
md.push('');
const extSeen = new Set();
md.push('| Text | URL | From |');
md.push('|---|---|---|');
for (const e of [...desktop.external, ...phone.external]) {
  const key = e.href;
  if (extSeen.has(key)) continue;
  extSeen.add(key);
  if (extSeen.size > 40) break;
  md.push(`| ${esc(e.text)} | ${esc(e.href)} | ${esc(e.from)} |`);
}
md.push('');
md.push('## Not in this tree');
md.push('');
md.push('- Individual winner pages beyond one sample `/sites/` entry. The directory is unbounded.');
md.push('- Search results, votes, submissions, newsletter signup, and account creation. No form was submitted.');
md.push('- Any page that required a password, a code, a captcha, or a social login.');
md.push('');

fs.writeFileSync(OUT, md.join('\n'));
fs.writeFileSync(path.join(SCRATCH, 'desktop.json'), JSON.stringify(desktop, null, 1));
fs.writeFileSync(path.join(SCRATCH, 'phone.json'), JSON.stringify({ pages: phone.pages, walls: phone.walls, buttons: phone.home?.facts?.buttons, nav: phone.home?.facts?.nav }, null, 1));
log('wrote', OUT, 'pages', desktop.pages.length, 'walls', wallSeen.size);
