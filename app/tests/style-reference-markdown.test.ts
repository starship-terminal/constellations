import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import type { LibraryDetail } from "@/contracts/library";
import { StyleOverview } from "@/features/style-reference";

describe("Refero design notes", () => {
  it("shows a note's images as text instead of loading a remote host", () => {
    const detail = {
      id: "refero:sample",
      source: "refero",
      slug: "sample",
      name: "Sample",
      themes: [],
      media: [],
      colors: [],
      typography: [],
      spacing: [],
      radii: [],
      guidelines: [],
      related: [],
      tags: [],
      interpreted: {
        designSystem: {
          customSections: [
            {
              title: "Agent Prompt Guide",
              content:
                "Use these values.\n\n![Hero](https://tracker.test/pixel.png)",
            },
          ],
        },
      },
    } as unknown as LibraryDetail;
    const html = renderToStaticMarkup(createElement(StyleOverview, { detail }));
    expect(html).toContain("Use these values.");
    expect(html).toContain("[Image: Hero]");
    expect(html).not.toContain("tracker.test");
  });
});
