import {
  sqliteTable,
  text,
  integer,
  primaryKey,
} from "drizzle-orm/sqlite-core";
export const conversations = sqliteTable("conversations", {
  id: text("id").primaryKey(),
  title: text("title").notNull(),
  messages: text("messages").notNull().default("[]"),
  pinnedIds: text("pinned_ids").notNull().default("[]"),
  excludedIds: text("excluded_ids").notNull().default("[]"),
  archived: integer("archived", { mode: "boolean" }).notNull().default(false),
  createdAt: integer("created_at").notNull(),
  updatedAt: integer("updated_at").notNull(),
});
export const collections = sqliteTable("collections", {
  id: text("id").primaryKey(),
  name: text("name").notNull(),
  notes: text("notes").notNull().default(""),
  createdAt: integer("created_at").notNull(),
  updatedAt: integer("updated_at").notNull(),
});
export const collectionItems = sqliteTable(
  "collection_items",
  {
    collectionId: text("collection_id")
      .notNull()
      .references(() => collections.id, { onDelete: "cascade" }),
    referenceId: text("reference_id").notNull(),
    note: text("note").notNull().default(""),
    addedAt: integer("added_at").notNull(),
  },
  (t) => [primaryKey({ columns: [t.collectionId, t.referenceId] })],
);
export const settings = sqliteTable("settings", {
  id: text("id").primaryKey(),
  value: text("value").notNull(),
});
export const collectionMedia = sqliteTable(
  "collection_media",
  {
    collectionId: text("collection_id")
      .notNull()
      .references(() => collections.id, { onDelete: "cascade" }),
    referenceId: text("reference_id").notNull(),
    mediaId: text("media_id").notNull(),
    addedAt: integer("added_at").notNull(),
  },
  (t) => [primaryKey({ columns: [t.collectionId, t.referenceId, t.mediaId] })],
);

export const taxonomySnapshots = sqliteTable("taxonomy_snapshots", {
  source: text("source").primaryKey(),
  capturedAt: text("captured_at").notNull(),
  coverage: text("coverage").notNull(),
  position: integer("position").notNull(),
});
export const taxonomyGroups = sqliteTable("taxonomy_groups", {
  id: text("id").primaryKey(),
  label: text("label").notNull(),
  kind: text("kind", { enum: ["taxonomy", "search-preset"] }).notNull(),
  appliesTo: text("applies_to").notNull(),
  sourceUrl: text("source_url").notNull(),
  coverage: text("coverage").notNull(),
  snapshotSource: text("snapshot_source")
    .notNull()
    .references(() => taxonomySnapshots.source),
  position: integer("position").notNull(),
});
export const taxonomyTerms = sqliteTable("taxonomy_terms", {
  id: text("id").primaryKey(),
  groupId: text("group_id")
    .notNull()
    .references(() => taxonomyGroups.id, { onDelete: "cascade" }),
  label: text("label").notNull(),
  sourceUrl: text("source_url"),
  subgroup: text("subgroup"),
  sourceIds: text("source_ids"),
  position: integer("position").notNull(),
});
export const referenceCategories = sqliteTable(
  "reference_categories",
  {
    referenceId: text("reference_id").notNull(),
    termId: text("term_id")
      .notNull()
      .references(() => taxonomyTerms.id, { onDelete: "cascade" }),
    reason: text("reason").notNull().default(""),
    origin: text("origin", { enum: ["curated", "manual"] }).notNull(),
  },
  (table) => [primaryKey({ columns: [table.referenceId, table.termId] })],
);

export const mediaTermAssignments = sqliteTable(
  "media_term_assignments",
  {
    referenceId: text("reference_id").notNull(),
    mediaId: text("media_id").notNull(),
    termId: text("term_id")
      .notNull()
      .references(() => taxonomyTerms.id, { onDelete: "cascade" }),
    reason: text("reason").notNull().default(""),
    origin: text("origin", { enum: ["curated", "manual"] }).notNull(),
  },
  (table) => [
    primaryKey({ columns: [table.referenceId, table.mediaId, table.termId] }),
  ],
);
