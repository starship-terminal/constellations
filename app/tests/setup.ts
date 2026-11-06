import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll } from "vitest";

// Source reads now hydrate app-owned classification from SQLite. Never migrate
// or inspect the developer's personal database while running tests.
const dataDirectory = mkdtempSync(join(tmpdir(), "studio-test-state-"));
process.env.DESIGN_RESEARCH_DATA_DIR = dataDirectory;
afterAll(() => rmSync(dataDirectory, { recursive: true, force: true }));
