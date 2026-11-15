-- refero.db schema, written by tools/refero/dump.py from the db.
-- Generated: never edit by hand. `make refero-db` rebuilds the
-- db from this folder; `make refero-dump` rewrites it.
PRAGMA page_size=4096;
PRAGMA auto_vacuum=0;
PRAGMA encoding='UTF-8';
PRAGMA journal_mode='delete';
PRAGMA user_version=0;
PRAGMA application_id=0;

CREATE TABLE styles (
  uuid TEXT PRIMARY KEY,
  slug TEXT UNIQUE,
  name TEXT,
  tagline TEXT,
  page_url TEXT NOT NULL,
  source_url TEXT,
  theme TEXT,
  extracted_at TEXT,
  fetched_at TEXT NOT NULL,
  design_md TEXT,
  variables_css TEXT,
  theme_css TEXT,
  tokens_json TEXT,
  design_system_json TEXT,
  prompt_txt TEXT,
  result_json TEXT,
  screenshot_url TEXT
, video_url TEXT, video_poster_url TEXT, video_detail_url TEXT, video_detail_poster_url TEXT, media_fetched_at TEXT, product_type TEXT, design_style TEXT, tags TEXT, components_json TEXT, components_at TEXT);

CREATE TABLE fetch_errors (
  uuid TEXT PRIMARY KEY,
  page_url TEXT,
  error TEXT,
  at TEXT NOT NULL
);

CREATE TABLE collections (
  slug TEXT PRIMARY KEY,
  url TEXT,
  title TEXT,
  description TEXT
);

CREATE TABLE collection_styles (
  collection_slug TEXT,
  section TEXT,
  rank INTEGER,
  style_uuid TEXT
);

CREATE TABLE similar (
            uuid TEXT, business TEXT, why TEXT, rank INTEGER,
            matched_slug TEXT);

CREATE TABLE screens (
  entry_type TEXT,     -- 'ios' or 'web'
  entry_id INTEGER,    -- upstream numeric id
  entry_key TEXT,      -- domain for web, App Store numeric id for iOS
  shot_uuid TEXT,
  shot_url TEXT,       -- first url of the record's url field (web full pages
                       -- are multi-part arrays; the rest share the prefix)
  thumb_url TEXT,
  page_url TEXT,       -- exact captured URL, NULL for iOS screens
  page_id INTEGER,
  colors_json TEXT,    -- extracted 5-swatch RGB palette
  patterns_json TEXT,  -- NULL until a tag pass fills it
  elements_json TEXT,  -- NULL until a tag pass fills it
  shot_created_at TEXT,
  fetched_at TEXT
);
