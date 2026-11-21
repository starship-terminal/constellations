// Map www.docusign.com from the homepage and photograph distinct public pages.
//
//   RAW=~/.design-systems/docusign/raw-shots PLAYWRIGHT=... node map-site.mjs
//
// Signed-out only. A control that opens a login, signup, account, or checkout
// wall is recorded and that branch stops. Nothing is typed. No SSO. No forms.
// No downloads. Cookie banners are hidden, never accepted.
import fs from 'node:fs';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE } from './lib.mjs';

const RAW = process.env.RAW || path.join(process.env.HOME, '.design-systems/docusign/raw-shots');
const OUT = process.env.OUT || path.join(process.env.HOME, '.design-systems/docusign');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });

const START = 'https://www.docusign.com/';
const MAX_PAGES = Number(process.env.MAX_PAGES || 90);
const MAX_SHOTS = Number(process.env.MAX_SHOTS || 220);

const WALL_HOSTS = [
  'account.docusign.com',
  'apps.docusign.com',
  'trial.docusign.com',
  'ecom.docusign.com',
  'go.docusign.com',
  'partners.docusign.com',
  'login.docusign.com',
  'admin.docusign.com',
  'app.docusign.com',
  'na1.docusign.net',
  'na2.docusign.net',
  'na3.docusign.net',
  'na4.docusign.net',
  'eu.docusign.net',
  'account-d.docusign.com',
];
const STORE_HOSTS = ['apps.apple.com', 'play.google.com', 'itunes.apple.com'];
const SKIP_HOSTS = new Set([
  'facebook.com', 'www.facebook.com', 'x.com', 'twitter.com', 'www.youtube.com',
  'youtube.com', 'www.linkedin.com', 'linkedin.com', 'instagram.com',
]);

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const slugify = (s) => s.toLowerCase().replace(/https?:\/\//, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 80);

function classify(url) {
  let u;
  try { u = new URL(url); } catch { return { kind: 'bad', host: '', path: '' }; }
  const host = u.hostname.replace(/^www\./, '');
  const pathName = u.pathname.replace(/\/$/, '') || '/';
  if (STORE_HOSTS.some((h) => host === h || host.endsWith('.' + h))) return { kind: 'store', host, path: pathName };
  if (WALL_HOSTS.some((h) => host === h || host.endsWith('.' + h))) return { kind: 'wall', host, path: pathName };
  if (/\/(login|signin|sign-in|signup|sign-up|checkout|cart)(\/|$)/i.test(pathName)) return { kind: 'wall', host, path: pathName };
  if (host === 'support.docusign.com' || host === 'community.docusign.com' || host === 'developers.docusign.com'
    || host === 'investor.docusign.com' || host === 'careers.docusign.com' || host === 'events.docusign.com'
    || host === 'momentum.docusign.com' || host === 'dsucustomers.docusign.com' || host === 'pref.docusign.com') {
    return { kind: 'sibling', host, path: pathName };
  }
  if (host === 'docusign.com') return { kind: 'public', host, path: pathName };
  if (SKIP_HOSTS.has(u.hostname) || SKIP_HOSTS.has(host)) return { kind: 'external', host, path: pathName };
  return { kind: 'external', host, path: pathName };
}

function templateKey(url) {
  const { kind, host, path: p } = classify(url);
  if (kind !== 'public') return `${kind}:${host}${p}`;
  const parts = p.split('/').filter(Boolean);
  if (parts[0] === 'blog' && parts.length > 1) return 'tpl:/blog/{post}';
  if (parts[0] === 'customer-stories' && parts.length > 2) return `tpl:/customer-stories/${parts[1]}/{item}`;
  if (parts[0] === 'customer-stories' && parts.length === 2 && !['industry', 'capabilities', 'department'].includes(parts[1])) return 'tpl:/customer-stories/{story}';
  if (parts[0] === 'trust' && parts[1] === 'alerts' && parts.length > 2) return 'tpl:/trust/alerts/{alert}';
  if (parts[0] === 'company' && parts[1] === 'news-center' && parts.length > 2) return 'tpl:/company/news-center/{item}';
  if (parts[0] === 'legal' && parts.length > 2) return `tpl:/legal/${parts[1]}/{doc}`;
  if (parts[0] === 'learn' && parts.length > 2) return `tpl:/learn/${parts[1]}/{item}`;
  if (parts[0] === 'resources' && parts.length > 2) return `tpl:/resources/${parts[1]}/{item}`;
  if (parts[0] === 'templates' && parts.length > 1) return 'tpl:/templates/{template}';
  if (parts[0] === 'integrations' && parts.length > 1) return 'tpl:/integrations/{integration}';
  if (parts[0] === 'products' && parts.length > 3) return `tpl:/products/${parts[1]}/${parts[2]}/{leaf}`;
  if (parts[0] === 'lp' && parts.length > 1) return 'tpl:/lp/{campaign}';
  return 'page:' + p;
}

const pages = [];
const controls = [];
const walls = [];
const visited = new Set();
const shotTemplates = new Set();
let shots = 0;

function recordControl(from, control, to, kind, note) {
  controls.push({ from, control, to, kind, note: note || '' });
}

async function shoot(page, name, requested) {
  if (shots >= MAX_SHOTS) return false;
  const file = path.join(RAW, name + '.png');
  await screenshotWithMetadata(page, { path: file }, requested);
  shots++;
  log('shot', name);
  return true;
}

async function hidePromo(page) {
  await page.evaluate(() => {
    const hide = (el) => el && el.style.setProperty('display', 'none', 'important');
    document.querySelectorAll('[class*="cookie" i], [id*="cookie" i], [class*="consent" i], #onetrust-banner-sdk, #onetrust-consent-sdk, .ot-sdk-container').forEach((el) => {
      const cs = getComputedStyle(el);
      if (cs.position === 'fixed' || cs.position === 'sticky' || el.id.includes('onetrust')) hide(el);
    });
    for (const el of document.querySelectorAll('[role="dialog"], [role="alertdialog"], div, aside')) {
      const t = (el.innerText || '').slice(0, 400);
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if ((cs.position === 'fixed' || cs.position === 'sticky') && /cookie|privacy preference|we value your privacy/i.test(t) && r.height < 500 && r.width > 200) hide(el);
    }
  }).catch(() => {});
}

async function pageFacts(page) {
  return page.evaluate(() => {
    const text = (el) => (el.innerText || el.getAttribute('aria-label') || el.getAttribute('title') || '').replace(/\s+/g, ' ').trim().slice(0, 140);
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return r.width > 8 && r.height > 8 && cs.visibility !== 'hidden' && cs.display !== 'none' && Number(cs.opacity) !== 0;
    };
    const nav = [...document.querySelectorAll('header a, header button, nav a, nav button')].filter(vis).map((el) => ({
      tag: el.tagName,
      text: text(el),
      href: el.href || '',
      expanded: el.getAttribute('aria-expanded'),
      controls: el.getAttribute('aria-controls'),
      haspopup: el.getAttribute('aria-haspopup'),
    }));
    const interactions = [...document.querySelectorAll('button, [role="tab"], summary, [aria-expanded], [aria-haspopup]')].filter(vis).slice(0, 80).map((el) => ({
      tag: el.tagName,
      role: el.getAttribute('role'),
      text: text(el).slice(0, 80),
      expanded: el.getAttribute('aria-expanded'),
      controls: el.getAttribute('aria-controls'),
      haspopup: el.getAttribute('aria-haspopup'),
    }));
    const links = [...document.querySelectorAll('a[href]')].map((a) => a.href);
    return {
      title: document.title,
      h1: (document.querySelector('h1') && document.querySelector('h1').innerText || '').replace(/\s+/g, ' ').trim().slice(0, 160),
      nav,
      interactions,
      links,
      bodyLen: (document.body && document.body.innerText || '').length,
    };
  });
}

async function openNamed(page, name) {
  const btn = page.getByRole('button', { name, exact: true }).first();
  if (!(await btn.count())) return false;
  const exp = await btn.getAttribute('aria-expanded');
  if (exp === 'true') return true;
  await btn.click({ timeout: 6000 });
  await page.waitForTimeout(700);
  return true;
}

async function closeNamed(page, name) {
  const btn = page.getByRole('button', { name, exact: true }).first();
  if (!(await btn.count())) return;
  if ((await btn.getAttribute('aria-expanded')) === 'true') {
    await btn.click({ timeout: 4000 }).catch(() => page.keyboard.press('Escape'));
    await page.waitForTimeout(300);
  }
}

const browser = await chromium.launch({ headless: true });

async function contextFor(mobile) {
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  return ctx;
}

const queue = [START];
const seenQueue = new Set([START]);

function enqueue(url) {
  let clean;
  try {
    const u = new URL(url);
    u.hash = '';
    if (u.search && !u.search.includes('term_node')) u.search = '';
    clean = u.toString().replace(/\/$/, '') || u.origin;
    if (u.pathname === '/') clean = u.origin + '/';
  } catch { return; }
  const c = classify(clean);
  if (c.kind !== 'public') return;
  if (/\/(en-ca|fr-ca|fr-fr|en-au|ja-jp|pt-br|nl-nl|de-de|en-gb|es-es|en-in|it-it|es-mx|en-sg|en-hk|en-se|en-za|es-co|fr-ch)\b/.test(clean)) return;
  const key = templateKey(clean);
  const already = pages.some((p) => templateKey(p.url) === key && key.startsWith('tpl:'));
  if (already && key.startsWith('tpl:')) return;
  if (seenQueue.has(clean) || visited.has(clean)) return;
  if (queue.length + visited.size > MAX_PAGES * 3) return;
  seenQueue.add(clean);
  queue.push(clean);
}

async function visit(ctx, url, mobile) {
  const prefix = mobile ? 'm-' : 'd-';
  const requested = mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  const page = await ctx.newPage();
  page.setDefaultNavigationTimeout(45000);
  page.setDefaultTimeout(12000);
  let status = 0;
  let finalUrl = url;
  try {
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    status = resp ? resp.status() : 0;
    await page.waitForTimeout(2200);
    finalUrl = page.url();
  } catch (e) {
    pages.push({ url, finalUrl, status, error: String(e.message).split('\n')[0], mobile, title: '' });
    await page.close().catch(() => {});
    log('NAVFAIL', url, String(e.message).split('\n')[0]);
    return;
  }
  const kind = classify(finalUrl);
  if (kind.kind === 'wall' || /password|sign in|log in|create account/i.test(await page.title().catch(() => ''))) {
    walls.push({ from: url, to: finalUrl.split('?')[0], status, why: 'redirected to a login, signup, account, or checkout wall' });
    recordControl(url, 'navigation', finalUrl.split('?')[0], 'wall', 'branch stopped');
    await page.close().catch(() => {});
    log('WALL', url, '->', finalUrl.split('?')[0]);
    return;
  }
  await hidePromo(page);
  const facts = await pageFacts(page).catch(() => null);
  if (!facts || facts.bodyLen < 40) {
    pages.push({ url, finalUrl, status, error: 'empty or blocked', mobile, title: facts && facts.title || '' });
    await page.close().catch(() => {});
    log('EMPTY', url, facts && facts.title);
    return;
  }
  const blocked = /just a moment|access denied|verify you are human/i.test(facts.title);
  if (blocked) {
    pages.push({ url, finalUrl, status, error: 'bot block', mobile, title: facts.title });
    await page.close().catch(() => {});
    log('BLOCK', url, facts.title);
    return;
  }
  const key = templateKey(finalUrl);
  const shotBase = prefix + slugify(new URL(finalUrl).pathname || 'home');
  const doShot = !shotTemplates.has(prefix + key) && shots < MAX_SHOTS;
  if (doShot) {
    shotTemplates.add(prefix + key);
    await shoot(page, shotBase + '-default', requested);
  }
  const entry = {
    url: finalUrl.split('?')[0],
    requested: url,
    status,
    title: facts.title,
    h1: facts.h1,
    mobile,
    template: key,
    shot: doShot ? shotBase + '-default' : '',
    nav: facts.nav.filter((n) => n.text || n.href).slice(0, 60),
    interactions: facts.interactions.filter((n) => n.text).slice(0, 40),
  };
  pages.push(entry);
  log('page', status, facts.title.slice(0, 70), finalUrl);

  if (!mobile) {
    for (const href of facts.links) enqueue(href);
    for (const n of facts.nav) {
      if (!n.href) continue;
      const c = classify(n.href);
      if (c.kind === 'wall' || c.kind === 'store') {
        walls.push({ from: finalUrl.split('?')[0], control: n.text || n.tag, to: n.href.split('?')[0], why: c.kind });
        recordControl(finalUrl.split('?')[0], n.text || 'nav link', n.href.split('?')[0], c.kind, 'branch stopped, not opened');
      } else if (c.kind === 'sibling' || c.kind === 'external') {
        recordControl(finalUrl.split('?')[0], n.text || 'nav link', n.href.split('?')[0], c.kind, 'not followed from this capture');
      }
    }
  }

  // Homepage interactions: menus, search, mobile drawer. One representative accordion/tab later.
  if ((new URL(finalUrl).pathname === '/' || new URL(finalUrl).pathname === '') && doShot) {
    if (!mobile) {
      for (const name of ['Products', 'Solutions', 'Resources']) {
        try {
          if (await openNamed(page, name)) {
            await hidePromo(page);
            await shoot(page, shotBase + '-menu-' + name.toLowerCase(), requested);
            const openLinks = await page.evaluate(() => [...document.querySelectorAll('a[href]')].filter((a) => {
              const r = a.getBoundingClientRect();
              return r.top > 220 && r.top < 760 && r.width > 20 && (a.innerText || '').trim();
            }).map((a) => ({ t: (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 100), h: a.href })));
            const seen = new Set();
            for (const l of openLinks) {
              const k = l.t + l.h;
              if (seen.has(k)) continue;
              seen.add(k);
              recordControl('https://www.docusign.com/', `${name} menu > ${l.t}`, l.h.split('?')[0], classify(l.h).kind, 'opened from mega-menu');
              enqueue(l.h);
              const c = classify(l.h);
              if (c.kind === 'wall' || c.kind === 'store') walls.push({ from: 'https://www.docusign.com/', control: `${name} menu > ${l.t}`, to: l.h.split('?')[0], why: c.kind });
            }
            await closeNamed(page, name);
          }
        } catch (e) { log('menu fail', name, e.message.split('\n')[0]); }
      }
      try {
        if (await openNamed(page, 'Search')) {
          await page.waitForTimeout(500);
          await shoot(page, shotBase + '-search', requested);
          recordControl('https://www.docusign.com/', 'Search button', 'in-page search panel', 'interaction', 'opened, query not typed');
          await closeNamed(page, 'Search');
        }
      } catch (e) { log('search fail', e.message.split('\n')[0]); }
    } else {
      try {
        const menu = page.locator('button[aria-label*="menu" i], button[aria-label*="Menu" i], header button').filter({ hasText: /menu/i }).first();
        const hamburger = (await menu.count()) ? menu : page.locator('header button').nth(1);
        if (await hamburger.count()) {
          await hamburger.click({ timeout: 5000 });
          await page.waitForTimeout(800);
          await shoot(page, shotBase + '-menu', requested);
          recordControl('https://www.docusign.com/', 'mobile menu button', 'in-page drawer', 'interaction', 'opened at 390');
        }
      } catch (e) { log('mobile menu fail', e.message.split('\n')[0]); }
    }
  }

  // One accordion and one tab on content pages, desktop only, first of each template family.
  if (!mobile && doShot && facts.interactions.some((i) => i.expanded === 'false' && /faq|question|\?/.test(i.text.toLowerCase()) || (i.role === 'tab'))) {
    const acc = facts.interactions.find((i) => i.expanded === 'false' && (i.text.includes('?') || /faq/i.test(i.text)));
    if (acc) {
      try {
        const loc = page.getByRole('button', { name: acc.text.slice(0, 40) }).first();
        if (await loc.count()) {
          await loc.scrollIntoViewIfNeeded();
          await loc.click({ timeout: 5000 });
          await page.waitForTimeout(600);
          await shoot(page, shotBase + '-accordion', requested);
          recordControl(finalUrl.split('?')[0], acc.text, 'in-page accordion', 'interaction', 'opened one item, not submitted');
        }
      } catch { /* optional */ }
    }
  }

  await page.close().catch(() => {});
  fs.writeFileSync(path.join(OUT, 'crawl-partial.json'), JSON.stringify({ pages, controls, walls, shots, queue: queue.slice(0, 40) }, null, 2));
}

const desktop = await contextFor(false);
let n = 0;
while (queue.length && n < MAX_PAGES) {
  const url = queue.shift();
  if (visited.has(url)) continue;
  visited.add(url);
  n++;
  await visit(desktop, url, false);
}
await desktop.close();

// Phone pass: homepage plus a sample of captured public templates.
const phoneUrls = [START];
for (const p of pages) {
  if (!p.url || p.mobile) continue;
  const key = p.template || templateKey(p.url);
  if (phoneUrls.length >= 18) break;
  if (!phoneUrls.some((u) => templateKey(u) === key)) phoneUrls.push(p.url);
}
const mobile = await contextFor(true);
for (const url of phoneUrls) {
  await visit(mobile, url, true);
}
await mobile.close();
await browser.close();

const report = { capturedAt: new Date().toISOString(), start: START, pages, controls, walls, shots, visited: [...visited] };
fs.writeFileSync(path.join(OUT, 'crawl.json'), JSON.stringify(report, null, 2));
log('done pages', pages.length, 'controls', controls.length, 'walls', walls.length, 'shots', shots);
