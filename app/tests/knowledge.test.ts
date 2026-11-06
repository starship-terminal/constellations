import { expect, test } from "vitest";
import { promises as fs } from "node:fs";
import path from "node:path";
import { renderToStaticMarkup } from "react-dom/server";
import {
  documentHref,
  headingId,
  listLibraryDocuments,
  readLibraryDocument,
} from "@/server/knowledge/docs";
import {
  counts,
  indexStats,
  load,
  systemReport,
  wordings,
} from "@/server/knowledge/scorecard";
import {
  ScorecardOverview,
  PackageScorecard,
  ScorecardCriteria,
  ScorecardHistory,
} from "@/features/knowledge/scorecard";
import { DocumentMarkdown } from "@/features/knowledge/markdown";
import { repoFixture, tempDir } from "./helpers";
async function fixture() {
  const root = await repoFixture("knowledge-");
  await fs.mkdir(path.join(root, "docs"));
  return root;
}
test("docs reader follows the mounted repository and rejects traversal and symlink escapes", async () => {
  const root = await fixture();
  await fs.writeFile(
    path.join(root, "docs/PACKAGE.md"),
    "---\ntitle: metadata\n---\n# A package\n\nThis paragraph describes the package.\n\n## Coverage\n",
  );
  await fs.writeFile(path.join(root, "secret.md"), "private value");
  await fs.symlink(
    path.join(root, "secret.md"),
    path.join(root, "docs/leak.md"),
  );
  expect(await readLibraryDocument("../secret")).toBeNull();
  expect(await readLibraryDocument("leak")).toBeNull();
  expect(await readLibraryDocument("%2e%2e/secret")).toBeNull();
  const docs = await listLibraryDocuments();
  expect(docs).toHaveLength(1);
  expect(docs[0]).toMatchObject({
    slug: "PACKAGE",
    title: "A package",
    excerpt: "This paragraph describes the package.",
  });
  expect(docs[0].text).not.toContain("metadata");
  const outside = await tempDir("knowledge-outside-");
  await fs.writeFile(path.join(outside, "external.md"), "outside");
  await fs.rm(path.join(root, "docs"), { recursive: true });
  await fs.symlink(outside, path.join(root, "docs"));
  expect(await listLibraryDocuments()).toEqual([]);
  expect(await readLibraryDocument("external")).toBeNull();
});
test("document links preserve anchors and point to new docs/package readers", () => {
  expect(documentHref("docs/EVIDENCE.md", "PACKAGE.md#layout")).toBe(
    "/docs/PACKAGE#layout",
  );
  expect(
    documentHref("docs/PACKAGE.md", "../systems/linear/components.md#button"),
  ).toBe("/library/linear?tab=files&file=components.md#button");
  expect(
    documentHref("docs/PACKAGE.md", "../systems/linear/screenshots/home.png"),
  ).toBe("/media/systems/linear/screenshots/home.png");
  expect(documentHref("docs/PACKAGE.md", "#designmd")).toBe("#designmd");
  for (const value of [
    "javascript:alert(1)",
    "//outside.test/x",
    "../../.env",
    "../server/db/index.ts",
  ])
    expect(documentHref("docs/PACKAGE.md", value)).toBeNull();
  expect(headingId("Using a style: README.md")).toBe("using-a-style-readmemd");
  const html = renderToStaticMarkup(
    DocumentMarkdown({
      text: "# Reading the evidence\n\n[Package](PACKAGE.md#layout)\n\n<script>alert(1)</script>",
      base: "docs/EVIDENCE.md",
    }),
  );
  expect(html).toContain('id="reading-the-evidence"');
  expect(html).toContain('href="/docs/PACKAGE#layout"');
  expect(html).not.toContain("<script>");
});
test("scorecard reads canonical platform wording, audit history and evidence from runtime root", async () => {
  const root = await fixture();
  await fs.mkdir(path.join(root, "scorecard/audits"), { recursive: true });
  const criteria = {
    version: "3",
    layers: { F: "Foundations" },
    criteria: [
      {
        id: "F1",
        layer: "Foundations",
        title: "Color roles",
        doneWhen: "Web roles",
        platforms: { mobile: "Mobile roles" },
      },
    ],
  };
  const system = {
    slug: "test",
    name: "Test",
    category: "App",
    goodFor: "Testing",
    url: "https://example.test",
    captured: "2026-10-01",
    themes: ["dark"],
    platform: "mobile",
    reviewedPlatform: "web",
    grades: {
      F1: { grade: "partly", evidence: "Only one state was captured" },
    },
  };
  await fs.writeFile(
    path.join(root, "scorecard/criteria.json"),
    JSON.stringify(criteria),
  );
  await fs.writeFile(
    path.join(root, "scorecard/audits/2026-10-01.json"),
    JSON.stringify({
      date: "2026-10-01",
      method: "Read captured evidence",
      systems: [system],
    }),
  );
  await fs.writeFile(
    path.join(root, "scorecard/audits/2026-10-01-2.json"),
    JSON.stringify({
      date: "2026-10-01",
      method: "Second review",
      systems: [
        {
          ...system,
          grades: { F1: { grade: "meets", evidence: "All states recorded" } },
        },
      ],
    }),
  );
  const data = load(),
    audit = data.audits.at(-1)!;
  expect(audit.seq).toBe(2);
  expect(counts(audit.systems[0]).meets).toBe(1);
  expect(indexStats(data.criteria, audit).pct).toBe(100);
  expect(systemReport(data.criteria, audit, "test")).toMatchObject({
    platform: "mobile",
    wasPlatform: "web",
    layers: [
      { rows: [{ doneWhen: "Mobile roles", evidence: "All states recorded" }] },
    ],
  });
  expect(wordings(data.criteria.criteria[0])).toHaveLength(2);
  const overview = renderToStaticMarkup(ScorecardOverview());
  expect(overview).toContain('href="/scorecard/test#f1"');
  expect(overview).toContain('aria-label="Package criterion heatmap"');
  const report = renderToStaticMarkup(PackageScorecard({ slug: "test" }));
  expect(report).toContain("All states recorded");
  expect(report).toContain("needs another review");
  expect(report).toContain('href="/styles/systems/test"');
  expect(renderToStaticMarkup(ScorecardCriteria())).toContain("Mobile roles");
  expect(renderToStaticMarkup(ScorecardHistory())).toContain("2026-10-01");
});

test("scorecard ranks applicable gaps by ratio and excludes N/A cells from completion", () => {
  const criteria = {
    version: "3",
    layers: { F: "Foundations" },
    criteria: [
      {
        id: "F1",
        layer: "Foundations",
        title: "Usually complete",
        doneWhen: "Recorded",
      },
      {
        id: "F2",
        layer: "Foundations",
        title: "Larger gap",
        doneWhen: "Recorded",
      },
      {
        id: "V1",
        layer: "Foundations",
        title: "Optional publication",
        doneWhen: "Published",
        optional: "Only when published",
      },
      {
        id: "C5",
        layer: "Foundations",
        title: "Optional applicable guidance",
        doneWhen: "Published",
        optional: "Only when published",
      },
    ],
  };
  const base = {
    slug: "a",
    name: "A",
    category: "App",
    goodFor: "Tests",
    url: "https://example.test",
    captured: "2026-10-01",
    themes: [],
    grades: {},
  };
  const grade = (value: "meets" | "partly" | "missing" | "na") => ({
    grade: value,
    evidence: "Recorded",
  });
  const audit = {
    date: "2026-10-01",
    method: "Reviewed",
    seq: 1,
    systems: [
      {
        ...base,
        grades: {
          F1: grade("meets"),
          F2: grade("missing"),
          V1: grade("na"),
          C5: grade("partly"),
        },
      },
      {
        ...base,
        slug: "b",
        name: "B",
        grades: {
          F1: grade("meets"),
          F2: grade("partly"),
          V1: grade("na"),
          C5: grade("na"),
        },
      },
      {
        ...base,
        slug: "c",
        name: "C",
        grades: {
          F1: grade("missing"),
          F2: grade("meets"),
          V1: grade("na"),
          C5: grade("na"),
        },
      },
    ],
  };
  const stats = indexStats(criteria, audit);
  expect(stats.totalCells).toBe(12);
  expect(stats.applicableCells).toBe(7);
  expect(stats.meets).toBe(3);
  expect(stats.pct).toBe(43);
  expect(stats.weakest.map((criterion) => criterion.id)).toEqual([
    "C5",
    "F2",
    "F1",
  ]);
  expect(stats.weakest[0]).toMatchObject({
    meets: 0,
    applicable: 1,
    unmetRatio: 1,
  });
  expect(
    stats.weakest.find((criterion) => criterion.id === "V1"),
  ).toBeUndefined();
  const allNa = indexStats(criteria, {
    ...audit,
    systems: [
      {
        ...base,
        grades: {
          F1: grade("na"),
          F2: grade("na"),
          V1: grade("na"),
          C5: grade("na"),
        },
      },
    ],
  });
  expect(allNa.applicableCells).toBe(0);
  expect(allNa.pct).toBeNull();
  expect(allNa.weakest).toEqual([]);
});
