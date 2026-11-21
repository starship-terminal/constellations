// Captures the public Clay marketing site (https://www.clay.com) into RAW.
// PRODUCT (adapt): Clay GTM marketing site. Login and signup are photographed empty and not entered.
// ADAPTED_FOR names this product so the kit guard does not treat the file as the Gauth example.
const ADAPTED_FOR = "Clay";
if (!ADAPTED_FOR && !process.env.KIT_EXAMPLE) {
  console.error("public.mjs is not adapted");
  process.exit(2);
}

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";
import { screenshotWithMetadata } from "./screenshot.mjs";
import { scrubConsole } from "./no-query.mjs";

scrubConsole();

const require = createRequire(process.env.PLAYWRIGHT || "/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs");
const { chromium } = require(process.env.PLAYWRIGHT || "/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs");

const RAW = process.env.RAW || path.join(os.homedir(), ".design-systems", "clay-com", "raw-shots");
fs.mkdirSync(RAW, { recursive: true });

const BASE = "https://www.clay.com";
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const PAGES = (process.argv[2] || "home,pricing,integrations,customers,about,faq,blog,changelog,enterprise,contact,legal,notfound,login,signup,menus,mobile").split(",").filter(Boolean);

function cleanUrl(url) {
  try {
    const u = new URL(url);
    u.search = "";
    u.hash = "";
    return u.origin + u.pathname;
  } catch {
    return null;
  }
}

async function dismissCookies(page) {
  const labels = [/accept/i, /agree/i, /got it/i, /allow all/i];
  for (const name of labels) {
    const b = page.getByRole("button", { name }).first();
    if (await b.count().catch(() => 0)) {
      const box = await b.boundingBox().catch(() => null);
      if (box && box.width > 0) {
        await b.click({ timeout: 2000 }).catch(() => {});
        await wait(page, 400);
        return;
      }
    }
  }
}

async function settle(page) {
  await page.waitForLoadState("domcontentloaded").catch(() => {});
  await wait(page, 1200);
  await dismissCookies(page);
  await wait(page, 400);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.p = page;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    const file = path.join(RAW, `${this.prefix}-${name}.png`);
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    log("  shot", `${this.prefix}-${name}`);
  }
  async full(name = "full") {
    const p = this.p;
    const H0 = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const steps = Math.min(12, Math.ceil(H0 / 700));
    for (let i = 0; i < steps; i++) {
      await p.evaluate((y) => scrollTo(0, y), i * 700);
      await wait(p, 180);
    }
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 500);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(8000 / this.dpr);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = path.join(RAW, `${this.prefix}-${name}`);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: `${f}.png`, fullPage: true }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    log("  shot", `${this.prefix}-${name}`, "H=" + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function measure(page, outName) {
  const data = await page.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const names = new Set();
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        for (const r of list) {
          if (r.style) for (const prop of r.style) if (prop.startsWith("--")) names.add(prop);
          if (r.cssRules) walk(r.cssRules);
        }
      };
      if (rules) walk(rules);
    }
    const vars = {};
    for (const n of [...names].sort()) vars[n] = root.getPropertyValue(n).trim();
    const pick = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || "").replace(/\s+/g, " ").trim().slice(0, 80),
        bg: s.backgroundColor, color: s.color, font: s.fontFamily, size: s.fontSize,
        weight: s.fontWeight, radius: s.borderRadius, pad: s.padding, border: s.border,
        lh: s.lineHeight, ls: s.letterSpacing, h: Math.round(r.height), w: Math.round(r.width),
      };
    };
    const h1 = document.querySelector("h1");
    const hs = h1 ? getComputedStyle(h1) : null;
    return {
      href: location.href.split("?")[0].split("#")[0],
      title: document.title,
      innerWidth: window.innerWidth,
      innerHeight: window.innerHeight,
      dpr: window.devicePixelRatio,
      colorScheme: root.colorScheme,
      body: {
        bg: getComputedStyle(document.body).backgroundColor,
        color: getComputedStyle(document.body).color,
        font: getComputedStyle(document.body).fontFamily,
        size: getComputedStyle(document.body).fontSize,
      },
      h1: hs && {
        text: h1.innerText.replace(/\s+/g, " ").trim().slice(0, 120),
        font: hs.fontFamily, size: hs.fontSize, weight: hs.fontWeight,
        color: hs.color, lh: hs.lineHeight, ls: hs.letterSpacing,
      },
      varCount: Object.keys(vars).length,
      vars,
    };
  });
  const file = path.join(RAW, outName);
  fs.writeFileSync(file, JSON.stringify(data, null, 2));
  log("  measured", outName, "vars", data.varCount);
  return data;
}

async function goto(page, url) {
  const res = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await settle(page);
  const final = cleanUrl(page.url());
  const title = await page.title();
  const status = res ? res.status() : null;
  log("  open", final, status, title.slice(0, 80));
  const body = await page.evaluate(() => (document.body.innerText || "").slice(0, 400));
  const wall = /just a moment|verify you are human|cf-challenge|captcha/i.test(body) && body.length < 800;
  return { final, title, status, wall, body: body.slice(0, 180) };
}

async function shotPage(page, shooter, slug) {
  await shooter.view("default");
  await shooter.full("full");
}

const desktopPages = {
  home: "/",
  pricing: "/pricing",
  integrations: "/integrations",
  customers: "/customers",
  about: "/about",
  faq: "/faq",
  blog: "/blog",
  changelog: "/changelog",
  enterprise: "/enterprise",
  contact: "/contact",
  legal: "/legal/terms-of-service",
  notfound: "/this-page-does-not-exist-capture-2026",
};

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    colorScheme: "light",
    locale: "en-US",
  });
  const page = await context.newPage();
  const S = new Shooter(page, "desktop", 1440, 900, 1);

  if (PAGES.includes("home") || PAGES.includes("measure")) {
    const info = await goto(page, BASE + "/");
    if (info.wall) {
      log("HOME IS A WALL", info.body);
      await browser.close();
      process.exit(3);
    }
    await measure(page, "home-vars.json");
    if (PAGES.includes("home")) {
      const home = new Shooter(page, "home-light", 1440, 900, 1);
      await home.view("default");
      await home.full("full");
    }
  }

  for (const [name, pathName] of Object.entries(desktopPages)) {
    if (name === "home") continue;
    if (!PAGES.includes(name)) continue;
    const info = await goto(page, BASE + pathName);
    if (info.wall) { log("  skip wall", name); continue; }
    const shooter = new Shooter(page, `${name}-light`, 1440, 900, 1);
    await shotPage(page, shooter, name);
    if (name === "pricing") await measure(page, "pricing-vars.json");
  }

  if (PAGES.includes("menus")) {
    await goto(page, BASE + "/");
    const menus = new Shooter(page, "home-light", 1440, 900, 1);
    for (const label of ["Product", "Solutions", "Resources", "Company"]) {
      const link = page.locator("nav").getByRole("link", { name: label, exact: true }).first();
      await link.hover().catch(() => {});
      await wait(page, 700);
      await menus.view(label.toLowerCase() + "-menu");
      await page.mouse.move(700, 800);
      await wait(page, 300);
    }
    const search = page.getByRole("button", { name: /K/ }).first();
    if (await search.count()) {
      await search.click().catch(() => {});
      await wait(page, 800);
      await menus.view("search-dialog");
      await page.keyboard.press("Escape").catch(() => {});
      await wait(page, 300);
    }
  }

  if (PAGES.includes("login")) {
    const info = await goto(page, "https://app.clay.com/");
    const inputs = await page.evaluate(() => [...document.querySelectorAll("input, textarea")].map((el) => ({
      type: el.type, name: el.name, placeholder: el.placeholder, valueLen: (el.value || "").length,
    })));
    fs.writeFileSync(path.join(RAW, "login-probe.json"), JSON.stringify({
      url: cleanUrl(page.url()), title: await page.title(), status: info.status, wall: info.wall, inputs, body: info.body,
    }, null, 2));
    if (!info.wall) {
      const shooter = new Shooter(page, "login-light", 1440, 900, 1);
      await shooter.view("default");
    } else log("  login wall challenge, shot discarded");
  }

  if (PAGES.includes("signup")) {
    const info = await goto(page, "https://app.clay.com/signup");
    const inputs = await page.evaluate(() => [...document.querySelectorAll("input, textarea")].map((el) => ({
      type: el.type, name: el.name, placeholder: el.placeholder, valueLen: (el.value || "").length,
    })));
    fs.writeFileSync(path.join(RAW, "signup-probe.json"), JSON.stringify({
      url: cleanUrl(page.url()), title: await page.title(), status: info.status, wall: info.wall, inputs, body: info.body,
    }, null, 2));
    if (!info.wall) {
      const shooter = new Shooter(page, "signup-light", 1440, 900, 1);
      await shooter.view("default");
    } else log("  signup wall challenge, shot discarded");
  }

  await context.close();

  if (PAGES.includes("mobile")) {
    const mctx = await browser.newContext({
      viewport: { width: 390, height: 844 },
      deviceScaleFactor: 2,
      isMobile: true,
      hasTouch: true,
      colorScheme: "light",
      locale: "en-US",
    });
    const mp = await mctx.newPage();
    await goto(mp, BASE + "/");
    const home = new Shooter(mp, "mobile-home-light", 390, 844, 2);
    await home.view("default");
    const menuBtn = mp.locator("button, a").filter({ hasText: /^menu$/i }).first();
    const burger = mp.locator("nav button, header button").first();
    if (await menuBtn.count()) await menuBtn.click().catch(() => {});
    else if (await burger.count()) await burger.click().catch(() => {});
    await wait(mp, 700);
    await home.view("menu");
    await goto(mp, BASE + "/pricing");
    const pricing = new Shooter(mp, "mobile-pricing-light", 390, 844, 2);
    await pricing.view("default");
    await mctx.close();
  }

  await browser.close();
  log("done");
}

main().catch((err) => {
  console.error(String(err && err.stack || err).split("\n").slice(0, 8).join("\n"));
  process.exit(1);
});
