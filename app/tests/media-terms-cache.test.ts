import { expect, test, vi } from "vitest";
import mediaSeed from "@/data/media-taxonomy.json";
import { tempStore } from "./helpers";

test("the media term map is read once and re-read after any write, plain SQL included", async () => {
  const { store } = await tempStore("media-terms-cache-");
  const first = await store.mediaTermsByMedia();
  expect(await store.mediaTermsByMedia()).toBe(first);
  const sample = mediaSeed.assignments[0];
  const id = `${sample.referenceId}:${sample.mediaId}`;
  expect(first.get(id)).toEqual(
    [...new Set(sample.terms.map((term) => term.termId))].sort(),
  );
  await store.client.execute({
    sql: "DELETE FROM media_term_assignments WHERE reference_id=? AND media_id=?",
    args: [sample.referenceId, sample.mediaId],
  });
  const afterDelete = await store.mediaTermsByMedia();
  expect(afterDelete).not.toBe(first);
  expect(afterDelete.has(id)).toBe(false);
  await store.client.execute({
    sql: "INSERT INTO media_term_assignments(reference_id,media_id,term_id,reason,origin) VALUES(?,?,?,'test','manual')",
    args: [sample.referenceId, sample.mediaId, sample.terms[0].termId],
  });
  expect((await store.mediaTermsByMedia()).get(id)).toEqual([
    sample.terms[0].termId,
  ]);
});

test("parallel reads share one load of the assignments", async () => {
  const { store } = await tempStore("media-terms-parallel-");
  const execute = vi.spyOn(store.client, "execute");
  const maps = await Promise.all([
    store.mediaTermsByMedia(),
    store.mediaTermsByMedia(),
    store.mediaTermsByMedia(),
  ]);
  expect(new Set(maps).size).toBe(1);
  const fullReads = execute.mock.calls.filter(([statement]) =>
    String(statement).includes("FROM media_term_assignments"),
  );
  expect(fullReads).toHaveLength(1);
  execute.mockRestore();
});

test("a version-44 store gains the revision table and its triggers", async () => {
  const { dir, store } = await tempStore("media-terms-v44-");
  for (const event of ["insert", "update", "delete"])
    await store.client.execute(`DROP TRIGGER media_terms_revision_${event}`);
  await store.client.execute("DROP TABLE media_terms_revision");
  await store.client.execute("PRAGMA user_version=44");
  store.close();
  const { createResearchStore, RESEARCH_DB_VERSION } =
    await import("@/server/db");
  const reopened = await createResearchStore(dir);
  try {
    expect(
      Number(
        (await reopened.client.execute("PRAGMA user_version")).rows[0]
          .user_version,
      ),
    ).toBe(RESEARCH_DB_VERSION);
    const before = await reopened.mediaTermsByMedia();
    await reopened.client.execute("DELETE FROM media_term_assignments");
    expect((await reopened.mediaTermsByMedia()).size).toBe(0);
    expect(before.size).toBeGreaterThan(0);
  } finally {
    reopened.close();
  }
});
