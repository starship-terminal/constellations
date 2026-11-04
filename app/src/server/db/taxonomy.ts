import type { Client, Transaction } from "@libsql/client";
import type {
  TaxonomyGroup,
  TaxonomySnapshot,
  TaxonomyTerm,
} from "@/contracts/taxonomy";

/** Vocabulary revisions are explicit database migrations, never startup upserts. */
export const taxonomyMigration = [
  `CREATE TABLE IF NOT EXISTS taxonomy_snapshots (source TEXT PRIMARY KEY, captured_at TEXT NOT NULL, coverage TEXT NOT NULL, position INTEGER NOT NULL)`,
  `CREATE TABLE IF NOT EXISTS taxonomy_groups (id TEXT PRIMARY KEY, label TEXT NOT NULL, kind TEXT NOT NULL CHECK(kind IN ('taxonomy','search-preset')), applies_to TEXT NOT NULL, source_url TEXT NOT NULL, coverage TEXT NOT NULL, snapshot_source TEXT NOT NULL REFERENCES taxonomy_snapshots(source), position INTEGER NOT NULL)`,
  `CREATE TABLE IF NOT EXISTS taxonomy_terms (id TEXT PRIMARY KEY, group_id TEXT NOT NULL REFERENCES taxonomy_groups(id) ON DELETE CASCADE, label TEXT NOT NULL, source_url TEXT, subgroup TEXT, source_ids TEXT, position INTEGER NOT NULL, UNIQUE(group_id,label))`,
  `CREATE INDEX IF NOT EXISTS taxonomy_terms_group_position ON taxonomy_terms(group_id,position)`,
  `CREATE TABLE IF NOT EXISTS reference_categories (reference_id TEXT NOT NULL, term_id TEXT NOT NULL REFERENCES taxonomy_terms(id) ON DELETE CASCADE, reason TEXT NOT NULL DEFAULT '', origin TEXT NOT NULL CHECK(origin IN ('curated','manual')), PRIMARY KEY(reference_id,term_id))`,
  `CREATE TRIGGER IF NOT EXISTS reference_categories_category_insert BEFORE INSERT ON reference_categories WHEN NOT EXISTS (SELECT 1 FROM taxonomy_terms t JOIN taxonomy_groups g ON g.id=t.group_id WHERE t.id=NEW.term_id AND g.kind='taxonomy' AND g.id IN ('web-categories','ios-categories')) BEGIN SELECT RAISE(ABORT,'Reference classifications must use category terms'); END`,
  `CREATE TRIGGER IF NOT EXISTS reference_categories_category_update BEFORE UPDATE OF term_id ON reference_categories WHEN NOT EXISTS (SELECT 1 FROM taxonomy_terms t JOIN taxonomy_groups g ON g.id=t.group_id WHERE t.id=NEW.term_id AND g.kind='taxonomy' AND g.id IN ('web-categories','ios-categories')) BEGIN SELECT RAISE(ABORT,'Reference classifications must use category terms'); END`,
];

/** Called only inside migration v4's transaction. JSON is seed evidence. */
export async function seedTaxonomy(tx: Transaction) {
  const { taxonomySnapshots } = await import("@/contracts/taxonomy");
  const { default: assignments } =
    await import("@/data/system-categories.json");
  // Existing rows are possible only in an older-version test/recovery database.
  // Do not overwrite them, or reapply curated assignments over manual choices.
  if ((await tx.execute("SELECT 1 FROM taxonomy_groups LIMIT 1")).rows.length)
    return;
  for (const [position, snapshot] of taxonomySnapshots.entries()) {
    await tx.execute({
      sql: "INSERT INTO taxonomy_snapshots(source,captured_at,coverage,position) VALUES(?,?,?,?)",
      args: [snapshot.source, snapshot.capturedAt, snapshot.coverage, position],
    });
    for (const [groupPosition, group] of snapshot.groups.entries()) {
      await tx.execute({
        sql: "INSERT INTO taxonomy_groups(id,label,kind,applies_to,source_url,coverage,snapshot_source,position) VALUES(?,?,?,?,?,?,?,?)",
        args: [
          group.id,
          group.label,
          group.kind,
          JSON.stringify(group.appliesTo),
          group.sourceUrl,
          group.coverage,
          snapshot.source,
          groupPosition,
        ],
      });
      for (const [termPosition, term] of group.terms.entries()) {
        await tx.execute({
          sql: "INSERT INTO taxonomy_terms(id,group_id,label,source_url,subgroup,source_ids,position) VALUES(?,?,?,?,?,?,?)",
          args: [
            term.id,
            group.id,
            term.label,
            term.sourceUrl ?? null,
            term.subgroup ?? null,
            term.sourceIds ? JSON.stringify(term.sourceIds) : null,
            termPosition,
          ],
        });
      }
    }
  }
  for (const assignment of assignments) {
    const group = taxonomySnapshots
      .flatMap((snapshot) => snapshot.groups)
      .find((candidate) => candidate.id === assignment.groupId);
    if (!group || !isCategoryGroup(group.id))
      throw new Error(`Invalid curated category group: ${assignment.groupId}`);
    for (const label of new Set(assignment.labels)) {
      const term = group.terms.find((candidate) => candidate.label === label);
      if (!term)
        throw new Error(
          `Unknown curated category: ${assignment.groupId}/${label}`,
        );
      await tx.execute({
        sql: "INSERT INTO reference_categories(reference_id,term_id,reason,origin) VALUES(?,?,?,'curated')",
        args: [assignment.referenceId, term.id, assignment.reason],
      });
    }
  }
}

function isCategoryGroup(groupId: string) {
  return groupId === "web-categories" || groupId === "ios-categories";
}

export function taxonomyStore(client: Client) {
  async function listTaxonomyGroups(): Promise<TaxonomyGroup[]> {
    const [groups, terms] = await Promise.all([
      client.execute(
        "SELECT g.* FROM taxonomy_groups g JOIN taxonomy_snapshots s ON s.source=g.snapshot_source ORDER BY s.position,g.position",
      ),
      client.execute("SELECT * FROM taxonomy_terms ORDER BY position"),
    ]);
    const byGroup = new Map<string, TaxonomyTerm[]>();
    for (const row of terms.rows) {
      const term: TaxonomyTerm = {
        id: String(row.id),
        label: String(row.label),
        ...(row.source_url !== null
          ? { sourceUrl: String(row.source_url) }
          : {}),
        ...(row.subgroup !== null ? { subgroup: String(row.subgroup) } : {}),
        ...(row.source_ids !== null
          ? { sourceIds: JSON.parse(String(row.source_ids)) as string[] }
          : {}),
      };
      const groupId = String(row.group_id);
      if (!byGroup.has(groupId)) byGroup.set(groupId, []);
      byGroup.get(groupId)!.push(term);
    }
    return groups.rows.map((row) => ({
      id: String(row.id),
      label: String(row.label),
      kind: row.kind as TaxonomyGroup["kind"],
      appliesTo: JSON.parse(String(row.applies_to)) as string[],
      sourceUrl: String(row.source_url),
      coverage: String(row.coverage),
      terms: byGroup.get(String(row.id)) ?? [],
    }));
  }
  return {
    listTaxonomyGroups,
    async listTaxonomySnapshots(): Promise<TaxonomySnapshot[]> {
      const [snapshots, groups, memberships] = await Promise.all([
        client.execute("SELECT * FROM taxonomy_snapshots ORDER BY position"),
        listTaxonomyGroups(),
        client.execute("SELECT id,snapshot_source FROM taxonomy_groups"),
      ]);
      const sourceByGroup = new Map(
        memberships.rows.map((row) => [
          String(row.id),
          String(row.snapshot_source),
        ]),
      );
      return snapshots.rows.map((row) => ({
        source: String(row.source),
        capturedAt: String(row.captured_at),
        coverage: String(row.coverage),
        groups: groups.filter(
          (group) => sourceByGroup.get(group.id) === row.source,
        ),
      }));
    },
    async listReferenceCategories(): Promise<
      { referenceId: string; termId: string }[]
    > {
      const result = await client.execute(
        "SELECT reference_id,term_id FROM reference_categories ORDER BY reference_id,term_id",
      );
      return result.rows.map((row) => ({
        referenceId: String(row.reference_id),
        termId: String(row.term_id),
      }));
    },
    async assignReferenceCategories(
      referenceId: string,
      groupId: string,
      labels: readonly string[],
      reason = "",
    ) {
      if (!referenceId.trim()) throw new Error("A reference ID is required");
      if (!isCategoryGroup(groupId))
        throw new Error("Only category groups can classify references");
      const tx = await client.transaction("write");
      try {
        const result = await tx.execute({
          sql: "SELECT id,label FROM taxonomy_terms WHERE group_id=?",
          args: [groupId],
        });
        const termByLabel = new Map(
          result.rows.map((row) => [String(row.label), String(row.id)]),
        );
        const termIds = [...new Set(labels)].map((label) => {
          const id = termByLabel.get(label);
          if (!id) throw new Error(`Unknown category: ${groupId}/${label}`);
          return id;
        });
        await tx.execute({
          sql: "DELETE FROM reference_categories WHERE reference_id=? AND term_id IN (SELECT id FROM taxonomy_terms WHERE group_id=?)",
          args: [referenceId, groupId],
        });
        for (const termId of termIds)
          await tx.execute({
            sql: "INSERT INTO reference_categories(reference_id,term_id,reason,origin) VALUES(?,?,?,'manual')",
            args: [referenceId, termId, reason],
          });
        await tx.commit();
      } catch (error) {
        await tx.rollback();
        throw error;
      }
    },
  };
}
