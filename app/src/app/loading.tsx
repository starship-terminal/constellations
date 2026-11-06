import { Mark } from "@/components/shell";
export default function Loading() {
  return (
    <div className="boot" role="status">
      <div className="boot-mark" aria-hidden="true">
        <Mark />
      </div>
      <span className="boot-track" aria-hidden="true">
        <span />
      </span>
      <p className="boot-label">Opening your workspace…</p>
    </div>
  );
}
