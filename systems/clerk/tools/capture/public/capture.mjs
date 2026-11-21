#!/usr/bin/env node
/**
 * Public Clerk marketing capture. Does not type, submit, click identity
 * providers, solve captchas, or enter the dashboard.
 *
 * PLAYWRIGHT=$HOME/.design-systems/pw/node_modules/playwright/index.js \
 *   node systems/clerk/tools/capture/public/capture.mjs
 */
import { createRequire } from "node:module";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const pwPath =
  process.env.PLAYWRIGHT ||
  path.join(process.env.HOME, ".design-systems/pw/node_modules/playwright/index.js");
const { chromium } = require(pwPath);

const here = path.dirname(fileURLToPath(import.meta.url));
const pkg = path.resolve(here, "../../..");
const shots = path.join(pkg, "screenshots");
const raw = path.join(pkg, "raw");
const outDir = process.env.SHOTS || "/tmp/clerk-public-shots";

const DESKTOP = { width: 1440, height: 900 };
const PHONE = { width: 390, height: 844 };

function hexFrom(color) {
  if (!color) return null;
  const m = String(color).match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/);
  if (!m) return color;
  const h = (n) => Number(n).toString(16).padStart(2, "0");
  const a = m[4] == null ? 1 : Number(m[4]);
  if (a >= 0.99) return `#${h(m[1])}${h(m[2])}${h(m[3])}`;
  return `rgba(${m[1]}, ${m[2]}, ${m[3]}, ${a})`;
}

async function harvest(page) {
  return page.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const vars = {};
    for (const sheet of document.styleSheets) {
      let rules;
      try {
        rules = sheet.cssRules;
      } catch {
        continue;
      }
      if (!rules) continue;
      for (const rule of rules) {
        if (!rule.style) continue;
        for (const name of rule.style) {
          if (!name.startsWith("--")) continue;
          const value = root.getPropertyValue(name).trim();
          if (value && vars[name] == null) vars[name] = value;
        }
      }
    }
    const pick = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim().slice(0, 80),
        backgroundColor: s.backgroundColor,
        color: s.color,
        borderTopColor: s.borderTopColor,
        borderTopWidth: s.borderTopWidth,
        borderRadius: s.borderRadius,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        height: Math.round(r.height),
        width: Math.round(r.width),
        padding: s.padding,
        boxShadow: s.boxShadow === "none" ? "none" : s.boxShadow.slice(0, 180),
      };
    };
    const byText = (sel, re) =>
      [...document.querySelectorAll(sel)].find((el) =>
        re.test((el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim()),
      );
    const links = [...document.querySelectorAll("a")]
      .map((a) => ({
        t: (a.innerText || a.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim().slice(0, 90),
        h: a.getAttribute("href"),
      }))
      .filter((a) => a.h);
    return {
      url: location.href,
      title: document.title,
      h1: document.querySelector("h1")?.innerText?.replace(/\s+/g, " ").trim().slice(0, 180) || null,
      colorScheme: root.colorScheme,
      viewport: { innerWidth: innerWidth, innerHeight: innerHeight, dpr: devicePixelRatio },
      body: pick(document.body),
      h1Style: pick(document.querySelector("h1")),
      nav: pick(document.querySelector("header, nav")),
      primary: pick(byText("a, button", /^(Sign up|Start building|Get started)$/i)),
      signIn: pick(byText("a, button", /^Sign in$/i)),
      field: pick(document.querySelector("input:not([type=hidden])")),
      link: pick(document.querySelector("main a, article a")),
      vars,
      linkCount: links.length,
      links: links.slice(0, 220),
    };
  });
}

async function shoot(page, name) {
  const file = path.join(outDir, `${name}.png`);
  await page.screenshot({ path: file, fullPage: false });
  const box = await page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
    title: document.title,
    h1: document.querySelector("h1")?.innerText?.replace(/\s+/g, " ").trim().slice(0, 160) || null,
  }));
  return { file, name, url: page.url(), ...box };
}

async function hideOverlays(page) {
  await page
    .addStyleTag({
      content: `
        [class*="cookie" i], [id*="cookie" i], [class*="consent" i], [id*="consent" i],
        iframe[src*="privacy" i], #onetrust-banner-sdk, .osano-cm-window {
          display: none !important;
        }
      `,
    })
    .catch(() => {});
}

async function openNav(page, name) {
  const btn = page.locator("header button, nav button").filter({ hasText: new RegExp(`^${name}$`) }).first();
  if ((await btn.count()) === 0) return { name, missing: true };
  await btn.click();
  await page.waitForTimeout(350);
  const items = await page.evaluate((label) => {
    const btn = [...document.querySelectorAll("header button, nav button")].find(
      (b) => (b.innerText || "").trim() === label && b.getAttribute("aria-controls"),
    );
    if (!btn) return [];
    const panel = document.getElementById(btn.getAttribute("aria-controls"));
    if (!panel) return [];
    return [...panel.querySelectorAll("a")].map((a) => ({
      t: (a.innerText || "").replace(/\s+/g, " ").trim().slice(0, 140),
      h: a.getAttribute("href"),
    }));
  }, name);
  return { name, items };
}

async function main() {
  await mkdir(outDir, { recursive: true });
  await mkdir(shots, { recursive: true });
  await mkdir(raw, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: DESKTOP,
    deviceScaleFactor: 1,
    colorScheme: "light",
    locale: "en-US",
  });
  const page = await context.newPage();
  page.setDefaultTimeout(30000);
  const log = [];
  const readings = {};
  const menus = {};

  async function goto(url) {
    const response = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 40000 });
    await page.waitForTimeout(1400);
    await hideOverlays(page);
    return response ? response.status() : null;
  }

  await goto("https://clerk.com/");
  readings.home = await harvest(page);
  log.push(await shoot(page, "public-home-desktop"));

  for (const name of ["Products", "Docs", "Changelog", "Company", "AI"]) {
    menus[name] = await openNav(page, name);
    log.push(await shoot(page, `public-nav-${name.toLowerCase()}-desktop`));
    await page.keyboard.press("Escape").catch(() => {});
    await page.waitForTimeout(200);
  }

  const pages = [
    ["public-pricing-desktop", "https://clerk.com/pricing"],
    ["public-docs-desktop", "https://clerk.com/docs"],
    ["public-auth-desktop", "https://clerk.com/user-authentication"],
    ["public-company-desktop", "https://clerk.com/company"],
    ["public-changelog-desktop", "https://clerk.com/changelog"],
    ["public-blog-desktop", "https://clerk.com/blog"],
    ["public-security-desktop", "https://clerk.com/security"],
    ["public-contact-desktop", "https://clerk.com/contact"],
  ];
  for (const [name, url] of pages) {
    const status = await goto(url);
    const key = name.replace("public-", "").replace("-desktop", "");
    readings[key] = await harvest(page);
    readings[key].status = status;
    log.push(await shoot(page, name));
  }

  // Empty login and signup walls. Do not type. Do not click providers.
  const loginStatus = await goto("https://dashboard.clerk.com/sign-in");
  await page.waitForTimeout(800);
  readings.login = await harvest(page);
  readings.login.status = loginStatus;
  readings.login.finalUrl = page.url();
  log.push(await shoot(page, "login-wall-desktop"));

  const signupStatus = await goto("https://dashboard.clerk.com/sign-up");
  await page.waitForTimeout(800);
  readings.signup = await harvest(page);
  readings.signup.status = signupStatus;
  readings.signup.finalUrl = page.url();
  log.push(await shoot(page, "signup-wall-desktop"));

  await page.setViewportSize(PHONE);
  await goto("https://clerk.com/");
  readings.homePhone = await harvest(page);
  log.push(await shoot(page, "public-home-mobile"));
  const burger = page.getByRole("button", { name: /open navigation/i }).first();
  if (await burger.count()) {
    await burger.click();
    await page.waitForTimeout(500);
    readings.mobileDrawer = await page.evaluate(() => {
      const drawer = document.getElementById("mobile-navigation");
      const root = drawer || document.body;
      return [...root.querySelectorAll("a, button")]
        .map((el) => ({
          tag: el.tagName,
          t: (el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim().slice(0, 80),
          h: el.getAttribute("href"),
        }))
        .filter((el) => el.t)
        .slice(0, 80);
    });
    log.push(await shoot(page, "public-menu-mobile"));
  }
  await goto("https://clerk.com/pricing");
  readings.pricingPhone = await harvest(page);
  log.push(await shoot(page, "public-pricing-mobile"));

  const slim = {};
  for (const [key, value] of Object.entries(readings)) {
    if (!value || typeof value !== "object") continue;
    const { vars, links, ...rest } = value;
    slim[key] = {
      ...rest,
      varCount: vars ? Object.keys(vars).length : 0,
      vars: vars || {},
      linkSample: (links || []).slice(0, 40),
    };
  }

  await writeFile(
    path.join(raw, "public-2026-11-22.json"),
    JSON.stringify({ date: "2026-11-22", menus, readings: slim, shots: log }, null, 2),
  );
  await writeFile(path.join(outDir, "manifest.json"), JSON.stringify(log, null, 2));
  console.log(JSON.stringify(log.map((s) => ({ name: s.name, url: s.url, title: s.title })), null, 2));
  await browser.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
