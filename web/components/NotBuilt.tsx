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
