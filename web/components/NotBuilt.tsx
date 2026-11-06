// Shown in place of a listing when web/data has not been generated yet,
// so a fresh checkout explains itself instead of throwing.
export function NotBuilt({ what = "The catalog" }: { what?: string }) {
  return (
    <div className="page">
      <p className="empty">
        {what} is not built yet: run <code>make build</code> in the repo.
      </p>
    </div>
  );
}

/** True when a data load failed because web/data is absent, the one failure
    NotBuilt explains; anything else should reach the error page and logs. */
export const isNotBuilt = (e: unknown): boolean =>
  !!e && typeof e === "object" && (e as { code?: unknown }).code === "ENOENT";
