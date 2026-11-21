#!/usr/bin/env node
/**
 * Public Walmart refresh. Does not type, submit, click identity providers,
 * enter checkout, solve a captcha, or follow a signed-in account.
 *
 * PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
 *   node systems/walmart/tools/capture/public/capture.mjs
 *
 * Screenshots land in $SHOTS (default /tmp/walmart-capture/shots).
 * Readings land in $RAW (default /tmp/walmart-capture/raw).
 */
import { createRequire } from "node:module";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const pwPath = process.env.PLAYWRIGHT || path.join(process.env.HOME, ".design-systems/pw/node_modules/playwright/index.mjs");
const { chromium } = require(pwPath);

const outDir = process.env.SHOTS || "/tmp/walmart-capture/shots";
const rawDir = process.env.RAW || "/tmp/walmart-capture/raw";
const DESKTOP = { width: 1440, height: 900 };
const PHONE = { width: 390, height: 844 };

function stripUrl(url) {
  try {
    const u = new URL(url);
    u.search = "";
    u.hash = "";
    return u.toString();
  } catch {
    return String(url || "").split("?")[0].split("#")[0];
  }
}

async function shoot(page, name) {
  const file = path.join(outDir, `${name}.png`);
  await page.screenshot({ path: file, animations: "disabled" });
  const box = await page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
    title: document.title,
  }));
  return { name, ...box, url: stripUrl(page.url()) };
}

async function goto(page, url) {
  const res = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 }).catch((err) => ({ error: String(err) }));
  await page.waitForTimeout(1600);
  const title = await page.title().catch(() => "");
  const finalUrl = stripUrl(page.url());
  const blocked = /robot or human|verify you are human|access denied|captcha/i.test(title);
  return { requested: stripUrl(url), finalUrl, title, blocked, status: res && res.status ? res.status() : null };
}

async function closeCaptcha(page) {
  const close = page.getByRole("button", { name: /close dialog/i }).first();
  if (await close.count()) {
    await close.click({ timeout: 1500 }).catch(() => {});
    await page.waitForTimeout(300);
  }
}

async function readHome(page) {
  return page.evaluate(() => {
    const cs = getComputedStyle(document.documentElement);
    const pick = [
      "--color-core-blue-100", "--color-core-blue-130", "--color-core-blue-160",
      "--color-core-blue-5", "--color-core-blue-10", "--color-core-blue-20",
      "--color-core-spark-100", "--color-core-spark-5",
      "--color-core-black", "--color-core-white", "--color-core-gray-100",
      "--color-core-gray-130", "--color-core-gray-50",
      "--ld-semantic-color-top-nav-fill", "--ld-semantic-color-text",
      "--ld-semantic-color-text-subtle", "--ld-semantic-color-background",
      "--ld-semantic-color-separator", "--ld-semantic-color-border",
      "--ld-semantic-color-fill-brand-bold", "--ld-semantic-color-fill-positive",
      "--ld-semantic-color-fill-negative", "--ld-semantic-color-fill-warning",
      "--ld-semantic-color-fill-accent-spark",
      "--ld-semantic-color-action-fill-primary",
      "--ld-semantic-color-action-fill-primary-hovered",
      "--ld-semantic-color-action-fill-primary-pressed",
      "--ld-semantic-color-action-fill-primary-disabled",
      "--font-family-default", "--font-weight-400", "--font-weight-700",
      "--border-radius-50", "--border-radius-100", "--border-radius-200",
      "--border-radius-round", "--elevation-100", "--elevation-200",
      "--duration-100", "--duration-200", "--motion-duration-short",
    ];
    const vars = {};
    for (const name of pick) vars[name] = cs.getPropertyValue(name).trim();
    const varNames = [];
    for (let i = 0; i < cs.length; i++) {
      const n = cs[i];
      if (n.startsWith("--")) varNames.push(n);
    }
    const motion = varNames.filter((n) => /duration|easing|motion/i.test(n)).slice(0, 40);
    const motionVals = {};
    for (const n of motion) motionVals[n] = cs.getPropertyValue(n).trim();

    function boxOf(el) {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim().slice(0, 80),
        w: Math.round(r.width),
        h: Math.round(r.height),
        bg: s.backgroundColor,
        color: s.color,
        font: s.fontFamily,
        size: s.fontSize,
        weight: s.fontWeight,
        lh: s.lineHeight,
        radius: s.borderRadius,
        border: `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`,
        pad: s.padding,
        shadow: s.boxShadow,
      };
    }
    const search = document.querySelector('input[type="search"], [role="combobox"][aria-label="Search"], input[aria-label="Search"]');
    const dept = [...document.querySelectorAll("button")].find((b) => /^Departments/.test((b.innerText || "").trim()));
    const sign = [...document.querySelectorAll("button")].find((b) => /Sign In/.test(b.innerText || "") && /Account/.test(b.innerText || ""));
    const cart = [...document.querySelectorAll("button")].find((b) => /Cart contains/.test(b.getAttribute("aria-label") || ""));
    const searchBtn = document.querySelector('button[aria-label="Search"]');
    const chip = [...document.querySelectorAll("a")].find((a) => /Pharmacy/.test(a.innerText || "") && a.getBoundingClientRect().top < 160);
    const header = document.querySelector("header, banner, [role=banner]") || document.querySelector("header");
    const banner = document.querySelector('[role="banner"]') || document.querySelector("header");
    return {
      title: document.title,
      colorScheme: cs.colorScheme,
      rootFont: cs.fontSize,
      varCount: varNames.length,
      vars,
      motionVals,
      themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
      controls: {
        search: boxOf(search),
        departments: boxOf(dept),
        signIn: boxOf(sign),
        cart: boxOf(cart),
        searchButton: boxOf(searchBtn),
        pharmacyChip: boxOf(chip),
        banner: boxOf(banner),
      },
    };
  });
}

async function mapNav(page) {
  return page.evaluate(() => {
    const secondary = [...document.querySelectorAll('nav a, [role="navigation"] a')].filter((a) => {
      const r = a.getBoundingClientRect();
      return r.top > 70 && r.top < 150 && r.height > 16;
    }).map((a) => ({
      t: (a.innerText || "").replace(/\s+/g, " ").trim().slice(0, 40),
      href: (a.getAttribute("href") || "").split("?")[0],
    }));
    const footer = document.querySelector("footer");
    const footerLinks = footer
      ? [...footer.querySelectorAll("a")].map((a) => ({
          t: (a.innerText || "").replace(/\s+/g, " ").trim().slice(0, 60),
          href: (a.getAttribute("href") || "").split("?")[0],
        })).filter((x) => x.t)
      : [];
    const headings = [...document.querySelectorAll("h1, h2")].slice(0, 8).map((h) => ({
      tag: h.tagName,
      t: (h.innerText || "").replace(/\s+/g, " ").trim().slice(0, 80),
      size: getComputedStyle(h).fontSize,
      weight: getComputedStyle(h).fontWeight,
      color: getComputedStyle(h).color,
      family: getComputedStyle(h).fontFamily,
    }));
    return { secondary, footerLinks: footerLinks.slice(0, 40), headings };
  });
}

async function openMenu(page, label) {
  const btn = page.getByRole("button", { name: new RegExp(`^${label}`) }).first();
  await btn.click({ timeout: 4000 });
  await page.waitForTimeout(500);
  return page.evaluate((label) => {
    const root = [...document.querySelectorAll('[aria-expanded="true"]')].find((el) => (el.innerText || "").includes(label));
    const panel = root ? root.parentElement : null;
    const items = panel
      ? [...panel.querySelectorAll("a, button")].map((el) => ({
          tag: el.tagName,
          t: (el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim().slice(0, 60),
          href: el.getAttribute("href"),
        })).filter((x) => x.t && x.t.length < 50)
      : [];
    return items.slice(0, 30);
  }, label);
}

async function main() {
  await mkdir(outDir, { recursive: true });
  await mkdir(rawDir, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: DESKTOP,
    deviceScaleFactor: 1,
    locale: "en-US",
    timezoneId: "America/Los_Angeles",
  });
  const page = await context.newPage();
  const log = [];
  const notes = { blocked: [], pages: [] };

  const homeNav = await goto(page, "https://www.walmart.com/");
  notes.pages.push(homeNav);
  await closeCaptcha(page);
  if (/robot or human/i.test(await page.title())) {
    notes.homeBlocked = true;
    log.push({ name: "home-blocked", url: stripUrl(page.url()), title: await page.title() });
    await writeFile(path.join(rawDir, "notes.json"), JSON.stringify({ notes, log }, null, 2));
    console.log("HOME_BLOCKED");
    await browser.close();
    process.exit(2);
  }
  log.push(await shoot(page, "home-light-default"));
  const homeRead = await readHome(page);
  await writeFile(path.join(rawDir, "home.json"), JSON.stringify(homeRead, null, 2));

  try {
    const dept = await openMenu(page, "Departments");
    notes.departments = dept;
    log.push(await shoot(page, "home-light-departments-menu"));
    const grocery = page.getByRole("button", { name: /^Grocery$/ }).first();
    if (await grocery.count()) {
      await grocery.click();
      await page.waitForTimeout(400);
      notes.grocery = await page.evaluate(() => {
        const links = [...document.querySelectorAll("a")].filter((a) => {
          const r = a.getBoundingClientRect();
          return r.left > 240 && r.left < 900 && r.top > 100 && r.top < 800 && r.width > 40;
        }).map((a) => ({
          t: (a.innerText || "").replace(/\s+/g, " ").trim().slice(0, 50),
          href: (a.getAttribute("href") || "").split("?")[0],
        }));
        return links.slice(0, 24);
      });
      log.push(await shoot(page, "home-light-departments-grocery"));
    }
    await page.keyboard.press("Escape");
    await page.waitForTimeout(250);
  } catch (err) {
    notes.departmentsError = String(err);
  }

  try {
    notes.services = await openMenu(page, "Services");
    log.push(await shoot(page, "home-light-services-menu"));
    await page.keyboard.press("Escape");
    await page.waitForTimeout(200);
  } catch (err) {
    notes.servicesError = String(err);
  }

  try {
    const sign = page.getByRole("button", { name: /Sign In/ }).first();
    await sign.click({ timeout: 4000 });
    await page.waitForTimeout(500);
    notes.accountMenu = await page.evaluate(() => {
      const links = [...document.querySelectorAll("a")].filter((a) => {
        const r = a.getBoundingClientRect();
        return r.top > 60 && r.top < 420 && r.left > 900 && r.width > 40;
      }).map((a) => ({
        t: (a.innerText || "").replace(/\s+/g, " ").trim().slice(0, 60),
        href: (a.getAttribute("href") || "").split("?")[0],
      }));
      return links.slice(0, 16);
    });
    log.push(await shoot(page, "home-light-account-menu"));
    await page.keyboard.press("Escape");
  } catch (err) {
    notes.accountError = String(err);
  }

  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(800);
  log.push(await shoot(page, "home-light-footer"));
  notes.nav = await mapNav(page);

  const inner = [
    ["category-light-default", "https://www.walmart.com/cp/toys/4171"],
    ["search-light-default", "https://www.walmart.com/search?q=notebook"],
    ["search-empty-light-default", "https://www.walmart.com/search?q=zzzzwalmartcaptureempty2026"],
    ["notfound-light-default", "https://www.walmart.com/this-page-does-not-exist-capture-2026"],
    ["help-light-default", "https://www.walmart.com/help"],
    ["services-light-default", "https://www.walmart.com/services"],
    ["departments-light-default", "https://www.walmart.com/all-departments"],
    ["plus-light-default", "https://www.walmart.com/plus"],
    ["privacy-light-default", "https://corporate.walmart.com/privacy-security/walmart-privacy-notice"],
  ];
  let productUrl = null;
  for (const [name, url] of inner) {
    const nav = await goto(page, url);
    notes.pages.push(nav);
    if (nav.blocked || /robot or human/i.test(await page.title())) {
      notes.blocked.push(nav);
      await closeCaptcha(page);
      continue;
    }
    log.push(await shoot(page, name));
    if (name === "search-light-default" && !productUrl) {
      productUrl = await page.evaluate(() => {
        const a = [...document.querySelectorAll('a[href*="/ip/"]')].find((el) => {
          const r = el.getBoundingClientRect();
          return r.width > 40 && r.top > 80;
        });
        return a ? a.href.split("?")[0] : null;
      });
      notes.productUrl = productUrl;
    }
  }

  if (productUrl) {
    const nav = await goto(page, productUrl);
    notes.pages.push({ ...nav, kind: "product" });
    if (!nav.blocked && !/robot or human/i.test(await page.title())) {
      log.push(await shoot(page, "product-light-default"));
      notes.product = await page.evaluate(() => {
        const h1 = document.querySelector("h1");
        const price = document.querySelector('[itemprop="price"], [data-testid="price-wrap"], [data-automation-id="product-price"]');
        const add = [...document.querySelectorAll("button")].find((b) => /add to cart/i.test(b.innerText || ""));
        function box(el) {
          if (!el) return null;
          const s = getComputedStyle(el);
          const r = el.getBoundingClientRect();
          return {
            text: (el.innerText || "").replace(/\s+/g, " ").trim().slice(0, 80),
            w: Math.round(r.width),
            h: Math.round(r.height),
            bg: s.backgroundColor,
            color: s.color,
            size: s.fontSize,
            weight: s.fontWeight,
            radius: s.borderRadius,
            family: s.fontFamily,
          };
        }
        return { title: document.title, h1: box(h1), price: box(price), add: box(add) };
      });
    } else {
      notes.blocked.push(nav);
    }
  }

  const loginUrls = [
    "https://identity.walmart.com/account/login",
    "https://www.walmart.com/account/signup",
    "https://identity.walmart.com/account/signup",
  ];
  for (const url of loginUrls) {
    const nav = await goto(page, url);
    notes.pages.push({ ...nav, kind: "auth" });
    const title = await page.title();
    if (/robot or human|verify you are human/i.test(title) || nav.blocked) {
      notes.blocked.push({ ...nav, title });
      continue;
    }
    const fields = await page.evaluate(() => {
      const inputs = [...document.querySelectorAll("input")].map((el) => ({
        type: el.type,
        name: el.name,
        placeholder: el.placeholder,
        label: el.getAttribute("aria-label"),
        valueLen: (el.value || "").length,
      }));
      const buttons = [...document.querySelectorAll("button, a")].filter((el) => {
        const r = el.getBoundingClientRect();
        return r.width > 40 && r.top > 40 && r.top < 800;
      }).map((el) => (el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim().slice(0, 50)).filter(Boolean);
      return { inputs, buttons: [...new Set(buttons)].slice(0, 20), title: document.title };
    });
    notes.auth = notes.auth || [];
    notes.auth.push({ url: stripUrl(page.url()), title, fields });
    const shot = /signup/i.test(url) ? "signup-light-default" : "login-light-default";
    if (!log.some((s) => s.name === shot)) log.push(await shoot(page, shot));
  }

  await page.setViewportSize(PHONE);
  const phoneHome = await goto(page, "https://www.walmart.com/");
  notes.pages.push({ ...phoneHome, width: 390 });
  await closeCaptcha(page);
  if (!/robot or human/i.test(await page.title())) {
    log.push(await shoot(page, "mobile-home-light-default"));
    const menu = page.getByRole("button", { name: /^Menu$/ }).first();
    if (await menu.count()) {
      await menu.click().catch(() => {});
      await page.waitForTimeout(500);
      notes.mobileMenu = await page.evaluate(() => {
        return [...document.querySelectorAll("a, button")].filter((el) => {
          const r = el.getBoundingClientRect();
          return r.width > 40 && r.top > 40 && r.top < 800 && r.left < 390;
        }).map((el) => (el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim().slice(0, 40)).filter(Boolean).slice(0, 24);
      });
      log.push(await shoot(page, "mobile-home-light-menu"));
    }
  } else {
    notes.blocked.push(phoneHome);
  }
  const phoneInner = await goto(page, "https://www.walmart.com/cp/toys/4171");
  notes.pages.push({ ...phoneInner, width: 390 });
  if (!phoneInner.blocked && !/robot or human/i.test(await page.title())) {
    log.push(await shoot(page, "mobile-category-light-default"));
  } else {
    notes.blocked.push(phoneInner);
  }

  await writeFile(path.join(rawDir, "notes.json"), JSON.stringify(notes, null, 2));
  await writeFile(path.join(rawDir, "shots.json"), JSON.stringify(log, null, 2));
  console.log(JSON.stringify(log.map((s) => s.name), null, 2));
  await browser.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
