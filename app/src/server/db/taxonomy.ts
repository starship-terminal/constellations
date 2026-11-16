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

/** Per-capture classifications live in app state, alongside the v4 vocabulary. */
export const mediaTaxonomyMigration = [
  `CREATE TABLE IF NOT EXISTS media_term_assignments (reference_id TEXT NOT NULL, media_id TEXT NOT NULL, term_id TEXT NOT NULL REFERENCES taxonomy_terms(id) ON DELETE CASCADE, reason TEXT NOT NULL DEFAULT '', origin TEXT NOT NULL CHECK(origin IN ('curated','manual')), PRIMARY KEY(reference_id,media_id,term_id))`,
  `CREATE INDEX IF NOT EXISTS media_term_assignments_term ON media_term_assignments(term_id)`,
  `CREATE TRIGGER IF NOT EXISTS media_terms_taxonomy_insert BEFORE INSERT ON media_term_assignments WHEN NOT EXISTS (SELECT 1 FROM taxonomy_terms t JOIN taxonomy_groups g ON g.id=t.group_id WHERE t.id=NEW.term_id AND g.kind='taxonomy' AND g.id NOT IN ('web-categories','ios-categories')) BEGIN SELECT RAISE(ABORT,'Media classifications must use screen taxonomy terms'); END`,
  `CREATE TRIGGER IF NOT EXISTS media_terms_taxonomy_update BEFORE UPDATE OF term_id ON media_term_assignments WHEN NOT EXISTS (SELECT 1 FROM taxonomy_terms t JOIN taxonomy_groups g ON g.id=t.group_id WHERE t.id=NEW.term_id AND g.kind='taxonomy' AND g.id NOT IN ('web-categories','ios-categories')) BEGIN SELECT RAISE(ABORT,'Media classifications must use screen taxonomy terms'); END`,
];

/** Seed exactly once in v5; subsequent opens always read current SQLite state. */
export async function seedMediaTaxonomy(tx: Transaction) {
  if (
    (await tx.execute("SELECT 1 FROM media_term_assignments LIMIT 1")).rows
      .length
  )
    return;
  const { default: seed } = await import("@/data/media-taxonomy.json");
  const known = new Set(
    (await tx.execute("SELECT id FROM taxonomy_terms")).rows.map((row) =>
      String(row.id),
    ),
  );
  const entries = seed.assignments.flatMap((assignment) =>
    // A v4 user may have removed vocabulary terms. Respect those deletions:
    // seed only still-existing terms instead of restoring them or blocking open.
    assignment.terms
      .filter((term) => known.has(term.termId))
      .map((term) => {
        if (!Object.hasOwn(seed.rules, term.rule))
          throw new Error(`Unknown media taxonomy seed rule: ${term.rule}`);
        if (
          !assignment.referenceId.startsWith("systems:") ||
          !assignment.mediaId.startsWith(
            `systems/${assignment.referenceId.slice("systems:".length)}/`,
          )
        )
          throw new Error("Invalid media taxonomy seed identity");
        return [
          assignment.referenceId,
          assignment.mediaId,
          term.termId,
          `${term.reason} Rule: ${term.rule}. Source: ${assignment.mediaId}`,
          "curated",
        ];
      }),
  );
  // Multi-row statements keep migration work bounded and avoid one round trip
  // per label, while staying below SQLite's conservative 999 parameter limit.
  for (let offset = 0; offset < entries.length; offset += 150) {
    const batch = entries.slice(offset, offset + 150);
    await tx.execute({
      sql: `INSERT INTO media_term_assignments(reference_id,media_id,term_id,reason,origin) VALUES ${batch.map(() => "(?,?,?,?,?)").join(",")}`,
      args: batch.flat(),
    });
  }
}

/**
 * Migration v6 tops up curated seed rows the guarded seeds missed: a database
 * already at v4/v5 never re-runs seedTaxonomy/seedMediaTaxonomy, so curated
 * rows added to the seed JSON since (the Dub package's, in this change) would
 * never arrive. A reference the database already classifies in that group is
 * left alone entirely — topping up never reapplies a curated label over a
 * user's manual choice, nor restores one a user removed.
 */
export async function seedNewCuratedCategories(
  tx: Transaction,
  onlyReferences?: ReadonlySet<string>,
) {
  const { taxonomySnapshots } = await import("@/contracts/taxonomy");
  const { default: assignments } =
    await import("@/data/system-categories.json");
  const classified = new Set(
    (
      await tx.execute(
        "SELECT c.reference_id,t.group_id FROM reference_categories c JOIN taxonomy_terms t ON t.id=c.term_id",
      )
    ).rows.map((row) => `${row.reference_id}${row.group_id}`),
  );
  const existingTerms = new Set(
    (await tx.execute("SELECT id FROM taxonomy_terms")).rows.map((row) =>
      String(row.id),
    ),
  );
  for (const assignment of assignments) {
    // A top-up scoped to one batch's new references never resurrects labels a
    // user cleared on an older package: those references are skipped before
    // the empty-assignment check can read them as "never labelled".
    if (onlyReferences && !onlyReferences.has(assignment.referenceId)) continue;
    const group = taxonomySnapshots
      .flatMap((snapshot) => snapshot.groups)
      .find((candidate) => candidate.id === assignment.groupId);
    if (!group || !isCategoryGroup(group.id))
      throw new Error(`Invalid curated category group: ${assignment.groupId}`);
    if (classified.has(`${assignment.referenceId}${assignment.groupId}`))
      continue;
    for (const label of new Set(assignment.labels)) {
      const term = group.terms.find((candidate) => candidate.label === label);
      if (!term)
        throw new Error(
          `Unknown curated category: ${assignment.groupId}/${label}`,
        );
      // As in seedMediaTaxonomy, a user may have removed vocabulary terms —
      // seed only still-existing ones instead of restoring them.
      if (!existingTerms.has(term.id)) continue;
      await tx.execute({
        sql: "INSERT INTO reference_categories(reference_id,term_id,reason,origin) VALUES(?,?,?,'curated')",
        args: [assignment.referenceId, term.id, assignment.reason],
      });
    }
  }
}

/** The media side of v6; a labelled media pair is never touched again. */
export async function seedNewCuratedMediaTerms(
  tx: Transaction,
  onlyReferences?: ReadonlySet<string>,
) {
  const { default: seed } = await import("@/data/media-taxonomy.json");
  const known = new Set(
    (await tx.execute("SELECT id FROM taxonomy_terms")).rows.map((row) =>
      String(row.id),
    ),
  );
  const labeled = new Set(
    (
      await tx.execute(
        "SELECT DISTINCT reference_id,media_id FROM media_term_assignments",
      )
    ).rows.map((row) => `${row.reference_id}${row.media_id}`),
  );
  const entries = seed.assignments.flatMap((assignment) => {
    if (onlyReferences && !onlyReferences.has(assignment.referenceId))
      return [];
    if (labeled.has(`${assignment.referenceId}${assignment.mediaId}`))
      return [];
    return assignment.terms
      .filter((term) => known.has(term.termId))
      .map((term) => {
        if (!Object.hasOwn(seed.rules, term.rule))
          throw new Error(`Unknown media taxonomy seed rule: ${term.rule}`);
        if (
          !assignment.referenceId.startsWith("systems:") ||
          !assignment.mediaId.startsWith(
            `systems/${assignment.referenceId.slice("systems:".length)}/`,
          )
        )
          throw new Error("Invalid media taxonomy seed identity");
        return [
          assignment.referenceId,
          assignment.mediaId,
          term.termId,
          `${term.reason} Rule: ${term.rule}. Source: ${assignment.mediaId}`,
          "curated",
        ];
      });
  });
  for (let offset = 0; offset < entries.length; offset += 150) {
    const batch = entries.slice(offset, offset + 150);
    await tx.execute({
      sql: `INSERT INTO media_term_assignments(reference_id,media_id,term_id,reason,origin) VALUES ${batch.map(() => "(?,?,?,?,?)").join(",")}`,
      args: batch.flat(),
    });
  }
}

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
    async listMediaTermAssignments(): Promise<
      { referenceId: string; mediaId: string; termId: string }[]
    > {
      const result = await client.execute(
        "SELECT reference_id,media_id,term_id FROM media_term_assignments ORDER BY reference_id,media_id,term_id",
      );
      return result.rows.map((row) => ({
        referenceId: String(row.reference_id),
        mediaId: String(row.media_id),
        termId: String(row.term_id),
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
    async listReferenceCategoryDetails(
      referenceIds?: readonly string[],
    ): Promise<{ referenceId: string; termId: string; label: string }[]> {
      const ids =
        referenceIds === undefined ? undefined : [...new Set(referenceIds)];
      if (ids?.length === 0) return [];
      // Stay below SQLite's conservative 999-bound-parameter limit.
      const batches: (string[] | undefined)[] = ids ? [] : [undefined];
      if (ids) {
        for (let offset = 0; offset < ids.length; offset += 900) {
          batches.push(ids.slice(offset, offset + 900));
        }
      }
      const details: { referenceId: string; termId: string; label: string }[] =
        [];
      for (const batch of batches) {
        const result = await client.execute({
          sql: `SELECT c.reference_id,c.term_id,t.label FROM reference_categories c JOIN taxonomy_terms t ON t.id=c.term_id WHERE t.group_id IN ('web-categories','ios-categories')${batch ? ` AND c.reference_id IN (${batch.map(() => "?").join(",")})` : ""} ORDER BY c.reference_id,c.term_id`,
          args: batch ?? [],
        });
        details.push(
          ...result.rows.map((row) => ({
            referenceId: String(row.reference_id),
            termId: String(row.term_id),
            label: String(row.label),
          })),
        );
      }
      return details.sort((a, b) =>
        a.referenceId < b.referenceId
          ? -1
          : a.referenceId > b.referenceId
            ? 1
            : a.termId < b.termId
              ? -1
              : a.termId > b.termId
                ? 1
                : 0,
      );
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
