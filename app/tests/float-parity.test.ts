import { expect, test } from "vitest";
import { promises as fs } from "node:fs";
import path from "node:path";
import { researchTools } from "@/server/research/agent";
import { packageTokens } from "@/server/research/evidence";
import {
  parseJson,
  pyFloatRepr,
  pyJsonStringify,
} from "@/server/sources/pyjson";
import { getReference } from "@/server/sources";
import { pyRound } from "@/server/sources/tokens";
import fixture from "./fixtures/float-parity.json";
import { repoFixture } from "./helpers";

// fixtures/float-parity.json holds what Python (server/library.py's JSON
// printing and tools/catalog.py's export) prints for the same inputs. Rebuild
// it with `python3 app/scripts/build-float-parity-fixture.py`.

test.each(fixture.json)("json.dumps parity: $name", ({ text, python }) => {
  expect(pyJsonStringify(parseJson(text))).toBe(python);
});

test("plain JSON.stringify still prints the number, for the database and the page", () => {
  const parsed = parseJson("[1.0, 0.5]");
  expect(JSON.stringify(parsed)).toBe("[1,0.5]");
  expect(pyJsonStringify(parsed)).toBe("[1.0,0.5]");
});

test("pyFloatRepr matches Python's repr on the edges", () => {
  expect(
    [0, -0, 1, 1e-4, 1e-5, 1e15, 1e16, 1.5e300, 5e-324, 0.1 + 0.2].map(
      pyFloatRepr,
    ),
  ).toEqual([
    "0.0",
    "-0.0",
    "1.0",
    "0.0001",
    "1e-05",
    "1000000000000000.0",
    "1e+16",
    "1.5e+300",
    "5e-324",
    "0.30000000000000004",
  ]);
});

async function tokenRepo() {
  const root = await repoFixture("float-parity-");
  await fs.mkdir(path.join(root, "systems/test"), { recursive: true });
  await fs.writeFile(
    path.join(root, "catalog.json"),
    JSON.stringify({
      systems: [
        {
          slug: "test",
          name: "Test",
          platform: "web",
          themes: [],
          tokens: "systems/test/tokens.json",
        },
      ],
    }),
  );
  await fs.writeFile(
    path.join(root, "systems/test/tokens.json"),
    fixture.tokens.text,
  );
}

test("package tokens print floats as catalog.py's export does", async () => {
  await tokenRepo();
  const page = await packageTokens("systems:test", "core", 0, new Set());
  const python = fixture.tokens.python as Record<string, string>;
  const byName = new Map(page.tokens!.map((token) => [token.name, token]));
  // Python exports CSS text; the tool keeps structured values, so a scalar
  // number must print as the text Python gives and a list as its elements.
  for (const [name, css] of [
    ["opacity", python["--opacity"]],
    ["lineHeight", python["--lineHeight"]],
    ["weight", python["--weight"]],
    ["tiny", python["--tiny"]],
    ["alias", python["--alias"]],
    ["legacy", python["--legacy"]],
  ])
    expect(pyJsonStringify(byName.get(`core.${name}`)!.value), name).toBe(css);
  expect(pyJsonStringify(byName.get("core.ease")!.value)).toBe(
    `[${python["--ease"].slice("cubic-bezier(".length, -1).replace(/, /g, ",")}]`,
  );
  // A DTCG colour with float components and alpha still becomes hex.
  expect(byName.get("core.wash")!.value).toBe(python["--wash"]);
  // 0.3 and 0.7 land on .5 after * 255: Python rounds those to even.
  expect(python["--half"]).toBe("#4cb2804c");
  expect(byName.get("core.half")!.value).toBe(python["--half"]);
});

test("the research tool hands the model the same text Python would print", async () => {
  await tokenRepo();
  const tools = researchTools({ excludedIds: [] });
  const output = await tools.getPackageTokens.execute!(
    { referenceId: "systems:test", group: "core.opacity", offset: 0 },
    { toolCallId: "test", messages: [], context: {} },
  );
  // Saved conversations and the stream are plain JSON; replay must still
  // show the model 1.0.
  const replayed = JSON.parse(JSON.stringify(output));
  expect(JSON.stringify(replayed.tokens[0].value)).toBe("1");
  const model = await tools.getPackageTokens.toModelOutput!({
    toolCallId: "test",
    input: { referenceId: "systems:test", group: "core.opacity", offset: 0 },
    output: replayed,
  });
  expect(model).toMatchObject({ type: "text" });
  expect((model as { value: string }).value).toContain('"value":1.0');
  expect((model as { value: string }).value).not.toContain('"value":1,');
});

test("reference detail shows floats the way str(float) prints them", async () => {
  await tokenRepo();
  await fs.writeFile(
    path.join(process.env.DESIGN_SYSTEMS_REPO!, "systems/test/tokens.json"),
    '{"core":{"spacing":{"unit":{"$value":8.0},"pair":{"$value":[4.0,0.5]}},"radius":{"card":{"$value":2.50}}}}',
  );
  const detail = await getReference("systems:test");
  const shown = new Map(
    [...detail!.spacing, ...detail!.radii].map((v) => [v.name, v.value]),
  );
  expect(shown.get("core.spacing.unit")).toBe("8.0");
  expect(shown.get("core.spacing.pair")).toBe("4.0, 0.5");
  expect(shown.get("core.radius.card")).toBe("2.5");
});

test("pyRound rounds halves to the even neighbour, as Python's round() does", () => {
  expect([0.5, 1.5, 2.5, 76.5, 178.5, 127.5, -0.5, -1.5].map(pyRound)).toEqual([
    0, 2, 2, 76, 178, 128, 0, -2,
  ]);
  expect([76.4, 76.6, 0, 255].map(pyRound)).toEqual([76, 77, 0, 255]);
});
