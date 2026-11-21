// Captures the public Superhuman marketing site (https://superhuman.com) into RAW.
// PRODUCT (adapt): Superhuman public marketing site. Login and signup are photographed empty and not entered.
// ADAPTED_FOR names this product so the kit guard does not treat the file as the Gauth example.
const ADAPTED_FOR = "Superhuman";
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

const RAW = process.env.RAW || path.join(os.homedir(), ".design-systems", "superhuman", "raw-shots");
fs.mkdirSync(RAW, { recursive: true });

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const PAGES = (process.argv[2] || "home,pricing,plans,mail,docs,go,agents,store,enterprise,customers,testimonials,whats-new,contact,notfound,login,signup,menus,signin-menu,mobile").split(",").filter(Boolean);

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

async function hideCookies(page) {
  // Hide only. Never click Accept or Reject: those can POST a consent choice.
  // The banner is not in the open DOM (closed shadow or a late overlay), so
  // also hide any large element pinned to the bottom of the viewport whose
  // box sits over the page. Do not hide the sticky header.
  await page.evaluate(() => {
    const styleId = "capture-hide-consent";
    if (!document.getElementById(styleId)) {
      const style = document.createElement("style");
      style.id = styleId;
      style.textContent = [
        "#transcend-consent-manager, #onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter,",
        "#ot-sdk-btn-floating, .ot-sdk-container,",
        "iframe[src*='onetrust'], iframe[src*='cookie'], iframe[title*='cookie' i],",
        "iframe[title*='privacy' i], iframe[id*='sp_message'], #sp_message_container,",
        "[class*='cookie-banner'], [id*='cookie-banner']",
        "{ display: none !important; visibility: hidden !important; pointer-events: none !important; }",
      ].join(" ");
      document.documentElement.appendChild(style);
    }
    const manager = document.getElementById("transcend-consent-manager");
    if (manager) manager.style.setProperty("display", "none", "important");
    const needles = ["We use cookies", "Accept non-essential cookies", "Reject non-essential cookies"];
    for (const el of document.querySelectorAll("div, section, aside, dialog")) {
      const text = (el.innerText || "").slice(0, 500);
      if (!needles.some((n) => text.includes(n))) continue;
      if (text.length > 2500) continue;
      el.style.setProperty("display", "none", "important");
    }
    const vh = window.innerHeight;
    const vw = window.innerWidth;
    for (const el of document.querySelectorAll("body *")) {
      const s = getComputedStyle(el);
      if (s.position !== "fixed" && s.position !== "sticky") continue;
      const r = el.getBoundingClientRect();
      if (r.width < vw * 0.7) continue;
      if (r.height < 80 || r.height > vh * 0.7) continue;
      if (r.top < 80) continue;
      if (r.bottom < vh - 8) continue;
      el.style.setProperty("display", "none", "important");
    }
  }).catch(() => {});
}

async function settle(page) {
  await page.waitForLoadState("domcontentloaded").catch(() => {});
  await wait(page, 1100);
  await hideCookies(page);
  await wait(page, 250);
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
    const pick = (el) => {
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
    const primary = [...document.querySelectorAll("a, button")].find((el) => /get superhuman|get started|sign up/i.test(el.innerText || "") && el.getBoundingClientRect().width > 40);
    const inputs = [...document.querySelectorAll("input, textarea")].slice(0, 10).map((el) => ({
      type: el.type || el.tagName,
      placeholder: el.getAttribute("placeholder"),
      name: el.getAttribute("name"),
      aria: el.getAttribute("aria-label"),
      valueLen: (el.value || "").length,
    }));
    const buttons = [...document.querySelectorAll("button, a")].slice(0, 50).map((el) => (el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim()).filter(Boolean);
    const nav = [...document.querySelectorAll("nav button, nav a, header a, header button")].map((el) => ({
      t: (el.innerText || "").replace(/\s+/g, " ").trim().slice(0, 60),
      href: el.getAttribute("href"),
    }));
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
        text: h1.innerText.replace(/\s+/g, " ").trim().slice(0, 160),
        font: hs.fontFamily,
        size: hs.fontSize,
        weight: hs.fontWeight,
        color: hs.color,
        lh: hs.lineHeight,
        ls: hs.letterSpacing,
      },
      primary: pick(primary),
      inputs,
      buttons: [...new Set(buttons)].slice(0, 30),
      nav: nav.slice(0, 40),
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
  log("  open", final, status, title.slice(0, 90));
  const body = await page.evaluate(() => (document.body.innerText || "").slice(0, 700));
  const wall = /just a moment|verify you are human|cf-challenge|are you a robot/i.test(body) && body.length < 900;
  return { final, title, status, wall, body: body.slice(0, 280) };
}

const desktopPages = {
  home: "https://superhuman.com/",
  pricing: "https://superhuman.com/plans",
  plans: "https://superhuman.com/plans",
  mail: "https://superhuman.com/mail",
  docs: "https://superhuman.com/docs",
  go: "https://superhuman.com/go",
  agents: "https://superhuman.com/agents",
  store: "https://superhuman.com/store",
  enterprise: "https://superhuman.com/enterprise",
  customers: "https://superhuman.com/customer-stories",
  testimonials: "https://superhuman.com/products/testimonials",
  "whats-new": "https://superhuman.com/products/whats-new",
  contact: "https://www.superhuman.com/contact-sales",
  notfound: "https://superhuman.com/this-page-does-not-exist-capture-2026",
};

const probes = [];

async function shotNamed(page, shooter, name) {
  await page.evaluate(() => scrollTo(0, 0)).catch(() => {});
  await hideCookies(page);
  await wait(page, 250);
  await shooter.view(name);
}

async function openNav(page, label) {
  const btn = page.locator("nav").getByRole("button", { name: label, exact: true }).first();
  await btn.click({ timeout: 4000 });
  await wait(page, 400);
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
    if (key === "home" || key === "pricing" || key === "plans") {
      await measure(page, `${key}-measure.json`);
    }
    continue;
  }
  if (key === "login" || key === "signup") {
    const url = key === "login"
      ? "https://superhuman.com/auth/login"
      : "https://superhuman.com/auth/signup";
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
    await goto(page, "https://superhuman.com/");
    const shooter = new Shooter(page, "menu-light", 1440, 900, 1);
    for (const label of ["Products", "Solutions", "AI", "Resources", "Pricing"]) {
      await openNav(page, label);
      await shotNamed(page, shooter, label.toLowerCase());
      await page.keyboard.press("Escape").catch(() => {});
      await wait(page, 200);
    }
    continue;
  }
  if (key === "signin-menu") {
    log("signin-menu");
    await goto(page, "https://superhuman.com/");
    const shooter = new Shooter(page, "signin-menu-light", 1440, 900, 1);
    const btn = page.locator("header").getByRole("button", { name: /sign in/i }).first();
    await btn.click({ timeout: 4000 });
    await wait(page, 400);
    await shotNamed(page, shooter, "default");
    await page.keyboard.press("Escape").catch(() => {});
    continue;
  }
  if (key === "mobile") {
    log("mobile");
    await page.setViewportSize({ width: 390, height: 844 });
    const shooter = new Shooter(page, "home-light-390", 390, 844, 2);
    shooter.requested.deviceScaleFactor = 2;
    await goto(page, "https://superhuman.com/");
    await shotNamed(page, shooter, "default");
    const toggle = page.getByRole("button", { name: /open navigation menu|open menu|menu/i }).first();
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
log("done", probes.length, "probes");
