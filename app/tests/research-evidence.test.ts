import { expect, test } from "vitest";
import { z } from "zod";
import { promises as fs } from "node:fs";
import path from "node:path";
import { researchTools, modelHistory } from "@/server/research/agent";
import {
  packageDocument,
  packageTokens,
  handoffPrompt,
} from "@/server/research/evidence";
import { repoFixture } from "./helpers";
const execution = { toolCallId: "test", messages: [], context: {} };
async function fixture() {
  const root = await repoFixture("research-evidence-");
  await fs.mkdir(path.join(root, "systems/test/screenshots"), {
    recursive: true,
  });
  await fs.writeFile(
    path.join(root, "catalog.json"),
    JSON.stringify({
      systems: [
        {
          slug: "test",
          name: "Test",
          platform: "web",
          themes: ["dark"],
          entry: "systems/test/README.md",
          tokens: "systems/test/tokens.json",
        },
      ],
    }),
  );
  await fs.writeFile(
    path.join(root, "systems/test/README.md"),
    "# Test\n\nCapture limit: one platform only.\n" +
      "captured evidence ".repeat(2000),
  );
  await fs.writeFile(
    path.join(root, "systems/test/components.md"),
    "# Components\n\nButton uses motion.fast.",
  );
  await fs.writeFile(
    path.join(root, "systems/test/tokens.json"),
    JSON.stringify({
      core: {
        duration: {
          $value: "150ms",
          $type: "duration",
          $extensions: { evidence: "Measured" },
        },
        loopA: { $value: "{core.loopB}" },
        loopB: { $value: "{core.loopA}" },
      },
      motion: {
        fast: {
          $value: "{core.duration}",
          $type: "duration",
          $extensions: { evidence: "Derived" },
        },
        composite: { $value: { duration: "{core.duration}" } },
      },
    }),
  );
  await fs.writeFile(
    path.join(root, "systems/test/screenshots/first.png"),
    new Uint8Array([137, 80, 78, 71]),
  );
  await fs.writeFile(
    path.join(root, "systems/test/screenshots/second.png"),
    new Uint8Array([137, 80, 78, 71, 2]),
  );
  return root;
}
test("research reads complete package documents in bounded pages and rejects hidden/raw/traversal files", async () => {
  const root = await fixture();
  const first = await packageDocument(
    "systems:test",
    "README.md",
    0,
    new Set(),
  );
  expect(first.text).toHaveLength(24000);
  expect(first.truncated).toBe(true);
  expect(first.text).toContain("Capture limit");
  const next = await packageDocument(
    "systems:test",
    "README.md",
    24000,
    new Set(),
  );
  expect(next.text).not.toHaveLength(0);
  expect(next.truncated).toBe(false);
  const components = await packageDocument(
    "systems:test",
    "components.md",
    0,
    new Set(),
  );
  expect(components.text).toContain("motion.fast");
  await fs.writeFile(path.join(root, ".env"), "SECRET=private");
  await fs.symlink(
    path.join(root, ".env"),
    path.join(root, "systems/test/leak.md"),
  );
  for (const file of ["../../.env", "leak.md", "raw/capture.json", ".env"])
    await expect(
      packageDocument("systems:test", file, 0, new Set()),
    ).rejects.toThrow("unavailable");
});
test("all token groups retain raw values and evidence while aliases and composite values resolve", async () => {
  await fixture();
  const groups = await packageTokens("systems:test", undefined, 0, new Set());
  expect(groups.groups?.map((group) => group.name)).toContain("motion");
  const motion = await packageTokens("systems:test", "motion", 0, new Set());
  expect(motion.tokens).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        name: "motion.fast",
        value: "150ms",
        rawValue: "{core.duration}",
        evidence: { evidence: "Derived" },
      }),
      expect.objectContaining({
        name: "motion.composite",
        value: { duration: "150ms" },
      }),
    ]),
  );
  // A cyclic alias terminates and stays an unresolved reference, never a value.
  const cycle = await packageTokens("systems:test", "core.loopA", 0, new Set());
  expect(cycle.tokens).toHaveLength(1);
  expect(cycle.tokens![0]).toMatchObject({
    name: "core.loopA",
    rawValue: "{core.loopB}",
  });
  expect(cycle.tokens![0].value).toMatch(/^\{core\.loop[AB]\}$/);
  const prompt = await handoffPrompt("systems:test", "a dashboard", new Set());
  expect(prompt.prompt).toContain("systems/test/README.md");
  expect(prompt.prompt).toContain("a dashboard");
  expect(prompt.prompt).toContain("per-value evidence");
});
test("selected media uses the requested capture and unsupported endpoints receive text only", async () => {
  await fixture();
  const tools = researchTools({ excludedIds: [] });
  const result = await tools.listReferenceMedia.execute!(
    { referenceId: "systems:test", offset: 0 },
    execution,
  );
  if (!("media" in result)) throw new Error("Expected completed media list");
  expect(result.media).toHaveLength(2);
  const second = result.media.find((media) => media.name.includes("second"))!;
  const viewed = await tools.viewReferenceMedia.execute!(
    { referenceId: "systems:test", mediaId: second.id },
    execution,
  );
  if (!("media" in viewed))
    throw new Error("Expected completed media inspection");
  expect(viewed.media.url).toContain("second.png");
  expect(viewed.visualEvidence).toBe("image-supplied");
  const output = await tools.viewReferenceMedia.toModelOutput!({
    toolCallId: "test",
    input: { referenceId: "systems:test", mediaId: second.id },
    output: viewed,
  });
  expect(JSON.stringify(output)).toContain('"type":"file"');
  const textTools = researchTools({ excludedIds: [] }, false),
    textOnly = await textTools.viewReferenceMedia.execute!(
      { referenceId: "systems:test", mediaId: second.id },
      execution,
    );
  if (!("visualEvidence" in textOnly))
    throw new Error("Expected completed text inspection");
  expect(textOnly.visualEvidence).toBe("text-only");
  await expect(
    tools.viewReferenceMedia.execute!(
      { referenceId: "systems:test", mediaId: "https://outside.test/secret" },
      execution,
    ),
  ).rejects.toThrow("not found");
});
test("exclusions apply to every new evidence tool and remove prior evidence from model history", async () => {
  await fixture();
  const tools = researchTools({ excludedIds: ["systems:test"] });
  await expect(
    tools.readPackageDocument.execute!(
      { referenceId: "systems:test", path: "README.md", offset: 0 },
      execution,
    ),
  ).rejects.toThrow("excluded");
  await expect(
    tools.getPackageTokens.execute!(
      { referenceId: "systems:test", offset: 0 },
      execution,
    ),
  ).rejects.toThrow("excluded");
  await expect(
    tools.listPackageDocuments.execute!(
      { referenceId: "systems:test", offset: 0 },
      execution,
    ),
  ).rejects.toThrow("excluded");
  await expect(
    tools.listReferenceMedia.execute!(
      { referenceId: "systems:test", offset: 0 },
      execution,
    ),
  ).rejects.toThrow("excluded");
  await expect(
    tools.handoffPrompt.execute!(
      { referenceId: "systems:test", appDescription: "" },
      execution,
    ),
  ).rejects.toThrow("excluded");
  const history = modelHistory(
    [
      {
        id: "a",
        role: "assistant",
        parts: [
          {
            type: "tool-readPackageDocument",
            toolCallId: "doc",
            state: "output-available",
            input: {
              referenceId: "systems:test",
              path: "README.md",
              offset: 0,
            },
            output: {
              kind: "package-document",
              referenceId: "systems:test",
              text: "Private evidence",
            },
          },
        ],
      },
    ] as any,
    ["systems:test"],
  );
  expect(JSON.stringify(history)).not.toContain("Private evidence");
});

test("a token named value keeps every sibling and its recorded value", async () => {
  const root = await fixture();
  // The shape that triggered the review (Telegram's light.color.text has a
  // token literally named "value"), copied with invented values so a
  // recapture of that package cannot change this test.
  await fs.writeFile(
    path.join(root, "systems/test/tokens.json"),
    JSON.stringify({
      light: {
        color: {
          text: {
            value: { $value: "#111111", $type: "color" },
            primary: { $value: "#222222", $type: "color" },
            secondary: {
              $value: "#333333",
              $type: "color",
              $extensions: { evidence: "Sampled" },
            },
          },
        },
      },
    }),
  );
  const text = await packageTokens(
    "systems:test",
    "light.color.text",
    0,
    new Set(),
  );
  expect(
    text.tokens?.map((token) => ({ name: token.name, value: token.value })),
  ).toEqual([
    { name: "light.color.text.value", value: "#111111" },
    { name: "light.color.text.primary", value: "#222222" },
    { name: "light.color.text.secondary", value: "#333333" },
  ]);
  expect(text.tokens?.some((token) => token.name === "light.color.text")).toBe(
    false,
  );
});

test("legacy primitive and composite value fields still read as token leaves", async () => {
  const root = await fixture();
  await fs.writeFile(
    path.join(root, "systems/test/tokens.json"),
    JSON.stringify({
      core: {
        legacy: { value: "150ms", type: "duration" },
        composite: {
          value: { duration: "150ms", easing: [0, 0, 1, 1] },
          type: "transition",
        },
        untyped: { value: { fontFamily: "Inter", fontSize: 14 } },
      },
    }),
  );
  const result = await packageTokens("systems:test", "core", 0, new Set());
  expect(result.tokens).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ name: "core.legacy", value: "150ms" }),
      expect.objectContaining({
        name: "core.composite",
        value: { duration: "150ms", easing: [0, 0, 1, 1] },
      }),
      expect.objectContaining({
        name: "core.untyped",
        value: { fontFamily: "Inter", fontSize: 14 },
      }),
    ]),
  );
});

test("document tool schema accepts the last page of a supported four-MiB file", async () => {
  const root = await fixture();
  const end = "complete final evidence";
  const size = 4 * 1024 * 1024;
  await fs.writeFile(
    path.join(root, "systems/test/large.md"),
    "x".repeat(size - end.length) + end,
  );
  const tools = researchTools({ excludedIds: [] });
  const schema = tools.readPackageDocument.inputSchema as z.ZodType<{
    referenceId: string;
    path: string;
    offset: number;
  }>;
  const input = schema.parse({
    referenceId: "systems:test",
    path: "large.md",
    offset: size - 24000,
  });
  const page = await tools.readPackageDocument.execute!(input, execution);
  if (!("text" in page)) throw new Error("Expected completed document read");
  expect(page.text).toHaveLength(24000);
  expect(page.text.endsWith(end)).toBe(true);
  expect(page.totalCharacters).toBe(size);
  expect(page.truncated).toBe(false);
  expect(schema.safeParse({ ...input, offset: size + 1 }).success).toBe(false);
});
