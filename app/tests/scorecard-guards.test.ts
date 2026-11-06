import { afterEach, expect, test } from "vitest";
import { promises as fs } from "node:fs";
import os from "node:os";
import path from "node:path";
import {
  changelog,
  counts,
  load,
  systemReport,
} from "@/server/knowledge/scorecard";

const originalRepo = process.env.DESIGN_SYSTEMS_REPO;
const dirs: string[] = [];
afterEach(async () => {
  if (originalRepo === undefined) delete process.env.DESIGN_SYSTEMS_REPO;
  else process.env.DESIGN_SYSTEMS_REPO = originalRepo;
  await Promise.all(
    dirs.splice(0).map((dir) => fs.rm(dir, { recursive: true, force: true })),
  );
});
const criteria = {
  version: "3",
  layers: { F: "Foundations" },
  criteria: [
    { id: "F1", layer: "Foundations", title: "Color roles", doneWhen: "Roles" },
    { id: "F2", layer: "Foundations", title: "Type scale", doneWhen: "Scale" },
  ],
};
const system = (grades: Record<string, unknown>) => ({
  slug: "test",
  name: "Test",
  category: "App",
  goodFor: "Testing",
  url: "https://example.test",
  captured: "2026-10-01",
  themes: ["dark"],
  platform: "web",
  grades,
});
async function fixture() {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), "scorecard-guards-"));
  dirs.push(root);
  process.env.DESIGN_SYSTEMS_REPO = root;
  await fs.mkdir(path.join(root, "scorecard/audits"), { recursive: true });
  await fs.writeFile(
    path.join(root, "scorecard/criteria.json"),
    JSON.stringify(criteria),
  );
  return root;
}
async function writeAudit(root: string, name: string, grades: object) {
  await fs.writeFile(
    path.join(root, `scorecard/audits/${name}.json`),
    JSON.stringify({
      date: name.slice(0, 10),
      method: "Review",
      systems: [system(grades as Record<string, unknown>)],
    }),
  );
}

test("a snapshot without a grade for a criterion renders instead of throwing", async () => {
  const root = await fixture();
  // The older snapshot predates F2; the newer one holds a typo'd grade.
  await writeAudit(root, "2026-10-01", {
    F1: { grade: "partly", evidence: "One state" },
  });
  await writeAudit(root, "2026-10-02", {
    F1: { grade: "meet", evidence: "Typo" },
    F2: { grade: "meets", evidence: "Scale recorded" },
  });
  const { criteria: rubric, audits } = load();
  const older = audits[0],
    newer = audits[1];
  const rows = systemReport(rubric, older, "test").layers[0].rows;
  expect(rows.find((row) => row.id === "F2")).toMatchObject({
    grade: "na",
    evidence: "Not graded in this audit.",
  });
  expect(
    systemReport(rubric, newer, "test").layers[0].rows.find(
      (row) => row.id === "F1",
    )?.grade,
  ).toBe("na");
  expect(counts(newer.systems[0])).toEqual({
    meets: 1,
    partly: 0,
    missing: 0,
    na: 0,
  });
  expect(JSON.stringify(changelog(rubric, audits))).toContain("partly → meet");
});

test("load reuses parsed snapshots until a scorecard file changes", async () => {
  const root = await fixture();
  await writeAudit(root, "2026-10-01", {
    F1: { grade: "partly", evidence: "One state" },
    F2: { grade: "missing", evidence: "None" },
  });
  const first = load();
  expect(load()).toBe(first);
  await writeAudit(root, "2026-10-02", {
    F1: { grade: "meets", evidence: "All states" },
    F2: { grade: "missing", evidence: "None" },
  });
  const second = load();
  expect(second).not.toBe(first);
  expect(second.audits).toHaveLength(2);
});
