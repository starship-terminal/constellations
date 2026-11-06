import { expect, test } from "vitest";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { ResearchResults } from "../src/features/research-results";
const props = {
  items: [],
  total: 14,
  query: "calm dashboard",
  platform: "desktop",
  theme: "dark",
  excluded: [],
  pinned: [],
  onInspect: () => {},
  onPin: () => {},
  onExclude: () => {},
};
test("mixed-source research preserves both catalog destinations and filters", () => {
  const html = renderToStaticMarkup(createElement(ResearchResults, props));
  expect(html).toContain(
    'href="/library?q=calm+dashboard&amp;platform=desktop&amp;theme=dark"',
  );
  expect(html).toContain(
    'href="/styles?q=calm+dashboard&amp;platform=desktop&amp;theme=dark"',
  );
  expect(html).toContain("Desktop apps");
});
test("Refero-only candidates link directly to Styles", () => {
  const html = renderToStaticMarkup(
    createElement(ResearchResults, { ...props, source: "refero" }),
  );
  expect(html).toContain('href="/styles?');
  expect(html).not.toContain('href="/library?');
  expect(html).not.toContain("<details");
});
