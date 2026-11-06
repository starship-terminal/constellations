import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { PackageMarkdown } from "../src/features/package-detail";

describe("package Markdown heading anchors", () => {
  it("gives every Markdown heading level a target, including the ResearchRabbit main-card link", () => {
    const html = renderToStaticMarkup(
      createElement(PackageMarkdown, {
        slug: "researchrabbit",
        path: "components.md",
        text: [
          "[Main card](#main-card)",
          "# Components",
          "## Anatomy",
          "### Workspace",
          "#### Main card",
          "##### Header strip",
          "###### Graph canvas",
        ].join("\n\n"),
      }),
    );
    expect(html).toContain('href="#main-card"');
    for (const [level, id] of [
      [1, "components"],
      [2, "anatomy"],
      [3, "workspace"],
      [4, "main-card"],
      [5, "header-strip"],
      [6, "graph-canvas"],
    ])
      expect(html).toContain(`<h${level} id="${id}">`);
  });
  it("builds anchors from the heading text when a heading holds inline markup", () => {
    const html = renderToStaticMarkup(
      createElement(PackageMarkdown, {
        slug: "demo",
        path: "components.md",
        text: [
          "## Using `Button` states",
          "### The **primary_action** row",
        ].join("\n\n"),
      }),
    );
    expect(html).toContain('<h2 id="using-button-states">');
    expect(html).toContain('<h3 id="the-primary_action-row">');
    expect(html).not.toContain("object");
  });
});
