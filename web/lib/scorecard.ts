/**
 * Data layer for the scorecard pages: the TypeScript port of the data logic in
 * tools/scorecard.py. Every function below is pure and returns typed data;
 * rendering is the caller's job, so nothing here produces HTML.
 *
 * The rubric is scorecard/criteria.json and each audit is one dated snapshot,
 * scorecard/audits/<YYYY-MM-DD>.json (a `-N` suffix marks run N of that day). A
 * criterion's `doneWhen` is its web wording; `platforms` may give mobile or
 * desktop wording, and a platform a criterion does not list uses `doneWhen`.
 * Each package is graded against the wording for its catalog `platform`. The
 * newest snapshot drives the scorecard; older ones feed the changelog.
 *
 * node:fs and node:path only, no dependencies.
 */
import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { basename, dirname, join } from 'node:path';

/** The repo root: process.cwd(), or its parent when the cwd is `web/` itself. */
export const ROOT =
  basename(process.cwd()) === 'web' ? dirname(process.cwd()) : process.cwd();

const DATA = join(ROOT, 'scorecard');

export type GradeValue = 'meets' | 'partly' | 'missing' | 'na';

export interface Grade {
  grade: GradeValue;
  evidence: string;
}

export interface Criterion {
  id: string;
  /** The layer's name (a value of `Criteria.layers`), not its letter. */
  layer: string;
  title: string;
  /** The web wording, and the default for platforms without their own. */
  doneWhen: string;
  /** Per-platform wording overrides; `web` is not allowed here (that is `doneWhen`). */
  platforms?: Record<string, string>;
  /** Why the criterion is optional for a capture; absent means mandatory. */
  optional?: string;
}

export interface Criteria {
  version: string;
  /** Layer letter -> layer name, in display order. */
  layers: Record<string, string>;
  criteria: Criterion[];
}

export interface AuditSystem {
  slug: string;
  name: string;
  short?: string;
  category: string;
  goodFor: string;
  url: string;
  captured: string;
  themes: string[];
  grades: Record<string, Grade>;
  platform?: string;
  reviewedPlatform?: string;
  reviewed?: string;
}

export interface Audit {
  date: string;
  rubric?: string;
  method: string;
  systems: AuditSystem[];
  base?: string;
  reviewMethod?: string;
  /** Which run of `date` this snapshot is (`2026-10-16-2.json` is 2); set by load(). */
  seq: number;
}

/** Grade value -> display glyph and word, in legend order. */
export const GRADES: Record<GradeValue, { glyph: string; word: string }> = {
  meets: { glyph: '●', word: 'Meets' },
  partly: { glyph: '◐', word: 'Partly' },
  missing: { glyph: '○', word: 'Missing' },
  na: { glyph: '–', word: 'Not applicable' },
};

/**
 * The platform a snapshot entry without one was graded as: before rubric 3 every
 * criterion had one wording, the web one.
 */
export const BASE_PLATFORM = 'web';

/** Every platform a criterion can carry wording for, in display order. */
export const PLATFORMS = ['web', 'mobile', 'desktop'] as const;

/** `2026-10-16.json` is run 1 of that day, `2026-10-16-2.json` run 2. */
export function seq(filename: string): number {
  const stem = basename(filename).replace(/\.[^.]*$/, '');
  const tail = stem.slice('YYYY-MM-DD'.length).replace(/^-+/, '');
  return /^\d+$/.test(tail) ? parseInt(tail, 10) : 1;
}

export function auditTitle(audit: Audit): string {
  if (audit.base) {
    return `${audit.date}, scripted re-grade of the ${audit.base} review`;
  }
  return audit.date;
}

export function platformOf(system: AuditSystem): string {
  return system.platform ?? BASE_PLATFORM;
}

/**
 * The criterion's done-when rule for a platform: its own wording when the
 * criterion lists one, else `doneWhen`, which is the web wording and the
 * default for the rest.
 */
export function doneWhen(criterion: Criterion, platform: string): string {
  return criterion.platforms?.[platform] ?? criterion.doneWhen;
}

export interface Wording {
  platforms: string[];
  text: string;
}

/** Every platform's wording, platforms that share one grouped, in PLATFORMS order. */
export function wordings(criterion: Criterion): Wording[] {
  const out: Wording[] = [];
  for (const platform of PLATFORMS) {
    const text = doneWhen(criterion, platform);
    const same = out.find((group) => group.text === text);
    if (same) {
      same.platforms.push(platform);
    } else {
      out.push({ platforms: [platform], text });
    }
  }
  return out;
}

/** `["mobile", "desktop"]` reads "Mobile and desktop". */
export function platformLabel(platforms: string[]): string {
  const text = platforms.join(' and ');
  return text.charAt(0).toUpperCase() + text.slice(1);
}

/**
 * Read the rubric and every audit snapshot, sorted by (date, seq) so the newest
 * run of a day sorts after the earlier ones. Throws when scorecard/audits/ is
 * missing or holds no snapshots, mirroring the Python's sys.exit.
 */
export function load(): { criteria: Criteria; audits: Audit[] } {
  const criteria = JSON.parse(
    readFileSync(join(DATA, 'criteria.json'), 'utf8'),
  ) as Criteria;
  const dir = join(DATA, 'audits');
  const names = existsSync(dir)
    ? readdirSync(dir).filter((name) => name.endsWith('.json'))
    : [];
  const audits = names
    .map((name): Audit => {
      const audit = JSON.parse(readFileSync(join(dir, name), 'utf8')) as Audit;
      audit.seq = seq(name);
      return audit;
    })
    .sort((a, b) =>
      a.date === b.date ? a.seq - b.seq : a.date < b.date ? -1 : 1,
    );
  if (!audits.length) {
    throw new Error('no audit snapshots in scorecard/audits/');
  }
  return { criteria, audits };
}

/** Every validation problem in the rubric and audit data, as readable strings. */
export function check(criteria: Criteria, audits: Audit[]): string[] {
  const ids = criteria.criteria.map((c) => c.id);
  const problems: string[] = [];
  for (const c of criteria.criteria) {
    // Web wording is `doneWhen`; a `platforms.web` would be a second copy that could drift.
    const wrong = Object.keys(c.platforms ?? {}).filter(
      (p) => !(PLATFORMS as readonly string[]).includes(p) || p === BASE_PLATFORM,
    );
    if (wrong.length) {
      problems.push(
        `criteria ${c.id}: platforms has ${wrong.join(', ')}; ` +
          `list only ${PLATFORMS.filter((p) => p !== BASE_PLATFORM).join(', ')}`,
      );
    }
  }
  for (const audit of audits) {
    const systems: unknown = audit.systems;
    if (!Array.isArray(systems)) {
      problems.push(
        `${audit.date ?? '?'}: systems must be a list of graded packages`,
      );
      continue;
    }
    const slugs = systems
      .filter((s): s is Record<string, unknown> => isRecord(s) && typeof s.slug === 'string')
      .map((s) => s.slug as string);
    const tally = new Map<string, number>();
    for (const slug of slugs) tally.set(slug, (tally.get(slug) ?? 0) + 1);
    const dupes = [...new Set(slugs.filter((s) => (tally.get(s) ?? 0) > 1))].sort();
    for (const slug of dupes) {
      problems.push(
        `${audit.date}: slug ${pyRepr(slug)} appears ${tally.get(slug)} times; ` +
          'each page needs its own',
      );
    }
    for (const s of systems) {
      if (!isRecord(s) || typeof s.slug !== 'string' || !s.slug) {
        problems.push(`${audit.date}: a systems entry is not an object with a slug`);
        continue;
      }
      const slug = s.slug;
      // Python's platform_of reads the key whenever it is present, so a JSON
      // `null` platform is reported too, never silently defaulted to web.
      if ('platform' in s && !(PLATFORMS as readonly unknown[]).includes(s.platform)) {
        problems.push(`${audit.date} ${slug}: unknown platform ${pyRepr(s.platform)}`);
      }
      const grades: unknown = s.grades;
      if (!isRecord(grades)) {
        problems.push(
          `${audit.date} ${slug}: grades must be an object of ` +
            'criterion -> {"grade", "evidence"}',
        );
        continue;
      }
      const missing = ids.filter((id) => !Object.hasOwn(grades, id));
      if (missing.length) {
        problems.push(`${audit.date} ${slug}: missing ${missing.join(', ')}`);
      }
      const unknown = Object.keys(grades).filter((id) => !ids.includes(id));
      if (unknown.length) {
        problems.push(
          `${audit.date} ${slug}: grades for criteria not in the rubric: ${unknown.join(', ')}`,
        );
      }
      for (const [cid, g] of Object.entries(grades)) {
        if (!isRecord(g)) {
          problems.push(
            `${audit.date} ${slug} ${cid}: a grade must be ` +
              '{"grade": ..., "evidence": ...}',
          );
          continue;
        }
        if (typeof g.grade !== 'string' || !Object.hasOwn(GRADES, g.grade)) {
          problems.push(`${audit.date} ${slug} ${cid}: unknown grade ${pyRepr(g.grade)}`);
        }
        if (typeof g.evidence !== 'string') {
          problems.push(
            `${audit.date} ${slug} ${cid}: every grade needs an "evidence" ` +
              'string saying what backs it',
          );
        }
      }
    }
  }
  return problems;
}

export function short(system: AuditSystem): string {
  return system.short || system.name;
}

export function counts(system: AuditSystem): Record<GradeValue, number> {
  const out: Record<GradeValue, number> = { meets: 0, partly: 0, missing: 0, na: 0 };
  for (const g of Object.values(system.grades)) {
    out[g.grade] += 1;
  }
  return out;
}

/** Systems sorted best first: most meets, then most partly, then name. */
export function ranked(systems: AuditSystem[]): AuditSystem[] {
  return [...systems].sort(
    (a, b) =>
      counts(b).meets - counts(a).meets ||
      counts(b).partly - counts(a).partly ||
      (a.name < b.name ? -1 : a.name > b.name ? 1 : 0),
  );
}

export interface ChangelogEntry {
  /** auditTitle(): the date, plus the base review on scripted re-grades. */
  title: string;
  /**
   * The diff lines against the previous audit, or null when nothing changed
   * (the caller renders "No grade changed."). On the first audit `first` is
   * true and `lines` holds the first-audit summary line instead of a diff.
   */
  lines: string[] | null;
  first: boolean;
}

/**
 * One entry per audit, newest first, each diffed against the one before it:
 * rubric version change, systems added, per-criterion grade changes
 * ("F1 Colour ramps partly → meets"), platform changes, and removals.
 */
export function changelog(criteria: Criteria, audits: Audit[]): ChangelogEntry[] {
  const titles = new Map(criteria.criteria.map((c) => [c.id, c.title]));
  const entries: ChangelogEntry[] = [];
  for (let i = audits.length - 1; i >= 0; i--) {
    const audit = audits[i];
    if (i === 0) {
      entries.push({
        title: auditTitle(audit),
        first: true,
        lines: [
          `First audit: ${audit.systems.length} systems against ` +
            `${criteria.criteria.length} criteria.`,
        ],
      });
      continue;
    }
    const before = new Map(audits[i - 1].systems.map((s) => [s.slug, s]));
    const lines: string[] = [];
    const oldRubric = audits[i - 1].rubric;
    const newRubric = audit.rubric;
    if (oldRubric && newRubric && oldRubric !== newRubric) {
      lines.push(
        `Rubric changed from version ${oldRubric} to ${newRubric} ` +
          '(criteria and method).',
      );
    }
    for (const s of ranked(audit.systems)) {
      const old = before.get(s.slug);
      if (!old) {
        lines.push(`${s.name} added: ${counts(s).meets} criteria met.`);
        continue;
      }
      const changed: string[] = [];
      for (const [cid, g] of Object.entries(s.grades)) {
        const oldGrade = old.grades[cid];
        if (oldGrade && oldGrade.grade !== g.grade) {
          changed.push(
            `${cid} ${titles.get(cid) ?? cid} ` +
              `${GRADES[oldGrade.grade].word.toLowerCase()} → ` +
              GRADES[g.grade].word.toLowerCase(),
          );
        }
      }
      if (old.platform !== undefined && platformOf(old) !== platformOf(s)) {
        changed.unshift(`platform ${platformOf(old)} → ${platformOf(s)}`);
      }
      if (changed.length) {
        lines.push(`${s.name}: ${changed.join('; ')}.`);
      }
    }
    // The Python iterates a dict-key set difference, whose order is CPython's;
    // document order of the previous audit is the deterministic equivalent.
    const current = new Set(audit.systems.map((s) => s.slug));
    for (const [slug, s] of before) {
      if (!current.has(slug)) {
        lines.push(`${s.name} removed.`);
      }
    }
    entries.push({ title: auditTitle(audit), first: false, lines: lines.length ? lines : null });
  }
  return entries;
}

export interface IndexStats {
  systemCount: number;
  /** systemCount × number of criteria. */
  totalCells: number;
  /** Grades that fully meet their criterion, across every system. */
  meets: number;
  /** `round(100 * meets / totalCells)`, with Python's round-half-to-even. */
  pct: number;
  /** The top-ranked system; `name` is its short name. */
  leader: { name: string; slug: string; meets: number };
  /** The criteria met by the fewest systems, in rubric order. */
  weakest: { id: string; title: string }[];
  /** How many systems meet each weakest criterion. */
  floor: number;
}

/** The numbers behind the index page's stat cards. */
export function indexStats(criteria: Criteria, audit: Audit): IndexStats {
  const systems = ranked(audit.systems);
  const totalCells = systems.length * criteria.criteria.length;
  const meets = systems.reduce((sum, s) => sum + counts(s).meets, 0);
  const best = systems[0];
  const byCriterion = new Map(
    criteria.criteria.map((c) => [
      c.id,
      systems.filter((s) => s.grades[c.id].grade === 'meets').length,
    ]),
  );
  const floor = Math.min(...byCriterion.values());
  const weakest = criteria.criteria
    .filter((c) => byCriterion.get(c.id) === floor)
    .map((c) => ({ id: c.id, title: c.title }));
  return {
    systemCount: systems.length,
    totalCells,
    meets,
    pct: roundHalfEven((100 * meets) / totalCells),
    leader: { name: short(best), slug: best.slug, meets: counts(best).meets },
    weakest,
    floor,
  };
}

export interface ReportRow {
  id: string;
  title: string;
  /** The criterion's done-when rule for this system's platform. */
  doneWhen: string;
  grade: GradeValue;
  evidence: string;
}

export interface ReportLayer {
  name: string;
  rows: ReportRow[];
}

export interface SystemReport {
  /** 1-based position in the ranked table. */
  rank: number;
  /** Total systems in the audit. */
  total: number;
  counts: Record<GradeValue, number>;
  platform: string;
  /** The platform the stored grades were reviewed against (`reviewedPlatform`, else `platform`). */
  wasPlatform: string;
  layers: ReportLayer[];
}

/** One system's page: rank and counts, then every criterion grouped by layer. */
export function systemReport(
  criteria: Criteria,
  audit: Audit,
  slug: string,
): SystemReport {
  const systems = ranked(audit.systems);
  const index = systems.findIndex((s) => s.slug === slug);
  if (index === -1) {
    throw new Error(`no system named ${pyRepr(slug)} in the ${audit.date} audit`);
  }
  const system = systems[index];
  const platform = platformOf(system);
  const layers = Object.values(criteria.layers).map((name) => ({
    name,
    rows: criteria.criteria
      .filter((c) => c.layer === name)
      .map((c) => {
        const g = system.grades[c.id];
        return {
          id: c.id,
          title: c.title,
          doneWhen: doneWhen(c, platform),
          grade: g.grade,
          evidence: g.evidence,
        };
      }),
  }));
  return {
    rank: index + 1,
    total: audit.systems.length,
    counts: counts(system),
    platform,
    wasPlatform: system.reviewedPlatform ?? platform,
    layers,
  };
}

/** Python's isinstance(x, dict): a plain object, not an array, not null. */
function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

/** Python's repr() for the values that can appear in check() messages. */
function pyRepr(value: unknown): string {
  if (value === null || value === undefined) return 'None';
  if (value === true) return 'True';
  if (value === false) return 'False';
  if (typeof value === 'string') {
    const escaped = value
      .replace(/\\/g, '\\\\')
      .replace(/\n/g, '\\n')
      .replace(/\r/g, '\\r')
      .replace(/\t/g, '\\t');
    if (!escaped.includes("'")) return `'${escaped}'`;
    if (!escaped.includes('"')) return `"${escaped}"`;
    return `'${escaped.replace(/'/g, "\\'")}'`;
  }
  return String(value);
}

/** Python's round(): nearest integer, ties to even (JS Math.round is ties up). */
function roundHalfEven(x: number): number {
  const floor = Math.floor(x);
  const diff = x - floor;
  if (diff < 0.5) return floor;
  if (diff > 0.5) return floor + 1;
  return floor % 2 === 0 ? floor : floor + 1;
}
