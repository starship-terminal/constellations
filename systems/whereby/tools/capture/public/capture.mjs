#!/usr/bin/env node
/**
 * Public Whereby refresh. Does not type, submit, click identity providers,
 * join a room, or follow a signed-in app.
 *
 * PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
 *   node systems/whereby/tools/capture/public/capture.mjs
 *
 * Screenshots go to $SHOTS (default /tmp/whereby-capture/shots) so a
 * skip-smudge checkout is not asked to write binaries into the worktree.
 */
import { createRequire } from "node:module";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const pwPath =
  process.env.PLAYWRIGHT ||
  path.join(process.env.HOME, ".design-systems/pw/node_modules/playwright/index.mjs");
const { chromium } = require(pwPath);

const here = path.dirname(fileURLToPath(import.meta.url));
const pkg = path.resolve(here, "../../..");
const outDir = process.env.SHOTS || "/tmp/whereby-capture/shots";
const rawDir = process.env.RAW || path.join(pkg, "raw");
const DESKTOP = { width: 1440, height: 900 };
const PHONE = { width: 390, height: 844 };

function rgbToHex(rgb) {
  const m = String(rgb).match(/rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)/);
  if (!m) return null;
  return (
    "#" +
    [m[1], m[2], m[3]].map((n) => Number(n).toString(16).padStart(2, "0")).join("")
  );
}

async function hideCookie(page) {
  await page
    .evaluate(() => {
      const buttons = [...document.querySelectorAll("button")];
      const accept = buttons.find((b) => /accept all cookies/i.test(b.innerText || ""));
      if (!accept) return;
      let node = accept;
      for (let i = 0; i < 8 && node; i += 1) {
        const text = node.innerText || "";
        if (/cookie/i.test(text) && text.length < 800 && node !== document.body) {
          node.style.setProperty("display", "none", "important");
          return;
        }
        node = node.parentElement;
      }
      accept.style.setProperty("display", "none", "important");
    })
    .catch(() => {});
}

async function shoot(page, name) {
  const file = path.join(outDir, `${name}.png`);
  await page.screenshot({ path: file });
  const box = await page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
    visualViewport: window.visualViewport
      ? {
          width: window.visualViewport.width,
          height: window.visualViewport.height,
          scale: window.visualViewport.scale,
        }
      : null,
  }));
  const url = page.url().split("?")[0].split("#")[0];
  return { name, ...box, url, file };
}

async function goto(page, url) {
  const response = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await page.waitForTimeout(1600);
  await hideCookie(page);
  const title = await page.title();
  const status = response ? response.status() : null;
  return { title, status, url: page.url() };
}

async function readControls(page) {
  return page.evaluate(() => {
    function pick(el) {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || "").replace(/\s+/g, " ").trim().slice(0, 80),
        color: s.color,
        background: s.backgroundColor,
        border: s.border,
        borderColor: s.borderColor,
        radius: s.borderRadius,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        padding: s.padding,
        height: Math.round(r.height),
        width: Math.round(r.width),
        shadow: s.boxShadow,
        letterSpacing: s.letterSpacing,
      };
    }
    const links = [...document.querySelectorAll("a")];
    const byText = (re) => links.find((a) => re.test((a.innerText || "").trim()) && a.getBoundingClientRect().width > 0);
    const h1 = document.querySelector("h1");
    const body = document.body;
    const root = getComputedStyle(document.documentElement);
    const tokens = {};
    for (const sheet of [...document.styleSheets]) {
      let rules;
      try {
        rules = [...sheet.cssRules];
      } catch {
        continue;
      }
      for (const rule of rules) {
        if (!rule.style) continue;
        for (const name of rule.style) {
          if (name.startsWith("--")) tokens[name] = rule.style.getPropertyValue(name).trim();
        }
      }
    }
    const rootVars = {};
    for (let i = 0; i < root.length; i += 1) {
      const name = root[i];
      if (name.startsWith("--")) rootVars[name] = root.getPropertyValue(name).trim();
    }
    return {
      h1: pick(h1),
      body: {
        background: getComputedStyle(body).backgroundColor,
        color: getComputedStyle(body).color,
        fontFamily: getComputedStyle(body).fontFamily,
        fontSize: getComputedStyle(body).fontSize,
      },
      login: pick(byText(/^Log in$/)),
      signup: pick(byText(/^Sign up$/)),
      getStarted: pick(byText(/^Get started$/)),
      explore: pick(byText(/^Explore Meetings$/)),
      varsCount: Object.keys(tokens).length,
      tokenSample: Object.fromEntries(Object.entries(tokens).slice(0, 80)),
      rootVars,
    };
  });
}

async function main() {
  await mkdir(outDir, { recursive: true });
  await mkdir(rawDir, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: DESKTOP,
    deviceScaleFactor: 1,
    locale: "en-US",
  });
  const page = await context.newPage();
  const log = [];
  const readings = {};

  const home = await goto(page, "https://whereby.com/");
  log.push({ ...(await shoot(page, "home-light-default")), title: home.title, status: home.status });
  readings.home = await readControls(page);

  const menuNames = [
    ["products", "home-light-products-menu"],
    ["pricing", "home-light-pricing-menu"],
    ["developers", "home-light-developers-menu"],
    ["resources", "home-light-resources-menu"],
  ];
  for (const [name, file] of menuNames) {
    const box = await page.evaluate((n) => {
      const el = document.querySelector(`[data-framer-name="${n}"]`);
      if (!el) return null;
      const r = el.getBoundingClientRect();
      return { x: r.x + r.width / 2, y: Math.min(r.y + 20, r.y + r.height / 2) };
    }, name);
    if (box) {
      await page.mouse.move(box.x, box.y);
      await page.waitForTimeout(500);
      log.push(await shoot(page, file));
    }
  }
  await page.mouse.move(10, 400);
  await page.waitForTimeout(200);
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(600);
  log.push(await shoot(page, "home-light-footer"));

  const pages = [
    ["pricing-light-default", "https://whereby.com/information/pricing"],
    ["meetings-pricing-light-default", "https://whereby.com/information/meetings/pricing"],
    ["embedded-pricing-light-default", "https://whereby.com/information/embedded/pricing"],
    ["meetings-light-default", "https://whereby.com/information/meetings"],
    ["embedded-light-default", "https://whereby.com/information/embedded"],
    ["features-light-default", "https://whereby.com/information/features"],
    ["about-light-default", "https://whereby.com/information/about-us/"],
    ["security-light-default", "https://whereby.com/information/security/"],
    ["privacy-light-default", "https://whereby.com/information/tos/privacy-policy/"],
    ["select-light-default", "https://whereby.com/information/select-product"],
    ["notfound-light-default", "https://whereby.com/information/this-page-does-not-exist-capture-2026/"],
    ["login-light-default", "https://whereby.com/user/login"],
    ["signup-light-default", "https://whereby.com/user/signup"],
  ];
  for (const [name, url] of pages) {
    const landed = await goto(page, url);
    const shot = await shoot(page, name);
    log.push({ ...shot, title: landed.title, status: landed.status });
    if (name === "meetings-pricing-light-default" || name === "login-light-default" || name === "signup-light-default") {
      readings[name] = await readControls(page);
      readings[name].fields = await page.evaluate(() => {
        return [...document.querySelectorAll("input, button, a")].slice(0, 40).map((el) => ({
          tag: el.tagName,
          type: el.getAttribute("type"),
          text: (el.innerText || el.getAttribute("placeholder") || el.getAttribute("aria-label") || "").trim().slice(0, 80),
          href: el.getAttribute("href"),
        }));
      });
    }
  }

  await page.setViewportSize(PHONE);
  const mobileHome = await goto(page, "https://whereby.com/");
  log.push({ ...(await shoot(page, "mobile-home-light-default")), title: mobileHome.title });
  const opened = await page.evaluate(() => {
    const ham = document.querySelector('[data-framer-name="hamburger-dark"], [data-framer-name*="hamburger"]');
    if (!ham) return false;
    ham.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    return true;
  });
  if (opened) {
    await page.waitForTimeout(500);
    log.push(await shoot(page, "mobile-home-light-menu"));
  }
  await goto(page, "https://whereby.com/information/meetings/pricing");
  log.push(await shoot(page, "mobile-meetings-pricing-light-default"));

  await writeFile(path.join(rawDir, "public-readings.json"), JSON.stringify({ readings, log }, null, 2));
  console.log(JSON.stringify(log.map((s) => ({ name: s.name, url: s.url, w: s.innerWidth, h: s.innerHeight })), null, 2));
  await browser.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
