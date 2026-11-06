import { afterEach, expect, test } from "vitest";
import { promises as fs } from "node:fs";
import os from "node:os";
import path from "node:path";
import { getReference } from "@/server/sources";
import { packageTokens } from "@/server/research/evidence";

// Shapes taken from real packages: Claude's set-scoped role aliases
// (core.color.role.accent.100 = {color.blue.100}), Polaris's legacy `value`
// leaves and CSS keyframe text, and Duolingo's core lip shadow whose colour
// exists only in each theme. The expected values are what
// `python3 tools/catalog.py export` prints for this file.
const TOKENS = {
  core: {
    color: {
      blue: { "100": { $value: "#cde2fb", $type: "color" } },
      role: {
        accent: { "100": { $value: "{color.blue.100}", $type: "color" } },
      },
      gray: { "1": { value: "rgba(255, 255, 255, 1)", type: "color" } },
      surface: { value: "{color.gray.1}", type: "color" },
    },
    shadow: {
      lip: {
        $value: {
          offsetX: "0px",
          offsetY: "4px",
          blur: "0px",
          spread: "0px",
          color: "{accent.lip}",
        },
        $type: "shadow",
      },
    },
    keyframes: { fade: { value: "{ to { opacity: 1 } }", type: "other" } },
  },
  light: {
    accent: { lip: { $value: "#58a700", $type: "color" } },
    text: { $value: "{color.role.accent.100}", $type: "color" },
  },
  dark: {
    accent: { lip: { $value: "#79b933", $type: "color" } },
    text: { $value: "{color.role.accent.100}", $type: "color" },
  },
};
const PYTHON_EXPORT = {
  base: {
    "core.color.role.accent.100": "#cde2fb",
    "core.color.surface": "rgba(255, 255, 255, 1)",
    "core.keyframes.fade": "{ to { opacity: 1 } }",
  },
  light: { "light.text": "#cde2fb", "core.shadow.lip": "#58a700" },
  dark: { "dark.text": "#cde2fb", "core.shadow.lip": "#79b933" },
};
const originalRepo = process.env.DESIGN_SYSTEMS_REPO;
const dirs: string[] = [];
afterEach(async () => {
  if (originalRepo === undefined) delete process.env.DESIGN_SYSTEMS_REPO;
  else process.env.DESIGN_SYSTEMS_REPO = originalRepo;
  await Promise.all(
    dirs.splice(0).map((dir) => fs.rm(dir, { recursive: true, force: true })),
  );
});
async function fixture() {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), "token-parity-"));
  dirs.push(root);
  process.env.DESIGN_SYSTEMS_REPO = root;
  await fs.mkdir(path.join(root, "systems/test"), { recursive: true });
  await fs.writeFile(
    path.join(root, "catalog.json"),
    JSON.stringify({
      systems: [
        {
          slug: "test",
          name: "Test",
          platform: "web",
          themes: ["light", "dark"],
          tokens: "systems/test/tokens.json",
        },
      ],
    }),
  );
  await fs.writeFile(
    path.join(root, "systems/test/tokens.json"),
    JSON.stringify(TOKENS),
  );
}

test("reference detail resolves set-scoped aliases and legacy value leaves like catalog.py", async () => {
  await fixture();
  const detail = await getReference("systems:test");
  const values = new Map(
    [...detail!.colors, ...detail!.typography, ...detail!.spacing].map((v) => [
      v.name,
      v.value,
    ]),
  );
  expect(values.get("core.color.role.accent.100")).toBe(
    PYTHON_EXPORT.base["core.color.role.accent.100"],
  );
  expect(values.get("core.color.gray.1")).toBe("rgba(255, 255, 255, 1)");
  expect(values.get("core.color.surface")).toBe(
    PYTHON_EXPORT.base["core.color.surface"],
  );
  expect(values.get("light.text")).toBe(PYTHON_EXPORT.light["light.text"]);
});

test("package tokens give catalog.py's values, per theme for core aliases into a theme", async () => {
  await fixture();
  const all = new Map<string, any>();
  for (const group of ["core", "light", "dark"]) {
    const page = await packageTokens("systems:test", group, 0, new Set());
    for (const token of page.tokens || []) all.set(token.name, token);
  }
  for (const [name, value] of Object.entries(PYTHON_EXPORT.base))
    expect(all.get(name).value, name).toBe(value);
  expect(all.get("light.text").value).toBe(PYTHON_EXPORT.light["light.text"]);
  expect(all.get("dark.text").value).toBe(PYTHON_EXPORT.dark["dark.text"]);
  const lip = all.get("core.shadow.lip");
  expect(lip.themes.light.color).toBe(PYTHON_EXPORT.light["core.shadow.lip"]);
  expect(lip.themes.dark.color).toBe(PYTHON_EXPORT.dark["core.shadow.lip"]);
  expect(lip.rawValue.color).toBe("{accent.lip}");
});
