import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { Mark } from "@/components/shell";

describe("Constellations mark", () => {
  it("uses the brand mark", () => {
    const html = renderToStaticMarkup(createElement(Mark));
    expect(html).toContain('src="/brand/flat/favicon.svg"');
    expect(html).toContain('class="brand-mark-glass"');
    expect(html).toContain('src="/brand/glass/icon-192.png"');
    expect(html).not.toContain("ds-mark-clip");
  });
});
