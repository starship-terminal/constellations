import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { Mark } from "@/components/shell";

describe("Studio mark", () => {
  it("gives each rendered mark its own clip path id", () => {
    const html = renderToStaticMarkup(
      createElement("div", null, createElement(Mark), createElement(Mark)),
    );
    const ids = [...html.matchAll(/<clipPath id="([^"]+)"/g)].map((m) => m[1]);
    expect(ids).toHaveLength(2);
    expect(new Set(ids).size).toBe(2);
    for (const id of ids) expect(html).toContain(`clip-path="url(#${id})"`);
  });
});
