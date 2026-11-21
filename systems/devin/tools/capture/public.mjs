// Captures the public Devin marketing site (https://devin.ai) into RAW.
// PRODUCT (adapt): Devin public marketing site. Login and signup are photographed empty and not entered.
// ADAPTED_FOR names this product so the kit guard does not treat the file as the Gauth example.
const ADAPTED_FOR = "Devin";
if (!ADAPTED_FOR && !process.env.KIT_EXAMPLE) {
  console.error("public.mjs is not adapted");
  process.exit(2);
}

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { createRequire } from "node:module";
import { screenshotWithMetadata } from "./screenshot.mjs";
import { scrubConsole } from "./no-query.mjs";

scrubConsole();

const PW = process.env.PLAYWRIGHT || "/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs";
const require = createRequire(PW);
const { chromium } = require(PW);

const RAW = process.env.RAW || path.join(os.homedir(), ".design-systems", "devin", "raw-shots");
fs.mkdirSync(RAW, { recursive: true });

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const PAGES = (process.argv[2] || "home,pricing,customers,blog,bots,security,enterprise,demo,brand,support,changelog,university,community,contact,privacy-choices,notfound,login,signup,menus,mobile").split(",").filter(Boolean);

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
  const labels = [/accept all/i, /^accept$/i, /agree/i, /got it/i, /allow all/i];
  for (const name of labels) {
    const b = page.getByRole("button", { name }).first();
    if (await b.count().catch(() => 0)) {
      const box = await b.boundingBox().catch(() => null);
      if (box && box.width > 0 && box.y < 900) {
        await b.click({ timeout: 1500 }).catch(() => {});
        await wait(page, 300);
        return;
      }
    }
  }
}

async function settle(page) {
  await page.waitForLoadState("domcontentloaded").catch(() => {});
  await wait(page, 900);
  await dismissCookies(page);
  await wait(page, 300);
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
}

async function measure(page, outName) {
  const data = await page.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const names = new Set();
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        if (!list) return;
        for (const r of list) {
          try {
            if (r.style) {
              for (let i = 0; i < r.style.length; i++) {
                const prop = r.style[i];
                if (prop && prop.startsWith("--")) names.add(prop);
              }
            }
            if (r.cssRules) walk(r.cssRules);
          } catch { /* cross-origin or unreadable rule */ }
        }
      };
      if (rules) walk(rules);
    }
    const vars = {};
    for (const n of [...names].sort()) {
      const v = root.getPropertyValue(n).trim();
      if (v && !/[?][^=]*[=]|token=|sig=/i.test(v)) vars[n] = v.slice(0, 240);
    }
    const pick = (sel) => {
      const el = typeof sel === "string" ? document.querySelector(sel) : sel;
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || "").replace(/\s+/g, " ").trim().slice(0, 90),
        bg: s.backgroundColor,
        color: s.color,
        font: s.fontFamily,
        size: s.fontSize,
        weight: s.fontWeight,
        radius: s.borderRadius,
        pad: s.padding,
        border: s.borderTopWidth + " " + s.borderTopStyle + " " + s.borderTopColor,
        lh: s.lineHeight,
        ls: s.letterSpacing,
        h: Math.round(r.height),
        w: Math.round(r.width),
      };
    };
    const h1 = document.querySelector("h1");
    const hs = h1 ? getComputedStyle(h1) : null;
    const primary = [...document.querySelectorAll("a, button")].find((el) => /get started/i.test(el.innerText || "") && el.getBoundingClientRect().width > 40);
    const login = [...document.querySelectorAll("a")].find((el) => /^log in$/i.test((el.innerText || "").trim()));
    const inputs = [...document.querySelectorAll("input, textarea")].slice(0, 8).map((el) => ({
      type: el.type || el.tagName,
      placeholder: el.getAttribute("placeholder"),
      name: el.getAttribute("name"),
      aria: el.getAttribute("aria-label"),
      valueLen: (el.value || "").length,
    }));
    const buttons = [...document.querySelectorAll("button, a")].slice(0, 40).map((el) => (el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim()).filter(Boolean);
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
        text: h1.innerText.replace(/\s+/g, " ").trim().slice(0, 140),
        font: hs.fontFamily,
        size: hs.fontSize,
        weight: hs.fontWeight,
        color: hs.color,
        lh: hs.lineHeight,
        ls: hs.letterSpacing,
      },
      primary: pick(primary),
      login: pick(login),
      inputs,
      buttons: [...new Set(buttons)].slice(0, 24),
      varCount: Object.keys(vars).length,
      vars,
    };
  });
  const file = path.join(RAW, outName);
  fs.writeFileSync(file, JSON.stringify(data, null, 2));
  log("  measured", outName, "vars", data.varCount, "title", (data.title || "").slice(0, 70));
  return data;
}

async function goto(page, url) {
  const res = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await settle(page);
  const final = cleanUrl(page.url());
  const title = await page.title();
  const status = res ? res.status() : null;
  log("  open", final, status, title.slice(0, 80));
  const body = await page.evaluate(() => (document.body.innerText || "").slice(0, 500));
  const wall = /just a moment|verify you are human|cf-challenge|captcha|are you a robot/i.test(body) && body.length < 900;
  return { final, title, status, wall, body: body.slice(0, 220) };
}

const desktopPages = {
  home: "https://devin.ai/",
  pricing: "https://devin.ai/pricing",
  customers: "https://devin.ai/customers",
  blog: "https://devin.ai/blog",
  bots: "https://devin.ai/bots",
  security: "https://devin.ai/security",
  enterprise: "https://devin.ai/enterprise",
  demo: "https://devin.ai/demo",
  brand: "https://devin.ai/brand",
  support: "https://devin.ai/support",
  changelog: "https://devin.ai/changelog",
  university: "https://devin.ai/university",
  community: "https://devin.ai/community",
  contact: "https://devin.ai/contact",
  "privacy-choices": "https://devin.ai/privacy-choices",
  notfound: "https://devin.ai/this-page-does-not-exist-capture-2026",
};

const probes = [];

async function shotNamed(page, shooter, name) {
  await page.evaluate(() => scrollTo(0, 0));
  await wait(page, 250);
  await shooter.view(name);
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  colorScheme: "light",
});
const page = await context.newPage();

for (const key of PAGES) {
  if (desktopPages[key]) {
    log("page", key);
    const info = await goto(page, desktopPages[key]);
    probes.push({ key, ...info });
    if (info.wall) {
      log("  WALL, skipping shots");
      continue;
    }
    const shooter = new Shooter(page, `${key}-light`, 1440, 900, 1);
    await shotNamed(page, shooter, "default");
    if (key === "home" || key === "pricing") {
      await measure(page, `${key}-measure.json`);
    }
    continue;
  }
  if (key === "login" || key === "signup") {
    const url = key === "login" ? "https://app.devin.ai/login" : "https://app.devin.ai/auth/signup";
    log("wall", key);
    const info = await goto(page, url);
    probes.push({ key, ...info });
    await page.evaluate(() => {
      for (const el of document.querySelectorAll("input, textarea")) el.value = "";
    }).catch(() => {});
    const shooter = new Shooter(page, `${key}-light`, 1440, 900, 1);
    await shotNamed(page, shooter, "default");
    await measure(page, `${key}-measure.json`);
    continue;
  }
  if (key === "menus") {
    log("menus");
    await goto(page, "https://devin.ai/");
    const shooter = new Shooter(page, "menu-light", 1440, 900, 1);
    for (const label of ["Product", "Solutions", "Resources"]) {
      const btn = page.getByRole("button", { name: label, exact: true }).first();
      await btn.hover().catch(() => {});
      await wait(page, 500);
      await shotNamed(page, shooter, label.toLowerCase());
      await page.mouse.move(700, 700);
      await wait(page, 200);
    }
    continue;
  }
  if (key === "mobile") {
    log("mobile");
    await page.setViewportSize({ width: 390, height: 844 });
    const shooter = new Shooter(page, "home-light-390", 390, 844, 2);
    shooter.requested.deviceScaleFactor = 2;
    await goto(page, "https://devin.ai/");
    await shotNamed(page, shooter, "default");
    const toggle = page.getByRole("button", { name: /toggle menu|open menu|menu/i }).first();
    if (await toggle.count()) {
      await toggle.click().catch(() => {});
      await wait(page, 500);
      await shotNamed(page, shooter, "drawer");
    }
    await page.setViewportSize({ width: 1440, height: 900 });
  }
}

fs.writeFileSync(path.join(RAW, "probes.json"), JSON.stringify(probes, null, 2));
await browser.close();
log("done", probes.length);
